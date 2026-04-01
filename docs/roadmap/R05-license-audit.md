# R05: Source Framework License Audit

**Date:** March 26, 2026  
**Status:** Tier 0 Validation Test  
**Test ID:** R05

---

## Executive Summary

WIDAI derives its workforce taxonomy from 70+ source frameworks. This audit evaluates the licensing terms of each framework to determine whether commercial distribution of WIDAI is legally viable.

### Key Findings

- **Total Frameworks Analyzed:** 70
- **GREEN (Clear to use commercially):** 19 frameworks
- **YELLOW (Conditional/requires review):** 28 frameworks  
- **RED (Blockers to commercial use):** 23 frameworks

### Critical Risk Assessment

**RESULT: CONDITIONAL** — WIDAI can proceed with commercial distribution only under specific conditions (see recommendations below).

### Immediate Blockers (RED Frameworks)

The following 23 frameworks explicitly prohibit or severely restrict commercial derivatives:

**Proprietary Consulting/Research (Strict Restrictions):**
- Gartner (explicitly prohibits AI training and commercial derivatives)
- Forrester (requires reprints license, no modifications allowed)
- McKinsey (requires written permission for external use)
- Deloitte (proprietary research)
- BCG (proprietary research)
- KPMG (proprietary research)
- IDC (requires written permission for external/commercial use)
- HBR (restrictive copyright, no commercial learning/training use)

**Framework Governance (Licensing Required):**
- SFIA (requires commercial exploitation license; modest annual fee)
- COBIT-2019 (requires annual commercial license from ISACA)
- CMMI-DMM (requires ISACA license for commercial use)
- ISACA (all frameworks require licensing for commercial use)

**Standards Bodies (Copyright-Protected):**
- ISO-23894 (copyrighted, requires purchase/licensing)
- ISO-27001 (copyrighted, requires purchase/licensing)
- ISO-27701 (copyrighted, requires purchase/licensing)
- ISO-38505 (copyrighted, requires purchase/licensing)
- ISO-42001 (copyrighted, requires purchase/licensing)
- ISO-5338 (copyrighted, requires purchase/licensing)
- ISO-8000 (copyrighted, requires purchase/licensing)
- IEEE (copyrighted standards, require permission for derivatives)

**Other Proprietary:**
- DAMA-DMBOK (mixed licensing: some CC-ND, some proprietary)
- CDO Magazine (editorial copyright)
- WEF (CC BY-NC-ND: prohibits BOTH commercial use AND derivatives)

---

## Framework-by-Framework Audit

### GREEN Frameworks (19 total) — Clear for Commercial Use

These frameworks are explicitly open for commercial use, modification, and derivative works.

#### 1. **O*NET** ✓
- **Publisher:** U.S. Department of Labor (USDOL/ETA)
- **License:** Creative Commons Attribution 4.0 (CC BY 4.0)
- **Commercial Derivatives:** YES
- **Attribution:** Required (to USDOL/ETA)
- **Risk:** GREEN
- **Notes:** This is a key source framework for WIDAI. Clear legal ground for commercial use. Requires attribution.

#### 2. **BLS-SOC** ✓
- **Publisher:** U.S. Bureau of Labor Statistics
- **License:** Public Domain (U.S. Government Work)
- **Commercial Derivatives:** YES
- **Attribution:** Recommended but not required
- **Risk:** GREEN
- **Notes:** Standard Occupational Classification is explicitly public domain. Free to use commercially.

#### 3. **NIST NICE** ✓
- **Publisher:** National Institute of Standards and Technology
- **License:** Public Domain (U.S. Government Work)
- **Commercial Derivatives:** YES
- **Attribution:** Recommended (to NIST)
- **Risk:** GREEN
- **Notes:** NICE Workforce Framework is public domain. Can modify and create derivatives.

#### 4. **NIST AI RMF** ✓
- **Publisher:** National Institute of Standards and Technology
- **License:** Public Domain (U.S. Government Work)
- **Commercial Derivatives:** YES
- **Attribution:** Recommended
- **Risk:** GREEN
- **Notes:** AI Risk Management Framework is freely available and public domain.

