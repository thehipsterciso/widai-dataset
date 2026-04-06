#!/usr/bin/env python3
"""
STRM-002-NICE: Build strm_mapping.json
Maps all 2,148 NICE Framework v2.1.0 TKS elements against WIDAI KSA Pool v0.5.2

Approach:
  1. Bi-encoder cosine screening (pre-computed in nice_tks_candidates.json)
  2. Keyword-domain matching for scope classification
  3. Relationship type assignment based on semantic scope analysis
"""

import json, os, re
from collections import Counter

# Load candidates (pre-computed bi-encoder screening)
with open('sources/nice_framework/nice_tks_candidates.json') as f:
    candidates = json.load(f)

# === SCOPE CLASSIFICATION RULES ===

# Keywords that strongly indicate OUT of WIDAI scope (purely tactical cyber ops)
OUT_OF_SCOPE_KEYWORDS = [
    r'\bmalware\b', r'\bexploit\w*\b', r'\bforensic\w*\b', r'\bpenetration test\w*\b',
    r'\bintrusion\b', r'\bpacket\s+analy\w*\b', r'\bincident\s+response\b',
    r'\bthreat\s+hunt\w*\b', r'\bvulnerability\s+scan\w*\b', r'\breverse\s+engineer\w*\b',
    r'\bCOMSEC\b', r'\bcryptanaly\w*\b', r'\bsignal\s+jamm\w*\b', r'\bSIGINT\b',
    r'\bHUMINT\b', r'\bcyber\s*attack\b', r'\bcountermeasure\b', r'\bphishing\b',
    r'\bindicators?\s+of\s+compromise\b', r'\bIDS\b', r'\bIPS\b', r'\bfirewall\b',
    r'\bVPN\b', r'\bdigital\s+evidence\b', r'\bchain\s+of\s+custody\b',
    r'\bweapon\w*\b', r'\bammunition\b', r'\bmunition\b',
    r'\bcyber\s*crime\b', r'\blaw\s+enforcement\b', r'\bcriminal\b',
    r'\bcovert\b', r'\bclandestine\b', r'\bespionage\b', r'\bintelligence\s+collect\w*\b',
    r'\btarget\s+(network|system|vulnerabilit)\w*\b',
    r'\bdrive\s+image\b', r'\bmount\s+a\s+drive\b', r'\bimage\s+collection\b',
    r'\bthreat\s+actor\b', r'\bmimick\w*\b', r'\bred\s+team\b',
    r'\bexploitation\b', r'\boffensive\b',
    r'\bjamming\b', r'\bspoofing\b', r'\bsniffing\b',
    r'\bwireless\s+(attack|exploit|hack)\w*\b',
    r'\bnetwork\s+exploitation\b', r'\bnetwork\s+defense\b',
    r'\bcyber\s+operations?\b', r'\bcyber\s+threat\b',
    r'\bwar\s*fight\w*\b', r'\bmilitar\w*\b', r'\bcombat\b',
    r'\bintelligence\s+(analysis|operation|report)\w*\b',
    r'\bcollection\s+(manag|plan|strateg)\w*\b',
]

