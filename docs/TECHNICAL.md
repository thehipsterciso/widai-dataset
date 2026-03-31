# ATLAS — Technical Documentation

This document covers the data architecture, schema design, repository structure, and validation tooling for the ATLAS dataset. For strategic context, use cases, and roadmap, see the [main README](../README.md).

---

## Architecture

ATLAS uses a shared-pool KSA model with entity-separated flat files and many-to-many role mappings. This architecture was established in [ADR-013](roadmap/adr/ADR-013-shared-pool-ksa-architecture.md), replacing the original role-centric model after a depth audit revealed a 14.9x shortfall against NICE framework benchmarks.

The core design principle: **KSAs are shared competencies organized by knowledge domain, not role properties.** A single KSA — "Knowledge of data classification frameworks and sensitivity labeling standards" — belongs to the Data Governance domain and can be referenced by a Data Governance Director, a Data Steward, a Privacy Officer, and an AI Governance Manager. Each role references the same KSA with a `proficiency_context` that differentiates how it applies: strategic for the Director, operational for the Steward, oversight for the Privacy Officer.

This follows patterns established by NIST NICE (where Tasks and KSAs exist independently, and roles reference them) and SFIA (where skills exist as a shared library and roles are assembled from them). The key difference: ATLAS organizes its shared pool by knowledge domain rather than by role category, enabling cross-domain sharing that role-centric models structurally prevent.

Each directory represents a node type. Each mapping file represents an edge type. The structure loads directly into Neo4j or any graph database without transformation.

### Primary Key Design

- `atlas_work_role_id` — Primary key for roles. Format: `WR-{CATEGORY}-{NN.NN}` (e.g., `WR-GOV-01.01`)
- `ksa_id` — Primary key for KSAs. Format: `{DOMAIN_CODE}-{TYPE}-{SEQUENCE}` (e.g., `DG-K-001`, `AI-S-012`)
  - Domain codes: DG, DA, DQ, AI, AG, SP, AB, LS, OP, RC, RM, TF
  - Type codes: K (Knowledge), S (Skill), A (Ability), T (Task)
- Relationship tables in `/mappings/` connect roles to KSAs via `work_role_id` → `ksa_id` with `proficiency_context`
- Role-to-framework mappings use `role_id` (format: `ATLAS-{CATEGORY}-{NNN}`)

### KSA Domain Taxonomy

KSAs are organized into 12 knowledge domains, each representing a coherent area of professional competency:

| Code | Domain | KSA Count |
|------|--------|-----------|
| AI | AI/ML Foundations | 72 |
| DQ | Data Quality & Management | 51 |
| RC | Regulatory & Compliance | 42 |
| LS | Leadership & Strategy | 41 |
| DA | Data Architecture & Infrastructure | 40 |
| DG | Data Governance & Policy | 40 |
| AG | AI Governance & Ethics | 37 |
| TF | Technical Foundations | 37 |
| SP | Security & Privacy | 36 |
| OP | Operations & Enablement | 35 |
| AB | Analytics & BI | 34 |
| RM | Risk Management | 32 |

Total: 497 unique KSAs across 12 domains (schema version 2.0.0).

---

## Repository Structure

```
atlas-dataset/
├── roles/                  One JSON file per category_code
│   └── 10 files            187 roles (GOV, ENG, DEV, DSM, ANL, RSK, OPS, LDR, REG, NICHE)
├── ksas/                   Shared KSA pool organized by knowledge domain
│   ├── AI_ksas.json        AI/ML Foundations (72)
│   ├── DQ_ksas.json        Data Quality & Management (51)
│   ├── RC_ksas.json        Regulatory & Compliance (42)
│   ├── LS_ksas.json        Leadership & Strategy (41)
│   ├── DA_ksas.json        Data Architecture & Infrastructure (40)
│   ├── DG_ksas.json        Data Governance & Policy (40)
│   ├── AG_ksas.json        AI Governance & Ethics (37)
│   ├── TF_ksas.json        Technical Foundations (37)
│   ├── SP_ksas.json        Security & Privacy (36)
│   ├── OP_ksas.json        Operations & Enablement (35)
│   ├── AB_ksas.json        Analytics & BI (34)
│   ├── RM_ksas.json        Risk Management (32)
│   └── _legacy_id_map.json Audit trail: old role-coupled IDs → new domain-based IDs
├── frameworks/             Reference data for source frameworks
│   └── frameworks.json     70 framework definitions with commercial_status
├── mappings/               Relationship tables (edge types)
│   ├── role_ksa_*.json     Role-to-KSA mappings (8 files, many-to-many with proficiency_context)
│   └── roles_to_*.json     Role-to-framework mappings (70 files)
├── methodology/            Product methodology specifications
│   ├── R04-pe-assessment-methodology.md
│   ├── pe-assessment-scoring-model.json
│   ├── pe-assessment-workflow.json
│   └── pe-assessment-deliverables.json
├── schema/                 JSON Schema definitions
│   └── role_record.json    Master schema (25+ fields, nested objects)
├── sources/                Canonical source citations for STRM framework mapping
│   └── onet_30_2_citation.json  O*NET 30.2 version-pinned citation
├── strm/                   NIST IR 8477 Set Theory Relationship Mappings (ADR-014)
│   ├── onet/               STRM-001: O*NET 30.2 (use case, mapping, QA/QC)
│   └── issues/             Gap issue register across all STRMs
├── docs/                   Architecture decisions and research
│   ├── roadmap/            Strategic roadmap, ADRs (15), validation results
│   ├── assets/             SVG graphics for documentation
│   └── *.md                Technical documentation
├── scripts/                Validation and quality gates
│   ├── validate.py         Schema and referential integrity checks
│   ├── check_consistency.py  Pre-commit consistency validation
│   ├── check_ksa_depth.py    KSA Depth Coverage Index (DCI) — ADR-012
│   ├── adversarial_quality_gate.py  5-pass Adversarial Quality Gate (AQG) — ADR-012
│   ├── migrate_to_domain_pool.py    Migration: role-centric → shared domain pool (ADR-013)
│   ├── coverage_gap_test.py   R01 validation test
│   ├── ksa_quality_audit.py   R24 quality audit
│   └── update_framework_licensing.py  R05 licensing update
├── atlas_manifest.json     Dataset index — no payload, metadata only
├── CHANGELOG.md            Version history
├── CONTRIBUTING.md         Pre-commit discipline checklist
└── ATTRIBUTION.md          Framework licensing attribution
```