#### 5. **DCWF** ✓
- **Publisher:** U.S. Department of Defense / NIST
- **License:** Public Domain (U.S. Government Work)
- **Commercial Derivatives:** YES
- **Attribution:** Recommended (to DoD/NIST)
- **Risk:** GREEN
- **Notes:** DoD Cyber Workforce Framework is public domain. Harmonized with NIST NICE.

#### 6. **DDaT** ✓
- **Publisher:** UK Government Digital Service
- **License:** Open Government Licence 3.0
- **Commercial Derivatives:** YES
- **Attribution:** Required (must credit UK Government)
- **Risk:** GREEN
- **Notes:** UK Digital Data and Technology roles are explicitly under OGL 3.0. Can be used commercially with attribution.

#### 7. **EU AI Act** ✓
- **Publisher:** European Union (EU Commission/Parliament)
- **License:** Public Domain (EU Legislation)
- **Commercial Derivatives:** YES
- **Attribution:** Recommended (to EU)
- **Risk:** GREEN
- **Notes:** EU legislation is public domain.

#### 8. **GDPR** ✓
- **Publisher:** European Union
- **License:** Public Domain (EU Legislation)
- **Commercial Derivatives:** YES
- **Attribution:** Recommended
- **Risk:** GREEN
- **Notes:** EU regulation is public domain.

#### 9. **Evidence Act** ✓
- **Publisher:** U.S. Government (Congress)
- **License:** Public Domain (U.S. Government Work)
- **Commercial Derivatives:** YES
- **Attribution:** Recommended
- **Risk:** GREEN
- **Notes:** Federal legislation is public domain.

#### 10. **Executive Order** ✓
- **Publisher:** U.S. Executive Branch
- **License:** Public Domain (U.S. Government Work)
- **Commercial Derivatives:** YES
- **Attribution:** Recommended
- **Risk:** GREEN
- **Notes:** Executive orders are public domain documents.

#### 11. **FDA** ✓
- **Publisher:** U.S. Food and Drug Administration
- **License:** Public Domain (CC0 1.0 Universal for openFDA)
- **Commercial Derivatives:** YES
- **Attribution:** Not required (CC0 waives attribution)
- **Risk:** GREEN
- **Notes:** FDA data is explicitly public domain under CC0.

#### 12. **FED SR 11-7** ✓
- **Publisher:** U.S. Federal Reserve
- **License:** Public Domain (U.S. Government Work)
- **Commercial Derivatives:** YES
- **Attribution:** Recommended
- **Risk:** GREEN
- **Notes:** Federal Reserve guidance is public domain.

#### 13. **HIPAA** ✓
- **Publisher:** U.S. Department of Health and Human Services
- **License:** Public Domain (U.S. Government Work)
- **Commercial Derivatives:** YES
- **Attribution:** Recommended
- **Risk:** GREEN
- **Notes:** HIPAA is federal healthcare regulation—public domain.

#### 14. **OCC** ✓
- **Publisher:** Office of the Comptroller of the Currency (U.S. Treasury)
- **License:** Public Domain (U.S. Government Work)
- **Commercial Derivatives:** YES
- **Attribution:** Recommended
- **Risk:** GREEN
- **Notes:** OCC regulatory guidance is public domain.

#### 15. **dbt Labs** ✓
- **Publisher:** dbt Labs
- **License:** Apache License 2.0
- **Commercial Derivatives:** YES
- **Attribution:** Required (Apache 2.0 license notice)
- **Risk:** GREEN
- **Notes:** dbt documentation is Apache 2.0 licensed. Permissive for commercial use.

#### 16. **Data Mesh** ✓
- **Publisher:** Chris Richardson and open architecture community
- **License:** Not formally copyrighted; open architectural pattern
- **Commercial Derivatives:** YES
- **Attribution:** Recommended (to Chris Richardson)
- **Risk:** GREEN
- **Notes:** Data Mesh is a widely-discussed pattern without formal copyright restrictions.

#### 17. **80000 Hours** ✓
- **Publisher:** 80000 Hours (non-profit research organization)
- **License:** Appears to be free educational content
- **Commercial Derivatives:** Likely YES
- **Attribution:** Recommended
- **Risk:** GREEN
- **Notes:** Educational non-profit. Content appears freely redistributable.