# Keywords that strongly indicate IN WIDAI scope (governance, data, AI, risk, compliance)
IN_SCOPE_KEYWORDS = [
    r'\bdata\s+(governance|quality|management|admin|steward|integr|catalog|lineage|architect|pipeline|lake|warehouse|model)\w*\b',
    r'\bprivacy\b', r'\bPIA\b', r'\bdata\s+protect\w*\b', r'\bPII\b', r'\bGDPR\b',
    r'\bartificial\s+intelligence\b', r'\b(AI|ML)\b', r'\bmachine\s+learn\w*\b',
    r'\brisk\s+(manag|assess|quantif|mitigat|fram|appetit|toleran)\w*\b',
    r'\bcompl(iance|y)\b', r'\bregulatv?\w*\b', r'\baudit\w*\b',
    r'\bgovernance\b', r'\bpolicy\b', r'\bpolicies\b',
    r'\bstrateg(y|ic)\b', r'\bleadership\b', r'\bworkforce\b',
    r'\bstakeholder\b', r'\bbudget\w*\b', r'\bprogram\s+manag\w*\b',
    r'\bservice[\s-]+level\b', r'\bSLA\b',
    r'\banalytics\b', r'\bstatistic\w*\b', r'\bvisualizat\w*\b',
    r'\bdata\s+analy\w*\b', r'\bdata\s+mining\b',
    r'\bdocumentat\w*\b', r'\breport\w*\b',
    r'\bsupply\s+chain\b', r'\bvendor\b', r'\bthird[\s-]+party\b',
    r'\bchange\s+manag\w*\b', r'\bconfiguration\s+manag\w*\b',
    r'\bincident\s+manag\w*\b',  # management vs response
    r'\bcontinuous\s+(monitor|improv)\w*\b',
    r'\bsecurity\s+(policy|governance|strategy|program|assessment|control|framework|posture|requirement)\w*\b',
    r'\binformation\s+security\b', r'\bcybersecurity\s+(policy|governance|strategy|program|risk|workforce|budget|training|awareness)\w*\b',
    r'\benterprise\s+architect\w*\b', r'\bsystem\w*\s+architect\w*\b',
    r'\bproject\s+manag\w*\b', r'\bproject\s+plan\w*\b',
    r'\btraining\b', r'\beducat\w*\b', r'\bcurricul\w*\b', r'\bawareness\b',
    r'\bknowledge\s+manag\w*\b', r'\bsoftware\s+develop\w*\b',
    r'\bcloud\b', r'\bencrypt\w*\b', r'\baccess\s+control\w*\b',
    r'\bidentity\b', r'\bauthenticat\w*\b', r'\bauthoriz\w*\b',
    r'\binformation\s+assurance\b', r'\boperational\s+technolog\w*\b',
    r'\bagentic\s+AI\b',
]

# WIDAI domain mapping hints based on NICE concept keywords
DOMAIN_HINTS = {
    'DG': [r'\bdata\s+(governance|steward|policy|policies|admin|catalog|lineage|classif)\w*\b', r'\bmetadata\b'],
    'DA': [r'\bdata(base|bases)\b', r'\bdata\s+(architect|platform|pipeline|warehouse|lake|model)\w*\b', r'\bETL\b', r'\bSQL\b'],
    'DQ': [r'\bdata\s+(quality|integr|valid|cleans)\w*\b', r'\bdata\s+standard\b'],
    'AI': [r'\bartificial\s+intelligence\b', r'\bmachine\s+learn\w*\b', r'\b(AI|ML)\b', r'\bneural\b', r'\bdeep\s+learn\w*\b', r'\bagentic\b', r'\bmodel\s+(train|develop|deploy)\w*\b'],
    'AG': [r'\bAI\s+(ethic|governance|bias|fairness|safe)\w*\b', r'\bresponsible\s+AI\b', r'\balgorithm\w*\s+(bias|fairness|transparen)\w*\b'],
    'SP': [r'\bprivacy\b', r'\bPIA\b', r'\bDPIA\b', r'\bdata\s+protect\w*\b', r'\bPII\b', r'\bGDPR\b', r'\bpersonal\s+data\b'],
    'AB': [r'\banalytics\b', r'\bstatistic\w*\b', r'\bvisualizat\w*\b', r'\bdata\s+analy\w*\b', r'\bdata\s+mining\b', r'\bdashboard\b'],
    'LS': [r'\bstrateg(y|ic)\b', r'\bleadership\b', r'\bworkforce\b', r'\bstakeholder\b', r'\bbudget\w*\b', r'\bprogram\s+manag\w*\b', r'\bexecutive\b', r'\bboard\b'],
    'OP': [r'\bservice[\s-]+level\b', r'\bSLA\b', r'\boperati\w+\b', r'\bdeployment\b', r'\bmonitoring\b', r'\bconfiguration\s+manag\w*\b', r'\bchange\s+manag\w*\b'],
    'RC': [r'\bcompl(iance|y)\b', r'\bregulatv?\w*\b', r'\baudit\w*\b', r'\bassess\w*\b', r'\bcontrol\s+(assess|evaluat)\w*\b'],
    'RM': [r'\brisk\s+(manag|assess|quantif|mitigat|fram|appetit|toleran)\w*\b', r'\bthreat\s+(assess|model)\w*\b'],
    'TF': [r'\barchitect\w*\b', r'\binfrastructur\w*\b', r'\bsoftware\s+develop\w*\b', r'\bcoding\b', r'\bprogram\w*\s+language\b', r'\bcloud\b', r'\bnetwork\w*\b', r'\bsystem\w*\s+admin\b'],
}

