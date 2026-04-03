# AI/ML Foundations — Abilities Dimension Synthesis

**Domain**: AI (AI/ML Foundations)
**Dimension**: Abilities
**Date**: 2026-04-03
**Schema**: 3.0.0
**Starting count**: 15 (AI-A-001 through AI-A-015)

---

## Evidence Summary

| Metric | Value |
|--------|-------|
| Total STRM mappings | 1,097 |
| Framework elements at STS ≥ 0.50 | 58 |
| Framework elements at STS ≥ 0.55 | 11 |
| Framework elements at STS ≥ 0.60 | 2 |

Evidence is sparse because abilities are abstract cognitive/judgment concepts that do not map cleanly to the specific competency elements described in NICE, DCWF, and other frameworks. This is structurally expected — abilities describe "how someone reasons" rather than "what they know or can do," and no source framework uses this abstraction level consistently.

Only 3 entries attract any elements at STS ≥ 0.55:

| Entry | Elements (≥ 0.55) | Max STS |
|-------|-------------------|---------|
| AI-A-003 (governance across heterogeneous systems) | 5 | — |
| AI-A-001 (ML vs rule-based problem selection) | 4 | 0.6655 |
| AI-A-002 (build-vs-buy evaluation) | 2 | 0.6112 |

---

## Duplicate Analysis

Examined all 15 entries for overlapping scope.

### Pair 1: AI-A-001 (ML vs rule-based selection) vs AI-A-004 (mathematical method selection)

- A-001: choosing whether a problem needs ML at all
- A-004: choosing which mathematical method is appropriate once ML is selected

Sequential in the reasoning chain, not overlapping. Different decision points.

**Decision**: KEEP SEPARATE.

### Pair 2: AI-A-008 (translate business to AI specs) vs AI-A-012 (bridge tech and strategy)

- A-008: translating business requirements into actionable AI system specifications (data reqs, model reqs, eval criteria)
- A-012: translating between what AI can do and what the org needs, at appropriate abstraction for each audience

A-008 is technical decomposition (requirements → specs). A-012 is communication bridging (tech ↔ strategy). Different cognitive functions.

**Decision**: KEEP SEPARATE.

### Pair 3: AI-A-010 (balancing competing requirements) vs AI-A-011 (integrating trustworthy AI principles)

- A-010: making trade-offs when performance, safety, fairness, transparency, cost conflict
- A-011: holding all trustworthy AI principles as simultaneous design constraints

These are closely related — both involve managing multiple AI requirements simultaneously. However, A-010 is about explicit trade-off decisions when requirements conflict. A-011 is about maintaining principles as constraints throughout design. The distinction is "conflict resolution" vs "constraint integration."

**Decision**: KEEP SEPARATE. Different cognitive operations confirmed by NIST AI RMF treating requirement trade-offs (AIRMF-MP-3.4) and trustworthy principle integration (AIRMF-GV-1.2) as separate competencies.

### Result: 0 duplicate merges

---

## Gap Analysis

The synthesis enforcer detected **0 automated gap signals**. Only 2 framework elements exceed STS 0.60:

1. O*NET [1.A.1.c.1] (STS=0.6655): "The ability to choose the right mathematical methods or formulas to solve a problem" → maps to AI-A-001. Covered.

2. NICE [T1029] (STS=0.6112): "Implement organizational evaluation and validation criteria" → maps to AI-A-002. Covered.

With only 11 elements at STS ≥ 0.55 across all frameworks, the evidence simply does not support expansion. The abilities dimension has structurally lower framework alignment because:

1. Source frameworks (NICE, DCWF, DDaT) describe competencies primarily as Knowledge, Skills, and Tasks
2. O*NET is the only framework with explicit "Ability" categorization, and its coverage yields only 6 elements at STS ≥ 0.45
3. EU AI Act and NIST AI RMF frame requirements as skills/knowledge, not abilities

The 15 current entries cover a comprehensive range of AI-related judgment capabilities: problem selection (A-001), platform decisions (A-002), governance (A-003), method selection (A-004), pattern recognition (A-005), output interpretation (A-006), tool assessment (A-007), requirements translation (A-008), cost-benefit reasoning (A-009), requirement trade-offs (A-010), trustworthy AI integration (A-011), strategy bridging (A-012), compliance evaluation (A-013), automated operations reasoning (A-014), and user interaction assessment (A-015).

**Result**: 0 new entries. Evidence does not support expansion.

---

## Post-STRM Entry Validation

Looking at the evidence matrix, entries A-004 through A-015 have zero or near-zero direct STRM evidence. However, all 15 entries are treated as a coherent set that was designed to represent the judgment/reasoning dimension of AI competency. The sparse evidence is structural (frameworks don't describe abilities well), not an indicator that these concepts are invalid. Each entry describes a judgment capability that logically complements the Knowledge and Skills dimensions.

All entries retained based on structural coherence rather than direct STRM evidence, which is appropriate for the Abilities dimension.

---

## Mandatory Checklist

- [x] 1. Duplicate groups: **0**. 3 pairs examined, all differentiated.
- [x] 2. Gap clusters: **0**. Only 2 framework elements at STS ≥ 0.60; 0 automated gap signals.
- [x] 3-5. No new entries needed.
- [x] 6. Post-STRM entries: structural validation — abilities are cognitive concepts not well-represented in source frameworks.
- [x] 7. Final count: **15**. No merges, no additions.
- [x] 8. Count unchanged at 15. No gaps warranted because: (a) only 11 elements at STS ≥ 0.55 across all 6 STRMs — insufficient evidence density to identify concept gaps; (b) abilities are structurally sparse in all source frameworks; (c) current 15 entries provide comprehensive cognitive coverage across AI decision-making domains.

---

## Final Entry Map

All 15 entries preserved as-is. No renumbering required.
