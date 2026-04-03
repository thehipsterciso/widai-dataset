# AI Abilities — Phase 1D Synthesis Analysis

**Domain:** AI/ML Foundations (AI)
**Dimension:** Abilities
**Date:** 2026-04-03
**Pre-synthesis count:** 15 (3 Phase 1A baseline + 12 post-STRM additions)
**Post-synthesis count:** 15

## Evidence Summary

- **Total mappings:** 1,097 across 6 frameworks
- **Phase 1A entries (A-001 to A-003):** All have STRM evidence (5/6 to 6/6 coverage)
- **Post-STRM entries (A-004 to A-015):** 0/6 coverage (added after STRM runs)

### High Watermark (unique FDE count at STS thresholds)

| Framework | >=0.45 | >=0.50 | >=0.55 | >=0.60 |
|-----------|--------|--------|--------|--------|
| O*NET 30.2 | 6 | 6 | 5 | 3 |
| NIST NICE v2.1.0 | 53 | 19 | 6 | 1 |
| DoD DCWF v5.1 | 134 | 39 | 8 | 0 |
| DDaT | 15 | 8 | 4 | 0 |
| EU AI Act | 12 | 4 | 0 | 0 |
| NIST AI RMF 1.0 | 11 | 3 | 0 | 0 |

### Strongest STRM Hits

| Entry | FW Cov | Max STS | Top framework evidence |
|-------|--------|---------|----------------------|
| AI-A-001 | 6/6 | 0.6655 | O*NET [1.A.1.c.1] mathematical method selection |
| AI-A-003 | 6/6 | 0.6058 | Various governance/standards elements |
| AI-A-002 | 5/6 | 0.6112 | NICE T1029 evaluation criteria; DCWF [5849] AI value assessment |

## Duplicate Identification (Phase 1A)

Only 3 Phase 1A entries exist. No near-duplicates identified.

**Net effect:** 3 Phase 1A entries, 0 merges = 3 distinct Phase 1A entries

## Post-STRM Entry Evaluation (A-004 to A-015)

| Entry | Concept | Framework evidence (indirect — mapped to A-001/002/003) | Verdict |
|-------|---------|--------------------------------------------------------|---------|
| A-004 | Mathematical/statistical method selection | O*NET [1.A.1.c.1] (0.6655) mathematical methods → A-001 | **KEEP** — distinct from A-001 (ML vs non-ML) |
| A-005 | Pattern recognition in data | O*NET [1.A.1.e.1] pattern organization → S entries; concept supported | **KEEP** — pre-analysis cognitive ability |
| A-006 | Model output interpretation in business context | DCWF [7055] ML output analysis → A-001; [5847] method limitations → A-001 | **KEEP** — distinct from A-005 (post-model vs pre-analysis) |
| A-007 | AI tool/platform applicability assessment | DCWF [3692] analytical tool applicability → A-001 | **KEEP** — distinct operational assessment |
| A-008 | Business-to-AI specification translation | DDaT business needs elements; DCWF requirements entries | **KEEP** — distinct from A-012 (strategy bridging) |
| A-009 | Cost-benefit reasoning for AI | NICE S0850 cost/benefit → A-002; DCWF [600] → A-002 | **KEEP** — broader than A-002 (build/buy) |
| A-010 | Balancing competing AI requirements | EUAIA-O-003 (0.5434) interaction effects → A-003 | **KEEP** — distinct from A-003 (governance) and A-011 (principles) |
| A-011 | Integrating trustworthy AI principles | AIRMF-GV-1.2 (0.5281) trustworthy AI integration → A-003 | **KEEP** — design constraint integration |
| A-012 | Bridging AI capability and org strategy | DDaT strategy elements; DCWF [3979] capabilities → A-003 | **KEEP** — distinct from A-008 (specs) |
| A-013 | Evaluating AI process conformity | NICE S0384 applying standards → A-003; EUAIA-O-022 non-conformity | **KEEP** — compliance evaluation |
| A-014 | Designing automated AI operations | DCWF [4329] automated operations → A-003 | **KEEP** — operational automation design |
| A-015 | Assessing user-AI interaction patterns | DCWF [5921] test user-AI interaction → A-001 | **KEEP** — human factors assessment |

**Net effect:** 12 kept, 0 removed

## Final Count

3 (Phase 1A) + 12 (validated post-STRM) = **15 entries**

## Entry Mapping: Current → Proposed

| Proposed | Source | Action |
|----------|--------|--------|
| AI-A-001 | A-001 | Preserve (ML problem distinction) |
| AI-A-002 | A-002 | Preserve (build vs buy) |
| AI-A-003 | A-003 | Preserve (governance standards) |
| AI-A-004 | A-004 | Preserve (method selection) |
| AI-A-005 | A-005 | Preserve (pattern recognition) |
| AI-A-006 | A-006 | Preserve (model output interpretation) |
| AI-A-007 | A-007 | Preserve (tool applicability) |
| AI-A-008 | A-008 | Preserve (requirements translation) |
| AI-A-009 | A-009 | Preserve (cost-benefit reasoning) |
| AI-A-010 | A-010 | Preserve (balancing requirements) |
| AI-A-011 | A-011 | Preserve (trustworthy AI integration) |
| AI-A-012 | A-012 | Preserve (strategy bridging) |
| AI-A-013 | A-013 | Preserve (conformity evaluation) |
| AI-A-014 | A-014 | Preserve (automated operations) |
| AI-A-015 | A-015 | Preserve (user interaction assessment) |

Note: All entries validated. No changes to the JSON file required — current AI_abilities.json is correct at 15 entries.
