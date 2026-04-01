#!/usr/bin/env python3
"""
WIDAI STRM-001 Strength of Relationship Scoring Pipeline
=========================================================
Multi-method scoring for O*NET FDE → WIDAI KSA mappings.

Primary:   Cross-Encoder STS (stsb-roberta-base) → strength_of_relationship 0-10
Secondary: BERTScore P/R/F1, NLI entailment/neutral/contradiction, 
           Bi-encoder cosine similarity, Jaccard token overlap

All methods documented per-FDE in rationale JSON files per ADR-014.
"""

import json
import os
import sys
import re
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


def score_pair(fde_text: str, ksa_text: str) -> dict:
    """Score a single FDE-KSA pair with all methods except BERTScore (batched later)."""
    
    # 1. Cross-Encoder STS (PRIMARY) — 0 to 1
    sts_raw = float(sts_model.predict([(fde_text, ksa_text)])[0])
    sts_strength = round(sts_raw * 10, 2)
    
    # 2. Cross-Encoder NLI — entailment, neutral, contradiction probabilities
    nli_scores = nli_model.predict([(fde_text, ksa_text)])[0]
    nli_entailment = float(nli_scores[0])  # label 0 = contradiction for this model
    nli_neutral = float(nli_scores[1])
    nli_contradiction = float(nli_scores[2])
    # For nli-deberta-v3-base: labels are [contradiction, entailment, neutral]
    # Correcting label order based on model card
    nli_result = {
        "contradiction": round(float(nli_scores[0]), 4),
        "entailment": round(float(nli_scores[1]), 4),
        "neutral": round(float(nli_scores[2]), 4)
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


def build_rationale_file(mapping: dict, scores: dict, bertscore_data: dict) -> dict:
    """Build the per-FDE rationale JSON per ADR-014 approved schema."""
    
    fde_id = mapping["fde_id"]
    
    # Determine strength: STS primary, rounded to nearest integer
    strength = round(scores["sts_strength_0_10"])
    
    # For "No relationship" entries, the strength should reflect the STS score
    # but we don't override — let the math speak
    
    rationale_json = {
        "strm_id": "STRM-001-ONET",
        "fde_id": fde_id,
        "_comment_nist_fields": "Fields below follow IR 8278Ar1 Section 3.2 OLIR template",
        "focal_document_element": fde_id,
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
                "final_strength_integer": strength
            },
            "secondary_methods": {
                "bertscore": {
                    "model": "roberta-large",
                    "description": "Token-level contextual embedding matching. Precision = FDE coverage of KSA tokens. Recall = KSA coverage by FDE tokens. F1 = harmonic mean.",
                    "precision": bertscore_data["precision"],
                    "recall": bertscore_data["recall"],
                    "f1": bertscore_data["f1"]
                },
                "nli_cross_encoder": {
                    "model": "cross-encoder/nli-deberta-v3-base",
                    "description": "Natural Language Inference. Classifies text pair as entailment, neutral, or contradiction. Indicates directional implication strength.",
                    "contradiction": scores["nli"]["contradiction"],
                    "entailment": scores["nli"]["entailment"],
                    "neutral": scores["nli"]["neutral"]
                },
                "biencoder_cosine": {
                    "model": "all-MiniLM-L6-v2",
                    "description": "Bi-encoder sentence embeddings with cosine similarity. Each text encoded independently; measures vector-space proximity.",
                    "cosine_similarity_0_1": scores["biencoder_cosine_0_1"]
                },
                "jaccard_token": {
                    "description": "Token-level Jaccard similarity (intersection/union of lowercased word tokens). Purely lexical baseline, hand-traceable.",
                    "similarity_0_1": scores["jaccard_token_0_1"]
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
    
    # Separate scored (have ref_id) vs no-relationship (no ref_id)
    scored_mappings = [m for m in mappings if m.get("ref_id")]
    norel_mappings = [m for m in mappings if not m.get("ref_id")]
    print(f"  {len(scored_mappings)} with relationships to score")
    print(f"  {len(norel_mappings)} with no relationship (strength = 0)\n")
    
    # ── Score all pairs with ref_id ──
    print("Scoring pairs with STS, NLI, Bi-Encoder, Jaccard...")
    all_scores = {}
    for i, m in enumerate(scored_mappings):
        fde_text = m["fde_description"]
        ksa_text = m["ref_statement"]
        scores = score_pair(fde_text, ksa_text)
        all_scores[m["fde_id"]] = scores
        if (i + 1) % 10 == 0:
            print(f"  Scored {i+1}/{len(scored_mappings)}")
    print(f"  Scored {len(scored_mappings)}/{len(scored_mappings)} — individual methods complete.\n")
    
    # ── BERTScore in batch (more efficient) ──
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
        bertscore_data[m["fde_id"]] = {
            "precision": round(float(P[i]), 4),
            "recall": round(float(R[i]), 4),
            "f1": round(float(F1[i]), 4)
        }
    print("BERTScore complete.\n")
    
    # ── Generate rationale files ──
    os.makedirs(RATIONALE_DIR, exist_ok=True)
    
    print("Generating per-FDE rationale files...")
    strength_values = []
    
    for m in mappings:
        fde_id = m["fde_id"]
        filename = fde_id.replace(".", "-") + ".json"
        filepath = os.path.join(RATIONALE_DIR, filename)
        
        if m.get("ref_id"):
            # Has a relationship — full scoring
            scores = all_scores[fde_id]
            bs = bertscore_data[fde_id]
            rationale = build_rationale_file(m, scores, bs)
            strength_values.append(rationale["strength_of_relationship"])
        else:
            # No relationship — strength is 0, minimal scoring
            rationale = {
                "strm_id": "STRM-001-ONET",
                "fde_id": fde_id,
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
    
    # ── Update strm_mapping.json strength values ──
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
        "strm_id": "STRM-001-ONET",
        "methodology": {
            "primary": {
                "name": "Cross-Encoder STS",
                "model": "cross-encoder/stsb-roberta-base",
                "role": "Generates strength_of_relationship integer (0-10)",
                "mapping": "raw_score (0-1) × 10, rounded to nearest integer"
            },
            "secondary": [
                {
                    "name": "BERTScore",
                    "model": "roberta-large",
                    "role": "Token-level audit trail (Precision, Recall, F1)"
                },
                {
                    "name": "NLI Cross-Encoder",
                    "model": "cross-encoder/nli-deberta-v3-base",
                    "role": "Directional implication classification (entailment/neutral/contradiction)"
                },
                {
                    "name": "Bi-Encoder Cosine",
                    "model": "all-MiniLM-L6-v2",
                    "role": "Independent embedding cosine similarity"
                },
                {
                    "name": "Jaccard Token",
                    "model": None,
                    "role": "Lexical baseline (word token intersection/union)"
                }
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
    
    # Stats by relationship type
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
            summary["statistics"]["strength_distribution"]["by_relationship_type"][rel] = {
                "count": len([m for m in norel_mappings if m["relationship"] == rel]),
                "mean": 0,
                "median": 0,
                "min": 0,
                "max": 0
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
            print(f"    {rel:<20} n={len(rel_s):>3}  mean={np.mean(rel_s):.1f}  range=[{np.min(rel_s):.1f}, {np.max(rel_s):.1f}]")
        else:
            n = len([m for m in norel_mappings if m["relationship"] == rel])
            print(f"    {rel:<20} n={n:>3}  strength=0 (out of scope)")
    
    print("\nDone.")


if __name__ == "__main__":
    main()
