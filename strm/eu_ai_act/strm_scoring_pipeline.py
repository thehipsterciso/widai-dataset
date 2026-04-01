#!/usr/bin/env python3
"""
WIDAI STRM-005 Scoring Pipeline — EU AI Act
============================================
EU AI Act (Regulation (EU) 2024/1689) → WIDAI KSA Pool mappings.

METHODOLOGY:
The EU AI Act is a regulation, not a workforce framework. Its elements fall into
two distinct categories:

  Competency elements (8): Articles that explicitly state workforce competency
    requirements (e.g., Art. 4 AI literacy).

  Obligation elements (54): Legal obligations whose fulfillment requires
    identifiable workforce competencies. Each obligation has a
    competency_implication field — the workforce competency interpretation
    of the legal requirement.

SCORING METHOD:
Cross-Encoder STS is the primary scoring method for ALL elements. This is
consistent with STRM-001 through STRM-004.

The competency_implication field bridges the vocabulary gap between legal
prose and competency language. Since the scoring text is competency-language
for both element types, STS appropriately measures semantic similarity.

EMPIRICAL VALIDATION:
NLI entailment was initially planned as primary for obligation elements
(ADR-019 documents this decision and its reversal). Diagnostic scoring of all
54 obligation elements showed NLI entailment mean=0.007, median=0.001 — the
NLI model classifies competency→competency pairs as "neutral" (related but
neither logically implies the other), producing near-zero signal. STS on the
same pairs: mean=0.635, range 0.358–0.824 — well-distributed, actionable
signal consistent with prior STRMs.

RATIONALE TYPE:
Functional (per NIST IR 8477 Section 4.3) — "how similar are the results of
executing the two concepts." Semantic rationale is inappropriate because the
mapping direction is obligation→competency (what workforce capability is needed
to fulfill this legal requirement?), not competency↔competency.

DUAL PROVENANCE:
Each rationale file preserves both the original obligation_text (faithful to
the regulation) and the competency_implication (workforce interpretation used
for scoring). This maintains full provenance for both the regulatory source
and the analytical interpretation.

See ADR-019 for full methodology documentation.
"""

import json
import os
import sys
import re
import math
import glob
from datetime import date

import numpy as np
from sentence_transformers import CrossEncoder, SentenceTransformer, util
from bert_score import score as bertscore_fn

# ── Configuration ──
REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
STRM_DIR = os.path.dirname(os.path.abspath(__file__))
ELEMENTS_FILE = os.path.join(REPO_ROOT, "sources/eu_ai_act/eu_ai_act_elements.json")
KSA_DIR = os.path.join(REPO_ROOT, "ksas")
MAPPING_FILE = os.path.join(STRM_DIR, "strm_mapping.json")
RATIONALE_DIR = os.path.join(STRM_DIR, "rationale")
SCORING_SUMMARY_FILE = os.path.join(STRM_DIR, "scoring_summary.json")
CANDIDATES_FILE = os.path.join(REPO_ROOT, "sources/eu_ai_act/eu_ai_act_candidates.json")

TODAY = date.today().isoformat()

STOPWORDS = {
    'a', 'an', 'the', 'and', 'or', 'of', 'to', 'in', 'for', 'with',
    'on', 'at', 'by', 'from', 'as', 'is', 'are', 'was', 'were', 'be',
    'been', 'being', 'have', 'has', 'had', 'do', 'does', 'did', 'will',
    'would', 'could', 'should', 'may', 'might', 'shall', 'can', 'that',
    'this', 'these', 'those', 'it', 'its', 'their', 'them', 'they',
    'which', 'who', 'whom', 'what', 'where', 'when', 'how', 'not',
    'no', 'nor', 'but', 'if', 'then', 'than', 'so', 'such', 'both',
    'each', 'all', 'any', 'into', 'through', 'during', 'before',
    'after', 'above', 'below', 'between', 'other', 'about', 'up',
    'out', 'over', 'under', 'also', 'including', 'e', 'g', 'you',
    'your', 'using', 'use', 'used', 'able', 'know', 'like', 'make',
    'need', 'new', 'work', 'working'
}


# ── Load Data ──

def load_eu_ai_act_elements():
    """Load EU AI Act elements from extracted JSON.

    Returns list of element dicts. The scoring text is competency_implication
    (the workforce competency interpretation), not obligation_text (the raw
    regulatory language). Both are preserved in rationale files for provenance.
    """
    with open(ELEMENTS_FILE) as f:
        data = json.load(f)
    return data["elements"], data["statistics"]


