# ADR-010: Validation Sprint (Tier 0) Before Product Build

**Status:** Accepted — Sprint executed 2026-03-26. All four tests complete. See PHASE-0-VALIDATION-SPRINT-RESULTS.md.
**Date:** 2026-03-26
**Closed:** 2026-03-26
**Author:** Thomas Jones / The Hipster CISO
**Derived From:** Ensemble Brainstorm Pass 4 (Constraint Inversion — Assumption Test Queue), Scoring Layer (Tier 0 items)

---

## Context

The Ensemble Brainstorm produced a roadmap with 25 scored items organized into dependency tiers. The analysis revealed that several foundational assumptions remain untested — and the shape of the entire roadmap depends on whether those assumptions hold.

Four items scored as Roadmap Anchors share a common characteristic: they are tests, not deliverables. Their purpose is to produce information that determines how subsequent tiers should be executed, or whether they should be executed at all.

## Decision

**The roadmap begins with a 2-week Validation Sprint (Tier 0) that runs four parallel tests before any product build work begins. The results of these tests are decision gates that may reshape Tiers 1-4.**

### The Four Tests

**R01: Coverage Gap Test**
Map 3-5 real data/AI team structures against current WIDAI data coverage. Use publicly available team structures, Thomas's network contacts, or anonymized organizational data. The question: can the current 37 KSA-complete roles support a minimum viable PE assessment?

- **If yes (≥60% role coverage):** Proceed to Tier 1 with current data (ADR-003 holds)
- **If no (<60% coverage):** Insert a focused KSA sprint targeting the 10-15 highest-frequency unmapped roles before Tier 1. This adds 2-4 weeks but prevents a failed pilot.

**R02: AI-Assisted KSA Quality Test**
Author KSAs for 5 roles using AI assistance. Blind-compare against manually-authored KSAs on completeness, source framework accuracy, style consistency, and assessment utility.

- **If quality is comparable:** Adopt AI-assisted workflow for all remaining roles (ADR-005 holds). KSA completion timeline compresses from months to weeks.
- **If quality falls short:** Identify failure modes. Determine if failures are systematic (abandon AI-assisted approach) or limited to specific role types (hybrid approach — AI for standard roles, manual for complex roles).

**R05: Source Framework License Audit**
Audit licensing terms for all 70+ source frameworks. WIDAI derives from O*NET (public domain), NICE (public domain), SFIA (copyrighted), DAMA DMBOK (copyrighted), ESCO (EU open data), and others. Determine which frameworks permit commercial derivative works and under what conditions.

- **If all clear:** Proceed with current cross-framework architecture
- **If restrictions found:** Determine scope of restrictions. If a major framework (SFIA, DAMA) restricts commercial use, the cross-framework mapping may need to exclude those sources or negotiate licensing. This affects the differentiator positioning (ADR-006).

**R24: KSA Quality Consistency Audit**
Review existing 37 KSA-complete roles for consistency. Are KSAs authored to the same standard across categories? Do GOV KSAs (73 entries, likely authored first) match the quality of later categories? Are there systematic patterns (e.g., later categories are thinner, or earlier categories use different terminology)?

- **If consistent:** The existing KSAs are a reliable benchmark for AI-assisted authoring (R02 depends on this)
- **If inconsistent:** Normalize the existing set before using it as a reference for scaled authoring. This is cheaper to fix now than after 150 additional roles inherit the inconsistencies.

### Why These Four, and Why Now

These four tests were selected because they share a critical property: their outcomes change the roadmap. Not refine it, not improve it — change it. A coverage gap test showing 40% coverage doesn't just slow the timeline; it restructures Tier 1 from "build assessment methodology" to "author 30 KSA sets first." A license audit finding that SFIA prohibits commercial derivatives doesn't just add a task; it potentially removes the cross-framework differentiator.

Running these tests before committing to Tier 1 work prevents:

1. Building a PE assessment methodology on a dataset that can't support it
2. Scaling an AI-assisted authoring process from an inconsistent reference set
3. Commercializing a product that infringes framework copyrights
4. Discovering these issues after months of downstream work

### Sprint Design

All four tests run in parallel during Weeks 1-2:

