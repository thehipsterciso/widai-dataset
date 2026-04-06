# WIDAI Architectural Decision Records

**Date:** 2026-03-26
**Author:** Thomas Jones / The Hipster CISO
**Source:** Ensemble Brainstorm — Five-Pass Algorithm for Strategic Thinking, applied to WIDAI roadmap

---

## What This Is

These Architectural Decision Records document the reasoning behind every major roadmap decision for the WIDAI project. Each ADR captures: what was decided, why, what alternatives were considered, and what the consequences are — including risks the decision creates.

The ADRs are derived from a systematic five-pass analysis (Forward Decomposition, Reverse Induction, Perspective Rotation, Constraint Inversion, Second-Order Mapping) conducted against WIDAI's six priority use cases, supported by five parallel research briefs covering PE due diligence, EU AI Act compliance, model risk governance, agentic AI workforce design, and competitive taxonomy landscape.

**Status:** ADRs 001–010 are Proposed (pre-Phase 0). ADRs 011–015 are Accepted and executed.

---

## ADR Index

| ADR | Title | Core Decision | Status |
|-----|-------|--------------|--------|
| [ADR-001](ADR-001-dependency-driven-roadmap-sequencing.md) | Dependency-Driven Roadmap Sequencing | Sequence by structural dependencies (Tier 0-4), not by priority ranking | Proposed |
| [ADR-002](ADR-002-pe-due-diligence-as-beachhead.md) | PE Due Diligence as Beachhead Product | PE workforce assessment is the first product — cascading adoption + audience alignment + data readiness | Proposed |
| [ADR-003](ADR-003-ship-on-current-data-coverage.md) | Ship on Current Data Coverage | Pilot on 37 KSA-complete roles rather than waiting for full 187-role completion | Proposed |
| [ADR-004](ADR-004-eu-ai-act-timeline-urgency.md) | EU AI Act as Urgent Parallel Track | Compliance role mapping targets July 2026 delivery — foundational work starts in Tier 1, product in Tier 2 | Proposed |
| [ADR-005](ADR-005-ai-assisted-ksa-authoring.md) | AI-Assisted KSA Authoring | AI drafts + Thomas reviews = 3-5x authoring speedup, contingent on quality validation (R02) | Proposed |
| [ADR-006](ADR-006-cross-regulatory-role-coverage.md) | Cross-Regulatory Role Coverage as Differentiator | One role → multiple regulatory obligations is the headline feature, not role count | Proposed |
| [ADR-007](ADR-007-product-positioning-assessment-service.md) | Position as Assessment Service, Not Dataset | Every product delivers answers, not data access — taxonomy is cost of goods | Proposed |
| [ADR-008](ADR-008-schema-modifications-before-enrichment.md) | Schema Modifications Before Enrichment | 7 schema changes implemented before data population to prevent rework | Proposed |
| [ADR-009](ADR-009-agentic-ai-roles-first-mover.md) | Agentic AI Roles as First-Mover Play | New role definitions in Tier 3 — after credibility established, before window closes | Proposed |
| [ADR-010](ADR-010-validation-sprint-before-product-build.md) | Validation Sprint Before Product Build | 2-week Tier 0 sprint runs 4 parallel tests that determine the roadmap's shape | Proposed |
| [ADR-011](ADR-011-pe-assessment-scoring-model.md) | PE Assessment Scoring Model Design | 4-dimension scoring model (Coverage, Capability, Criticality, Concentration Risk) → WRS 0-100 | Accepted |
| [ADR-012](ADR-012-ksa-depth-correction.md) | KSA Depth Correction | External benchmarking, DCI metric, adversarial quality gate — corrects R02 validation gap | Accepted |
| [ADR-013](ADR-013-shared-pool-ksa-architecture.md) | Shared-Pool KSA Architecture | Domain-based KSA pool with many-to-many role mappings — replaces role-centric model | Accepted |
| [ADR-014](ADR-014-strm-based-ksa-enrichment.md) | STRM-Based KSA Enrichment Methodology | NIST IR 8477 Set Theory Relationship Mapping for evidence-based KSA pool enrichment | Accepted |
| [ADR-015](ADR-015-strm-onet.md) | STRM — O*NET Database 30.2 | First framework STRM: 126 FDEs mapped, 6 gap signals, QA/QC PASS | Accepted |

---

## How ADRs Relate to the Roadmap

The ADRs collectively define the logic of the phased roadmap:

**Phase 0: Validation Sprint (Weeks 1-2)** — Governed by ADR-010
Run R01, R02, R05, R24. Results may reshape ADR-003 (data coverage) and ADR-005 (AI authoring).

**Phase 1: First Product (Weeks 3-8)** — Governed by ADR-002, ADR-003, ADR-007, ADR-012, ADR-013, ADR-014
Build PE assessment methodology. Ship on current data. Position as service. KSA depth correction (ADR-012) → shared-pool architecture (ADR-013) → STRM-based enrichment (ADR-014). Framework STRMs execute per ADR-014 Phase 1C, documented individually (ADR-015+).

**Phase 2: Compliance + Validation (Weeks 9-16)** — Governed by ADR-004, ADR-006
EU AI Act role mapping. Cross-regulatory analysis. Practitioner validation.

**Phase 3: Expansion (Weeks 17-24)** — Governed by ADR-009
Agentic AI roles. SR 11-7 org design. CDAIO toolkit assembly.

**Phase 4: Scale (Weeks 25+)**
API, graph database, full coverage. Informed by all prior phases.

---

## How to Read These

Start with ADR-001 (roadmap sequencing logic) and ADR-010 (validation sprint). These frame the overall approach. Then read the use-case-specific ADRs (002, 004, 009) and the cross-cutting decisions (003, 005, 006, 007, 008) in any order. ADR-012 through ADR-015 document the KSA enrichment methodology evolution — read these in sequence.

Each ADR is self-contained but references other ADRs where decisions interact. The supporting analysis lives in [ensemble-brainstorm-widai.md](../ensemble-brainstorm-widai.md).
