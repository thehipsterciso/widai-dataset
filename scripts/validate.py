#!/usr/bin/env python3
"""
Validation script for WIDAI dataset.
Validates JSON integrity, referential integrity, and duplicate detection.
"""

import json
import os
import sys
import glob


def load_json(filepath):
    """Load and parse a JSON file."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        return None, f"Invalid JSON in {filepath}: {e}"
    except Exception as e:
        return None, f"Failed to load {filepath}: {e}"


def main():
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    errors = []

    # ── 1. Validate all JSON files parse correctly ──
    print("Validating JSON integrity...")
    for directory in ["roles", "ksas", "mappings", "frameworks", "schema"]:
        dir_path = os.path.join(base, directory)
        if not os.path.isdir(dir_path):
            errors.append(f"Missing directory: {directory}/")
            continue
        for fp in sorted(glob.glob(os.path.join(dir_path, "*.json"))):
            result = load_json(fp)
            if isinstance(result, tuple):
                errors.append(result[1])

    # ── 2. Validate manifest ──
    print("Validating widai_manifest.json...")
    manifest_path = os.path.join(base, "widai_manifest.json")
    if not os.path.exists(manifest_path):
        errors.append("widai_manifest.json not found")
    else:
        result = load_json(manifest_path)
        if isinstance(result, tuple):
            errors.append(result[1])
        else:
            manifest = result
            for field in ["dataset_id", "dataset_title", "version", "created_date", "statistics"]:
                if field not in manifest:
                    errors.append(f"widai_manifest.json missing required field: {field}")

    # ── 3. Collect all role_ids ──
    print("Collecting role IDs...")
    all_role_ids = {}
    roles_dir = os.path.join(base, "roles")
    for fp in sorted(glob.glob(os.path.join(roles_dir, "*.json"))):
        result = load_json(fp)
        if isinstance(result, tuple):
            continue
        data = result
        for role in data.get("roles", []):
            rid = role.get("role_id")
            if rid:
                if rid in all_role_ids:
                    errors.append(f"Duplicate role_id: {rid} (in {os.path.basename(fp)} and {all_role_ids[rid]})")
                else:
                    all_role_ids[rid] = os.path.basename(fp)

    # ── 4. Collect all ksa_ids ──
    print("Collecting KSA IDs...")
    all_ksa_ids = {}
    ksas_dir = os.path.join(base, "ksas")
    for fp in sorted(glob.glob(os.path.join(ksas_dir, "*.json"))):
        if os.path.basename(fp).startswith("_"):
            continue  # Skip metadata files like _legacy_id_map.json
        result = load_json(fp)
        if isinstance(result, tuple):
            continue
        data = result
        for ksa in data.get("ksas", []):
            kid = ksa.get("ksa_id")
            if kid:
                if kid in all_ksa_ids:
                    errors.append(f"Duplicate ksa_id: {kid} (in {os.path.basename(fp)} and {all_ksa_ids[kid]})")
                else:
                    all_ksa_ids[kid] = os.path.basename(fp)

    # ── 5. Validate referential integrity in role_ksa mappings ──
    print("Validating referential integrity...")
    mappings_dir = os.path.join(base, "mappings")
    role_ksa_count = 0
    role_fw_count = 0

    for fp in sorted(glob.glob(os.path.join(mappings_dir, "role_ksa_*.json"))):
        result = load_json(fp)
        if isinstance(result, tuple):
            continue
        data = result
        for rel in data.get("relationships", []):
            role_ksa_count += 1
            wrid = rel.get("work_role_id")
            kid = rel.get("ksa_id")
            # work_role_id uses WR-GOV-01.01 format, not WIDAI-GOV-0001
            # so we skip role_id validation for these (different ID space)
            if kid and kid not in all_ksa_ids:
                errors.append(f"Orphaned ksa_id: {kid} in {os.path.basename(fp)}")

    for fp in sorted(glob.glob(os.path.join(mappings_dir, "roles_to_*.json"))):
        result = load_json(fp)
        if isinstance(result, tuple):
            continue
        data = result
        for mapping in data.get("mappings", []):
            role_fw_count += 1
            rid = mapping.get("role_id")
            if rid and rid not in all_role_ids:
                errors.append(f"Orphaned role_id: {rid} in {os.path.basename(fp)}")

    # ── 6. Count frameworks ──
    fw_path = os.path.join(base, "frameworks", "frameworks.json")
    fw_count = 0
    if os.path.exists(fw_path):
        result = load_json(fw_path)
        if not isinstance(result, tuple):
            fw_count = len(result.get("frameworks", []))

    # ── Summary ──
    print(f"\n{'='*50}")
    print("VALIDATION SUMMARY")
    print(f"{'='*50}")
    print(f"Roles:                  {len(all_role_ids)}")
    print(f"KSAs:                   {len(all_ksa_ids)}")
    print(f"Role-KSA relationships: {role_ksa_count}")
    print(f"Role-FW mappings:       {role_fw_count}")
    print(f"Frameworks:             {fw_count}")
    print(f"{'='*50}")

    if errors:
        print(f"\n{len(errors)} VALIDATION ERROR(S):")
        for e in errors:
            print(f"  - {e}")
        return 1
    else:
        print("\nAll validations PASSED")
        return 0


if __name__ == "__main__":
    sys.exit(main())
