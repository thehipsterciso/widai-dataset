#!/usr/bin/env python3
"""
WIDAI STRM-004 Strength of Relationship Scoring Pipeline
=========================================================
Multi-method scoring for DDaT Capability Framework Skills → WIDAI KSA mappings.

Primary:   Cross-Encoder STS (stsb-roberta-base) → strength_of_relationship 0-10
Secondary: BERTScore P/R/F1, NLI entailment/neutral/contradiction,
           Bi-encoder cosine similarity, Jaccard token overlap

Methodology identical to STRM-001-ONET, STRM-002-NICE, STRM-003-DCWF.
Bi-encoder candidate identification used as preprocessing to establish
DDaT→WIDAI pairings (189 × 497 = 93,933 potential pairs), then full
multi-method scoring on every mapped pair.
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
DDAT_ELEMENTS_FILE = os.path.join(REPO_ROOT, "sources/ddat/ddat_elements.json")
KSA_DIR = os.path.join(REPO_ROOT, "ksas")
MAPPING_FILE = os.path.join(STRM_DIR, "strm_mapping.json")
RATIONALE_DIR = os.path.join(STRM_DIR, "rationale")
SCORING_SUMMARY_FILE = os.path.join(STRM_DIR, "scoring_summary.json")
CANDIDATES_FILE = os.path.join(REPO_ROOT, "sources/ddat/ddat_skill_candidates.json")

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

# DDaT-specific out-of-scope terms (IT ops, UX, accessibility, not data/AI)
DDAT_OOS_TERMS = {
    'accessibility', 'screen reader', 'assistive technology',
    'wcag', 'aria', 'usability', 'user experience',
    'interaction design', 'graphic design', 'visual design',
    'typography', 'illustration', 'animation',
    'content design', 'copy writing', 'editorial',
    'frontend', 'css', 'html', 'javascript', 'dom',
    'router', 'switch', 'firewall', 'cabling', 'rack',
    'desktop support', 'helpdesk', 'service desk',
    'printing', 'telephony', 'voip',
    'incident management', 'change management', 'release management',
    'itil', 'itsm'
}

# Data/AI/governance in-scope terms
DATA_AI_TERMS = {
    'data', 'analytics', 'ai', 'artificial intelligence', 'machine learning',
    'model', 'algorithm', 'dataset', 'database', 'governance', 'compliance',
    'privacy', 'risk', 'audit', 'policy', 'regulation', 'standard',
    'architecture', 'infrastructure', 'cloud', 'strategy', 'leadership',
    'stakeholder', 'program', 'project', 'management', 'quality',
    'steward', 'stewardship', 'catalog', 'metadata', 'pipeline',
    'integration', 'warehouse', 'lake', 'etl', 'visualization',
    'reporting', 'dashboard', 'kpi', 'metric', 'performance',
    'ethics', 'fairness', 'bias', 'transparency', 'accountability',
    'lifecycle', 'training', 'inference', 'deployment', 'monitoring',
    'workforce', 'talent', 'career', 'competency', 'certification',
    'vendor', 'procurement', 'budget', 'investment', 'portfolio',
    'enterprise', 'business', 'organization', 'operational',
    'statistics', 'statistical', 'analysis', 'engineering',
    'automation', 'testing', 'security', 'protection'
}


# ── Load Data ──
def load_ddat_elements():
    """Load DDaT skill elements from extracted JSON."""
    with open(DDAT_ELEMENTS_FILE) as f:
        data = json.load(f)
    return data["skills"], data["roles"]


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


def classify_element(desc, cosine_score):
    """Classify DDaT skill as in-scope or out-of-scope for WIDAI."""
    desc_lower = desc.lower()

    # Check for DDaT OOS signals
    oos_hits = sum(1 for t in DDAT_OOS_TERMS if t in desc_lower)
    # Check for data/AI in-scope signals
    inscope_hits = sum(1 for t in DATA_AI_TERMS if t in desc_lower)

    # Strong out-of-scope: many OOS terms, few data/AI terms, low cosine
    if oos_hits >= 2 and inscope_hits == 0 and cosine_score < 0.35:
        return "No relationship"
    if oos_hits >= 3 and cosine_score < 0.40:
        return "No relationship"

    # High cosine with in-scope terms = relationship exists
    if cosine_score >= 0.65 and inscope_hits >= 2:
        return "Equal"
    if cosine_score >= 0.55:
        return "Superset of"
    if cosine_score >= 0.30:
        return "Intersects with"

    # Low cosine, no strong in-scope signal
    if cosine_score < 0.30 and inscope_hits <= 1:
        return "No relationship"

    return "Intersects with"


# ── Significance Generators ──

def sig_sts(sts_raw, strength, ta, fde_text, ksa_text):
    parts = [f"STS {strength}/10 (raw {sts_raw:.3f})."]
    if ta["shared_sub"]:
        parts.append(f"Shared vocabulary: [{', '.join(ta['shared_sub'][:10])}].")
    else:
        parts.append("No substantive shared vocabulary — relationship is purely semantic.")
    if ta["fde_only"] and ta["ksa_only"]:
        parts.append(
            f"DDaT-only terms [{', '.join(ta['fde_only'][:6])}] "
            f"vs WIDAI-only terms [{', '.join(ta['ksa_only'][:6])}] "
            f"define the semantic distance between the descriptions."
        )
    return " ".join(parts)


def sig_bertscore(p, r, f1, ta):
    parts = [f"BERTScore F1={f1:.3f} (P={p:.3f}, R={r:.3f})."]
    fw = ta["fde_words"]
    kw = ta["ksa_words"]
    if abs(p - r) < 0.02:
        parts.append(
            f"Balanced P/R — the {fw}-word DDaT element and "
            f"{kw}-word WIDAI KSA cover each other's token-level "
            f"semantic content symmetrically."
        )
    elif p > r:
        parts.append(
            f"P exceeds R by {p - r:.3f} — the DDaT element's {fw} words "
            f"are well-captured by the WIDAI KSA's {kw} words, "
            f"but the KSA contains additional specificity "
            f"not reflected in the DDaT element."
        )
    else:
        parts.append(
            f"R exceeds P by {r - p:.3f} — the WIDAI KSA's {kw} words "
            f"are well-captured by the DDaT element's {fw} words, "
            f"but the DDaT element contains broader scope "
            f"not fully reflected in the matched WIDAI KSA."
        )
    return " ".join(parts)


def sig_nli(nli, fde_text, ksa_text, relationship):
    c, e, n = nli["contradiction"], nli["entailment"], nli["neutral"]
    fde_short = fde_text[:80].rstrip()
    ksa_short = ksa_text[:80].rstrip()
    if e > 0.5:
        return (
            f"NLI: entailment-dominant ({e:.1%}). "
            f"The model interprets \"{fde_short}\" as logically implying "
            f"aspects of \"{ksa_short}\" — directional semantic containment "
            f"consistent with '{relationship}' classification."
        )
    elif c > 0.5:
        return (
            f"NLI: contradiction-dominant ({c:.1%}). "
            f"Despite '{relationship}' classification, the model detects "
            f"semantic tension between \"{fde_short}\" and "
            f"\"{ksa_short}\". Indicates these concepts operate in "
            f"adjacent but distinct professional domains — "
            f"shared vocabulary, different application context."
        )
    elif n > 0.8:
        return (
            f"NLI: neutral-dominant ({n:.1%}). "
            f"\"{fde_short}\" and \"{ksa_short}\" are related but neither "
            f"implies nor contradicts the other. Standard result for cross-framework "
            f"mapping where two independent frameworks describe overlapping "
            f"competencies with independent vocabulary."
        )
    else:
        return (
            f"NLI: mixed signal (E:{e:.1%}, N:{n:.1%}, C:{c:.1%}). "
            f"No dominant classification for \"{fde_short}\" vs "
            f"\"{ksa_short}\" — the relationship is genuinely ambiguous "
            f"from a logical inference perspective."
        )


def sig_biencoder(bienc, sts, ta):
    gap = bienc - sts
    abs_gap = abs(gap)
    shared_str = ', '.join(ta['shared_sub'][:5]) if ta['shared_sub'] else 'none'
    if abs_gap < 0.05:
        return (
            f"Bi-encoder {bienc:.3f} \u2248 STS {sts:.3f} (gap {abs_gap:.3f}). "
            f"Independent encoding and cross-attention agree. "
            f"Shared terms [{shared_str}] are sufficient for "
            f"independent encoding to detect the match."
        )
    elif gap > 0:
        return (
            f"Bi-encoder {bienc:.3f} > STS {sts:.3f} (gap +{gap:.3f}). "
            f"Independent encoding finds more similarity than cross-attention. "
            f"Shared surface terms [{shared_str}] inflate the bi-encoder, "
            f"but cross-attention detects semantic divergence beneath "
            f"the vocabulary overlap."
        )
    else:
        return (
            f"Bi-encoder {bienc:.3f} < STS {sts:.3f} (gap {gap:.3f}). "
            f"Cross-attention finds deeper alignment than independent encoding. "
            f"The relationship depends on cross-text reasoning — "
            f"concept-level mapping between [{', '.join(ta['fde_only'][:3])}] "
            f"and [{', '.join(ta['ksa_only'][:3])}] that bi-encoders "
            f"structurally cannot capture."
        )


def sig_jaccard(jaccard, ta):
    if not ta["shared_sub"]:
        return (
            f"Jaccard {jaccard:.1%}. Zero substantive shared tokens. "
            f"The entire relationship is semantic — no lexical trace. "
            f"DDaT terms: [{', '.join(ta['fde_only'][:6])}]. "
            f"WIDAI terms: [{', '.join(ta['ksa_only'][:6])}]."
        )
    return (
        f"Jaccard {jaccard:.1%}. "
        f"Shared tokens: [{', '.join(ta['shared_sub'])}]. "
        f"DDaT-only: [{', '.join(ta['fde_only'][:6])}]. "
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


def build_rationale_file(mapping, scores, bertscore_data, ta):
    """Build the per-FDE rationale JSON with content-specific significance."""
    strength = round(scores["sts_strength_0_10"])
    fde_text = mapping["fde_description"]
    ksa_text = mapping["ref_statement"]
    relationship = mapping["relationship"]

    sts_sig = sig_sts(scores["sts_raw_0_1"], scores["sts_strength_0_10"], ta, fde_text, ksa_text)
    bs_sig = sig_bertscore(bertscore_data["precision"], bertscore_data["recall"], bertscore_data["f1"], ta)
    nli_sig = sig_nli(scores["nli"], fde_text, ksa_text, relationship)
    bienc_sig = sig_biencoder(scores["biencoder_cosine_0_1"], scores["sts_raw_0_1"], ta)
    jac_sig = sig_jaccard(scores["jaccard_token_0_1"], ta)

    return {
        "strm_id": "STRM-004-DDAT",
        "fde_id": mapping["fde_id"],
        "fde_type": mapping["fde_type"],
        "_comment_nist_fields": "Fields below follow IR 8278Ar1 Section 3.2 OLIR template",
        "focal_document_element": mapping["fde_id"],
        "focal_document_element_description": fde_text,
        "rationale": mapping["rationale"],
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
            "methodology": "Multi-method computational scoring",
            "primary_method": {
                "name": "Cross-Encoder STS",
                "model": "cross-encoder/stsb-roberta-base",
                "description": "Semantic Textual Similarity via cross-encoder regression trained on STS-Benchmark.",
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
                    "description": "Natural Language Inference classification.",
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
        "gap_signal": None,
        "evaluated_by": "AI-assisted (Claude) with human review",
        "evaluation_date": TODAY
    }


def main():
    # ── Load data ──
    print("Loading DDaT elements and WIDAI KSAs...", flush=True)
    ddat_skills, ddat_roles = load_ddat_elements()
    widai_ksas = load_widai_ksas()
    print(f"  DDaT: {len(ddat_skills)} skills across {len(ddat_roles)} roles", flush=True)
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
    candidates = {c["ddat_id"]: c for c in cand_data["candidates"]}
    print(f"  Loaded {len(candidates)} candidate sets.\n", flush=True)

    # ── Phase 2: Classification and mapping ──
    print("Phase 2: Classification and mapping...", flush=True)
    mappings = []
    for skill in ddat_skills:
        ddat_id = skill["ddat_id"]
        desc = skill["description"]

        cand = candidates[ddat_id]
        best = cand["candidates"][0]
        cosine = best["cosine_similarity"]

        relationship = classify_element(desc, cosine)

        if relationship == "No relationship":
            mappings.append({
                "fde_id": ddat_id,
                "fde_type": "skill",
                "fde_description": desc,
                "skill_name": skill["skill_name"],
                "relationship": "No relationship",
                "ref_id": None,
                "ref_statement": None,
                "ref_domain": None,
                "rationale": "Semantic",
                "notes": f"DDaT skill classified as out of WIDAI scope. "
                         f"Best candidate: {best['ksa_id']} ({best['domain_code']}, cosine: {cosine:.3f}). "
                         f"Insufficient semantic overlap with data/AI workforce competencies.",
                "strength": 0
            })
        else:
            secondaries = [
                f"{c['ksa_id']} ({c['domain_code']}, cosine: {c['cosine_similarity']:.3f})"
                for c in cand["candidates"][1:3]
            ]
            mappings.append({
                "fde_id": ddat_id,
                "fde_type": "skill",
                "fde_description": desc,
                "skill_name": skill["skill_name"],
                "relationship": relationship,
                "ref_id": best["ksa_id"],
                "ref_statement": best["statement"],
                "ref_domain": best["domain_code"],
                "rationale": "Semantic",
                "notes": f"DDaT skill {relationship.lower()} WIDAI {best['domain_code']} domain. "
                         f"{best['ksa_id']} is the strongest semantic match. "
                         f"Secondary: {', '.join(secondaries)}.",
                "strength": 0  # Will be filled by scoring
            })

    scored_mappings = [m for m in mappings if m.get("ref_id")]
    norel_mappings = [m for m in mappings if not m.get("ref_id")]
    print(f"  {len(mappings)} total mappings", flush=True)
    print(f"  {len(scored_mappings)} with relationships to score", flush=True)
    print(f"  {len(norel_mappings)} no relationship\n", flush=True)

    # Save initial mapping
    strm_data = {
        "strm_id": "STRM-004-DDAT",
        "framework": "DDaT Capability Framework",
        "framework_source": "Government Digital and Data Profession Capability Framework (2026-03-23)",
        "widai_version": "0.5.2",
        "total_fdes": len(mappings),
        "mapping_date": TODAY,
        "mappings": [{k: v for k, v in m.items() if k != "skill_name"} for m in mappings]
    }
    with open(MAPPING_FILE, 'w') as f:
        json.dump(strm_data, f, indent=2)
    print(f"  Initial mapping saved to {MAPPING_FILE}\n", flush=True)

    # ── Phase 3: Full multi-method scoring ──
    print("Phase 3: Scoring pairs with STS, NLI, Bi-Encoder, Jaccard...", flush=True)
    all_scores = {}
    all_text_analysis = {}
    for i, m in enumerate(scored_mappings):
        scores = score_pair(m["fde_description"], m["ref_statement"],
                           sts_model, nli_model, bienc_model)
        all_scores[m["fde_id"]] = scores
        all_text_analysis[m["fde_id"]] = get_text_analysis(m["fde_description"], m["ref_statement"])
        if (i + 1) % 50 == 0:
            print(f"  Scored {i+1}/{len(scored_mappings)}", flush=True)
    print(f"  Scored {len(scored_mappings)}/{len(scored_mappings)} — individual methods complete.\n", flush=True)

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
        filename = str(fde_id).replace("/", "-") + ".json"
        filepath = os.path.join(RATIONALE_DIR, filename)

        if m.get("ref_id"):
            scores = all_scores[fde_id]
            bs = bertscore_data[fde_id]
            ta = all_text_analysis[fde_id]
            rationale = build_rationale_file(m, scores, bs, ta)
            strength_values.append(rationale["strength_of_relationship"])
        else:
            rationale = {
                "strm_id": "STRM-004-DDAT",
                "fde_id": fde_id,
                "fde_type": "skill",
                "_comment_nist_fields": "Fields below follow IR 8278Ar1 Section 3.2 OLIR template",
                "focal_document_element": fde_id,
                "focal_document_element_description": m["fde_description"],
                "rationale": m["rationale"],
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
                    "methodology": "No computational scoring — element determined out of WIDAI scope",
                    "primary_method": None,
                    "secondary_methods": None
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
    print("Updating strm_mapping.json with STS-derived strength scores...", flush=True)
    for m in mappings:
        fde_id = m["fde_id"]
        if m.get("ref_id"):
            scores = all_scores[fde_id]
            m["strength"] = round(scores["sts_strength_0_10"])
        else:
            m["strength"] = 0

    strm_data["mappings"] = [{k: v for k, v in m.items() if k != "skill_name"} for m in mappings]
    with open(MAPPING_FILE, 'w') as f:
        json.dump(strm_data, f, indent=2)
    print("  strm_mapping.json updated.\n", flush=True)

    # ── Generate scoring summary ──
    scored_strengths = [all_scores[m["fde_id"]]["sts_strength_0_10"] for m in scored_mappings]
    all_strengths = [s for s in strength_values]

    summary = {
        "pipeline_run_date": TODAY,
        "strm_id": "STRM-004-DDAT",
        "framework": "DDaT Capability Framework",
        "methodology": {
            "primary": {
                "name": "Cross-Encoder STS",
                "model": "cross-encoder/stsb-roberta-base",
                "role": "Generates strength_of_relationship integer (0-10)",
                "mapping": "raw_score (0-1) x 10, rounded to nearest integer"
            },
            "secondary": [
                {"name": "BERTScore", "model": "roberta-large", "role": "Token-level audit trail"},
                {"name": "NLI Cross-Encoder", "model": "cross-encoder/nli-deberta-v3-base", "role": "Directional implication classification"},
                {"name": "Bi-Encoder Cosine", "model": "all-MiniLM-L6-v2", "role": "Independent embedding cosine similarity"},
                {"name": "Jaccard Token", "model": None, "role": "Lexical baseline"}
            ]
        },
        "statistics": {
            "total_mappings": len(mappings),
            "scored_mappings": len(scored_mappings),
            "no_relationship_mappings": len(norel_mappings),
            "strength_distribution": {
                "all": {
                    "mean": round(float(np.mean(all_strengths)), 2),
                    "median": round(float(np.median(all_strengths)), 2),
                    "std": round(float(np.std(all_strengths)), 2),
                    "min": round(float(np.min(all_strengths)), 2),
                    "max": round(float(np.max(all_strengths)), 2)
                },
                "scored_only": {
                    "mean": round(float(np.mean(scored_strengths)), 2),
                    "median": round(float(np.median(scored_strengths)), 2),
                    "std": round(float(np.std(scored_strengths)), 2),
                    "min": round(float(np.min(scored_strengths)), 2),
                    "max": round(float(np.max(scored_strengths)), 2)
                },
                "by_relationship_type": {}
            },
            "rationale_files_generated": len(mappings)
        }
    }

    rel_types = set(m["relationship"] for m in mappings)
    for rel in sorted(rel_types):
        rel_strengths = [
            all_scores[m["fde_id"]]["sts_strength_0_10"]
            for m in scored_mappings
            if m["relationship"] == rel
        ]
        if rel_strengths:
            summary["statistics"]["strength_distribution"]["by_relationship_type"][rel] = {
                "count": len(rel_strengths),
                "mean": round(float(np.mean(rel_strengths)), 2),
                "median": round(float(np.median(rel_strengths)), 2),
                "min": round(float(np.min(rel_strengths)), 2),
                "max": round(float(np.max(rel_strengths)), 2)
            }
        else:
            n = len([m for m in norel_mappings if m["relationship"] == rel])
            summary["statistics"]["strength_distribution"]["by_relationship_type"][rel] = {
                "count": n, "mean": 0, "median": 0, "min": 0, "max": 0
            }

    with open(SCORING_SUMMARY_FILE, 'w') as f:
        json.dump(summary, f, indent=2)
    print(f"Scoring summary saved to {SCORING_SUMMARY_FILE}", flush=True)

    # ── Console summary ──
    print("\n" + "="*70, flush=True)
    print("PIPELINE COMPLETE", flush=True)
    print("="*70, flush=True)
    print(f"  Rationale files:  {len(mappings)} written to rationale/", flush=True)
    print(f"  strm_mapping.json: strength scores updated", flush=True)
    print(f"  scoring_summary.json: statistics saved", flush=True)
    print(f"\n  Strength (scored pairs): mean={np.mean(scored_strengths):.1f}, "
          f"median={np.median(scored_strengths):.1f}, "
          f"std={np.std(scored_strengths):.1f}", flush=True)
    print(f"  Strength (all w/ zeros): mean={np.mean(all_strengths):.1f}, "
          f"median={np.median(all_strengths):.1f}", flush=True)

    for rel in sorted(rel_types):
        rel_s = [all_scores[m["fde_id"]]["sts_strength_0_10"] for m in scored_mappings if m["relationship"] == rel]
        if rel_s:
            print(f"    {rel:<20} n={len(rel_s):>4}  mean={np.mean(rel_s):.1f}  range=[{np.min(rel_s):.1f}, {np.max(rel_s):.1f}]", flush=True)
        else:
            n = len([m for m in norel_mappings if m["relationship"] == rel])
            print(f"    {rel:<20} n={n:>4}  strength=0 (out of scope)", flush=True)

    print("\nDone.", flush=True)


if __name__ == "__main__":
    main()
