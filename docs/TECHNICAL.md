# ATLAS — Technical Documentation

This document covers the data architecture, schema design, repository structure, and validation tooling for the ATLAS dataset. For strategic context, use cases, and roadmap, see the [main README](../README.md).

---

## Architecture

ATLAS uses entity-separated flat files with foreign key references. This is a deliberate design choice: KSAs are independent entities, not role properties. A single KSA can belong to multiple roles. Two frameworks can describe the same KSA differently. The relationship tables capture all of this without duplicating the KSA itself.

This follows patterns established by NIST NICE (Tasks own KSAs, roles reference Tasks) and SFIA (skills exist independently, roles are assembled from skills). The disagreement between frameworks about how to describe a competency is analytically valuable — we record it rather than reconciling it.

Each directory represents a node type. Each mapping file represents an edge type. The structure loads directly into Neo4j or any graph database without transformation.

### Primary Key Design

- `role_id` — Primary key for roles. Format: `ATLAS-{CATEGORY}-{NNN}` (e.g., `ATLAS-GOV-001`)
- `ksa_id` — Primary key for KSAs. Format: `ATLAS-KSA-{CATEGORY}-{NNN}` (e.g., `ATLAS-KSA-GOV-001`)
- Relationship tables in `/mappings/` connect roles to KSAs and roles to source frameworks via these keys

---

## Repository Structure

```
atlas-dataset/
├── roles/                  One JSON file per category (GOV.json, ENG.json, ...)
│   └── 10 files            187 roles total
├── ksas/                   Independent KSA entities by category
│   └── 8 files             322 KSAs (NICHE and REG have 0)
├── frameworks/             Reference data for source frameworks
│   └── frameworks.json     70+ framework definitions
├── mappings/               Relationship tables
│   ├── role_ksa_*.json     Role-to-KSA mappings (8 files)
│   └── roles_to_*.json     Role-to-framework mappings (70+ files)
├── schema/                 JSON Schema definitions
│   └── role_record.json    Master schema (25+ fields, nested objects)
├── docs/                   Architecture decisions and research
│   ├── roadmap/            Strategic roadmap and ADRs
│   ├── assets/             SVG graphics for documentation
│   └── *.md                Technical documentation
├── scripts/                Validation and build tooling
│   ├── validate.py         Schema and referential integrity checks
│   ├── coverage_gap_test.py  R01 validation test
│   └── ksa_quality_audit.py  R24 quality audit
├── career_tracks/          Career progression paths (future)
├── job_descriptions/       Per-role JD templates (future)
├── tests/                  Test suite
├── atlas_manifest.json     Index of everything — no payload
└── CHANGELOG.md            Version history
```

---

## Role Categories

| Code | Title | Roles | KSAs | Coverage |
|------|-------|-------|------|----------|
| GOV | Governance, Strategy, and Executive Leadership | 25 | 73 | Full |
| ENG | Engineering, Architecture, and Platform | 25 | 53 | Full |
| DEV | Data Science, ML, and AI Development | 15 | 46 | Full |
| DSM | Data Stewardship and Master Data | 21 | 38 | Full |
| ANL | Analytics and Business Intelligence | 14 | 30 | Full |
| RSK | Risk, Ethics, Safety, Compliance, and Audit | 24 | 35 | Partial |
| OPS | Operations, Monitoring, and Reliability | 15 | 23 | Partial |
| LDR | Leadership and Management (VP/Director) | 31 | 24 | Partial |
| REG | Regulatory and Standards Compliance | 8 | 0 | Scaffold only |
| NICHE | Niche and Emerging Specializations | 9 | 0 | Scaffold only |

---

## Schema Design

The master schema (`schema/role_record.json`) defines 25+ fields per role record, including nested objects for regulatory and framework context. Seven schema modifications were applied based on a Field-by-Field Assessment ([ADR-008](roadmap/adr/ADR-008-schema-modifications-before-enrichment.md)):

### Key Schema Fields

**Core Identity:** `role_id`, `role_title`, `category_code` (enum: GOV, ENG, DEV, DSM, ANL, RSK, OPS, LDR, REG, NICHE), `functional_domain`, `secondary_domains`, `role_summary`

