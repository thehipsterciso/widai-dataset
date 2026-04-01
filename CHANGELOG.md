# Changelog

All notable changes to the WIDAI dataset are documented here.
This project uses [Semantic Versioning](https://semver.org/).

## [0.5.7] - 2026-04-01

### Phase 1C: STRM-005 — EU AI Act (Regulation (EU) 2024/1689) (ADR-019)

**Fifth STRM complete — first Tier 2, first regulatory framework.** EU AI Act mapped against WIDAI KSA Pool v0.5.6. First obligation→competency mapping. Functional rationale (first deviation from Semantic).

**Why:** The EU AI Act is the first comprehensive AI-specific regulation globally. Unlike STRM-001–004 (which mapped workforce competency frameworks), STRM-005 maps regulatory obligations to workforce competencies — answering "what workforce capabilities are required to comply?" This is the highest-value question for PE assessment: organizations with EU market exposure need to know which competencies they have and which they lack.

**What changed:**
- 62 elements extracted from 21 articles (8 competency, 54 obligation)
- Each element preserves dual provenance: obligation_text (original regulatory language) + competency_implication (workforce competency interpretation used for scoring)
- Relationship distribution: 27 Equal (43.5%), 31 Superset of (50.0%), 4 Intersects with (6.5%), 0 No relationship (0.0%)
- Mean strength (scored): 6.34/10 — higher than prior STRMs (4.18–5.12), explained by focused regulatory scope and competency-language scoring text
- Competency elements (mean 6.31) and obligation elements (mean 6.35) score nearly identically, validating the competency_implication bridging approach
- Zero gap signals — WIDAI KSA pool covers all EU AI Act workforce requirements (expected: requirements were input to Phase 1A enrichment)
- 4 elements with partial coverage (Intersects with): deep fake disclosure, biometric disclosure, training data bias, deployer AI literacy
- Methodology evolution: NLI-primary initially planned for obligation elements, diagnostic scoring showed near-zero entailment (mean 0.007), revised to STS-primary for all elements. Documented in ADR-019.
- QA/QC: PASS on all 7 criteria
- Cumulative: 5 frameworks, 5,470 elements scored, 5,470 rationale files, 18 gap signals, 19 ADRs

**Scoring methodology — STS-primary, Functional rationale:**
- Bi-encoder candidate identification (62 × 497 = 30,814 pairs) via all-MiniLM-L6-v2
- Full multi-method scoring pipeline (STS primary + 4 secondary) for all 62 scored pairs
- Functional rationale per NIST IR 8477 Section 4.3 — obligation→competency mapping direction
- 62 per-FDE rationale files with content-specific significance and dual provenance
- NLI diagnostic documented: entailment measures strict logical implication, not semantic relatedness

**New deliverables:**
- `sources/eu_ai_act/eu_ai_act_elements.json` — 62 elements with dual-provenance fields
- `sources/eu_ai_act/eu_ai_act_citation.json` — canonical source citation
- `sources/eu_ai_act/eu_ai_act_candidates.json` — bi-encoder candidate identifications
- `strm/eu_ai_act/strm_mapping.json` — STRM mapping data
- `strm/eu_ai_act/rationale/*.json` — 62 per-FDE rationale files
- `strm/eu_ai_act/scoring_summary.json` — scoring statistics with NLI diagnostic
- `strm/eu_ai_act/use_case.json` — NIST IR 8477 Section 3 use case
- `strm/eu_ai_act/qa_qc_report.json` — 7/7 checks pass
- `strm/issues/STRM-005-EU-AI-ACT-gaps.json` — gap register (0 gaps)
- `docs/roadmap/adr/ADR-019-strm-eu-ai-act.md` — full ADR with methodology evolution

## [0.5.6] - 2026-04-01

### Phase 1C: STRM-004 — UK Government DDaT Capability Framework (ADR-018)

**Fourth STRM complete — Tier 1 complete.** DDaT Capability Framework mapped against WIDAI KSA Pool v0.5.2. First international framework. First 100% match rate.

**Why:** DDaT is the UK government's authoritative digital/data workforce framework — 52 roles across 8 role families with 189 skills. As the first non-US framework in the STRM sequence, DDaT provides cross-jurisdictional validation: does a workforce framework developed under entirely different institutional context confirm WIDAI's KSA coverage patterns?

**What changed:**
- 189 DDaT skills evaluated exhaustively across all 8 role families
- Relationship distribution: 123 Intersects with (65.1%), 55 Superset of (29.1%), 11 Equal (5.8%), 0 No relationship (0.0%)
- 100% match rate — first STRM with zero no-relationship classifications
- Mean strength (scored): 4.72/10 — between STRM-001 (4.18, general-purpose) and STRM-003 (4.79, federal), reflecting DDaT's broad scope
- 39 DDaT skills with empty source descriptions resolved through proficiency-level text synthesis, fully tagged and validated
- 3 gap signals identified: foundational communication skills (moderate, corroborates ONET-GAP-001), workforce planning/financial management (low, corroborates DCWF-GAP-002), IT security management boundary (low, new)
- 2 of 3 gap signals corroborate existing gaps — cross-framework evidence accumulation continues
- Tier 1 complete: 4 frameworks, 5,408 elements scored, 5,408 rationale files, 18 gap signals
- QA/QC: PASS on all 7 criteria

**Scoring methodology — identical to STRM-001 through STRM-003:**
- Bi-encoder candidate identification (189 × 497 = 93,933 pairs) via all-MiniLM-L6-v2
- Full multi-method scoring pipeline (STS primary + 4 secondary) for all 189 scored pairs
- 189 per-FDE rationale files with content-specific significance
- Every significance field references actual text content — no templated or score-derived language

**New files:** `strm/ddat/` (strm_mapping.json, scoring_summary.json, strm_scoring_pipeline.py, qa_qc_report.json, 189 rationale files), `strm/issues/STRM-004-DDAT-gaps.json`, `sources/ddat/` (ddat_roles_skills.csv, ddat_skills_az.csv, ddat_elements.json, ddat_citation.json, ddat_skill_candidates.json), `docs/roadmap/adr/ADR-018-strm-ddat.md`

## [0.5.5] - 2026-04-01

### Phase 1C: STRM-003 — DoD Cyber Workforce Framework (DCWF) v5.1 (ADR-017)

**Third STRM complete** — DoD DCWF v5.1 mapped against WIDAI KSA Pool v0.5.2. Highest match rate of any framework to date.

**Why:** DCWF is the US federal government's authoritative cyber workforce framework — and the only Tier 1 framework with a dedicated Data/AI workforce element containing 11 work roles. At 2,945 KSAT elements across 75 work roles in 7 workforce elements (IT, Cybersecurity, Cyber Effects, Intelligence, Enablers, Software Engineering, Data/AI), this STRM validates WIDAI against the framework most likely to define federal data/AI workforce requirements.

**What changed:**
- 2,945 DCWF KSAT elements (1,277 tasks, 1,668 KSAs) evaluated exhaustively
- Relationship distribution: 1,836 Intersects with (62.3%), 990 Superset of (33.6%), 109 Equal (3.7%), 10 No relationship (0.3%)
- 99.7% match rate — highest of any STRM. Only 10 elements (all tactical military/forensic operations) classified as No relationship
- Mean strength (scored only): 4.79/10 — between STRM-001 (4.18, general-purpose) and STRM-002 (5.12, cybersecurity-specific), reflecting DCWF's mixed domain composition
- 4 gap signals identified: data/AI incident response (moderate, corroborates NICE-GAP-002), workforce planning/organizational design (moderate, partial corroboration of ONET-GAP-004), supply chain integrity (low, corroborates NICE-GAP-005), test and evaluation methodology (low, new)
- 3 of 4 gap signals corroborate existing gaps — cross-framework evidence accumulation continues
- DCWF Data/AI workforce element validates WIDAI's core domain model with consistent 5–8 strength range
- QA/QC: PASS on all 7 criteria

**Scoring methodology — identical to STRM-001-ONET and STRM-002-NICE:**
- Bi-encoder candidate identification (2,945 × 497 = 1.46M pairs) via all-MiniLM-L6-v2 to establish DCWF→WIDAI pairings
- Full multi-method scoring pipeline (STS primary + 4 secondary) for all 2,935 scored pairs — same models, same rigor
- 2,945 per-FDE rationale files with content-specific significance: shared vocabulary, unique terms per side, concept-level analysis
- Every significance field references actual text content — no templated or score-derived language

**WIDAI domain coverage from DCWF:**
- TF (Technical Foundations): 463 mappings — highest, confirming technical overlap
- SP (Security & Privacy): 443 | OP (Operations): 282 | AI: 272
- LS: 245 | DA: 232 | RC: 208 | RM: 200 | DQ: 198 | AB: 186 | DG: 130 | AG: 76

**New files:** `sources/dcwf/` (DCWF Work Role Tool v5.1, extracted elements, citation, candidate screening), `strm/dcwf/use_case.json`, `strm/dcwf/strm_mapping.json`, `strm/dcwf/strm_scoring_pipeline.py`, `strm/dcwf/scoring_summary.json`, `strm/dcwf/qa_qc_report.json`, `strm/dcwf/rationale/*.json` (2,945 files), `strm/issues/STRM-003-DCWF-gaps.json`

**New ADRs:** ADR-017 (STRM — DoD DCWF v5.1)

## [0.5.4] - 2026-04-01

### Phase 1C: STRM-002 — NIST NICE Framework v2.1.0 (ADR-016)

**Second STRM complete** — NICE Workforce Framework for Cybersecurity v2.1.0 (SP 800-181) mapped against WIDAI KSA Pool v0.5.2.

**Why:** NICE is the authoritative cybersecurity workforce framework. Mapping it defines the formal boundary between cybersecurity and data/AI professional domains — critical for positioning WIDAI as complementary to NICE. At 2,148 TKS elements, this is 17x the volume of STRM-001 and validates the scoring pipeline at production scale.

**What changed:**
- 2,148 NICE Focal Document Elements (946 tasks, 662 knowledge, 540 skills) evaluated exhaustively
- Relationship distribution: 1,106 Intersects with (51.5%), 582 Superset of (27.1%), 428 No relationship (19.9%), 32 Equal (1.5%)
- Mean strength (scored only): 5.12/10 — appropriately lower than STRM-001 (5.5) due to cross-domain vocabulary divergence
- 5 gap signals identified: data de-identification (moderate), data/AI incident response (moderate), technical audit/compliance (low), process maturity assessment (low), supply chain integrity for data/AI (low)
- Gap signals are boundary-zone (cybersecurity-data/AI overlap) rather than foundational (STRM-001 pattern)
- First cross-STRM corroboration: NICE-GAP-004 ↔ ONET-GAP-004 (operational maturity assessment)
- QA/QC: PASS on all 7 criteria

**Scoring methodology — identical to STRM-001-ONET:**
- Bi-encoder candidate identification (2,148 × 497 = 1.07M pairs) via all-MiniLM-L6-v2 to establish NICE→WIDAI pairings
- Full multi-method scoring pipeline (STS primary + 4 secondary) for all 1,720 scored pairs — same models, same rigor
- 2,148 per-FDE rationale files with content-specific significance: shared vocabulary, unique terms per side, concept-level analysis
- Every significance field references actual text content — no templated or score-derived language

**WIDAI domain coverage from NICE:**
- SP (Security & Privacy): 312 mappings — highest, confirming natural overlap
- TF (Technical Foundations): 212 | RM (Risk Management): 187 | OP (Operations): 187
- AI: 153 | DA: 131 | RC: 120 | DQ: 103 | LS: 102 | DG: 100 | AB: 80 | AG: 33

**New files:** `sources/nice_framework/` (NIST JSON, XLSX, citation, candidate screening, build script), `strm/nice/use_case.json`, `strm/nice/strm_mapping.json`, `strm/nice/strm_scoring_pipeline.py`, `strm/nice/scoring_summary.json`, `strm/nice/qa_qc_report.json`, `strm/nice/rationale/*.json` (2,148 files), `strm/issues/STRM-002-NICE-gaps.json`

**New ADRs:** ADR-016 (STRM — NIST NICE Framework v2.1.0)

## [0.5.3] - 2026-03-31

### Project Rename: ATLAS → WIDAI

**Workforce Initiative for Data and AI (WIDAI)** — project renamed across all documentation, data files, and tooling. Repo folder rename pending (handled separately at the GitHub level).

### Phase 1B: Framework Prioritization

**Framework prioritization complete** — 70 source frameworks assessed for STRM eligibility.

**What changed:**
- 34 frameworks classified as STRM-eligible (define KSA-equivalent concepts)
- 36 frameworks classified as not eligible (job aggregators, consultancy research, vendor docs, publications)
- 4-tier prioritized execution sequence established: Tier 1 (O*NET, NIST NICE, DCWF, DDAT), Tier 2 (EU AI Act, NIST AI RMF, FED SR 11-7, GDPR, DAMA DMBOK), Tier 3 (7 frameworks), Tier 4 (18 specialized)
- Governs ADR-014 Phase 1C execution order

### Phase 1C: STRM-001 — O*NET Database 30.2 (ADR-015)

**First STRM complete** — O*NET Content Model 30.2 mapped against WIDAI KSA Pool v0.5.2.

**Why:** O*NET is the largest occupational competency database (923 occupations, 169 content model elements). First STRM establishes methodology rhythm and validates baseline KSA pool against the broadest general-purpose competency taxonomy available.

**What changed:**
- 126 in-scope O*NET Focal Document Elements evaluated exhaustively against WIDAI KSA pool
- Relationship distribution: 82 Intersects with (65%), 23 No relationship (18%), 17 Superset of (14%), 4 Equal (3%)
- 6 gap signals identified (foundational communication, continuous learning, service orientation, project management, conflict resolution, ethical reasoning foundations)
- Gap signals cluster in foundational professional skills, not domain-specific technical areas — validating Phase 1A enrichment quality
- QA/QC: PASS on all criteria

**Multi-method computational scoring pipeline established:**
- Primary: Cross-Encoder STS (`cross-encoder/stsb-roberta-base`) — industry-standard pairwise semantic textual similarity. Raw 0-1 score mapped to NIST 0-10 strength scale.
- Secondary: BERTScore P/R/F1 (`roberta-large`), NLI Cross-Encoder (`nli-deberta-v3-base`), Bi-Encoder Cosine (`all-MiniLM-L6-v2`), Jaccard Token Overlap
- Each scored pair documented with all five methods plus per-method interpretive `significance` reasoning
- Scoring pipeline is reproducible — identical inputs produce identical outputs

**Per-FDE rationale files (126):**
- One JSON file per O*NET Focal Document Element in `strm/onet/rationale/`
- Full NIST IR 8278Ar1 OLIR template fields plus WIDAI extensions per ADR-014
- Complete five-method scoring audit trail with interpretive reasoning per method
- File naming: FDE ID with dashes (e.g., `2-C-1-f.json`)

**New files:** `sources/onet_30_2_citation.json`, `sources/onet_30_2/` (raw database), `strm/onet/use_case.json`, `strm/onet/strm_mapping.json`, `strm/onet/strm_scoring_pipeline.py`, `strm/onet/scoring_summary.json`, `strm/onet/qa_qc_report.json`, `strm/onet/rationale/*.json` (126 files), `strm/issues/STRM-001-ONET-gaps.json`

**New ADRs:** ADR-015 (STRM — O*NET Database 30.2)

**New documentation:** `docs/roadmap/phase-1b-framework-prioritization.md`

**Documentation cleanup:** README and docs/README rewritten to track progress rather than snapshot-specific statistics. Evolving numbers (KSA counts, strength distributions) deferred to individual STRM ADRs and rationale files until synthesis (Phase 1D) produces stable figures. `widai_manifest.json` renamed from `widai_manifest.json`.

## [0.5.2] - 2026-03-31

### Phase 1A: Baseline KSA Enrichment

**KSA pool expanded** from 363 to 497 unique KSAs across all 12 domain pools.

**Why:** ADR-014 (STRM-Based KSA Enrichment) identified that the WIDAI KSA pool at 363 entries was too thin for meaningful STRM framework mapping. At 5–19 KSAs per role, STRM would produce overwhelmingly "No relationship" results — confirming known gaps without producing actionable signal. Phase 1A establishes a reasonable baseline so STRM mappings produce genuine validation.

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

**Manifest updated:** widai_manifest.json statistics and per-domain KSA counts synchronized.

## [0.5.1] - 2026-03-31

### STRM-Based KSA Enrichment Methodology (ADR-014)

**Methodology redesign** — KSA enrichment approach replaced from bulk AI-assisted authoring to NIST IR 8477 Set Theory Relationship Mapping (STRM) framework-by-framework evidence-based methodology.

**Why:** Adversarial review on 2026-03-31 identified that bulk KSA authoring — even with the Adversarial Quality Gate (AQG-v1) — produces KSAs without provenance chain, identifies gaps by intuition rather than systematic framework comparison, and determines cross-cutting KSAs by assumption rather than multi-framework evidence. The KSA pool is the core intellectual property of WIDAI. Every commercial product scores against it. It requires the same methodological rigor as the roadmap itself.

**What changed:**
- ADR-014 adopted: STRM-based enrichment supersedes ADR-012 Section 4 (Dataset Enrichment Sprint)
- Roadmap Phase 1 restructured into four sub-phases: 1A (Baseline Enrichment), 1B (Framework Prioritization), 1C (Per-Framework STRM Cycle), 1D (Synthesis)
- STRM deliverable format defined: NIST IR 8477 Table 5 six-column structure + Strength of Relationship (WIDAI extension from SCF practice)
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
- Added CONTRIBUTING.md: Pre-commit checklist specific to WIDAI (update, create, verify phases)
- Added scripts/check_consistency.py: Automated validation of manifest accuracy, framework consistency, cross-references, CHANGELOG currency
- Added .github/workflows/consistency.yml: CI gate running consistency checks on every push/PR
- Fixed documentation drift from Phase 0 (CHANGELOG, README, manifest, ADR-003, ADR-005 all synced)

## [0.4.1] - 2026-03-26

### Roadmap & Strategy
- Redesigned README.md as C-suite strategy deck with competitive positioning, market opportunity, and execution roadmap
- Published WIDAI Roadmap: Ensemble Brainstorm five-pass strategic analysis (Forward Decomposition, Reverse Induction, Perspective Rotation, Constraint Inversion, Second-Order Mapping)
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
- `widai_manifest.json` as dataset index (no payload, metadata only)
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
- WIDAI v0.3.0 Base Structure: 8 WRCs, 34 work roles, KSA spine (ksa_id, type, statement)
- KSAs embedded inside work role records
- No entity separation, no relationship tables

## [0.2.0] - 2026-03-24

### Prior state (imported from chat)
- 187-role scaffold across 3 parts (A/B/C) split by sequence number
- Scaffold status: canonical_title, category, seniority, key_variants, sources populated
- KSAs and all enrichment fields deferred
