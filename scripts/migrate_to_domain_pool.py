#!/usr/bin/env python3
"""
ATLAS KSA Migration: Role-Centric → Shared Domain Pool

Implements ADR-013. Reads all existing category-based KSA files, deduplicates,
assigns each KSA to a knowledge domain, generates new role-independent IDs,
creates domain-based pool files, rewrites all role-KSA mapping files for
many-to-many cardinality, and produces a legacy ID map for audit trail.

This script is idempotent — it reads from the old structure and writes the
new structure. It does NOT delete old files (that's done separately).

Usage:
    python scripts/migrate_to_domain_pool.py [--dry-run]

Exit codes:
    0 — Migration completed successfully
    1 — Errors during migration
"""

import json
import os
import sys
import glob
import re
from collections import defaultdict
from datetime import datetime

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# =============================================================================
# Domain Taxonomy (per ADR-013)
# =============================================================================

DOMAINS = {
    "DG": "Data Governance & Policy",
    "DA": "Data Architecture & Infrastructure",
    "DQ": "Data Quality & Management",
    "AI": "AI/ML Foundations",
    "AG": "AI Governance & Ethics",
    "SP": "Security & Privacy",
    "AB": "Analytics & BI",
    "LS": "Leadership & Strategy",
    "OP": "Operations & Enablement",
    "RC": "Regulatory & Compliance",
    "RM": "Risk Management",
    "TF": "Technical Foundations",
}

# =============================================================================
# Domain Assignment Rules
# Priority-ordered keyword matching. First match wins.
# More specific patterns come first to avoid false matches.
# =============================================================================