**Seniority:** `seniority_level` — array of objects with provenance, supporting multiple framework perspectives on the same role's level

**Competencies:** `knowledge`, `skills`, `abilities` — each with `importance_score` and `level_score` for quantified assessment

**Regulatory Context:** `regulatory_context` — nested object containing:
- `eu_ai_act`: applicable articles and operator type requirements
- `nist_ai_rmf_functions`: GOVERN, MAP, MEASURE, MANAGE function mappings
- `iso_42001_controls`: applicable control mappings
- `jurisdictions`: applicable regulatory jurisdictions

**Framework Context:** `framework_specific_context` — nested object with sub-objects for:
- `dama`: DAMA DMBOK knowledge area mappings
- `nist`: NIST framework mappings (NICE, AI RMF)
- `togaf`: TOGAF architecture domain mappings
- `mlops`: MLOps lifecycle phase mappings

**Provenance:** `source_frameworks` (array), `introduced_in_version` (string), source provenance on every mapping

### Schema Modification History

| Modification | Rationale |
|-------------|-----------|
| `secondary_domains` → enum | Ensures domain classification consistency with `functional_domain` |
| `category_code` → proper enum | 10 values with mapping documentation; previously implicit in file organization |
| `in_atlas_v030` → `introduced_in_version` | Supports proper version tracking as the dataset evolves |
| `seniority_level` → array with provenance | Different frameworks define seniority differently for the same role |
| `abilities` + scoring fields | Enables quantified assessment and gap analysis |
| `regulatory_context` expansion | Added NIST AI RMF functions, jurisdictions for multi-regulatory support |
| `dama_context` → `framework_specific_context` | Generalized for any professional framework, not just DAMA |

---

## Validation

```bash
python3 scripts/validate.py
```

Current validation checks:
- JSON structural integrity for all data files
- Referential integrity: every `ksa_id` and `role_id` in mapping files resolves to an existing entity
- Duplicate detection across categories
- Manifest completeness against actual file inventory

Planned validation expansion (R23):
- Full schema validation against `role_record.json` including nested objects
- Enum value validation for all constrained fields
- Cross-file referential integrity for framework mappings
- Provenance field validation
- CI/CD integration via GitHub Actions

---

## Scope

ATLAS covers the full data and AI profession. It explicitly excludes the CISO and cybersecurity workforce, which is covered comprehensively by NIST NICE. Boundary roles (Database Administrator, Privacy Officer, etc.) are included with domain-qualified framing, following the NICE precedent for adjacent roles. See [NICE Boundary Scoping](nice-boundary-scoping.md) for the detailed analysis.

---

## Source Frameworks

ATLAS unifies 70+ source frameworks. The major frameworks and their roles in the taxonomy:

| Framework | Type | Role in ATLAS |
|-----------|------|--------------|
| O\*NET | Occupational taxonomy | General occupation codes, task descriptions |
| NIST NICE | Cybersecurity workforce | Boundary role definitions, KSA methodology model |
| SFIA | IT skills framework | Skills-based role definitions, seniority levels |
| DAMA DMBOK | Data management body of knowledge | Knowledge areas, functional domains |
| ESCO | European skills/occupations | EU occupation codes, skills classification |
| EU AI Act | Regulation | Obligation-to-role mappings, compliance context |
| ISO 42001 | AI management standard | Control mappings, governance requirements |
| SR 11-7 | Model risk guidance | Model risk governance roles, independence requirements |
| NIST AI RMF | AI risk management | GOVERN/MAP/MEASURE/MANAGE function mappings |
| TOGAF | Enterprise architecture | Architecture domain context |

All framework mappings include source provenance. The complete framework list is in `frameworks/frameworks.json`.

---

## License

Copyright 2026 Thomas Jones. All rights reserved.

A source framework license audit ([R05](roadmap/adr/ADR-010-validation-sprint-before-product-build.md)) is in progress to determine commercial viability of derivative works under each source framework's licensing terms.
