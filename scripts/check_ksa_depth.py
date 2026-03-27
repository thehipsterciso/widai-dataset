#!/usr/bin/env python3
"""
ATLAS KSA Depth Coverage Index (DCI)

Measures whether each mapped role has sufficient KSA depth to support
meaningful workforce assessment. Benchmarks against the NIST NICE Framework
v2.1.0 as the industry reference for machine-readable KSA-per-role standards.

This script implements the corrective measure defined in ADR-012:
- Per-role Depth Coverage Index (DCI) score
- Dataset-wide aggregate DCI
- Minimum depth thresholds with CI/CD gate enforcement
- NICE framework benchmark comparison

Reference benchmarks (NICE v2.1.0, sampled from NICCS.CISA.GOV):
  Defensive Cybersecurity:        206 KSAs (43T, 125K, 38S)
  Secure Software Development:    159 KSAs (48T, 87K, 24S)
  Executive Cybersecurity Leadership: 100 KSAs (37T, 45K, 18S)
  Cybersecurity Policy & Planning:  68 KSAs (25T, 34K, 9S)
  Mean:                           133.3 KSAs per role

Exit codes:
  0 — All roles meet minimum depth thresholds
  1 — One or more roles below threshold (CI/CD gate failure)
  2 — Data loading error

ADR: ADR-012-ksa-depth-correction.md
"""

import json
import os
import sys
import glob
from collections import defaultdict
from datetime import datetime

# =============================================================================
# NICE Framework v2.1.0 Benchmark Data
# Sampled from NICCS.CISA.GOV on 2026-03-27
# =============================================================================

NICE_BENCHMARKS = {
    "PD-WRL-001": {
        "name": "Defensive Cybersecurity",
        "tasks": 43, "knowledge": 125, "skills": 38, "total": 206
    },
    "DD-WRL-003": {
        "name": "Secure Software Development",
        "tasks": 48, "knowledge": 87, "skills": 24, "total": 159
    },
    "OG-WRL-007": {
        "name": "Executive Cybersecurity Leadership",
        "tasks": 37, "knowledge": 45, "skills": 18, "total": 100
    },
    "OG-WRL-002": {
        "name": "Cybersecurity Policy and Planning",
        "tasks": 25, "knowledge": 34, "skills": 9, "total": 68
    },
}

NICE_MEAN_TOTAL = sum(b["total"] for b in NICE_BENCHMARKS.values()) / len(NICE_BENCHMARKS)
NICE_MIN_TOTAL = min(b["total"] for b in NICE_BENCHMARKS.values())
NICE_MAX_TOTAL = max(b["total"] for b in NICE_BENCHMARKS.values())

# Mean breakdown by type
NICE_MEAN_TASKS = sum(b["tasks"] for b in NICE_BENCHMARKS.values()) / len(NICE_BENCHMARKS)
NICE_MEAN_KNOWLEDGE = sum(b["knowledge"] for b in NICE_BENCHMARKS.values()) / len(NICE_BENCHMARKS)
NICE_MEAN_SKILLS = sum(b["skills"] for b in NICE_BENCHMARKS.values()) / len(NICE_BENCHMARKS)

# =============================================================================
# Thresholds (per ADR-012)
# =============================================================================

# Absolute minimum KSAs per role — roles below this FAIL the gate
MINIMUM_DEPTH_STANDARD = 40

# Elevated minimum for regulatory-assessment roles
MINIMUM_DEPTH_REGULATORY = 60

# Regulatory-assessment role work_role_ids (require higher depth)
REGULATORY_ROLE_IDS = {
    "WR-GOV-01.07",  # Data Protection Officer
    "WR-RSK-06.05",  # Model Risk Manager
    "WR-RSK-06.01",  # AI Risk and Ethics Specialist
    "WR-GOV-01.04",  # Data Governance Director
    "WR-GOV-01.05",  # AI Governance Manager
}

# DCI score bands
DCI_BANDS = {
    "Critical": (0, 0.15),      # <15% of NICE mean
    "Deficient": (0.15, 0.30),  # 15-30% of NICE mean
    "Developing": (0.30, 0.50), # 30-50% of NICE mean
    "Adequate": (0.50, 0.75),   # 50-75% of NICE mean
    "Strong": (0.75, 1.0),      # 75-100% of NICE mean
    "Comprehensive": (1.0, float("inf")),  # ≥100% of NICE mean
}

# Target DCI for gate passage: "Developing" or above (≥30% of NICE mean)
# This translates to the 40-KSA minimum (40/133.3 = 30%)
DCI_GATE_THRESHOLD = MINIMUM_DEPTH_STANDARD / NICE_MEAN_TOTAL


