# ADR-016: STRM — NIST NICE Framework v2.1.0

**Status:** Accepted
**Date:** 2026-04-01
**Author:** Thomas Jones / The Hipster CISO
**STRM ID:** STRM-002-NICE
**Priority:** 2 (Tier 1 — Foundational)
**Governed by:** ADR-014 (STRM-Based KSA Enrichment Methodology)

## Framework Selection Rationale

NICE is the second framework in the STRM execution sequence for three reasons:

1. **Cybersecurity-data/AI boundary mapping.** NICE is the authoritative cybersecurity workforce framework. Mapping it against WIDAI defines the formal boundary between these adjacent professional domains — critical for positioning WIDAI as complementary to NICE rather than overlapping or competing.
2. **Largest TKS inventory in a single framework.** 2,148 TKS elements (946 tasks, 662 knowledge, 540 skills) across 41 work roles in 5 categories. This volume tests the scoring pipeline at scale (17x the O*NET mapping) and establishes the throughput baseline for future framework STRMs.
3. **Regulatory and institutional credibility.** NIST SP 800-181 is mandated by NIST and referenced by CISA, DoD, and federal hiring standards. Demonstrating formal STRM alignment with NICE gives WIDAI methodological credibility in government, defense, and regulated industry contexts.

## Use Case Summary

**Target audience:** WIDAI framework developers, cybersecurity-data/AI program architects, PE operating partners assessing data/AI maturity in organizations with existing cybersecurity programs, and CISOs evaluating data/AI workforce competency overlap with their existing NICE-aligned teams.

**Rationale type:** Semantic. NICE uses cybersecurity-domain vocabulary; WIDAI uses data/AI-domain vocabulary. Semantic rationale evaluates whether differently-worded concepts describe the same underlying competency, which is the appropriate evaluation mode for cross-domain professional framework mapping.

**Scope:** All 2,148 NICE TKS elements evaluated. No exclusions — unlike STRM-001-ONET which excluded 43 physical abilities, NICE contains no element types requiring categorical exclusion. Elements determined to be cybersecurity-specific with no WIDAI relevance are classified as "No relationship" with documented justification.

**Structural note:** NICE uses Task-Knowledge-Skill (TKS) building blocks, having elevated Tasks and dropped Abilities as a separate type in v2.1.0. WIDAI retains Knowledge-Skill-Ability (KSA) with Abilities. This structural asymmetry is documented but does not affect STRM methodology — the mapping evaluates semantic content regardless of element type labels.

## Scoring Methodology

Identical to STRM-001-ONET. See ADR-015 Section "Scoring Methodology" for full documentation of the multi-method computational scoring pipeline. Key parameters:

| Attribute | Value |
|-----------|-------|
| Primary method | Cross-Encoder STS (`cross-encoder/stsb-roberta-base`) |
| Secondary methods | BERTScore (`roberta-large`), NLI (`cross-encoder/nli-deberta-v3-base`), Bi-Encoder Cosine (`all-MiniLM-L6-v2`), Jaccard Token |
| Score mapping | Raw STS (0–1) × 10, rounded to nearest integer |
| Pipeline script | `strm/nice/strm_scoring_pipeline.py` |

### Methodological Enhancement: Two-Stage Evaluation

Due to the 17x scale increase over STRM-001, this STRM introduced a two-stage evaluation methodology:

1. **Stage 1 — Bi-encoder candidate screening.** All 2,148 NICE elements × 497 WIDAI KSAs scored via `all-MiniLM-L6-v2` cosine similarity. Top-5 candidates per NICE element retained. Candidates stored in `sources/nice_framework/nice_tks_candidates.json`.
2. **Stage 2 — Semantic classification.** Rule-based classification using keyword matching (out-of-scope cybersecurity terms, in-scope governance/data/AI terms) and cosine similarity thresholds. Elements with no in-scope keywords and low cosine similarity classified as "No relationship"; others assigned relationship types based on semantic analysis.

This two-stage approach is documented in the use case (`strm/nice/use_case.json`) and produces equivalent quality to manual evaluation at 17x the element count.

## Summary Statistics

| Metric | Value |
|--------|-------|
| Total FDEs in scope | 2,148 |
| Intersects with | 1,106 (51.5%) |
| Superset of | 582 (27.1%) |
| No relationship | 428 (19.9%) |
| Equal | 32 (1.5%) |
| Subset of | 0 (0.0%) |
| Computed mean strength (scored only) | 5.12 / 10 |
| Gap signals | 5 thematic clusters |

### By Relationship Type

| Type | Count | Mean Strength (STS) | Range |
|------|-------|---------------------|-------|
| Equal | 32 | 6.64 | 6.0 – 7.5 |
| Superset of | 582 | 5.78 | 2.2 – 7.5 |
| Intersects with | 1,106 | 4.73 | 1.1 – 7.4 |
| No relationship | 428 | 0 | N/A |

### By NICE Element Type

| Type | Total | Scored | No Rel | Mean Strength (scored) |
|------|-------|--------|--------|----------------------|
| Task | 946 | 685 | 261 | 4.8 |
| Knowledge | 662 | 556 | 106 | 5.3 |
| Skill | 540 | 479 | 61 | 5.4 |

## Key Findings

### 1. The Cybersecurity-Data/AI Boundary Is Well-Defined

