# Changelog

All notable changes to the ATLAS dataset are documented here.
This project uses [Semantic Versioning](https://semver.org/).

## [0.4.0] - 2026-03-26

### Added
- Entity-separated architecture: roles, KSAs, and framework mappings as independent entity types
- 187 roles split by `category_code` into 10 category files (GOV, ENG, DEV, DSM, ANL, RSK, OPS, LDR, REG, NICHE)
- 322 KSAs extracted from v0.3.0 base structure as independent entities in `/ksas/`
- 322 Role_KSA relationship records in `/mappings/role_ksa_*.json`
- 70 framework references in `/frameworks/frameworks.json`
- 333 role-to-framework mappings across 70 source frameworks
- `atlas_manifest.json` as dataset index (no payload, metadata only)
- JSON Schema for CDAIO Domain Master Role Record (`/schema/role_record.json`)
- Validation script (`/scripts/validate.py`) with referential integrity checks
- GitHub Actions CI workflow (`.github/workflows/validate.yml`)
- Architecture documentation from design phase in `/docs/`

### Changed
- Roles restructured from sequence-based parts (A/B/C) to semantically meaningful category-based files
- KSAs decomposed from embedded role properties to independent entities with stable `ksa_id` identifiers
- Framework mappings separated from role records into dedicated relationship files

### Architecture decisions
- KSAs are independent entities, not role properties (per NICE Task-based and SFIA skill-library patterns)
- `role_id` is the foreign key throughout all relationship files
- Each directory represents a node type; each mapping file represents an edge type
- Designed for direct Neo4j ingestion: directories as node types, mappings as edge types

## [0.3.0] - 2026-03-24

### Prior state (imported from chat)
- ATLAS v0.3.0 Base Structure: 8 WRCs, 34 work roles, KSA spine (ksa_id, type, statement)
- KSAs embedded inside work role records
- No entity separation, no relationship tables

## [0.2.0] - 2026-03-24

### Prior state (imported from chat)
- 187-role scaffold across 3 parts (A/B/C) split by sequence number
- Scaffold status: canonical_title, category, seniority, key_variants, sources populated
- KSAs and all enrichment fields deferred