def load_widai_ksas():
    """Load all WIDAI KSAs from domain files."""
    all_ksas = []
    for fp in sorted(glob.glob(os.path.join(KSA_DIR, "*_ksas.json"))):
        with open(fp) as f:
            data = json.load(f)
        for item in data["ksas"]:
            all_ksas.append({
                "id": item["ksa_id"],
                "type": item["type"],
                "statement": item["statement"],
                "domain": item["domain_code"]
            })
    return all_ksas


# ── Text Analysis Utilities ──

def tokenize(text):
    """Lowercased word tokens as a set."""
    return set(re.findall(r'\b\w+\b', text.lower()))


def substantive_tokens(tokens):
    """Filter stopwords, return sorted substantive tokens."""
    return sorted(tokens - STOPWORDS)


def jaccard_similarity(text_a, text_b):
    """Token-level Jaccard similarity."""
    tokens_a = tokenize(text_a)
    tokens_b = tokenize(text_b)
    if not tokens_a or not tokens_b:
        return 0.0
    return len(tokens_a & tokens_b) / len(tokens_a | tokens_b)


def softmax(logits):
    """Convert raw logits to probabilities."""
    exp_logits = [math.exp(x) for x in logits]
    total = sum(exp_logits)
    return [x / total for x in exp_logits]


def get_text_analysis(fde_text, ksa_text):
    """Compute shared/unique tokens and concept bridges for a pair."""
    fde_tok = tokenize(fde_text)
    ksa_tok = tokenize(ksa_text)
    shared = sorted(fde_tok & ksa_tok)
    shared_sub = sorted(set(shared) - STOPWORDS)
    fde_only = sorted((fde_tok - ksa_tok) - STOPWORDS)
    ksa_only = sorted((ksa_tok - fde_tok) - STOPWORDS)
    fde_words = len(fde_text.split())
    ksa_words = len(ksa_text.split())
    return {
        "shared": shared,
        "shared_sub": shared_sub,
        "fde_only": fde_only,
        "ksa_only": ksa_only,
        "fde_words": fde_words,
        "ksa_words": ksa_words,
    }


# ── Classification Logic ──

def classify_element(cosine_score, sts_raw, element_type):
    """Classify any element using STS as primary signal.

    STS is the primary scoring method for all elements because the scoring
    text (competency_implication) is competency-language for both element types.

    Classification thresholds are consistent with STRM-001 through STRM-004.
    """
    if sts_raw >= 0.65:
        return "Equal"
    if sts_raw >= 0.50:
        return "Superset of"
    if sts_raw >= 0.30:
        return "Intersects with"
    if cosine_score >= 0.35:
        return "Intersects with"
    return "No relationship"


# ── Significance Generators ──

def sig_sts(sts_raw, strength, ta, fde_text, ksa_text, element_type):
    """STS significance — primary method for all elements."""
    label = "competency requirement" if element_type == "competency" else "competency implication"
    parts = [f"STS {strength}/10 (raw {sts_raw:.3f})."]
    if ta["shared_sub"]:
        parts.append(f"Shared vocabulary: [{', '.join(ta['shared_sub'][:10])}].")
    else:
        parts.append("No substantive shared vocabulary — relationship is purely semantic.")
    if ta["fde_only"] and ta["ksa_only"]:
        parts.append(
            f"EU AI Act {label} terms [{', '.join(ta['fde_only'][:6])}] "
            f"vs WIDAI terms [{', '.join(ta['ksa_only'][:6])}] "
            f"define the semantic distance."
        )
    return " ".join(parts)


def sig_bertscore(p, r, f1, ta, element_type):
    """BERTScore significance."""
    parts = [f"BERTScore F1={f1:.3f} (P={p:.3f}, R={r:.3f})."]
    fw = ta["fde_words"]
    kw = ta["ksa_words"]
    label = "competency implication" if element_type == "obligation" else "EU AI Act competency"
    if abs(p - r) < 0.02:
        parts.append(
            f"Balanced P/R — the {fw}-word {label} and "
            f"{kw}-word WIDAI KSA cover each other's token-level "
            f"semantic content symmetrically."
        )
    elif p > r:
        parts.append(
            f"P exceeds R by {p - r:.3f} — the {label}'s {fw} words "
            f"are well-captured by the WIDAI KSA's {kw} words, "
            f"but the KSA contains additional specificity."
        )
    else:
        parts.append(
            f"R exceeds P by {r - p:.3f} — the WIDAI KSA's {kw} words "
            f"are well-captured by the {label}'s {fw} words, "
            f"but the {label} contains broader scope."
        )
    return " ".join(parts)


