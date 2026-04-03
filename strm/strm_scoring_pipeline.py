#!/usr/bin/env python3
"""
WIDAI Framework-Adaptive Exhaustive Scoring Pipeline
=====================================================
Reprocesses any STRM using domain-exhaustive scoring with SCF-calibrated
thresholds. Scores ALL elements against ALL 504 WIDAI KSAs.

Usage:
    python3 -u strm/strm_scoring_pipeline.py --strm nice
    python3 -u strm/strm_scoring_pipeline.py --strm dcwf
    python3 -u strm/strm_scoring_pipeline.py --strm ddat
    python3 -u strm/strm_scoring_pipeline.py --strm euaiact
    python3 -u strm/strm_scoring_pipeline.py --strm nistairm

Scoring: Cross-Encoder STS primary + BERTScore, NLI, Bi-Encoder, Jaccard
Classification: SCF STRM-calibrated thresholds
Strength: Discrete scale 3, 5, 8, 10
"""

import argparse
import json
import glob
import math
import os
import re
import sys
from collections import Counter, defaultdict
from datetime import date

import gc
import numpy as np
from sentence_transformers import CrossEncoder, SentenceTransformer, util
from bert_score import score as bertscore_fn

# ── Resolve paths relative to repo root ──
REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
KSA_DIR = os.path.join(REPO_ROOT, "ksas")
TODAY = date.today().isoformat()

# ── SCF-Calibrated Thresholds ──
THRESH_EQUAL = 0.82
THRESH_SUBSET = 0.70
THRESH_INTERSECT = 0.35
NLI_CONTRADICTION_GATE = 0.70

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


# ══════════════════════════════════════════════════════════════════
# Framework Configurations
# ══════════════════════════════════════════════════════════════════

FRAMEWORK_CONFIGS = {
    "nice": {
        "strm_id": "STRM-002-NICE",
        "framework_name": "NIST NICE Framework v2.1.0 (SP 800-181)",
        "framework_source": "National Initiative for Cybersecurity Education",
        "widai_version": "0.5.9",
        "rationale_type": "Semantic",
        "source_file": "sources/nice_framework/cprt_SP_800_181_2_1_0.json",
        "strm_dir": "strm/nice",
    },
    "dcwf": {
        "strm_id": "STRM-003-DCWF",
        "framework_name": "DoD Cyber Workforce Framework v5.1",
        "framework_source": "Department of Defense",
        "widai_version": "0.5.9",
        "rationale_type": "Semantic",
        "source_file": "sources/dcwf/dcwf_elements.json",
        "strm_dir": "strm/dcwf",
    },
    "ddat": {
        "strm_id": "STRM-004-DDAT",
        "framework_name": "UK Digital, Data and Technology Capability Framework",
        "framework_source": "UK Government Digital Service",
        "widai_version": "0.5.9",
        "rationale_type": "Semantic",
        "source_file": "sources/ddat/ddat_elements.json",
        "strm_dir": "strm/ddat",
    },
    "euaiact": {
        "strm_id": "STRM-005-EU-AI-ACT",
        "framework_name": "EU AI Act (Regulation (EU) 2024/1689)",
        "framework_source": "European Parliament and Council",
        "widai_version": "0.5.9",
        "rationale_type": "Functional",
        "source_file": "sources/eu_ai_act/eu_ai_act_elements.json",
        "strm_dir": "strm/eu_ai_act",
    },
    "nistairm": {
        "strm_id": "STRM-006-NIST-AI-RMF",
        "framework_name": "NIST AI Risk Management Framework 1.0 (AI 100-1)",
        "framework_source": "National Institute of Standards and Technology",
        "widai_version": "0.5.9",
        "rationale_type": "Functional",
        "source_file": "sources/nist_ai_rmf/nist_ai_rmf_elements.json",
        "strm_dir": "strm/nist_ai_rmf",
    },
}


# ══════════════════════════════════════════════════════════════════
# Element Loaders (framework-specific)
# ══════════════════════════════════════════════════════════════════

def load_nice_elements(filepath):
    """Load NICE TKS elements (tasks, knowledge, skills)."""
    with open(filepath) as f:
        data = json.load(f)
    raw = data["response"]["elements"]["elements"]
    elements = []
    for e in raw:
        if e["element_type"] in ("task", "knowledge", "skill"):
            elements.append({
                "fde_id": e["element_identifier"],
                "fde_name": e.get("title", ""),
                "fde_type": e["element_type"],
                "scoring_text": e["text"],
                "extra": {},
            })
    return elements


