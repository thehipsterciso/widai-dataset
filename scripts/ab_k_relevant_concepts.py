#!/usr/bin/env python3
"""
AB Knowledge — Relevant Concept Extraction
Filter NICE and DCWF elements to those genuinely relevant to analytics/BI,
then cluster into distinct knowledge concept groups.
"""
import json
from pathlib import Path
from collections import defaultdict

BASE_DIR = Path(__file__).resolve().parent.parent
STRM_DIR = BASE_DIR / "strm"

# Analytics/BI relevant keyword patterns — concepts that belong in an analytics domain
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
    "data vaulting", "embedded", "automation", "AI", "validation",
    "business impact", "decision support",
]

# Cybersecurity/intelligence noise patterns — NOT analytics domain
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

def is_analytics_relevant(desc):
    """Check if a description is genuinely about analytics/BI, not just tangential."""
    desc_lower = desc.lower()

    # First check: does it contain cyber noise?
    for noise in CYBER_NOISE:
        if noise.lower() in desc_lower:
            return False

    # Second check: does it contain analytics keywords?
    for kw in ANALYTICS_KEYWORDS:
        if kw.lower() in desc_lower:
            return True

    return False


# Process NICE K-elements
with open(STRM_DIR / "nice" / "strm_mapping.json") as f:
    nice = json.load(f)

nice_relevant = {}
nice_noise = {}
for m in nice["mappings"]:
    ref_id = m.get("ref_id") or ""
    if not ref_id.startswith("AB-K-"):
        continue
    fde_id = m.get("fde_id", "")
    if not fde_id.startswith("K"):
        continue
    sts = m.get("sts_raw") or 0
    if sts < 0.50:
        continue

    desc = m.get("fde_description") or m.get("fde_name") or ""

    if fde_id not in nice_relevant and fde_id not in nice_noise:
        if is_analytics_relevant(desc):
            nice_relevant[fde_id] = {
                "id": fde_id, "desc": desc,
                "best_sts": sts, "ksa_matches": set(),
            }
        else:
            nice_noise[fde_id] = {
                "id": fde_id, "desc": desc,
                "best_sts": sts, "ksa_matches": set(),
            }

    target = nice_relevant if fde_id in nice_relevant else nice_noise
    if fde_id in target:
        if sts > target[fde_id]["best_sts"]:
            target[fde_id]["best_sts"] = sts
        target[fde_id]["ksa_matches"].add(ref_id)

del nice

print("NICE K-ELEMENTS — ANALYTICS-RELEVANT vs NOISE")
print(f"  Total at STS >= 0.50: {len(nice_relevant) + len(nice_noise)}")
print(f"  Analytics-relevant: {len(nice_relevant)}")
print(f"  Cyber/intel noise: {len(nice_noise)}")

print(f"\nANALYTICS-RELEVANT NICE K-ELEMENTS ({len(nice_relevant)}):")
print("=" * 100)
for i, k in enumerate(sorted(nice_relevant.values(), key=lambda x: x["best_sts"], reverse=True)):
    ksas = ", ".join(sorted(k["ksa_matches"]))
    print(f"  {i+1:>3}. STS={k['best_sts']:.4f} [{k['id']}] {k['desc'][:120]}")

# Same for DCWF
with open(STRM_DIR / "dcwf" / "strm_mapping.json") as f:
    dcwf = json.load(f)

dcwf_relevant = {}
dcwf_noise = {}
for m in dcwf["mappings"]:
    ref_id = m.get("ref_id") or ""
    if not ref_id.startswith("AB-K-"):
        continue
    fde_desc = m.get("fde_description") or m.get("fde_name") or ""
    if not fde_desc.lower().startswith("knowledge of"):
        continue
    sts = m.get("sts_raw") or 0
    if sts < 0.50:
        continue
    fde_id = m.get("fde_id", "")

    if fde_id not in dcwf_relevant and fde_id not in dcwf_noise:
        if is_analytics_relevant(fde_desc):
            dcwf_relevant[fde_id] = {
                "id": fde_id, "desc": fde_desc,
                "best_sts": sts, "ksa_matches": set(),
            }
        else:
            dcwf_noise[fde_id] = {
                "id": fde_id, "desc": fde_desc,
                "best_sts": sts, "ksa_matches": set(),
            }

    target = dcwf_relevant if fde_id in dcwf_relevant else dcwf_noise
    if fde_id in target:
        if sts > target[fde_id]["best_sts"]:
            target[fde_id]["best_sts"] = sts
        target[fde_id]["ksa_matches"].add(ref_id)

del dcwf

print(f"\n\nDCWF KNOWLEDGE ELEMENTS — ANALYTICS-RELEVANT vs NOISE")
print(f"  Total at STS >= 0.50: {len(dcwf_relevant) + len(dcwf_noise)}")
print(f"  Analytics-relevant: {len(dcwf_relevant)}")
print(f"  Cyber/intel noise: {len(dcwf_noise)}")

print(f"\nANALYTICS-RELEVANT DCWF ELEMENTS ({len(dcwf_relevant)}):")
print("=" * 100)
for i, k in enumerate(sorted(dcwf_relevant.values(), key=lambda x: x["best_sts"], reverse=True)):
    ksas = ", ".join(sorted(k["ksa_matches"]))
    print(f"  {i+1:>3}. STS={k['best_sts']:.4f} [{k['id']}] {k['desc'][:120]}")

# Combined count
all_relevant = len(nice_relevant) + len(dcwf_relevant)
print(f"\n\nCOMBINED ANALYTICS-RELEVANT KNOWLEDGE ELEMENTS: {all_relevant}")
print(f"  NICE: {len(nice_relevant)}")
print(f"  DCWF: {len(dcwf_relevant)}")
print(f"\nAfter deduplication and clustering, this suggests a target of ~{all_relevant // 4}-{all_relevant // 3} AB-K KSAs")
print(f"(Each WIDAI KSA typically subsumes 3-5 source framework elements)")
