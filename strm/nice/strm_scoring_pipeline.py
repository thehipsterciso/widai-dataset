#!/usr/bin/env python3
"""
WIDAI STRM-002 Strength of Relationship Scoring Pipeline
=========================================================
Multi-method scoring for NICE Framework v2.1.0 TKS → WIDAI KSA mappings.

Primary:   Cross-Encoder STS (stsb-roberta-base) → strength_of_relationship 0-10
Secondary: BERTScore P/R/F1, NLI entailment/neutral/contradiction,
           Bi-encoder cosine similarity, Jaccard token overlap

All methods documented per-FDE in rationale JSON files per ADR-014.
Adapted from STRM-001-ONET pipeline for higher volume (2,148 vs 126 elements).
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

# ── Load Models ──
print("Loading models...")
print("  [1/4] Cross-Encoder STS (stsb-roberta-base)...")
sts_model = CrossEncoder('cross-encoder/stsb-roberta-base')

print("  [2/4] Cross-Encoder NLI (nli-deberta-v3-base)...")
nli_model = CrossEncoder('cross-encoder/nli-deberta-v3-base')

print("  [3/4] Bi-Encoder (all-MiniLM-L6-v2)...")
bienc_model = SentenceTransformer('all-MiniLM-L6-v2')

print("  [4/4] BERTScore will run in batch after individual scoring...")
print("Models loaded.\n")


def jaccard_similarity(text_a: str, text_b: str) -> float:
    """Token-level Jaccard similarity. Purely lexical, hand-traceable."""
    tokens_a = set(re.findall(r'\b\w+\b', text_a.lower()))
    tokens_b = set(re.findall(r'\b\w+\b', text_b.lower()))
    if not tokens_a or not tokens_b:
        return 0.0
    intersection = tokens_a & tokens_b
    union = tokens_a | tokens_b
    return len(intersection) / len(union)


def softmax(logits):
    """Convert raw logits to probabilities."""
    exp_logits = [math.exp(x) for x in logits]
    total = sum(exp_logits)
    return [x / total for x in exp_logits]


def score_pair(fde_text: str, ksa_text: str) -> dict:
    """Score a single FDE-KSA pair with all methods except BERTScore (batched later)."""
    
    # 1. Cross-Encoder STS (PRIMARY) — 0 to 1
    sts_raw = float(sts_model.predict([(fde_text, ksa_text)])[0])
    sts_strength = round(sts_raw * 10, 2)
    
    # 2. Cross-Encoder NLI — softmax probabilities
    nli_logits = nli_model.predict([(fde_text, ksa_text)])[0]
    # nli-deberta-v3-base labels: [contradiction, entailment, neutral]
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


def generate_significance(scores, relationship, fde_text, ksa_text):
    """Generate per-method significance interpretations."""
    sts = scores["sts_raw_0_1"]
    nli = scores["nli"]
    bienc = scores["biencoder_cosine_0_1"]
    jaccard = scores["jaccard_token_0_1"]
    sts_str = scores["sts_strength_0_10"]
    
    # STS significance
    if sts_str >= 7:
        sts_sig = f"Strong similarity ({sts_str}/10). The cross-encoder detects substantial semantic alignment between these concepts, indicating they describe closely related competencies despite domain-specific vocabulary."
    elif sts_str >= 4:
        sts_sig = f"Moderate similarity ({sts_str}/10). The cross-encoder finds meaningful but bounded overlap — consistent with cross-framework mapping between cybersecurity and data/AI domains where shared governance concepts use different terminology."
    elif sts_str >= 2:
        sts_sig = f"Weak similarity ({sts_str}/10). Limited semantic overlap detected. The relationship exists but the concepts diverge significantly in scope or application domain."
    else:
        sts_sig = f"Minimal similarity ({sts_str}/10). Near-zero cross-encoder score indicates the concepts share little semantic content despite being mapped as related."
    
    # NLI significance
    max_nli = max(nli.values())
    dominant = [k for k, v in nli.items() if v == max_nli][0]
    if dominant == "entailment" and nli["entailment"] > 0.5:
        nli_sig = f"Entailment-dominant ({nli['entailment']:.1%}). The NICE element logically implies aspects of the WIDAI KSA, indicating directional semantic containment."
    elif dominant == "neutral":
        nli_sig = f"Neutral-dominant ({nli['neutral']:.1%}). The model finds the descriptions related but neither implying nor contradicting each other — typical for cross-domain framework mapping where concepts overlap without strict logical implication."
    elif dominant == "contradiction" and nli["contradiction"] > 0.5:
        nli_sig = f"Contradiction-dominant ({nli['contradiction']:.1%}). The model detects scope divergence — the concepts may use similar vocabulary in opposing contexts. This warrants review but may reflect domain-specific usage patterns rather than true semantic conflict."
    else:
        nli_sig = f"Mixed signal (E:{nli['entailment']:.1%}, N:{nli['neutral']:.1%}, C:{nli['contradiction']:.1%}). No dominant classification — the relationship is genuinely ambiguous from a logical inference perspective."
    
    # Bi-encoder significance
    gap = abs(sts - bienc)
    if gap < 0.05:
        bienc_sig = f"Bi-encoder ({bienc:.3f}) closely tracks STS ({sts:.3f}). The small gap ({gap:.3f}) indicates the relationship is capturable through independent encoding — shared surface semantics align with cross-attention analysis."
    elif bienc > sts:
        bienc_sig = f"Bi-encoder ({bienc:.3f}) exceeds STS ({sts:.3f}). The independent embeddings find more similarity than cross-attention, suggesting surface-level vocabulary overlap exceeds the deeper semantic relationship."
    else:
        bienc_sig = f"Bi-encoder ({bienc:.3f}) trails STS ({sts:.3f}). Cross-attention captures semantic relationships that independent encoding misses — typical for cross-domain pairs where shared meaning exists beneath divergent vocabulary."
    
    # Jaccard significance
    if jaccard >= 0.15:
        jac_sig = f"Moderate lexical overlap ({jaccard:.1%} of tokens shared). Some shared vocabulary provides a traceable baseline for the semantic relationship."
    elif jaccard >= 0.05:
        jac_sig = f"Low lexical overlap ({jaccard:.1%}). Limited shared vocabulary — the relationship is primarily semantic rather than terminological."
    else:
        jac_sig = f"Near-zero lexical overlap ({jaccard:.1%}). The concepts use almost entirely different vocabulary, confirming the relationship is detected through semantic understanding, not word matching."
    
    return {
        "sts": sts_sig,
        "nli": nli_sig,
        "biencoder": bienc_sig,
        "jaccard": jac_sig
    }


def build_rationale_file(mapping, scores, bertscore_data, significance):
    """Build the per-FDE rationale JSON per ADR-014 approved schema."""
    
    strength = round(scores["sts_strength_0_10"])
    
    rationale_json = {
        "strm_id": "STRM-002-NICE",
        "fde_id": mapping["fde_id"],
        "fde_type": mapping["fde_type"],
        "_comment_nist_fields": "Fields below follow IR 8278Ar1 Section 3.2 OLIR template",
        "focal_document_element": mapping["fde_id"],
        "focal_document_element_description": mapping["fde_description"],
        "rationale": mapping["rationale"],
        "relationship": mapping["relationship"],
        "reference_document_element": mapping["ref_id"],
        "reference_document_element_description": mapping["ref_statement"],
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
                "significance": significance["sts"]
            },
            "secondary_methods": {
                "bertscore": {
                    "model": "roberta-large",
                    "description": "Token-level contextual embedding matching. Precision = FDE coverage of KSA tokens. Recall = KSA coverage by FDE tokens. F1 = harmonic mean.",
                    "precision": bertscore_data["precision"],
                    "recall": bertscore_data["recall"],
                    "f1": bertscore_data["f1"],
                    "significance": bertscore_data.get("significance", "")
                },
                "nli_cross_encoder": {
                    "model": "cross-encoder/nli-deberta-v3-base",
                    "description": "Natural Language Inference. Classifies text pair as entailment, neutral, or contradiction. Indicates directional implication strength.",
                    "contradiction": scores["nli"]["contradiction"],
                    "entailment": scores["nli"]["entailment"],
                    "neutral": scores["nli"]["neutral"],
                    "significance": significance["nli"]
                },
                "biencoder_cosine": {
                    "model": "all-MiniLM-L6-v2",
                    "description": "Bi-encoder sentence embeddings with cosine similarity. Each text encoded independently; measures vector-space proximity.",
                    "cosine_similarity_0_1": scores["biencoder_cosine_0_1"],
                    "significance": significance["biencoder"]
                },
                "jaccard_token": {
                    "description": "Token-level Jaccard similarity (intersection/union of lowercased word tokens). Purely lexical baseline, hand-traceable.",
                    "similarity_0_1": scores["jaccard_token_0_1"],
                    "significance": significance["jaccard"]
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
    print(f"Loading mappings from {MAPPING_FILE}...")
    with open(MAPPING_FILE, 'r') as f:
        strm_data = json.load(f)
    
    mappings = strm_data["mappings"]
    print(f"  {len(mappings)} total mappings loaded.")
    
    scored_mappings = [m for m in mappings if m.get("ref_id")]
    norel_mappings = [m for m in mappings if not m.get("ref_id")]
    print(f"  {len(scored_mappings)} with relationships to score")
    print(f"  {len(norel_mappings)} with no relationship (strength = 0)\n")
    
    # ── Score all pairs ──
    print("Scoring pairs with STS, NLI, Bi-Encoder, Jaccard...")
    all_scores = {}
    for i, m in enumerate(scored_mappings):
        scores = score_pair(m["fde_description"], m["ref_statement"])
        all_scores[m["fde_id"]] = scores
        if (i + 1) % 100 == 0:
            print(f"  Scored {i+1}/{len(scored_mappings)}")
    print(f"  Scored {len(scored_mappings)}/{len(scored_mappings)} — individual methods complete.\n")
    
    # ── BERTScore in batch ──
    print("Running BERTScore batch...")
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
        p = round(float(P[i]), 4)
        r = round(float(R[i]), 4)
        f1 = round(float(F1[i]), 4)
        
        # Generate BERTScore significance
        if f1 >= 0.90:
            sig = f"High token-level alignment (F1={f1:.3f}). Strong contextual embedding overlap at the token level."
        elif f1 >= 0.85:
            sig = f"Moderate token-level alignment (F1={f1:.3f}). "
            if p > r + 0.02:
                sig += f"Precision exceeds Recall (P={p:.3f} > R={r:.3f}), indicating the NICE element's semantic content is more tightly aligned with the KSA than the reverse."
            elif r > p + 0.02:
                sig += f"Recall exceeds Precision (R={r:.3f} > P={p:.3f}), indicating the KSA covers more of the NICE element than the element covers the KSA."
            else:
                sig += f"Balanced P/R ({p:.3f}/{r:.3f}) indicating symmetric token-level overlap."
        else:
            sig = f"Lower token-level alignment (F1={f1:.3f}). The concepts share limited contextual embedding similarity at the token level, consistent with cross-domain vocabulary divergence."
        
        bertscore_data[m["fde_id"]] = {
            "precision": p,
            "recall": r,
            "f1": f1,
            "significance": sig
        }
    print("BERTScore complete.\n")
    
    # ── Generate rationale files ──
    os.makedirs(RATIONALE_DIR, exist_ok=True)
    
    print("Generating per-FDE rationale files...")
    strength_values = []
    
    for m in mappings:
        fde_id = m["fde_id"]
        filename = fde_id + ".json"
        filepath = os.path.join(RATIONALE_DIR, filename)
        
        if m.get("ref_id"):
            scores = all_scores[fde_id]
            bs = bertscore_data[fde_id]
            significance = generate_significance(scores, m["relationship"], m["fde_description"], m["ref_statement"])
            rationale = build_rationale_file(m, scores, bs, significance)
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
    
    print(f"  Written {len(mappings)} rationale files to {RATIONALE_DIR}/\n")
    
    # ── Update strm_mapping.json ──
    print("Updating strm_mapping.json with STS-derived strength scores...")
    for m in mappings:
        fde_id = m["fde_id"]
        if m.get("ref_id"):
            scores = all_scores[fde_id]
            m["strength"] = round(scores["sts_strength_0_10"])
        else:
            m["strength"] = 0
    
    with open(MAPPING_FILE, 'w') as f:
        json.dump(strm_data, f, indent=2)
    print("  strm_mapping.json updated.\n")
    
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
    print(f"Scoring summary saved to {SCORING_SUMMARY_FILE}")
    
    # ── Console summary ──
    print("\n" + "="*70)
    print("PIPELINE COMPLETE")
    print("="*70)
    print(f"  Rationale files:  {len(mappings)} written to rationale/")
    print(f"  strm_mapping.json: strength scores updated")
    print(f"  scoring_summary.json: statistics saved")
    print(f"\n  Strength (scored pairs): mean={np.mean(scored_strengths):.1f}, "
          f"median={np.median(scored_strengths):.1f}, "
          f"std={np.std(scored_strengths):.1f}")
    print(f"  Strength (all w/ zeros): mean={np.mean(all_strengths):.1f}, "
          f"median={np.median(all_strengths):.1f}")
    
    for rel in sorted(rel_types):
        rel_s = [all_scores[m["fde_id"]]["sts_strength_0_10"] for m in scored_mappings if m["relationship"] == rel]
        if rel_s:
            print(f"    {rel:<20} n={len(rel_s):>4}  mean={np.mean(rel_s):.1f}  range=[{np.min(rel_s):.1f}, {np.max(rel_s):.1f}]")
        else:
            n = len([m for m in norel_mappings if m["relationship"] == rel])
            print(f"    {rel:<20} n={n:>4}  strength=0 (out of scope)")
    
    print("\nDone.")


if __name__ == "__main__":
    main()
