#!/usr/bin/env python3
"""
AB Domain — Dimension Synthesis
Reusable script for any AB dimension (skills, abilities, tasks).
Extracts mappings from all 6 STRMs, computes high watermark,
filters to analytics-relevant elements, and outputs analysis.

Usage:
  python3 scripts/ab_dimension_synthesis.py --dimension skills
  python3 scripts/ab_dimension_synthesis.py --dimension abilities
  python3 scripts/ab_dimension_synthesis.py --dimension tasks
"""
import json
import argparse
from pathlib import Path
from collections import defaultdict

BASE_DIR = Path(__file__).resolve().parent.parent
STRM_DIR = BASE_DIR / "strm"
KSA_DIR = BASE_DIR / "ksas"

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

# Cybersecurity/intelligence noise patterns
CYBER_NOISE = [
    "intrusion", "malware", "exploit", "attack", "adversar",
    "vulnerability", "penetration", "firewall", "encryption",
    "cryptograph", "cipher", "IPSEC", "AES", "PKI", "certificate",
    "incident response", "forensic", "threat hunt", "kill chain",
    "SIGINT", "HUMINT", "COMINT", "targeting", "weapon",
    "military", "combat", "warfare", "countermeasure",
    "access control", "authentication", "authorization",
    "malicious", "ransomware", "phishing", "social engineer",
    "reverse engineer", "disassembl", "decompil",
    "intelligence collection", "intelligence gathering",
    "intelligence discipline", "intelligence fusion",
    "intelligence support", "intelligence capability",
    "collection tasking", "collection system", "collection strateg",
    "dissemination", "indications and warning",
    "cyber operation", "cyber risk", "cybersecurity",
    "network traffic", "packet", "protocol anal",
    "security model", "security system", "security engineer",
    "security control", "security requirement", "security feature",
    "security implication", "security management",
    "cross domain", "multi-level security",
    "credential", "password", "token",
]

ANALYTICS_KEYWORDS = [
    "statist", "analyt", "analy", "data ", "database", "query", "visual",
    "model", "math", "algorithm", "machine learn", "monitor", "metric",
    "correlation", "aggregat", "report", "dashboard", "intelligence",
    "classification", "pattern", "anomaly", "forecast", "predict",
    "optimization", "performance", "assessment", "evaluation", "test",
    "simulation", "process", "research", "design", "collection",
    "information management", "knowledge management", "quality",
    "data science", "geospatial", "data mining", "data type",
    "data handling", "data manipulation", "data processing",
    "data asset", "data remediation", "data structure",
    "embedded", "automation", "AI", "validation",
    "business impact", "decision support", "communicat",
    "stakeholder", "present", "document", "train", "mentor",
    "govern", "lifecycle", "certif", "standard",
    "pipeline", "automat", "workflow", "schedul",
    "collaborat", "cross-functional", "requirement",
    "interpret", "translat", "narrat", "story",
]