def sig_nli(nli, fde_text, ksa_text, relationship, element_type):
    """NLI significance — secondary method for all elements.

    Note: NLI entailment is systematically low for competency→competency pairs
    (mean ~0.007 for obligation elements, ~0.009 for competency elements).
    This is expected: NLI measures strict logical implication, not semantic
    relatedness. Two overlapping competency statements are typically "neutral"
    in NLI terms. The NLI signal's value is in detecting contradiction
    (competency domain conflicts) rather than confirming relationships.
    """
    c, e, n = nli["contradiction"], nli["entailment"], nli["neutral"]
    fde_short = fde_text[:80].rstrip()
    ksa_short = ksa_text[:80].rstrip()

    if c > 0.5:
        return (
            f"NLI: contradiction-dominant ({c:.1%}). "
            f"Semantic tension between \"{fde_short}\" and "
            f"\"{ksa_short}\". Despite STS-based '{relationship}' "
            f"classification, these concepts may operate in adjacent "
            f"but distinct professional domains."
        )
    elif e > 0.2:
        return (
            f"NLI: notable entailment ({e:.1%}). "
            f"\"{fde_short}\" shows logical implication toward "
            f"\"{ksa_short}\" — stronger than typical for cross-framework "
            f"competency pairs, reinforcing the STS-based relationship."
        )
    elif n > 0.8:
        return (
            f"NLI: neutral-dominant ({n:.1%}). "
            f"Standard result for cross-framework competency mapping — "
            f"the EU AI Act element and WIDAI KSA describe overlapping "
            f"competencies without strict logical implication."
        )
    else:
        return (
            f"NLI: mixed signal (E:{e:.1%}, N:{n:.1%}, C:{c:.1%}). "
            f"No dominant NLI classification — the logical relationship "
            f"between the regulatory requirement and WIDAI KSA is ambiguous."
        )


def sig_biencoder(bienc, sts_raw, ta):
    """Bi-encoder significance."""
    gap = bienc - sts_raw
    abs_gap = abs(gap)
    shared_str = ', '.join(ta['shared_sub'][:5]) if ta['shared_sub'] else 'none'

    if abs_gap < 0.05:
        return (
            f"Bi-encoder {bienc:.3f} ≈ STS {sts_raw:.3f} (gap {abs_gap:.3f}). "
            f"Independent encoding and cross-attention agree. "
            f"Shared terms [{shared_str}] are sufficient for "
            f"independent encoding to detect the match."
        )
    elif gap > 0:
        return (
            f"Bi-encoder {bienc:.3f} > STS {sts_raw:.3f} (gap +{gap:.3f}). "
            f"Independent encoding finds more similarity than cross-attention. "
            f"Shared surface terms [{shared_str}] inflate the bi-encoder, "
            f"but cross-attention detects semantic divergence beneath "
            f"the vocabulary overlap."
        )
    else:
        return (
            f"Bi-encoder {bienc:.3f} < STS {sts_raw:.3f} (gap {gap:.3f}). "
            f"Cross-attention finds deeper alignment than independent encoding. "
            f"The relationship depends on cross-text reasoning between "
            f"[{', '.join(ta['fde_only'][:3])}] and [{', '.join(ta['ksa_only'][:3])}] "
            f"that bi-encoders structurally cannot capture."
        )


def sig_jaccard(jaccard, ta, element_type):
    """Jaccard significance."""
    if not ta["shared_sub"]:
        return (
            f"Jaccard {jaccard:.1%}. Zero substantive shared tokens. "
            f"The entire relationship is semantic — no lexical trace. "
            f"EU AI Act terms: [{', '.join(ta['fde_only'][:6])}]. "
            f"WIDAI terms: [{', '.join(ta['ksa_only'][:6])}]."
        )
    return (
        f"Jaccard {jaccard:.1%}. "
        f"Shared tokens: [{', '.join(ta['shared_sub'])}]. "
        f"EU AI Act-only: [{', '.join(ta['fde_only'][:6])}]. "
        f"WIDAI-only: [{', '.join(ta['ksa_only'][:6])}]."
    )


# ── Scoring ──

