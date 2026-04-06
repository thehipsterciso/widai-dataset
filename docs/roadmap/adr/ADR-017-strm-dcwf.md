# ADR-017: STRM — DoD Cyber Workforce Framework (DCWF) v5.1

**Status:** Accepted
**Date:** 2026-04-01
**Author:** Thomas Jones / The Hipster CISO
**STRM ID:** STRM-003-DCWF
**Priority:** 3 (Tier 1 — Foundational)
**Governed by:** ADR-014 (STRM-Based KSA Enrichment Methodology)

## Framework Selection Rationale

DCWF is the third framework in the STRM execution sequence for three reasons:

1. **Dedicated Data/AI workforce element.** DCWF v5.1 is the only Tier 1 framework that explicitly defines a Data/AI workforce category — 11 work roles spanning data officers, data architects, data engineers, data scientists, AI/ML specialists, and AI innovation leads. This creates direct overlap with WIDAI's scope that NICE (pure cybersecurity) and O*NET (general occupations) do not have.
2. **Federal workforce authority for data/AI.** DCWF governs the DoD's 750,000+ cyber workforce positions. Its KSAT definitions will be cited in federal data/AI workforce requirements, hiring standards, and training programs. WIDAI must demonstrate formal alignment with the framework most likely to define federal data/AI competency expectations.
3. **NICE lineage with broader scope.** DCWF derives from the NICE Framework but extends it across seven workforce elements (IT, Cybersecurity, Cyber Effects, Intelligence, Enablers, Software Engineering, Data/AI). This provides a cross-domain validation opportunity — how WIDAI's KSAs perform against a framework that spans both cybersecurity and data/AI rather than one domain exclusively.

## Use Case Summary

**Target audience:** WIDAI framework developers, DoD workforce planners, PE operating partners evaluating organizations with federal/defense data and AI programs, and CDAIOs building workforce competency programs aligned with DoD requirements.

**Rationale type:** Semantic. DCWF and WIDAI share significant vocabulary overlap — both define data, AI, governance, and management competencies. Semantic rationale evaluates whether concepts describe the same or overlapping competencies, which is the appropriate mode given the substantial domain intersection.

**Scope:** All 2,945 DCWF KSAT elements evaluated (1,277 tasks, 1,668 KSAs). No exclusions — DCWF spans cybersecurity, IT, intelligence, cyber effects, enablers, software engineering, and Data/AI. Elements outside WIDAI scope produce "No relationship" results documenting the boundary.

**Structural note:** DCWF uses KSAT building blocks derived from NICE Framework. The Work Role Tool v5.1 combines K, S, and A into a single "KSA" type with Tasks separate. WIDAI uses KSA with distinct type labels. This structural difference is cosmetic — the mapping evaluates semantic content regardless of element type labels.

## Scoring Methodology

Identical to STRM-001-ONET and STRM-002-NICE. See ADR-015 Section "Scoring Methodology" for full documentation of the multi-method computational scoring pipeline. Key parameters:

| Attribute | Value |
|-----------|-------|
| Primary method | Cross-Encoder STS (`cross-encoder/stsb-roberta-base`) |
| Secondary methods | BERTScore (`roberta-large`), NLI (`cross-encoder/nli-deberta-v3-base`), Bi-Encoder Cosine (`all-MiniLM-L6-v2`), Jaccard Token |
| Score mapping | Raw STS (0–1) × 10, rounded to nearest integer |
| Pipeline script | `strm/dcwf/strm_scoring_pipeline.py` |

### Candidate Identification

Due to the volume of DCWF elements (2,945 × 497 WIDAI KSAs = 1.46M potential pairs), bi-encoder embeddings (`all-MiniLM-L6-v2`) were used to identify the most semantically relevant WIDAI KSA candidate for each DCWF element. This is a preprocessing step for pairing — not a scoring shortcut. Candidate data stored in `sources/dcwf/dcwf_ksat_candidates.json`.

Once pairs were established, every mapped pair was scored through the identical multi-method pipeline used in STRM-001-ONET and STRM-002-NICE: Cross-Encoder STS primary, plus BERTScore, NLI, Bi-Encoder Cosine, and Jaccard Token Overlap as secondary methods. Same models, same scoring logic, same rigor. Each rationale file contains content-specific significance referencing actual shared vocabulary, unique terms per side, and concept-level analysis.

