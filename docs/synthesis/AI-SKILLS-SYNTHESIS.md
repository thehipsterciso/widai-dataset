# AI/ML Foundations — Skills Dimension Synthesis

**Domain**: AI (AI/ML Foundations)
**Dimension**: Skills
**Date**: 2026-04-03
**Schema**: 3.0.0
**Starting count**: 29 (AI-S-001 through AI-S-029)

---

## Evidence Summary

| Metric | Value |
|--------|-------|
| Total STRM mappings | 22,682 |
| Framework elements at STS ≥ 0.50 | 280 |
| Framework elements at STS ≥ 0.55 | 225 |
| Framework elements at STS ≥ 0.60 | 175 |
| Phase 1A entries (with STRM evidence) | 19 (S-001 through S-019, all 6/6 coverage) |
| Post-STRM entries (zero evidence) | 10 (S-020 through S-029) |

Evidence density: 175 / 29 = 6.0 elements per entry at STS ≥ 0.60.

### Entry Evidence Matrix

All 19 Phase 1A entries have 6/6 framework coverage. Strongest:

| Entry | Total Maps | Max STS | Strong |
|-------|-----------|---------|--------|
| AI-S-010 (fine-tuning) | 2,292 | 0.7674 | 11 |
| AI-S-016 (infra troubleshooting) | 1,688 | 0.7036 | 1 |
| AI-S-009 (guardrails) | 1,660 | 0.6792 | 0 |
| AI-S-001 (problem formulation) | 1,628 | 0.6764 | 0 |
| AI-S-008 (RAG pipelines) | 1,591 | 0.7456 | 0 |

Weakest Phase 1A (still well-supported):

| Entry | Total Maps | Max STS |
|-------|-----------|---------|
| AI-S-004 (stakeholder communication) | 300 | 0.6250 |
| AI-S-015 (CI/CD for ML) | 560 | 0.6457 |
| AI-S-007 (prompt engineering) | 688 | 0.6440 |

---

## Duplicate Analysis

Examined all 29 entries for overlapping scope.

### Pair 1: AI-S-003 (production ML code) vs AI-S-014 (feature engineering pipelines)

- S-003: writing and refactoring ML code to production quality — data processing, training, evaluation, unit testing
- S-014: designing feature pipelines for batch and real-time serving — consistency, reproducibility, low-latency

S-003 is about code quality across all ML code. S-014 is specifically about feature pipeline design. Different scopes confirmed by evidence: S-003 attracts 39 elements at STS ≥ 0.55; S-014 attracts 89 with minimal overlap.

**Decision**: KEEP SEPARATE.

### Pair 2: AI-S-005 (serving APIs) vs AI-S-028 (integration/deployment orchestration)

- S-005: designing model serving APIs — input validation, output formatting, error handling, versioning
- S-028: orchestrating end-to-end AI integration — enterprise systems coordination, API contracts, infrastructure-as-code

S-005 is the specific API design skill. S-028 is the broader orchestration that includes API contracts as one component.

**Decision**: KEEP SEPARATE. Different granularity.

### Pair 3: AI-S-019 (transparency/explainability) vs AI-S-021 (fairness/bias)

- S-019: implementing transparency and explainability mechanisms
- S-021: evaluating fairness and bias, detecting disparate impact

Distinct concept areas: transparency is about making decisions understandable; fairness is about equitable outcomes. EU AI Act treats these separately.

**Decision**: KEEP SEPARATE.

### Pair 4: AI-S-002 (EDA) vs AI-S-023 (data preprocessing for ML)

- S-002: exploratory data analysis — distributional analysis, correlation, anomaly detection, translating EDA into modeling decisions
- S-023: data preprocessing — cleaning, deduplication, normalization, label quality, documentation

EDA is analytical (understanding data); preprocessing is operational (preparing data for training). Different phases of the ML workflow.

**Decision**: KEEP SEPARATE.

### Result: 0 duplicate merges

---

## Gap Analysis

### Entry Overload (STS ≥ 0.55)

| Entry | Elements | Assessment |
|-------|----------|-----------|
| AI-S-010 | 144 | High — attracts generic ML tool/training elements from NICE/DCWF |
| AI-S-001 | 120 | High — broad "problem formulation" concept naturally attracts many elements |
| AI-S-016 | 102 | High — infrastructure troubleshooting touches many system-level elements |
| AI-S-011 | 93 | High — NLP evaluation intersects many testing elements |

S-010 overload analysis: 144 elements at STS ≥ 0.55 is the highest in the AI domain. The fine-tuning concept intersects with training, evaluation, tool usage, and software configuration elements from NICE and DCWF. However, the overload is distributed across generic elements (S0745 "testing tools", S0681 "design modeling") rather than concentrated in a specific uncovered concept. No decomposition warranted — the concept is already specific enough.

### Broader Gap Assessment

146 gap signals from the enforcer. Categories:

1. **Generic framework elements**: S0631 "data preprocessing" (STS=0.7149, maps to 6 entries), S0745 "testing tools" (STS=0.6859, maps to 15 entries). These are nonspecific descriptors. No action.

2. **EU AI Act skill concepts already covered by post-STRM entries**:
   - EUAIA-O-012 (transparency, STS=0.7674) → covered by S-019
   - EUAIA-O-004 (test protocols, STS=0.6802) → covered by S-022
   - EUAIA-O-054 (resilience engineering, STS=0.7039) → partially covered by S-022