---

## Role Categories

| Code | Title | Roles |
|------|-------|-------|
| GOV | Governance, Strategy, and Executive Leadership | 25 |
| ENG | Engineering, Architecture, and Platform | 25 |
| DEV | Data Science, ML, and AI Development | 15 |
| DSM | Data Stewardship and Master Data | 21 |
| ANL | Analytics and Business Intelligence | 14 |
| RSK | Risk, Ethics, Safety, Compliance, and Audit | 24 |
| OPS | Operations, Monitoring, and Reliability | 15 |
| LDR | Leadership and Management (VP/Director) | 31 |
| REG | Regulatory and Standards Compliance | 8 |
| NICHE | Niche and Emerging Specializations | 9 |

**KSA coverage model:** Roles reference KSAs from any domain via many-to-many mappings. A role in the GOV category can reference KSAs from DG (Data Governance), LS (Leadership), RC (Regulatory), AG (AI Governance), and RM (Risk Management) domains simultaneously. The `proficiency_context` field (strategic, operational, technical, oversight) differentiates how each role applies the shared KSA.

Current state: 42 roles have KSA mappings (364 role-KSA relationships). KSA depth enrichment is in progress — target is 40-80 KSAs per role using the shared pool model.

---

## Schema Design

The master schema (`schema/role_record.json`) defines 25+ fields per role record, including nested objects for regulatory and framework context. Seven schema modifications were applied based on a Field-by-Field Assessment ([ADR-008](roadmap/adr/ADR-008-schema-modifications-before-enrichment.md)).

### Role Record Fields

**Core Identity:** `atlas_work_role_id`, `canonical_title`, `category_code` (enum: GOV, ENG, DEV, DSM, ANL, RSK, OPS, LDR, REG, NICHE), `functional_domain`, `secondary_domains`, `role_summary`

**Seniority:** `seniority_level` — array of objects with provenance, supporting multiple framework perspectives on the same role's level

**Regulatory Context:** `regulatory_context` — nested object containing eu_ai_act (applicable articles and operator type requirements), nist_ai_rmf_functions (GOVERN, MAP, MEASURE, MANAGE function mappings), iso_42001_controls (applicable control mappings), jurisdictions (applicable regulatory jurisdictions)

**Framework Context:** `framework_specific_context` — nested object with sub-objects for dama (DAMA DMBOK knowledge area mappings), nist (NIST framework mappings), togaf (TOGAF architecture domain mappings), mlops (MLOps lifecycle phase mappings)

**Provenance:** `source_frameworks` (array), `introduced_in_version` (string), source provenance on every mapping

### KSA Record Fields (Schema v2.0.0)

**Core Identity:** `ksa_id` (domain-based, e.g., `DG-K-001`), `type` (Knowledge, Skill, Ability, Task), `domain` (full domain name), `domain_code` (two-letter code), `statement` (the KSA description)

**Provenance:** `origin_framework` (source framework name), `origin_version` (dataset version when authored), `legacy_ids` (array of old role-coupled IDs for audit trail)

### Role-KSA Mapping Fields (Schema v2.0.0)

**Relationship:** `work_role_id` (references atlas_work_role_id), `ksa_id` (references domain-based KSA ID), `relationship_type` (requires), `proficiency_context` (strategic, operational, technical, oversight)

---

## Quality Gates