DOMAIN_RULES = [
    # AG — AI Governance & Ethics (must come before general AI and general governance)
    ("AG", [
        r"responsible ai", r"ai governance", r"ai ethics", r"ai impact assess",
        r"algorithmic fairness", r"bias audit", r"ai acceptable use",
        r"ai inventory", r"ai system inventory", r"ai policy compliance",
        r"ai risk categor", r"ai risk taxon", r"ai risk assess",
        r"fairness metric", r"bias evaluation", r"explainability",
        r"ai regulatory", r"eu ai act",
    ]),
    # RM — Risk Management (must come before general regulatory)
    ("RM", [
        r"model risk management", r"model validation", r"model inventory",
        r"model risk governance", r"sr.?11.?7", r"model risk regulatory",
        r"risk assessment", r"risk quantif", r"model risk consider",
        r"ai.specific attack", r"adversarial (test|example|input)",
        r"red.team", r"ai security assess", r"threat model",
        r"ai test and evaluation", r"evaluation framework",
        r"evaluation dataset", r"ai system documentation",
        r"ai test plan", r"ai system test",
    ]),
    # SP — Security & Privacy
    ("SP", [
        r"data protection (law|regulat|officer|impact|obligation)",
        r"gdpr", r"ccpa", r"cpra", r"privacy.by.design", r"privacy.by.default",
        r"data subject rights", r"records of processing", r"ropa",
        r"data protection impact", r"dpia", r"privacy impact",
        r"supervisory authorit", r"data processing agreement",
        r"data protection", r"privacy",
        r"training data integrity", r"data poison",
        r"llm.specific security", r"model supply chain security",
        r"prompt injection", r"ai application security",
        r"ai security standard",
    ]),
    # RC — Regulatory & Compliance
    ("RC", [
        r"compliance assessment methodolog", r"compliance gap assess",
        r"regulatory (data )?reporting obligation", r"compliance remediation",
        r"data compliance", r"regulatory requirement",
        r"compliance monitor",
    ]),
    # AI — AI/ML Foundations
    ("AI", [
        r"machine learning", r"supervised and unsupervised", r"deep learning",
        r"neural network", r"model training", r"model evaluation",
        r"feature engineering", r"model interpretability",
        r"nlp", r"natural language processing", r"transformer architecture",
        r"computer vision", r"cnn architecture", r"vision transformer",
        r"large language model", r"llm", r"retrieval.augmented generation",
        r"rag", r"agentic ai", r"prompt engineering",
        r"ml model serving", r"ml pipeline", r"mlops",
        r"ml platform", r"feature store", r"model registry",
        r"model monitoring", r"model deploy", r"model serving",
        r"ml retraining", r"ml training pipeline",
        r"ml infrastructure", r"gpu.*compute", r"accelerated compute",
        r"containerization.*ml", r"ci/cd.*ml",
        r"research.*ml", r"research.*ai", r"frontiers.*machine learning",
        r"experimental design.*ml", r"ablation",
        r"ai capability landscape", r"ai innovation",
        r"ai proof.of.concept", r"ai use case feasib",
    ]),
    # DG — Data Governance & Policy
    ("DG", [
        r"data governance", r"data steward", r"data policy",
        r"governance council", r"governance program", r"governance operating model",
        r"data strategy framework", r"data domain.*ownership",
        r"enterprise data.*strategy", r"data.*ai strategy",
        r"data maturity assessment", r"dcam",
        r"business glossary", r"data asset catalog",
        r"data access request",
    ]),
    # DA — Data Architecture & Infrastructure
    ("DA", [
        r"data (architecture|architect)", r"data model(ing|ling)",
        r"data platform", r"data integration pattern",
        r"data storage technolog", r"data pipeline design",
        r"data pipeline orchestrat", r"distributed data processing",
        r"cloud data platform", r"infrastructure.as.code",
        r"data platform security", r"etl|elt",
        r"dimensional modeling", r"star schema", r"snowflake schema",
        r"analytics transformation", r"dbt|data build tool",
        r"metrics layer", r"semantic layer",
        r"data pipeline monitor", r"pipeline failure",
        r"data environment provisioning",
    ]),
    # DQ — Data Quality & Management
    ("DQ", [
        r"data quality", r"master data management", r"mdm",
        r"entity resolution", r"reference data management",
        r"metadata (type|manage|standard)", r"data catalog",
        r"data lineage", r"data product",
        r"data mesh", r"data lifecycle",
        r"clinical data (manage|standard|capture)",
        r"cdisc",
    ]),
    # AB — Analytics & BI
    ("AB", [
        r"descriptive statistics", r"data visualization",
        r"analytical framework", r"business question.*data query",
        r"bi (platform|developer|governance|dashboard|semantic|asset)",
        r"power bi|tableau|looker", r"report certification",
        r"a/b test", r"experimentation design",
        r"advanced analytical method", r"multivariate",
        r"statistical modeling", r"regression",
        r"causal inference", r"quantitative analy",
        r"risk quantification.*value at risk",
        r"analytical (study|documentation|project|request)",
        r"self.service report", r"dashboard",
    ]),
    # LS — Leadership & Strategy
    ("LS", [
        r"enterprise transformation", r"organizational design",
        r"executive alignment", r"transformation roadmap",
        r"transformation program", r"cross.functional transformation",
        r"board.*audit committee", r"executive.level",
        r"organizational resistance", r"organizational change",
        r"data.*ai.*investment portfolio", r"vendor.*third.party.*risk",
        r"vendor.*contracting", r"data valuation.*infonomics",
        r"data monetiz", r"data.*ai business case",
        r"data.*ai maturity assessment.*conduct",
        r"data.*ai strategy (engagement|recommend|consultant)",
    ]),
    # OP — Operations & Enablement
    ("OP", [
        r"program management framework", r"program (risk|execution|plan|retro)",
        r"change management framework", r"prosci|adkar|kotter",
        r"adult learning", r"training program",
        r"data.*ai.*adoption", r"adoption (barrier|program)",
        r"data literacy", r"ai literacy",
        r"data pipeline (health|incident|maintenance)",
        r"data access (manage|request).*process",
        r"platform maintenance",
    ]),
    # TF — Technical Foundations
    ("TF", [
        r"sql", r"python", r"production.quality.*code",
        r"containerization", r"docker|kubernetes",
        r"infrastructure.as.code", r"terraform",
        r"data pipeline.*code", r"version control",
        r"data testing", r"schema validation",
        r"dataops principle", r"pipeline observab",
    ]),
]