| Test | Effort | Dependencies | Output |
|------|--------|-------------|--------|
| R01: Coverage gap | 2-3 days | Access to real team structures (Thomas's network, public data) | Go/no-go for Tier 1 on current data |
| R02: AI-assisted KSA | 3-4 days | R24 ideally complete first (but can start in parallel) | Go/no-go for AI-assisted authoring |
| R05: License audit | 2-3 days | Access to framework licensing terms | Commercial viability confirmation |
| R24: KSA consistency | 2-3 days | None | Quality baseline for authoring |

Total: 2 weeks of parallel execution. No sequential dependencies between R01, R05, and R24. R02 benefits from R24 results but can start simultaneously.

## Rationale

**The Ensemble Brainstorm methodology specifically calls for testing assumptions before building.** Pass 4 (Constraint Inversion) exists to surface assumptions masquerading as facts. Three of the four tests emerged directly from Pass 4. The fourth (R24) emerged from the scoring layer when existing data quality was flagged as an unverified assumption.

**Two weeks is cheap insurance.** The alternative — proceeding to Tier 1 without validation and discovering issues mid-build — costs 4-8 weeks of rework and damages momentum. The Validation Sprint trades 2 weeks of focused testing for confidence in every subsequent decision.

**Decision gates create accountability.** Each test has explicit pass/fail criteria and documented consequences for each outcome. This prevents the common failure mode of "tests that produce data nobody acts on." If R01 shows 45% coverage, the roadmap restructures. There is no ambiguity about what the result means.

## Consequences

**Positive:**
- Prevents building on unvalidated assumptions — the most expensive category of project failure
- Produces concrete evidence for every ADR that depends on foundational assumptions (ADR-003, ADR-005, ADR-006)
- Two weeks is short enough to maintain momentum, long enough to produce reliable results
- Parallel execution means the sprint doesn't serialize the roadmap

**Negative:**
- Delays Tier 1 by 2 weeks. For UC2 (EU AI Act), this compresses an already tight timeline to August 2026. Mitigated by the fact that Tier 1 regulatory context work (R07) is more efficient when the quality baseline (R24) is known.
- Tests may produce ambiguous results. "Coverage is 55% — is that enough?" requires judgment, not just data.

**Risks:**
- Multiple tests produce negative results simultaneously (e.g., R01 shows low coverage AND R05 finds license restrictions AND R24 finds quality inconsistencies). This would require a substantial roadmap restructure. Mitigation: this is exactly why Tier 0 exists — better to know in Week 2 than in Week 16.
- The Validation Sprint becomes a procrastination mechanism — "we need more data before we can act." Mitigation: hard 2-week timebox. Tests produce results with the data available, not with perfect data.

## Execution Results (2026-03-26)

All four tests executed in parallel on Day 1 of the sprint. Results:

| Test | Result | Gate Threshold | Outcome |
|------|--------|----------------|---------|
| R01: Coverage Gap | PASS (92.2%) | ≥60% KSA coverage | Proceed to Tier 1 on current data |
| R02: AI-Assisted KSA | PASS (4.26/5) | Quality comparable | Adopt AI-assisted workflow |
| R05: License Audit | CONDITIONAL (19G/28Y/23R) | No blockers | GREEN frameworks safe; dependency analysis needed |
| R24: KSA Consistency | PASS WITH CONDITIONS (8.2/10) | Consistent baseline | Proceed; document Ability type decision |

**Roadmap impact:** Tier 1 is unblocked. Three conditions documented in PHASE-0-VALIDATION-SPRINT-RESULTS.md must be addressed during Tier 1 execution:
1. RED framework dependency analysis (R05 follow-up)
2. Ability type design decision (R24 follow-up)
3. Thomas reviews R02 AI-authored KSAs (independent quality validation)

**Detailed results:** See `docs/roadmap/PHASE-0-VALIDATION-SPRINT-RESULTS.md` and individual test reports (R01, R02, R05, R24) in the same directory.

## References

- Ensemble Brainstorm — WIDAI Roadmap, Pass 4: Assumption Test Queue (5 prioritized tests)
- Ensemble Brainstorm — WIDAI Roadmap, Scoring: R01, R02, R05, R24 (all Roadmap Anchors)
- Ensemble Brainstorm — WIDAI Roadmap, Dependency Chain: Tier 0
- Ensemble Brainstorm — WIDAI Roadmap, Roadmap Summary: Phase 0 (Validation Sprint)
