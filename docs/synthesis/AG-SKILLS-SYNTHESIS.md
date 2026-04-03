# AG Skills — Phase 1D Synthesis Analysis

**Domain:** AI Governance & Ethics (AG)
**Dimension:** Skills
**Date:** 2026-04-03
**Pre-synthesis count:** 20 (8 Phase 1A baseline + 12 post-STRM additions)
**Post-synthesis count:** 19

## Evidence Summary

- **Total mappings:** 16,686 across 6 frameworks
- **Phase 1A entries (S-001 to S-008):** All have STRM evidence (6/6 coverage)
- **Post-STRM entries (S-009 to S-020):** 0/6 coverage (added after STRM runs)

### High Watermark (unique FDE count at STS thresholds)

| Framework | >=0.45 | >=0.50 | >=0.55 | >=0.60 |
|-----------|--------|--------|--------|--------|
| O*NET 30.2 | 18 | 7 | 1 | 0 |
| NIST NICE v2.1.0 | 901 | 592 | 337 | 157 |
| DoD DCWF v5.1 | 1,393 | 926 | 490 | 192 |
| DDaT | 96 | 61 | 26 | 3 |
| EU AI Act | 61 | 60 | 57 | 51 |
| NIST AI RMF 1.0 | 70 | 70 | 70 | 68 |

### Strongest STRM Hits

| Entry | Strong | Max STS | Top framework evidence |
|-------|--------|---------|----------------------|
| AG-S-008 | 17 | 0.7869 | EUAIA-O-042 downstream integration documentation |
| AG-S-005 | 8 | 0.7372 | AIRMF-MS-2.11 fairness/bias evaluation |
| AG-S-002 | 6 | 0.7270 | EUAIA-O-001 AI risk management system design |
| AG-S-007 | 2 | 0.8104 | AIRMF-GV-3.2 human-AI interaction governance |
| AG-S-004 | 2 | 0.7174 | AIRMF-MG-2.4 feedback incorporation systems |
| AG-S-006 | 1 | 0.7107 | AIRMF-MS-2.11 fairness/bias evaluation |
| AG-S-001 | 0 | 0.6843 | O*NET [2.C.8.a] security policies/strategies |
| AG-S-003 | 0 | 0.6673 | DCWF [3987] intelligence process conceptualization |

## Duplicate Identification (Phase 1A)

No near-duplicate entries identified within the Phase 1A baseline. All 8 entries have distinct functional focus:

- S-001: Governance council operations (organizational structures, decision rights)
- S-002: Lifecycle governance framework design
- S-003: Risk communication to non-technical audiences
- S-004: Governance review process management (intake, triage, coordination)
- S-005: AI impact assessments (risk tiering, harm, bias)
- S-006: Bias audit design and execution
- S-007: Human oversight mechanism design
- S-008: AI system documentation (model cards, system cards, datasheets)

**Net effect:** 8 Phase 1A entries, 0 merges = 8 distinct Phase 1A entries

## Post-STRM Entry Evaluation (S-009 to S-020)

| Entry | Concept | Framework evidence | Verdict |
|-------|---------|-------------------|---------|
| S-009 | Regulatory-grade AI documentation | EUAIA-O-009 (0.7518) technical documentation; EUAIA-O-041 (0.7469) GPAI docs | **MERGE with S-008** — both cover AI system documentation; S-009 adds regulatory specificity (EU AI Act, NIST standards, conformity assessment evidence) |
| S-010 | Iterative AI risk assessment | EUAIA-O-002 (0.6978) iterative risk assessment; AIRMF-MG-1.2 (0.6868) risk prioritization | **KEEP** — lifecycle risk assessment process, distinct from S-005 (impact assessment as discrete activity) |
| S-011 | Post-market monitoring systems | EUAIA-O-049 (0.7289) post-market monitoring; EUAIA-O-050 (0.6489) performance data | **KEEP** — distinct operational concept |
| S-012 | AI quality management systems | EUAIA-O-019 (0.7139) QMS design; EUAIA-O-004 (0.7119) test protocols | **KEEP** — distinct from governance frameworks (S-002) |
| S-013 | AI incident management | EUAIA-O-047 (0.7238) incident management; EUAIA-O-052 (0.6954) incident investigation | **KEEP** — distinct concept |
| S-014 | Third-party AI risk monitoring | AIRMF-MG-3.1 (0.7101) third-party monitoring; AIRMF-GV-6.2 (0.6438) contingency planning | **KEEP** — distinct concept |
| S-015 | Risk tracking infrastructure | AIRMF-MS-3.1 (0.7057) risk tracking; AIRMF-MS-3.2 (0.6470) proxy indicators | **KEEP** — tracking infrastructure, distinct from S-010 (assessment process) |
| S-016 | TEVV effectiveness evaluation | AIRMF-MS-2.13 (0.7051) TEVV effectiveness; AIRMF-MP-3.4 (0.7004) TEVV trade-offs | **KEEP** — distinct concept |
| S-017 | Stakeholder feedback/engagement | AIRMF-MG-2.4 (0.7174) feedback systems; AIRMF-GV-5.2 (0.6893) engagement practices | **KEEP** — distinct concept |
| S-018 | Fundamental rights impact assessment | EUAIA-O-032 (0.6524) FRIA; EUAIA-O-031 (0.6708) DPIA for AI | **KEEP** — specific rights-focused assessment, distinct from S-005 (general impact) |
| S-019 | Transparency/accountability evaluation | AIRMF-MS-2.8 (0.6968) transparency risks; EUAIA-O-012 (0.6895) transparency design | **KEEP** — distinct concept |
| S-020 | AI system inventory/classification | AIRMF-GV-1.6 (0.6992) system inventory; EUAIA-O-053 (0.6744) risk classification | **KEEP** — distinct operational skill |

**Net effect:** 11 kept, 1 merged into Phase 1A S-008

## Final Count

8 (Phase 1A, no internal duplicates) + 11 (validated post-STRM) = **19 entries**

Note: S-009 content (regulatory-grade specificity) merged into S-008, enriching the documentation skill to cover both internal governance and regulatory conformity assessment requirements.

## Entry Mapping: Current → Proposed

| Proposed | Source | Action |
|----------|--------|--------|
| AG-S-001 | S-001 | Preserve (governance council operations) |
| AG-S-002 | S-002 | Preserve (lifecycle governance framework design) |
| AG-S-003 | S-003 | Preserve (risk communication) |
| AG-S-004 | S-004 | Preserve (governance review processes) |
| AG-S-005 | S-005 | Preserve (AI impact assessments) |
| AG-S-006 | S-006 | Preserve (bias audit design/execution) |
| AG-S-007 | S-007 | Preserve (human oversight mechanisms) |
| AG-S-008 | S-008 + S-009 | Merge (AI system documentation + regulatory-grade documentation) |
| AG-S-009 | S-010 | Renumber (iterative risk assessment) |
| AG-S-010 | S-011 | Renumber (post-market monitoring) |
| AG-S-011 | S-012 | Renumber (quality management systems) |
| AG-S-012 | S-013 | Renumber (incident management) |
| AG-S-013 | S-014 | Renumber (third-party AI risk) |
| AG-S-014 | S-015 | Renumber (risk tracking infrastructure) |
| AG-S-015 | S-016 | Renumber (TEVV effectiveness) |
| AG-S-016 | S-017 | Renumber (stakeholder feedback/engagement) |
| AG-S-017 | S-018 | Renumber (fundamental rights impact assessment) |
| AG-S-018 | S-019 | Renumber (transparency/accountability evaluation) |
| AG-S-019 | S-020 | Renumber (AI system inventory/classification) |
