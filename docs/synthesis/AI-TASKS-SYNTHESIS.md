# AI/ML Foundations — Tasks Dimension Synthesis

**Domain**: AI (AI/ML Foundations)
**Dimension**: Tasks
**Date**: 2026-04-03
**Schema**: 3.0.0
**Starting count**: 36 (AI-T-001 through AI-T-036)

---

## Evidence Summary

| Metric | Value |
|--------|-------|
| Total STRM mappings | 16,786 |
| Framework elements at STS ≥ 0.50 | 264 |
| Framework elements at STS ≥ 0.55 | 197 |
| Framework elements at STS ≥ 0.60 | 149 |
| Phase 1A entries (with STRM evidence) | 21 (T-001 through T-021, all 6/6 coverage) |
| Post-STRM entries (zero evidence) | 15 (T-022 through T-036) |

Evidence density: 149 / 36 = 4.1 elements per entry at STS ≥ 0.60.

### Entry Evidence Matrix

Strongest Phase 1A entries:

| Entry | Total Maps | Max STS | Strong |
|-------|-----------|---------|--------|
| AI-T-007 (evaluate AI performance) | 699 | 0.7891 | 4 |
| AI-T-015 (data platform infra) | 994 | 0.7527 | 1 |
| AI-T-020 (AI risk assessment) | 1,293 | 0.7472 | 2 |
| AI-T-004 (monitoring systems) | 887 | 0.7406 | 1 |
| AI-T-016 (research projects) | 814 | 0.7169 | 1 |

Weakest Phase 1A (still well-supported):

| Entry | Total Maps | Max STS |
|-------|-----------|---------|
| AI-T-011 (ML platform architecture) | 293 | 0.6356 |
| AI-T-021 (fairness evaluation) | 295 | 0.7066 |
| AI-T-009 (NLP error analysis) | 486 | 0.5907 |

---

## Duplicate Analysis

### Pair 1: AI-T-003 (post-deployment monitoring) vs AI-T-004 (monitoring system implementation)

- T-003: conducting monitoring — identifying degradation, drift, retraining conditions (operational task)
- T-004: implementing monitoring systems — dashboards, alerting, automated triggers (engineering task)

"Conduct monitoring" vs "build monitoring infrastructure." Different task types (operate vs build).

**Decision**: KEEP SEPARATE.

### Pair 2: AI-T-002 (model documentation) vs AI-T-023 (regulatory documentation)

- T-002: model card, performance characteristics, known limitations, monitoring recommendations (deployment documentation)
- T-023: regulatory-grade technical specs, risk records, conformity evidence, data provenance (compliance documentation)

T-002 is internal deployment documentation. T-023 is external regulatory compliance documentation. Different audiences and standards.

**Decision**: KEEP SEPARATE.

### Pair 3: AI-T-017 (AI innovation pipeline) vs AI-T-026 (use case feasibility)

- T-017: managing the innovation pipeline — ideation, triage, prioritization, POC communication
- T-026: conducting feasibility assessments — data availability, complexity, readiness, value quantification

T-017 is portfolio management. T-026 is individual use case assessment. T-026 feeds into T-017.

**Decision**: KEEP SEPARATE.

### Pair 4: AI-T-018 (build PoC) vs AI-T-026 (feasibility assessment)

- T-018: build and deliver proof-of-concepts, documenting approach and results
- T-026: conduct feasibility assessments before PoC commitment

Sequential tasks. Assessment precedes build.

**Decision**: KEEP SEPARATE.

### Result: 0 duplicate merges

---

## Gap Analysis

86 gap signals from the enforcer. Analysis:

1. **Generic framework elements**: T1528 "software testing" (STS=0.6589, 11 entries), T1135 "design/develop software" (STS=0.6587, 7 entries). Nonspecific descriptors that naturally map broadly. No action.

2. **DCWF AI-specific elements already covered**: [5872] "design, develop, implement AI tools" (STS=0.7108) maps to 7 entries — generic AI development task, already fully covered by T-001 through T-010.

3. **EU AI Act task concepts covered by post-STRM entries**: Adversarial testing → T-022. Regulatory documentation → T-023. Data governance → T-024. Human oversight → T-025. Incident management → T-029. Decommissioning → T-034.

4. **NIST AI RMF task concepts covered**: Risk assessment → T-020. Feedback mechanisms → T-032. Third-party assessment → T-031. System inventory → T-033.