## Summary Statistics

| Metric | Value |
|--------|-------|
| Total FDEs in scope | 2,945 |
| Intersects with | 1,836 (62.3%) |
| Superset of | 990 (33.6%) |
| Equal | 109 (3.7%) |
| No relationship | 10 (0.3%) |
| Subset of | 0 (0.0%) |
| Computed mean strength (scored only) | 4.79 / 10 |
| Gap signals | 4 thematic clusters |

### By Relationship Type

| Type | Count | Mean Strength (STS) | Range |
|------|-------|---------------------|-------|
| Equal | 109 | 6.17 | 5 – 8 |
| Superset of | 990 | 5.51 | 2 – 8 |
| Intersects with | 1,836 | 4.32 | 1 – 7 |
| No relationship | 10 | 0 | N/A |

### By DCWF Element Type

| Type | Total | Scored | No Rel | Mean Strength (scored) |
|------|-------|--------|--------|----------------------|
| Task | 1,277 | 1,272 | 5 | 4.69 |
| KSA | 1,668 | 1,663 | 5 | 4.86 |

### By WIDAI Domain (scored mappings)

| Domain | Count | Description |
|--------|-------|-------------|
| TF | 463 | Technical Foundations — highest, confirming technical overlap |
| SP | 443 | Security & Privacy — second, confirming security/data boundary |
| OP | 282 | Operations & Enablement |
| AI | 272 | AI/ML Foundations |
| LS | 245 | Leadership & Strategy |
| DA | 232 | Data Architecture & Infrastructure |
| RC | 208 | Regulatory & Compliance |
| RM | 200 | Risk Management |
| DQ | 198 | Data Quality & Management |
| AB | 186 | Analytics & BI |
| DG | 130 | Data Governance & Policy |
| AG | 76 | AI Governance & Ethics — lowest, reflecting DCWF's limited AI governance coverage |

## Key Findings

### 1. DCWF Has the Highest WIDAI Match Rate of Any Framework

99.7% of DCWF elements have documented relationships with WIDAI KSAs — compared to 81.7% for O*NET and 80.1% for NICE. Only 10 elements (0.3%) classified as "No relationship," all unambiguous tactical military/forensic operations (network hardware installation, disk forensics, nodal analysis, geolocation operations, target deconfliction, forensic memory/disk abilities).

This result confirms that DCWF's dedicated Data/AI workforce element creates substantial direct overlap with WIDAI. The 15 WIDAI roles that map to DCWF work roles (Data Steward, Data Officer, Data Architect, Data Engineer, Database Administrator, Data Scientist, AI/ML Specialist, Knowledge Manager, Data Analyst, AI Risk and Ethics Specialist, AI Test and Evaluation Specialist, Data and AI Program Manager, Data and AI Adoption Specialist, Data Operations Specialist, AI Innovation Lead) represent significant coverage.

### 2. Strength Scores Confirm Cross-Framework Methodology Consistency

The strength ordering (Equal 6.17 > Superset 5.51 > Intersects 4.32) replicates the pattern observed in all three STRMs. The mean scored strength (4.79) sits between STRM-001 (4.18, general-purpose O*NET) and STRM-002 (5.12, cybersecurity-specific NICE). This intermediate position reflects DCWF's mixed composition — substantial data/AI-relevant elements scoring higher, alongside cybersecurity/intelligence/military elements creating vocabulary divergence. The consistency across three independent framework STRMs confirms the multi-method scoring pipeline produces ordinally valid and analytically coherent results.

### 3. The "No Relationship" Set Is Analytically Clean

Unlike STRM-002-NICE (428 no-relationship elements, 4 borderline cases requiring review), DCWF's 10 no-relationship elements are unambiguous. Zero borderline cases. This reflects DCWF's broader workforce scope — elements that are truly outside data/AI scope are narrow tactical operations, not broad professional competencies that might have partial overlap.

### 4. Gap Signals Are Corroborative, Not Novel

Three of four DCWF gap signals corroborate gaps identified in prior STRMs:

