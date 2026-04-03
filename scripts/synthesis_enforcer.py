#!/usr/bin/env python3
"""
SYNTHESIS PROCESS ENFORCER

This script enforces the complete re-synthesis methodology for each domain×dimension.
It parses dimension_synthesis.py output and generates a MANDATORY analysis template
that covers BOTH deduplication AND expansion.

The AB domain is the reference: 10 Phase 1A entries → 29 after evidence-driven expansion.
Every domain must go through the same process. If this script shows gap clusters
and the final count only goes down, something is wrong.

PROCESS (from the prompt — non-negotiable):
  1. Read STRM evidence (dimension_synthesis.py output)
  2. Cluster the concepts that actually appear in framework elements
  3. Identify which clusters are GAPS against existing entries
  4. Write entries for every real gap
  5. Identify duplicates within existing entries
  6. Validate post-STRM entries (if any) against evidence
  7. Write synthesis doc → THEN write JSON
  8. Count is OUTPUT, never input

Usage:
  python3 scripts/synthesis_enforcer.py --domain AI --dimension knowledge --synthesis-file /tmp/ai_knowledge_synthesis.txt
"""

import argparse
import json
import re
import os
import sys
from collections import defaultdict


def parse_evidence_matrix(text):
    """Extract evidence matrix from synthesis output."""
    entries = {}
    matrix_match = re.search(r'EVIDENCE MATRIX.*?\n-+\n(.*?)\n\n', text, re.DOTALL)
    if not matrix_match:
        return entries
    for line in matrix_match.group(1).strip().split('\n'):
        parts = line.split()
        if len(parts) >= 5 and parts[0].startswith(('DQ-', 'DG-', 'AI-', 'AG-', 'DA-', 'AB-',
                                                      'LS-', 'OP-', 'RC-', 'RM-', 'SP-', 'TF-')):
            entries[parts[0]] = {
                'fw_cov': parts[1],
                'strong': int(parts[2]),
                'total': int(parts[3]),
                'max_sts': float(parts[4])
            }
    return entries


def parse_high_watermark(text):
    """Extract high watermark counts."""
    hw = {}
    hw_match = re.search(r'HIGH WATERMARK.*?\n-+\n(.*?)\n\n', text, re.DOTALL)
    if not hw_match:
        return hw
    for line in hw_match.group(1).strip().split('\n'):
        parts = line.rsplit(None, 4)
        if len(parts) >= 5:
            try:
                fw_name = ' '.join(parts[:-4])
                hw[fw_name] = {
                    '>=0.45': int(parts[-4]),
                    '>=0.50': int(parts[-3]),
                    '>=0.55': int(parts[-2]),
                    '>=0.60': int(parts[-1])
                }
            except (ValueError, IndexError):
                pass
    return hw


def parse_framework_elements(text):
    """Extract top framework elements per framework with their KSA mappings."""
    elements = []
    # Find each framework section
    fw_sections = re.findall(
        r'={80}\n(.*?) — WIDAI-relevant elements.*?\n={80}\n(.*?)(?=\n={80}|\Z)',
        text, re.DOTALL
    )
    for fw_name, section in fw_sections:
        # Parse each numbered element
        elem_pattern = r'\s+\d+\.\s+STS=([\d.]+)\s+\[(.*?)\]\s+(.*?)\n\s+-> (.*?)(?:\n|$)'
        for match in re.finditer(elem_pattern, section):
            sts = float(match.group(1))
            element_id = match.group(2)
            description = match.group(3).strip()
            mappings = [m.strip() for m in match.group(4).split(',')]
            elements.append({
                'framework': fw_name.strip(),
                'element_id': element_id,
                'sts': sts,
                'description': description[:200],
                'maps_to': mappings
            })
    return elements


def identify_concept_clusters(elements, existing_ids):
    """
    Group high-STS framework elements by the KSA IDs they map to.
    Elements that map to many entries suggest broad concepts.
    Elements that map to only 1-2 entries, especially at high STS, may indicate
    that the concept is being forced to a "nearest neighbor" rather than having
    its own dedicated entry.

    KEY: Look for elements at STS >= 0.60 that map broadly (to 3+ entries)
    — this suggests the concept doesn't have a precise home.
    Also look for CLUSTERS of related elements that all map to the same 1-2 entries
    — this suggests those entries are overloaded.
    """
    # Group elements by their primary mapping pattern
    mapping_patterns = defaultdict(list)
    for elem in elements:
        if elem['sts'] >= 0.55:
            key = tuple(sorted(elem['maps_to']))
            mapping_patterns[key].append(elem)

    # Find overloaded entries (entries that attract disproportionate mappings)
    entry_load = defaultdict(list)
    for elem in elements:
        if elem['sts'] >= 0.55:
            for ksa_id in elem['maps_to']:
                entry_load[ksa_id].append(elem)

    return mapping_patterns, entry_load


