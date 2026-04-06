#!/usr/bin/env python3
"""
AB Knowledge High Watermark Analysis
Find which framework contributes the most DISTINCT knowledge-level elements
that map to AB-K territory. This becomes the target KSA count.
"""
import json
from pathlib import Path
from collections import defaultdict

BASE_DIR = Path(__file__).resolve().parent.parent
STRM_DIR = BASE_DIR / "strm"
KSA_FILE = BASE_DIR / "ksas" / "AB_knowledge.json"

FRAMEWORKS = ["onet", "nice", "dcwf", "ddat", "eu_ai_act", "nist_ai_rmf"]
FW_LABELS = {
    "onet": "O*NET 30.2",
    "nice": "NIST NICE v2.1.0",
    "dcwf": "DoD DCWF v5.1",
    "ddat": "DDaT",
    "eu_ai_act": "EU AI Act",
    "nist_ai_rmf": "NIST AI RMF 1.0",
}

with open(KSA_FILE) as f:
    ksa_data = json.load(f)
ab_ksas = {e["ksa_id"]: e["statement"] for e in ksa_data["entries"]}

# For each framework: collect unique FDEs that mapped to AB-K
# Filter to meaningful matches (STS >= 0.45 — above weak/noise)
# Then cluster by DISTINCT concepts (not just element count)

STS_FLOOR = 0.45  # Above noise floor

for fw in FRAMEWORKS:
    mapping_file = STRM_DIR / fw / "strm_mapping.json"
    if not mapping_file.exists():
        continue

    print(f"\n{'='*100}")
    print(f"FRAMEWORK: {FW_LABELS[fw]}")
    print(f"{'='*100}")

    with open(mapping_file) as f:
        data = json.load(f)

    # Collect unique FDEs that map to AB-K at meaningful STS
    fde_map = {}  # fde_id -> best match info
    for m in data["mappings"]:
        ref_id = m.get("ref_id") or ""
        if not ref_id.startswith("AB-K-"):
            continue
        sts = m.get("sts_raw") or m.get("primary_score") or 0
        if sts < STS_FLOOR:
            continue

        fde_id = m.get("fde_id")
        fde_name = m.get("fde_name") or ""
        fde_desc = m.get("fde_description") or ""

        if fde_id not in fde_map or sts > fde_map[fde_id]["best_sts"]:
            fde_map[fde_id] = {
                "fde_id": fde_id,
                "fde_name": fde_name,
                "fde_desc": fde_desc,
                "best_sts": sts,
                "best_ksa": ref_id,
                "ksa_matches": set(),
            }
        fde_map[fde_id]["ksa_matches"].add(ref_id)

    # Sort by STS descending
    fdes_sorted = sorted(fde_map.values(), key=lambda x: x["best_sts"], reverse=True)

    print(f"Unique FDEs with STS >= {STS_FLOOR} against AB-K: {len(fdes_sorted)}")
    print(f"\nTop 40 (by best STS):")
    for i, fde in enumerate(fdes_sorted[:40]):
        desc = fde["fde_desc"][:100] if fde["fde_desc"] else fde["fde_name"][:100]
        print(f"  {i+1:>3}. STS={fde['best_sts']:.4f} [{fde['fde_id']}] {desc}")
        print(f"       Maps to: {', '.join(sorted(fde['ksa_matches']))}")

    del data

# Now do cross-framework: unique CONCEPTS (deduplicated by description similarity)
print("\n" + "=" * 100)
print("CROSS-FRAMEWORK SUMMARY — Unique FDE count per framework at STS >= 0.45")
print("=" * 100)

totals = {}
for fw in FRAMEWORKS:
    mapping_file = STRM_DIR / fw / "strm_mapping.json"
    if not mapping_file.exists():
        continue
    with open(mapping_file) as f:
        data = json.load(f)

    unique_fdes = set()
    unique_fdes_50 = set()
    unique_fdes_55 = set()
    unique_fdes_60 = set()
    for m in data["mappings"]:
        ref_id = m.get("ref_id") or ""
        if not ref_id.startswith("AB-K-"):
            continue
        sts = m.get("sts_raw") or m.get("primary_score") or 0
        fde_id = m.get("fde_id")
        if sts >= 0.45:
            unique_fdes.add(fde_id)
        if sts >= 0.50:
            unique_fdes_50.add(fde_id)
        if sts >= 0.55:
            unique_fdes_55.add(fde_id)
        if sts >= 0.60:
            unique_fdes_60.add(fde_id)

    totals[fw] = {
        "gte_45": len(unique_fdes),
        "gte_50": len(unique_fdes_50),
        "gte_55": len(unique_fdes_55),
        "gte_60": len(unique_fdes_60),
    }
    del data

print(f"\n{'Framework':<25} {'>=0.45':>8} {'>=0.50':>8} {'>=0.55':>8} {'>=0.60':>8}")
print("-" * 60)
for fw in FRAMEWORKS:
    t = totals.get(fw, {})
    print(f"{FW_LABELS[fw]:<25} {t.get('gte_45',0):>8} {t.get('gte_50',0):>8} {t.get('gte_55',0):>8} {t.get('gte_60',0):>8}")

# High watermark
hw_45 = max(totals.values(), key=lambda x: x["gte_45"])
hw_50 = max(totals.values(), key=lambda x: x["gte_50"])
hw_fw_45 = [fw for fw in FRAMEWORKS if totals.get(fw, {}).get("gte_45") == hw_45["gte_45"]][0]
hw_fw_50 = [fw for fw in FRAMEWORKS if totals.get(fw, {}).get("gte_50") == hw_50["gte_50"]][0]
print(f"\nHigh watermark at >= 0.45: {FW_LABELS[hw_fw_45]} with {hw_45['gte_45']} unique FDEs")
print(f"High watermark at >= 0.50: {FW_LABELS[hw_fw_50]} with {hw_50['gte_50']} unique FDEs")