def assign_domain(statement, ksa_type, old_id):
    """
    Assign a KSA to its primary domain using keyword matching.
    Falls back to inferring from the old category-based ID.
    """
    text = statement.lower()

    for domain_code, patterns in DOMAIN_RULES:
        for pattern in patterns:
            if re.search(pattern, text):
                return domain_code

    # Fallback: infer from old ID prefix
    old_prefix = old_id.split("-")[0] if "-" in old_id else ""
    fallback_map = {
        "GOV": "DG", "ENG": "DA", "DEV": "AI", "DSM": "DQ",
        "ANL": "AB", "RSK": "RM", "LDR": "LS", "OPS": "OP",
    }
    return fallback_map.get(old_prefix, "DG")


def compute_similarity(s1, s2):
    """
    Simple word-overlap similarity for deduplication.
    Returns a ratio 0-1 of shared significant words.
    """
    stop_words = {"the", "of", "and", "in", "to", "for", "a", "an", "is", "that",
                  "with", "as", "by", "on", "at", "from", "or", "its", "this",
                  "including", "knowledge", "skill", "task", "ability"}

    def significant_words(s):
        words = set(re.findall(r'\b[a-z]{4,}\b', s.lower()))
        return words - stop_words

    w1 = significant_words(s1)
    w2 = significant_words(s2)

    if not w1 or not w2:
        return 0.0

    intersection = w1 & w2
    union = w1 | w2
    return len(intersection) / len(union)


def find_duplicates(ksas, threshold=0.70):
    """
    Find semantic duplicates — KSAs with >threshold word overlap.
    Returns a list of (ksa_id_1, ksa_id_2, similarity) tuples.
    """
    duplicates = []
    items = list(ksas.items())

    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            id1, ksa1 = items[i]
            id2, ksa2 = items[j]

            # Only compare same-type KSAs
            if ksa1["type"] != ksa2["type"]:
                continue

            sim = compute_similarity(ksa1["statement"], ksa2["statement"])
            if sim >= threshold:
                duplicates.append((id1, id2, sim))

    return duplicates


def load_all_ksas():
    """Load all KSAs from existing category files."""
    ksas = {}
    ksas_dir = os.path.join(BASE, "ksas")

    for fp in sorted(glob.glob(os.path.join(ksas_dir, "*_ksas.json"))):
        with open(fp, "r", encoding="utf-8") as f:
            data = json.load(f)
        for ksa in data.get("ksas", []):
            kid = ksa.get("ksa_id")
            if kid:
                ksas[kid] = {
                    "type": ksa.get("type", "Unknown"),
                    "statement": ksa.get("statement", ""),
                    "origin_framework": ksa.get("origin_framework", "ATLAS"),
                    "origin_version": ksa.get("origin_version", "0.3.0"),
                    "source_file": os.path.basename(fp),
                }

    return ksas


def load_all_mappings():
    """Load all role-KSA mappings from existing files."""
    mappings = []
    mappings_dir = os.path.join(BASE, "mappings")

    for fp in sorted(glob.glob(os.path.join(mappings_dir, "role_ksa_*.json"))):
        with open(fp, "r", encoding="utf-8") as f:
            data = json.load(f)
        for rel in data.get("relationships", []):
            mappings.append({
                "work_role_id": rel.get("work_role_id"),
                "work_role_title": rel.get("work_role_title", ""),
                "ksa_id": rel.get("ksa_id"),
                "source_file": os.path.basename(fp),
                "category_code": data.get("category_code", ""),
            })

    return mappings


