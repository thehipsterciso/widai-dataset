#!/usr/bin/env python3
"""
Coverage Gap Test: Can a PE workforce due diligence assessment be run against
the current 37 KSA-covered roles?

This script:
1. Loads all roles and KSAs from the WIDAI dataset
2. Identifies which roles have KSA coverage
3. Defines 5 representative PE portfolio company data/AI team structures
4. Maps team roles to WIDAI roles and checks KSA coverage
5. Outputs a comprehensive coverage report
"""

import json
import os
import sys
from pathlib import Path
from collections import defaultdict
from difflib import SequenceMatcher

# Get the dataset root directory (parent of scripts/)
DATASET_ROOT = Path(__file__).parent.parent

def load_all_roles():
    """Load all role files from roles/ directory."""
    roles_dir = DATASET_ROOT / "roles"
    all_roles = {}

    for role_file in sorted(roles_dir.glob("*.json")):
        with open(role_file) as f:
            data = json.load(f)
            for role in data.get("roles", []):
                role_id = role["role_id"]
                all_roles[role_id] = role

    return all_roles


def load_all_ksas():
    """Load all KSA files from ksas/ directory."""
    ksas_dir = DATASET_ROOT / "ksas"
    all_ksas = {}

    for ksa_file in sorted(ksas_dir.glob("*.json")):
        with open(ksa_file) as f:
            data = json.load(f)
            for ksa in data.get("ksas", []):
                ksa_id = ksa["ksa_id"]
                all_ksas[ksa_id] = ksa

    return all_ksas


def load_ksa_mappings():
    """Load all role-KSA mapping files from mappings/ directory."""
    mappings_dir = DATASET_ROOT / "mappings"
    # Maps role_id -> set of ksa_ids
    role_to_ksas = defaultdict(set)

    for mapping_file in sorted(mappings_dir.glob("role_ksa_*.json")):
        with open(mapping_file) as f:
            data = json.load(f)
            for rel in data.get("relationships", []):
                work_role_id = rel.get("work_role_id")
                ksa_id = rel.get("ksa_id")
                # Store by work_role_id (e.g., WR-DSM-04.01)
                role_to_ksas[work_role_id].add(ksa_id)

    return role_to_ksas


def get_roles_with_ksa_coverage(all_roles, role_to_ksas):
    """Return roles that have at least 1 KSA mapped to them."""
    covered_roles = {}

    for role_id, role in all_roles.items():
        work_role_id = role.get("widai_work_role_id")
        if work_role_id and work_role_id in role_to_ksas:
            ksa_count = len(role_to_ksas[work_role_id])
            if ksa_count > 0:
                covered_roles[role_id] = {
                    "role": role,
                    "ksa_count": ksa_count,
                    "work_role_id": work_role_id
                }

    return covered_roles


def similarity_ratio(a, b):
    """Calculate string similarity ratio (0-1)."""
    return SequenceMatcher(None, a.lower(), b.lower()).ratio()


def find_closest_widai_role(team_role_title, all_roles):
    """
    Find the closest matching WIDAI role by comparing canonical_title
    and key_variants.

    Returns (role_id, role_dict, match_score) or (None, None, 0) if no good match.
    """
    best_match = None
    best_score = 0

    for role_id, role in all_roles.items():
        canonical = role.get("canonical_title", "").lower()
        variants = [v.lower() for v in role.get("key_variants", [])]
        all_titles = [canonical] + variants

        # Check similarity to each title variant
        for title in all_titles:
            score = similarity_ratio(team_role_title.lower(), title)
            if score > best_score:
                best_score = score
                best_match = (role_id, role, score)

    # Only return if score is reasonably high (>0.6 similarity)
    if best_score >= 0.6:
        return best_match
    return None, None, 0


