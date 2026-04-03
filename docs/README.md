# WIDAI Documentation Index

**Last Updated:** 2026-04-03
**Scope:** Chief Data and AI Officer (CDAIO) Domain Workforce Framework

---

## What Is WIDAI?

WIDAI is a unified workforce framework that maps roles across the CDAIO domain, unifying workforce frameworks (NICE, O*NET, SFIA, ESCO, DDaT, DAMA DMBOK, EU AI Act, ISO 42001, SR 11-7, and others) into a single JSON schema with full provenance tracking.

- **187 roles** across 10 functional categories (governance, engineering, data science, analytics, risk/ethics, operations, leadership, etc.)
- **12 knowledge domains** organized as shared KSA pools with many-to-many role mappings
- **70 source frameworks** unified through deterministic role mappings — 34 assessed as STRM-eligible for active enrichment
- **Full provenance tracking** for every field, framework, and relationship
- **STRM enrichment pipeline** — NIST IR 8477 Set Theory Relationship Mapping produces evidence-based KSA validation and gap identification, framework by framework

---

## Documentation Structure

### Core Architecture & Design

**[Master Schema Design](master-schema-design.md)** — Complete unified JSON schema for the full role dataset. All fields across source frameworks mapped to schema properties, with design decisions and rationale.

**[Field-by-Field Assessment](field-by-field-assessment.md)** — Every schema field analyzed for use case value. Assessment of which fields are load-bearing vs. optional, prioritized by strategic importance.

**[NICE Boundary Scoping](nice-boundary-scoping.md)** — How NICE Framework handles adjacent/boundary roles. Which roles WIDAI includes and why. Integration patterns for NICE-WIDAI role mapping.

**[Gap Analysis](gap-analysis.md)** — Full inventory of roles across categories. Coverage assessment against source frameworks. Identified gaps and priority areas.

**[Technical Architecture](TECHNICAL.md)** — Entity-separated flat files, schema design, graph-ready structure, validation.

### Strategic Analysis

**[Axis 3 & Axis 4 Discovery](axis3-axis4-discovery.md)** — Exhaustive enumeration of outputs the framework produces and organizational contexts where WIDAI creates value. Highest-value buyer profiles and strategic implications.

**[Axis 3 & Axis 4 Summary](axis3-axis4-summary.md)** — Executive summary of discovery findings and strategic implications.

### Roadmap & Decisions

**[Execution Roadmap](roadmap/ensemble-brainstorm-widai.md)** — Five-pass strategic analysis (Forward Decomposition, Reverse Induction, Perspective Rotation, Constraint Inversion, Second-Order Mapping).

**[Phase 0 Validation Results](roadmap/PHASE-0-VALIDATION-SPRINT-RESULTS.md)** — Four parallel tests executed with results. Go decision for Phase 1.

**[Phase 1B Framework Prioritization](roadmap/phase-1b-framework-prioritization.md)** — 70 frameworks assessed for STRM eligibility. 4-tier prioritized execution sequence.

**[Architectural Decision Records](roadmap/adr/)** — 19 ADRs documenting rationale for every major roadmap and methodology decision.

### Methodology

**[PE Assessment Methodology](../methodology/R04-pe-assessment-methodology.md)** — Scoring model, engagement workflow, and deliverable specifications for the PE workforce due diligence product.

### Synthesis

**[AB Knowledge Synthesis](../strm/AB-KNOWLEDGE-SYNTHESIS.md)** — Cross-framework synthesis for the AB Knowledge dimension. 7,874 mappings across 6 frameworks analyzed, leading to expansion from 10 → 29 KSAs. See also [Expansion Proposal](../strm/AB-KNOWLEDGE-EXPANSION-PROPOSAL.md) for the full high watermark analysis and concept clustering methodology.

### STRM Framework Mappings

**[STRM Directory](../strm/)** — Per-framework NIST IR 8477 Set Theory Relationship Mappings. Each framework STRM produces: mapping data, per-element rationale files with multi-method scoring, gap issue register, scoring summary, and QA/QC report. See individual framework ADRs for methodology and findings.

---

## File Structure