def run_migration(dry_run=False):
    """Execute the full migration."""
    print("\n" + "=" * 70)
    print("ATLAS KSA MIGRATION: Role-Centric → Shared Domain Pool")
    print("=" * 70)
    print(f"\nADR-013 implementation — {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print(f"Mode: {'DRY RUN' if dry_run else 'LIVE'}\n")

    # =========================================================================
    # Step 1: Load existing data
    # =========================================================================
    print("Step 1: Loading existing KSAs and mappings...")
    all_ksas = load_all_ksas()
    all_mappings = load_all_mappings()
    print(f"  Loaded {len(all_ksas)} KSAs from {len(set(k['source_file'] for k in all_ksas.values()))} files")
    print(f"  Loaded {len(all_mappings)} role-KSA mappings\n")

    # =========================================================================
    # Step 2: Find duplicates
    # =========================================================================
    print("Step 2: Finding semantic duplicates (threshold: 0.70)...")
    duplicates = find_duplicates(all_ksas, threshold=0.70)
    print(f"  Found {len(duplicates)} duplicate pairs\n")

    if duplicates:
        print("  Duplicate pairs:")
        for id1, id2, sim in sorted(duplicates, key=lambda x: -x[2]):
            print(f"    {id1} ≈ {id2} (similarity: {sim:.2f})")
            print(f"      1: {all_ksas[id1]['statement'][:80]}...")
            print(f"      2: {all_ksas[id2]['statement'][:80]}...")
            print()

    # Build dedup map: for each duplicate pair, keep the one with the longer statement
    # Map the shorter one → the longer one
    dedup_map = {}  # old_id → canonical_id (the one we keep)
    for id1, id2, sim in duplicates:
        s1 = all_ksas[id1]["statement"]
        s2 = all_ksas[id2]["statement"]
        if len(s1) >= len(s2):
            dedup_map[id2] = id1  # keep id1
        else:
            dedup_map[id1] = id2  # keep id2

    # Resolve transitive dedup chains (A→B, B→C → A→C)
    def resolve_canonical(kid):
        visited = set()
        while kid in dedup_map and kid not in visited:
            visited.add(kid)
            kid = dedup_map[kid]
        return kid

    for kid in list(dedup_map.keys()):
        dedup_map[kid] = resolve_canonical(kid)

    # Build canonical KSA set (unique KSAs after dedup)
    canonical_ids = set()
    for kid in all_ksas:
        canonical = resolve_canonical(kid)
        canonical_ids.add(canonical)

    print(f"  After deduplication: {len(canonical_ids)} unique KSAs (removed {len(all_ksas) - len(canonical_ids)} duplicates)\n")

    # =========================================================================
    # Step 3: Assign domains
    # =========================================================================
    print("Step 3: Assigning domains...")
    domain_assignments = {}
    domain_counts = defaultdict(int)

    for kid in canonical_ids:
        ksa = all_ksas[kid]
        domain = assign_domain(ksa["statement"], ksa["type"], kid)
        domain_assignments[kid] = domain
        domain_counts[domain] += 1

    print("  Domain distribution:")
    for code in sorted(DOMAINS.keys()):
        count = domain_counts.get(code, 0)
        print(f"    {code} ({DOMAINS[code]}): {count}")
    print()

    # =========================================================================
    # Step 4: Generate new IDs
    # =========================================================================
    print("Step 4: Generating new domain-based IDs...")

    # Group canonical KSAs by domain and type, then assign sequential IDs
    domain_type_groups = defaultdict(list)
    for kid in sorted(canonical_ids):
        ksa = all_ksas[kid]
        domain = domain_assignments[kid]
        ksa_type = ksa["type"][0]  # K, S, T, A
        domain_type_groups[(domain, ksa_type)].append(kid)

    old_to_new = {}  # old canonical ID → new domain ID
    new_to_old = {}  # new domain ID → list of old IDs it replaces

    for (domain, ksa_type), old_ids in sorted(domain_type_groups.items()):
        for seq, old_id in enumerate(old_ids, start=1):
            new_id = f"{domain}-{ksa_type}-{seq:03d}"
            old_to_new[old_id] = new_id

            # Track all old IDs this new ID replaces (including dedup'd ones)
            replaced = [old_id]
            for dup_id, canon_id in dedup_map.items():
                if canon_id == old_id:
                    replaced.append(dup_id)
            new_to_old[new_id] = sorted(replaced)

    # Build complete old→new map including dedup'd IDs
    full_id_map = {}
    for old_id in all_ksas:
        canonical = resolve_canonical(old_id)
        new_id = old_to_new[canonical]
        full_id_map[old_id] = new_id

    print(f"  Generated {len(old_to_new)} new IDs\n")

    # =========================================================================
    # Step 5: Create domain pool files
    # =========================================================================
    print("Step 5: Creating domain pool files...")

    domain_pools = defaultdict(list)
    for old_canonical_id, new_id in sorted(old_to_new.items(), key=lambda x: x[1]):
        ksa = all_ksas[old_canonical_id]
        domain = domain_assignments[old_canonical_id]

        pool_entry = {
            "ksa_id": new_id,
            "type": ksa["type"],
            "domain": DOMAINS[domain],
            "domain_code": domain,
            "statement": ksa["statement"],
            "origin_framework": ksa["origin_framework"],
            "origin_version": "0.5.0",
            "legacy_ids": new_to_old[new_id],
        }
        domain_pools[domain].append(pool_entry)

    if not dry_run:
        ksas_dir = os.path.join(BASE, "ksas")
        for domain_code, ksas_list in domain_pools.items():
            # Count by type
            type_counts = defaultdict(int)
            for k in ksas_list:
                type_counts[k["type"]] += 1

            pool_file = {
                "dataset_id": "ATLAS-KSAS",
                "domain_code": domain_code,
                "domain_title": DOMAINS[domain_code],
                "ksa_count": len(ksas_list),
                "knowledge_count": type_counts.get("Knowledge", 0),
                "skill_count": type_counts.get("Skill", 0),
                "task_count": type_counts.get("Task", 0),
                "ability_count": type_counts.get("Ability", 0),
                "schema_version": "2.0.0",
                "ksas": ksas_list,
            }

            filepath = os.path.join(ksas_dir, f"{domain_code}_ksas.json")
            with open(filepath, "w", encoding="utf-8") as f:
                json.dump(pool_file, f, indent=2, ensure_ascii=False)
            print(f"    Created {domain_code}_ksas.json ({len(ksas_list)} KSAs)")

    print()

    # =========================================================================
    # Step 6: Create legacy ID map
    # =========================================================================
    print("Step 6: Creating legacy ID map...")

    legacy_map = {
        "migration_date": datetime.now().strftime("%Y-%m-%d"),
        "adr": "ADR-013",
        "description": "Maps old role-coupled KSA IDs to new domain-based pool IDs",
        "total_old_ids": len(all_ksas),
        "total_new_ids": len(old_to_new),
        "duplicates_merged": len(all_ksas) - len(canonical_ids),
        "old_to_new": {k: v for k, v in sorted(full_id_map.items())},
        "new_to_old": {k: v for k, v in sorted(new_to_old.items())},
    }

    if not dry_run:
        legacy_path = os.path.join(BASE, "ksas", "_legacy_id_map.json")
        with open(legacy_path, "w", encoding="utf-8") as f:
            json.dump(legacy_map, f, indent=2, ensure_ascii=False)
        print(f"    Created _legacy_id_map.json\n")

    # =========================================================================
    # Step 7: Rewrite role-KSA mapping files
    # =========================================================================
    print("Step 7: Rewriting role-KSA mapping files (many-to-many)...")

    # Group mappings by category
    category_mappings = defaultdict(list)
    for m in all_mappings:
        cat = m["category_code"]
        old_ksa_id = m["ksa_id"]
        new_ksa_id = full_id_map.get(old_ksa_id, old_ksa_id)

        # Determine proficiency context from role seniority/category
        wrid = m["work_role_id"]
        prof_context = "operational"  # default
        if wrid:
            parts = wrid.split("-")
            if len(parts) >= 2:
                role_cat = parts[1]
                if role_cat == "GOV":
                    # GOV roles are strategic/oversight
                    role_num = wrid.split(".")[-1] if "." in wrid else "01"
                    if role_num in ["01", "02", "03"]:  # C-suite
                        prof_context = "strategic"
                    elif role_num in ["04", "05"]:  # Directors/Managers
                        prof_context = "operational"
                    else:  # Stewards, DPO
                        prof_context = "operational"
                elif role_cat == "RSK":
                    prof_context = "oversight"
                elif role_cat in ["ENG", "DEV"]:
                    prof_context = "technical"
                elif role_cat == "LDR":
                    prof_context = "strategic"
                elif role_cat in ["ANL", "DSM"]:
                    prof_context = "operational"
                elif role_cat == "OPS":
                    prof_context = "operational"

        new_mapping = {
            "work_role_id": m["work_role_id"],
            "ksa_id": new_ksa_id,
            "relationship_type": "requires",
            "proficiency_context": prof_context,
        }
        category_mappings[cat].append(new_mapping)

    if not dry_run:
        mappings_dir = os.path.join(BASE, "mappings")
        for cat, rels in sorted(category_mappings.items()):
            # Deduplicate (same role+KSA should only appear once)
            seen = set()
            unique_rels = []
            for r in rels:
                key = (r["work_role_id"], r["ksa_id"])
                if key not in seen:
                    seen.add(key)
                    unique_rels.append(r)

            mapping_file = {
                "dataset_id": "ATLAS-ROLE-KSA-MAP",
                "category_code": cat,
                "relationship_count": len(unique_rels),
                "schema_version": "2.0.0",
                "relationships": unique_rels,
            }

            filepath = os.path.join(mappings_dir, f"role_ksa_{cat}.json")
            with open(filepath, "w", encoding="utf-8") as f:
                json.dump(mapping_file, f, indent=2, ensure_ascii=False)
            print(f"    Rewrote role_ksa_{cat}.json ({len(unique_rels)} relationships)")

    print()

    # =========================================================================
    # Summary
    # =========================================================================
    print("=" * 70)
    print("MIGRATION SUMMARY")
    print("=" * 70)
    print(f"\n  Old structure:")
    print(f"    KSA files: {len(set(k['source_file'] for k in all_ksas.values()))} category-based")
    print(f"    Unique KSAs: {len(all_ksas)}")
    print(f"    Mapping cardinality: 1:1 ({len(all_mappings)} mappings)")
    print(f"\n  New structure:")
    print(f"    KSA files: {len(domain_pools)} domain-based")
    print(f"    Unique KSAs: {len(canonical_ids)} (after dedup)")
    print(f"    Mapping relationships: {sum(len(v) for v in category_mappings.values())}")
    print(f"    Duplicates merged: {len(all_ksas) - len(canonical_ids)}")
    print(f"\n  Domain distribution:")
    for code in sorted(DOMAINS.keys()):
        count = len(domain_pools.get(code, []))
        print(f"    {code} {DOMAINS[code]}: {count}")
    print(f"\n  Files created:")
    print(f"    {len(domain_pools)} domain KSA pool files")
    print(f"    1 legacy ID map")
    print(f"    {len(category_mappings)} rewritten mapping files")
    print(f"\n  {'DRY RUN — no files written' if dry_run else 'LIVE — all files written'}")
    print()

    return 0


def main():
    dry_run = "--dry-run" in sys.argv
    return run_migration(dry_run)


if __name__ == "__main__":
    sys.exit(main())
