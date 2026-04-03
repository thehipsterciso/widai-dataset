# AI Tasks — Phase 1D Synthesis Analysis

**Domain:** AI/ML Foundations (AI)
**Dimension:** Tasks
**Date:** 2026-04-03
**Pre-synthesis count:** 38 (21 Phase 1A baseline + 17 post-STRM additions)
**Post-synthesis count:** 36

## Evidence Summary

- **Total mappings:** 16,786 across 6 frameworks
- **Phase 1A entries (T-001 to T-021):** All have STRM evidence (6/6 coverage)
- **Post-STRM entries (T-022 to T-038):** 0/6 coverage (added after STRM runs)

### High Watermark (unique FDE count at STS thresholds)

| Framework | >=0.45 | >=0.50 | >=0.55 | >=0.60 |
|-----------|--------|--------|--------|--------|
| O*NET 30.2 | 31 | 13 | 10 | 2 |
| NIST NICE v2.1.0 | 638 | 408 | 214 | 71 |
| DoD DCWF v5.1 | 1,139 | 677 | 349 | 142 |
| DDaT | 94 | 66 | 27 | 11 |
| EU AI Act | 48 | 40 | 25 | 13 |
| NIST AI RMF 1.0 | 66 | 57 | 33 | 21 |

### Strongest STRM Hits

| Entry | Strong | Max STS | Top framework evidence |
|-------|--------|---------|----------------------|
| AI-T-007 | 4 | 0.7891 | DCWF [5889] AI use cases, best practices, failure modes |
| AI-T-020 | 2 | 0.7472 | EUAIA-O-041 GPAI technical documentation |
| AI-T-015 | 1 | 0.7527 | DCWF [5829] security configuration baselines |
| AI-T-004 | 1 | 0.7406 | AIRMF-MG-3.2 pre-trained model monitoring |
| AI-T-016 | 1 | 0.7169 | DDaT-SK-132 programming and build |
| AI-T-018 | 1 | 0.7108 | DCWF [5872] AI tools for org objectives |
| AI-T-021 | 1 | 0.7066 | DCWF [4360] troubleshoot hardware/software |
| AI-T-006 | 1 | 0.7034 | DCWF [515A] software testing/validation |
| AI-T-017 | 1 | 0.7026 | AIRMF-MG-3.2 pre-trained model monitoring |

## Duplicate Identification (Phase 1A)

Two groups of near-duplicate entries identified within the Phase 1A baseline:

### Group 1: ML Pipeline Building
- **T-005:** Build and maintain ML training pipelines (data ingestion, preprocessing, training, evaluation, model registration)
- **T-016:** Build and maintain automated ML pipelines (feature engineering through training, validation, deployment, monitoring; reproducibility, auditability)
- **Action:** Merge → single entry covering full ML pipeline lifecycle with quality attributes
- **Evidence:** T-005 (576 mappings, max 0.6664) + T-016 (814 mappings, max 0.7169)

### Group 2: Model Monitoring Implementation
- **T-004:** Implement model monitoring dashboards and alerting (degradation thresholds, drift detection, incident response)
- **T-017:** Implement model monitoring and observability systems (data drift, prediction drift, degradation, alerts, automated retraining)
- **Action:** Merge → single entry covering monitoring implementation including dashboards, observability, and automated response
- **Evidence:** T-004 (887 mappings, max 0.7406) + T-017 (1,669 mappings, max 0.7026)

Note: T-003 (conduct post-deployment monitoring) is preserved as the analytical monitoring task, distinct from the implementation merge of T-004 + T-017.

**Net effect:** 21 Phase 1A entries − 2 merges = 19 distinct Phase 1A entries

## Post-STRM Entry Evaluation (T-022 to T-038)

