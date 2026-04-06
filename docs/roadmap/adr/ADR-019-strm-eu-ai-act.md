# ADR-019: STRM — EU AI Act (Regulation (EU) 2024/1689)

**Status:** Accepted
**Date:** 2026-04-01
**Author:** Thomas Jones / The Hipster CISO
**STRM ID:** STRM-005-EU-AI-ACT
**Priority:** 5 (Tier 2 — Regulatory)
**Governed by:** ADR-014 (STRM-Based KSA Enrichment Methodology)

## Framework Selection Rationale

The EU AI Act is the first Tier 2 framework and the first regulatory (non-workforce) source in the STRM sequence. It is prioritized as the Tier 2 lead for three reasons:

1. **First regulatory framework.** STRM-001 through STRM-004 mapped workforce competency frameworks (O\*NET, NICE, DCWF, DDaT). The EU AI Act introduces a fundamentally different element type: legal obligations that imply workforce competencies. This STRM validates that the methodology can bridge the gap between regulatory requirements and workforce competencies — a prerequisite for STRM-006 (NIST AI RMF), STRM-008 (FED SR 11-7), and STRM-009 (GDPR).

2. **Direct commercial relevance.** The EU AI Act imposes workforce obligations with defined enforcement dates (Art. 4/5: Feb 2025, GPAI: Aug 2025, High-risk: Aug 2026). Every PE portfolio company with EU market exposure needs to know which workforce competencies they require for compliance. This STRM directly enables WIDAI's PE assessment product to answer that question with evidence.

3. **Explicit competency requirements.** Unlike most regulations, the EU AI Act explicitly defines workforce competency requirements in several articles (Art. 4 AI literacy, Art. 9(8) relevant expertise, Art. 14(4) human oversight competence, Art. 26(6) deployer AI literacy). These provide directly mappable elements alongside the obligation-derived elements.

## Element Types

The EU AI Act contains two distinct element types that required careful methodological treatment:

### Competency Elements (8)

Articles that explicitly state workforce competency, training, or literacy requirements. These elements use language like "sufficient level of AI literacy" (Art. 4), "relevant expertise and training" (Art. 9(8)), and "sufficient ability and authority to oversee" (Art. 14(4)).

These are directly mappable to WIDAI KSAs — they express the same concept type (what a person must know or be able to do).

### Obligation Elements (54)

Legal obligations whose fulfillment requires identifiable workforce competencies. These elements use language like "shall establish a risk management system" (Art. 9(1)), "shall draw up technical documentation" (Art. 11(1)), and "shall implement a quality management system" (Art. 17(1)).

The obligation text itself is legal prose, not competency language. To score these against WIDAI KSAs, each element includes a `competency_implication` field — the workforce competency interpretation of the legal requirement. This is the scoring text.

### Dual Provenance

Every rationale file preserves both:
- `obligation_text` — the original regulatory language, faithful to the source
- `scoring_text` (= `competency_implication`) — the workforce competency interpretation used for scoring

This maintains full provenance. Any reviewer can trace from the scored match back to the actual regulatory text.

## Scoring Methodology

### Primary Method

Cross-Encoder STS (`cross-encoder/stsb-roberta-base`) — consistent with STRM-001 through STRM-004. Scores the `competency_implication` text against WIDAI KSA statements. Raw 0–1 mapped to 0–10 strength integer.

### Rationale Type: Functional

This is a deviation from STRM-001 through STRM-004, which used Semantic rationale.

**Justification:** The mapping direction is obligation→competency: what workforce capability is required to fulfill this regulatory requirement? Per NIST IR 8477 Section 4.3, this is a Functional question: "how similar are the results of executing the two concepts." Semantic rationale ("how similar are the meanings") is appropriate for competency↔competency mapping but does not capture the obligation→competency inference.

### Methodology Evolution: NLI Diagnostic