def match_keywords(text, patterns):
    """Check if text matches any of the regex patterns."""
    text_lower = text.lower()
    for pattern in patterns:
        if re.search(pattern, text_lower, re.IGNORECASE):
            return True
    return False

def get_domain_hints(text):
    """Get WIDAI domains that the text hints at."""
    hints = []
    text_lower = text.lower()
    for domain, patterns in DOMAIN_HINTS.items():
        for pattern in patterns:
            if re.search(pattern, text_lower, re.IGNORECASE):
                hints.append(domain)
                break
    return hints

def classify_element(candidate):
    """Classify a NICE TKS element for STRM mapping."""
    text = candidate['fde_text']
    top_cosine = candidate['top_cosine']
    best_match = candidate['candidates'][0]
    
    # Step 1: Check for strong out-of-scope signals
    is_out_of_scope = match_keywords(text, OUT_OF_SCOPE_KEYWORDS)
    is_in_scope = match_keywords(text, IN_SCOPE_KEYWORDS)
    
    # Step 2: Combined signal
    # If clearly out of scope AND low cosine, it's No Relationship
    if is_out_of_scope and not is_in_scope and top_cosine < 0.50:
        return 'no_relationship', None, 'out_of_scope_cyber'
    
    # If clearly out of scope but high cosine, it might still have a relationship
    # (e.g., "network defense policy" — defense is out-of-scope keyword, but policy is in-scope)
    if is_out_of_scope and is_in_scope:
        # Mixed signals — evaluate based on cosine
        if top_cosine >= 0.45:
            return 'evaluate', best_match, 'mixed_signals'
        else:
            return 'no_relationship', None, 'mixed_but_weak'
    
    # If clearly in scope, evaluate
    if is_in_scope:
        return 'evaluate', best_match, 'in_scope_keywords'
    
    # No strong keyword signals — use cosine threshold
    if top_cosine >= 0.50:
        return 'evaluate', best_match, 'cosine_threshold'
    elif top_cosine >= 0.40:
        # Borderline — check if the best match domain makes sense
        domain_hints = get_domain_hints(text)
        if domain_hints or best_match['cosine'] >= 0.45:
            return 'evaluate', best_match, 'borderline_with_hints'
        else:
            return 'no_relationship', None, 'borderline_no_hints'
    else:
        return 'no_relationship', None, 'low_cosine'

def determine_relationship_type(nice_text, nice_type, ksa_statement, ksa_type, ksa_domain, cosine):
    """Determine the NIST IR 8477 relationship type."""
    nice_lower = nice_text.lower()
    ksa_lower = ksa_statement.lower()
    
    # High cosine + similar scope = potential Equal
    if cosine >= 0.70:
        return 'Equal'
    
    # NICE is a cybersecurity framework; its elements are typically broader than
    # WIDAI's domain-specific KSAs, or they intersect at the governance/management level
    
    # Check if NICE element is more general than WIDAI KSA
    # NICE elements are typically short and general; WIDAI KSAs are long and specific
    if len(nice_text) < len(ksa_statement) * 0.5:
        # NICE is much shorter/more general → likely Superset
        if cosine >= 0.55:
            return 'Superset of'
        else:
            return 'Intersects with'
    
    # Default for cross-framework mapping: Intersects with
    # This is correct for most cases where a cybersecurity framework element
    # partially overlaps with a data/AI domain framework element
    return 'Intersects with'

