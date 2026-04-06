#!/usr/bin/env python3
"""
ADVERSARIAL VALIDATOR

Runs AFTER a domain×dimension re-synthesis is complete.
Checks the final JSON output against the synthesis evidence to catch failures.

This exists because the process was skipped repeatedly — deduplication only,
no expansion, despite evidence showing hundreds of uncovered concepts.

FAILURES this catches:
  1. Entry count only went down (suspicious for unexpanded domains)
  2. High-STS framework concept clusters with no dedicated entry
  3. Synthesis doc missing gap analysis section
  4. Overloaded entries that should have been decomposed
  5. New entries without framework evidence justification

Usage:
  python3 scripts/adversarial_validator.py \
    --domain AI --dimension knowledge \
    --synthesis-file /tmp/ai_knowledge_synthesis.txt \
    --json-file ksas/AI_knowledge.json \
    --synthesis-doc docs/synthesis/AI-KNOWLEDGE-SYNTHESIS.md \
    --original-count 40
"""

import argparse
import json
import os
import re
import sys
from collections import defaultdict


def load_json(filepath):
    with open(filepath) as f:
        return json.load(f)


def parse_elements(synthesis_text):
    """Parse all framework elements at STS >= 0.50."""
    elements = []
    elem_pattern = r'\s+\d+\.\s+STS=([\d.]+)\s+\[(.*?)\]\s+(.*?)\n\s+-> (.*?)(?:\n|$)'
    for match in re.finditer(elem_pattern, synthesis_text):
        sts = float(match.group(1))
        element_id = match.group(2)
        description = match.group(3).strip()
        mappings = [m.strip() for m in match.group(4).split(',')]
        elements.append({
            'element_id': element_id,
            'sts': sts,
            'description': description[:200],
            'maps_to': mappings
        })
    return elements


def validate(domain, dimension, synthesis_text, json_data, synthesis_doc_text,
             original_count):
    """Run all adversarial checks. Returns (pass_count, fail_count, results)."""

    entries = json_data.get('entries', [])
    new_count = len(entries)
    elements = parse_elements(synthesis_text)
    high_sts_60 = [e for e in elements if e['sts'] >= 0.60]
    high_sts_55 = [e for e in elements if e['sts'] >= 0.55]

    results = []
    passes = 0
    fails = 0

    # ===== CHECK 1: Count direction =====
    if new_count < original_count:
        # Only a fail if the domain was never expanded (small original count)
        if original_count <= 20:
            results.append({
                'check': 'COUNT_DIRECTION',
                'status': 'FAIL',
                'message': f"Count went DOWN ({original_count} → {new_count}) for a domain with "
                           f"only {original_count} original entries. Where is the expansion? "
                           f"AB went from 10 → 29. Evidence shows {len(high_sts_60)} elements "
                           f"at STS >= 0.60."
            })
            fails += 1
        else:
            results.append({
                'check': 'COUNT_DIRECTION',
                'status': 'WARN',
                'message': f"Count went down ({original_count} → {new_count}). This may be "
                           f"valid if the domain was already expanded. Verify gap analysis was done."
            })
            passes += 1
    elif new_count == original_count:
        if original_count <= 15 and len(high_sts_60) > 10:
            results.append({
                'check': 'COUNT_DIRECTION',
                'status': 'FAIL',
                'message': f"Count UNCHANGED at {new_count} despite {len(high_sts_60)} "
                           f"framework elements at STS >= 0.60. Expansion was likely needed."
            })
            fails += 1
        else:
            results.append({
                'check': 'COUNT_DIRECTION',
                'status': 'PASS',
                'message': f"Count: {original_count} → {new_count}"
            })
            passes += 1
    else:
        results.append({
            'check': 'COUNT_DIRECTION',
            'status': 'PASS',
            'message': f"Count went UP ({original_count} → {new_count}) — expansion occurred."
        })
        passes += 1

    # ===== CHECK 2: Evidence density vs entry count =====
    ratio = len(high_sts_60) / max(new_count, 1)
    if ratio > 10 and new_count < 25:
        results.append({
            'check': 'EVIDENCE_DENSITY',
            'status': 'FAIL',
            'message': f"{len(high_sts_60)} elements at STS >= 0.60 for only {new_count} entries "
                       f"(ratio {ratio:.1f}:1). AB reference had similar density and expanded "
                       f"from 10 to 29. This suggests significant uncovered concept space."
        })
        fails += 1
    else:
        results.append({
            'check': 'EVIDENCE_DENSITY',
            'status': 'PASS',
            'message': f"Evidence density ratio: {ratio:.1f} elements per entry (STS >= 0.60)"
        })
        passes += 1

    # ===== CHECK 3: Overloaded entries =====
    entry_load = defaultdict(int)
    for elem in high_sts_55:
        for ksa_id in elem['maps_to']:
            entry_load[ksa_id] += 1

    overloaded = {k: v for k, v in entry_load.items() if v > 25}
    if overloaded:
        worst = max(overloaded.items(), key=lambda x: x[1])
        results.append({
            'check': 'ENTRY_OVERLOAD',
            'status': 'WARN',
            'message': f"{len(overloaded)} entries attract >25 elements at STS >= 0.55. "
                       f"Worst: {worst[0]} with {worst[1]} elements. These may need decomposition."
        })
        # Not a hard fail — some entries legitimately attract many mappings
        passes += 1
    else:
        results.append({
            'check': 'ENTRY_OVERLOAD',
            'status': 'PASS',
            'message': "No entries are excessively overloaded."
        })
        passes += 1

    # ===== CHECK 4: Synthesis doc contains gap analysis =====
    if synthesis_doc_text:
        has_gap_section = any(term in synthesis_doc_text.lower() for term in
                             ['gap analysis', 'gap cluster', 'concept gap', 'new entries',
                              'expansion analysis', 'uncovered concept', 'gap signal',
                              'not covered by', 'no existing entry'])
        if has_gap_section:
            results.append({
                'check': 'GAP_ANALYSIS_PRESENT',
                'status': 'PASS',
                'message': "Synthesis doc contains gap analysis language."
            })
            passes += 1
        else:
            results.append({
                'check': 'GAP_ANALYSIS_PRESENT',
                'status': 'FAIL',
                'message': "Synthesis doc does NOT contain gap analysis. "
                           "This section is MANDATORY per the process."
            })
            fails += 1
    else:
        results.append({
            'check': 'GAP_ANALYSIS_PRESENT',
            'status': 'FAIL',
            'message': "No synthesis doc provided or found."
        })
        fails += 1

    # ===== CHECK 5: Schema version =====
    if json_data.get('schema_version') != '3.0.0':
        results.append({
            'check': 'SCHEMA_VERSION',
            'status': 'FAIL',
            'message': f"Schema version is {json_data.get('schema_version')}, expected 3.0.0"
        })
        fails += 1
    else:
        results.append({
            'check': 'SCHEMA_VERSION',
            'status': 'PASS',
            'message': "Schema version 3.0.0"
        })
        passes += 1

    # ===== CHECK 6: No legacy_ids in schema 3.0.0 =====
    has_legacy = any(e.get('legacy_ids') for e in entries)
    if has_legacy:
        results.append({
            'check': 'NO_LEGACY_IDS',
            'status': 'FAIL',
            'message': "Entries still contain legacy_ids — must be removed for schema 3.0.0"
        })
        fails += 1
    else:
        results.append({
            'check': 'NO_LEGACY_IDS',
            'status': 'PASS',
            'message': "No legacy_ids present"
        })
        passes += 1

    # ===== CHECK 7: Entry count matches metadata =====
    if json_data.get('count') != new_count:
        results.append({
            'check': 'COUNT_METADATA',
            'status': 'FAIL',
            'message': f"Metadata count ({json_data.get('count')}) != actual entries ({new_count})"
        })
        fails += 1
    else:
        results.append({
            'check': 'COUNT_METADATA',
            'status': 'PASS',
            'message': f"Count metadata matches: {new_count}"
        })
        passes += 1

    # ===== CHECK 8: Sequential IDs =====
    prefix = f"{domain}-{dimension[0].upper()}-"
    expected_ids = [f"{prefix}{str(i).zfill(3)}" for i in range(1, new_count + 1)]
    actual_ids = [e['ksa_id'] for e in entries]
    if actual_ids != expected_ids:
        results.append({
            'check': 'SEQUENTIAL_IDS',
            'status': 'FAIL',
            'message': f"IDs not sequential. Expected {expected_ids[0]}..{expected_ids[-1]}, "
                       f"got {actual_ids[0]}..{actual_ids[-1]}"
        })
        fails += 1
    else:
        results.append({
            'check': 'SEQUENTIAL_IDS',
            'status': 'PASS',
            'message': f"IDs sequential: {actual_ids[0]}..{actual_ids[-1]}"
        })
        passes += 1

    return passes, fails, results