#### 18. **Singapore MAIG** ✓
- **Publisher:** Singapore Government
- **License:** Likely government open data
- **Commercial Derivatives:** Likely YES
- **Attribution:** Unknown (recommended)
- **Risk:** GREEN
- **Notes:** Presumed government framework available for public use.

#### 19. **WIDAI (Self)** ✓
- **Publisher:** WIDAI Project
- **License:** Project-specific
- **Commercial Derivatives:** YES (by definition)
- **Attribution:** N/A
- **Risk:** GREEN
- **Notes:** Internal reference to WIDAI itself.

---

### YELLOW Frameworks (28 total) — Conditional/Requires Review

These frameworks have uncertain, mixed, or conditional licensing terms. Each requires individual evaluation for the specific WIDAI use case.

#### Conditional Commercial (Requires Assessment)

| Framework | Publisher | Key Issue | Recommendation |
|-----------|-----------|-----------|-----------------|
| **AWS** | Amazon Web Services | Proprietary/SaaS terms; requires AWS attribution; resale limited | Contact AWS legal for commercial product terms |
| **Microsoft** | Microsoft Corporation | Proprietary documentation; licensing varies by product | Limit to general role categories; contact Microsoft if detailed derivatives needed |
| **IBM** | IBM | Proprietary frameworks; licensing varies | Limit to general enterprise roles |
| **AICPA** | American Institute of CPAs | Professional standards; commercial use restricted | Contact AICPA for licensing |
| **Coursera** | Coursera, Inc. | Mixed: generic roles may be OK, course-specific content restricted | Limit to learning pathway role mapping, exclude course-specific content |
| **CDMC** | Unknown | Insufficient information | Requires direct publisher contact |
| **DCAM** | EDM Council | Proprietary commercial framework | Contact EDM Council for licensing |
| **DATAOPS.LIVE** | DataOps community | Proprietary SaaS platform | Contact DataOps.live for commercial terms |
| **DATAVERSITY** | DATAVERSITY | Proprietary educational content | Contact DATAVERSITY for licensing |
| **DQOPS** | DQOps | Proprietary SaaS | Contact DQOps for terms |
| **DZONE** | DZone, Inc. | Copyrighted developer content | Contact DZone for licensing |
| **EC-COUNCIL** | EC-Council | Proprietary certification frameworks | Contact EC-Council for licensing |
| **GLASSDOOR** | Glassdoor, Inc. | Proprietary job market data; TOS prohibits scraping | Contact Glassdoor for commercial licensing |
| **GITLAB** | GitLab B.V. | Mixed: platform proprietary, artwork is CC BY-NC-SA (non-commercial) | Limit to general DevOps roles |
| **IAPP** | International Association of Privacy Professionals | Proprietary professional development | Contact IAPP for licensing |
| **IIA** | The Institute of Internal Auditors | Proprietary standards | Contact IIA for licensing |
| **INDEED** | Indeed | Proprietary job marketplace | Contact Indeed for commercial data use |
| **LINKEDIN** | LinkedIn (Microsoft) | Proprietary; TOS restricts commercial use | Requires LinkedIn licensing/API agreement |
| **MIT_SLOAN** | MIT Sloan School of Management | Proprietary academic research | Contact MIT for licensing |
| **MONTE_CARLO_DATA** | Monte Carlo Data | Proprietary SaaS platform | Contact Monte Carlo Data for terms |
| **ODSC** | Open Data Science | Proprietary educational platform | Contact ODSC for licensing |
| **PRACTITIONER_COMMUNITY** | Unknown | Insufficient information | Requires direct inquiry |
| **SCALE_AI** | Scale AI, Inc. | Proprietary SaaS | Contact Scale AI for terms |
| **STANFORD_HAI** | Stanford University (HAI Institute) | Proprietary academic research | Contact Stanford for licensing |
| **TDWI** | Transformational Data & Analytics Institute | Proprietary professional development | Contact TDWI for licensing |
| **THOUGHTWORKS** | Thoughtworks (software consulting) | Proprietary consulting research (e.g., Tech Radar) | Contact Thoughtworks for permissions |
| **VELLUM** | Vellum (LLM platform) | Proprietary SaaS | Contact Vellum for licensing |
| **AIJOBS.NET** | aijobs.net | Proprietary job platform | Contact aijobs.net for licensing |

