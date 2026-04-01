#!/usr/bin/env python3
"""
WIDAI STRM-002 Strength of Relationship Scoring Pipeline
=========================================================
Multi-method scoring for NICE Framework v2.1.0 TKS → WIDAI KSA mappings.

Primary:   Cross-Encoder STS (stsb-roberta-base) → strength_of_relationship 0-10
Secondary: BERTScore P/R/F1, NLI entailment/neutral/contradiction,
           Bi-encoder cosine similarity, Jaccard token overlap

Each scored pair receives substantive, content-specific significance
analysis referencing actual shared vocabulary, concept bridges, and
directional implications for the specific text pair.

Adapted from STRM-001-ONET pipeline. Single-stage: every mapped pair
scored with all five methods in one pass.
"""

import json
import os
import sys
import re
import math
from datetime import date

import numpy as np
from sentence_transformers import CrossEncoder, SentenceTransformer, util
from bert_score import score as bertscore_fn

# ── Configuration ──
STRM_DIR = os.path.dirname(os.path.abspath(__file__))
MAPPING_FILE = os.path.join(STRM_DIR, "strm_mapping.json")
RATIONALE_DIR = os.path.join(STRM_DIR, "rationale")
SCORING_SUMMARY_FILE = os.path.join(STRM_DIR, "scoring_summary.json")

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
    'out', 'over', 'under', 'also', 'including', 'e', 'g'
}


# ── Load Models ──
print("Loading models...", flush=True)
print("  [1/4] Cross-Encoder STS (stsb-roberta-base)...", flush=True)
sts_model = CrossEncoder('cross-encoder/stsb-roberta-base')

print("  [2/4] Cross-Encoder NLI (nli-deberta-v3-base)...", flush=True)
nli_model = CrossEncoder('cross-encoder/nli-deberta-v3-base')

print("  [3/4] Bi-Encoder (all-MiniLM-L6-v2)...", flush=True)
bienc_model = SentenceTransformer('all-MiniLM-L6-v2')

print("  [4/4] BERTScore will run in batch after individual scoring...", flush=True)
print("Models loaded.\n", flush=True)


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


# ── Significance Generators ──

def sig_sts(sts_raw, strength, ta, fde_text, ksa_text):
    """STS significance: shared vocab, concept bridges, unique terms."""
    parts = [f"STS {strength}/10 (raw {sts_raw:.3f})."]

    if ta["shared_sub"]:
        parts.append(f"Shared vocabulary: [{', '.join(ta['shared_sub'][:10])}].")
    else:
        parts.append("No substantive shared vocabulary — relationship is purely semantic.")

    if ta["fde_only"] and ta["ksa_only"]:
        parts.append(
            f"NICE-only terms [{', '.join(ta['fde_only'][:6])}] "
            f"vs WIDAI-only terms [{', '.join(ta['ksa_only'][:6])}] "
            f"define the semantic distance between the descriptions."
        )

    return " ".join(parts)


def sig_bertscore(p, r, f1, ta):
    """BERTScore significance: directional analysis with word counts."""
    parts = [f"BERTScore F1={f1:.3f} (P={p:.3f}, R={r:.3f})."]

    fw = ta["fde_words"]
    kw = ta["ksa_words"]

    if abs(p - r) < 0.02:
        parts.append(
            f"Balanced P/R — the {fw}-word NICE element and "
            f"{kw}-word WIDAI KSA cover each other's token-level "
            f"semantic content symmetrically."
        )
    elif p > r:
        parts.append(
            f"P exceeds R by {p - r:.3f} — the NICE element's {fw} words "
            f"are well-captured by the WIDAI KSA's {kw} words, "
            f"but the KSA contains additional specificity "
            f"not reflected in the NICE element."
        )
    else:
        parts.append(
            f"R exceeds P by {r - p:.3f} — the WIDAI KSA's {kw} words "
            f"are well-captured by the NICE element's {fw} words, "
            f"but the NICE element contains broader scope "
            f"not fully reflected in the matched WIDAI KSA."
        )

    return " ".join(parts)


