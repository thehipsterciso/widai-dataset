#!/usr/bin/env python3
"""
Generate bi-encoder candidate identifications for EU AI Act elements.

For each element, encodes the competency_implication text and finds the
top-5 most similar WIDAI KSAs by cosine similarity using all-MiniLM-L6-v2.

Output: eu_ai_act_candidates.json
"""

import json
import os
import glob

from sentence_transformers import SentenceTransformer, util

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
ELEMENTS_FILE = os.path.join(os.path.dirname(__file__), "eu_ai_act_elements.json")
KSA_DIR = os.path.join(REPO_ROOT, "ksas")
OUTPUT_FILE = os.path.join(os.path.dirname(__file__), "eu_ai_act_candidates.json")


def load_elements():
    with open(ELEMENTS_FILE) as f:
        data = json.load(f)
    return data["elements"]


def load_widai_ksas():
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


def main():
    print("Loading EU AI Act elements...", flush=True)
    elements = load_elements()
    print(f"  {len(elements)} elements loaded.", flush=True)

    print("Loading WIDAI KSAs...", flush=True)
    ksas = load_widai_ksas()
    print(f"  {len(ksas)} KSAs loaded.", flush=True)

    print("Loading bi-encoder model (all-MiniLM-L6-v2)...", flush=True)
    model = SentenceTransformer('all-MiniLM-L6-v2')

    print("Encoding WIDAI KSAs...", flush=True)
    ksa_texts = [k["statement"] for k in ksas]
    ksa_embeddings = model.encode(ksa_texts, convert_to_tensor=True, show_progress_bar=True)

    print("Encoding EU AI Act elements (competency_implication)...", flush=True)
    element_texts = [e["competency_implication"] for e in elements]
    element_embeddings = model.encode(element_texts, convert_to_tensor=True, show_progress_bar=True)

    print("Computing cosine similarities and identifying top-5 candidates...", flush=True)
    candidates = []
    for i, element in enumerate(elements):
        cos_scores = util.cos_sim(element_embeddings[i], ksa_embeddings)[0]
        top_k_indices = cos_scores.argsort(descending=True)[:5]

        cand_list = []
        for idx in top_k_indices:
            idx = int(idx)
            cand_list.append({
                "ksa_id": ksas[idx]["id"],
                "domain_code": ksas[idx]["domain"],
                "statement": ksas[idx]["statement"],
                "cosine_similarity": round(float(cos_scores[idx]), 4)
            })

        candidates.append({
            "element_id": element["element_id"],
            "element_type": element["element_type"],
            "article": element["article"],
            "competency_implication": element["competency_implication"],
            "candidates": cand_list
        })

    output = {
        "strm_id": "STRM-005-EU-AI-ACT",
        "model": "all-MiniLM-L6-v2",
        "widai_ksa_count": len(ksas),
        "element_count": len(elements),
        "top_k": 5,
        "total_pairs_evaluated": len(elements) * len(ksas),
        "candidates": candidates
    }

    with open(OUTPUT_FILE, 'w') as f:
        json.dump(output, f, indent=2)

    print(f"\nCandidates written to {OUTPUT_FILE}", flush=True)
    print(f"  {len(candidates)} elements × {len(ksas)} KSAs = "
          f"{len(elements) * len(ksas):,} pairs evaluated", flush=True)
    print("Done.", flush=True)


if __name__ == "__main__":
    main()