def load_dcwf_elements(filepath):
    """Load DCWF KSAT elements."""
    with open(filepath) as f:
        data = json.load(f)
    elements = []
    for e in data["elements"]:
        elements.append({
            "fde_id": e["dcwf_id"],
            "fde_name": "",
            "fde_type": e["element_type"].lower(),
            "scoring_text": e["description"],
            "extra": {
                "base_id": e.get("base_id"),
                "variant": e.get("variant"),
            },
        })
    return elements


def load_ddat_elements(filepath):
    """Load DDaT skill elements."""
    with open(filepath) as f:
        data = json.load(f)
    elements = []
    for e in data["skills"]:
        elements.append({
            "fde_id": e["ddat_id"],
            "fde_name": e["skill_name"],
            "fde_type": e.get("element_type", "skill"),
            "scoring_text": e["description"],
            "extra": {},
        })
    return elements


def load_euaiact_elements(filepath):
    """Load EU AI Act elements. Scoring uses competency_implication."""
    with open(filepath) as f:
        data = json.load(f)
    elements = []
    for e in data["elements"]:
        elements.append({
            "fde_id": e["element_id"],
            "fde_name": e.get("article_title", ""),
            "fde_type": e["element_type"],
            "scoring_text": e["competency_implication"],
            "extra": {
                "article": e.get("article"),
                "article_title": e.get("article_title"),
                "obligation_text": e.get("obligation_text"),
                "applies_to": e.get("applies_to"),
                "risk_category": e.get("risk_category"),
                "enforcement_date": e.get("enforcement_date"),
            },
        })
    return elements


def load_nistairm_elements(filepath):
    """Load NIST AI RMF elements. Scoring uses competency_implication."""
    with open(filepath) as f:
        data = json.load(f)
    elements = []
    for e in data["elements"]:
        elements.append({
            "fde_id": e["element_id"],
            "fde_name": e.get("category_title", ""),
            "fde_type": e["element_type"],
            "scoring_text": e["competency_implication"],
            "extra": {
                "function": e.get("function"),
                "category": e.get("category"),
                "subcategory_id": e.get("subcategory_id"),
                "outcome_text": e.get("outcome_text"),
                "applies_to": e.get("applies_to"),
                "function_description": e.get("function_description"),
            },
        })
    return elements


ELEMENT_LOADERS = {
    "nice": load_nice_elements,
    "dcwf": load_dcwf_elements,
    "ddat": load_ddat_elements,
    "euaiact": load_euaiact_elements,
    "nistairm": load_nistairm_elements,
}


# ══════════════════════════════════════════════════════════════════
# Shared Utilities
# ══════════════════════════════════════════════════════════════════

def load_widai_ksas():
    """Load all WIDAI KSAs from type-separated domain files."""
    all_ksas = []
    for fp in sorted(glob.glob(os.path.join(KSA_DIR, "*_knowledge.json")) +
                     glob.glob(os.path.join(KSA_DIR, "*_skills.json")) +
                     glob.glob(os.path.join(KSA_DIR, "*_tasks.json")) +
                     glob.glob(os.path.join(KSA_DIR, "*_abilities.json"))):
        with open(fp) as f:
            data = json.load(f)
        for item in data["entries"]:
            all_ksas.append({
                "id": item["ksa_id"],
                "type": item["type"],
                "statement": item["statement"],
                "domain": item["domain_code"],
            })
    return all_ksas


def softmax(logits):
    """Convert raw logits to probabilities."""
    exp_logits = [math.exp(x) for x in logits]
    total = sum(exp_logits)
    return [x / total for x in exp_logits]


def jaccard(text_a, text_b):
    """Token-level Jaccard similarity."""
    a = set(re.findall(r'\b\w+\b', text_a.lower())) - STOPWORDS
    b = set(re.findall(r'\b\w+\b', text_b.lower())) - STOPWORDS
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