def score_pair(fde_text, ksa_text, sts_model, nli_model, bienc_model):
    """Score a single FDE-KSA pair with all methods except BERTScore (batched)."""
    sts_raw = float(sts_model.predict([(fde_text, ksa_text)])[0])
    sts_strength = round(sts_raw * 10, 2)

    nli_logits = nli_model.predict([(fde_text, ksa_text)])[0]
    probs = softmax([float(x) for x in nli_logits])
    nli_result = {
        "contradiction": round(probs[0], 4),
        "entailment": round(probs[1], 4),
        "neutral": round(probs[2], 4)
    }

    emb_fde = bienc_model.encode(fde_text, convert_to_tensor=True)
    emb_ksa = bienc_model.encode(ksa_text, convert_to_tensor=True)
    bienc_cosine = float(util.cos_sim(emb_fde, emb_ksa)[0][0])

    jaccard = jaccard_similarity(fde_text, ksa_text)

    return {
        "sts_raw_0_1": round(sts_raw, 4),
        "sts_strength_0_10": round(sts_strength, 1),
        "nli": nli_result,
        "biencoder_cosine_0_1": round(bienc_cosine, 4),
        "jaccard_token_0_1": round(jaccard, 4)
    }


def build_rationale_file(mapping, scores, bertscore_data, ta, element):
    """Build the per-FDE rationale JSON with content-specific significance.

    STS is primary for all elements. Rationale type is Functional for all
    elements (obligation→competency mapping direction). Dual provenance
    preserved: obligation_text + competency_implication.
    """
    element_type = element["element_type"]
    fde_text = mapping["fde_description"]
    ksa_text = mapping["ref_statement"]
    relationship = mapping["relationship"]
    strength = round(scores["sts_strength_0_10"])

    sts_sig = sig_sts(scores["sts_raw_0_1"], scores["sts_strength_0_10"],
                      ta, fde_text, ksa_text, element_type)
    bs_sig = sig_bertscore(bertscore_data["precision"], bertscore_data["recall"],
                           bertscore_data["f1"], ta, element_type)
    nli_sig = sig_nli(scores["nli"], fde_text, ksa_text, relationship, element_type)
    bienc_sig = sig_biencoder(scores["biencoder_cosine_0_1"], scores["sts_raw_0_1"], ta)
    jac_sig = sig_jaccard(scores["jaccard_token_0_1"], ta, element_type)

    return {
        "strm_id": "STRM-005-EU-AI-ACT",
        "fde_id": mapping["fde_id"],
        "fde_type": element_type,
        "article": element["article"],
        "article_title": element["article_title"],
        "obligation_text": element["obligation_text"],
        "scoring_text": element["competency_implication"],
        "_comment_nist_fields": "Fields below follow IR 8278Ar1 Section 3.2 OLIR template",
        "focal_document_element": mapping["fde_id"],
        "focal_document_element_description": element["competency_implication"],
        "rationale": "Functional",
        "relationship": relationship,
        "reference_document_element": mapping["ref_id"],
        "reference_document_element_description": ksa_text,
        "comments": mapping["notes"],
        "strength_of_relationship": strength,
        "relationship_type": None,
        "relationship_explanation": None,
        "relationship_property": None,
        "_comment_widai_extensions": "Fields below are WIDAI extensions per ADR-014",
        "strength_justification": {
            "methodology": "Multi-method computational scoring (STS-primary, Functional rationale)",
            "primary_method": {
                "name": "Cross-Encoder STS",
                "model": "cross-encoder/stsb-roberta-base",
                "description": (
                    "Semantic Textual Similarity via cross-encoder regression. "
                    "Primary method for all elements. Scores the competency_implication "
                    "text (workforce competency interpretation of the regulatory "
                    "requirement) against WIDAI KSA statements."
                ),
                "raw_score_0_1": scores["sts_raw_0_1"],
                "mapped_strength_0_10": scores["sts_strength_0_10"],
                "final_strength_integer": strength,
                "significance": sts_sig
            },
            "secondary_methods": {
                "bertscore": {
                    "model": "roberta-large",
                    "description": "Token-level contextual embedding matching.",
                    "precision": bertscore_data["precision"],
                    "recall": bertscore_data["recall"],
                    "f1": bertscore_data["f1"],
                    "significance": bs_sig
                },
                "nli_cross_encoder": {
                    "model": "cross-encoder/nli-deberta-v3-base",
                    "description": (
                        "Natural Language Inference classification. NLI entailment is "
                        "systematically low for competency→competency pairs (mean ~0.007) "
                        "because NLI measures strict logical implication, not semantic "
                        "relatedness. Primary diagnostic value is in detecting contradiction."
                    ),
                    "contradiction": scores["nli"]["contradiction"],
                    "entailment": scores["nli"]["entailment"],
                    "neutral": scores["nli"]["neutral"],
                    "significance": nli_sig
                },
                "biencoder_cosine": {
                    "model": "all-MiniLM-L6-v2",
                    "description": "Bi-encoder sentence embeddings with cosine similarity.",
                    "cosine_similarity_0_1": scores["biencoder_cosine_0_1"],
                    "significance": bienc_sig
                },
                "jaccard_token": {
                    "description": "Token-level Jaccard similarity (intersection/union of lowercased word tokens).",
                    "similarity_0_1": scores["jaccard_token_0_1"],
                    "significance": jac_sig
                }
            }
        },
        "regulatory_context": {
            "applies_to": element["applies_to"],
            "risk_category": element["risk_category"],
            "enforcement_date": element["enforcement_date"]
        },
        "gap_signal": None,
        "evaluated_by": "AI-assisted (Claude) with human review",
        "evaluation_date": TODAY
    }