def detect_gap_signals(elements, existing_ids):
    """
    Detect framework elements that suggest concept gaps.

    Gap signals:
    1. High-STS elements (>= 0.60) that map to 4+ existing entries — the concept
       is so broad it doesn't have a precise home
    2. Clusters of related elements from multiple frameworks that all converge
       on the same 1-2 entries — those entries may be overloaded
    3. Framework elements with descriptions that don't semantically match
       any existing entry well (high STS to domain but concept is tangential)
    """
    gap_signals = []

    # Signal 1: Broad-mapping high-STS elements
    for elem in elements:
        if elem['sts'] >= 0.60 and len(elem['maps_to']) >= 5:
            gap_signals.append({
                'type': 'BROAD_MAPPING',
                'element': elem,
                'reason': f"STS {elem['sts']:.4f} maps to {len(elem['maps_to'])} entries — concept may lack dedicated entry"
            })

    # Signal 2: Entry overload — entries attracting >15 elements at STS >= 0.55
    entry_counts = defaultdict(int)
    for elem in elements:
        if elem['sts'] >= 0.55:
            for ksa_id in elem['maps_to']:
                entry_counts[ksa_id] += 1

    overloaded = {k: v for k, v in entry_counts.items() if v > 15}
    for entry_id, count in sorted(overloaded.items(), key=lambda x: -x[1]):
        gap_signals.append({
            'type': 'ENTRY_OVERLOAD',
            'entry_id': entry_id,
            'element_count': count,
            'reason': f"{entry_id} attracts {count} elements at STS >= 0.55 — may need decomposition"
        })

    return gap_signals


def load_current_entries(domain, dimension, repo_root):
    """Load current JSON entries for comparison."""
    dim_map = {'knowledge': 'knowledge', 'skills': 'skills', 'abilities': 'abilities', 'tasks': 'tasks'}
    filename = f"{domain}_{dim_map[dimension]}.json"
    filepath = os.path.join(repo_root, 'ksas', filename)

    if not os.path.exists(filepath):
        return [], "2.0.0"

    with open(filepath) as f:
        data = json.load(f)

    return data.get('entries', []), data.get('schema_version', '2.0.0')