### KSA Depth Coverage Index (DCI) — ADR-012

Benchmarks every mapped role's KSA count against the NIST NICE Framework v2.1.0. The NICE framework averages 133.3 KSAs per role (range: 68-206). ATLAS targets a minimum of 40 KSAs per standard role and 60 per regulatory role.

```bash
python3 scripts/check_ksa_depth.py
```

DCI bands: Critical (<15%), Deficient (15-30%), Developing (30-50%), Adequate (50-75%), Strong (75-100%), Comprehensive (≥100% of NICE mean).

### Adversarial Quality Gate (AQG) — ADR-012

Five-pass adversarial review evaluating KSA completeness from multiple perspectives: Breadth Scan (domain coverage), Depth Challenge (type balance), External Benchmark (NICE comparison), Assessability Test (statement clarity), Adversarial Review (PE operating partner perspective).

```bash
python3 scripts/adversarial_quality_gate.py
```

Gate fails if any critical pass (external benchmark, adversarial review) fails or if 3+ passes fail.

### Consistency Check

Pre-commit validation ensuring manifest accuracy, framework consistency, cross-reference integrity, and CHANGELOG currency.

```bash
python3 scripts/check_consistency.py
```

### Referential Integrity

Schema and referential integrity validation for all JSON data files.

```bash
python3 scripts/validate.py
```

Current validation checks: JSON structural integrity, referential integrity (every ksa_id and role_id in mappings resolves), duplicate detection, manifest completeness.

---

## Scope

ATLAS covers the full data and AI profession. It explicitly excludes the CISO and cybersecurity workforce, which is covered comprehensively by NIST NICE. Boundary roles (Database Administrator, Privacy Officer, etc.) are included with domain-qualified framing, following the NICE precedent for adjacent roles. See [NICE Boundary Scoping](nice-boundary-scoping.md) for the detailed analysis.

---

## Source Frameworks

ATLAS unifies 70 source frameworks. Each framework carries a `commercial_status` classification (GREEN/YELLOW/RED) from the R05 License Audit. The major frameworks and their roles in the taxonomy:

| Framework | Type | Role in ATLAS | Commercial Status |
|-----------|------|--------------|-------------------|
| O\*NET | Occupational taxonomy | General occupation codes, task descriptions | GREEN |
| NIST NICE | Cybersecurity workforce | Boundary role definitions, KSA methodology model | GREEN |
| SFIA | IT skills framework | Skills-based role definitions, seniority levels | YELLOW |
| DAMA DMBOK | Data management body of knowledge | Knowledge areas, functional domains | YELLOW |
| ESCO | European skills/occupations | EU occupation codes, skills classification | GREEN |
| EU AI Act | Regulation | Obligation-to-role mappings, compliance context | GREEN |
| ISO 42001 | AI management standard | Control mappings, governance requirements | YELLOW |
| SR 11-7 | Model risk guidance | Model risk governance roles, independence requirements | GREEN |
| NIST AI RMF | AI risk management | GOVERN/MAP/MEASURE/MANAGE function mappings | GREEN |
| TOGAF | Enterprise architecture | Architecture domain context | RED |

All framework mappings include source provenance. The complete framework list with licensing details is in `frameworks/frameworks.json` and `ATTRIBUTION.md`.

---

## Version History

| Version | Date | Architecture | Key Change |
|---------|------|-------------|------------|
| 0.5.3 | 2026-03-31 | Shared-pool + STRM | Phase 1B framework prioritization, STRM-001 O*NET complete (ADR-015) |
| 0.5.2 | 2026-03-31 | Shared-pool KSA | Phase 1A baseline enrichment — 363 → 497 KSAs, all 12 domains expanded |
| 0.5.1 | 2026-03-31 | Shared-pool KSA | STRM enrichment methodology adopted (ADR-014) |
| 0.5.0 | 2026-03-27 | Shared-pool KSA (ADR-013) | Domain-based KSA pool, many-to-many mappings, schema v2.0.0 |
| 0.4.3 | 2026-03-27 | Role-centric (SUPERSEDED) | R08 gap KSAs — valid statements, invalid architecture |
| 0.4.2 | 2026-03-27 | Role-centric | R04 PE Assessment Methodology, commit discipline |
| 0.4.1 | 2026-03-26 | Role-centric | Phase 0 validation sprint, roadmap, ADRs 1-10 |
| 0.4.0 | 2026-03-26 | Entity-separated | Initial entity separation, 322 KSAs, validation |
| 0.3.0 | 2026-03-24 | Embedded KSAs | 34 roles with embedded KSA spine |

---

## License

Copyright 2026 Thomas Jones. All rights reserved.

Source framework licensing: 19 GREEN (commercial use permitted), 28 YELLOW (requires attribution), 23 RED (citation-only). Full details in [ATTRIBUTION.md](../ATTRIBUTION.md) and the [R05 License Audit](roadmap/adr/ADR-010-validation-sprint-before-product-build.md).
