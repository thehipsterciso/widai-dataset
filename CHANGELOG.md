# Changelog

All notable changes to the ATLAS dataset are documented here.
This project uses [Semantic Versioning](https://semver.org/).

## [0.5.3] - 2026-03-31

### Phase 1B: Framework Prioritization

**Framework prioritization complete** — 70 source frameworks assessed for STRM eligibility.

**What changed:**
- 34 frameworks classified as STRM-eligible (define KSA-equivalent concepts)
- 36 frameworks classified as not eligible (job aggregators, consultancy research, vendor docs, publications)
- 4-tier prioritized execution sequence established: Tier 1 (O*NET, NIST NICE, DCWF, DDAT), Tier 2 (EU AI Act, NIST AI RMF, FED SR 11-7, GDPR, DAMA DMBOK), Tier 3 (7 frameworks), Tier 4 (18 specialized)
- Governs ADR-014 Phase 1C execution order

### Phase 1C: STRM-001 — O*NET Database 30.2 (ADR-015)

**First STRM complete** — O*NET Content Model 30.2 mapped against ATLAS KSA Pool v0.5.2.

**Why:** O*NET is the largest occupational competency database (923 occupations, 169 content model elements). First STRM establishes methodology rhythm and validates baseline KSA pool against the broadest general-purpose competency taxonomy available.

**What changed:**
- 126 in-scope O*NET Focal Document Elements evaluated exhaustively against 497 ATLAS KSAs
- Relationship distribution: 82 Intersects with (65%), 23 No relationship (18%), 17 Superset of (14%), 4 Equal (3%)
- Mean Strength of Relationship: 5.2/10
- 6 gap signals identified (foundational communication, continuous learning, service orientation, project management, conflict resolution, ethical reasoning foundations)
- Gap signals cluster in foundational professional skills, not domain-specific technical areas — validating Phase 1A enrichment quality
- QA/QC: PASS on all criteria

**New files:** `sources/onet_30_2_citation.json`, `sources/onet_30_2/` (raw database), `strm/onet/use_case.json`, `strm/onet/strm_mapping.json`, `strm/onet/qa_qc_report.json`, `strm/issues/STRM-001-ONET-gaps.json`

**New ADRs:** ADR-015 (STRM — O*NET Database 30.2)

**New documentation:** `docs/roadmap/phase-1b-framework-prioritization.md`

## [0.5.2] - 2026-03-31

### Phase 1A: Baseline KSA Enrichment

**KSA pool expanded** from 363 to 497 unique KSAs across all 12 domain pools.

**Why:** ADR-014 (STRM-Based KSA Enrichment) identified that the ATLAS KSA pool at 363 entries was too thin for meaningful STRM framework mapping. At 5–19 KSAs per role, STRM would produce overwhelmingly "No relationship" results — confirming known gaps without producing actionable signal. Phase 1A establishes a reasonable baseline so STRM mappings produce genuine validation.

**What changed:**
- RC (Regulatory & Compliance): 7 → 42 KSAs. Major expansion covering data protection regulations, AI-specific regulatory frameworks, sector-specific compliance, cross-jurisdictional mapping, DPIAs, data subject rights, international data transfers, consent management, and regulatory examination readiness.
- TF (Technical Foundations): 7 → 37 KSAs. Expanded from SQL-only to comprehensive technical foundations including Python, databases (relational, NoSQL, graph, vector), cloud platforms, distributed computing, containerization, CI/CD, API design, Linux fundamentals, and networking.
- OP (Operations & Enablement): 16 → 35 KSAs. Added DataOps, service management, vendor evaluation, operational budgeting, self-service platforms, pipeline operations, capacity planning, and community of practice facilitation.
- LS (Leadership & Strategy): 19 → 41 KSAs. Added strategy development, talent management, board governance, vendor ecosystem, M&A due diligence, data monetization, workforce planning, and investment portfolio management.
- AB (Analytics & BI): 29 → 34 KSAs. Added augmented analytics knowledge, segmentation skills, and three Abilities (challenge narratives, method selection, correlation vs. causation).
- AG (AI Governance & Ethics): 31 → 37 KSAs. Added human oversight design, AI documentation skills, and four Abilities (risk-proportional governance, ethical trade-offs, value-driven RAI, policy translation).
- DQ (Data Quality & Management): 47 → 51 KSAs. Added four Abilities (impact-based prioritization, source vs. transformation remediation, business-connected quality, data product design).
- RM (Risk Management): 26 → 32 KSAs. Added enterprise risk integration, risk appetite design, and four Abilities (proportional assessment, independence, synthesis, framework adaptation).
- SP (Security & Privacy): 29 → 36 KSAs. Added anonymization/pseudonymization, privacy engineering, data classification, security assessment skills, and three Abilities (enabling architecture, emerging tech assessment, sharing vs. protection balance).
- AI, DA, DG: Unchanged (72, 40, 40 — already at target depth)

**Systematic gap addressed:** Abilities were absent from 6 of 12 domains (AB, AG, DQ, RM had 0; OP, RC had 0). All 12 domains now have Abilities.

**Enrichment methodology:** Research-grounded domain-expertise first pass informed by DAMA DMBOK, SFIA, O*NET, EU AI Act, GDPR competency frameworks, SR 11-7/SS1/23, DPO competency frameworks, and AI conformity assessment requirements. This baseline is explicitly pre-validation — STRM phase (Phase 1C) will validate, correct, and refine.

**Manifest updated:** atlas_manifest.json statistics and per-domain KSA counts synchronized.

## [0.5.1] - 2026-03-31

### STRM-Based KSA Enrichment Methodology (ADR-014)

**Methodology redesign** — KSA enrichment approach replaced from bulk AI-assisted authoring to NIST IR 8477 Set Theory Relationship Mapping (STRM) framework-by-framework evidence-based methodology.

**Why:** Adversarial review on 2026-03-31 identified that bulk KSA authoring — even with the Adversarial Quality Gate (AQG-v1) — produces KSAs without provenance chain, identifies gaps by intuition rather than systematic framework comparison, and determines cross-cutting KSAs by assumption rather than multi-framework evidence. The KSA pool is the core intellectual property of ATLAS. Every commercial product scores against it. It requires the same methodological rigor as the roadmap itself.

**What changed:**
- ADR-014 adopted: STRM-based enrichment supersedes ADR-012 Section 4 (Dataset Enrichment Sprint)
- Roadmap Phase 1 restructured into four sub-phases: 1A (Baseline Enrichment), 1B (Framework Prioritization), 1C (Per-Framework STRM Cycle), 1D (Synthesis)
- STRM deliverable format defined: NIST IR 8477 Table 5 six-column structure + Strength of Relationship (ATLAS extension from SCF practice)
- Seven deliverables per framework: canonical source, use case, STRM mapping data, per-FDE rationale files, gap issue register, QA/QC report, ADR
- New repo directories planned: `sources/`, `strm/`, `strm/issues/`
- Synthesis rules intentionally deferred until all framework STRMs are complete — rules emerge from evidence, not before it

**New ADRs:** ADR-014 (STRM-Based KSA Enrichment Methodology)

**Roadmap impact:** R03 (Pilot Engagement) remains blocked until enrichment completes via post-STRM synthesis. R08 (KSA Authoring) superseded — authoring now driven by STRM evidence. Phase 2 (First Product + Compliance) follows Phase 1D (Synthesis).

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
