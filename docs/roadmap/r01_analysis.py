#!/usr/bin/env python3
"""R01 Coverage Gap Test: Archetype Mapping and Coverage Analysis"""

import json
import os
from collections import defaultdict

os.chdir('/sessions/awesome-elegant-mayer/mnt/WIDAI/atlas-dataset')

# Load all role files
categories = {}
for cat in ['GOV', 'ENG', 'DEV', 'DSM', 'ANL', 'RSK', 'OPS', 'LDR']:
    with open(f'roles/{cat}.json') as f:
        categories[cat] = json.load(f)['roles']

# Build a lookup: role title -> (role_id, has_ksa, category)
role_lookup = {}
ksa_coverage = set()

for cat in ['ENG', 'DEV', 'DSM', 'ANL', 'GOV', 'RSK', 'OPS', 'LDR']:
    try:
        with open(f'mappings/role_ksa_{cat}.json') as f:
            ksa_map = json.load(f)
        # Extract work_role_ids that have KSAs (from relationships)
        for rel in ksa_map.get('relationships', []):
            if 'work_role_id' in rel:
                ksa_coverage.add(rel['work_role_id'])
    except FileNotFoundError:
        pass

# Now add roles from categories
for cat, roles in categories.items():
    for role in roles:
        canonical = role['canonical_title'].lower()
        work_role_id = role.get('atlas_work_role_id')
        has_ksa = work_role_id in ksa_coverage if work_role_id else False

        role_lookup[canonical] = {
            'role_id': role['role_id'],
            'canonical_title': role['canonical_title'],
            'category': cat,
            'work_role_id': work_role_id,
            'has_ksa': has_ksa
        }

print(f"Loaded {len(role_lookup)} roles across {len(categories)} categories")
print(f"KSA Coverage: {sum(1 for r in role_lookup.values() if r['has_ksa'])} roles have KSAs")

# Define 5 representative mid-market archetypes
archetypes = {
    "PE-Backed Manufacturer": {
        "description": "Manufacturing company with growing data/analytics function",
        "headcount": 18,
        "roles": [
            ("Chief Data Officer", 1),
            ("Data Governance Director", 1),
            ("Senior Data Engineer", 2),
            ("Data Engineer", 2),
            ("Senior Data Analyst", 1),
            ("Data Analyst", 3),
            ("BI Developer", 2),
            ("Data Quality Manager", 1),
            ("Analytics Engineer", 1),
            ("Data Architect", 1),
        ]
    },
    "Mid-Market Financial Services": {
        "description": "Regional bank/insurance with model risk and regulatory overlay",
        "headcount": 30,
        "roles": [
            ("Chief Data Officer", 1),
            ("Chief AI Officer", 1),
            ("Data Governance Director", 1),
            ("AI Risk and Ethics Specialist", 1),
            ("Data Compliance Analyst", 2),
            ("Model Risk Officer", 1),
            ("Senior Data Engineer", 2),
            ("Data Engineer", 3),
            ("Data Architect", 1),
            ("Senior Data Analyst", 2),
            ("Data Analyst", 4),
            ("BI Developer", 3),
            ("Data Scientist", 2),
            ("ML Engineer", 1),
            ("Data Quality Manager", 1),
            ("Master Data Manager", 1),
            ("Data Product Manager", 1),
        ]
    },
    "PE-Backed SaaS/Technology": {
        "description": "SaaS or platform company with technical data/AI team",
        "headcount": 25,
        "roles": [
            ("Chief Data Officer", 1),
            ("Data Architect", 1),
            ("Senior Data Engineer", 2),
            ("Data Engineer", 3),
            ("Data Scientist", 2),
            ("ML Engineer", 2),
            ("MLOps Engineer", 1),
            ("AI Engineer", 1),
            ("Analytics Engineer", 1),
            ("Senior Data Analyst", 1),
            ("Data Analyst", 2),
            ("BI Developer", 2),
            ("Data Quality Manager", 1),
            ("Data Product Manager", 1),
            ("DataOps Engineer", 1),
        ]
    },
    "Healthcare/Life Sciences": {
        "description": "Regulated industry with clinical/privacy focus",
        "headcount": 22,
        "roles": [
            ("Chief Data Officer", 1),
            ("Data Governance Director", 1),
            ("Data Compliance Analyst", 1),
            ("Data Protection Officer", 1),
            ("Data Privacy Specialist", 1),
            ("Senior Data Engineer", 1),
            ("Data Engineer", 2),
            ("Data Scientist", 1),
            ("Senior Data Analyst", 2),
            ("Data Analyst", 3),
            ("BI Developer", 2),
            ("Clinical Data Manager", 1),
            ("Data Quality Manager", 1),
            ("Master Data Manager", 1),
        ]
    },
    "Mid-Market Retail/Consumer": {
        "description": "Smaller, analytics-heavy team with minimal governance structure",
        "headcount": 12,
        "roles": [
            ("Senior Data Analyst", 1),
            ("Data Analyst", 3),
            ("BI Developer", 2),
            ("Data Engineer", 2),
            ("Analytics Engineer", 1),
            ("Data Scientist", 1),
            ("Data Quality Manager", 1),
            ("Marketing Analyst", 1),
        ]
    }
}