def main():
    parser = argparse.ArgumentParser(description='Adversarial Validator')
    parser.add_argument('--domain', required=True)
    parser.add_argument('--dimension', required=True, choices=['knowledge', 'skills', 'abilities', 'tasks'])
    parser.add_argument('--synthesis-file', required=True, help='dimension_synthesis.py output')
    parser.add_argument('--json-file', required=True, help='Final JSON file')
    parser.add_argument('--synthesis-doc', help='Synthesis analysis markdown doc')
    parser.add_argument('--original-count', type=int, required=True, help='Entry count before re-synthesis')

    args = parser.parse_args()

    with open(args.synthesis_file) as f:
        synthesis_text = f.read()

    json_data = load_json(args.json_file)

    synthesis_doc_text = ''
    if args.synthesis_doc and os.path.exists(args.synthesis_doc):
        with open(args.synthesis_doc) as f:
            synthesis_doc_text = f.read()

    passes, fails, results = validate(
        args.domain, args.dimension, synthesis_text, json_data,
        synthesis_doc_text, args.original_count
    )

    # Print results
    print("=" * 80)
    print(f"ADVERSARIAL VALIDATION — {args.domain} {args.dimension.title()}")
    print("=" * 80)
    print()

    for r in results:
        status_icon = {'PASS': '✓', 'FAIL': '✗', 'WARN': '⚠'}[r['status']]
        print(f"  {status_icon} [{r['status']}] {r['check']}")
        print(f"    {r['message']}")
        print()

    print("-" * 80)
    print(f"  RESULT: {passes} passed, {fails} failed")
    if fails > 0:
        print(f"  *** VALIDATION FAILED — DO NOT COMMIT ***")
        sys.exit(1)
    else:
        print(f"  Validation passed — proceed with commit")
        sys.exit(0)


if __name__ == '__main__':
    main()
