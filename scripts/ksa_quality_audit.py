#!/usr/bin/env python3
"""
WIDAI KSA Quality Audit Script

Audits the quality and consistency of KSA data across all categories.
"""

import json
import os
from pathlib import Path
from collections import defaultdict, Counter
from difflib import SequenceMatcher
from typing import Dict, List, Set, Tuple
import statistics

class KSAQualityAudit:
    def __init__(self, base_path: str):
        self.base_path = Path(base_path)
        self.ksas_dir = self.base_path / "ksas"
        self.mappings_dir = self.base_path / "mappings"
        self.roles_dir = self.base_path / "roles"

        # Data containers
        self.all_ksas = {}  # {category: {ksa_id: ksa_record}}
        self.all_mappings = {}  # {category: [relationships]}
        self.all_roles = {}  # {category: [roles]}
        self.categories = set()

        # Quality findings
        self.findings = defaultdict(list)
        self.warnings = defaultdict(list)
        self.errors = []

    def load_data(self):
        """Load all KSA, mapping, and role data."""
        print("Loading KSA files...")
        for ksa_file in sorted(self.ksas_dir.glob("*_ksas.json")):
            category = ksa_file.stem.replace("_ksas", "")
            with open(ksa_file) as f:
                data = json.load(f)
                self.all_ksas[category] = {ksa["ksa_id"]: ksa for ksa in data.get("ksas", [])}
                self.categories.add(category)

        print("Loading role-KSA mapping files...")
        for mapping_file in sorted(self.mappings_dir.glob("role_ksa_*.json")):
            category = mapping_file.stem.replace("role_ksa_", "")
            with open(mapping_file) as f:
                data = json.load(f)
                self.all_mappings[category] = data.get("relationships", [])
                self.categories.add(category)

        print("Loading role files...")
        for role_file in sorted(self.roles_dir.glob("*.json")):
            category = role_file.stem
            if category == "widai_manifest":
                continue
            with open(role_file) as f:
                data = json.load(f)
                self.all_roles[category] = data.get("roles", [])
                self.categories.add(category)

    def audit_per_category_stats(self):
        """Analyze per-category KSA statistics."""
        print("\n=== CATEGORY STATISTICS ===\n")

        category_stats = {}

        for category in sorted(self.categories):
            if category not in self.all_ksas:
                continue

            ksas = self.all_ksas[category]
            mappings = self.all_mappings.get(category, [])
            roles = self.all_roles.get(category, [])

            # Basic counts
            ksa_count = len(ksas)
            role_count = len(roles)

            # KSA type distribution
            type_counter = Counter(ksa.get("type", "Unknown") for ksa in ksas.values())

            # Average text length
            text_lengths = [len(ksa.get("statement", "")) for ksa in ksas.values()]
            avg_text_length = statistics.mean(text_lengths) if text_lengths else 0

            # KSAs per role
            role_ksa_counts = defaultdict(int)
            for rel in mappings:
                role_id = rel.get("work_role_id")
                role_ksa_counts[role_id] += 1

            if role_ksa_counts:
                ksa_per_role_values = list(role_ksa_counts.values())
                avg_ksa_per_role = statistics.mean(ksa_per_role_values)
                min_ksa_per_role = min(ksa_per_role_values)
                max_ksa_per_role = max(ksa_per_role_values)
                roles_with_ksas = len(role_ksa_counts)
                roles_without_ksas = role_count - roles_with_ksas
            else:
                avg_ksa_per_role = 0
                min_ksa_per_role = 0
                max_ksa_per_role = 0
                roles_with_ksas = 0
                roles_without_ksas = role_count

            category_stats[category] = {
                "ksa_count": ksa_count,
                "role_count": role_count,
                "type_distribution": dict(type_counter),
                "avg_text_length": round(avg_text_length, 1),
                "avg_ksa_per_role": round(avg_ksa_per_role, 2),
                "min_ksa_per_role": min_ksa_per_role,
                "max_ksa_per_role": max_ksa_per_role,
                "roles_with_ksas": roles_with_ksas,
                "roles_without_ksas": roles_without_ksas,
            }

            print(f"{category}:")
            print(f"  KSA Count: {ksa_count}")
            print(f"  Role Count: {role_count}")
            print(f"  Type Distribution: {dict(type_counter)}")
            print(f"  Avg Text Length: {round(avg_text_length, 1)} chars")
            print(f"  Avg KSAs per Role: {round(avg_ksa_per_role, 2)}")
            print(f"  KSA Range per Role: {min_ksa_per_role} - {max_ksa_per_role}")
            print(f"  Roles with KSAs: {roles_with_ksas}/{role_count}")
            if roles_without_ksas > 0:
                print(f"  ⚠️  Roles without KSAs: {roles_without_ksas}")
                self.warnings[category].append(f"{roles_without_ksas} roles have no KSA mappings")
            print()

        return category_stats

    def audit_cross_category_consistency(self):
        """Check for cross-category consistency issues."""
        print("\n=== CROSS-CATEGORY CONSISTENCY CHECKS ===\n")

        # Check 1: KSA ID uniqueness
        all_ksa_ids = {}
        for category, ksas in self.all_ksas.items():
            for ksa_id in ksas:
                if ksa_id in all_ksa_ids:
                    self.errors.append(f"Duplicate KSA ID '{ksa_id}' found in {category} and {all_ksa_ids[ksa_id]}")
                else:
                    all_ksa_ids[ksa_id] = category

        if not self.errors:
            print("✓ All KSA IDs are unique across the dataset")
        else:
            print(f"✗ Found {len(self.errors)} duplicate KSA IDs")
        print()

        # Check 2: Referenced KSA IDs exist
        print("Checking if all referenced KSA IDs exist...")
        missing_ksas = set()
        for category, mappings in self.all_mappings.items():
            for rel in mappings:
                ksa_id = rel.get("ksa_id")
                if ksa_id not in all_ksa_ids:
                    missing_ksas.add(ksa_id)

        if missing_ksas:
            self.errors.append(f"Found {len(missing_ksas)} KSA IDs referenced in mappings but not defined in KSA files")
            for ksa_id in sorted(missing_ksas):
                self.errors.append(f"  - {ksa_id}")
            print(f"✗ {len(missing_ksas)} missing KSA IDs")
        else:
            print("✓ All referenced KSA IDs exist in KSA files")
        print()

        # Check 3: Role IDs exist in role files
        print("Checking if all work role IDs in mappings exist...")
        all_work_role_ids = {}
        for category, roles in self.all_roles.items():
            for role in roles:
                if "atlas_work_role_id" in role and role["atlas_work_role_id"]:
                    all_work_role_ids[role["atlas_work_role_id"]] = (category, role.get("canonical_title"))

        missing_roles = set()
        for category, mappings in self.all_mappings.items():
            for rel in mappings:
                work_role_id = rel.get("work_role_id")
                if work_role_id not in all_work_role_ids:
                    missing_roles.add(work_role_id)

        if missing_roles:
            self.errors.append(f"Found {len(missing_roles)} work role IDs in mappings but not defined in role files")
            for role_id in sorted(missing_roles):
                self.errors.append(f"  - {role_id}")
            print(f"✗ {len(missing_roles)} missing work role IDs")
        else:
            print("✓ All work role IDs in mappings exist in role files")
        print()

        # Check 4: Orphaned KSAs
        print("Checking for orphaned KSAs...")
        referenced_ksa_ids = set()
        for mappings in self.all_mappings.values():
            for rel in mappings:
                referenced_ksa_ids.add(rel.get("ksa_id"))

        orphaned_ksas = []
        for category, ksas in self.all_ksas.items():
            for ksa_id in ksas:
                if ksa_id not in referenced_ksa_ids:
                    orphaned_ksas.append((category, ksa_id))

        if orphaned_ksas:
            self.warnings["global"].append(f"Found {len(orphaned_ksas)} orphaned KSAs not referenced in any mapping")
            print(f"⚠️  {len(orphaned_ksas)} KSAs exist but are not referenced in mappings:")
            for category, ksa_id in sorted(orphaned_ksas)[:10]:
                print(f"  - {ksa_id} ({category})")
            if len(orphaned_ksas) > 10:
                print(f"  ... and {len(orphaned_ksas) - 10} more")
        else:
            print("✓ No orphaned KSAs found")
        print()

        # Check 5: Variance in KSAs per role between categories
        print("Checking variance in KSAs per role across categories...")
        category_avg_ksa_per_role = {}
        for category, mappings in self.all_mappings.items():
            role_ksa_counts = defaultdict(int)
            for rel in mappings:
                role_ksa_counts[rel.get("work_role_id")] += 1
            if role_ksa_counts:
                category_avg_ksa_per_role[category] = statistics.mean(role_ksa_counts.values())

        if category_avg_ksa_per_role:
            min_avg = min(category_avg_ksa_per_role.values())
            max_avg = max(category_avg_ksa_per_role.values())
            ratio = max_avg / min_avg if min_avg > 0 else 0

            print(f"Average KSAs per role by category:")
            for category in sorted(category_avg_ksa_per_role.keys()):
                avg = category_avg_ksa_per_role[category]
                print(f"  {category}: {avg:.2f}")
            print(f"\nVariance ratio (max/min): {ratio:.2f}x")

            if ratio > 3:
                self.warnings["global"].append(f"High variance in KSAs per role: {ratio:.2f}x difference between categories")

    def audit_quality_signals(self):
        """Check for quality issues."""
        print("\n=== QUALITY SIGNAL CHECKS ===\n")

        stub_ksas = []
        duplicate_ksas = []

        # Check for stub KSAs (very short descriptions)
        print("Checking for stub KSAs (< 20 chars)...")
        for category, ksas in self.all_ksas.items():
            for ksa_id, ksa in ksas.items():
                statement = ksa.get("statement", "")
                if len(statement) < 20:
                    stub_ksas.append((category, ksa_id, statement))

        if stub_ksas:
            self.warnings["global"].append(f"Found {len(stub_ksas)} KSA descriptions shorter than 20 characters")
            print(f"⚠️  {len(stub_ksas)} stub KSAs found:")
            for category, ksa_id, statement in stub_ksas[:10]:
                print(f"  - {ksa_id} ({category}): '{statement}'")
            if len(stub_ksas) > 10:
                print(f"  ... and {len(stub_ksas) - 10} more")
        else:
            print("✓ No stub KSAs found")
        print()

        # Check for duplicates/near-duplicates
        print("Checking for duplicate or near-duplicate KSA text...")
        all_statements = []
        for category, ksas in self.all_ksas.items():
            for ksa_id, ksa in ksas.items():
                statement = ksa.get("statement", "").strip()
                all_statements.append((ksa_id, statement, category))

        # Check exact duplicates
        statement_map = defaultdict(list)
        for ksa_id, statement, category in all_statements:
            statement_map[statement].append((ksa_id, category))

        exact_dupes = {stmt: ids for stmt, ids in statement_map.items() if len(ids) > 1}
        if exact_dupes:
            self.warnings["global"].append(f"Found {len(exact_dupes)} statements with exact duplicates")
            print(f"⚠️  {len(exact_dupes)} exact duplicate statements:")
            for statement, occurrences in list(exact_dupes.items())[:5]:
                print(f"  - '{statement[:80]}...' appears in:")
                for ksa_id, category in occurrences:
                    print(f"    • {ksa_id} ({category})")
            if len(exact_dupes) > 5:
                print(f"  ... and {len(exact_dupes) - 5} more")
        else:
            print("✓ No exact duplicate statements found")
        print()

        # Check for near-duplicates (> 90% similar)
        print("Checking for near-duplicate KSA text (>90% similar)...")
        near_dupes = []
        for i, (id1, stmt1, cat1) in enumerate(all_statements):
            for id2, stmt2, cat2 in all_statements[i+1:]:
                if id1 >= id2:  # Avoid checking twice
                    continue
                ratio = SequenceMatcher(None, stmt1, stmt2).ratio()
                if ratio > 0.90 and ratio < 1.0:
                    near_dupes.append((id1, id2, ratio))

        if near_dupes:
            self.warnings["global"].append(f"Found {len(near_dupes)} near-duplicate KSA pairs (>90% similar)")
            print(f"⚠️  {len(near_dupes)} near-duplicate pairs found")
            for id1, id2, ratio in near_dupes[:5]:
                print(f"  - {id1} and {id2} ({ratio*100:.1f}% similar)")
            if len(near_dupes) > 5:
                print(f"  ... and {len(near_dupes) - 5} more")
        else:
            print("✓ No near-duplicate statements found")
        print()

    def audit_missing_categories(self):
        """Identify categories with roles but no KSAs."""
        print("\n=== MISSING CATEGORY ANALYSIS ===\n")

        categories_without_ksas = []
        for category in sorted(self.categories):
            if category in self.all_roles and category not in self.all_ksas:
                roles = self.all_roles[category]
                categories_without_ksas.append((category, len(roles)))

        if categories_without_ksas:
            print("Categories with roles but no KSA file:")
            for category, role_count in categories_without_ksas:
                print(f"  - {category}: {role_count} roles, no KSA file")
                self.findings["missing_ksas"].append(f"{category} ({role_count} roles)")
        else:
            print("✓ All categories with roles have KSA files")
        print()

    def calculate_quality_score(self) -> int:
        """Calculate an overall quality score (0-100)."""
        score = 100

        # Deduct for errors
        score -= len(self.errors) * 10

        # Deduct for warnings
        total_warnings = sum(len(v) for v in self.warnings.values())
        score -= min(total_warnings * 3, 30)

        # Check coverage: all roles should have KSAs
        for category in self.all_mappings:
            roles = self.all_roles.get(category, [])
            mappings = self.all_mappings[category]

            role_ksa_counts = defaultdict(int)
            for rel in mappings:
                role_ksa_counts[rel.get("work_role_id")] += 1

            roles_without_ksas = len(roles) - len(role_ksa_counts)
            if roles_without_ksas > 0:
                coverage_penalty = int((roles_without_ksas / len(roles)) * 15)
                score -= coverage_penalty

        return max(0, min(100, score))

    def generate_report(self):
        """Generate and print the final audit report."""
        print("\n" + "="*70)
        print("WIDAI KSA QUALITY AUDIT - FINAL REPORT")
        print("="*70 + "\n")

        self.load_data()
        category_stats = self.audit_per_category_stats()
        self.audit_cross_category_consistency()
        self.audit_quality_signals()
        self.audit_missing_categories()

        quality_score = self.calculate_quality_score()

        print("\n" + "="*70)
        print("SUMMARY")
        print("="*70 + "\n")

        print(f"Categories Analyzed: {len(self.all_ksas)}")
        print(f"Total KSAs: {sum(len(ksas) for ksas in self.all_ksas.values())}")
        print(f"Total Roles: {sum(len(roles) for roles in self.all_roles.values())}")
        print(f"Total Role-KSA Mappings: {sum(len(rels) for rels in self.all_mappings.values())}")
        print()

        if self.errors:
            print(f"ERRORS ({len(self.errors)}):")
            for error in self.errors[:10]:
                print(f"  ✗ {error}")
            if len(self.errors) > 10:
                print(f"  ... and {len(self.errors) - 10} more")
            print()

        if any(self.warnings.values()):
            total_warnings = sum(len(v) for v in self.warnings.values())
            print(f"WARNINGS ({total_warnings}):")
            for category in sorted(self.warnings.keys()):
                for warning in self.warnings[category]:
                    print(f"  ⚠️  [{category}] {warning}")
            print()

        if any(self.findings.values()):
            print("FINDINGS:")
            for category in sorted(self.findings.keys()):
                for finding in self.findings[category]:
                    print(f"  • [{category}] {finding}")
            print()

        print(f"QUALITY SCORE: {quality_score}/100")
        print()

        if quality_score >= 90:
            print("Status: EXCELLENT - Dataset is well-structured and consistent")
        elif quality_score >= 75:
            print("Status: GOOD - Minor issues detected, recommend review")
        elif quality_score >= 60:
            print("Status: FAIR - Several issues detected, recommend improvements")
        else:
            print("Status: POOR - Significant issues detected, immediate review recommended")

        print()
        print("="*70)


def main():
    base_path = Path(__file__).parent.parent
    audit = KSAQualityAudit(str(base_path))
    audit.generate_report()


if __name__ == "__main__":
    main()
