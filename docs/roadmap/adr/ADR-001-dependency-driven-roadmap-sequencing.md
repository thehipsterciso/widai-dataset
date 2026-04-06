# ADR-001: Dependency-Driven Roadmap Sequencing

**Status:** Proposed
**Date:** 2026-03-26
**Author:** Thomas Jones / The Hipster CISO
**Derived From:** Ensemble Brainstorm Pass 1 (Forward Decomposition), Pass 4 (Constraint Inversion), Scoring Layer

---

## Context

WIDAI has six use cases scored at high Strategic Opportunity Index (15-20/25 each). Traditional product roadmapping would prioritize by impact or revenue potential — which would suggest pursuing all five 20/25-scored use cases simultaneously or picking the one with the most executive appeal.

The five-pass analysis surfaced a structural problem with priority-based sequencing: the use cases share foundational dependencies but diverge in their specific requirements. UC1 (PE Due Diligence) needs role coverage and a scoring model. UC2 (EU AI Act) needs regulatory context fields. UC3 (Model Risk Governance) needs RSK category depth. UC4 (Agentic AI) needs entirely new roles. UC5 (CDAIO Toolkit) depends on components from UC1-UC3.

A priority-ranked roadmap creates either serialization (do one thing at a time, each taking months) or fragmentation (start five things, finish none). Neither serves a solo-operator project with a finite execution window.

## Decision

**Sequence the WIDAI roadmap by structural dependency chains, not by use case priority or strategic value.**

The roadmap is organized into five topological tiers:

- **Tier 0 — Validation tests** that determine the roadmap itself (R01 coverage gap test, R02 AI-assisted KSA quality test, R05 license audit, R24 KSA quality audit). These run first because their outcomes change the shape of everything downstream.
- **Tier 1 — First product foundations** (R03 pilot partner, R04 assessment methodology, R07 regulatory context, R12 methodology documentation). These build the beachhead product.
- **Tier 2 — Product delivery + compliance** (R06 EU AI Act mapping, R08 priority KSAs, R11 cross-regulatory analysis, R14 practitioner validation, R25 assessment interface). These run concurrently with the first pilot.
- **Tier 3 — Expansion** (R09 SR 11-7 org design, R10 agentic AI roles, R15 CDAIO toolkit, R22 NICHE/REG KSAs). Informed by pilot results.
- **Tier 4 — Scale infrastructure** (R19 API, R20 Neo4j pipeline, R23 validation tooling). Funded by earlier phases.

A separate Watch List tracks trigger-dependent items (R13, R16, R17, R18, R21) that activate when external conditions are met rather than on a schedule.

## Rationale

The Ensemble Brainstorm's Forward Decomposition (Pass 1) mapped what each use case requires to function. Reverse Induction (Pass 2) identified failure modes — several of which stem from trying to build complete capability before validating the underlying hypothesis. Constraint Inversion (Pass 4) tested the assumption that the dataset must be complete before products ship, and found it false: current data likely supports a pilot assessment.

The dependency chain emerged from topological sorting of these relationships. Items in each tier depend only on items in prior tiers. This means:

1. **No wasted work.** Tier 0 validation tests can invalidate assumptions before Tier 1 investment. If the coverage gap test (R01) shows current data can't support even a narrow pilot, the roadmap pivots to KSA completion first — before building assessment methodology.
2. **Parallel execution within tiers.** Items in the same tier have no dependencies on each other, enabling concurrent work.
3. **Natural funding sequence.** Each tier produces something that funds the next. Tier 1 produces a pilot. The pilot produces revenue and validation. Revenue funds Tier 2 partnerships. Validation informs Tier 3 scope.

## Consequences

**Positive:**
- Prevents the "complete the dataset" serialization trap that could consume 6-12 months before any market validation
- Creates natural decision gates — each tier's output informs whether to proceed, pivot, or pause
- Respects the solo-operator constraint by limiting work-in-progress at each stage

**Negative:**
- Use cases with independent urgency (UC2's August 2026 EU AI Act deadline) may feel under-served by waiting for Tier 0 completion — mitigated by running Tier 0 as a 2-week sprint, not a months-long phase
- The Watch List items lack clear activation timelines, creating a risk of indefinite deferral — mitigated by reviewing Watch List triggers at each tier transition

**Risks:**
- If Tier 0 validation tests produce ambiguous results, the roadmap stalls at the decision gate. Mitigation: define clear pass/fail criteria for each test before running them.

## References

- Ensemble Brainstorm — WIDAI Roadmap, Scoring and Classification section (25 scored items)
- Ensemble Brainstorm — WIDAI Roadmap, Dependency Chain (Topological Sort)
- Ensemble Brainstorm — WIDAI Roadmap, Roadmap Summary (Phase 0-4)