class DepthCoverageIndex:
    """Calculates KSA depth metrics for every mapped role in ATLAS."""

    def __init__(self, base_path):
        self.base = base_path
        self.errors = []
        self.warnings = []
        self.role_ksas = defaultdict(list)  # work_role_id -> list of ksa_ids
        self.ksa_details = {}  # ksa_id -> {type, statement, ...}
        self.role_details = {}  # work_role_id -> {title, category, ...}
        self.results = []

    def load_json(self, filepath):
        """Load JSON file. Returns (data, error)."""
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                return json.load(f), None
        except Exception as e:
            return None, f"Failed to load {filepath}: {e}"

    def collect_data(self):
        """Load all KSAs, mappings, and role metadata."""
        # Load KSAs (skip metadata files like _legacy_id_map.json)
        ksas_dir = os.path.join(self.base, "ksas")
        for fp in sorted(glob.glob(os.path.join(ksas_dir, "*.json"))):
            if os.path.basename(fp).startswith("_"):
                continue
            data, error = self.load_json(fp)
            if error:
                self.errors.append(error)
                continue
            for ksa in data.get("ksas", []):
                kid = ksa.get("ksa_id")
                if kid:
                    self.ksa_details[kid] = {
                        "type": ksa.get("type", "unknown"),
                        "statement": ksa.get("statement", ""),
                        "domain": ksa.get("domain", ""),
                        "domain_code": ksa.get("domain_code", ""),
                    }

        # Load role-KSA mappings
        mappings_dir = os.path.join(self.base, "mappings")
        for fp in sorted(glob.glob(os.path.join(mappings_dir, "role_ksa_*.json"))):
            data, error = self.load_json(fp)
            if error:
                self.errors.append(error)
                continue
            for rel in data.get("relationships", []):
                wrid = rel.get("work_role_id")
                kid = rel.get("ksa_id")
                if wrid and kid:
                    self.role_ksas[wrid].append(kid)

        # Load role metadata
        roles_dir = os.path.join(self.base, "roles")
        for fp in sorted(glob.glob(os.path.join(roles_dir, "*.json"))):
            data, error = self.load_json(fp)
            if error:
                self.errors.append(error)
                continue
            for role in data.get("roles", []):
                wrid = role.get("atlas_work_role_id")
                if wrid:
                    self.role_details[wrid] = {
                        "title": role.get("canonical_title", "Unknown"),
                        "category": role.get("category_code", ""),
                        "role_id": role.get("role_id", ""),
                        "seniority": role.get("seniority_level", ""),
                    }

    def calculate_role_dci(self, work_role_id):
        """
        Calculate Depth Coverage Index for a single role.

        DCI = (role_ksa_count / NICE_mean_total)

        Returns dict with:
          - work_role_id, title, category
          - total_ksas, knowledge_count, skill_count, task_count
          - dci_score (0.0-1.0+, ratio to NICE mean)
          - dci_band (Critical/Deficient/Developing/Adequate/Strong/Comprehensive)
          - minimum_threshold (40 or 60 depending on role type)
          - passes_gate (bool)
        """
        ksa_ids = self.role_ksas.get(work_role_id, [])
        total = len(ksa_ids)

        # Count by type
        type_counts = defaultdict(int)
        for kid in ksa_ids:
            ksa_type = self.ksa_details.get(kid, {}).get("type", "unknown")
            type_counts[ksa_type] += 1

        # DCI score
        dci_score = total / NICE_MEAN_TOTAL if NICE_MEAN_TOTAL > 0 else 0

        # Determine band
        dci_band = "Critical"
        for band_name, (low, high) in DCI_BANDS.items():
            if low <= dci_score < high:
                dci_band = band_name
                break

        # Determine minimum threshold
        is_regulatory = work_role_id in REGULATORY_ROLE_IDS
        min_threshold = MINIMUM_DEPTH_REGULATORY if is_regulatory else MINIMUM_DEPTH_STANDARD

        # Gate check
        passes_gate = total >= min_threshold

        role_info = self.role_details.get(work_role_id, {})

        return {
            "work_role_id": work_role_id,
            "title": role_info.get("title", "Unknown"),
            "category": role_info.get("category", ""),
            "role_id": role_info.get("role_id", ""),
            "total_ksas": total,
            "knowledge_count": type_counts.get("Knowledge", 0),
            "skill_count": type_counts.get("Skill", 0),
            "task_count": type_counts.get("Task", 0),
            "ability_count": type_counts.get("Ability", 0),
            "dci_score": round(dci_score, 4),
            "dci_percentage": round(dci_score * 100, 1),
            "dci_band": dci_band,
            "minimum_threshold": min_threshold,
            "is_regulatory_role": is_regulatory,
            "passes_gate": passes_gate,
            "gap_to_threshold": max(0, min_threshold - total),
            "gap_to_nice_mean": max(0, round(NICE_MEAN_TOTAL) - total),
        }

    def calculate_type_distribution_index(self, work_role_id):
        """
        Calculate how well a role's KSA type distribution matches NICE norms.

        NICE distribution (mean): 28.7% Tasks, 54.6% Knowledge, 16.7% Skills
        A balanced role should have representation across all three types.

        Returns a distribution balance score (0-1) where 1 = perfectly balanced
        per NICE proportions.
        """
        ksa_ids = self.role_ksas.get(work_role_id, [])
        total = len(ksa_ids)
        if total == 0:
            return 0.0

        type_counts = defaultdict(int)
        for kid in ksa_ids:
            ksa_type = self.ksa_details.get(kid, {}).get("type", "unknown")
            type_counts[ksa_type] += 1

        # NICE reference proportions
        nice_props = {
            "Task": NICE_MEAN_TASKS / NICE_MEAN_TOTAL,
            "Knowledge": NICE_MEAN_KNOWLEDGE / NICE_MEAN_TOTAL,
            "Skill": NICE_MEAN_SKILLS / NICE_MEAN_TOTAL,
        }

        # Actual proportions
        actual_props = {
            "Task": type_counts.get("Task", 0) / total,
            "Knowledge": type_counts.get("Knowledge", 0) / total,
            "Skill": type_counts.get("Skill", 0) / total,
        }

        # Calculate cosine similarity between distributions
        import math
        dot_product = sum(nice_props[t] * actual_props[t] for t in nice_props)
        nice_mag = math.sqrt(sum(v ** 2 for v in nice_props.values()))
        actual_mag = math.sqrt(sum(v ** 2 for v in actual_props.values()))

        if nice_mag == 0 or actual_mag == 0:
            return 0.0

        return round(dot_product / (nice_mag * actual_mag), 4)

    def run_analysis(self):
        """Run full DCI analysis across all mapped roles."""
        print("\n" + "=" * 70)
        print("ATLAS KSA DEPTH COVERAGE INDEX (DCI)")
        print("=" * 70)
        print(f"\nBenchmark: NIST NICE Framework v2.1.0")
        print(f"  NICE mean KSAs/role: {NICE_MEAN_TOTAL:.1f}")
        print(f"  NICE range: {NICE_MIN_TOTAL} - {NICE_MAX_TOTAL}")
        print(f"  NICE type distribution: {NICE_MEAN_TASKS:.1f}T / {NICE_MEAN_KNOWLEDGE:.1f}K / {NICE_MEAN_SKILLS:.1f}S")
        print(f"\nATLAS thresholds:")
        print(f"  Standard minimum: {MINIMUM_DEPTH_STANDARD} KSAs/role")
        print(f"  Regulatory minimum: {MINIMUM_DEPTH_REGULATORY} KSAs/role")
        print(f"  DCI gate threshold: {DCI_GATE_THRESHOLD:.2%} of NICE mean\n")

        self.collect_data()
        if self.errors:
            print("ERRORS loading data:")
            for e in self.errors:
                print(f"  ✗ {e}")
            return 2

        if not self.role_ksas:
            print("No role-KSA mappings found.")
            return 2

        # Calculate per-role DCI
        gate_failures = []
        for wrid in sorted(self.role_ksas.keys()):
            result = self.calculate_role_dci(wrid)
            result["distribution_score"] = self.calculate_type_distribution_index(wrid)
            self.results.append(result)
            if not result["passes_gate"]:
                gate_failures.append(result)

        # Print per-role results
        print("-" * 70)
        print(f"{'Role':<45} {'KSAs':>5} {'DCI':>7} {'Band':<14} {'Gate':>6}")
        print("-" * 70)

        for r in sorted(self.results, key=lambda x: x["dci_score"]):
            gate_status = "✓ PASS" if r["passes_gate"] else "✗ FAIL"
            reg_marker = " (R)" if r["is_regulatory_role"] else ""
            title = r["title"][:40] + reg_marker
            print(f"  {title:<43} {r['total_ksas']:>5} {r['dci_percentage']:>6.1f}% {r['dci_band']:<14} {gate_status}")

        # Dataset-wide aggregate
        total_ksas = sum(r["total_ksas"] for r in self.results)
        mapped_roles = len(self.results)
        mean_ksas = total_ksas / mapped_roles if mapped_roles > 0 else 0
        dataset_dci = mean_ksas / NICE_MEAN_TOTAL if NICE_MEAN_TOTAL > 0 else 0

        print("\n" + "=" * 70)
        print("DATASET AGGREGATE")
        print("=" * 70)
        print(f"\n  Mapped roles:          {mapped_roles}")
        print(f"  Total KSA mappings:    {total_ksas}")
        print(f"  Mean KSAs/role:        {mean_ksas:.1f}")
        print(f"  Dataset DCI:           {dataset_dci:.1%} of NICE mean")
        print(f"  KSAs needed (min 40):  {sum(r['gap_to_threshold'] for r in self.results)}")
        print(f"  KSAs needed (NICE eq): {sum(r['gap_to_nice_mean'] for r in self.results)}")

        # Band distribution
        band_counts = defaultdict(int)
        for r in self.results:
            band_counts[r["dci_band"]] += 1

        print(f"\n  Band Distribution:")
        for band_name in ["Critical", "Deficient", "Developing", "Adequate", "Strong", "Comprehensive"]:
            count = band_counts.get(band_name, 0)
            pct = count / mapped_roles * 100 if mapped_roles > 0 else 0
            bar = "█" * int(pct / 2)
            print(f"    {band_name:<15} {count:>3} ({pct:>5.1f}%) {bar}")

        # Gate results
        print(f"\n" + "=" * 70)
        print("GATE RESULT")
        print("=" * 70)

        if gate_failures:
            print(f"\n  ✗ GATE FAILED — {len(gate_failures)} of {mapped_roles} roles below minimum depth\n")
            for r in sorted(gate_failures, key=lambda x: x["total_ksas"]):
                req = r["minimum_threshold"]
                gap = r["gap_to_threshold"]
                print(f"    {r['title']:<40} has {r['total_ksas']:>3} KSAs, needs {req} (gap: {gap})")
            print(f"\n  Total KSAs needed to pass gate: {sum(r['gap_to_threshold'] for r in gate_failures)}")
            return 1
        else:
            print(f"\n  ✓ GATE PASSED — all {mapped_roles} roles meet minimum depth thresholds\n")
            return 0

    def write_results_json(self):
        """Write machine-readable results to docs/roadmap/."""
        output = {
            "analysis": "KSA Depth Coverage Index",
            "analysis_date": datetime.now().strftime("%Y-%m-%d"),
            "adr": "ADR-012",
            "benchmark": {
                "framework": "NIST NICE v2.1.0",
                "source": "NICCS.CISA.GOV",
                "sampled_roles": len(NICE_BENCHMARKS),
                "mean_total": round(NICE_MEAN_TOTAL, 1),
                "min_total": NICE_MIN_TOTAL,
                "max_total": NICE_MAX_TOTAL,
                "mean_tasks": round(NICE_MEAN_TASKS, 1),
                "mean_knowledge": round(NICE_MEAN_KNOWLEDGE, 1),
                "mean_skills": round(NICE_MEAN_SKILLS, 1),
                "roles": {k: v for k, v in NICE_BENCHMARKS.items()},
            },
            "thresholds": {
                "standard_minimum": MINIMUM_DEPTH_STANDARD,
                "regulatory_minimum": MINIMUM_DEPTH_REGULATORY,
                "dci_gate_threshold": round(DCI_GATE_THRESHOLD, 4),
                "regulatory_role_ids": sorted(REGULATORY_ROLE_IDS),
            },
            "results": {
                "mapped_roles": len(self.results),
                "total_ksas": sum(r["total_ksas"] for r in self.results),
                "mean_ksas_per_role": round(
                    sum(r["total_ksas"] for r in self.results) / len(self.results), 1
                ) if self.results else 0,
                "dataset_dci": round(
                    (sum(r["total_ksas"] for r in self.results) / len(self.results) / NICE_MEAN_TOTAL), 4
                ) if self.results else 0,
                "roles_passing_gate": sum(1 for r in self.results if r["passes_gate"]),
                "roles_failing_gate": sum(1 for r in self.results if not r["passes_gate"]),
                "ksas_needed_for_gate": sum(r["gap_to_threshold"] for r in self.results),
                "per_role": self.results,
            },
        }

        output_path = os.path.join(self.base, "docs", "roadmap", "dci-analysis.json")
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(output, f, indent=2)
        print(f"\n  Results written to: docs/roadmap/dci-analysis.json")

        return output


def main():
    """Entry point."""
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    analyzer = DepthCoverageIndex(base)
    exit_code = analyzer.run_analysis()
    if analyzer.results:
        analyzer.write_results_json()
    return exit_code


if __name__ == "__main__":
    sys.exit(main())