The pre-execution analysis (documented in the session working notes) recommended a dual-mode pipeline: STS as primary for competency elements, NLI entailment as primary for obligation elements. The reasoning was sound — obligation→competency mapping is fundamentally an inference question ("does having this KSA entail ability to fulfill this obligation?"), which NLI is designed to answer.

**Diagnostic finding:** NLI entailment scored near-zero for all element types:
- Obligation elements: mean=0.007, median=0.001, max=0.218
- Competency elements: mean=0.009, median=0.001, max=0.019

**Root cause:** NLI models trained on MNLI classify sentence pairs as entailment/neutral/contradiction based on strict logical implication. Two related competency statements — even very similar ones — are "neutral" in NLI terms because neither logically implies the other. "Knowledge of AI risk management system design" does not logically imply "Knowledge of risk management frameworks" even though they are clearly semantically related.

**Resolution:** The `competency_implication` field bridges the vocabulary gap between legal prose and competency language. Since both the scoring text and WIDAI KSAs are in competency language, STS appropriately measures semantic relatedness. Pipeline revised to STS-primary for all elements.

**Lesson documented:** The pre-execution analysis correctly identified the problem (vocabulary domain gap) but the solution was in the data architecture (competency_implication field), not the scoring method. NLI is retained as a secondary signal — its primary diagnostic value is in detecting contradiction (competency domain conflicts).

### Secondary Methods

| Method | Model | Role |
|--------|-------|------|
| BERTScore | `roberta-large` | Token-level semantic matching audit trail |
| NLI Cross-Encoder | `cross-encoder/nli-deberta-v3-base` | Contradiction detection, logical implication secondary |
| Bi-Encoder Cosine | `all-MiniLM-L6-v2` | Independent embedding similarity |
| Jaccard Token | N/A | Lexical baseline |

### Candidate Identification

Bi-encoder embeddings (`all-MiniLM-L6-v2`) used to identify top-5 WIDAI KSA candidates per element. 62 × 497 = 30,814 potential pairs evaluated. This is a preprocessing step for pairing; all scoring performed by the STRM scoring pipeline.

## Summary Statistics

| Metric | Value |
|--------|-------|
| Total elements | 62 (8 competency, 54 obligation) |
| Articles covered | 21 of 113 |
| Scored mappings | 62 |
| No relationship | 0 |
| Mean strength (scored) | 6.34 |
| Median strength (scored) | 6.35 |
| Strength range | 3.6–8.2 |
| Rationale files | 62 |

### Relationship Type Distribution

| Relationship | Count | % | Mean Strength | Range |
|-------------|-------|---|---------------|-------|
| Equal | 27 | 43.5% | 7.17 | 6.6–8.2 |
| Superset of | 31 | 50.0% | 5.88 | 5.0–6.5 |
| Intersects with | 4 | 6.5% | 4.30 | 3.6–4.7 |
| No relationship | 0 | 0.0% | — | — |

### By Element Type

| Element Type | Count | Mean Strength | Median | Std |
|-------------|-------|---------------|--------|-----|
| Competency | 8 | 6.31 | 6.45 | 0.74 |
| Obligation | 54 | 6.35 | 6.35 | 0.95 |

Competency and obligation elements score nearly identically, confirming the `competency_implication` field successfully bridges the vocabulary gap.

### Comparison to Prior STRMs

| STRM | Framework | Elements | Scored Mean | No Relationship % |
|------|-----------|----------|-------------|-------------------|
| 001 | O\*NET 30.2 | 2,076 | 4.18 | 0.3% |
| 002 | NICE v2.1.0 | 2,148 | 5.12 | 9.5% |
| 003 | DCWF v5.1 | 2,945 | 4.79 | 0.3% |
| 004 | DDaT | 189 | 4.72 | 0.0% |
| **005** | **EU AI Act** | **62** | **6.34** | **0.0%** |

STRM-005's higher mean (6.34) is expected and methodologically explained:
1. The `competency_implication` text was authored to describe workforce competencies — naturally closer to WIDAI KSA language than raw framework descriptions
2. The EU AI Act scope (62 elements from 21 articles) is focused specifically on data/AI governance — the core of WIDAI's domain
3. Prior STRMs included many elements outside WIDAI scope that produced low-strength or no-relationship results