def define_team_structures():
    """Define 5 representative PE portfolio company team structures."""
    teams = {
        "Team A: Early-stage data team": [
            ("Chief Data Officer", 1),
            ("Data Engineer", 3),
            ("Data Scientist", 2),
            ("Data Analyst", 2),
            ("Analytics Engineer", 1),
            ("Data Governance Lead", 1),
        ],
        "Team B: Scale-up with ML": [
            ("Chief Data Officer", 1),
            ("Data Engineer", 3),
            ("Data Scientist", 2),
            ("Data Analyst", 2),
            ("Analytics Engineer", 1),
            ("Data Governance Lead", 1),
            ("ML Engineer", 2),
            ("MLOps Engineer", 1),
            ("AI Engineer", 1),
            ("Data Architect", 1),
            ("Data Platform Engineer", 1),
            ("Privacy Officer", 1),
            ("VP Data", 1),
        ],
        "Team C: Enterprise with AI governance": [
            ("Chief Data Officer", 1),
            ("Data Engineer", 3),
            ("Data Scientist", 2),
            ("Data Analyst", 2),
            ("Analytics Engineer", 1),
            ("Data Governance Lead", 1),
            ("ML Engineer", 2),
            ("MLOps Engineer", 1),
            ("AI Engineer", 1),
            ("Data Architect", 1),
            ("Data Platform Engineer", 1),
            ("Privacy Officer", 1),
            ("VP Data", 1),
            ("Chief Information Security Officer", 1),
            ("AI Governance Manager", 1),
            ("Model Risk Manager", 1),
            ("Data Steward", 3),
            ("VP Analytics", 1),
            ("VP Engineering", 1),
            ("Compliance Manager", 1),
        ],
        "Team D: Regulated industry": [
            ("Model Validator", 1),
            ("AI Auditor", 1),
            ("Data Protection Officer", 1),
            ("Compliance Analyst", 2),
            ("Risk Manager", 1),
            ("Chief Data Officer", 1),
            ("Data Engineer", 2),
            ("Data Scientist", 1),
            ("Data Analyst", 1),
            ("Analytics Engineer", 1),
            ("Privacy Officer", 1),
            ("VP Data", 1),
        ],
        "Team E: AI-native startup": [
            ("AI Engineer", 3),
            ("ML Engineer", 2),
            ("LLMOps Engineer", 1),
            ("RAG Engineer", 1),
            ("Data Engineer", 2),
            ("Product Manager AI", 1),
            ("AI Safety Engineer", 1),
        ],
    }
    return teams


def map_team_to_widai(team_roles, all_roles):
    """
    Map a team composition to WIDAI roles.

    Returns list of (team_role, count, widai_role_id, widai_role, match_score).
    """
    mappings = []

    for team_role, count in team_roles:
        result = find_closest_widai_role(team_role, all_roles)
        widai_role_id, widai_role, score = result

        mappings.append({
            "team_role": team_role,
            "count": count,
            "widai_role_id": widai_role_id,
            "widai_role": widai_role,
            "match_score": score,
        })

    return mappings


def analyze_team_coverage(team_name, team_roles, all_roles, covered_roles, role_to_ksas):
    """Analyze KSA coverage for a single team."""
    mappings = map_team_to_widai(team_roles, all_roles)

    total_positions = sum(m["count"] for m in mappings)
    covered_positions = 0
    covered_details = []
    uncovered_details = []

    for mapping in mappings:
        team_role = mapping["team_role"]
        count = mapping["count"]
        widai_role_id = mapping["widai_role_id"]
        widai_role = mapping["widai_role"]
        score = mapping["match_score"]

        if widai_role_id and widai_role_id in covered_roles:
            ksa_count = covered_roles[widai_role_id]["ksa_count"]
            covered_positions += count
            covered_details.append({
                "team_role": team_role,
                "count": count,
                "widai_role": widai_role.get("canonical_title"),
                "widai_role_id": widai_role_id,
                "ksa_count": ksa_count,
                "match_score": f"{score:.2f}",
            })
        else:
            uncovered_details.append({
                "team_role": team_role,
                "count": count,
                "widai_role": widai_role.get("canonical_title") if widai_role else "NOT FOUND",
                "widai_role_id": widai_role_id,
                "match_score": f"{score:.2f}" if score > 0 else "NO MATCH",
            })

    coverage_pct = (covered_positions / total_positions * 100) if total_positions > 0 else 0

    return {
        "team_name": team_name,
        "total_positions": total_positions,
        "covered_positions": covered_positions,
        "uncovered_positions": total_positions - covered_positions,
        "coverage_pct": coverage_pct,
        "covered_details": covered_details,
        "uncovered_details": uncovered_details,
    }


def get_priority_roles_to_add(all_teams_analysis, all_roles):
    """
    Identify the highest-priority roles to add KSAs for.
    Priority = appears in most teams but lacks KSA coverage.
    """
    uncovered_role_counts = defaultdict(int)
    uncovered_role_info = {}

    for team_analysis in all_teams_analysis:
        for uncovered in team_analysis["uncovered_details"]:
            role_id = uncovered["widai_role_id"]
            if role_id:
                uncovered_role_counts[role_id] += uncovered["count"]
                if role_id not in uncovered_role_info:
                    uncovered_role_info[role_id] = {
                        "widai_role": uncovered["widai_role"],
                        "category": all_roles[role_id].get("category_code") if role_id in all_roles else "UNKNOWN",
                    }

    # Sort by frequency
    sorted_roles = sorted(
        uncovered_role_counts.items(),
        key=lambda x: x[1],
        reverse=True
    )

    return [
        {
            "widai_role_id": role_id,
            "widai_role": uncovered_role_info[role_id]["widai_role"],
            "category": uncovered_role_info[role_id]["category"],
            "appearances": count,
        }
        for role_id, count in sorted_roles[:10]
    ]