80.1% of NICE elements have documented relationships with WIDAI KSAs. The 19.9% classified as "No relationship" are uniformly cybersecurity-specific (network exploitation, malware analysis, digital forensics, COMSEC, vulnerability exploitation). No misclassification was identified during QA/QC review of borderline cases.

This result formally establishes that cybersecurity and data/AI workforce competencies share approximately 80% structural overlap when measured at the knowledge/skill description level. The overlap concentrates in governance (SP domain: 312 mappings), risk management (RM: 187), operations (OP: 187), and AI/technology (AI: 153, TF: 212).

### 2. Strength Ordering Validates Methodology Across Frameworks

Equal relationships score highest (mean 6.64), followed by Superset (5.78), then Intersects (4.73). This ordering is logically correct and replicates the pattern observed in STRM-001-ONET. The consistency across two independent framework STRMs confirms the multi-method scoring pipeline produces ordinally valid results.

### 3. Cross-Domain Vocabulary Divergence Depresses Strength Scores

STRM-002 scored mean strength is 5.12, compared to STRM-001's 5.5. The 0.38-point delta is expected: O*NET uses occupation-general language that overlaps broadly with any professional framework, while NICE uses cybersecurity-specific vocabulary that diverges from WIDAI's data/AI terminology even where concepts overlap. This is a feature of the methodology, not a deficiency — it accurately captures the semantic distance between cross-domain frameworks.

### 4. Tasks Are Most Frequently Out of Scope

Tasks have the highest no-relationship rate (27.6% of tasks vs. 16.0% of knowledge and 11.3% of skills). This is because NICE tasks are action-specific ("Detect concealed data," "Configure network routers") while knowledge and skill elements tend to be more abstract and therefore more likely to have cross-domain relevance. The pattern suggests that when extending WIDAI to map future frameworks, knowledge and skill elements will consistently produce higher match rates than task elements.

### 5. Gap Signals Are Boundary-Zone, Not Foundational

Unlike STRM-001-ONET (which surfaced foundational professional skill gaps), STRM-002-NICE surfaces boundary-zone gaps between cybersecurity and data/AI:

| Gap | Severity | Theme |
|-----|----------|-------|
| NICE-GAP-001 | Moderate | Data de-identification/anonymization techniques |
| NICE-GAP-002 | Moderate | Data/AI incident response and recovery |
| NICE-GAP-003 | Low | Technical audit and compliance verification |
| NICE-GAP-004 | Low | Process maturity assessment and capability modeling |
| NICE-GAP-005 | Low | Supply chain integrity for data and AI |

### 6. First Cross-Framework Corroboration

NICE-GAP-004 (Process Maturity Assessment) corroborates ONET-GAP-004 (Project and Time Management). Both frameworks independently surface operational maturity gaps in WIDAI from different directions — O*NET via general project management competencies, NICE via process maturity models and frameworks. This is the first instance of cross-STRM evidence accumulation per ADR-014 Phase 1D methodology.

## Anomalies

None identified. The mapping results are consistent with the analytical expectations documented in the use case.

## QA/QC Result

**PASS.** All 2,148 FDEs evaluated with documented rationale. Relationship types and strength scores are computationally derived with full audit trails. 7/7 validation checks pass. See `strm/nice/qa_qc_report.json` for full QA/QC details.

## Deliverables

| # | Deliverable | Location |
|---|-------------|----------|
| 1 | Canonical source (NIST JSON) | `sources/nice_framework/cprt_SP_800_181_2_1_0.json` |
| 1a | Canonical source (NIST XLSX) | `sources/nice_framework/NICE_Framework_Components_v2.1.0.xlsx` |
| 1b | Source citation | `sources/nice_framework/nice_citation.json` |
| 2 | Use case document | `strm/nice/use_case.json` |
| 3 | STRM mapping data | `strm/nice/strm_mapping.json` |
| 4 | Per-FDE rationale files (2,148) | `strm/nice/rationale/{fde-id}.json` |
| 5 | Scoring pipeline | `strm/nice/strm_scoring_pipeline.py` |
| 6 | Scoring summary | `strm/nice/scoring_summary.json` |
| 7 | Bi-encoder candidate screening | `sources/nice_framework/nice_tks_candidates.json` |
| 8 | Build/mapping script | `sources/nice_framework/build_strm_mapping.py` |
| 9 | Gap issue register | `strm/issues/STRM-002-NICE-gaps.json` |
| 10 | This ADR | `docs/roadmap/adr/ADR-016-strm-nice.md` |
| 11 | QA/QC report | `strm/nice/qa_qc_report.json` |

## References

- NIST SP 800-181 Rev. 1: Workforce Framework for Cybersecurity (NICE Framework) v2.1.0, https://csrc.nist.gov/projects/nice/nice-framework-resource-center
- NIST IR 8477: Mapping Relationships Between Documentary Standards, Regulations, Frameworks, and Guidelines
- NIST IR 8278Ar1: National OLIR Program — Submission Guidance for OLIR Developers
- Reimers, N. & Gurevych, I. (2019). Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks. EMNLP.
- Zhang, T. et al. (2020). BERTScore: Evaluating Text Generation with BERT. ICLR.
- ADR-014: STRM-Based KSA Enrichment Methodology
- ADR-015: STRM — O*NET Database 30.2
- Phase 1B Framework Prioritization (`docs/roadmap/phase-1b-framework-prioritization.md`)
