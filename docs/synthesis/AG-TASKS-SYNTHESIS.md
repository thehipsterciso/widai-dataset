# AG Tasks — Phase 1D Synthesis Analysis

**Domain:** AI Governance & Ethics (AG)
**Dimension:** Tasks
**Date:** 2026-04-03
**Pre-synthesis count:** 25 (11 Phase 1A baseline + 14 post-STRM additions)
**Post-synthesis count:** 23

## Evidence Summary

- **Total mappings:** 11,745 across 6 frameworks
- **Phase 1A entries (T-001 to T-011):** All have STRM evidence (10 at 6/6, 1 at 5/6)
- **Post-STRM entries (T-012 to T-025):** 0/6 coverage (added after STRM runs)

### High Watermark (unique FDE count at STS thresholds)

| Framework | >=0.45 | >=0.50 | >=0.55 | >=0.60 |
|-----------|--------|--------|--------|--------|
| O*NET 30.2 | 8 | 3 | 2 | 0 |
| NIST NICE v2.1.0 | 601 | 342 | 153 | 57 |
| DoD DCWF v5.1 | 995 | 575 | 291 | 102 |
| DDaT | 58 | 30 | 14 | 2 |
| EU AI Act | 57 | 53 | 42 | 23 |
| NIST AI RMF 1.0 | 69 | 66 | 61 | 44 |

### Strongest STRM Hits

| Entry | Strong | Max STS | Top framework evidence |
|-------|--------|---------|----------------------|
| AG-T-008 | 9 | 0.7926 | AIRMF-MG-1.4 residual risk documentation |
| AG-T-010 | 9 | 0.7503 | DCWF 5934 automated T&E tool framework |
| AG-T-007 | 3 | 0.7041 | AIRMF-MG-3.1 third-party risk monitoring |
| AG-T-002 | 1 | 0.7534 | AIRMF-GV-1.6 AI system inventory mechanisms |
| AG-T-009 | 1 | 0.7094 | AIRMF-MS-2.13 TEVV effectiveness assessment |
| AG-T-001 | 0 | 0.6933 | DCWF 5882 responsible AI processes |
| AG-T-006 | 0 | 0.6598 | NICE T1792 assess intelligence production effectiveness |
| AG-T-003 | 0 | 0.6349 | DCWF 7056 assessing AI for bias/ethical concerns |
| AG-T-005 | 0 | 0.6661 | NICE T1950 manage continuous monitoring program |
| AG-T-004 | 0 | 0.6498 | DCWF 5868 AI risk assessment policies |
| AG-T-011 | 0 | 0.6775 | DCWF 1070A monitor emerging tech impact on regulations |

## Duplicate Identification (Phase 1A)