def map_role_to_atlas(job_title):
    """Try to match a job title to WIDAI roles"""
    title_lower = job_title.lower().strip()

    # Direct match first
    if title_lower in role_lookup:
        info = role_lookup[title_lower]
        return {
            'matched': True,
            'role_id': info['role_id'],
            'canonical_title': info['canonical_title'],
            'category': info['category'],
            'has_ksa': info['has_ksa'],
            'readiness': 'Full' if info['has_ksa'] else 'Partial'
        }

    # Fuzzy/semantic matching
    fuzzy_matches = []
    for stored_title, info in role_lookup.items():
        score = 0
        title_words = set(title_lower.split())
        stored_words = set(stored_title.split())

        # Check keyword overlap
        common_words = title_words & stored_words
        if common_words:
            score += len(common_words) * 10

        # Special case handling
        if 'marketing analyst' in title_lower and 'data analyst' in stored_title:
            score += 5
        if 'clinical data manager' in title_lower and 'data quality' in stored_title:
            score += 5
        if 'model risk officer' in title_lower and ('risk' in stored_title or 'compliance' in stored_title):
            score += 8

        if score > 0:
            fuzzy_matches.append((score, info))

    if fuzzy_matches:
        fuzzy_matches.sort(key=lambda x: x[0], reverse=True)
        info = fuzzy_matches[0][1]
        return {
            'matched': True,
            'role_id': info['role_id'],
            'canonical_title': info['canonical_title'],
            'category': info['category'],
            'has_ksa': info['has_ksa'],
            'readiness': 'Full' if info['has_ksa'] else 'Partial'
        }

    return {
        'matched': False,
        'role_id': None,
        'canonical_title': None,
        'category': None,
        'has_ksa': False,
        'readiness': 'None'
    }

# Process all archetypes
results = {}
unmapped_across_archetypes = defaultdict(int)

for arch_name, arch_data in archetypes.items():
    arch_results = {
        'description': arch_data['description'],
        'declared_headcount': arch_data['headcount'],
        'roles_in_team': [],
    }

    for job_title, count in arch_data['roles']:
        mapping = map_role_to_atlas(job_title)
        arch_results['roles_in_team'].append({
            'title': job_title,
            'count': count,
            **mapping
        })
        if not mapping['matched']:
            unmapped_across_archetypes[job_title] += 1

    # Calculate metrics
    total_roles = len(arch_results['roles_in_team'])
    mapped = sum(1 for r in arch_results['roles_in_team'] if r['matched'])
    full_ksa = sum(1 for r in arch_results['roles_in_team'] if r['has_ksa'])

    arch_results['mapping_summary'] = {
        'total_roles': total_roles,
        'roles_mapped': mapped,
        'roles_mapped_pct': round((mapped / total_roles * 100) if total_roles else 0, 1),
        'roles_with_full_ksa': full_ksa,
        'roles_with_full_ksa_pct': round((full_ksa / total_roles * 100) if total_roles else 0, 1),
        'unmapped_roles': [r['title'] for r in arch_results['roles_in_team'] if not r['matched']]
    }

    results[arch_name] = arch_results

# Calculate cross-archetype metrics
all_mapped = sum(r['mapping_summary']['roles_mapped'] for r in results.values())
all_total = sum(r['mapping_summary']['total_roles'] for r in results.values())
all_full_ksa = sum(r['mapping_summary']['roles_with_full_ksa'] for r in results.values())

overall_coverage = round((all_mapped / all_total * 100) if all_total else 0, 1)
overall_ksa_coverage = round((all_full_ksa / all_total * 100) if all_total else 0, 1)

# Most common unmapped roles
top_unmapped = sorted(unmapped_across_archetypes.items(), key=lambda x: x[1], reverse=True)

# Generate summary
summary = {
    'test_date': '2026-03-26',
    'test_version': 'R01',
    'atlas_version': '0.4.0',
    'archetype_count': len(results),
    'total_roles_analyzed': all_total,
    'total_roles_mapped': all_mapped,
    'overall_coverage_pct': overall_coverage,
    'overall_ksa_coverage_pct': overall_ksa_coverage,
    'most_common_gaps': [{'role': role, 'frequency': count} for role, count in top_unmapped[:10]],
    'archetypes': results,
    'decision_gate': {
        'threshold': 60,
        'measured': overall_ksa_coverage,
        'result': 'PASS' if overall_ksa_coverage >= 60 else 'FAIL',
        'interpretation': 'Can proceed to Tier 1' if overall_ksa_coverage >= 60 else 'Recommend focused KSA sprint'
    }
}

# Save JSON output
with open('docs/roadmap/R01-coverage-gap-test.json', 'w') as f:
    json.dump(summary, f, indent=2)

print("\nR01 COVERAGE GAP TEST RESULTS")
print("=" * 70)
print(f"Overall Coverage: {overall_coverage}% ({all_mapped}/{all_total} roles)")
print(f"KSA Coverage: {overall_ksa_coverage}% ({all_full_ksa}/{all_total} roles)")
print(f"Decision Gate (≥60%): {'PASS' if overall_ksa_coverage >= 60 else 'FAIL'}")
print(f"\nTop Unmapped Roles (frequency across archetypes):")
for role, count in top_unmapped[:5]:
    print(f"  {role}: {count} archetype(s)")

print("\nPer-Archetype Results:")
for name, result in results.items():
    print(f"\n{name}:")
    print(f"  Coverage: {result['mapping_summary']['roles_mapped_pct']}%")
    print(f"  KSA Coverage: {result['mapping_summary']['roles_with_full_ksa_pct']}%")
    if result['mapping_summary']['unmapped_roles']:
        print(f"  Gaps: {', '.join(result['mapping_summary']['unmapped_roles'])}")
