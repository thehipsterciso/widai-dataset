#!/usr/bin/env python3
"""
WIDAI Adversarial Quality Gate (AQG)

Five-pass adversarial review process for KSA completeness validation.
Modeled on the ensemble brainstorm algorithm's multi-perspective methodology.

This script implements the adversarial stage gate defined in ADR-012.
It does NOT author KSAs — it evaluates whether an existing KSA set for a role
is sufficient for workforce assessment purposes.

The five passes:
  1. Breadth Scan — enumerate expected knowledge domains from source frameworks
  2. Depth Challenge — check whether current KSAs cover each domain
  3. External Benchmark — compare against NICE analog depth
  4. Assessability Test — verify each KSA is observable/scorable
  5. Adversarial Review — PE operating partner perspective challenge

Exit codes:
  0 — All roles pass quality gate
  1 — One or more roles fail quality gate
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
# Domain Coverage Reference
# =============================================================================
# For each WIDAI category, the expected knowledge domains that any role in
# that category should partially address. Derived from source frameworks
# (DAMA DMBOK, NIST AI RMF, NICE, O*NET, SFIA, ISO 42001).
#
# A role doesn't need to cover ALL domains — but any role with <3 domains
# covered is almost certainly too thin.
# =============================================================================

EXPECTED_DOMAINS = {
    "GOV": {
        "domains": [
            "Strategic Planning & Vision",
            "Organizational Design & Structure",
            "Policy Development & Enforcement",
            "Regulatory Compliance & Interpretation",
            "Stakeholder Management & Communication",
            "Budget & Resource Allocation",
            "Risk Management & Oversight",
            "Data Governance Frameworks",
            "AI Governance Frameworks",
            "Ethics & Responsible AI",
            "Vendor & Third-Party Oversight",
            "Metrics & Performance Measurement",
            "Change Management",
            "Cross-Functional Coordination",
        ],
        "min_domain_coverage": 5,
    },
    "ENG": {
        "domains": [
            "Architecture Design & Patterns",
            "Data Modeling & Schema Design",
            "Pipeline Development & Orchestration",
            "Platform Operations & Reliability",
            "Security & Access Control",
            "Performance Optimization & Tuning",
            "Cloud Infrastructure & Services",
            "Data Integration & ETL/ELT",
            "Testing & Validation",
            "Version Control & CI/CD",
            "Monitoring & Observability",
            "Documentation & Standards",
        ],
        "min_domain_coverage": 4,
    },
    "RSK": {
        "domains": [
            "Risk Assessment & Quantification",
            "Regulatory Framework Interpretation",
            "Compliance Monitoring & Reporting",
            "Audit & Assurance",
            "Incident Response & Remediation",
            "Policy Development",
            "Ethical Analysis & Impact Assessment",
            "Security Architecture & Controls",
            "Model Validation & Testing",
            "Third-Party Risk Management",
            "Privacy & Data Protection",
            "Documentation & Evidence Management",
        ],
        "min_domain_coverage": 4,
    },
    "ANL": {
        "domains": [
            "Statistical Analysis & Methods",
            "Data Visualization & Communication",
            "Business Requirements Translation",
            "Data Quality Assessment",
            "Tool & Platform Proficiency",
            "Domain Knowledge Application",
            "Report Development & Delivery",
            "Exploratory Data Analysis",
            "Stakeholder Communication",
            "Data Collection & Preparation",
        ],
        "min_domain_coverage": 4,
    },
    "DEV": {
        "domains": [
            "Algorithm Design & Selection",
            "Model Training & Optimization",
            "Feature Engineering",
            "Experiment Design & Evaluation",
            "Production Deployment & MLOps",
            "Data Preprocessing & Cleaning",
            "Research & Literature Review",
            "Domain Application & Transfer",
            "Tool & Framework Proficiency",
            "Documentation & Reproducibility",
            "Model Interpretability & Explainability",
            "Ethical AI & Bias Detection",
        ],
        "min_domain_coverage": 4,
    },
    "DSM": {
        "domains": [
            "Data Quality Management",
            "Master Data Management",
            "Metadata Management",
            "Data Lifecycle Management",
            "Data Standards & Classification",
            "Privacy & Compliance",
            "Stakeholder Collaboration",
            "Tool & Platform Proficiency",
            "Documentation & Cataloging",
            "Change Management & Governance",
        ],
        "min_domain_coverage": 4,
    },
    "LDR": {
        "domains": [
            "Strategic Vision & Direction",
            "Innovation & Research",
            "Stakeholder Influence & Communication",
            "Team Development & Mentorship",
            "Cross-Functional Leadership",
            "Market & Industry Analysis",
            "Change Management",
            "Vendor & Partnership Management",
        ],
        "min_domain_coverage": 3,
    },
    "OPS": {
        "domains": [
            "Program & Project Management",
            "Process Design & Optimization",
            "Training & Enablement",
            "Communication & Adoption",
            "Metrics & Reporting",
            "Tool Administration & Support",
            "Resource Coordination",
            "Documentation & Knowledge Management",
        ],
        "min_domain_coverage": 3,
    },
}


# =============================================================================
# Assessability Keywords
# =============================================================================
# KSAs containing these vague patterns are flagged for assessability review.
# A PE assessor should be able to determine presence/absence of the capability
# through document review, interview, or artifact inspection.
# =============================================================================

VAGUE_PATTERNS = [
    "general understanding",
    "basic knowledge",
    "awareness of",
    "familiarity with",
    "appreciation for",
    "understanding of various",
    "knowledge of multiple",
    "broad understanding",
    "general principles",
    "various aspects",
]

STRONG_ASSESSMENT_VERBS = [
    "design", "implement", "develop", "configure", "deploy",
    "evaluate", "assess", "audit", "validate", "test",
    "document", "report", "communicate", "present",
    "manage", "coordinate", "lead", "establish",
    "analyze", "interpret", "monitor", "measure",
    "build", "create", "architect", "integrate",
]


class AdversarialQualityGate:
    """Five-pass adversarial quality gate for WIDAI KSA completeness."""

    def __init__(self, base_path):
        self.base = base_path
        self.role_ksas = defaultdict(list)
        self.ksa_details = {}
        self.role_details = {}
        self.role_frameworks = defaultdict(set)
        self.results = {}
        self.errors = []

    def load_json(self, filepath):
        """Load JSON file. Returns (data, error)."""
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                return json.load(f), None
        except Exception as e:
            return None, f"Failed to load {filepath}: {e}"

    def collect_data(self):
        """Load all necessary data."""
        # KSAs (skip metadata files like _legacy_id_map.json)
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
                    self.ksa_details[kid] = ksa

        # Role-KSA mappings
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

        # Role metadata
        roles_dir = os.path.join(self.base, "roles")
        for fp in sorted(glob.glob(os.path.join(roles_dir, "*.json"))):
            data, error = self.load_json(fp)
            if error:
                self.errors.append(error)
                continue
            for role in data.get("roles", []):
                wrid = role.get("atlas_work_role_id")
                if wrid:
                    # Normalize field names for downstream use
                    role["work_role_title"] = role.get("canonical_title", "Unknown")
                    role["atlas_category_code"] = role.get("category_code", "")
                    self.role_details[wrid] = role

        # Role-framework mappings (for breadth scan)
        for fp in sorted(glob.glob(os.path.join(mappings_dir, "roles_to_*.json"))):
            data, error = self.load_json(fp)
            if error:
                continue
            for mapping in data.get("mappings", []):
                rid = mapping.get("role_id")
                fid = mapping.get("framework_id")
                # Find work_role_id for this role_id
                for wrid, details in self.role_details.items():
                    if details.get("role_id") == rid:
                        self.role_frameworks[wrid].add(fid)
                        break

    def pass_1_breadth_scan(self, work_role_id):
        """
        Pass 1: Breadth Scan
        Check how many expected knowledge domains the role's KSAs cover.
        Uses keyword matching against domain descriptions.
        """
        ksa_ids = self.role_ksas.get(work_role_id, [])
        role_info = self.role_details.get(work_role_id, {})
        category = role_info.get("atlas_category_code", "")

        expected = EXPECTED_DOMAINS.get(category, {})
        domains = expected.get("domains", [])
        min_coverage = expected.get("min_domain_coverage", 3)

        if not domains:
            return {
                "pass": "breadth_scan",
                "status": "SKIP",
                "reason": f"No domain reference for category {category}",
                "domains_expected": 0,
                "domains_covered": 0,
                "coverage_ratio": 0,
            }

        # Crude domain matching: check if any KSA statement contains
        # keywords from the domain name
        covered_domains = []
        uncovered_domains = []

        all_statements = " ".join(
            self.ksa_details.get(kid, {}).get("statement", "").lower()
            for kid in ksa_ids
        )

        for domain in domains:
            # Split domain into keywords and check for presence
            keywords = [w.lower() for w in domain.split() if len(w) > 3]
            # Require at least 2 keyword matches or 1 for short domain names
            threshold = min(2, len(keywords))
            matches = sum(1 for kw in keywords if kw in all_statements)
            if matches >= threshold:
                covered_domains.append(domain)
            else:
                uncovered_domains.append(domain)

        coverage_ratio = len(covered_domains) / len(domains) if domains else 0
        passes = len(covered_domains) >= min_coverage

        return {
            "pass": "breadth_scan",
            "status": "PASS" if passes else "FAIL",
            "domains_expected": len(domains),
            "domains_covered": len(covered_domains),
            "domains_uncovered": uncovered_domains[:5],  # Top 5 gaps
            "coverage_ratio": round(coverage_ratio, 3),
            "min_required": min_coverage,
        }

    def pass_2_depth_challenge(self, work_role_id):
        """
        Pass 2: Depth Challenge
        For each KSA type (K, S, T), check whether count meets minimum
        expectations. A role with only Knowledge and no Tasks is unassessable
        in a PE context.
        """
        ksa_ids = self.role_ksas.get(work_role_id, [])
        type_counts = defaultdict(int)

        for kid in ksa_ids:
            ksa_type = self.ksa_details.get(kid, {}).get("type", "unknown")
            type_counts[ksa_type] += 1

        total = len(ksa_ids)

        # Minimum expectations per type
        issues = []
        if type_counts.get("Knowledge", 0) < 3:
            issues.append(f"Knowledge items too thin ({type_counts.get('Knowledge', 0)} < 3 minimum)")
        if type_counts.get("Skill", 0) < 2:
            issues.append(f"Skill items too thin ({type_counts.get('Skill', 0)} < 2 minimum)")
        if type_counts.get("Task", 0) < 2:
            issues.append(f"Task items too thin ({type_counts.get('Task', 0)} < 2 minimum)")

        # Check type balance — no single type should be >70% of total
        for ktype, count in type_counts.items():
            if total > 0 and count / total > 0.70:
                issues.append(f"{ktype} dominates at {count/total:.0%} — unbalanced KSA distribution")

        return {
            "pass": "depth_challenge",
            "status": "PASS" if not issues else "FAIL",
            "total_ksas": total,
            "type_counts": dict(type_counts),
            "issues": issues,
        }

    # NICE Framework v2.1.0 benchmark (inline to avoid cross-script import issues)
    NICE_MEAN_TOTAL = 133.25  # Mean KSAs per role across 4 sampled NICE roles

    def pass_3_external_benchmark(self, work_role_id):
        """
        Pass 3: External Benchmark
        Compare KSA count against NICE framework mean.
        Flag if <25% of benchmark depth (per ADR-012).
        """
        nice_mean = self.NICE_MEAN_TOTAL
        ksa_ids = self.role_ksas.get(work_role_id, [])
        total = len(ksa_ids)
        ratio = total / nice_mean if nice_mean > 0 else 0

        return {
            "pass": "external_benchmark",
            "status": "PASS" if ratio >= 0.25 else "FAIL",
            "atlas_count": total,
            "nice_mean": round(nice_mean, 1),
            "ratio": round(ratio, 4),
            "ratio_pct": round(ratio * 100, 1),
            "threshold": "25% of NICE mean",
            "threshold_value": round(nice_mean * 0.25),
        }

    def pass_4_assessability(self, work_role_id):
        """
        Pass 4: Assessability Test
        Check each KSA statement for assessability markers.
        Flag vague statements. Score overall assessability.
        """
        ksa_ids = self.role_ksas.get(work_role_id, [])
        vague_ksas = []
        strong_ksas = []
        neutral_ksas = []

        for kid in ksa_ids:
            statement = self.ksa_details.get(kid, {}).get("statement", "").lower()

            is_vague = any(pattern in statement for pattern in VAGUE_PATTERNS)
            is_strong = any(verb in statement for verb in STRONG_ASSESSMENT_VERBS)

            if is_vague:
                vague_ksas.append(kid)
            elif is_strong:
                strong_ksas.append(kid)
            else:
                neutral_ksas.append(kid)

        total = len(ksa_ids)
        assessability_score = (
            (len(strong_ksas) * 1.0 + len(neutral_ksas) * 0.7 + len(vague_ksas) * 0.3) / total
            if total > 0 else 0
        )

        vague_ratio = len(vague_ksas) / total if total > 0 else 0

        return {
            "pass": "assessability",
            "status": "PASS" if vague_ratio < 0.20 else "FAIL",
            "total_ksas": total,
            "strong_count": len(strong_ksas),
            "neutral_count": len(neutral_ksas),
            "vague_count": len(vague_ksas),
            "vague_ratio": round(vague_ratio, 3),
            "assessability_score": round(assessability_score, 3),
            "vague_ksa_ids": vague_ksas[:5],  # Show first 5
        }

    def pass_5_adversarial_review(self, work_role_id):
        """
        Pass 5: Adversarial Review (PE Operating Partner Perspective)

        Asks: "If I hired against this KSA set, would I miss any
        critical capability?"

        Checks:
        - Framework source count (more sources = better coverage)
        - Seniority-appropriate depth (senior roles need more KSAs)
        - Regulatory role completeness
        """
        ksa_ids = self.role_ksas.get(work_role_id, [])
        role_info = self.role_details.get(work_role_id, {})
        total = len(ksa_ids)

        issues = []

        # Check: Does the role have mappings from multiple source frameworks?
        fw_count = len(self.role_frameworks.get(work_role_id, set()))
        if fw_count < 2:
            issues.append(f"Only {fw_count} source framework(s) — single-source roles miss cross-cutting competencies")

        # Check: Seniority-appropriate depth
        seniority = role_info.get("seniority_level", "").lower()
        if seniority in ["director", "senior", "executive", "c-suite"] and total < 15:
            issues.append(f"Senior/executive role with only {total} KSAs — likely missing strategic and leadership competencies")
        elif seniority in ["mid", "mid-senior"] and total < 10:
            issues.append(f"Mid-level role with only {total} KSAs — likely missing operational depth")

        # Check: Can a PE assessor differentiate performance levels?
        # With <10 KSAs, there's not enough granularity to distinguish
        # "adequate" from "exceptional" in assessment scoring
        if total < 10:
            issues.append(f"Only {total} KSAs — insufficient granularity for PE assessment scoring differentiation")

        # Check: Does the role have Task-type KSAs? (Tasks are the most
        # directly assessable — you can ask "show me evidence of this task")
        type_counts = defaultdict(int)
        for kid in ksa_ids:
            ksa_type = self.ksa_details.get(kid, {}).get("type", "unknown")
            type_counts[ksa_type] += 1

        if type_counts.get("Task", 0) == 0:
            issues.append("No Task-type KSAs — assessor cannot ask 'show me evidence of doing X'")

        return {
            "pass": "adversarial_review",
            "status": "PASS" if not issues else "FAIL",
            "framework_sources": fw_count,
            "seniority": seniority,
            "total_ksas": total,
            "issues": issues,
        }

    def evaluate_role(self, work_role_id):
        """Run all 5 passes for a single role."""
        passes = [
            self.pass_1_breadth_scan(work_role_id),
            self.pass_2_depth_challenge(work_role_id),
            self.pass_3_external_benchmark(work_role_id),
            self.pass_4_assessability(work_role_id),
            self.pass_5_adversarial_review(work_role_id),
        ]

        # Aggregate
        pass_count = sum(1 for p in passes if p["status"] == "PASS")
        fail_count = sum(1 for p in passes if p["status"] == "FAIL")
        skip_count = sum(1 for p in passes if p["status"] == "SKIP")

        # Gate logic: FAIL if any critical pass fails
        # Critical passes: external_benchmark (3), adversarial_review (5)
        critical_failures = [
            p for p in passes
            if p["status"] == "FAIL" and p["pass"] in ("external_benchmark", "adversarial_review")
        ]

        overall_status = "FAIL" if critical_failures or fail_count >= 3 else "PASS"

        role_info = self.role_details.get(work_role_id, {})

        return {
            "work_role_id": work_role_id,
            "title": role_info.get("work_role_title", "Unknown"),
            "category": role_info.get("atlas_category_code", ""),
            "overall_status": overall_status,
            "passes_passed": pass_count,
            "passes_failed": fail_count,
            "passes_skipped": skip_count,
            "pass_results": passes,
        }

    def run_gate(self):
        """Run adversarial quality gate across all mapped roles."""
        print("\n" + "=" * 70)
        print("WIDAI ADVERSARIAL QUALITY GATE (AQG)")
        print("=" * 70)
        print(f"\n  Five-pass adversarial review per ADR-012")
        print(f"  Pass 1: Breadth Scan — domain coverage against category reference")
        print(f"  Pass 2: Depth Challenge — type balance and minimum counts")
        print(f"  Pass 3: External Benchmark — NICE framework comparison")
        print(f"  Pass 4: Assessability Test — statement clarity and observability")
        print(f"  Pass 5: Adversarial Review — PE operating partner perspective\n")

        self.collect_data()
        if self.errors:
            print("ERRORS loading data:")
            for e in self.errors:
                print(f"  ✗ {e}")
            return 2

        if not self.role_ksas:
            print("No role-KSA mappings found.")
            return 2

        # Evaluate each mapped role
        gate_failures = []
        for wrid in sorted(self.role_ksas.keys()):
            result = self.evaluate_role(wrid)
            self.results[wrid] = result
            if result["overall_status"] == "FAIL":
                gate_failures.append(result)

        # Print summary
        print("-" * 70)
        print(f"{'Role':<42} {'P1':>4} {'P2':>4} {'P3':>4} {'P4':>4} {'P5':>4} {'Gate':>6}")
        print("-" * 70)

        for wrid in sorted(self.results.keys()):
            r = self.results[wrid]
            title = r["title"][:40]
            statuses = []
            for p in r["pass_results"]:
                s = p["status"]
                statuses.append("✓" if s == "PASS" else ("✗" if s == "FAIL" else "—"))
            gate = "✓ PASS" if r["overall_status"] == "PASS" else "✗ FAIL"
            print(f"  {title:<40} {statuses[0]:>4} {statuses[1]:>4} {statuses[2]:>4} {statuses[3]:>4} {statuses[4]:>4} {gate}")

        # Aggregate stats
        total_roles = len(self.results)
        passing = total_roles - len(gate_failures)

        print(f"\n" + "=" * 70)
        print("GATE RESULT")
        print("=" * 70)

        if gate_failures:
            print(f"\n  ✗ GATE FAILED — {len(gate_failures)} of {total_roles} roles did not pass\n")

            # Aggregate all issues
            all_issues = []
            for r in gate_failures:
                for p in r["pass_results"]:
                    if p["status"] == "FAIL":
                        for issue in p.get("issues", []):
                            all_issues.append(f"  [{r['title'][:30]}] {issue}")
                        if "domains_uncovered" in p and p.get("domains_uncovered"):
                            all_issues.append(
                                f"  [{r['title'][:30]}] Uncovered domains: {', '.join(p['domains_uncovered'][:3])}"
                            )

            if all_issues:
                print("  Top issues:")
                for issue in all_issues[:20]:
                    print(f"    {issue}")

            return 1
        else:
            print(f"\n  ✓ GATE PASSED — all {total_roles} roles pass adversarial review\n")
            return 0

    def write_results_json(self):
        """Write machine-readable results."""
        output = {
            "analysis": "Adversarial Quality Gate",
            "analysis_date": datetime.now().strftime("%Y-%m-%d"),
            "adr": "ADR-012",
            "methodology": "5-pass adversarial review (breadth, depth, benchmark, assessability, adversarial)",
            "results": {
                "total_roles_evaluated": len(self.results),
                "roles_passing": sum(1 for r in self.results.values() if r["overall_status"] == "PASS"),
                "roles_failing": sum(1 for r in self.results.values() if r["overall_status"] == "FAIL"),
                "per_role": {wrid: result for wrid, result in self.results.items()},
            },
        }

        output_path = os.path.join(self.base, "docs", "roadmap", "aqg-analysis.json")
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(output, f, indent=2, default=str)
        print(f"\n  Results written to: docs/roadmap/aqg-analysis.json")


def main():
    """Entry point."""
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    gate = AdversarialQualityGate(base)
    exit_code = gate.run_gate()
    if gate.results:
        gate.write_results_json()
    return exit_code


if __name__ == "__main__":
    sys.exit(main())