## Key Findings

### 1. Zero Gap Signals

All 62 elements mapped to at least one WIDAI KSA with strength ≥ 4. The WIDAI KSA pool comprehensively covers the EU AI Act's workforce-relevant requirements. This is the expected outcome for a regulatory framework whose requirements were considered during Phase 1A enrichment.

### 2. Domain Coverage Pattern

WIDAI domains with strongest EU AI Act representation:
- **AG (AI Governance):** AI literacy, human oversight, transparency, documentation, quality management, conformity assessment
- **RC (Regulatory Compliance):** Provider/deployer obligations, corrective actions, conformity assessment
- **RM (Risk Management):** Risk management system, accuracy/robustness, adversarial testing
- **SP (Security and Privacy):** Data governance, record-keeping, registration, cybersecurity

### 3. Weakest Matches (Partial Coverage)

Four elements scored as "Intersects with" (strength 4), indicating partial rather than full coverage:
- **Art. 50(3)** — Deep fake disclosure obligations
- **Art. 50(4)** — Emotion recognition/biometric system disclosure
- **Art. 10(5)** — Training data bias examination
- **Art. 26(6)** — Deployer workforce AI literacy

These represent areas where the WIDAI pool has related but not fully aligned competencies.

### 4. Methodology Validation

The dual-provenance approach (obligation_text + competency_implication) successfully enables regulatory framework mapping within the STRM methodology. The Functional rationale type is appropriate and can be applied to subsequent regulatory STRMs (NIST AI RMF, SR 11-7, GDPR).

## Deliverables

| # | Deliverable | Location |
|---|-------------|----------|
| 1 | Canonical source citation | `sources/eu_ai_act/eu_ai_act_citation.json` |
| 2 | Element extraction | `sources/eu_ai_act/eu_ai_act_elements.json` |
| 3 | Bi-encoder candidates | `sources/eu_ai_act/eu_ai_act_candidates.json` |
| 4 | Use case document | `strm/eu_ai_act/use_case.json` |
| 5 | STRM mapping data | `strm/eu_ai_act/strm_mapping.json` |
| 6 | Per-FDE rationale files | `strm/eu_ai_act/rationale/` (62 files) |
| 7 | Scoring summary | `strm/eu_ai_act/scoring_summary.json` |
| 8 | Gap issue register | `strm/issues/STRM-005-EU-AI-ACT-gaps.json` |
| 9 | QA/QC report | `strm/eu_ai_act/qa_qc_report.json` |
| 10 | Scoring pipeline | `strm/eu_ai_act/strm_scoring_pipeline.py` |
| 11 | Candidate generation | `sources/eu_ai_act/generate_candidates.py` |
| 12 | This ADR | `docs/roadmap/adr/ADR-019-strm-eu-ai-act.md` |

## Implications for Subsequent STRMs

1. **Regulatory framework methodology established.** Dual-provenance (obligation_text + competency_implication), Functional rationale, and STS-primary scoring are validated for regulatory sources. Apply to STRM-006 (NIST AI RMF), STRM-008 (FED SR 11-7), STRM-009 (GDPR).

2. **NLI role clarified.** NLI is a contradiction-detection secondary signal, not a primary scoring method for competency text. This applies to all STRMs.

3. **Element extraction methodology.** Each regulatory obligation should be decomposed to discrete elements with clear competency implications. The competency_implication field is required for meaningful scoring.

## References

- Regulation (EU) 2024/1689 (Artificial Intelligence Act), Official Journal L 2024/1689: https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng
- NIST IR 8477: Mapping Relationships Between Documentary Standards, Regulations, Frameworks, and Guidelines (February 2024)
- ADR-014: STRM-Based KSA Enrichment Methodology
- ADR-015: STRM — O\*NET (scoring methodology reference)
- ADR-018: STRM — DDaT (prior STRM reference)