```
widai-dataset/
├── roles/                    One file per category (GOV.json, ENG.json, etc.)
├── ksas/                     Type-separated KSA pools (12 domains × 4 types: knowledge, skills, tasks, abilities)
├── frameworks/               Reference data for 70 source frameworks
├── mappings/                 Relationship tables (role↔KSA, role↔framework)
├── sources/                  Canonical source citations and raw framework data
├── strm/                     Per-framework STRM mappings and rationale
│   ├── onet/                 O*NET 30.2 STRM (complete)
│   ├── nice/                 NICE v2.1.0 STRM (complete)
│   ├── dcwf/                 DCWF v5.1 STRM (complete)
│   ├── ddat/                 DDaT Capability Framework STRM (complete)
│   ├── eu_ai_act/            EU AI Act STRM (complete) — first regulatory framework
│   ├── nist_ai_rmf/          NIST AI RMF 1.0 STRM (complete) — second regulatory framework
│   ├── strm_scoring_pipeline.py  Consolidated domain-exhaustive scoring pipeline
│   └── issues/               Gap issue registers across all STRMs
├── methodology/              Assessment and scoring methodologies
├── schema/                   JSON Schema definitions
├── docs/                     Documentation (you are here)
│   ├── roadmap/              Execution roadmap, phase results, ADRs
│   └── assets/               SVG graphics for README
├── scripts/                  Validation and build tooling
└── widai_manifest.json       Index (no payload)
```

---

## Progress Tracking

### Phase 0 — Validation: Complete
All four validation tests passed. Go decision for Phase 1.

### Phase 1 — First Product: In Progress

| Sub-Phase | Status | Summary |
|-----------|--------|---------|
| 1A — Baseline KSA Enrichment | Complete | KSA pool expanded across all 12 domains. Abilities coverage gap closed. |
| 1B — Framework Prioritization | Complete | 34 STRM-eligible frameworks identified. 4-tier execution sequence. |
| 1C — Per-Framework STRM Cycle | In Progress | Tier 1 complete (4 frameworks). Tier 2: 2 of 5 complete (EU AI Act, NIST AI RMF). All 6 STRMs reprocessed through consolidated domain-exhaustive pipeline — 2.76M pairs scored, 536,737 rationale files. See STRM progress below. |
| 1D — Synthesis | In Progress | 4 of 12 domains complete. AB (Analytics & BI): 99 KSAs. AI (AI/ML Foundations): 123 KSAs. AG (AI Governance & Ethics): 85 KSAs. DA (Data Architecture & Infrastructure): 88 KSAs. Reusable synthesis script: `scripts/dimension_synthesis.py`. |

### STRM Framework Progress

| Tier | Framework | Status | ADR |
|------|-----------|--------|-----|
| 1 | O*NET 30.2 | Complete | [ADR-015](roadmap/adr/ADR-015-strm-onet.md) |
| 1 | NIST NICE v2.1.0 | Complete | [ADR-016](roadmap/adr/ADR-016-strm-nice.md) |
| 1 | DoD DCWF v5.1 | Complete | [ADR-017](roadmap/adr/ADR-017-strm-dcwf.md) |
| 1 | DDaT | Complete | [ADR-018](roadmap/adr/ADR-018-strm-ddat.md) |
| 2 | EU AI Act | Complete | [ADR-019](roadmap/adr/ADR-019-strm-eu-ai-act.md) |
| 2 | NIST AI RMF | Complete | — |
| 2 | DAMA DMBOK | Queued | — |
| 2 | FED SR 11-7 | Queued | — |
| 2 | GDPR | Queued | — |
| 2 | SFIA | Queued | — |

KSA pool statistics, gap analysis, and strength distributions will be published after synthesis (Phase 1D), when cross-framework evidence provides stable numbers. Individual STRM results are documented in their respective ADRs and rationale files.

### Phase 2 — Compliance + Validation: Not Started
### Phase 3 — Expand: Not Started
### Phase 4 — Scale: Not Started

---

## Validation

```bash
python3 scripts/validate.py
```

Checks: JSON structural integrity, referential integrity (all IDs resolve), duplicate detection, manifest completeness. Runs automatically via GitHub Actions on push/PR.

---

## Scope & Boundary

**In Scope:** All roles and functions in the Chief Data and AI Officer organizational domain. All roles required for data governance, data engineering, AI development, analytics, risk/ethics, operations, leadership. Boundary roles that cross into data/AI (Database Administrator, Privacy Officer, CISO where security overlaps AI governance).

**Out of Scope:** Cybersecurity workforce (covered by NIST NICE). Software engineering roles unrelated to data/AI. Domain-specific roles (radiologists, traders, researchers) that happen to use data/AI.

**Boundary Methodology:** Follows NIST NICE precedent — include roles that are essential to the domain or substantially modified by the domain.

---

## License

All content copyright © 2026 Thomas Jones. All rights reserved.