def sig_nli(nli, fde_text, ksa_text, relationship):
    """NLI significance: what the classification means for this specific pair."""
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
    """Bi-encoder significance: explain the STS gap using shared vocab."""
    gap = bienc - sts
    abs_gap = abs(gap)
    shared_str = ', '.join(ta['shared_sub'][:5]) if ta['shared_sub'] else 'none'

    if abs_gap < 0.05:
        return (
            f"Bi-encoder {bienc:.3f} ≈ STS {sts:.3f} (gap {abs_gap:.3f}). "
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
    """Jaccard significance: list actual shared tokens, unique tokens."""
    if not ta["shared_sub"]:
        return (
            f"Jaccard {jaccard:.1%}. Zero substantive shared tokens. "
            f"The entire relationship is semantic — no lexical trace. "
            f"NICE terms: [{', '.join(ta['fde_only'][:6])}]. "
            f"WIDAI terms: [{', '.join(ta['ksa_only'][:6])}]."
        )

    return (
        f"Jaccard {jaccard:.1%}. "
        f"Shared tokens: [{', '.join(ta['shared_sub'])}]. "
        f"NICE-only: [{', '.join(ta['fde_only'][:6])}]. "
        f"WIDAI-only: [{', '.join(ta['ksa_only'][:6])}]."
    )


# ── Scoring ──

def score_pair(fde_text, ksa_text):
    """Score a single FDE-KSA pair with all methods except BERTScore (batched)."""

    # 1. Cross-Encoder STS (PRIMARY) — 0 to 1
    sts_raw = float(sts_model.predict([(fde_text, ksa_text)])[0])
    sts_strength = round(sts_raw * 10, 2)

    # 2. Cross-Encoder NLI — softmax probabilities
    nli_logits = nli_model.predict([(fde_text, ksa_text)])[0]
    probs = softmax([float(x) for x in nli_logits])
    nli_result = {
        "contradiction": round(probs[0], 4),
        "entailment": round(probs[1], 4),
        "neutral": round(probs[2], 4)
    }

    # 3. Bi-Encoder Cosine Similarity — 0 to 1
    emb_fde = bienc_model.encode(fde_text, convert_to_tensor=True)
    emb_ksa = bienc_model.encode(ksa_text, convert_to_tensor=True)
    bienc_cosine = float(util.cos_sim(emb_fde, emb_ksa)[0][0])

    # 4. Jaccard Token Overlap — 0 to 1
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

    # Generate all significance fields
    sts_sig = sig_sts(scores["sts_raw_0_1"], scores["sts_strength_0_10"], ta, fde_text, ksa_text)
    bs_sig = sig_bertscore(bertscore_data["precision"], bertscore_data["recall"], bertscore_data["f1"], ta)
    nli_sig = sig_nli(scores["nli"], fde_text, ksa_text, relationship)
    bienc_sig = sig_biencoder(scores["biencoder_cosine_0_1"], scores["sts_raw_0_1"], ta)
    jac_sig = sig_jaccard(scores["jaccard_token_0_1"], ta)

    rationale_json = {
        "strm_id": "STRM-002-NICE",
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
                "description": "Semantic Textual Similarity via cross-encoder regression trained on STS-Benchmark. Both texts processed jointly through transformer; outputs calibrated 0-1 similarity score.",
                "raw_score_0_1": scores["sts_raw_0_1"],
                "mapped_strength_0_10": scores["sts_strength_0_10"],
                "final_strength_integer": strength,
                "significance": sts_sig
            },
            "secondary_methods": {
                "bertscore": {
                    "model": "roberta-large",
                    "description": "Token-level contextual embedding matching. Precision = FDE coverage of KSA tokens. Recall = KSA coverage by FDE tokens. F1 = harmonic mean.",
                    "precision": bertscore_data["precision"],
                    "recall": bertscore_data["recall"],
                    "f1": bertscore_data["f1"],
                    "significance": bs_sig
                },
                "nli_cross_encoder": {
                    "model": "cross-encoder/nli-deberta-v3-base",
                    "description": "Natural Language Inference. Classifies text pair as entailment, neutral, or contradiction. Indicates directional implication strength.",
                    "contradiction": scores["nli"]["contradiction"],
                    "entailment": scores["nli"]["entailment"],
                    "neutral": scores["nli"]["neutral"],
                    "significance": nli_sig
                },
                "biencoder_cosine": {
                    "model": "all-MiniLM-L6-v2",
                    "description": "Bi-encoder sentence embeddings with cosine similarity. Each text encoded independently; measures vector-space proximity.",
                    "cosine_similarity_0_1": scores["biencoder_cosine_0_1"],
                    "significance": bienc_sig
                },
                "jaccard_token": {
                    "description": "Token-level Jaccard similarity (intersection/union of lowercased word tokens). Purely lexical baseline, hand-traceable.",
                    "similarity_0_1": scores["jaccard_token_0_1"],
                    "significance": jac_sig
                }
            }
        },
        "gap_signal": None,
        "evaluated_by": "AI-assisted (Claude) with human review",
        "evaluation_date": TODAY
    }

    return rationale_json