| Entry | Concept | Framework evidence | Verdict |
|-------|---------|-------------------|---------|
| T-022 | AI risk assessment | AIRMF-MS-2.6 (0.7413) safety evaluation; EUAIA-O-002 | **KEEP** — distinct from T-007 (quality/safety eval) |
| T-023 | Fairness/bias evaluation | AIRMF-MS-2.11 fairness metrics; EUAIA-O-028 | **KEEP** — distinct concept |
| T-024 | Adversarial testing/red-teaming | DCWF [7054] robustness testing; EUAIA-O-054 | **KEEP** — distinct from T-007 (general eval) |
| T-025 | Regulatory documentation | EUAIA-O-041 (0.7472) GPAI docs; EUAIA-O-009 | **KEEP** — distinct from T-002 (model docs) |
| T-026 | Training data governance | EUAIA-O-006; EUAIA-O-007 | **KEEP** — distinct concept |
| T-027 | Human oversight mechanisms | EUAIA-O-014; AIRMF-GV-3.2 | **KEEP** — distinct concept |
| T-028 | Use case feasibility assessment | AIRMF-MP-1.3; AIRMF-MP-3.1 | **KEEP** — distinct from T-019 (pipeline mgmt) |
| T-029 | End-to-end deployment orchestration | DCWF [5944] CI/CD; DCWF [7088] | **KEEP** — distinct from T-005/T-016 (pipeline building) |
| T-030 | Transparency/explainability | EUAIA-O-012; AIRMF-MS-2.9 | **KEEP** — distinct concept |
| T-031 | AI incident management | EUAIA-O-047; EUAIA-O-052 | **KEEP** — distinct concept |
| T-032 | AI literacy/training programs | EUAIA-C-001; AIRMF-GV-2.2 | **KEEP** — distinct concept |
| T-033 | Third-party AI assessment | AIRMF-MG-3.1; AIRMF-GV-6.1 | **KEEP** — distinct concept |
| T-034 | Feedback systems | AIRMF-GV-5.2; AIRMF-MG-2.4; AIRMF-MS-3.3 | **KEEP** — distinct concept |
| T-035 | AI system inventory | AIRMF-GV-1.6 | **KEEP** — distinct operational task |
| T-036 | AI decommissioning | AIRMF-MG-1.3; lifecycle evidence | **KEEP** — distinct concept |
| T-037 | AI workload cost optimization | DDaT-SK-089, DDaT-SK-091 financial/budget | **KEEP** — distinct operational task |
| T-038 | Executive communication | DCWF [7058] communicating AI/ML; [5909] | **KEEP** — distinct from T-002 (technical docs) |

**Net effect:** 17 kept, 0 removed

## Final Count

19 (Phase 1A deduplicated) + 17 (validated post-STRM) = **36 entries**

## Entry Mapping: Current → Proposed

| Proposed | Source | Action |
|----------|--------|--------|
| AI-T-001 | T-001 | Preserve (design/train/evaluate ML models) |
| AI-T-002 | T-002 | Preserve (model documentation) |
| AI-T-003 | T-003 | Preserve (post-deployment monitoring) |
| AI-T-004 | T-004 + T-017 | Merge (monitoring/observability implementation) |
| AI-T-005 | T-005 + T-016 | Merge (ML pipeline building) |
| AI-T-006 | T-006 | Preserve (LLM application systems) |
| AI-T-007 | T-007 | Preserve (AI eval against criteria) |
| AI-T-008 | T-008 | Preserve (NLP systems) |
| AI-T-009 | T-009 | Preserve (NLP error analysis) |
| AI-T-010 | T-010 | Preserve (CV systems) |
| AI-T-011 | T-011 | Preserve (ML platform architecture) |
| AI-T-012 | T-012 | Preserve (MLOps standards) |
| AI-T-013 | T-013 | Preserve (ML tooling evaluation) |
| AI-T-014 | T-014 | Preserve (data collaboration) |
| AI-T-015 | T-015 | Preserve (platform infrastructure) |
| AI-T-016 | T-018 | Renumber (research projects) |
| AI-T-017 | T-019 | Renumber (AI innovation pipeline) |
| AI-T-018 | T-020 | Renumber (POC building) |
| AI-T-019 | T-021 | Renumber (platform maintenance) |
| AI-T-020 | T-022 | Renumber (AI risk assessment) |
| AI-T-021 | T-023 | Renumber (fairness/bias evaluation) |
| AI-T-022 | T-024 | Renumber (adversarial testing) |
| AI-T-023 | T-025 | Renumber (regulatory documentation) |
| AI-T-024 | T-026 | Renumber (training data governance) |
| AI-T-025 | T-027 | Renumber (human oversight) |
| AI-T-026 | T-028 | Renumber (use case feasibility) |
| AI-T-027 | T-029 | Renumber (deployment orchestration) |
| AI-T-028 | T-030 | Renumber (transparency/explainability) |
| AI-T-029 | T-031 | Renumber (incident management) |
| AI-T-030 | T-032 | Renumber (AI literacy/training) |
| AI-T-031 | T-033 | Renumber (third-party assessment) |
| AI-T-032 | T-034 | Renumber (feedback systems) |
| AI-T-033 | T-035 | Renumber (AI system inventory) |
| AI-T-034 | T-036 | Renumber (decommissioning) |
| AI-T-035 | T-037 | Renumber (cost optimization) |
| AI-T-036 | T-038 | Renumber (executive communication) |
