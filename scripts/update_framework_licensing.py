#!/usr/bin/env python3
"""Update frameworks.json with commercial_status and license_classification fields.
Based on R05 License Audit and R05 Dependency Analysis results."""

import json

FRAMEWORKS_PATH = "/sessions/awesome-elegant-mayer/mnt/ATLAS/atlas-dataset/frameworks/frameworks.json"

# Classification map: framework_id -> (license_class, commercial_status, license_type, notes)
CLASSIFICATIONS = {
    # GREEN — Clear for commercial use
    "80000_HOURS": ("GREEN", "approved", "Free educational content", ""),
    "ATLAS": ("GREEN", "approved", "Project-specific", "Self-reference"),
    "BLS_SOC": ("GREEN", "approved", "Public Domain (U.S. Government)", ""),
    "DATA_MESH": ("GREEN", "approved", "Open architectural pattern", "Credit Zhamak Dehghani"),
    "DBT_LABS": ("GREEN", "approved", "Apache License 2.0", "Include Apache 2.0 notice"),
    "DCWF": ("GREEN", "approved", "Public Domain (U.S. Government)", ""),
    "DDAT": ("GREEN", "approved", "Open Government Licence v3.0", "Attribution required to UK Government"),
    "EU_AI_ACT": ("GREEN", "approved", "Public Domain (EU legislation)", ""),
    "EVIDENCE_ACT": ("GREEN", "approved", "Public Domain (U.S. Government)", ""),
    "EXECUTIVE_ORDER": ("GREEN", "approved", "Public Domain (U.S. Government)", ""),
    "FDA": ("GREEN", "approved", "CC0 1.0 Universal", "No attribution required"),
    "FED_SR_11_7": ("GREEN", "approved", "Public Domain (U.S. Government)", ""),
    "GDPR": ("GREEN", "approved", "Public Domain (EU legislation)", ""),
    "HIPAA": ("GREEN", "approved", "Public Domain (U.S. Government)", ""),
    "NIST_AI_RMF": ("GREEN", "approved", "Public Domain (U.S. Government)", ""),
    "NIST_NICE": ("GREEN", "approved", "Public Domain (U.S. Government)", ""),
    "O*NET": ("GREEN", "approved", "CC BY 4.0", "Attribution required to USDOL/ETA"),
    "OCC": ("GREEN", "approved", "Public Domain (U.S. Government)", ""),
    "SINGAPORE_MAIG": ("GREEN", "approved", "Government framework", ""),
    # Reclassified GREEN — Thomas's original practitioner expertise
    "PRACTITIONER_COMMUNITY": ("GREEN", "approved", "ATLAS original (practitioner expertise)", "Reclassified from YELLOW per author confirmation 2026-03-26"),
    
    # RED — Excluded from commercial distribution (citation-only, zero data loss)
    "BCG": ("RED", "excluded-commercial", "Proprietary (copyrighted)", "Citation-only dependency; safe to exclude"),
    "CDO_MAGAZINE": ("RED", "excluded-commercial", "Editorial copyright", "Citation-only dependency; safe to exclude"),
    "CMMI_DMM": ("RED", "excluded-commercial", "Proprietary (ISACA)", "Citation-only; annual license required for commercial use"),
    "COBIT_2019": ("RED", "excluded-commercial", "Proprietary (ISACA)", "Citation-only; annual license required for commercial use"),
    "DAMA_DMBOK": ("RED", "excluded-commercial", "Mixed CC BY-ND / Proprietary", "Citation-only; 26 mappings but no structural derivatives. License or rewrite if upgrading to premium tier"),
    "DELOITTE": ("RED", "excluded-commercial", "Proprietary (consulting)", "Citation-only dependency; safe to exclude"),
    "FORRESTER": ("RED", "excluded-commercial", "Proprietary (analyst research)", "Citation-only dependency; safe to exclude"),
    "GARTNER": ("RED", "excluded-commercial", "Proprietary (analyst research)", "Explicitly prohibits AI training/derivatives; citation-only; safe to exclude"),
    "HBR": ("RED", "excluded-commercial", "Proprietary (Harvard Business Publishing)", "Citation-only dependency; safe to exclude"),
    "IDC": ("RED", "excluded-commercial", "Proprietary (analyst research)", "Citation-only dependency; safe to exclude"),
    "IEEE": ("RED", "excluded-commercial", "Copyrighted standards", "Citation-only dependency; safe to exclude"),
    "ISACA": ("RED", "excluded-commercial", "Proprietary (ISACA)", "Citation-only; all frameworks require licensing"),
    "ISO_23894": ("RED", "excluded-commercial", "Copyrighted (ISO)", "Citation-only; standard ID reference only"),
    "ISO_27001": ("RED", "excluded-commercial", "Copyrighted (ISO)", "Citation-only; standard ID reference only"),
    "ISO_27701": ("RED", "excluded-commercial", "Copyrighted (ISO)", "Citation-only; standard ID reference only"),
    "ISO_38505": ("RED", "excluded-commercial", "Copyrighted (ISO)", "Citation-only; standard ID reference only"),
    "ISO_42001": ("RED", "excluded-commercial", "Copyrighted (ISO)", "Citation-only; 8 mappings. Consider licensing for UC2 premium tier"),
    "ISO_5338": ("RED", "excluded-commercial", "Copyrighted (ISO)", "Citation-only; standard ID reference only"),
    "ISO_8000": ("RED", "excluded-commercial", "Copyrighted (ISO)", "Citation-only; standard ID reference only"),
    "KPMG": ("RED", "excluded-commercial", "Proprietary (consulting)", "Citation-only dependency; safe to exclude"),
    "MCKINSEY": ("RED", "excluded-commercial", "Proprietary (consulting)", "Citation-only dependency; safe to exclude"),
    "WEF": ("RED", "excluded-commercial", "CC BY-NC-ND 4.0", "Complete commercial blocker; citation-only; safe to exclude"),
    
    # YELLOW — Conditional, case-by-case assessment
    "AICPA": ("YELLOW", "conditional", "Proprietary (professional association)", "Likely certification citation only"),
    "AIJOBS.NET": ("YELLOW", "conditional", "Proprietary (job platform)", "Market research reference only"),
    "AWS": ("YELLOW", "conditional", "Proprietary (cloud platform)", "Public documentation references; likely fair use"),
    "CDMC": ("YELLOW", "conditional", "Unknown (EDM Council)", "Needs publisher clarification"),
    "CONVERSATION_DESIGN_INSTITUTE": ("YELLOW", "conditional", "Unknown", "Needs publisher clarification"),
    "COURSERA": ("YELLOW", "conditional", "Mixed", "Generic role mapping only; course content excluded"),
    "DATAOPS.LIVE": ("YELLOW", "conditional", "Proprietary (SaaS)", "Market research reference only"),
    "DATAVERSITY": ("YELLOW", "conditional", "Proprietary (educational)", "Market research reference only"),
    "DCAM": ("YELLOW", "conditional", "Proprietary (EDM Council)", "Needs EDM Council clarification"),
    "DQOPS": ("YELLOW", "conditional", "Proprietary (SaaS)", "Market research reference only"),
    "DZONE": ("YELLOW", "conditional", "Copyrighted (developer content)", "Market research reference only"),
    "EC_COUNCIL": ("YELLOW", "conditional", "Proprietary (certifications)", "Certification citation only"),
    "GITLAB": ("YELLOW", "conditional", "Mixed (CC BY-NC-SA for some)", "General DevOps role references only"),
    "GLASSDOOR": ("YELLOW", "conditional", "Proprietary (job platform)", "Market research reference only"),
    "IAPP": ("YELLOW", "conditional", "Proprietary (professional association)", "Certification citation only"),
    "IBM": ("YELLOW", "conditional", "Proprietary (technology)", "Public documentation references; likely fair use"),
    "IIA": ("YELLOW", "conditional", "Proprietary (professional association)", "Three Lines Model reference; likely fair use for model name"),
    "INDEED": ("YELLOW", "conditional", "Proprietary (job platform)", "Market research reference only"),
    "LINKEDIN": ("YELLOW", "conditional", "Proprietary (Microsoft)", "15 mappings; market research only; no verbatim data stored"),
    "MICROSOFT": ("YELLOW", "conditional", "Proprietary (technology)", "Public documentation references; likely fair use"),
    "MIT_SLOAN": ("YELLOW", "conditional", "Proprietary (academic)", "Research citation only"),
    "MONTE_CARLO_DATA": ("YELLOW", "conditional", "Proprietary (SaaS)", "Market research reference only"),
    "ODSC": ("YELLOW", "conditional", "Proprietary (educational)", "Market research reference only"),
    "SCALE_AI": ("YELLOW", "conditional", "Proprietary (SaaS)", "Market research reference only"),
    "STANFORD_HAI": ("YELLOW", "conditional", "Proprietary (academic)", "Research citation only"),
    "TDWI": ("YELLOW", "conditional", "Proprietary (professional development)", "Market research reference only"),
    "THOUGHTWORKS": ("YELLOW", "conditional", "Proprietary (consulting)", "Tech Radar reference only"),
    "VELLUM": ("YELLOW", "conditional", "Proprietary (SaaS)", "Market research reference only"),
}

