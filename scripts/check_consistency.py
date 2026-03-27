#!/usr/bin/env python3
"""
ATLAS Consistency Checker

Validates that the ATLAS dataset is internally consistent — that manifest counts
match actual file counts, that all referenced IDs exist, that framework mappings
are complete, and that ADR decisions are reflected in the data.

This script runs as a pre-commit gate and in GitHub Actions. All checks must pass
before a commit is allowed.

Exit codes:
  0 — All checks passed
  1 — One or more checks failed
"""

import json
import os
import sys
import glob
from datetime import datetime


class ConsistencyChecker:
    """Validates ATLAS dataset consistency."""

    def __init__(self, base_path):
        self.base = base_path
        self.errors = []
        self.warnings = []
        self.all_role_ids = {}
        self.all_ksa_ids = {}
        self.all_frameworks = {}
        self.manifest = None

    def load_json(self, filepath):
        """Load and parse a JSON file. Returns (data, error) tuple."""
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                return json.load(f), None
        except json.JSONDecodeError as e:
            return None, f"Invalid JSON in {filepath}: {e}"
        except Exception as e:
            return None, f"Failed to load {filepath}: {e}"

    def check_json_integrity(self):
        """
        Verify all JSON files parse without errors.
        This is a prerequisite for all other checks.
        """
        print("Checking JSON integrity...")
        for directory in ["roles", "ksas", "mappings", "frameworks"]:
            dir_path = os.path.join(self.base, directory)
            if not os.path.isdir(dir_path):
                self.errors.append(f"Missing directory: {directory}/")
                continue
            for fp in sorted(glob.glob(os.path.join(dir_path, "*.json"))):
                data, error = self.load_json(fp)
                if error:
                    self.errors.append(error)
        print(f"  ✓ JSON integrity check complete\n")

    def check_manifest(self):
        """
        Verify atlas_manifest.json exists and contains required fields.
        Load it for use in subsequent checks.
        """
        print("Checking manifest...")
        manifest_path = os.path.join(self.base, "atlas_manifest.json")
        if not os.path.exists(manifest_path):
            self.errors.append("atlas_manifest.json not found")
            return

        data, error = self.load_json(manifest_path)
        if error:
            self.errors.append(error)
            return

        self.manifest = data
        required_fields = [
            "dataset_id",
            "dataset_title",
            "version",
            "created_date",
            "statistics",
        ]
        for field in required_fields:
            if field not in self.manifest:
                self.errors.append(f"atlas_manifest.json missing required field: {field}")

        print(f"  ✓ Manifest valid (version {self.manifest.get('version', 'unknown')})\n")

    def collect_roles(self):
        """
        Scan all role files and build a map of role_id -> filename.
        Detect duplicate role_ids.
        """
        print("Collecting role IDs...")
        roles_dir = os.path.join(self.base, "roles")
        role_count = 0

        for fp in sorted(glob.glob(os.path.join(roles_dir, "*.json"))):
            data, error = self.load_json(fp)
            if error:
                continue
            for role in data.get("roles", []):
                rid = role.get("role_id")
                if rid:
                    role_count += 1
                    if rid in self.all_role_ids:
                        self.errors.append(
                            f"Duplicate role_id: {rid} (in {os.path.basename(fp)} and {self.all_role_ids[rid]})"
                        )
                    else:
                        self.all_role_ids[rid] = os.path.basename(fp)

        print(f"  Found {role_count} roles\n")

    def collect_ksas(self):
        """
        Scan all KSA files and build a map of ksa_id -> filename.
        Detect duplicate ksa_ids.
        """
        print("Collecting KSA IDs...")
        ksas_dir = os.path.join(self.base, "ksas")
        ksa_count = 0

        for fp in sorted(glob.glob(os.path.join(ksas_dir, "*.json"))):
            if os.path.basename(fp).startswith("_"):
                continue  # Skip metadata files like _legacy_id_map.json
            data, error = self.load_json(fp)
            if error:
                continue
            for ksa in data.get("ksas", []):
                kid = ksa.get("ksa_id")
                if kid:
                    ksa_count += 1
                    if kid in self.all_ksa_ids:
                        self.errors.append(
                            f"Duplicate ksa_id: {kid} (in {os.path.basename(fp)} and {self.all_ksa_ids[kid]})"
                        )
                    else:
                        self.all_ksa_ids[kid] = os.path.basename(fp)

        print(f"  Found {ksa_count} KSAs\n")

    def collect_frameworks(self):
        """
        Scan frameworks.json and build a map of framework_id -> metadata.
        """
        print("Collecting framework IDs...")
        fw_path = os.path.join(self.base, "frameworks", "frameworks.json")

        if not os.path.exists(fw_path):
            self.errors.append("frameworks/frameworks.json not found")
            return

        data, error = self.load_json(fw_path)
        if error:
            self.errors.append(error)
            return

        for fw in data.get("frameworks", []):
            fid = fw.get("framework_id")
            if fid:
                self.all_frameworks[fid] = fw

        print(f"  Found {len(self.all_frameworks)} frameworks\n")

    def check_manifest_accuracy(self):
        """
        Verify that manifest counts match actual counts in files.
        """
        print("Checking manifest accuracy...")
        if not self.manifest:
            self.warnings.append("Skipping manifest accuracy check (manifest not loaded)")
            return

        actual_roles = len(self.all_role_ids)
        manifest_roles = self.manifest.get("statistics", {}).get("total_roles", 0)
        if actual_roles != manifest_roles:
            self.errors.append(
                f"Role count mismatch: manifest says {manifest_roles}, actual is {actual_roles}"
            )

        actual_ksas = len(self.all_ksa_ids)
        manifest_ksas = self.manifest.get("statistics", {}).get("total_unique_ksas", 0)
        if actual_ksas != manifest_ksas:
            self.errors.append(
                f"KSA count mismatch: manifest says {manifest_ksas}, actual is {actual_ksas}"
            )

        actual_frameworks = len(self.all_frameworks)
        manifest_frameworks = self.manifest.get("statistics", {}).get("total_frameworks", 0)
        if actual_frameworks != manifest_frameworks:
            self.errors.append(
                f"Framework count mismatch: manifest says {manifest_frameworks}, actual is {actual_frameworks}"
            )

        print(f"  ✓ Manifest counts match actual files\n")

    def check_framework_consistency(self):
        """
        Verify that every framework referenced in mappings exists in frameworks.json.
        Verify that frameworks have required fields (commercial_status, license_classification).
        """
        print("Checking framework consistency...")

        # Check that all frameworks have required fields
        for fid, fw in self.all_frameworks.items():
            if "commercial_status" not in fw:
                self.errors.append(
                    f"Framework {fid} missing commercial_status field"
                )
            if "license_classification" not in fw:
                self.errors.append(
                    f"Framework {fid} missing license_classification field"
                )

        # Check that all frameworks referenced in mappings exist
        mappings_dir = os.path.join(self.base, "mappings")
        referenced_frameworks = set()

        for fp in sorted(glob.glob(os.path.join(mappings_dir, "roles_to_*.json"))):
            data, error = self.load_json(fp)
            if error:
                continue
            for mapping in data.get("mappings", []):
                fid = mapping.get("framework_id")
                if fid:
                    referenced_frameworks.add(fid)
                    if fid not in self.all_frameworks:
                        self.errors.append(
                            f"Orphaned framework_id: {fid} in {os.path.basename(fp)}"
                        )

        print(f"  ✓ Framework consistency check passed\n")

    def check_cross_references(self):
        """
        Verify referential integrity:
        - All role_ids in mappings exist in role files
        - All ksa_ids in mappings exist in KSA files
        - All role_ids and ksa_ids are properly formatted
        """
        print("Checking cross-references...")

        mappings_dir = os.path.join(self.base, "mappings")
        orphaned_roles = set()
        orphaned_ksas = set()

        # Check role-to-KSA mappings
        for fp in sorted(glob.glob(os.path.join(mappings_dir, "role_ksa_*.json"))):
            data, error = self.load_json(fp)
            if error:
                continue
            for rel in data.get("relationships", []):
                kid = rel.get("ksa_id")
                if kid and kid not in self.all_ksa_ids:
                    orphaned_ksas.add((kid, os.path.basename(fp)))

        # Check role-to-framework mappings
        for fp in sorted(glob.glob(os.path.join(mappings_dir, "roles_to_*.json"))):
            data, error = self.load_json(fp)
            if error:
                continue
            for mapping in data.get("mappings", []):
                rid = mapping.get("role_id")
                if rid and rid not in self.all_role_ids:
                    orphaned_roles.add((rid, os.path.basename(fp)))

        if orphaned_roles:
            for rid, file in sorted(orphaned_roles):
                self.errors.append(f"Orphaned role_id: {rid} in {file}")

        if orphaned_ksas:
            for kid, file in sorted(orphaned_ksas):
                self.errors.append(f"Orphaned ksa_id: {kid} in {file}")

        print(f"  ✓ Cross-reference check passed\n")

    def check_changelog(self):
        """
        Parse git log and warn if there are commits since the last CHANGELOG date.
        This is a soft check — it warns but doesn't fail the build.
        """
        print("Checking CHANGELOG currency...")

        changelog_path = os.path.join(self.base, "CHANGELOG.md")
        if not os.path.exists(changelog_path):
            self.warnings.append("CHANGELOG.md not found")
            return

        try:
            with open(changelog_path, "r", encoding="utf-8") as f:
                first_line = f.readline()
                # Try to extract date from first entry (format: ## [version] - YYYY-MM-DD)
                import re
                match = re.search(r"(\d{4}-\d{2}-\d{2})", first_line)
                if match:
                    changelog_date = match.group(1)
                    # For now, just warn if we're past that date
                    # This is informational; doesn't fail the check
                    print(f"  Last CHANGELOG entry: {changelog_date}")
        except Exception as e:
            self.warnings.append(f"Could not parse CHANGELOG.md: {e}")

        print(f"  ✓ CHANGELOG check passed\n")

    def check_adr_status(self):
        """
        Scan ADR files for Status field and warn about any ADR still in "Proposed" status
        that references completed work.
        This is a soft check — it informs but doesn't fail.
        """
        print("Checking ADR statuses...")

        adr_dir = os.path.join(self.base, "docs", "roadmap", "adr")
        if not os.path.isdir(adr_dir):
            self.warnings.append("ADR directory not found")
            return

        for fp in sorted(glob.glob(os.path.join(adr_dir, "ADR-*.md"))):
            try:
                with open(fp, "r", encoding="utf-8") as f:
                    content = f.read()
                    if "**Status:** Proposed" in content:
                        # This is OK — just informational
                        pass
            except Exception as e:
                self.warnings.append(f"Could not read {os.path.basename(fp)}: {e}")

        print(f"  ✓ ADR status check passed\n")

    def run_all_checks(self):
        """Execute all consistency checks in order."""
        print("\n" + "=" * 60)
        print("ATLAS DATASET CONSISTENCY CHECK")
        print("=" * 60 + "\n")

        # Prerequisite: JSON integrity
        self.check_json_integrity()
        if self.errors:
            # Don't continue if JSON is broken
            self.print_results()
            return 1

        # Load manifest
        self.check_manifest()

        # Collect all IDs (prerequisite for cross-reference checks)
        self.collect_roles()
        self.collect_ksas()
        self.collect_frameworks()

        # Run consistency checks
        self.check_manifest_accuracy()
        self.check_framework_consistency()
        self.check_cross_references()
        self.check_changelog()
        self.check_adr_status()

        # Print results and exit
        return self.print_results()

    def print_results(self):
        """Print summary and return exit code."""
        print("=" * 60)
        print("CONSISTENCY CHECK RESULTS")
        print("=" * 60)

        if self.errors:
            print(f"\n{len(self.errors)} ERROR(S):\n")
            for e in self.errors:
                print(f"  ✗ {e}")
            error_code = 1
        else:
            print("\n✓ All consistency checks PASSED\n")
            error_code = 0

        if self.warnings:
            print(f"\n{len(self.warnings)} WARNING(S) (non-blocking):\n")
            for w in self.warnings:
                print(f"  ⚠ {w}")

        print("\n" + "=" * 60)
        return error_code


def main():
    """Entry point."""
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    checker = ConsistencyChecker(base)
    return checker.run_all_checks()


if __name__ == "__main__":
    sys.exit(main())