def generate_notes(nice_el, classification, match, reason, candidates_list):
    """Generate mapping notes."""
    text = nice_el['fde_text']
    fde_type = nice_el['fde_type']
    
    if classification == 'no_relationship':
        if reason == 'out_of_scope_cyber':
            return f"Tactical cybersecurity element outside WIDAI scope. WIDAI covers data and AI workforce competencies, not operational cyber defense. No gap — intentionally out of scope."
        elif reason == 'low_cosine':
            return f"No meaningful semantic overlap with any WIDAI KSA (top cosine: {nice_el['top_cosine']:.3f}). Element is specific to cybersecurity operations with no data/AI governance equivalent."
        elif reason == 'mixed_but_weak':
            return f"Contains both cybersecurity and governance keywords but weak semantic match to WIDAI KSAs (cosine: {nice_el['top_cosine']:.3f}). Classified as out of WIDAI scope."
        elif reason == 'borderline_no_hints':
            return f"Borderline cosine ({nice_el['top_cosine']:.3f}) but no domain alignment with WIDAI's 12 knowledge domains. Cybersecurity-specific element."
        else:
            return f"No relationship to WIDAI KSA pool. {reason}."
    
    # Has a relationship
    secondary = []
    for c in candidates_list[1:3]:
        if c['cosine'] >= 0.40:
            secondary.append(f"{c['ksa_id']} ({c['domain_code']}, cosine: {c['cosine']:.3f})")
    
    sec_note = f" Secondary: {', '.join(secondary)}." if secondary else ""
    
    if match:
        return f"NICE {fde_type} intersects with WIDAI {match['domain_code']} domain. {match['type']} {match['ksa_id']} is the strongest semantic match.{sec_note}"

    return f"Mapped based on semantic analysis.{sec_note}"


# === MAIN MAPPING LOOP ===
mappings = []
stats = Counter()

for cand in candidates:
    classification, match, reason = classify_element(cand)
    stats[classification] += 1
    stats[f"{classification}_{reason}"] += 1
    
    if classification == 'no_relationship':
        mapping = {
            'fde_id': cand['fde_id'],
            'fde_type': cand['fde_type'],
            'fde_name': '',  # NICE TKS don't have titles
            'fde_description': cand['fde_text'],
            'rationale': 'Semantic',
            'relationship': 'No relationship',
            'ref_id': None,
            'ref_statement': None,
            'strength': 0,
            'notes': generate_notes(cand, classification, None, reason, cand['candidates'])
        }
    else:
        # Determine relationship type
        rel_type = determine_relationship_type(
            cand['fde_text'], cand['fde_type'],
            match['statement'], match['type'],
            match['domain_code'], match['cosine']
        )
        
        mapping = {
            'fde_id': cand['fde_id'],
            'fde_type': cand['fde_type'],
            'fde_name': '',
            'fde_description': cand['fde_text'],
            'rationale': 'Semantic',
            'relationship': rel_type,
            'ref_id': match['ksa_id'],
            'ref_statement': match['statement'],
            'strength': 0,  # Will be computed by scoring pipeline
            'notes': generate_notes(cand, classification, match, reason, cand['candidates'])
        }
    
    mappings.append(mapping)

# Print statistics
print(f"\n=== CLASSIFICATION STATISTICS ===")
print(f"Total elements: {len(mappings)}")
print(f"  Evaluate (has relationship): {stats['evaluate']}")
print(f"  No relationship: {stats['no_relationship']}")
print(f"\nEvaluate reasons:")
for k, v in sorted(stats.items()):
    if k.startswith('evaluate_'):
        print(f"  {k}: {v}")
print(f"\nNo relationship reasons:")
for k, v in sorted(stats.items()):
    if k.startswith('no_relationship_'):
        print(f"  {k}: {v}")

# Relationship type distribution
rel_types = Counter(m['relationship'] for m in mappings)
print(f"\nRelationship types:")
for rt, cnt in rel_types.most_common():
    print(f"  {rt}: {cnt} ({cnt*100/len(mappings):.1f}%)")

# By NICE element type
for etype in ['task', 'knowledge', 'skill']:
    type_rels = Counter(m['relationship'] for m in mappings if m['fde_type'] == etype)
    total = sum(type_rels.values())
    has_rel = total - type_rels.get('No relationship', 0)
    print(f"\n{etype.upper()} ({total}): {has_rel} with relationships ({has_rel*100/total:.1f}%)")

# Save the mapping
output = {
    'strm_id': 'STRM-002-NICE',
    'focal_document': 'NIST NICE Framework v2.1.0',
    'focal_document_version': '2.1.0',
    'focal_document_date': '2025-12-03',
    'focal_document_source': 'NIST SP 800-181 Rev. 1',
    'reference_document': 'WIDAI KSA Pool v0.5.2',
    'mapping_date': '2026-04-01',
    'rationale_type_default': 'Semantic',
    'total_fdes_in_scope': len(mappings),
    'mappings': mappings
}

os.makedirs('strm/nice', exist_ok=True)
with open('strm/nice/strm_mapping.json', 'w') as f:
    json.dump(output, f, indent=2)

print(f"\nMapping saved to strm/nice/strm_mapping.json")
