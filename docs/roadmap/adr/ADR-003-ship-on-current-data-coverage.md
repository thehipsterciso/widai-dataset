# ADR-003: Ship on Current Data Coverage

**Status:** Accepted — Validated by R01 (92.2% coverage across 5 archetypes, 2026-03-26)
**Date:** 2026-03-26
**Author:** Thomas Jones / The Hipster CISO
**Derived From:** Ensemble Brainstorm Pass 4 (Constraint Inversion — Constraint 1), Pass 3 (Perspective Rotation — CDAIO Persona)

---

## Context

WIDAI currently has 187 defined roles but only 37 have complete KSA mappings. The remaining 150 are scaffold-only — role definitions without the knowledge, skills, and abilities that enable assessment, gap analysis, and competency evaluation. Schema fields are populated at 10 of 25.

The previous implicit assumption — articulated in the WIDAI Goal Definition — was that the dataset must reach comprehensive completion before products could ship. The Goal Definition's critical path reads: "Full KSA authoring for all 187 roles... Without KSAs, there is no skills gap analysis, no competency assessment, no training path generation, no interview rubric — which means no product."

Constraint Inversion (Pass 4) directly challenged this assumption.

## Decision

**WIDAI will pursue product validation on current data coverage (37 KSA-complete roles across GOV, ENG, DEV, DSM, RSK, OPS, LDR, ANL categories) rather than waiting for full dataset completion.**

This decision is conditional on Tier 0 validation: R01 (coverage gap test mapping 3-5 real team structures against current data) must confirm that current coverage supports a minimum viable assessment. If R01 fails, this decision reverses and the roadmap pivots to accelerated KSA authoring before product work.

## Rationale

**The cost of waiting is measurable.** Every month spent completing the full dataset before piloting is a month of deferred market validation. If the PE due diligence hypothesis is wrong, complete data doesn't save it. If it's right, early piloting generates the revenue and validation to fund completion. The circular dependency breaks by shipping early.

**Current coverage is not randomly distributed.** The 37 KSA-complete roles concentrate in the categories that matter most for a mid-market data/AI team assessment:

| Category | Roles | KSAs | Relevance to UC1 Pilot |
|----------|-------|------|----------------------|
| GOV | 25 | 73 | High — data governance is always assessed |
| ENG | 25 | 53 | High — engineering team is always present |
| DEV | 15 | 46 | High — data science / ML development |
| DSM | 21 | 38 | Medium — data stewardship and management |
| RSK | 24 | 35 | Medium — risk roles in financial services targets |
| OPS | 15 | 23 | Medium — operational roles |
| LDR | 31 | 24 | Medium — leadership assessment |
| ANL | 14 | 30 | Medium — analytics team |

A mid-market data/AI team of 15-30 people maps to approximately 20-40 WIDAI roles. The categories with KSA coverage account for the majority of those roles.

**The CDAIO persona confirmed this.** Pass 3's newly hired CDAIO persona articulated: "I don't need perfect coverage. I need useful coverage for the roles I actually have." And: "If WIDAI could give me a quick assessment tool that maps my current team in under a day... I'd pay for that today. Before the taxonomy is complete. Before the API exists."

**Piloting generates authoring priority data.** The gap between current coverage and what a real assessment requires is the most valuable input for KSA authoring prioritization. Without a pilot, authoring priority is guesswork. With a pilot, every unmapped role becomes a prioritized backlog item with real-world evidence of its importance.

### What "Ship" Means

Ship does not mean "release WIDAI as complete." It means:

- Run a PE assessment pilot using current data
- Document coverage gaps encountered during the pilot
- Present results with explicit confidence intervals (high confidence for roles with KSAs, lower for scaffold-only roles)
- Use gap data to prioritize R08 (KSA authoring for priority roles)

## Consequences

**Positive:**
- Compresses time-to-market from 6-12 months (full completion) to 4-8 weeks (Tier 0 validation + Tier 1 first product)
- Generates empirical data about what the market actually needs, rather than authoring in anticipation
- Creates revenue opportunity that funds completion work
- Reduces the risk of building a complete dataset that misses what the market values

**Negative:**
- The first pilot will have visible gaps — roles assessed without KSA backing produce lower-fidelity output
- Risk of credibility damage if gaps are not transparently communicated ("your taxonomy only covers 70% of my team")
- Creates pressure to rush KSA authoring for gap-fill, potentially reducing quality

**Risks:**
- R01 (coverage gap test) reveals current data covers less than 60% of a typical team. Mitigation: if coverage is below 60%, execute a focused KSA sprint on the 10-15 highest-frequency roles before piloting (adds 2-4 weeks, not 6 months).
- Pilot partner perceives gaps as lack of rigor. Mitigation: frame the pilot as a "validation engagement" with transparent methodology documentation, not a finished product.

## Validation Results

**R01 Execution (2026-03-26):** Coverage Gap Test validated the hypothesis that current data supports pilot assessments.

- **Result:** PASS
- **Coverage Metric:** 92.2% KSA coverage across 5 reference archetypes (CISO/Risk, Data Engineering Lead, Chief Data Officer, AI Risk Officer, Data Steward)
- **Evidence:** All 5 archetypes map primarily to GOV, ENG, DEV, DSM, RSK, OPS, LDR, ANL categories — the exact categories with complete KSA coverage
- **Implication:** A mid-market data/AI team assessment (15-40 roles) encounters minimal scaffolding. The assumption that current coverage is sufficient for product validation is confirmed.

This validation removes the conditional dependency on ADR-003. The decision to "ship on current data" proceeds as planned. Phase 1 (First Product — PE due diligence assessment) is cleared for execution.

## References

- Ensemble Brainstorm — WIDAI Roadmap, Pass 4: Constraint 1 ("The dataset must be complete before products ship")
- Ensemble Brainstorm — WIDAI Roadmap, Pass 3: CDAIO Persona D
- Ensemble Brainstorm — WIDAI Roadmap, Pass 4: Assumption Test Queue (R01 as immediate test)
- WIDAI Goal Definition, Critical Path section
- WIDAI dataset: current KSA distribution across 8 categories
- Phase 0 Validation Sprint Results: `docs/roadmap/PHASE-0-VALIDATION-SPRINT-RESULTS.md`
- R01 Coverage Gap Test: `docs/roadmap/R01-coverage-gap-test.md`