def classify(sts_raw, nli_probs):
    """Classify relationship using SCF-calibrated thresholds + NLI gate."""
    contradiction = nli_probs[0]
    if sts_raw >= THRESH_EQUAL and contradiction <= NLI_CONTRADICTION_GATE:
        return "Equal"
    if sts_raw >= THRESH_SUBSET and contradiction <= NLI_CONTRADICTION_GATE:
        return "Subset Of"
    if sts_raw >= THRESH_INTERSECT:
        return "Intersects With"
    return "No Relationship"


def discrete_strength(sts_raw):
    """Map STS raw to discrete SCF-aligned strength."""
    if sts_raw >= THRESH_EQUAL:
        return 10
    if sts_raw >= THRESH_SUBSET:
        return 8
    if sts_raw >= 0.45:
        return 5
    if sts_raw >= THRESH_INTERSECT:
        return 3
    return 0


# ══════════════════════════════════════════════════════════════════
# Core Scoring Engine
# ══════════════════════════════════════════════════════════════════

def run_pipeline(framework_key):
    """Run exhaustive scoring pipeline for the given framework."""
    config = FRAMEWORK_CONFIGS[framework_key]
    strm_id = config["strm_id"]
    strm_dir = os.path.join(REPO_ROOT, config["strm_dir"])
    source_file = os.path.join(REPO_ROOT, config["source_file"])
    rationale_type = config["rationale_type"]

    mapping_file = os.path.join(strm_dir, "strm_mapping.json")
    rationale_dir = os.path.join(strm_dir, "rationale")
    summary_file = os.path.join(strm_dir, "scoring_summary.json")

    print(f"{'='*60}", flush=True)
    print(f"{strm_id} EXHAUSTIVE SCORING PIPELINE", flush=True)
    print(f"Framework: {config['framework_name']}", flush=True)
    print(f"{'='*60}\n", flush=True)

    # ── Load elements ──
    print("Loading framework elements...", flush=True)
    loader = ELEMENT_LOADERS[framework_key]
    elements = loader(source_file)
    type_counts = Counter(e["fde_type"] for e in elements)
    print(f"  {len(elements)} elements ({', '.join(f'{k}: {v}' for k, v in type_counts.items())})", flush=True)

    # ── Load KSAs ──
    print("Loading WIDAI KSAs...", flush=True)
    ksas = load_widai_ksas()
    domain_counts = Counter(k["domain"] for k in ksas)
    print(f"  {len(ksas)} KSAs across {len(domain_counts)} domains", flush=True)

    # ── Build ALL pairs ──
    print("\nBuilding pair list (all elements x all KSAs)...", flush=True)
    pairs = []         # (scoring_text, ksa_statement)
    pair_meta = []     # (element_index, ksa_index)
    for ei, elem in enumerate(elements):
        for ki, ksa in enumerate(ksas):
            pairs.append((elem["scoring_text"], ksa["statement"]))
            pair_meta.append((ei, ki))

    total_pairs = len(pairs)
    print(f"  Total pairs: {total_pairs:,} ({len(elements)} elements x {len(ksas)} KSAs)", flush=True)

    # ── Score ALL pairs (sequential model loading to manage memory) ──
    print(f"\nScoring {total_pairs:,} pairs...", flush=True)

    # Phase 1: STS scoring
    print("  [1/5] Loading Cross-Encoder STS...", flush=True)
    sts_model = CrossEncoder('cross-encoder/stsb-roberta-base')
    print("  STS scoring...", flush=True)
    sts_scores = sts_model.predict(pairs, batch_size=128, show_progress_bar=True)
    sts_scores = [float(s) for s in sts_scores]
    del sts_model; gc.collect()
    print("  STS complete, model freed.", flush=True)

    # Phase 2: NLI scoring (batch_size=32 — DeBERTa is memory-heavy)
    print("  [2/5] Loading Cross-Encoder NLI...", flush=True)
    nli_model = CrossEncoder('cross-encoder/nli-deberta-v3-base')
    print("  NLI scoring...", flush=True)
    nli_raw = nli_model.predict(pairs, batch_size=32, show_progress_bar=True)
    nli_probs_all = [softmax(logits.tolist()) for logits in nli_raw]
    del nli_model, nli_raw; gc.collect()
    print("  NLI complete, model freed.", flush=True)

    # Phase 3: Bi-encoder scoring
    print("  [3/5] Loading Bi-Encoder...", flush=True)
    bienc_model = SentenceTransformer('all-MiniLM-L6-v2')
    print("  Encoding KSA statements...", flush=True)
    ksa_statements = [k["statement"] for k in ksas]
    ksa_embeddings = bienc_model.encode(ksa_statements, batch_size=64, show_progress_bar=True)
    print("  Encoding element texts...", flush=True)
    elem_texts = [elem["scoring_text"] for elem in elements]
    elem_embeddings = bienc_model.encode(elem_texts, batch_size=64, show_progress_bar=True)
    # Compute per-pair cosine from pre-encoded embeddings
    bienc_scores = []
    for ei, ki in pair_meta:
        sim = float(util.cos_sim(elem_embeddings[ei], ksa_embeddings[ki])[0][0])
        bienc_scores.append(sim)
    del bienc_model, ksa_embeddings, elem_embeddings; gc.collect()
    print("  Bi-encoder complete, model freed.", flush=True)

    # Phase 4: Jaccard scoring (no model needed)
    print("  [4/5] Jaccard scoring...", flush=True)
    jaccard_scores = []
    for p in pairs:
        jaccard_scores.append(jaccard(p[0], p[1]))

    # Phase 5: BERTScore
    print("  [5/5] BERTScore...", flush=True)
    refs = [p[0] for p in pairs]
    cands = [p[1] for p in pairs]
    P, R, F1 = bertscore_fn(cands, refs, lang="en", verbose=True)
    bert_p = [float(x) for x in P]
    bert_r = [float(x) for x in R]
    bert_f1 = [float(x) for x in F1]
    del P, R, F1; gc.collect()

    print("\nAll scoring complete.\n", flush=True)

    # ── Classify and build output ──
    print("Classifying relationships and building output...", flush=True)

    # Clear and recreate rationale directory
    os.makedirs(rationale_dir, exist_ok=True)
    for old_f in glob.glob(os.path.join(rationale_dir, "*.json")):
        os.remove(old_f)

    mappings = []
    rationale_count = 0

    for idx in range(total_pairs):
        ei, ki = pair_meta[idx]
        elem = elements[ei]
        ksa = ksas[ki]
        sts_raw = sts_scores[idx]
        nli_probs = nli_probs_all[idx]
        bienc = bienc_scores[idx]
        jacc = jaccard_scores[idx]
        bp, br, bf = bert_p[idx], bert_r[idx], bert_f1[idx]

        relationship = classify(sts_raw, nli_probs)
        strength = discrete_strength(sts_raw)

        if relationship == "No Relationship":
            continue  # Only record qualifying matches

        # ── Mapping row ──
        mappings.append({
            "fde_id": elem["fde_id"],
            "fde_name": elem["fde_name"],
            "fde_description": elem["scoring_text"],
            "rationale": rationale_type,
            "relationship": relationship,
            "ref_id": ksa["id"],
            "ref_domain": ksa["domain"],
            "ref_statement": ksa["statement"],
            "strength": strength,
            "sts_raw": round(sts_raw, 4),
            "bienc_score": round(bienc, 4),
        })

        # ── Rationale file ──
        safe_fde = re.sub(r'[^\w\-]', '_', elem["fde_id"])
        safe_ksa = re.sub(r'[^\w\-]', '_', ksa["id"])
        rat_filename = f"{safe_fde}_{safe_ksa}.json"

        rationale_obj = {
            "strm_id": strm_id,
            "pipeline_version": "domain-exhaustive",
            "fde_id": elem["fde_id"],
            "fde_name": elem["fde_name"],
            "fde_type": elem["fde_type"],
            "focal_document_element": elem["fde_id"],
            "focal_document_element_description": elem["scoring_text"],
            "rationale": rationale_type,
            "relationship": relationship,
            "reference_document_element": ksa["id"],
            "reference_document_element_description": ksa["statement"],
            "strength_of_relationship": strength,
            "strength_justification": {
                "methodology": f"Multi-method computational scoring (domain-exhaustive, SCF-calibrated)",
                "candidate_selection": "Exhaustive — all KSAs scored through cross-encoder",
                "discrete_scale": "SCF-aligned: 3, 5, 8, 10",
                "primary_method": {
                    "name": "Cross-Encoder STS",
                    "model": "cross-encoder/stsb-roberta-base",
                    "raw_score_0_1": round(sts_raw, 4),
                    "mapped_strength": strength,
                },
                "secondary_methods": {
                    "bertscore": {
                        "model": "roberta-large",
                        "precision": round(bp, 4),
                        "recall": round(br, 4),
                        "f1": round(bf, 4),
                    },
                    "nli_cross_encoder": {
                        "model": "cross-encoder/nli-deberta-v3-base",
                        "contradiction": round(nli_probs[0], 4),
                        "entailment": round(nli_probs[1], 4),
                        "neutral": round(nli_probs[2], 4),
                    },
                    "biencoder_cosine": {
                        "model": "all-MiniLM-L6-v2",
                        "cosine_similarity": round(bienc, 4),
                    },
                    "jaccard_token": {
                        "similarity": round(jacc, 4),
                    },
                },
                "classification_thresholds": {
                    "equal": ">= 0.82",
                    "subset_of": ">= 0.7",
                    "intersects_with": ">= 0.35",
                    "no_relationship": "< 0.35",
                    "nli_contradiction_gate": "> 0.7",
                },
            },
            "gap_signal": None,
            "evaluated_by": "AI-assisted (Claude) with human review",
            "evaluation_date": TODAY,
        }

        # Add framework-specific extra fields to rationale
        if elem["extra"]:
            rationale_obj["framework_metadata"] = elem["extra"]

        with open(os.path.join(rationale_dir, rat_filename), 'w') as f:
            json.dump(rationale_obj, f, indent=2)
        rationale_count += 1

    # ── Handle No Relationship elements ──
    # Elements where NO KSA cleared the threshold
    mapped_fde_ids = set(m["fde_id"] for m in mappings)
    nr_elements = [e for e in elements if e["fde_id"] not in mapped_fde_ids]

    for elem in nr_elements:
        # Find the best STS score for this element across all KSAs
        ei = elements.index(elem)
        start_idx = ei * len(ksas)
        end_idx = start_idx + len(ksas)
        elem_sts = sts_scores[start_idx:end_idx]
        best_ki = int(np.argmax(elem_sts))
        best_sts = elem_sts[best_ki]
        best_ksa = ksas[best_ki]

        mappings.append({
            "fde_id": elem["fde_id"],
            "fde_name": elem["fde_name"],
            "fde_description": elem["scoring_text"],
            "rationale": rationale_type,
            "relationship": "No Relationship",
            "ref_id": None,
            "ref_domain": None,
            "ref_statement": None,
            "strength": 0,
            "sts_raw": round(best_sts, 4),
            "bienc_score": 0,
        })

        # Write No Relationship rationale
        safe_fde = re.sub(r'[^\w\-]', '_', elem["fde_id"])
        rat_filename = f"{safe_fde}_NO_RELATIONSHIP.json"
        rationale_obj = {
            "strm_id": strm_id,
            "pipeline_version": "domain-exhaustive",
            "fde_id": elem["fde_id"],
            "fde_name": elem["fde_name"],
            "fde_type": elem["fde_type"],
            "focal_document_element": elem["fde_id"],
            "focal_document_element_description": elem["scoring_text"],
            "rationale": rationale_type,
            "relationship": "No Relationship",
            "reference_document_element": None,
            "reference_document_element_description": None,
            "strength_of_relationship": 0,
            "strength_justification": {
                "methodology": "Multi-method computational scoring (domain-exhaustive, SCF-calibrated)",
                "best_candidate": {
                    "ksa_id": best_ksa["id"],
                    "domain": best_ksa["domain"],
                    "sts_raw": round(best_sts, 4),
                },
                "classification_thresholds": {
                    "intersects_with": ">= 0.35",
                    "no_relationship": "< 0.35",
                },
                "note": f"Best STS score {best_sts:.4f} below Intersects With threshold (0.35). All {len(ksas)} KSAs evaluated.",
            },
            "gap_signal": None,
            "evaluated_by": "AI-assisted (Claude) with human review",
            "evaluation_date": TODAY,
        }
        if elem["extra"]:
            rationale_obj["framework_metadata"] = elem["extra"]

        with open(os.path.join(rationale_dir, rat_filename), 'w') as f:
            json.dump(rationale_obj, f, indent=2)
        rationale_count += 1

    print(f"  {rationale_count} rationale files written", flush=True)
    print(f"  {len(mappings)} total mapping rows", flush=True)

    # ── Sort mappings by FDE then by strength descending ──
    mappings.sort(key=lambda m: (m["fde_id"], -m["strength"], -(m["sts_raw"] or 0)))

    # ── Write mapping file ──
    scored = [m for m in mappings if m["relationship"] != "No Relationship"]
    nr = [m for m in mappings if m["relationship"] == "No Relationship"]
    unique_ksas = set(m["ref_id"] for m in scored)
    unique_fdes_scored = set(m["fde_id"] for m in scored)
    domain_dist = Counter(m["ref_domain"] for m in scored)

    strm_data = {
        "strm_id": strm_id,
        "framework": config["framework_name"],
        "framework_source": config["framework_source"],
        "widai_version": config["widai_version"],
        "pipeline_version": "domain-exhaustive",
        "scoring_methodology": (
            "Exhaustive scoring — all elements scored against all WIDAI KSAs. "
            "Cross-Encoder STS primary with SCF-calibrated thresholds. "
            "NLI contradiction gate. Discrete strength scale (3, 5, 8, 10)."
        ),
        "rationale_type": rationale_type,
        "total_fdes": len(elements),
        "mapping_date": TODAY,
        "mappings": mappings,
    }

    with open(mapping_file, 'w') as f:
        json.dump(strm_data, f, indent=2)
    print(f"\nMapping file: {mapping_file}", flush=True)

    # ── Write scoring summary ──
    sts_scored = [m["sts_raw"] for m in scored]
    strength_dist = Counter(m["strength"] for m in mappings)
    rel_dist = Counter(m["relationship"] for m in mappings)

    summary = {
        "pipeline_run_date": TODAY,
        "strm_id": strm_id,
        "pipeline_version": "domain-exhaustive",
        "methodology": {
            "approach": "Exhaustive scoring — all elements against all KSAs",
            "total_pairs_scored": total_pairs,
            "note": f"{len(elements)} elements x {len(ksas)} KSAs = {total_pairs:,} pairs",
        },
        "statistics": {
            "total_fdes": len(elements),
            "total_mapping_rows": len(mappings),
            "scored_mappings": len(scored),
            "no_relationship_fdes": len(nr),
            "unique_ksas_matched": len(unique_ksas),
            "rationale_files": rationale_count,
            "relationship_distribution": dict(rel_dist),
            "strength_distribution": {str(k): v for k, v in sorted(strength_dist.items())},
            "domain_distribution": dict(sorted(domain_dist.items(), key=lambda x: -x[1])),
            "sts_statistics_scored": {
                "count": len(sts_scored),
                "mean": round(float(np.mean(sts_scored)), 4) if sts_scored else 0,
                "median": round(float(np.median(sts_scored)), 4) if sts_scored else 0,
                "std": round(float(np.std(sts_scored)), 4) if sts_scored else 0,
                "min": round(min(sts_scored), 4) if sts_scored else 0,
                "max": round(max(sts_scored), 4) if sts_scored else 0,
            },
        },
    }

    with open(summary_file, 'w') as f:
        json.dump(summary, f, indent=2)
    print(f"Summary file: {summary_file}", flush=True)

    # ── Print results ──
    print(f"\n{'='*60}", flush=True)
    print(f"PIPELINE COMPLETE — {strm_id}", flush=True)
    print(f"{'='*60}", flush=True)
    print(f"  Elements:          {len(elements)}", flush=True)
    print(f"  Pairs scored:      {total_pairs:,}", flush=True)
    print(f"  Mapping rows:      {len(mappings)}", flush=True)
    print(f"  Scored mappings:   {len(scored)}", flush=True)
    print(f"  No Relationship:   {len(nr)}", flush=True)
    print(f"  Unique KSAs:       {len(unique_ksas)}", flush=True)
    print(f"  Rationale files:   {rationale_count}", flush=True)
    print(f"  Strength dist:     {dict(sorted(strength_dist.items()))}", flush=True)
    print(f"  Relationship dist: {dict(rel_dist)}", flush=True)
    if sts_scored:
        print(f"  STS mean (scored): {np.mean(sts_scored):.4f}", flush=True)
    print(f"\nDone.", flush=True)


# ══════════════════════════════════════════════════════════════════
# Main
# ══════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="WIDAI Exhaustive STRM Scoring Pipeline")
    parser.add_argument("--strm", required=True, choices=list(FRAMEWORK_CONFIGS.keys()),
                        help="Framework to process")
    args = parser.parse_args()
    run_pipeline(args.strm)
