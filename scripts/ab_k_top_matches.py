#!/usr/bin/env python3
"""
AB Knowledge — Top Match Analysis
Find the highest-STS matches per KSA to understand why no strong classifications.
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

# Collect ALL AB-K mappings with full detail
all_matches = []
for fw in FRAMEWORKS:
    mapping_file = STRM_DIR / fw / "strm_mapping.json"
    if not mapping_file.exists():
        continue
    with open(mapping_file) as f:
        data = json.load(f)
    for m in data["mappings"]:
        ref_id = m.get("ref_id") or ""
        if ref_id.startswith("AB-K-"):
            all_matches.append({
                "ksa_id": ref_id,
                "framework": fw,
                "fde_id": m.get("fde_id"),
                "fde_name": m.get("fde_name"),
                "fde_description": m.get("fde_description", ""),
                "relationship": m.get("relationship"),
                "strength": m.get("strength"),
                "sts_raw": m.get("sts_raw") or m.get("primary_score") or 0,
            })
    del data

print(f"Total AB-K matches across all frameworks: {len(all_matches)}")

# Top 10 matches per KSA
print("\n" + "=" * 100)
print("TOP 10 MATCHES PER KSA (by STS score)")
print("=" * 100)

for ksa_id in sorted(ab_ksas.keys()):
    ksa_matches = sorted(
        [m for m in all_matches if m["ksa_id"] == ksa_id],
        key=lambda x: x["sts_raw"],
        reverse=True,
    )
    print(f"\n{'='*100}")
    print(f"{ksa_id}: {ab_ksas[ksa_id][:120]}")
    print(f"{'='*100}")
    for i, m in enumerate(ksa_matches[:10]):
        print(f"  #{i+1} STS={m['sts_raw']:.4f} [{FW_LABELS[m['framework']]}] {m['fde_id']}")
        print(f"      {m['fde_name']}")
        if m.get('fde_description'):
            print(f"      Desc: {m['fde_description'][:150]}")

# STS distribution analysis
print("\n" + "=" * 100)
print("STS SCORE DISTRIBUTION ACROSS ALL AB-K MATCHES")
print("=" * 100)

brackets = [
    (0.60, 0.70, "Near-Subset (0.60-0.70)"),
    (0.50, 0.60, "Moderate-High (0.50-0.60)"),
    (0.45, 0.50, "Moderate (0.45-0.50)"),
    (0.35, 0.45, "Weak-Moderate (0.35-0.45)"),
]

for low, high, label in brackets:
    count = sum(1 for m in all_matches if low <= m["sts_raw"] < high)
    print(f"  {label}: {count} matches")

# Near-miss analysis: matches with STS >= 0.60 (close to Subset threshold of 0.70)
print("\n" + "=" * 100)
print("NEAR-MISS ANALYSIS — Matches with STS >= 0.60 (approaching Subset threshold 0.70)")
print("=" * 100)

near_misses = sorted(
    [m for m in all_matches if m["sts_raw"] >= 0.60],
    key=lambda x: x["sts_raw"],
    reverse=True,
)
print(f"\n{len(near_misses)} matches at STS >= 0.60")

# Group by KSA
nm_by_ksa = defaultdict(list)
for m in near_misses:
    nm_by_ksa[m["ksa_id"]].append(m)

for ksa_id in sorted(nm_by_ksa.keys()):
    matches = nm_by_ksa[ksa_id]
    print(f"\n  {ksa_id} ({len(matches)} near-misses):")
    for m in matches[:5]:
        print(f"    STS={m['sts_raw']:.4f} [{FW_LABELS[m['framework']]}] {m['fde_id']}: {m['fde_name']}")

# Thematic gap identification: what FDE topics appear most but never reach strong?
print("\n" + "=" * 100)
print("THEMATIC COVERAGE — FDE topics that map to AB-K most frequently")
print("=" * 100)

fde_freq = defaultdict(lambda: {"count": 0, "max_sts": 0, "ksas": set(), "frameworks": set()})
for m in all_matches:
    key = m["fde_name"]
    fde_freq[key]["count"] += 1
    if m["sts_raw"] > fde_freq[key]["max_sts"]:
        fde_freq[key]["max_sts"] = m["sts_raw"]
    fde_freq[key]["ksas"].add(m["ksa_id"])
    fde_freq[key]["frameworks"].add(m["framework"])

print("\nFDEs mapping to 5+ AB-K KSAs (broad analytics coverage):")
broad_fdes = {k: v for k, v in fde_freq.items() if len(v["ksas"]) >= 5}
for name, info in sorted(broad_fdes.items(), key=lambda x: (-len(x[1]["ksas"]), -x[1]["max_sts"]))[:20]:
    print(f"  [{len(info['ksas'])} KSAs, max STS={info['max_sts']:.4f}] {name}")
    print(f"    KSAs: {', '.join(sorted(info['ksas']))}")
    print(f"    Frameworks: {', '.join(FW_LABELS[fw] for fw in sorted(info['frameworks']))}")