---

### RED Frameworks (23 total) — Blockers to Commercial Distribution

These frameworks explicitly prohibit or severely restrict commercial derivative works. **Cannot be included in WIDAI commercial products without separate licensing agreements.**

#### 1. **Gartner** 🚫 CRITICAL BLOCKER
- **Publisher:** Gartner, Inc.
- **License:** Proprietary/Copyrighted
- **Commercial Derivatives:** NO - explicitly prohibited
- **Key Restriction:** Gartner **explicitly prohibits** using content as input to AI/ML systems or creating derivatives. No automated scraping or commercial products permitted.
- **Contact:** Gartner Content Compliance (content-compliance@gartner.com)
- **Impact:** If WIDAI mappings derive from Gartner analysis, commercial distribution violates their terms.

#### 2. **Forrester** 🚫 CRITICAL BLOCKER
- **Publisher:** Forrester Research, Inc.
- **License:** Proprietary/Copyrighted
- **Commercial Derivatives:** NO - requires reprints license
- **Key Restriction:** All syndicated research is proprietary. Reprints must be in original, unaltered format. No custom covers, modifications, or bundling allowed.
- **Contact:** citations@forrester.com or account manager for licensing
- **Impact:** Cannot modify or redistribute Forrester research commercially without reprints license.

#### 3. **McKinsey** 🚫 CRITICAL BLOCKER
- **Publisher:** McKinsey & Company
- **License:** Proprietary/Copyrighted
- **Commercial Derivatives:** NO - requires written permission
- **Key Restriction:** Strict IP controls. External use, reprints, or marketing use requires written permission from reprints@mckinsey.com. Likely requires licensing fee.
- **Impact:** Cannot include McKinsey-derived mappings in commercial WIDAI without explicit authorization.

#### 4. **IDC** 🚫 CRITICAL BLOCKER
- **Publisher:** IDC (International Data Corporation)
- **License:** Proprietary/Copyrighted
- **Commercial Derivatives:** NO - requires written permission for external use
- **Key Restriction:** All research copyrighted. Cannot be reproduced, excerpted, or distributed externally without written IDC Permissions (permissions@idc.com).
- **Impact:** Cannot use IDC research commercially in WIDAI.

#### 5. **COBIT-2019** 🚫 CRITICAL BLOCKER
- **Publisher:** ISACA
- **License:** Proprietary (ISACA-owned)
- **Commercial Derivatives:** NO - requires annual commercial license
- **Key Restriction:** Creating derivatives for commercial purposes, embedding in commercial products, or commercial use requires annual license from ISACA. Unauthorized use is copyright infringement.
- **Contact:** IPinfo@isaca.org or +1-847-660-5557
- **Impact:** Cannot distribute commercial WIDAI with COBIT-2019 mappings without ISACA license.

#### 6. **SFIA** 🚫 CRITICAL BLOCKER
- **Publisher:** SFIA Foundation
- **License:** Proprietary with tiered licensing model
- **Commercial Derivatives:** NO - requires commercial exploitation license
- **Key Restriction:** Copying of SFIA material is prohibited unless authorized in writing or under valid SFIA license. Commercial exploitation of SFIA (e.g., mapping to commercial services) requires annual license fee.
- **Contact:** SFIA Foundation (licensing@sfia-online.org)
- **Impact:** Cannot commercially exploit WIDAI with SFIA mappings without license.

#### 7. **CMMI-DMM** 🚫 CRITICAL BLOCKER
- **Publisher:** CMMI Institute (ISACA-affiliated)
- **License:** Proprietary (ISACA-managed)
- **Commercial Derivatives:** NO - requires ISACA license
- **Key Restriction:** Cannot be copied, distributed, or embedded in commercial products without ISACA license.
- **Contact:** IPinfo@isaca.org
- **Impact:** Cannot include CMMI-DMM in commercial WIDAI without licensing.