3. **NIST AI RMF concepts already covered by post-STRM entries**:
   - AIRMF-GV-5.2 (feedback mechanisms, STS=0.6874) → covered by S-026
   - AIRMF-MP-1.3 (business value, STS=0.6987) → covered by S-017
   - AIRMF-MS-2.5 (validity/reliability, STS=0.6783) → covered by S-022

4. **Concepts better suited to other domains**: Executive governance skills (AIRMF-GV-2.3) → LS domain. Organizational safety culture → AG domain.

5. **Potential gaps examined**:
   - *AI resilience engineering skill*: EUAIA-O-054 at STS=0.7039. Partially covered by S-022 (adversarial testing includes resilience testing). The remaining uncovered aspect (error handling design, fault tolerance) is an engineering practice more than a distinct skill category. Not enough evidence for standalone.
   - *AI incident response skill*: EUAIA-O-052 at STS=0.5444. Low STS suggests weak mapping. Better suited for RC (Risk & Compliance) domain.

**Result**: 0 new entries. Evidence does not support expansion beyond current 29.

---

## Post-STRM Entry Validation

### AI-S-020: AI Risk Assessment
- EUAIA-O-002 (STS=0.5835): "conducting iterative AI risk assessment across the system lifecycle"
- EUAIA-O-004 (STS=0.6802): "designing and executing test protocols for high-risk AI systems"
- AIRMF-MS-1.1 (STS=0.5315 via Knowledge): AI risk measurement approaches

**Decision**: RETAIN.

### AI-S-021: Fairness and Bias Evaluation
- AIRMF-MS-2.11 (STS=0.5192 via Knowledge): "AI fairness and bias evaluation"
- EUAIA-O-012 (STS=0.7674): transparency elements include bias disclosure

**Decision**: RETAIN.

### AI-S-022: Adversarial Testing / Red-Teaming
- DCWF [7054] (STS=0.7381): "testing robustness and resilience of AI products"
- EUAIA-O-054 (STS=0.7039): "AI system resilience engineering"
- DCWF [5922] (STS=0.6851): "test reliability, security, and compatibility"

**Decision**: RETAIN. Strong indirect evidence.

### AI-S-023: Data Preprocessing for ML
- NICE [S0631] (STS=0.7149): "performing data preprocessing"
- NICE [S0954] (STS=0.6648): "dividing data into training, validation, and test data sets"

**Decision**: RETAIN. Strong direct evidence.

### AI-S-024: Regulatory Documentation
- EUAIA-O-042 (STS=0.5803 via Knowledge): "downstream integration documentation"
- EUAIA-O-010 (STS=0.5361 via Knowledge): "AI system logging architecture"
- Multiple EUAIA conformity/documentation elements at moderate STS

**Decision**: RETAIN.

### AI-S-025: AI Monitoring and Observability
- EUAIA-O-049 (STS=0.6079 via Knowledge): "AI post-market monitoring systems"
- EUAIA-O-011 (STS=0.5171 via Knowledge): "monitoring and logging systems"
- DCWF [7029] (STS=0.6576 via Knowledge): "collect, store, and monitor data"

**Decision**: RETAIN.

### AI-S-026: Feedback Incorporation Mechanisms
- AIRMF-GV-5.2 (STS=0.6874): "feedback incorporation mechanisms, adjudication processes"
- AIRMF-MG-2.4 (STS=0.6845): "AI feedback incorporation systems"
- AIRMF-MS-3.3 (STS=0.6299): "end-user and community feedback mechanisms"

**Decision**: RETAIN. Strong evidence from NIST AI RMF.

### AI-S-027: Third-Party AI Assessment
- AIRMF-GV-6.2 (STS=0.6224): "contingency plans for third-party AI dependencies"
- AIRMF-MG-3.1 (STS=0.5984 via Knowledge): "third-party AI risk monitoring"

**Decision**: RETAIN.

### AI-S-028: Integration and Deployment Orchestration
- DCWF [7028] (STS=0.7083): "automate development, testing, security, and deployment of AI/ML software"
- DCWF [5944] (STS=0.7036): "tooling for CI/CD pipelines"

**Decision**: RETAIN. Strong evidence.

### AI-S-029: AI Literacy and Training Programs
- EUAIA-C-001 (STS=0.5124 via Knowledge): "AI literacy program design, competency assessment"
- AIRMF-GV-2.2 (STS=0.5071 via Knowledge): "AI risk management training programs"

**Decision**: RETAIN.

---

## Mandatory Checklist

- [x] 1. Duplicate groups: **0**. 4 pairs examined, all differentiated.
- [x] 2. Gap clusters from evidence: **0** warranting new entries.
- [x] 3-5. No new entries needed — all framework concepts are covered by existing entries or post-STRM entries.
- [x] 6. Post-STRM validated: All 10 (S-020 through S-029) confirmed with indirect evidence.
- [x] 7. Final count: **29**. No merges, no additions. 19 Phase 1A + 10 post-STRM = 29.
- [x] 8. Count unchanged at 29. No gaps exist because: (a) 10 post-STRM entries already fill the major gap areas (risk, fairness, adversarial testing, preprocessing, documentation, monitoring, feedback, supply chain, integration, literacy); (b) evidence density of 6.0:1 at STS ≥ 0.60 is reasonable given broad concepts; (c) remaining gap signals are generic framework elements or concepts better suited to other WIDAI domains.

---

## Final Entry Map

All 29 entries preserved as-is. No renumbering required.

| ID Range | Type | Count |
|----------|------|-------|
| AI-S-001 through AI-S-019 | Phase 1A (STRM-evidenced) | 19 |
| AI-S-020 through AI-S-029 | Post-STRM (indirect evidence) | 10 |