def main():
    # ── Load mappings ──
    print(f"Loading mappings from {MAPPING_FILE}...", flush=True)
    with open(MAPPING_FILE, 'r') as f:
        strm_data = json.load(f)

    mappings = strm_data["mappings"]
    print(f"  {len(mappings)} total mappings loaded.", flush=True)

    scored_mappings = [m for m in mappings if m.get("ref_id")]
    norel_mappings = [m for m in mappings if not m.get("ref_id")]
    print(f"  {len(scored_mappings)} with relationships to score", flush=True)
    print(f"  {len(norel_mappings)} with no relationship (strength = 0)\n", flush=True)

    # ── Score all pairs (single-stage) ──
    print("Scoring pairs with STS, NLI, Bi-Encoder, Jaccard...", flush=True)
    all_scores = {}
    all_text_analysis = {}
    for i, m in enumerate(scored_mappings):
        scores = score_pair(m["fde_description"], m["ref_statement"])
        all_scores[m["fde_id"]] = scores
        all_text_analysis[m["fde_id"]] = get_text_analysis(m["fde_description"], m["ref_statement"])
        if (i + 1) % 100 == 0:
            print(f"  Scored {i+1}/{len(scored_mappings)}", flush=True)
    print(f"  Scored {len(scored_mappings)}/{len(scored_mappings)} — individual methods complete.\n", flush=True)

    # ── BERTScore in batch ──
    print("Running BERTScore batch...", flush=True)
    fde_texts = [m["fde_description"] for m in scored_mappings]
    ksa_texts = [m["ref_statement"] for m in scored_mappings]

    P, R, F1 = bertscore_fn(
        cands=fde_texts,
        refs=ksa_texts,
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

    # ── Clear and regenerate rationale files ──
    if os.path.exists(RATIONALE_DIR):
        for f in os.listdir(RATIONALE_DIR):
            os.remove(os.path.join(RATIONALE_DIR, f))
        print(f"Cleared existing rationale files.", flush=True)
    os.makedirs(RATIONALE_DIR, exist_ok=True)

    print("Generating per-FDE rationale files...", flush=True)
    strength_values = []

    for m in mappings:
        fde_id = m["fde_id"]
        filename = fde_id + ".json"
        filepath = os.path.join(RATIONALE_DIR, filename)

        if m.get("ref_id"):
            scores = all_scores[fde_id]
            bs = bertscore_data[fde_id]
            ta = all_text_analysis[fde_id]
            rationale = build_rationale_file(m, scores, bs, ta)
            strength_values.append(rationale["strength_of_relationship"])
        else:
            rationale = {
                "strm_id": "STRM-002-NICE",
                "fde_id": fde_id,
                "fde_type": m["fde_type"],
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
                    "methodology": "No computational scoring — element determined out of WIDAI scope during semantic analysis",
                    "primary_method": None,
                    "secondary_methods": None
                },
                "gap_signal": None,
                "evaluated_by": "AI-assisted (Claude) with human review",
                "evaluation_date": TODAY
            }
            strength_values.append(0)

        with open(filepath, 'w') as f:
            json.dump(rationale, f, indent=2)

    print(f"  Written {len(mappings)} rationale files to {RATIONALE_DIR}/\n", flush=True)

    # ── Update strm_mapping.json ──
    print("Updating strm_mapping.json with STS-derived strength scores...", flush=True)
    for m in mappings:
        fde_id = m["fde_id"]
        if m.get("ref_id"):
            scores = all_scores[fde_id]
            m["strength"] = round(scores["sts_strength_0_10"])
        else:
            m["strength"] = 0

    with open(MAPPING_FILE, 'w') as f:
        json.dump(strm_data, f, indent=2)
    print("  strm_mapping.json updated.\n", flush=True)

    # ── Generate scoring summary ──
    scored_strengths = [all_scores[m["fde_id"]]["sts_strength_0_10"] for m in scored_mappings]
    all_strengths = [s for s in strength_values]

    summary = {
        "pipeline_run_date": TODAY,
        "strm_id": "STRM-002-NICE",
        "framework": "NIST NICE Framework v2.1.0",
        "methodology": {
            "primary": {
                "name": "Cross-Encoder STS",
                "model": "cross-encoder/stsb-roberta-base",
                "role": "Generates strength_of_relationship integer (0-10)",
                "mapping": "raw_score (0-1) × 10, rounded to nearest integer"
            },
            "secondary": [
                {"name": "BERTScore", "model": "roberta-large", "role": "Token-level audit trail (Precision, Recall, F1)"},
                {"name": "NLI Cross-Encoder", "model": "cross-encoder/nli-deberta-v3-base", "role": "Directional implication classification (entailment/neutral/contradiction)"},
                {"name": "Bi-Encoder Cosine", "model": "all-MiniLM-L6-v2", "role": "Independent embedding cosine similarity"},
                {"name": "Jaccard Token", "model": None, "role": "Lexical baseline (word token intersection/union)"}
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

    # ── Show example for verification ──
    example_path = os.path.join(RATIONALE_DIR, "T1857.json")
    if os.path.exists(example_path):
        with open(example_path) as f:
            ex = json.load(f)
        sj = ex["strength_justification"]
        print("\n--- EXAMPLE: T1857 ---", flush=True)
        print(f"STS: {sj['primary_method']['significance']}", flush=True)
        print(f"BERTScore: {sj['secondary_methods']['bertscore']['significance']}", flush=True)
        print(f"NLI: {sj['secondary_methods']['nli_cross_encoder']['significance']}", flush=True)
        print(f"Bi-enc: {sj['secondary_methods']['biencoder_cosine']['significance']}", flush=True)
        print(f"Jaccard: {sj['secondary_methods']['jaccard_token']['significance']}", flush=True)

    print("\nDone.", flush=True)


if __name__ == "__main__":
    main()