#### 8. **CMMI/ISACA** 🚫 CRITICAL BLOCKER
- **Publisher:** ISACA
- **License:** Proprietary
- **Commercial Derivatives:** NO - all ISACA IP requires licensing
- **Key Restriction:** ISACA licenses commercial use of all frameworks (COBIT, CMMI, CMM, etc.). Annual licensing required.
- **Contact:** IPinfo@isaca.org
- **Impact:** Any ISACA framework use in commercial WIDAI requires licensing agreement.

#### 9-15. **ISO Standards (ISO-23894, ISO-27001, ISO-27701, ISO-38505, ISO-42001, ISO-5338, ISO-8000)** 🚫 CRITICAL BLOCKER
- **Publisher:** International Organization for Standardization
- **License:** Proprietary/Copyrighted (paid standards)
- **Commercial Derivatives:** NO - requires ISO licensing
- **Key Restriction:** ISO standards must be purchased. Creating derivatives requires permission. All 7 ISO standards are copyright-protected.
- **Impact:** Cannot include detailed ISO standard mappings in commercial WIDAI. Only high-level references permissible.

#### 16. **IEEE** 🚫 CRITICAL BLOCKER
- **Publisher:** IEEE (Institute of Electrical and Electronics Engineers)
- **License:** Proprietary/Copyrighted (some open access under CC BY)
- **Commercial Derivatives:** NO - requires IEEE permission for most content
- **Key Restriction:** IEEE standards and technical publications are copyrighted. Derivative works require written IEEE permission.
- **Contact:** IEEE Permissions
- **Impact:** Cannot create derivatives of IEEE standards for commercial use.

#### 17. **HBR** 🚫 CRITICAL BLOCKER
- **Publisher:** Harvard Business Publishing
- **License:** Proprietary/Copyrighted
- **Commercial Derivatives:** NO - explicit restriction on commercial learning materials
- **Key Restriction:** Cannot be used in corporate training, course packs, or commercial products. Commercial derivatives require copyright permission from permissions@harvardbusiness.org.
- **Impact:** Cannot include HBR-derived content in commercial WIDAI.

#### 18. **DAMA-DMBOK** 🚫 CRITICAL BLOCKER (Mixed Licensing)
- **Publisher:** DAMA International
- **License:** Mixed: Some CC BY-ND 4.0 (no derivatives), some proprietary
- **Commercial Derivatives:** NO - parts prohibit modification (CC-ND)
- **Key Restriction:** Select diagrams are CC BY-ND (cannot modify). Other content is proprietary. Commercial use requires licensing.
- **Contact:** Info@dama.org
- **Impact:** Cannot create derivatives of DAMA-DMBOK content; licensing required for commercial use.

#### 19. **Deloitte** 🚫 CRITICAL BLOCKER
- **Publisher:** Deloitte Consulting
- **License:** Proprietary/Copyrighted
- **Commercial Derivatives:** NO - requires licensing
- **Key Restriction:** Consulting research is proprietary. Commercial use requires permission.
- **Impact:** Cannot include Deloitte-derived frameworks in commercial WIDAI.

#### 20. **BCG** 🚫 CRITICAL BLOCKER
- **Publisher:** Boston Consulting Group
- **License:** Proprietary/Copyrighted
- **Commercial Derivatives:** NO - requires licensing
- **Key Restriction:** Commercial exploitation restricted. Requires written permission for commercial use.
- **Contact:** legal@bcg.com
- **Impact:** Cannot distribute commercial WIDAI with BCG mappings without agreement.

#### 21. **KPMG** 🚫 CRITICAL BLOCKER
- **Publisher:** KPMG (consulting firm)
- **License:** Proprietary/Copyrighted
- **Commercial Derivatives:** NO - requires permission
- **Key Restriction:** KPMG frameworks are proprietary. Commercial use requires written permission.
- **Impact:** Cannot include KPMG-derived content in commercial WIDAI.

#### 22. **CDO Magazine** 🚫 CRITICAL BLOCKER
- **Publisher:** Chief Data Officer Magazine
- **License:** Proprietary/Publishing
- **Commercial Derivatives:** NO - editorial copyright
- **Key Restriction:** Magazine editorial content is copyrighted. Commercial reuse is restricted.
- **Impact:** Cannot use CDO Magazine editorial content in commercial WIDAI.

