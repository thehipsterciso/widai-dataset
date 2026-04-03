# AG Abilities — Phase 1D Synthesis Analysis

**Domain:** AI Governance & Ethics (AG)
**Dimension:** Abilities
**Date:** 2026-04-03
**Pre-synthesis count:** 15 (4 Phase 1A baseline + 11 post-STRM additions)
**Post-synthesis count:** 15 (no changes)

## Evidence Summary

- **Total mappings:** 3,839 across 6 frameworks
- **Phase 1A entries (A-001 to A-004):** All have STRM evidence (A-001, A-002, A-004 at 6/6; A-003 at 5/6)
- **Post-STRM entries (A-005 to A-015):** 0/6 coverage (added after STRM runs)

### High Watermark (unique FDE count at STS thresholds)

| Framework | >=0.45 | >=0.50 | >=0.55 | >=0.60 |
|-----------|--------|--------|--------|--------|
| O*NET 30.2 | 10 | 4 | 2 | 0 |
| NIST NICE v2.1.0 | 287 | 111 | 36 | 3 |
| DoD DCWF v5.1 | 443 | 194 | 67 | 15 |
| DDaT | 36 | 26 | 17 | 6 |
| EU AI Act | 37 | 26 | 13 | 3 |
| NIST AI RMF 1.0 | 65 | 58 | 30 | 12 |

### Strongest STRM Hits

| Entry | Strong | Max STS | Top framework evidence |
|-------|--------|---------|----------------------|
| AG-A-004 | 0 | 0.6888 | AIRMF-MS-4.2 integrate measurement into risk decisions |
| AG-A-001 | 0 | 0.6410 | EUAIA-O-049 post-market monitoring systems |
| AG-A-003 | 0 | 0.6317 | DDaT SK-150 organisational data strategy |
| AG-A-002 | 0 | 0.6296 | DDaT SK-064 risk governance processes |

Note: Abilities as a dimension consistently show lower STS scores than Knowledge or Skills due to their higher-order cognitive framing. Zero "strong" hits (STS >= 0.70) is expected — abilities describe capacity to apply knowledge and skills, which maps less directly to framework element descriptions.

## Duplicate Identification (Phase 1A)

No near-duplicate entries identified within the Phase 1A baseline. All 4 entries have distinct functional focus:

- A-001: Risk-proportional governance calibration
- A-002: Ethical trade-off navigation (fairness vs accuracy, transparency vs privacy)
- A-003: Building organizational commitment through business value demonstration
- A-004: Translating emerging research, regulation, and societal expectations into policy

**Net effect:** 4 Phase 1A entries, 0 merges = 4 distinct Phase 1A entries

## Post-STRM Entry Evaluation (A-005 to A-015)

| Entry | Concept | Framework evidence | Verdict |
|-------|---------|-------------------|---------|
| A-005 | Multi-framework requirement synthesis | NICE T0220 (0.6150) resolve regulatory conflicts; DCWF 834 (0.6054) same; AIRMF-GV-1.2 (0.6782) trustworthy AI principle integration | **KEEP** — distinct cross-framework harmonization ability |
| A-006 | Evidence-driven governance decision-making | AIRMF-MS-4.2 (0.6888) integrate measurements into risk decisions; DCWF 5902 (0.6330) monitor/evaluate AI use | **KEEP** — quantitative integration into governance |
| A-007 | Stakeholder conflict mediation | DCWF 4055 (0.5859) resolve conflicting requirements; AIRMF-MG-2.3 (0.5371) stakeholder engagement | **KEEP** — distinct interpersonal/organizational ability |
| A-008 | Governance-operation divergence detection | DCWF 5902 (0.6330) monitor AI use; AIRMF-MS-2.4 (0.5828) production monitoring | **KEEP** — gap detection between intent and reality |
| A-009 | Second-order governance effect anticipation | DCWF 7061 (0.6879) policy/strategy; AIRMF-MP-3.5 (0.5064) impact assessment | **KEEP** — systemic thinking ability |
| A-010 | Governance adaptation to emerging capabilities | DCWF 1070A (0.6185) monitor emerging tech impact; AIRMF-GV-1.5 (0.5442) monitoring/review | **KEEP** — adaptive governance ability |
| A-011 | Governance effectiveness evaluation | AIRMF-MS-1.2 (0.6342) evaluate measurement effectiveness; DCWF 5849 (0.5573) assess AI project value | **KEEP** — evidence-based governance assessment |
| A-012 | Cross-boundary governance coordination | AIRMF-GV-2.1 (0.6058) roles/responsibilities; DCWF 5882 (0.5923) responsible AI processes | **KEEP** — organizational coordination ability |
| A-013 | Multi-audience governance communication | DDaT SK-030 (0.5552) technical/non-technical communication; DCWF 5869 (0.5597) demonstrate to stakeholders | **KEEP** — communication adaptation ability |
| A-014 | Governance continuity through change | AIRMF-MG-2.2 (0.5508) sustain AI value; DCWF 5892 (0.5837) lead through change | **KEEP** — organizational resilience ability |
| A-015 | Rigor-velocity balance | DCWF 7061 (0.6879) policy/strategy; related to A-001 but distinct angle (speed vs risk calibration) | **KEEP** — velocity-focused vs A-001's risk-focused framing |

**Net effect:** 11 kept, 0 merged

## Final Count

4 (Phase 1A, no internal duplicates) + 11 (validated post-STRM) = **15 entries** (no change)

No JSON rewrite required. Current AG_abilities.json is validated as-is.
