# AI Skills — Phase 1D Synthesis Analysis

**Domain:** AI/ML Foundations (AI)
**Dimension:** Skills
**Date:** 2026-04-03
**Pre-synthesis count:** 30 (19 Phase 1A baseline + 11 post-STRM additions)
**Post-synthesis count:** 29

## Evidence Summary

- **Total mappings:** 22,682 across 6 frameworks
- **Phase 1A entries (S-001 to S-019):** All have STRM evidence (6/6 coverage)
- **Post-STRM entries (S-020 to S-030):** 0/6 coverage (added after STRM runs)

### High Watermark (unique FDE count at STS thresholds)

| Framework | >=0.45 | >=0.50 | >=0.55 | >=0.60 |
|-----------|--------|--------|--------|--------|
| O*NET 30.2 | 29 | 19 | 9 | 3 |
| NIST NICE v2.1.0 | 889 | 636 | 415 | 212 |
| DoD DCWF v5.1 | 1,446 | 984 | 533 | 240 |
| DDaT | 92 | 58 | 21 | 6 |
| EU AI Act | 59 | 53 | 41 | 23 |
| NIST AI RMF 1.0 | 69 | 66 | 51 | 31 |

### Strongest STRM Hits

| Entry | Strong | Max STS | Top framework evidence |
|-------|--------|---------|----------------------|
| AI-S-010 | 11 | 0.7674 | EUAIA-O-012 AI transparency design |
| AI-S-006 | 3 | 0.7483 | NICE S0631 data preprocessing, DCWF [7054] AI robustness testing |
| AI-S-011 | 1 | 0.7320 | DCWF [224] design modeling |
| AI-S-016 | 1 | 0.7036 | DCWF [5944] CI/CD tooling |

## Duplicate Identification (Phase 1A)

One group of near-duplicate entries identified within the Phase 1A baseline:

### Group 1: Production ML Code
- **S-003:** Writing production-quality Python code for data processing, feature engineering, model training, and evaluation
- **S-005:** Refactoring research-quality data science code into production-grade, tested, documented, and deployable ML systems
- **Action:** Merge → single entry covering both writing and refactoring ML code to production quality
- **Evidence:** S-003 (697 mappings, max 0.6480) + S-005 (780 mappings, max 0.6681)

**Net effect:** 19 Phase 1A entries − 1 merge = 18 distinct Phase 1A entries

## Post-STRM Entry Evaluation (S-020 to S-030)

| Entry | Concept | Framework evidence | Verdict |
|-------|---------|-------------------|---------|
| S-020 | AI transparency/explainability | EUAIA-O-012 (0.7674); AIRMF-MS-2.9 explanations | **KEEP** — distinct from S-010 (guardrails) |
| S-021 | AI risk assessment | EUAIA-O-002; AIRMF-MG-1.1-1.3; AIRMF-MS-2.6 | **KEEP** — distinct concept |
| S-022 | Fairness/bias evaluation | AIRMF-MS-2.11 fairness metrics; EUAIA-O-028 input data quality | **KEEP** — distinct concept |
| S-023 | Adversarial testing/red-teaming | DCWF [7054] (0.7381) robustness testing; EUAIA-O-054 resilience | **KEEP** — distinct from S-012 (NLP eval) |
| S-024 | Data preprocessing for ML | NICE S0631 (0.7149); DCWF [5924] train/evaluate | **KEEP** — distinct from S-002 (EDA) and S-013 (CV data) |
| S-025 | Regulatory-grade AI documentation | EUAIA-O-009, O-041; AIRMF-MS-2.1 | **KEEP** — distinct concept |
| S-026 | AI monitoring/observability | EUAIA-O-011; AIRMF-MS-2.4; AIRMF-MG-3.2 | **KEEP** — distinct from S-007 (retraining triggers) |
| S-027 | Feedback mechanisms for AI | AIRMF-GV-5.2; AIRMF-MG-2.4; AIRMF-MS-3.3 | **KEEP** — distinct concept |
| S-028 | Third-party AI assessment | AIRMF-MG-3.1; AIRMF-GV-6.1, 6.2 | **KEEP** — distinct supply chain skill |
| S-029 | End-to-end deployment orchestration | DCWF [5944], [7088], [5870] CI/CD + containers | **KEEP** — distinct from S-006 (API) and S-016 (CI/CD) |
| S-030 | AI literacy/training programs | EUAIA-C-001; AIRMF-GV-2.2 | **KEEP** — distinct organizational capability |

**Net effect:** 11 kept, 0 removed

## Final Count

18 (Phase 1A deduplicated) + 11 (validated post-STRM) = **29 entries**

## Entry Mapping: Current → Proposed

| Proposed | Source | Action |
|----------|--------|--------|
| AI-S-001 | S-001 | Preserve (ML problem formulation) |
| AI-S-002 | S-002 | Preserve (EDA) |
| AI-S-003 | S-003 + S-005 | Merge (production ML code) |
| AI-S-004 | S-004 | Preserve (stakeholder communication) |
| AI-S-005 | S-006 | Renumber (model serving APIs) |
| AI-S-006 | S-007 | Renumber (retraining pipelines) |
| AI-S-007 | S-008 | Renumber (prompt engineering) |
| AI-S-008 | S-009 | Renumber (RAG pipelines) |
| AI-S-009 | S-010 | Renumber (AI guardrails) |
| AI-S-010 | S-011 | Renumber (fine-tuning) |
| AI-S-011 | S-012 | Renumber (NLP evaluation) |
| AI-S-012 | S-013 | Renumber (CV data prep) |
| AI-S-013 | S-014 | Renumber (CV model training) |
| AI-S-014 | S-015 | Renumber (feature engineering) |
| AI-S-015 | S-016 | Renumber (CI/CD for ML) |
| AI-S-016 | S-017 | Renumber (infra troubleshooting) |
| AI-S-017 | S-018 | Renumber (use case feasibility) |
| AI-S-018 | S-019 | Renumber (PoC demos) |
| AI-S-019 | S-020 | Renumber (AI transparency/explainability) |
| AI-S-020 | S-021 | Renumber (AI risk assessment) |
| AI-S-021 | S-022 | Renumber (fairness/bias evaluation) |
| AI-S-022 | S-023 | Renumber (adversarial testing) |
| AI-S-023 | S-024 | Renumber (data preprocessing for ML) |
| AI-S-024 | S-025 | Renumber (regulatory documentation) |
| AI-S-025 | S-026 | Renumber (AI monitoring/observability) |
| AI-S-026 | S-027 | Renumber (feedback mechanisms) |
| AI-S-027 | S-028 | Renumber (third-party AI assessment) |
| AI-S-028 | S-029 | Renumber (deployment orchestration) |
| AI-S-029 | S-030 | Renumber (AI literacy/training) |
