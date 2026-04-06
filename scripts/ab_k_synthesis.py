#!/usr/bin/env python3
"""
AB Knowledge Domain — Cross-Framework Synthesis
Extracts AB-K mappings from all 6 STRM mapping files and builds evidence matrix.
"""
import json
import os
import sys
from collections import defaultdict
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
STRM_DIR = BASE_DIR / "strm"
KSA_FILE = BASE_DIR / "ksas" / "AB_knowledge.json"
OUTPUT_FILE = BASE_DIR / "strm" / "ab_knowledge_synthesis.json"

FRAMEWORKS = ["onet", "nice", "dcwf", "ddat", "eu_ai_act", "nist_ai_rmf"]
FW_LABELS = {
    "onet": "O*NET 30.2",
    "nice": "NIST NICE v2.1.0",
    "dcwf": "DoD DCWF v5.1",
    "ddat": "DDaT",
    "eu_ai_act": "EU AI Act",
    "nist_ai_rmf": "NIST AI RMF 1.0",
}

STRONG_RELS = {"Equal", "Subset Of", "Superset Of"}
MODERATE_RELS = {"Intersects With"}


def main():
    # Load AB Knowledge KSAs
    with open(KSA_FILE) as f:
        ksa_data = json.load(f)
    ab_ksas = {e["ksa_id"]: e["statement"] for e in ksa_data["entries"]}
    print(f"AB Knowledge KSAs loaded: {len(ab_ksas)}")

    # Evidence matrix: ksa_id -> framework -> list of mappings
    evidence = defaultdict(lambda: defaultdict(list))

    # Process each framework
    for fw in FRAMEWORKS:
        mapping_file = STRM_DIR / fw / "strm_mapping.json"
        if not mapping_file.exists():
            print(f"  SKIP {fw}: no mapping file")
            continue

        print(f"  Processing {FW_LABELS[fw]}...", end="", flush=True)
        with open(mapping_file) as f:
            data = json.load(f)

        count = 0
        for m in data["mappings"]:
            ref_id = m.get("ref_id") or ""
            if ref_id.startswith("AB-K-"):
                evidence[ref_id][fw].append({
                    "fde_id": m.get("fde_id"),
                    "fde_name": m.get("fde_name"),
                    "relationship": m.get("relationship"),
                    "strength": m.get("strength"),
                    "sts_raw": m.get("sts_raw") or m.get("primary_score"),
                    "bienc_score": m.get("bienc_score"),
                })
                count += 1
        del data
        print(f" {count} mappings")

    # Build summary matrix
    print("\n" + "=" * 80)
    print("CROSS-FRAMEWORK EVIDENCE MATRIX — AB Knowledge Domain")
    print("=" * 80)

    summary = {}
    for ksa_id in sorted(ab_ksas.keys()):
        stmt = ab_ksas[ksa_id]
        row = {
            "ksa_id": ksa_id,
            "statement": stmt,
            "frameworks": {},
            "total_mappings": 0,
            "strong_mappings": 0,
            "moderate_mappings": 0,
            "frameworks_with_evidence": 0,
            "max_sts": 0.0,
            "top_fdes": [],
        }

        for fw in FRAMEWORKS:
            mappings = evidence[ksa_id].get(fw, [])
            strong = [m for m in mappings if m["relationship"] in STRONG_RELS]
            moderate = [m for m in mappings if m["relationship"] in MODERATE_RELS]

            row["frameworks"][fw] = {
                "total": len(mappings),
                "strong": len(strong),
                "moderate": len(moderate),
                "max_sts": max((m.get("sts_raw") or 0 for m in mappings), default=0),
            }

            row["total_mappings"] += len(mappings)
            row["strong_mappings"] += len(strong)
            row["moderate_mappings"] += len(moderate)
            if mappings:
                row["frameworks_with_evidence"] += 1
                local_max = max((m.get("sts_raw") or 0 for m in mappings), default=0)
                if local_max > row["max_sts"]:
                    row["max_sts"] = local_max

            # Track top FDEs (strong matches, high STS)
            for m in strong:
                row["top_fdes"].append({
                    "framework": FW_LABELS[fw],
                    "fde_id": m["fde_id"],
                    "fde_name": m["fde_name"],
                    "relationship": m["relationship"],
                    "sts": m.get("sts_raw") or 0,
                })

        row["top_fdes"].sort(key=lambda x: x["sts"], reverse=True)
        row["top_fdes"] = row["top_fdes"][:10]
        summary[ksa_id] = row

    # Print matrix
    print(f"\n{'KSA ID':<12} {'FW Cov':>6} {'Strong':>7} {'Moderate':>9} {'Total':>6} {'Max STS':>8}")
    print("-" * 55)
    for ksa_id in sorted(summary.keys()):
        r = summary[ksa_id]
        print(f"{ksa_id:<12} {r['frameworks_with_evidence']:>3}/6  {r['strong_mappings']:>6}  {r['moderate_mappings']:>8}  {r['total_mappings']:>5}  {r['max_sts']:>8.4f}")

    # Gap analysis
    print("\n" + "=" * 80)
    print("GAP ANALYSIS")
    print("=" * 80)

    weak_ksas = []
    strong_ksas = []
    for ksa_id, r in sorted(summary.items()):
        if r["frameworks_with_evidence"] <= 2 or r["strong_mappings"] == 0:
            weak_ksas.append(r)
        elif r["frameworks_with_evidence"] >= 4 and r["strong_mappings"] >= 3:
            strong_ksas.append(r)

    print(f"\nSTRONG CORROBORATION ({len(strong_ksas)} KSAs — 4+ frameworks, 3+ strong):")
    for r in strong_ksas:
        print(f"  {r['ksa_id']}: {r['frameworks_with_evidence']}/6 fw, {r['strong_mappings']} strong | {r['statement'][:100]}")

    print(f"\nWEAK/MISSING CORROBORATION ({len(weak_ksas)} KSAs — <=2 frameworks or 0 strong):")
    for r in weak_ksas:
        print(f"  {r['ksa_id']}: {r['frameworks_with_evidence']}/6 fw, {r['strong_mappings']} strong | {r['statement'][:100]}")

    # Middle tier
    mid_ksas = [r for r in summary.values() if r not in [s for s in strong_ksas] and r not in [w for w in weak_ksas]]
    if mid_ksas:
        print(f"\nMODERATE CORROBORATION ({len(mid_ksas)} KSAs):")
        for r in sorted(mid_ksas, key=lambda x: x['ksa_id']):
            print(f"  {r['ksa_id']}: {r['frameworks_with_evidence']}/6 fw, {r['strong_mappings']} strong | {r['statement'][:100]}")

    # Per-framework coverage
    print("\n" + "=" * 80)
    print("PER-FRAMEWORK COVERAGE")
    print("=" * 80)
    for fw in FRAMEWORKS:
        total_ksas_hit = sum(1 for ksa_id in ab_ksas if evidence[ksa_id].get(fw))
        total_maps = sum(len(evidence[ksa_id].get(fw, [])) for ksa_id in ab_ksas)
        strong_maps = sum(
            len([m for m in evidence[ksa_id].get(fw, []) if m["relationship"] in STRONG_RELS])
            for ksa_id in ab_ksas
        )
        print(f"  {FW_LABELS[fw]:<25} {total_ksas_hit:>2}/10 KSAs   {total_maps:>5} maps   {strong_maps:>4} strong")

    # Detailed per-KSA evidence
    print("\n" + "=" * 80)
    print("DETAILED PER-KSA EVIDENCE")
    print("=" * 80)
    for ksa_id in sorted(summary.keys()):
        r = summary[ksa_id]
        print(f"\n--- {ksa_id} ---")
        print(f"Statement: {r['statement']}")
        print(f"Coverage: {r['frameworks_with_evidence']}/6 fw | {r['strong_mappings']} strong | {r['moderate_mappings']} moderate | {r['total_mappings']} total | max STS: {r['max_sts']:.4f}")

        for fw in FRAMEWORKS:
            fw_data = r["frameworks"].get(fw, {})
            if fw_data.get("total", 0) > 0:
                print(f"  {FW_LABELS[fw]:<25}: {fw_data['total']:>3} maps ({fw_data['strong']} strong, {fw_data['moderate']} moderate) max STS={fw_data['max_sts']:.4f}")

        if r["top_fdes"]:
            print(f"  Top strong matches:")
            for fde in r["top_fdes"][:5]:
                print(f"    [{fde['framework']}] {fde['fde_id']}: {fde['fde_name']} ({fde['relationship']}, STS={fde['sts']:.4f})")

    # Collect all unique strong-matched FDE themes
    print("\n" + "=" * 80)
    print("FDE THEME ANALYSIS — What source frameworks emphasize for AB Knowledge")
    print("=" * 80)
    fde_to_ksas = defaultdict(lambda: {"count": 0, "ksas": set(), "frameworks": set()})
    for ksa_id in ab_ksas:
        for fw in FRAMEWORKS:
            for m in evidence[ksa_id].get(fw, []):
                if m["relationship"] in STRONG_RELS:
                    key = m["fde_name"]
                    fde_to_ksas[key]["count"] += 1
                    fde_to_ksas[key]["ksas"].add(ksa_id)
                    fde_to_ksas[key]["frameworks"].add(FW_LABELS[fw])

    print(f"\nUnique FDEs with strong AB-K matches: {len(fde_to_ksas)}")
    print("\nTop FDE themes (by cross-KSA breadth):")
    for name, info in sorted(fde_to_ksas.items(), key=lambda x: (-len(x[1]["ksas"]), -x[1]["count"]))[:20]:
        ksas_str = ", ".join(sorted(info["ksas"]))
        fw_str = ", ".join(sorted(info["frameworks"]))
        print(f"  [{len(info['ksas'])} KSAs, {info['count']}x] {name}")
        print(f"    KSAs: {ksas_str}")
        print(f"    Frameworks: {fw_str}")

    # Save full evidence to JSON
    output = {
        "synthesis_date": "2026-04-03",
        "domain": "AB",
        "dimension": "Knowledge",
        "ksa_count": len(ab_ksas),
        "frameworks_analyzed": list(FW_LABELS.values()),
        "summary": {},
        "raw_evidence": {},
    }
    for ksa_id in sorted(summary.keys()):
        s = summary[ksa_id]
        # Convert top_fdes for JSON
        output["summary"][ksa_id] = s
    for ksa_id in ab_ksas:
        output["raw_evidence"][ksa_id] = {
            fw: evidence[ksa_id][fw] for fw in FRAMEWORKS if evidence[ksa_id].get(fw)
        }

    with open(OUTPUT_FILE, "w") as f:
        json.dump(output, f, indent=2, default=str)
    print(f"\nFull evidence saved to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