def main():
    with open(FRAMEWORKS_PATH, 'r') as f:
        data = json.load(f)
    
    updated = 0
    for fw in data['frameworks']:
        fid = fw['framework_id']
        if fid in CLASSIFICATIONS:
            cls, status, license_type, notes = CLASSIFICATIONS[fid]
            fw['license_classification'] = cls
            fw['commercial_status'] = status
            fw['license_type'] = license_type
            if notes:
                fw['commercial_notes'] = notes
            updated += 1
        else:
            print(f"WARNING: No classification for {fid}")
    
    # Add metadata
    data['commercial_audit_date'] = '2026-03-26'
    data['commercial_audit_ref'] = 'R05-license-audit, R05-dependency-analysis'
    
    # Count by classification
    green = sum(1 for fw in data['frameworks'] if fw.get('license_classification') == 'GREEN')
    yellow = sum(1 for fw in data['frameworks'] if fw.get('license_classification') == 'YELLOW')
    red = sum(1 for fw in data['frameworks'] if fw.get('license_classification') == 'RED')
    
    with open(FRAMEWORKS_PATH, 'w') as f:
        json.dump(data, f, indent=2)
    
    print(f"Updated {updated}/{len(data['frameworks'])} frameworks")
    print(f"GREEN: {green} | YELLOW: {yellow} | RED: {red}")
    print(f"Practitioner Community reclassified: YELLOW -> GREEN")

if __name__ == '__main__':
    main()