### Duplicate Group 1: AI System Inventory (T-002 + T-005)
- **T-002:** "Establish and maintain the enterprise AI inventory, cataloging all AI systems in production with risk tier, owner, training data provenance, model version, and review status."
- **T-005:** "Maintain the enterprise AI system inventory, ensuring all AI applications are registered, risk-tiered, owned, and subject to appropriate review and monitoring."
- **Resolution:** Merge into single inventory task combining establishment, cataloging, and ongoing maintenance. T-002 has stronger evidence (6/6, 1 strong, max 0.7534 vs T-005's 6/6, 0 strong, max 0.6661).

### Duplicate Group 2: AI Impact Assessment (T-006 + T-008)
- **T-006:** "Conduct AI impact assessments for new and materially modified AI systems prior to production deployment."
- **T-008:** "Conduct AI impact assessments for new and materially modified AI systems, producing documented risk findings with recommended mitigations and residual risk statements."
- **Resolution:** Merge. T-008 is a superset of T-006, adding the output specification (documented risk findings, mitigations, residual risk). Use T-008 as base and retain T-006's "prior to production deployment" timing.

**Net effect:** 11 Phase 1A entries, 2 merges = 9 distinct Phase 1A entries

## Post-STRM Entry Evaluation (T-012 to T-025)

| Entry | Concept | Framework evidence | Verdict |
|-------|---------|-------------------|---------|
| T-012 | Governance review process operations | DCWF 5882 (0.7242) responsible AI processes; DCWF 5862 (0.6700) governance structure | **KEEP** — distinct operational task |
| T-013 | Iterative lifecycle risk assessment | EUAIA-O-002 (0.6786) iterative risk assessment; AIRMF-MG-1.3 (0.7081) risk response strategy | **KEEP** — lifecycle-spanning process, distinct from merged T-006+T-008 (discrete pre-deployment assessment) |
| T-014 | Regulatory-grade documentation | EUAIA-O-009 (0.6352) technical documentation; EUAIA-O-041 (0.6573) GPAI documentation | **KEEP** — distinct documentation task |
| T-015 | Post-market monitoring | EUAIA-O-049 (0.7344) post-market monitoring; EUAIA-O-050 (0.7016) performance data | **KEEP** — distinct operational task |
| T-016 | Incident management | EUAIA-O-047 (0.6203) incident management; EUAIA-O-052 (0.6412) incident investigation | **KEEP** — distinct |
| T-017 | Third-party AI risk | AIRMF-MG-3.1 (0.7041) third-party monitoring; AIRMF-GV-6.1 (0.6524) supply chain risk | **KEEP** — distinct |
| T-018 | TEVV governance | AIRMF-MS-2.13 (0.7094) TEVV effectiveness; AIRMF-MP-3.4 (0.6569) TEVV trade-offs | **KEEP** — distinct |
| T-019 | Fundamental rights impact assessment | EUAIA-O-032 (0.5871) FRIA; EUAIA-O-031 (0.6661) DPIA for AI | **KEEP** — distinct |
| T-020 | Governance literacy/training | DCWF 5330A (0.7270) AI workforce metrics; AIRMF-GV-2.2 (0.6024) risk management training | **KEEP** — distinct |
| T-021 | Stakeholder engagement | AIRMF-GV-5.1 (0.6264) external stakeholder engagement; AIRMF-MS-3.3 (0.6110) feedback mechanisms | **KEEP** — distinct |
| T-022 | Conformity assessment | EUAIA-O-018 (0.6126) conformity assessment execution | **KEEP** — distinct |
| T-023 | Transparency/disclosure | EUAIA-O-037 (0.5314) interaction disclosure; EUAIA-O-038 (0.5195) content provenance | **KEEP** — distinct |
| T-024 | Risk quantification/measurement | AIRMF-MS-1.1 (0.6286) risk measurement; DCWF 5873 (0.6624) risk metrics | **KEEP** — distinct |
| T-025 | Decommissioning | AIRMF-GV-1.7 (0.6504) decommissioning procedures | **KEEP** — distinct |

**Net effect:** 14 kept, 0 merged

## Final Count

9 (Phase 1A after 2 merges) + 14 (validated post-STRM) = **23 entries**

## Entry Mapping: Current → Proposed

| Proposed | Source | Action |
|----------|--------|--------|
| AG-T-001 | T-001 | Preserve (enterprise AI governance framework) |
| AG-T-002 | T-002 + T-005 | Merge (AI system inventory: establish + maintain) |
| AG-T-003 | T-003 | Preserve (AI ethics reviews) |
| AG-T-004 | T-004 | Preserve (acceptable use policy) |
| AG-T-005 | T-006 + T-008 | Merge (AI impact assessments with documented outputs) |
| AG-T-006 | T-007 | Renumber (policy compliance monitoring) |
| AG-T-007 | T-009 | Renumber (bias audits) |
| AG-T-008 | T-010 | Renumber (responsible AI assessment tools) |
| AG-T-009 | T-011 | Renumber (regulatory development monitoring) |
| AG-T-010 | T-012 | Renumber (governance review operations) |
| AG-T-011 | T-013 | Renumber (iterative lifecycle risk assessment) |
| AG-T-012 | T-014 | Renumber (regulatory-grade documentation) |
| AG-T-013 | T-015 | Renumber (post-market monitoring) |
| AG-T-014 | T-016 | Renumber (incident management) |
| AG-T-015 | T-017 | Renumber (third-party AI risk) |
| AG-T-016 | T-018 | Renumber (TEVV governance) |
| AG-T-017 | T-019 | Renumber (fundamental rights impact assessment) |
| AG-T-018 | T-020 | Renumber (governance literacy/training) |
| AG-T-019 | T-021 | Renumber (stakeholder engagement) |
| AG-T-020 | T-022 | Renumber (conformity assessment) |
| AG-T-021 | T-023 | Renumber (transparency/disclosure) |
| AG-T-022 | T-024 | Renumber (risk quantification/measurement) |
| AG-T-023 | T-025 | Renumber (decommissioning) |