def main():
    # ── Load data ──
    print("Loading EU AI Act elements and WIDAI KSAs...", flush=True)
    elements, stats = load_eu_ai_act_elements()
    widai_ksas = load_widai_ksas()
    competency_elements = [e for e in elements if e["element_type"] == "competency"]
    obligation_elements = [e for e in elements if e["element_type"] == "obligation"]
    print(f"  EU AI Act: {len(elements)} elements "
          f"({len(competency_elements)} competency, {len(obligation_elements)} obligation)", flush=True)
    print(f"  WIDAI: {len(widai_ksas)} KSAs across 12 domains\n", flush=True)

    # ── Load models ──
    print("Loading models...", flush=True)
    print("  [1/4] Cross-Encoder STS (stsb-roberta-base)...", flush=True)
    sts_model = CrossEncoder('cross-encoder/stsb-roberta-base')
    print("  [2/4] Cross-Encoder NLI (nli-deberta-v3-base)...", flush=True)
    nli_model = CrossEncoder('cross-encoder/nli-deberta-v3-base')
    print("  [3/4] Bi-Encoder (all-MiniLM-L6-v2)...", flush=True)
    bienc_model = SentenceTransformer('all-MiniLM-L6-v2')
    print("  [4/4] BERTScore will run in batch after scoring...", flush=True)
    print("Models loaded.\n", flush=True)

    # ── Phase 1: Load pre-computed candidates ──
    print("Phase 1: Loading bi-encoder candidate identifications...", flush=True)
    with open(CANDIDATES_FILE) as f:
        cand_data = json.load(f)
    candidates = {c["element_id"]: c for c in cand_data["candidates"]}
    print(f"  Loaded {len(candidates)} candidate sets.\n", flush=True)

    # ── Phase 2: STS-based classification ──
    print("Phase 2: STS-primary classification for all elements...", flush=True)
    print("  Rationale type: Functional (obligation→competency mapping)\n", flush=True)

    # Build element lookup
    element_lookup = {e["element_id"]: e for e in elements}

    mappings = []
    for element in elements:
        eid = element["element_id"]
        scoring_text = element["competency_implication"]
        etype = element["element_type"]

        cand = candidates[eid]
        best = cand["candidates"][0]
        cosine = best["cosine_similarity"]

        # Pre-score with STS for classification
        sts_raw = float(sts_model.predict([(scoring_text, best["statement"])])[0])

        relationship = classify_element(cosine, sts_raw, etype)

        if relationship == "No relationship":
            mappings.append({
                "fde_id": eid,
                "fde_type": etype,
                "fde_description": scoring_text,
                "article": element["article"],
                "article_title": element["article_title"],
                "relationship": "No relationship",
                "ref_id": None,
                "ref_statement": None,
                "ref_domain": None,
                "rationale": "Functional",
                "notes": (
                    f"EU AI Act {etype} element (Art. {element['article']}) classified as "
                    f"no relationship to WIDAI KSA pool. "
                    f"Best candidate: {best['ksa_id']} ({best['domain_code']}, "
                    f"cosine: {cosine:.3f}, STS: {sts_raw:.3f}). "
                    f"Insufficient semantic overlap with WIDAI workforce competencies."
                ),
                "strength": 0
            })
        else:
            secondaries = [
                f"{c['ksa_id']} ({c['domain_code']}, cosine: {c['cosine_similarity']:.3f})"
                for c in cand["candidates"][1:3]
            ]
            mappings.append({
                "fde_id": eid,
                "fde_type": etype,
                "fde_description": scoring_text,
                "article": element["article"],
                "article_title": element["article_title"],
                "relationship": relationship,
                "ref_id": best["ksa_id"],
                "ref_statement": best["statement"],
                "ref_domain": best["domain_code"],
                "rationale": "Functional",
                "notes": (
                    f"EU AI Act Art. {element['article']} ({etype}) {relationship.lower()} "
                    f"WIDAI {best['domain_code']} domain. "
                    f"{best['ksa_id']} is the strongest match "
                    f"(STS: {sts_raw:.3f}, cosine: {cosine:.3f}). "
                    f"Secondary: {', '.join(secondaries)}."
                ),
                "strength": 0  # Will be filled by scoring
            })

    scored_mappings = [m for m in mappings if m.get("ref_id")]
    norel_mappings = [m for m in mappings if not m.get("ref_id")]
    comp_scored = [m for m in scored_mappings if m["fde_type"] == "competency"]
    obl_scored = [m for m in scored_mappings if m["fde_type"] == "obligation"]
    print(f"  {len(mappings)} total mappings", flush=True)
    print(f"  {len(scored_mappings)} with relationships "
          f"({len(comp_scored)} competency, {len(obl_scored)} obligation)", flush=True)
    print(f"  {len(norel_mappings)} no relationship\n", flush=True)

    # Save initial mapping
    strm_data = {
        "strm_id": "STRM-005-EU-AI-ACT",
        "framework": "EU AI Act (Regulation (EU) 2024/1689)",
        "framework_source": "Official Journal L 2024/1689, EUR-Lex",
        "widai_version": "0.5.6",
        "scoring_methodology": "STS-primary for all elements (consistent with STRM-001–004). Competency_implication field bridges vocabulary gap between legal prose and competency language.",
        "rationale_type": "Functional (per NIST IR 8477 Section 4.3)",
        "total_fdes": len(mappings),
        "competency_fdes": len(competency_elements),
        "obligation_fdes": len(obligation_elements),
        "mapping_date": TODAY,
        "mappings": [
            {k: v for k, v in m.items() if k not in ("article", "article_title")}
            for m in mappings
        ]
    }
    with open(MAPPING_FILE, 'w') as f:
        json.dump(strm_data, f, indent=2)
    print(f"  Initial mapping saved to {MAPPING_FILE}\n", flush=True)

    # ── Phase 3: Full multi-method scoring ──
    print("Phase 3: Full multi-method scoring (STS, NLI, Bi-Encoder, Jaccard)...", flush=True)
    all_scores = {}
    all_text_analysis = {}
    for i, m in enumerate(scored_mappings):
        scores = score_pair(m["fde_description"], m["ref_statement"],
                           sts_model, nli_model, bienc_model)
        all_scores[m["fde_id"]] = scores
        all_text_analysis[m["fde_id"]] = get_text_analysis(m["fde_description"], m["ref_statement"])
        if (i + 1) % 10 == 0 or (i + 1) == len(scored_mappings):
            print(f"  Scored {i+1}/{len(scored_mappings)}", flush=True)
    print(f"  All {len(scored_mappings)} pairs scored.\n", flush=True)

    # ── BERTScore in batch ──
    print("Running BERTScore batch...", flush=True)
    fde_texts = [m["fde_description"] for m in scored_mappings]
    ksa_texts_scored = [m["ref_statement"] for m in scored_mappings]

    P, R, F1 = bertscore_fn(
        cands=fde_texts,
        refs=ksa_texts_scored,
        lang="en",
        verbose=True
    )

    bertscore_data = {}
    for i, m in enumerate(scored_mappings):
        bertscore_data[m["fde_id"]] = {
            "precision": round(float(P[i]), 4),
            "recall": round(float(R[i]), 4),
            "f1": round(float(F1[i]), 4),
        }
    print("BERTScore complete.\n", flush=True)

    # ── Generate rationale files ──
    if os.path.exists(RATIONALE_DIR):
        for f_name in os.listdir(RATIONALE_DIR):
            os.remove(os.path.join(RATIONALE_DIR, f_name))
        print("Cleared existing rationale files.", flush=True)
    os.makedirs(RATIONALE_DIR, exist_ok=True)

    print("Generating per-FDE rationale files...", flush=True)
    strength_values = []

    for m in mappings:
        fde_id = m["fde_id"]
        element = element_lookup[fde_id]
        filename = str(fde_id).replace("/", "-") + ".json"
        filepath = os.path.join(RATIONALE_DIR, filename)

        if m.get("ref_id"):
            scores = all_scores[fde_id]
            bs = bertscore_data[fde_id]
            ta = all_text_analysis[fde_id]
            rationale = build_rationale_file(m, scores, bs, ta, element)
            strength_values.append(rationale["strength_of_relationship"])
        else:
            rationale = {
                "strm_id": "STRM-005-EU-AI-ACT",
                "fde_id": fde_id,
                "fde_type": element["element_type"],
                "article": element["article"],
                "article_title": element["article_title"],
                "obligation_text": element["obligation_text"],
                "scoring_text": element["competency_implication"],
                "_comment_nist_fields": "Fields below follow IR 8278Ar1 Section 3.2 OLIR template",
                "focal_document_element": fde_id,
                "focal_document_element_description": element["competency_implication"],
                "rationale": "Functional",
                "relationship": "No relationship",
                "reference_document_element": None,
                "reference_document_element_description": None,
                "comments": m["notes"],
                "strength_of_relationship": 0,
                "relationship_type": None,
                "relationship_explanation": None,
                "relationship_property": None,
                "_comment_widai_extensions": "Fields below are WIDAI extensions per ADR-014",
                "strength_justification": {
                    "methodology": "No computational scoring — element has no match in WIDAI KSA pool",
                    "primary_method": None,
                    "secondary_methods": None
                },
                "regulatory_context": {
                    "applies_to": element["applies_to"],
                    "risk_category": element["risk_category"],
                    "enforcement_date": element["enforcement_date"]
                },
                "gap_signal": None,
                "evaluated_by": "AI-assisted (Claude) with human review",
                "evaluation_date": TODAY
            }
            strength_values.append(0)

        with open(filepath, 'w') as f_out:
            json.dump(rationale, f_out, indent=2)

    print(f"  Written {len(mappings)} rationale files to {RATIONALE_DIR}/\n", flush=True)

    # ── Update strm_mapping.json with strength scores ──
    print("Updating strm_mapping.json with strength scores...", flush=True)
    for m in mappings:
        fde_id = m["fde_id"]
        if m.get("ref_id"):
            scores = all_scores[fde_id]
            m["strength"] = round(scores["sts_strength_0_10"])
        else:
            m["strength"] = 0

    strm_data["mappings"] = [
        {k: v for k, v in m.items() if k not in ("article", "article_title")}
        for m in mappings
    ]
    with open(MAPPING_FILE, 'w') as f:
        json.dump(strm_data, f, indent=2)
    print("  strm_mapping.json updated.\n", flush=True)

    # ── Generate scoring summary ──
    print("Generating scoring summary...", flush=True)

    # Separate statistics by element type
    comp_strengths = [all_scores[m["fde_id"]]["sts_strength_0_10"] for m in comp_scored]
    obl_strengths = [all_scores[m["fde_id"]]["sts_strength_0_10"] for m in obl_scored]
    all_strengths = [s for s in strength_values]
    scored_strengths = comp_strengths + obl_strengths

    def stats_block(values):
        if not values:
            return {"count": 0, "mean": 0, "median": 0, "std": 0, "min": 0, "max": 0}
        return {
            "count": len(values),
            "mean": round(float(np.mean(values)), 2),
            "median": round(float(np.median(values)), 2),
            "std": round(float(np.std(values)), 2),
            "min": round(float(np.min(values)), 2),
            "max": round(float(np.max(values)), 2)
        }

    # By relationship type
    by_relationship = {}
    rel_types = set(m["relationship"] for m in mappings)
    for rel in sorted(rel_types):
        if rel == "No relationship":
            n = len([m for m in norel_mappings if m["relationship"] == rel])
            by_relationship[rel] = {"count": n, "mean": 0, "median": 0, "min": 0, "max": 0}
        else:
            rel_strengths = [
                all_scores[m["fde_id"]]["sts_strength_0_10"]
                for m in scored_mappings
                if m["relationship"] == rel
            ]
            by_relationship[rel] = stats_block(rel_strengths)

    # NLI diagnostic summary — documenting why NLI is secondary
    nli_entailments = [all_scores[m["fde_id"]]["nli"]["entailment"] for m in scored_mappings]
    nli_diagnostic = {
        "note": "NLI entailment is systematically low for competency→competency pairs. This is expected behavior, not a data quality issue.",
        "entailment_distribution": stats_block(nli_entailments),
        "interpretation": (
            "NLI measures strict logical implication. Two overlapping competency "
            "statements are typically 'neutral' in NLI terms — they describe related "
            "concepts without one logically implying the other. STS is the appropriate "
            "primary signal for measuring semantic relatedness between competency texts."
        )
    }

    summary = {
        "pipeline_run_date": TODAY,
        "strm_id": "STRM-005-EU-AI-ACT",
        "framework": "EU AI Act (Regulation (EU) 2024/1689)",
        "methodology": {
            "primary_method": {
                "name": "Cross-Encoder STS",
                "model": "cross-encoder/stsb-roberta-base",
                "role": "Generates strength_of_relationship integer (0-10)",
                "mapping": "raw_score (0-1) × 10, rounded to nearest integer",
                "note": "Consistent with STRM-001–004. Scores competency_implication text, not raw obligation_text."
            },
            "rationale_type": "Functional (per NIST IR 8477 Section 4.3)",
            "rationale_justification": (
                "The mapping direction is obligation→competency: what workforce "
                "capability is required to fulfill this regulatory requirement? "
                "This is a Functional question ('how similar are the results of "
                "executing the two concepts'), not a Semantic question."
            ),
            "scoring_text": "competency_implication field (workforce competency interpretation of each element)",
            "secondary": [
                {"name": "BERTScore", "model": "roberta-large", "role": "Token-level audit trail"},
                {"name": "NLI Cross-Encoder", "model": "cross-encoder/nli-deberta-v3-base", "role": "Contradiction detection, logical implication secondary signal"},
                {"name": "Bi-Encoder Cosine", "model": "all-MiniLM-L6-v2", "role": "Independent embedding cosine similarity"},
                {"name": "Jaccard Token", "model": None, "role": "Lexical baseline"}
            ],
            "nli_diagnostic": nli_diagnostic,
            "methodology_evolution": (
                "Originally planned as dual-mode (STS for competency elements, NLI "
                "for obligation elements). Diagnostic scoring revealed NLI entailment "
                "is near-zero for all element types (mean 0.007 for obligations). "
                "Revised to STS-primary for all elements. The competency_implication "
                "field bridges the vocabulary gap between legal prose and competency "
                "language, making STS appropriate. See ADR-019 for full documentation."
            )
        },
        "statistics": {
            "total_mappings": len(mappings),
            "scored_mappings": len(scored_mappings),
            "no_relationship_mappings": len(norel_mappings),
            "strength_distribution": {
                "all": stats_block(all_strengths),
                "scored_only": stats_block(scored_strengths),
                "competency_elements": stats_block(comp_strengths),
                "obligation_elements": stats_block(obl_strengths),
                "by_relationship_type": by_relationship
            },
            "element_type_breakdown": {
                "competency": {"total": len(competency_elements), "scored": len(comp_scored), "no_relationship": len(competency_elements) - len(comp_scored)},
                "obligation": {"total": len(obligation_elements), "scored": len(obl_scored), "no_relationship": len(obligation_elements) - len(obl_scored)}
            },
            "rationale_files_generated": len(mappings)
        }
    }

    with open(SCORING_SUMMARY_FILE, 'w') as f:
        json.dump(summary, f, indent=2)
    print(f"Scoring summary saved to {SCORING_SUMMARY_FILE}", flush=True)

    # ── Console summary ──
    print("\n" + "="*70, flush=True)
    print("STRM-005-EU-AI-ACT PIPELINE COMPLETE", flush=True)
    print("="*70, flush=True)
    print(f"  Primary method:   Cross-Encoder STS (all elements)", flush=True)
    print(f"  Rationale type:   Functional", flush=True)
    print(f"  Scoring text:     competency_implication field", flush=True)
    print(f"  Rationale files:  {len(mappings)} written to rationale/", flush=True)
    print(f"  strm_mapping.json: strength scores updated", flush=True)
    print(f"  scoring_summary.json: statistics saved", flush=True)

    if comp_strengths:
        print(f"\n  Competency elements: n={len(comp_strengths)}, "
              f"mean={np.mean(comp_strengths):.1f}, median={np.median(comp_strengths):.1f}, "
              f"std={np.std(comp_strengths):.1f}", flush=True)
    if obl_strengths:
        print(f"  Obligation elements: n={len(obl_strengths)}, "
              f"mean={np.mean(obl_strengths):.1f}, median={np.median(obl_strengths):.1f}, "
              f"std={np.std(obl_strengths):.1f}", flush=True)

    print(f"\n  Combined (all w/ zeros): mean={np.mean(all_strengths):.1f}, "
          f"median={np.median(all_strengths):.1f}", flush=True)

    print("\n  By relationship type:", flush=True)
    for rel in sorted(rel_types):
        info = by_relationship.get(rel, {})
        n = info.get("count", 0)
        if rel == "No relationship":
            print(f"    {rel:<20} n={n:>4}  strength=0", flush=True)
        elif n > 0:
            print(f"    {rel:<20} n={n:>4}  mean={info['mean']:.1f}  "
                  f"range=[{info['min']:.1f}, {info['max']:.1f}]", flush=True)

    print("\nDone.", flush=True)


if __name__ == "__main__":
    main()
