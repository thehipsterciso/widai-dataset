#!/usr/bin/env python3
"""
AB Knowledge Concept Clustering
Take the NICE K-elements that map to AB-K at STS >= 0.50,
strip the cybersecurity-specific noise, and identify distinct
analytics/BI knowledge concepts.
"""
import json
from pathlib import Path
from collections import defaultdict

BASE_DIR = Path(__file__).resolve().parent.parent
STRM_DIR = BASE_DIR / "strm"

# Load NICE mapping, extract K-elements that hit AB-K
with open(STRM_DIR / "nice" / "strm_mapping.json") as f:
    nice = json.load(f)

# Collect NICE K-elements with meaningful AB-K matches
k_elements = {}
for m in nice["mappings"]:
    ref_id = m.get("ref_id") or ""
    if not ref_id.startswith("AB-K-"):
        continue
    fde_id = m.get("fde_id", "")
    if not fde_id.startswith("K"):  # Only knowledge elements
        continue
    sts = m.get("sts_raw") or 0
    if sts < 0.50:
        continue

    if fde_id not in k_elements:
        k_elements[fde_id] = {
            "id": fde_id,
            "desc": m.get("fde_description") or m.get("fde_name") or "",
            "best_sts": sts,
            "ksa_matches": set(),
        }
    if sts > k_elements[fde_id]["best_sts"]:
        k_elements[fde_id]["best_sts"] = sts
    k_elements[fde_id]["ksa_matches"].add(ref_id)

del nice

print(f"NICE K-elements with STS >= 0.50 against AB-K: {len(k_elements)}")
print()

# Sort by STS
sorted_ks = sorted(k_elements.values(), key=lambda x: x["best_sts"], reverse=True)

# Print all for manual clustering analysis
print("ALL NICE K-ELEMENTS MAPPING TO AB-K AT STS >= 0.50")
print("=" * 100)
for i, k in enumerate(sorted_ks):
    ksas = ", ".join(sorted(k["ksa_matches"]))
    print(f"{i+1:>3}. STS={k['best_sts']:.4f} [{k['id']}] {k['desc']}")
    print(f"     -> {ksas}")

# Now do the same for DCWF but only knowledge-typed elements
print("\n\n")
with open(STRM_DIR / "dcwf" / "strm_mapping.json") as f:
    dcwf = json.load(f)

dcwf_elements = {}
for m in dcwf["mappings"]:
    ref_id = m.get("ref_id") or ""
    if not ref_id.startswith("AB-K-"):
        continue
    fde_id = m.get("fde_id", "")
    fde_desc = m.get("fde_description") or m.get("fde_name") or ""
    sts = m.get("sts_raw") or 0
    if sts < 0.50:
        continue
    # DCWF doesn't have K-prefix, but filter to "Knowledge of" descriptions
    if not fde_desc.lower().startswith("knowledge of"):
        continue

    if fde_id not in dcwf_elements:
        dcwf_elements[fde_id] = {
            "id": fde_id,
            "desc": fde_desc,
            "best_sts": sts,
            "ksa_matches": set(),
        }
    if sts > dcwf_elements[fde_id]["best_sts"]:
        dcwf_elements[fde_id]["best_sts"] = sts
    dcwf_elements[fde_id]["ksa_matches"].add(ref_id)

del dcwf

sorted_dcwf = sorted(dcwf_elements.values(), key=lambda x: x["best_sts"], reverse=True)
print(f"DCWF 'Knowledge of' elements with STS >= 0.50 against AB-K: {len(sorted_dcwf)}")
print("=" * 100)
for i, k in enumerate(sorted_dcwf):
    ksas = ", ".join(sorted(k["ksa_matches"]))
    print(f"{i+1:>3}. STS={k['best_sts']:.4f} [{k['id']}] {k['desc'][:120]}")
    print(f"     -> {ksas}")

# Summary
print(f"\n\nSUMMARY")
print(f"NICE K-elements at STS >= 0.50: {len(k_elements)}")
print(f"DCWF Knowledge elements at STS >= 0.50: {len(dcwf_elements)}")
print(f"Combined unique knowledge concepts: needs manual clustering")