5. **Potential gaps examined**: No framework element clusters suggest uncovered task concepts. The 15 post-STRM entries already fill governance, compliance, and lifecycle gaps.

**Result**: 0 new entries. Evidence does not support expansion beyond 36.

---

## Post-STRM Entry Validation

### T-022: Adversarial Testing / Red-Teaming
- DCWF [7054] (STS=0.7381 via Skills): "testing robustness and resilience of AI products"
- EUAIA-O-054 (STS=0.7039 via Skills): "AI system resilience engineering"

**Decision**: RETAIN.

### T-023: Regulatory Documentation
- EUAIA-O-042 (STS=0.5803 via Knowledge): downstream integration documentation
- Multiple EUAIA conformity assessment elements

**Decision**: RETAIN.

### T-024: Training Data Governance
- EUAIA-O-006 (STS=0.5385 via Knowledge): AI training data governance
- EUAIA-O-028 (STS=0.5195 via Knowledge): AI input data quality management

**Decision**: RETAIN.

### T-025: Human Oversight Mechanisms
- EUAIA-C-003 (STS=0.6804 via Knowledge): exercise human oversight
- AIRMF-GV-3.2 (STS=0.5439 via Knowledge): human-AI interaction governance

**Decision**: RETAIN.

### T-026: Use Case Feasibility
- AIRMF-MP-1.3 (STS=0.6260 via Knowledge): evaluate AI business value
- DCWF [7042] (STS=0.6496 via Knowledge): resources required for AI projects

**Decision**: RETAIN.

### T-027: Integration and Deployment
- DCWF [7028] (STS=0.7083 via Skills): automate AI development/deployment

**Decision**: RETAIN.

### T-028: Transparency / Explainability
- AIRMF-MS-2.9 (STS=0.6111 via Knowledge): model explanation and interpretation

**Decision**: RETAIN.

### T-029: Incident Management
- EUAIA-O-052 (STS=0.5444 via Skills): AI serious incident investigation
- EUAIA-O-047 (STS=0.5530 via Knowledge): serious incident management

**Decision**: RETAIN.

### T-030: AI Literacy Programs
- EUAIA-C-001 (STS=0.5124 via Knowledge): AI literacy program design

**Decision**: RETAIN.

### T-031: Third-Party AI Assessment
- AIRMF-GV-6.1 (STS=0.5483 via Knowledge): AI supply chain risk management

**Decision**: RETAIN.

### T-032: Feedback Systems
- AIRMF-GV-5.2 (STS=0.6874 via Skills): feedback incorporation mechanisms

**Decision**: RETAIN.

### T-033: AI System Inventory
- AIRMF-GV-1.6 (STS=0.5311 via Knowledge): AI system inventory mechanisms

**Decision**: RETAIN.

### T-034: System Decommissioning
- AIRMF-GV-1.7 (STS=0.5625 via Knowledge): AI system decommissioning procedures

**Decision**: RETAIN.

### T-035: Cost / Resource Optimization
- DCWF elements on resource management and GPU scheduling. Indirect evidence from platform operations elements.

**Decision**: RETAIN.

### T-036: Executive Communication
- DCWF [7058] (STS=0.6807 via Skills): communicating AI solutions to wide audiences

**Decision**: RETAIN.

---

## Mandatory Checklist

- [x] 1. Duplicate groups: **0**. 4 pairs examined, all differentiated.
- [x] 2. Gap clusters: **0** warranting new entries.
- [x] 3-5. No new entries needed.
- [x] 6. Post-STRM validated: All 15 (T-022 through T-036) confirmed with indirect evidence.
- [x] 7. Final count: **36**. No merges, no additions.
- [x] 8. Count unchanged at 36. No gaps exist because: (a) 15 post-STRM entries comprehensively fill governance, compliance, lifecycle, and communication task gaps; (b) evidence density of 4.1:1 is reasonable; (c) 86 gap signals are all generic framework elements or concepts already covered.

---

## Final Entry Map

All 36 entries preserved as-is. No renumbering required.

| ID Range | Type | Count |
|----------|------|-------|
| AI-T-001 through AI-T-021 | Phase 1A (STRM-evidenced) | 21 |
| AI-T-022 through AI-T-036 | Post-STRM (indirect evidence) | 15 |
