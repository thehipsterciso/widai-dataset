# AG Tasks — Evidence-Driven Re-Synthesis (Enforced)

## Overview

Domain: AI Governance & Ethics (AG)
Dimension: Tasks
Starting count: 23 (from prior evidence-first expansion)
Final count: 23 (validated, no changes)
Schema: 3.0.0
Methodology: Evidence-first synthesis with programmatic enforcement (synthesis_enforcer.py) and adversarial validation (adversarial_validator.py)

## Evidence Summary

Total mappings across 6 frameworks: 11,745
Framework elements at STS >= 0.50: 457
Framework elements at STS >= 0.55: 457
Framework elements at STS >= 0.60: 195

Evidence density: 8.5 elements per entry at STS >= 0.60.

### High Watermark

| Framework | >=0.45 | >=0.50 | >=0.55 | >=0.60 |
|-----------|--------|--------|--------|--------|
| O*NET 30.2 | 8 | 3 | 2 | 0 |
| NIST NICE v2.1.0 | 601 | 342 | 153 | 57 |
| DoD DCWF v5.1 | 995 | 575 | 291 | 102 |
| DDaT | 58 | 30 | 14 | 2 |
| EU AI Act | 57 | 53 | 42 | 23 |
| NIST AI RMF 1.0 | 69 | 66 | 61 | 44 |

DCWF provides the richest task evidence (102 elements at STS >= 0.60). NIST AI RMF close behind (44). EU AI Act provides 23 high-confidence task mappings.

11 Phase 1A entries (T-001 through T-011): have STRM evidence.
12 post-STRM entries (T-012 through T-023): 0/6 direct coverage — added during prior expansion.

## Duplicate Analysis

4 close pairs examined:

**Pair 1: AG-T-005 (AI impact assessments for new systems) vs AG-T-011 (iterative risk assessment across lifecycle)**
T-005 covers pre-production impact assessment for new or modified systems. T-011 covers ongoing iterative risk assessment throughout the system lifecycle. Pre-deployment gate vs continuous lifecycle activity. EU AI Act distinguishes these (Article 9 initial vs Article 9(2) lifecycle). No merge.

**Pair 2: AG-T-006 (policy compliance monitoring) vs AG-T-007 (bias audits)**
T-006 covers broad policy compliance monitoring across deployed AI systems. T-007 covers specifically bias audits with methodology documentation. Bias audits are a specific type of compliance activity with distinct methodology. No merge.

**Pair 3: AG-T-012 (regulatory-grade documentation) vs AG-T-021 (transparency/disclosure requirements)**
T-012 covers producing comprehensive technical documentation for regulatory compliance. T-021 covers implementing transparency and disclosure specifically (interaction notifications, content labeling). Documentation vs disclosure are distinct governance tasks. No merge.

**Pair 4: AG-T-008 (assessment tools/templates/rubrics) vs AG-T-022 (risk quantification/measurement)**
T-008 covers developing assessment instruments. T-022 covers designing risk quantification approaches and metrics. Tools vs measurement frameworks — one is about creating the instruments, the other about the measurement methodology. No merge.

**Merges: 0**

## Gap Analysis

Synthesis enforcer detected 83 gap signals.

**Top DCWF elements:**
- DCWF 5883 (STS 0.7493): "Evaluate and develop AI workforce structure resources and requirements." Maps to 6 entries. This is a workforce planning task. Already covered indirectly by AG-T-018 (governance literacy and training programs) which includes competency assessment. The workforce structure angle could be a gap, but it sits more naturally in an organizational/HR domain than AG. No new entry — workforce structure development is not a core governance task.

- DCWF 5889 (STS 0.7357): "Identify and submit exemplary AI use cases, best practices, failure modes, and risk mitigation strategies." Maps to 8 entries. Covered by AG-T-008 (assessment tools and rubrics) and AG-T-009 (monitoring regulatory developments). Best practice identification is embedded in governance operations, not a standalone task. No new entry.

- DCWF 5330A (STS 0.7270): "Establish and collect metrics to monitor and validate AI workforce readiness." Maps to 8 entries. Workforce readiness metrics overlap with AG-T-018 (training programs, competency assessment). No new entry.

- DCWF 5882 (STS 0.7242): "Establish/maintain processes to ensure Responsible AI practices." Maps to 6 entries. Covered directly by AG-T-001 (define and maintain enterprise AI governance framework). No new entry.