| DCWF Gap | Corroborates | Theme |
|----------|-------------|-------|
| DCWF-GAP-001 | NICE-GAP-002 | Data/AI incident response and recovery |
| DCWF-GAP-002 | ONET-GAP-004 (partial) | Workforce planning and organizational design |
| DCWF-GAP-003 | NICE-GAP-005 | Supply chain integrity for data/AI |
| DCWF-GAP-004 | — (new) | Test and evaluation methodology for data/AI |

The corroborative pattern is significant. When multiple independent frameworks surface the same gap from different perspectives, the case for WIDAI enrichment strengthens. DCWF-GAP-001 (incident response) is now corroborated by two frameworks and should be treated as high priority during Phase 1D Synthesis.

### 5. DCWF's Data/AI Workforce Element Validates WIDAI's Core Domain Model

The 11 DCWF Data/AI work roles map to 15 WIDAI roles across governance, engineering, development, operations, analytics, risk, and leadership categories. The KSAT elements associated with these roles consistently score in the 5–8 strength range against WIDAI KSAs. This validates that WIDAI's shared-pool KSA architecture captures the competencies that the US federal government defines for its data/AI workforce — a significant institutional credibility signal.

### 6. Technical Foundations and Security/Privacy Dominate Domain Coverage

TF (463) and SP (443) together account for 31% of all scored mappings. This confirms the structural reality: federal cyber workforce competencies concentrate in technical foundations (systems, networks, infrastructure) and security/privacy (access control, encryption, threat assessment). WIDAI's TF and SP domains provide the bridge vocabulary between cybersecurity and data/AI workforce competencies.

## Anomalies

None identified. The mapping results are consistent with the analytical expectations documented in the use case. The 99.7% match rate, while high, is explained by DCWF's dedicated Data/AI workforce element — the first framework in the STRM sequence with explicit data/AI scope.

## QA/QC Result

**PASS.** All 2,945 FDEs evaluated with documented rationale. Relationship types and strength scores are computationally derived with full audit trails. 7/7 validation checks pass. See `strm/dcwf/qa_qc_report.json` for full QA/QC details.

## Deliverables

| # | Deliverable | Location |
|---|-------------|----------|
| 1 | DCWF Work Role Tool v5.1 (source) | `sources/dcwf/DCWF_Work_Role_Tool_v5.1.xlsx` |
| 1a | Extracted structured data | `sources/dcwf/dcwf_elements.json` |
| 1b | Source citation | `sources/dcwf/dcwf_citation.json` |
| 2 | Use case document | `strm/dcwf/use_case.json` |
| 3 | STRM mapping data | `strm/dcwf/strm_mapping.json` |
| 4 | Per-FDE rationale files (2,945) | `strm/dcwf/rationale/{fde-id}.json` |
| 5 | Scoring pipeline | `strm/dcwf/strm_scoring_pipeline.py` |
| 6 | Scoring summary | `strm/dcwf/scoring_summary.json` |
| 7 | Bi-encoder candidate screening | `sources/dcwf/dcwf_ksat_candidates.json` |
| 8 | Gap issue register | `strm/issues/STRM-003-DCWF-gaps.json` |
| 9 | This ADR | `docs/roadmap/adr/ADR-017-strm-dcwf.md` |
| 10 | QA/QC report | `strm/dcwf/qa_qc_report.json` |

## References

- DoD Cyber Workforce Framework (DCWF) Work Role Tool v5.1, https://www.cyber.mil/dod-workforce-innovation-directorate/dod-cyber-workforce-framework
- DoD CIO Cyber Workforce Framework, https://dodcio.defense.gov/Cyber-Workforce/DCWF/
- NIST IR 8477: Mapping Relationships Between Documentary Standards, Regulations, Frameworks, and Guidelines
- NIST IR 8278Ar1: National OLIR Program — Submission Guidance for OLIR Developers
- Reimers, N. & Gurevych, I. (2019). Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks. EMNLP.
- Zhang, T. et al. (2020). BERTScore: Evaluating Text Generation with BERT. ICLR.
- ADR-014: STRM-Based KSA Enrichment Methodology
- ADR-015: STRM — O*NET Database 30.2
- ADR-016: STRM — NIST NICE Framework v2.1.0
- Phase 1B Framework Prioritization (`docs/roadmap/phase-1b-framework-prioritization.md`)
