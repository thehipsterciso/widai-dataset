# Changelog

All notable changes to the ATLAS dataset are documented here.
This project uses [Semantic Versioning](https://semver.org/).

## [0.5.0] - 2026-03-27

### BREAKING: Shared-Pool KSA Architecture (ADR-013)

**Architectural restructuring** — KSA data model migrated from role-centric ownership to shared domain-based pool with many-to-many role mappings.

**Why:** Manual review on 2026-03-27 exposed two critical failures: (1) KSA depth averaged 8.95 per role versus NICE framework's 68-206 — a 14.9x shortfall, and (2) the KSA identity model (IDs embedding role ownership, perfect 1:1 mapping cardinality, zero cross-role sharing) structurally prevented the depth correction needed.

**What changed:**
- KSA files reorganized from 8 category-based files to 12 domain-based pool files
- KSA IDs changed from role-coupled (`GOV-01.01-K-001`) to domain-based (`DG-K-001`)
- 364 KSAs deduplicated to 363 unique (1 semantic duplicate merged)
- Role-KSA mappings rewritten with new IDs and `proficiency_context` field
- Schema version bumped to 2.0.0

**KSA Domain Taxonomy (12 domains):**
AB (Analytics & BI), AG (AI Governance & Ethics), AI (AI/ML Foundations), DA (Data Architecture & Infrastructure), DG (Data Governance & Policy), DQ (Data Quality & Management), LS (Leadership & Strategy), OP (Operations & Enablement), RC (Regulatory & Compliance), RM (Risk Management), SP (Security & Privacy), TF (Technical Foundations)

**Files removed:** 8 old category KSA files, R08 outputs (superseded by ADR-012), r08_author_gap_ksas.py

**Files added:** 12 domain KSA pool files, `_legacy_id_map.json` (old→new ID audit trail), `migrate_to_domain_pool.py`, `check_ksa_depth.py` (DCI metric), `adversarial_quality_gate.py` (AQG)

**New ADRs:** ADR-012 (KSA Depth Correction), ADR-013 (Shared-Pool Architecture)

**New documentation:** R02 Failure Assessment, Architecture Brainstorm, Repo Audit

**Note:** KSA depth enrichment (40-80 KSAs per role) is pending. This release establishes the correct architecture. The next release will populate it to industry-standard depth.

## [0.4.3] - 2026-03-27 [SUPERSEDED by v0.5.0]

### R08 — Priority KSA Authoring for Gap Roles (DEPRECATED — built on flawed 1:1 model)
- 42 KSAs authored across 5 gap roles — statement quality valid, architecture invalidated by ADR-012/013
- See R02-FAILURE-ASSESSMENT.md for root cause analysis

## [0.4.2] - 2026-03-27

### Phase 1 — First Product (R04)
- **R04 (PE Assessment Methodology):** Complete product specification for PE Workforce Due Diligence Assessment
- Scoring model: 4-dimension model (Coverage, Capability, Criticality, Concentration Risk) → 3 composite indices (TCI, KPRS, GSI) → single Workforce Readiness Score (WRS, 0-100)
- Engagement workflow: 30-day, 5-phase process designed for PE deal timelines
- 4 deliverables defined: Executive Summary, Workforce Capability Map, Gap Analysis & Hiring Priority Plan, Key Person Risk Assessment
- 5 reference architectures by company profile (Early-Stage through Enterprise)
- Compensation modeling intentionally deferred as modular add-on (no Lightcast dependency)
- ADR-011: PE Assessment Scoring Model Design — documents key design decisions and alternatives considered

### Commit Discipline
- Added CONTRIBUTING.md: Pre-commit checklist specific to ATLAS (update, create, verify phases)
- Added scripts/check_consistency.py: Automated validation of manifest accuracy, framework consistency, cross-references, CHANGELOG currency
- Added .github/workflows/consistency.yml: CI gate running consistency checks on every push/PR
- Fixed documentation drift from Phase 0 (CHANGELOG, README, manifest, ADR-003, ADR-005 all synced)

## [0.4.1] - 2026-03-26

### Roadmap & Strategy
- Redesigned README.md as C-suite strategy deck with competitive positioning, market opportunity, and execution roadmap
- Published ATLAS Roadmap: Ensemble Brainstorm five-pass strategic analysis (Forward Decomposition, Reverse Induction, Perspective Rotation, Constraint Inversion, Second-Order Mapping)
- Added 10 Architectural Decision Records (ADRs) documenting rationale for roadmap decisions, consequences, and alternatives considered

### Phase 0 Validation Sprint — Complete
- **R01 (Coverage Gap Test):** PASS — 92.2% KSA coverage across 5 archetypes (2026-03-26). Current 37-role KSA coverage spans 8 categories supporting mid-market team assessments (15-40 roles). Validated ADR-003 decision to ship on current data.
- **R02 (AI-Assisted KSA Quality Test):** PASS — Average quality score 4.26/5 across AI-assisted drafts blind-compared to manual baselines. No systematic deficiencies; quality comparable to existing KSA set. Validated AI-assisted authoring as primary acceleration strategy for remaining 150 roles. Established provenance tagging for transparency.
- **R24 (KSA Quality Consistency Audit):** PASS WITH CONDITIONS — 8.2/10 consistency score across existing KSAs. Documented style drift in historical roles; consistency requirements established for future authoring.
- **R05 (Source Framework License Audit):** CONDITIONAL — 19 GREEN (commercial use permitted), 28 YELLOW (requires attribution or notice), 23 RED (citation-only, no commercial use). Licensed frameworks reclassified into commercial_status field. Dependency analysis: ALL 70 frameworks carry citation-only requirements at minimum; NO dependencies block commercial build. Added ATTRIBUTION.md documenting licensing requirements for each framework.
- **ADR-010 (Validation Sprint) Execution:** All tests complete. Go decision: Phase 1 (PE due diligence assessment) and Phase 2 (EU AI Act compliance tracking) cleared for product build.

### R05 License Audit Follow-Through
- Added `commercial_status` field to all 70 frameworks (GREEN/YELLOW/RED classification)
- Reclassified Practitioner Community framework as citation-only per license review
- Completed framework dependency analysis: documented that all framework citations are attribution-only; no blocking dependencies for commercial products
- Created ATTRIBUTION.md with per-framework licensing notices, required citations, and GREEN framework commercial pathway

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