def print_report(all_roles, covered_roles, all_teams_analysis, priority_roles):
    """Print the comprehensive coverage report."""

    print("\n" + "="*80)
    print("PE WORKFORCE DUE DILIGENCE ASSESSMENT")
    print("KSA Coverage Analysis for 37 KSA-Covered Roles")
    print("="*80)

    # Section 1: Overall Coverage
    print("\n[1] OVERALL KSA COVERAGE")
    print("-" * 80)
    print(f"Total WIDAI roles loaded:         {len(all_roles)}")
    print(f"Roles with KSA coverage:          {len(covered_roles)}")
    print(f"Coverage rate:                    {len(covered_roles)/len(all_roles)*100:.1f}%")

    # Section 2: Team-by-Team Analysis
    print("\n[2] TEAM COMPOSITION ANALYSIS")
    print("-" * 80)

    for team_analysis in all_teams_analysis:
        team_name = team_analysis["team_name"]
        total = team_analysis["total_positions"]
        covered = team_analysis["covered_positions"]
        uncovered = team_analysis["uncovered_positions"]
        pct = team_analysis["coverage_pct"]

        print(f"\n{team_name}")
        print(f"  Total positions:                {total}")
        print(f"  Covered by KSAs:                {covered} ({pct:.1f}%)")
        print(f"  NOT covered by KSAs:            {uncovered} ({100-pct:.1f}%)")

        if team_analysis["covered_details"]:
            print("\n  ✓ COVERED ROLES:")
            for detail in team_analysis["covered_details"]:
                print(f"    - {detail['team_role']} (x{detail['count']})")
                print(f"      → {detail['widai_role']} ({detail['ksa_count']} KSAs)")
                print(f"      [Match: {detail['match_score']}]")

        if team_analysis["uncovered_details"]:
            print("\n  ✗ UNCOVERED ROLES:")
            for detail in team_analysis["uncovered_details"]:
                status = detail["match_score"] if detail["match_score"] != "NO MATCH" else "NO MATCH FOUND"
                print(f"    - {detail['team_role']} (x{detail['count']})")
                if detail["widai_role"] != "NOT FOUND":
                    print(f"      → {detail['widai_role']} (NO KSAs)")
                    print(f"      [Match: {status}]")
                else:
                    print(f"      → Role not found in WIDAI")

    # Section 3: Assessment Verdict
    print("\n[3] ASSESSMENT VERDICT")
    print("-" * 80)

    all_teams_sufficient = all(t["coverage_pct"] >= 80 for t in all_teams_analysis)

    if all_teams_sufficient:
        verdict = "✓ YES - All representative team compositions have ≥80% KSA coverage"
        assessment = "PASS"
    else:
        insufficient_teams = [t["team_name"] for t in all_teams_analysis if t["coverage_pct"] < 80]
        verdict = f"✗ PARTIAL - {len(insufficient_teams)} teams below 80% coverage: {', '.join(insufficient_teams)}"
        assessment = "NEEDS WORK"

    print(f"\nCan we run a PE assessment on these team compositions?")
    print(f"Answer: {verdict}")
    print(f"Assessment Status: {assessment}")

    # Section 4: Priority Gaps
    print("\n[4] HIGHEST-PRIORITY GAPS (Roles to add KSAs for)")
    print("-" * 80)
    print("\nThese roles appear in multiple team compositions but lack KSA coverage:")
    print("(Ranked by frequency across teams)\n")

    for i, role in enumerate(priority_roles, 1):
        print(f"{i}. {role['widai_role']} ({role['widai_role_id']})")
        print(f"   Category: {role['category']}")
        print(f"   Appears in {role['appearances']} team positions")

    print("\n" + "="*80)
    print("Report generated successfully")
    print("="*80 + "\n")


def main():
    """Main execution."""
    print("Loading WIDAI dataset...")

    # Load data
    all_roles = load_all_roles()
    all_ksas = load_all_ksas()
    role_to_ksas = load_ksa_mappings()
    covered_roles = get_roles_with_ksa_coverage(all_roles, role_to_ksas)

    print(f"  Loaded {len(all_roles)} roles")
    print(f"  Loaded {len(all_ksas)} KSAs")
    print(f"  Found {len(covered_roles)} roles with KSA coverage")

    # Define team structures
    print("\nDefining 5 representative PE portfolio company team structures...")
    teams = define_team_structures()

    # Analyze each team
    print("Analyzing KSA coverage for each team...")
    all_teams_analysis = []
    for team_name, team_roles in teams.items():
        analysis = analyze_team_coverage(team_name, team_roles, all_roles, covered_roles, role_to_ksas)
        all_teams_analysis.append(analysis)

    # Get priority roles to add
    print("Identifying priority gaps...")
    priority_roles = get_priority_roles_to_add(all_teams_analysis, all_roles)

    # Print report
    print_report(all_roles, covered_roles, all_teams_analysis, priority_roles)


if __name__ == "__main__":
    main()