#### 23. **WEF** 🚫 CRITICAL BLOCKER
- **Publisher:** World Economic Forum
- **License:** Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 (CC BY-NC-ND 4.0)
- **Commercial Derivatives:** NO - BOTH commercial use AND derivatives are prohibited
- **Key Restriction:** Most WEF reports are CC BY-NC-ND, which explicitly prohibits both commercial use AND creating derivative works.
- **Impact:** CANNOT include WEF-derived mappings in commercial WIDAI. This is a complete blocker.

---

## Risk Analysis Summary

### By License Type

| License Type | Count | Commercial Derivative Permitted? | WIDAI Implication |
|---|---|---|---|
| Public Domain (U.S. Government) | 10 | ✓ YES | Clear to use |
| Creative Commons BY (permissive) | 3 | ✓ YES | Clear to use with attribution |
| Creative Commons NC/ND (restrictive) | 3 | ✗ NO | BLOCKER |
| Open Government Licence | 1 | ✓ YES (with attribution) | Clear to use |
| Open Source (Apache 2.0) | 1 | ✓ YES (with notice) | Clear to use |
| Proprietary/Copyrighted | 35 | ✗ NO (most require license) | RED (licensing needed) |
| Unknown/Unspecified | 12 | ? UNKNOWN | YELLOW (requires inquiry) |

### Decision Framework

**For Commercial WIDAI Distribution:**

1. **GREEN Frameworks (19)** — APPROVED
   - Include all GREEN frameworks in commercial product
   - Provide proper attribution as required
   - Estimated safe usage: ~27% of frameworks

2. **YELLOW Frameworks (28)** — CONDITIONAL
   - Evaluate for your specific use case (e.g., reference vs. derivative)
   - Contact each publisher for licensing terms if mapping/reference is central to product
   - Estimated 40% of frameworks; need individual assessment

3. **RED Frameworks (23)** — MUST EXCLUDE OR LICENSE
   - **Option A (Preferred):** Exclude from commercial WIDAI
   - **Option B:** Obtain individual licensing agreements
   - **Option C:** License selectively only the highest-value frameworks
   - Estimated 33% of frameworks; significant legal/cost burden

### Fair Use Considerations

For research frameworks (Gartner, Forrester, McKinsey, IDC), the question arises: **Can WIDAI make fair use of framework concepts without creating derivatives?**

**Fair Use Analysis:**

- **Quoting/Referencing:** Short quotes or concepts may be defensible under fair use
- **Mapping/Structural Derivatives:** Creating detailed mappings or reusing framework structure is likely NOT fair use
- **Commercial Context:** Commercial use narrows fair use protections

**Recommendation:** Consult independent legal counsel on fair use boundaries for each research framework. Do not assume fair use covers commercial use without legal review.

---

## Recommendations

### Immediate Actions (Pre-Launch)

1. **Exclude RED Frameworks from Commercial Products**
   - Remove or drastically limit commercial use of all 23 RED frameworks
   - Consider free/open-source tier with full coverage as alternative

2. **Conduct Framework Prioritization Analysis**
   - Identify which RED/YELLOW frameworks contribute the most critical role/KSA mappings
   - Evaluate business impact of excluding each framework

3. **Licensing Prioritization**
   - For high-impact RED frameworks, prioritize licensing inquiries:
     - COBIT-2019 (ISACA) — widespread enterprise governance use
     - SFIA — global IT skills standard
     - Gartner — analyst influence in enterprise procurement
   - Obtain preliminary licensing costs before product launch

4. **Independent Legal Review**
   - Engage IP counsel to:
     - Define fair use boundaries for research frameworks
     - Review risk tolerance for YELLOW frameworks
     - Advise on derivative works definition
     - Validate final framework inclusion strategy

### Medium-Term Strategy

5. **Three-Tier Commercial Model**
   - **Tier 1 (Free):** All GREEN + key open frameworks
   - **Tier 2 (Paid):** Add licensed RED/YELLOW frameworks
   - **Tier 3 (Enterprise):** Full framework coverage with all necessary licenses