def is_analytics_relevant(desc):
    desc_lower = desc.lower()
    for noise in CYBER_NOISE:
        if noise.lower() in desc_lower:
            return False
    for kw in ANALYTICS_KEYWORDS:
        if kw.lower() in desc_lower:
            return True
    return False


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dimension", required=True, choices=["skills", "abilities", "tasks"])
    args = parser.parse_args()

    dim = args.dimension
    prefix_map = {"skills": "AB-S-", "abilities": "AB-A-", "tasks": "AB-T-"}
    prefix = prefix_map[dim]

    # Load current KSAs
    ksa_file = KSA_DIR / f"AB_{dim}.json"
    with open(ksa_file) as f:
        ksa_data = json.load(f)
    current_ksas = {e["ksa_id"]: e["statement"] for e in ksa_data["entries"]}
    print(f"Current AB {dim}: {len(current_ksas)} entries")

    # Extract mappings from all frameworks
    evidence = defaultdict(lambda: defaultdict(list))
    for fw in FRAMEWORKS:
        mapping_file = STRM_DIR / fw / "strm_mapping.json"
        if not mapping_file.exists():
            continue
        print(f"  Processing {FW_LABELS[fw]}...", end="", flush=True)
        with open(mapping_file) as f:
            data = json.load(f)
        count = 0
        for m in data["mappings"]:
            ref_id = m.get("ref_id") or ""
            if ref_id.startswith(prefix):
                evidence[ref_id][fw].append({
                    "fde_id": m.get("fde_id"),
                    "fde_name": m.get("fde_name"),
                    "fde_description": m.get("fde_description") or m.get("fde_name") or "",
                    "relationship": m.get("relationship"),
                    "strength": m.get("strength"),
                    "sts_raw": m.get("sts_raw") or m.get("primary_score") or 0,
                })
                count += 1
        del data
        print(f" {count} mappings")

    total = sum(sum(len(v) for v in ksa_ev.values()) for ksa_ev in evidence.values())
    print(f"\nTotal {prefix}* mappings: {total}")

    # Evidence matrix
    print(f"\n{'='*80}")
    print(f"EVIDENCE MATRIX — AB {dim.title()}")
    print(f"{'='*80}")
    print(f"\n{'KSA ID':<12} {'FW Cov':>6} {'Strong':>7} {'Total':>6} {'Max STS':>8}")
    print("-" * 45)
    for ksa_id in sorted(current_ksas.keys()):
        fw_count = sum(1 for fw in FRAMEWORKS if evidence[ksa_id].get(fw))
        strong = sum(
            len([m for m in evidence[ksa_id].get(fw, []) if m["relationship"] in STRONG_RELS])
            for fw in FRAMEWORKS
        )
        total_maps = sum(len(evidence[ksa_id].get(fw, [])) for fw in FRAMEWORKS)
        max_sts = max(
            (m["sts_raw"] for fw in FRAMEWORKS for m in evidence[ksa_id].get(fw, [])),
            default=0
        )
        print(f"{ksa_id:<12} {fw_count:>3}/6  {strong:>6}  {total_maps:>5}  {max_sts:>8.4f}")

    # High watermark — unique FDEs per framework at various thresholds
    print(f"\n{'='*80}")
    print(f"HIGH WATERMARK — Unique FDE count per framework")
    print(f"{'='*80}")

    totals = {}
    for fw in FRAMEWORKS:
        mapping_file = STRM_DIR / fw / "strm_mapping.json"
        if not mapping_file.exists():
            continue
        with open(mapping_file) as f:
            data = json.load(f)

        fdes_45 = set()
        fdes_50 = set()
        fdes_55 = set()
        fdes_60 = set()
        for m in data["mappings"]:
            ref_id = m.get("ref_id") or ""
            if not ref_id.startswith(prefix):
                continue
            sts = m.get("sts_raw") or m.get("primary_score") or 0
            fde_id = m.get("fde_id")
            if sts >= 0.45: fdes_45.add(fde_id)
            if sts >= 0.50: fdes_50.add(fde_id)
            if sts >= 0.55: fdes_55.add(fde_id)
            if sts >= 0.60: fdes_60.add(fde_id)

        totals[fw] = {
            "gte_45": len(fdes_45), "gte_50": len(fdes_50),
            "gte_55": len(fdes_55), "gte_60": len(fdes_60),
        }
        del data

    print(f"\n{'Framework':<25} {'>=0.45':>8} {'>=0.50':>8} {'>=0.55':>8} {'>=0.60':>8}")
    print("-" * 60)
    for fw in FRAMEWORKS:
        t = totals.get(fw, {})
        print(f"{FW_LABELS[fw]:<25} {t.get('gte_45',0):>8} {t.get('gte_50',0):>8} {t.get('gte_55',0):>8} {t.get('gte_60',0):>8}")

    # Analytics-relevant filtering for top two frameworks (NICE + DCWF)
    for fw in ["nice", "dcwf"]:
        mapping_file = STRM_DIR / fw / "strm_mapping.json"
        with open(mapping_file) as f:
            data = json.load(f)

        relevant = {}
        noise = {}
        for m in data["mappings"]:
            ref_id = m.get("ref_id") or ""
            if not ref_id.startswith(prefix):
                continue
            sts = m.get("sts_raw") or m.get("primary_score") or 0
            if sts < 0.50:
                continue
            fde_id = m.get("fde_id", "")
            fde_desc = m.get("fde_description") or m.get("fde_name") or ""

            if fde_id not in relevant and fde_id not in noise:
                if is_analytics_relevant(fde_desc):
                    relevant[fde_id] = {"id": fde_id, "desc": fde_desc, "best_sts": sts, "ksa_matches": set()}
                else:
                    noise[fde_id] = {"id": fde_id, "desc": fde_desc, "best_sts": sts}

            if fde_id in relevant:
                if sts > relevant[fde_id]["best_sts"]:
                    relevant[fde_id]["best_sts"] = sts
                relevant[fde_id]["ksa_matches"].add(ref_id)

        del data

        print(f"\n{'='*80}")
        print(f"{FW_LABELS[fw]} — Analytics-relevant elements at STS >= 0.50")
        print(f"{'='*80}")
        print(f"  Total: {len(relevant) + len(noise)}")
        print(f"  Analytics-relevant: {len(relevant)}")
        print(f"  Noise filtered: {len(noise)}")

        print(f"\nTop 60 analytics-relevant elements:")
        for i, e in enumerate(sorted(relevant.values(), key=lambda x: x["best_sts"], reverse=True)[:60]):
            ksas = ", ".join(sorted(e["ksa_matches"]))
            print(f"  {i+1:>3}. STS={e['best_sts']:.4f} [{e['id']}] {e['desc'][:120]}")
            print(f"       -> {ksas}")


if __name__ == "__main__":
    main()