def generate_enforcement_report(domain, dimension, synthesis_text, repo_root):
    """Generate the mandatory analysis report."""

    # Parse everything
    evidence = parse_evidence_matrix(synthesis_text)
    watermark = parse_high_watermark(synthesis_text)
    elements = parse_framework_elements(synthesis_text)
    entries, schema_ver = load_current_entries(domain, dimension, repo_root)

    existing_ids = [e['ksa_id'] for e in entries]
    phase1a = [e for e in entries if e.get('origin_version') in ('0.5.0', '0.7.0') and not e.get('ksa_id', '').split('-')[-1].startswith(('0', ))]
    # Better detection: entries with legacy_ids are Phase 1A original
    has_legacy = [e for e in entries if e.get('legacy_ids')]
    no_legacy = [e for e in entries if not e.get('legacy_ids')]

    # Determine if domain was ever expanded
    was_expanded = schema_ver == '3.0.0' or len(entries) > 20  # rough heuristic

    # Detect gaps
    gap_signals = detect_gap_signals(elements, existing_ids)
    mapping_patterns, entry_load = identify_concept_clusters(elements, existing_ids)

    # Count high-STS elements
    high_sts_60 = [e for e in elements if e['sts'] >= 0.60]
    high_sts_55 = [e for e in elements if e['sts'] >= 0.55]
    high_sts_50 = [e for e in elements if e['sts'] >= 0.50]

    # Build report
    report = []
    report.append("=" * 80)
    report.append(f"SYNTHESIS ENFORCEMENT REPORT — {domain} {dimension.title()}")
    report.append("=" * 80)
    report.append("")

    # Section 1: Current State
    report.append("## CURRENT STATE")
    report.append(f"  Entries: {len(entries)}")
    report.append(f"  Schema: {schema_ver}")
    report.append(f"  With legacy_ids (Phase 1A original): {len(has_legacy)}")
    report.append(f"  Without legacy_ids (post-expansion): {len(no_legacy)}")
    report.append(f"  Was previously expanded: {'YES' if was_expanded else 'NO — EXPANSION REQUIRED'}")
    report.append("")

    # Section 2: Evidence Summary
    total_mappings = sum(v['total'] for v in evidence.values()) if evidence else 0
    report.append("## EVIDENCE SUMMARY")
    report.append(f"  Total mappings: {total_mappings:,}")
    report.append(f"  Framework elements at STS >= 0.50: {len(high_sts_50)}")
    report.append(f"  Framework elements at STS >= 0.55: {len(high_sts_55)}")
    report.append(f"  Framework elements at STS >= 0.60: {len(high_sts_60)}")
    report.append("")

    # Section 3: High Watermark
    report.append("## HIGH WATERMARK (unique FDE counts)")
    for fw, counts in watermark.items():
        report.append(f"  {fw}: {counts}")
    report.append("")

    # Section 4: MANDATORY — Duplicate Analysis
    report.append("## MANDATORY STEP: DUPLICATE ANALYSIS")
    report.append("  [Must identify ALL entry pairs with overlapping scope]")
    report.append("  [For each pair: cite the specific overlap, cite evidence, state merge decision]")
    report.append("")

    # Section 5: MANDATORY — Gap Analysis (THE STEP THAT KEEPS GETTING SKIPPED)
    report.append("=" * 80)
    report.append("## *** MANDATORY STEP: GAP ANALYSIS — DO NOT SKIP ***")
    report.append("=" * 80)
    report.append("")
    report.append("  This is the step that was skipped for EVERY domain except AB.")
    report.append("  AB went from 10 → 29 Knowledge entries through gap analysis.")
    report.append("  If this dimension has fewer than ~25 entries and the evidence")
    report.append("  shows hundreds of WIDAI-relevant framework elements, there ARE gaps.")
    report.append("")

    if gap_signals:
        report.append(f"  DETECTED {len(gap_signals)} GAP SIGNALS:")
        report.append("")
        for i, signal in enumerate(gap_signals[:30], 1):
            if signal['type'] == 'BROAD_MAPPING':
                elem = signal['element']
                report.append(f"  {i}. {signal['type']}: [{elem['element_id']}] STS={elem['sts']:.4f}")
                report.append(f"     \"{elem['description']}\"")
                report.append(f"     Maps to: {', '.join(elem['maps_to'])}")
                report.append(f"     → {signal['reason']}")
                report.append("")
            elif signal['type'] == 'ENTRY_OVERLOAD':
                report.append(f"  {i}. {signal['type']}: {signal['entry_id']} ({signal['element_count']} elements)")
                report.append(f"     → {signal['reason']}")
                report.append("")
    else:
        report.append("  No automated gap signals detected (unusual — verify manually)")
        report.append("")

    # Section 6: Entry Load Analysis
    report.append("## ENTRY LOAD ANALYSIS (elements at STS >= 0.55 per entry)")
    entry_load_counts = defaultdict(int)
    for elem in high_sts_55:
        for ksa_id in elem['maps_to']:
            entry_load_counts[ksa_id] += 1
    for entry_id in sorted(entry_load_counts, key=lambda x: -entry_load_counts[x]):
        count = entry_load_counts[entry_id]
        marker = " *** OVERLOADED" if count > 20 else ""
        report.append(f"  {entry_id}: {count} elements{marker}")
    report.append("")

    # Section 7: Top framework elements not well-covered
    report.append("## TOP FRAMEWORK ELEMENTS AT STS >= 0.60 (potential gap indicators)")
    for elem in sorted(high_sts_60, key=lambda x: -x['sts'])[:40]:
        broad = " [BROAD]" if len(elem['maps_to']) >= 4 else ""
        report.append(f"  STS={elem['sts']:.4f} [{elem['element_id']}]{broad}")
        report.append(f"    \"{elem['description']}\"")
        report.append(f"    → {', '.join(elem['maps_to'])}")
        report.append("")

    # Section 8: MANDATORY Checklist
    report.append("=" * 80)
    report.append("## MANDATORY CHECKLIST — ALL MUST BE ANSWERED BEFORE WRITING JSON")
    report.append("=" * 80)
    report.append("")
    report.append("  [ ] 1. How many duplicate groups were identified? List each.")
    report.append("  [ ] 2. How many gap clusters were identified from framework evidence?")
    report.append("  [ ] 3. For each gap cluster: what concept does it represent?")
    report.append("  [ ] 4. For each gap cluster: what new entry statement was written?")
    report.append("  [ ] 5. For each gap cluster: which framework elements provide evidence?")
    report.append("  [ ] 6. Were post-STRM entries (if any) validated against evidence?")
    report.append("  [ ] 7. What is the final entry count and how was it derived?")
    report.append(f"  [ ] 8. Starting count: {len(entries)}. If final count <= {len(entries)},")
    report.append("         explain why no gaps exist despite the evidence density above.")
    report.append("")

    # Final warning
    if len(entries) < 20 and len(high_sts_60) > 20:
        report.append("!!! WARNING: LOW ENTRY COUNT WITH HIGH EVIDENCE DENSITY !!!")
        report.append(f"    {len(entries)} entries but {len(high_sts_60)} framework elements at STS >= 0.60")
        report.append("    This strongly suggests expansion is needed. AB had 10 entries")
        report.append("    and expanded to 29. Do NOT proceed with deduplication only.")
        report.append("")

    return '\n'.join(report)


def main():
    parser = argparse.ArgumentParser(description='Synthesis Process Enforcer')
    parser.add_argument('--domain', required=True, help='Domain code (e.g., AI, DG)')
    parser.add_argument('--dimension', required=True, choices=['knowledge', 'skills', 'abilities', 'tasks'])
    parser.add_argument('--synthesis-file', required=True, help='Path to dimension_synthesis.py output')
    parser.add_argument('--repo-root', default='.', help='Repository root directory')
    parser.add_argument('--output', help='Output file (default: stdout)')

    args = parser.parse_args()

    with open(args.synthesis_file) as f:
        synthesis_text = f.read()

    report = generate_enforcement_report(
        args.domain, args.dimension, synthesis_text, args.repo_root
    )

    if args.output:
        with open(args.output, 'w') as f:
            f.write(report)
        print(f"Report written to {args.output}")
    else:
        print(report)


if __name__ == '__main__':
    main()
