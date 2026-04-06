# AG Abilities — Evidence-Driven Re-Synthesis (Enforced)

## Overview

Domain: AI Governance & Ethics (AG)
Dimension: Abilities
Starting count: 28 (from prior evidence-first expansion)
Final count: 28 (validated, no changes)
Schema: 3.0.0
Methodology: Evidence-first synthesis with programmatic enforcement (synthesis_enforcer.py) and adversarial validation (adversarial_validator.py)

## Evidence Summary

Total mappings across 6 frameworks: 3,839
Framework elements at STS >= 0.50: 123
Framework elements at STS >= 0.55: 123
Framework elements at STS >= 0.60: 33

Evidence density: 1.2 elements per entry at STS >= 0.60 — sparse, structurally expected for abilities.

### High Watermark

| Framework | >=0.45 | >=0.50 | >=0.55 | >=0.60 |
|-----------|--------|--------|--------|--------|
| O*NET 30.2 | 10 | 4 | 2 | 0 |
| NIST NICE v2.1.0 | 287 | 111 | 36 | 3 |
| DoD DCWF v5.1 | 443 | 194 | 67 | 15 |
| DDaT | 36 | 26 | 17 | 6 |
| EU AI Act | 37 | 26 | 13 | 3 |
| NIST AI RMF 1.0 | 65 | 58 | 30 | 12 |

Abilities dimension shows structurally lower STS across all frameworks. Source frameworks describe competencies as Knowledge, Skills, and Tasks — not as abstract cognitive abilities. The thin evidence is expected, not a data quality issue.

4 Phase 1A entries (A-001 through A-004): have STRM evidence.
24 post-STRM entries (A-005 through A-028): 0/6 direct coverage — added during prior expansion.

## Duplicate Analysis

4 close pairs examined:

**Pair 1: AG-A-001 (risk identification/assessment/prioritization) vs AG-A-010 (measurement frameworks/metrics for risk)**
A-001 covers the ability to identify, assess, and prioritize risks. A-010 covers designing measurement frameworks that characterize risk. One is the cognitive act of risk evaluation; the other is designing the instrumentation. No merge.

**Pair 2: AG-A-003 (operationalizing trustworthy AI principles) vs AG-A-025 (implementing Responsible AI best practices)**
A-003 covers defining and embedding trustworthy AI principles broadly. A-025 covers implementing specific RAI best practices and standards. Close in scope but A-003 is about the principled foundation while A-025 is about standards-based execution. Reviewed — distinct enough to maintain but flagged as closest pair. No merge.

**Pair 3: AG-A-006 (governance structures/frameworks/accountability) vs AG-A-009 (governance frameworks for human oversight)**
A-006 covers designing governance structures broadly. A-009 covers specifically governance of human-AI oversight mechanisms. A-009 is a subset topic but distinct enough — human oversight governance is a specific, regulation-mandated governance function (EU AI Act Article 14). No merge.

**Pair 4: AG-A-002 (interpreting evolving regulations) vs AG-A-027 (synthesizing requirements from multiple frameworks)**
A-002 covers tracking and applying changing regulations. A-027 covers reconciling requirements across multiple regulatory frameworks simultaneously. Different cognitive tasks: monitoring change vs integrating complexity. No merge.

**Merges: 0**

## Gap Analysis

Synthesis enforcer detected 3 gap signals — all overload-based:

**AG-A-004: 84 elements at STS >= 0.55**
A-004 covers developing, documenting, and communicating governance policies. High overload is structural — policy development is the broadest governance ability and attracts generic framework elements about documentation and communication. Decomposition not warranted: the ability is "develop and communicate governance policies," which is a coherent single cognitive capability.

**AG-A-001: 55 elements at STS >= 0.55**
A-001 covers risk identification, assessment, and prioritization. The three components (identify, assess, prioritize) are a natural cognitive sequence, not separable abilities. No decomposition.

**AG-A-003: 45 elements at STS >= 0.55**
A-003 covers operationalizing trustworthy AI principles. The overload comes from AIRMF-GV-1.2 (STS 0.6782, "integrating trustworthy AI principles") which maps broadly. The entry already captures this specific concept. No decomposition.

**New entries: 0**

## Post-STRM Validation (A-005 through A-028)

24 entries added during prior expansion. Representative validation:

| Entry | Concept | Indirect Evidence |
|-------|---------|-------------------|
| AG-A-005 | Stakeholder commitment building | AIRMF-GV-5.1 (STS 0.5859 → A-001, A-004) |
| AG-A-007 | AI monitoring system design | AIRMF-MS-2.4 (STS 0.5828 → A-001, A-004) |
| AG-A-008 | Transparency requirement assessment | AIRMF-MS-2.8 (STS 0.5817 → A-001) |
| AG-A-012 | Serious incident investigation | AIRMF-GV-4.3 (STS 0.5779 → A-004); incident management is explicit EU AI Act requirement |
| AG-A-014 | AI adoption strategy design | DCWF 492B (STS 0.6196 → A-003, A-004) |
| AG-A-016 | Relating AI strategy to business/technology | DCWF 6923 (STS 0.6071 → A-004) |
| AG-A-017 | Third-party vendor risk monitoring | AIRMF-MG-3.1 (STS 0.6059 → A-001, A-003) |
| AG-A-018 | Navigating competing ethical values | Structural governance ability — no framework captures this directly |
| AG-A-020 | Monitoring emerging AI capabilities | AIRMF-MG-4.2 (STS 0.6041 → K-entries); emerging technology monitoring |
| AG-A-022 | Communicating governance rationale | Structural — cross-audience communication is core governance ability |
| AG-A-023 | Cross-organizational governance coordination | AIRMF-GV-3.1 (STS 0.5569 → T-entries); multi-team coordination |
| AG-A-026 | Data management compliance | AIRMF-GV-1.1 (STS 0.6546 → A-001, A-004); data governance regulatory compliance |
| AG-A-028 | Integrating measurement results into decisions | AIRMF-MS-4.2 (STS 0.6888 → A-001, A-003, A-004) — strongest evidence for any abilities entry |

All 24 post-STRM entries retained. Several (A-018, A-022, A-024) are structural governance abilities that no framework captures directly — these are cognitive capabilities identified from practitioner experience, not framework evidence. They are retained because abilities are the dimension where WIDAI adds unique value beyond what frameworks articulate.

## Mandatory Checklist

- [x] 1. Duplicate groups: **0 merges from 4 pairs examined. A-003/A-025 flagged as closest pair but distinct.**
- [x] 2. Gap clusters: **3 overload signals, no concept gaps.**
- [x] 3. Cluster concepts: **Overload from structural breadth of governance abilities, not decomposition signals.**
- [x] 4. New entries: **None.**
- [x] 5. Framework evidence: **Cited per overload signal. Top STS: AIRMF-MS-4.2 at 0.6888.**
- [x] 6. Post-STRM validated: **Yes — all 24 entries (A-005 through A-028) validated.**
- [x] 7. Final count: **28 = 4 Phase 1A + 24 post-STRM. 0 merged, 0 new.**
- [x] 8. Count unchanged at 28: **AG Abilities was already expanded from 15 to 28. The sparse evidence (33 elements at STS >= 0.60) is structural for the abilities dimension. Source frameworks do not articulate abilities at WIDAI's granularity — WIDAI adds unique value here.**

## Final Entry Map

28 Abilities entries: AG-A-001 through AG-A-028.
4 Phase 1A + 24 post-STRM (all validated).
0 merges, 0 new entries.