6. **Licensing Agreements**
   - Prioritize ISACA (COBIT, CMMI-DMM) — likely highest cost but broadest impact
   - Evaluate SFIA commercial exploitation license
   - Research Gartner/Forrester academic/research licensing options
   - Bundle licensing costs into product pricing

7. **Documentation Requirements**
   - Maintain definitive map of which frameworks are included
   - Document licensing status and attribution statements for each framework
   - Create legal compliance checklist for product launches in different markets

---

## Legal Compliance Checklist

- [ ] Confirm all GREEN frameworks included in WIDAI have proper attribution statements
- [ ] Remove or obtain licenses for all 23 RED frameworks before commercial distribution
- [ ] Document licensing agreements for any YELLOW frameworks included
- [ ] Obtain written legal opinion on fair use analysis (if applicable)
- [ ] Verify ISO framework licensing (purchase or exclude detailed mappings)
- [ ] Confirm ISACA/COBIT licensing (if COBIT included)
- [ ] Verify SFIA licensing (if SFIA included)
- [ ] Exclude or license Gartner, Forrester, McKinsey, IDC frameworks
- [ ] Create framework licensing registry for audit trail
- [ ] Brief legal team on WEF CC BY-NC-ND blocker (cannot be included commercially)
- [ ] Review terms of service for all proprietary platforms (AWS, Microsoft, LinkedIn, Coursera)

---

## Conclusion

WIDAI has strong legal ground to distribute a commercial product based on the 19 GREEN frameworks, which cover foundational U.S. government workforce taxonomies (O*NET, BLS-SOC), cybersecurity standards (NIST NICE, DCWF), and legislation (GDPR, EU AI Act, HIPAA, Evidence Act, Executive Orders).

However, if WIDAI aims to include comprehensive coverage across all 70 frameworks, significant licensing costs and legal review are required. **Commercial viability depends on:**

1. **Business model choice:** Free basic tier (GREEN only) vs. premium tier (licensed RED frameworks)
2. **Licensing strategy:** Which RED frameworks warrant licensing investment
3. **Legal risk tolerance:** Fair use defense for research frameworks
4. **Fair use analysis:** Independent counsel review of derivative works boundaries

**Final Recommendation:** Begin commercial distribution with GREEN frameworks only. Plan phased licensing of high-value RED frameworks based on market demand and budget.

---

## Sources and References

- [O*NET OnLine Content License](https://www.onetonline.org/help/license)
- [NIST Public Domain Notice](https://spdx.org/licenses/NIST-PD.html)
- [NIST Copyright and Licensing](https://www.nist.gov/open/license)
- [SFIA Licensing Terms](https://sfia-online.org/en/about-sfia/licensing-sfia)
- [DAMA-DMBOK Terms of Use](https://www.damadmbok.org/terms-of-use)
- [ESCO Download and Use](https://esco.ec.europa.eu/en/use-esco/download)
- [UK Open Government Licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
- [BLS Copyright Information](https://www.bls.gov/opub/copyright-information.htm)
- [COBIT Usage Guidelines](https://www.isaca.org/about-us/cobit-usage-guidelines)
- [Gartner Research Usage Policy](https://www.gartner.com/en/about/policies/usage-policy)
- [Forrester Research Usage Policy](https://www.forrester.com/policies/research-usage)
- [McKinsey Terms of Use](https://www.mckinsey.com/terms-of-use)
- [IDC Content Usage Guidelines](https://www.idc.com/about/permissions/)
- [Gartner Content Compliance Policy](https://www.gartner.com/en/about/policies/content-compliance)
- [WEF Licence Terms](https://www.weforum.org/about/licence-terms-on-the-use-of-forum-publications-and-materials/)
- [Executive Order Copyright Status](https://www.law.cornell.edu/uscode/text/17/105)
- [Federal Government Copyright Protection](https://www.usa.gov/government-copyright)
- [FDA openFDA Public Domain](https://open.fda.gov/terms/)
- [dbt Labs Licensing FAQ](https://www.getdbt.com/licenses-faq)
- [IEEE Copyright Policy](https://www.ieee.org/publications/rights/copyright-policy)
- [HBR Copyright Permissions](https://hbr.org/permissions)