**Top NIST AI RMF elements:**
- AIRMF-MG-1.4 (STS 0.7926): Residual risk documentation. Maps to T-008, T-009, T-011. Covered by AG-T-011 (iterative risk assessment) which includes residual risk documentation. No new entry.

- AIRMF-MP-1.5 (STS 0.7751): Organizational AI risk tolerance. Maps to 9 entries (broad). Covered by multiple entries — risk tolerance is a cross-cutting concept, not a standalone task. No new entry.

**Entry overload analysis:**
AG-T-010 (259 elements) and AG-T-008 (244 elements) are the highest-loaded entries. T-010 covers operating AI governance review processes (intake, triage, coordination, escalation). T-008 covers developing assessment tools. Both are broad operational tasks. The overload is structural — governance operations attract generic framework elements. No decomposition warranted.

**New entries: 0**

## Post-STRM Validation (T-012 through T-023)

12 entries added during prior expansion. Validated against indirect evidence:

| Entry | Concept | Indirect Evidence |
|-------|---------|-------------------|
| AG-T-012 | Regulatory-grade documentation | EUAIA-O-009 (STS 0.7518 → S-entries; explicit EU AI Act requirement) |
| AG-T-013 | Post-market monitoring systems | EUAIA-O-049 (STS 0.7344 → T-001 through T-011) |
| AG-T-014 | AI incident management | EUAIA-O-047 (STS 0.7238 → S-entries; EU AI Act serious incident requirement) |
| AG-T-015 | Third-party AI risk assessment | AIRMF-MG-3.1 (STS 0.7041 → T-001 through T-011) |
| AG-T-016 | Governing TEVV processes | AIRMF-MS-2.13 (STS 0.7094 → T-003, T-006 through T-011) |
| AG-T-017 | Fundamental rights impact assessment | EUAIA-O-031 (STS 0.6661 → T-entries; EU AI Act explicit requirement) |
| AG-T-018 | Governance training programs | AIRMF-GV-2.2 (STS 0.6024 → T-010); workforce development |
| AG-T-019 | Stakeholder engagement mechanisms | AIRMF-GV-5.1 (STS 0.6264 → T-008, T-010) |
| AG-T-020 | Conformity assessment procedures | EUAIA-O-018 (STS 0.5531 → A-entries; EU AI Act conformity assessment) |
| AG-T-021 | Transparency/disclosure requirements | EUAIA-O-037 (STS 0.7449 → K-entries; EU AI Act transparency obligation) |
| AG-T-022 | Risk quantification/measurement | AIRMF-MS-1.1 (STS 0.6286 → T-001, T-007 through T-011) |
| AG-T-023 | AI system decommissioning governance | AIRMF-GV-1.7 (STS 0.6504 → T-001, T-008); lifecycle completion |

All 12 post-STRM entries retained. Each maps to explicit governance activities defined in EU AI Act or NIST AI RMF.

## Mandatory Checklist

- [x] 1. Duplicate groups: **0 merges from 4 pairs examined.**
- [x] 2. Gap clusters: **4 DCWF clusters + 2 NIST AI RMF clusters analyzed. All covered.**
- [x] 3. Cluster concepts: **Workforce structure, best practices, Responsible AI processes, risk documentation, risk tolerance, overload.**
- [x] 4. New entries: **None — workforce structure tasks sit in organizational domain, not AG. All other concepts already covered.**
- [x] 5. Framework evidence: **Cited per cluster. Top STS: AIRMF-MG-1.4 at 0.7926.**
- [x] 6. Post-STRM validated: **Yes — all 12 entries (T-012 through T-023) validated.**
- [x] 7. Final count: **23 = 11 Phase 1A + 12 post-STRM. 0 merged, 0 new.**
- [x] 8. Count unchanged at 23: **AG Tasks was already expanded from the Phase 1A baseline. The 12 post-STRM entries capture specific governance operational tasks from EU AI Act and NIST AI RMF. Remaining gap signals are either workforce-domain tasks (not AG) or generic DCWF/NICE elements with structural overlap.**

## Final Entry Map

23 Tasks entries: AG-T-001 through AG-T-023.
11 Phase 1A + 12 post-STRM (all validated).
0 merges, 0 new entries.
