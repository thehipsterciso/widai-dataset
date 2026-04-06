# WIDAI Pilot Role-KSA Provenance — Summary

**Version:** WIDAI v0.5.7 (KSA files at v0.8.0)  
**Pilot date:** 2026-04-06  
**Methodology:** 4-step quality-first provenance (STRM evidence → gap analysis → adversarial pass → provenance schema)

---

## Category Corrections

Three of five user-supplied category labels did not match the WIDAI dataset:

| Role | User-Supplied | Actual WIDAI Category |
|---|---|---|
| Chief Data Officer | LDR | GOV (Governance, Strategy, and Executive Leadership) |
| ML Research Scientist | DSM | DEV (Data Science, ML, and AI Development) — matched as WIDAI-DEV-0058 "AI Research Scientist" (key_variants: ML Researcher, Applied Researcher) |
| Data Privacy Officer | REG | GOV (Governance, Strategy, and Executive Leadership) — matched as WIDAI-GOV-0016 "Data Protection Officer" |

This is a WIDAI dataset documentation issue. REG contains EU AI Act implementation roles. GOV contains CDO and privacy officer roles. LDR contains VP/Director-level roles; CDO is in GOV.

---

## Results Summary

| Role | Role ID | STRM Coverage | Included KSAs | Excluded (documented) | Avg STRM Strength |
|---|---|---|---|---|---|
| Chief Data Officer | WIDAI-GOV-0002 | - | 20 | 4 | N/A (web only) |
| Data Engineer | WIDAI-ENG-0028 | Yes | 23 | 6 | 6.76 |
| AI Governance Manager | WIDAI-GOV-0008 | Yes | 18 | 5 | 8.11 |
| AI Research Scientist | WIDAI-DEV-0058 | - | 19 | 5 | N/A (web only) |
| Data Privacy Officer | WIDAI-GOV-0016 | Yes | 16 | 5 | 7.92 |

---

## STRM Framework Coverage by Role

**Chief Data Officer (WIDAI-GOV-0002):**  
No STRM framework anchors. Sources (Evidence Act, DAMA-DMBOK, Gartner, Deloitte) are not represented in any WIDAI STRM. Web research is the primary signal. Confidence tier: medium across all records.

**Data Engineer (WIDAI-ENG-0028):**  
DCWF WR624 (55 elements → 60 KSAs scored ≥3; 12 at strength=8, 48 at strength=5) + DDaT Data Engineer (11 skill FDEs → 30 KSAs scored ≥3; 4 at strength=8, 26 at strength=5). Natural threshold set at strength=8 for direct includes, strength=5 with web confirmation for conditional includes. O*NET STRM-001 does not use occupation code format (uses content model element IDs — not queryable by 15-1243.00).

**AI Governance Manager (WIDAI-GOV-0008):**  
NIST AI RMF (70/70 FDE IDs → 60 unique KSAs scored ≥3; 1 at strength=10, 53 at strength=8, 6 at strength=5). Strongest STRM coverage in the pilot. Natural threshold clear at strength=8. Adversarial pass removed 5 ML practitioner KSAs that appeared due to semantic overlap in AI system documentation language.

**AI Research Scientist (WIDAI-DEV-0058):**  
No STRM (O*NET STRM-001 uses content model IDs, not occupation codes — cannot filter to 15-1221.00). Web research is primary signal. This is an architectural gap in WIDAI's O*NET STRM design that should be resolved by adding occupation-element crosswalk data.

**Data Privacy Officer (WIDAI-GOV-0016):**  
EU AI Act (62/62 FDE IDs → 50 KSAs scored ≥3; 1 at strength=10, 30 at strength=8, 19 at strength=5). Important caveat: EU AI Act is not a primary DPO source — GDPR Articles 37-39 and ISO-27701 are. The EU AI Act STRM provides a useful secondary signal (AI systems that process personal data fall under both regimes), but many top-scoring EU AI Act KSAs are ML practitioner competencies that fail the DPO seniority test. Web research (IAPP, GDPR sources) served as primary signal for GDPR-specific KSA inclusions.

---

## Adversarial Findings

**Arbitrary-target warnings: None.** No role shows evidence of KSA count inflation to hit a round number. Inclusion decisions were driven by evidence thresholds and adversarial tests.

**Seniority failures caught and excluded:**
- DG-K-001, DG-K-002, LS-S-008, LS-S-010 excluded from Data Engineer (too strategic — C-suite governance framing)
- AI-S-010, AI-S-006, AI-S-008, AI-T-001 excluded from AI Governance Manager (ML practitioner skills, not governance)
- DG-K-001, LS-K-010, RM-S-008 excluded from AI Research Scientist (organizational strategy/governance, not researcher scope)
- AI-S-010, AI-T-001, AI-S-006 excluded from Data Privacy Officer (ML engineering skills, not privacy officer scope)

**Surprises:**
1. DCWF WR624 is data infrastructure-heavy (strong TF/networking KSAs) but data engineering-specific KSAs appear at strength=5 rather than strength=8. The strength=8 mappings in WR624 reflect general IT professional competencies that happen to appear in the Data Operations Specialist role. This limits DCWF as a discriminating signal for Data Engineer.
2. The NIST AI RMF has the cleanest, most directly applicable STRM coverage — all 70 FDE outcomes are relevant to AI Governance Manager. This role has the highest average STRM strength (8.0 for included KSAs).
3. The EU AI Act STRM over-generates ML practitioner KSAs for the Data Privacy Officer because the Act's technical provisions (conformity assessment, logging, transparency) use language that semantically overlaps with engineering skills. 5 of 50 EU AI Act candidates failed the DPO adversarial test.
4. CDO and AI Research Scientist have zero STRM coverage — this is an infrastructure gap, not a KSA gap. Both roles are well-defined in the WIDAI catalog but their source documents (Evidence Act, DAMA, Gartner for CDO; Stanford HAI for AI Research Scientist) are not in any STRM framework.

---

## Recommendations for WIDAI Roadmap

1. **Add CDO framework anchor.** DAMA CDMP competency framework or the Federal Data Strategy (Evidence Act) should be incorporated as a STRM. The CDO role currently has no computational evidence path.
2. **Add O*NET occupation-element crosswalk.** The O*NET STRM uses content model IDs. Adding occupation-element rating data (from O*NET database) would enable occupation-specific KSA scoring for roles like Data Engineer (15-1243.00) and AI Research Scientist (15-1221.00).
3. **Add ISO-27701 and GDPR competency STRM.** The Data Privacy Officer role is sourced entirely from GDPR/ISO-27701/IAPP — none of these are in WIDAI STRM. Adding STRM-007-ISO-27701 would give the DPO role computational evidence.
4. **Review EU AI Act STRM for DPO over-generation.** Consider adding a post-processing filter for ML practitioner relationship types when mapping to DPO-profile roles.
5. **Fix category labels in the pilot documentation.** The user-supplied category labels for CDO (LDR), ML Research Scientist (DSM), and Data Privacy Officer (REG) should be corrected to GOV, DEV, and GOV respectively in any downstream system.
