# R08: Priority KSA Authoring — Gap Role Completion

**Execution Date:** 2026-03-27
**ATLAS Version:** 0.4.2 → 0.4.3
**Roadmap Item:** R08 (Tier 1)
**Dependencies:** R01 (gap identification), R02 (authoring workflow validation), R04 (scoring model)

---

## Executive Summary

R08 authors KSAs for the 5 roles identified by R01 as having "Partial" assessment readiness — roles that appeared in PE due diligence archetypes but lacked KSA mappings. These are the specific gaps that would prevent the R04 scoring model from producing a complete Workforce Readiness Score for certain archetype assessments.

**Result: 42 KSAs authored across 5 roles. PE archetype KSA coverage moves from 92.2% to 100%.**

All KSAs were authored using the AI-assisted workflow validated by R02 (4.26/5 average quality score). Each KSA follows the structure, granularity, and specificity standards established by the existing human-authored reference set (GOV, ENG, RSK, ANL categories).

---

## Roles Completed

### 1. Model Risk Manager (ATLAS-RSK-0108)
**Category:** RSK | **Seniority:** Director | **Work Role ID:** WR-RSK-06.05
**Archetype:** Mid-Market Financial Services
**Sources:** Fed SR 11-7, OCC Bulletin 2011-12

| Type | Count | ID Range |
|------|-------|----------|
| Knowledge | 4 | RSK-06.05-K-001 through K-004 |
| Skill | 2 | RSK-06.05-S-001 through S-002 |
| Task | 3 | RSK-06.05-T-001 through T-003 |
| **Total** | **9** | |

**Design rationale:** This role is critical for the Financial Services archetype and directly supports Phase 2 SR 11-7 organizational design patterns. KSAs ground in SR 11-7 and OCC regulatory expectations while addressing the AI/ML extension that traditional MRM frameworks are still adapting to. K-004 specifically addresses how traditional model risk frameworks must adapt for non-parametric and foundation models — a gap that PE assessors will encounter in every fintech and AI-forward financial services target.

---

### 2. MLOps Engineer (ATLAS-ENG-0041)
**Category:** ENG | **Seniority:** Mid–Senior | **Work Role ID:** WR-ENG-02.06
**Archetype:** PE-Backed SaaS/Technology
**Sources:** AWS ML Lens, Coursera, LinkedIn

| Type | Count | ID Range |
|------|-------|----------|
| Knowledge | 4 | ENG-02.06-K-001 through K-004 |
| Skill | 2 | ENG-02.06-S-001 through S-002 |
| Task | 2 | ENG-02.06-T-001 through T-002 |
| **Total** | **8** | |

**Design rationale:** MLOps is the operational backbone of any production ML capability. PE targets claiming "AI-powered" products need this role filled and functioning — its absence is a concentration risk signal. KSAs cover the full deployment lifecycle from pipeline orchestration through production monitoring. K-003 (drift detection) and T-002 (monitoring systems) are specifically designed to be assessable in a PE due diligence — you can ask "show me your drift detection" and get a binary answer.

---

### 3. DataOps Engineer (ATLAS-ENG-0037)
**Category:** ENG | **Seniority:** Mid | **Work Role ID:** WR-ENG-02.07
**Archetype:** PE-Backed SaaS/Technology
**Sources:** TDWI, McKinsey, DataOps.live

| Type | Count | ID Range |
|------|-------|----------|
| Knowledge | 3 | ENG-02.07-K-001 through K-003 |
| Skill | 2 | ENG-02.07-S-001 through S-002 |
| Task | 3 | ENG-02.07-T-001 through T-003 |
| **Total** | **8** | |

**Design rationale:** DataOps is the data pipeline equivalent of DevOps — the operational discipline that separates teams shipping reliably from teams firefighting. KSAs explicitly distinguish DataOps from DevOps and MLOps (K-001) because PE assessors will encounter confusion about these boundaries in target organizations. T-003 (environment management) addresses a common maturity gap: teams that develop against production data because they have no environment parity.

---

### 4. Data Protection Officer (ATLAS-GOV-0016)
**Category:** GOV | **Seniority:** Senior | **Work Role ID:** WR-GOV-01.07
**Archetype:** Healthcare/Life Sciences
**Sources:** GDPR Art 37-39, ISO 27701, IAPP

| Type | Count | ID Range |
|------|-------|----------|
| Knowledge | 4 | GOV-01.07-K-001 through K-004 |
| Skill | 2 | GOV-01.07-S-001 through S-002 |
| Task | 3 | GOV-01.07-T-001 through T-003 |
| **Total** | **9** | |

**Design rationale:** The DPO is a legally mandated role under GDPR with specific statutory requirements for independence and reporting. KSAs are grounded in the actual regulatory text (Art 37-39) rather than general privacy knowledge. K-002 explicitly addresses the independence requirements and conflict-of-interest prohibitions — assessable facts that a PE due diligence can verify. This role directly supports Phase 2 EU AI Act work, as the DPO is a key stakeholder in AI governance for any GDPR-subject organization.

---

### 5. Clinical Data Manager (ATLAS-ANL-0092)
**Category:** ANL | **Seniority:** Mid–Senior | **Work Role ID:** WR-ANL-05.05
**Archetype:** Healthcare/Life Sciences
**Sources:** O*NET

| Type | Count | ID Range |
|------|-------|----------|
| Knowledge | 3 | ANL-05.05-K-001 through K-003 |
| Skill | 2 | ANL-05.05-S-001 through S-002 |
| Task | 3 | ANL-05.05-T-001 through T-003 |
| **Total** | **8** | |

**Design rationale:** Clinical Data Manager is the most domain-specific role in the gap set. KSAs are grounded in GCP/ICH requirements and CDISC standards that are non-negotiable in regulated clinical environments. K-002 covers 21 CFR Part 11 compliance (FDA electronic records rule) — any PE target in clinical trials must have this competency or face regulatory risk. This role enables assessment of healthcare/life sciences targets where data integrity has direct patient safety implications.

---

## Impact Assessment

### KSA Coverage Before and After

| Metric | Before R08 | After R08 |
|--------|-----------|-----------|
| Total KSAs in ATLAS | 322 | 364 |
| PE archetype KSA coverage | 92.2% (59/64) | 100% (64/64) |
| Roles with "Partial" readiness | 5 | 0 |
| Categories affected | 4 (RSK, ENG, GOV, ANL) | 4 (all now fully covered) |

### PE Assessment Readiness

| Archetype | Before R08 | After R08 |
|-----------|-----------|-----------|
| PE-Backed Manufacturer | 100% | 100% (unchanged) |
| Mid-Market Financial Services | 94.1% | 100% (+Model Risk Manager) |
| PE-Backed SaaS/Technology | 86.7% | 100% (+MLOps, +DataOps) |
| Healthcare/Life Sciences | 85.7% | 100% (+DPO, +Clinical Data Mgr) |
| Mid-Market Retail/Consumer | 100% | 100% (unchanged) |

### Scoring Model Impact

The R04 PE Assessment Scoring Model can now produce a complete Workforce Readiness Score for all 5 archetypes without coverage gaps. Previously, the 5 gap roles would have received Coverage dimension scores based on role existence only, without the KSA-level capability assessment that makes the score meaningful. Now every role in every archetype can be scored on all 4 dimensions.

---

## Quality Assurance

All KSAs were authored following the standards validated by R02:

- **Statement structure:** Each begins with "Knowledge of," "Skill in," or an imperative verb (Tasks), consistent with the existing reference set
- **Granularity:** 7-9 KSAs per role, matching the R02 test range of 8-9
- **Specificity:** Statements reference specific frameworks, standards, and regulatory texts rather than generic competency language
- **Assessability:** Each KSA is designed to be observable and scorable in a PE due diligence context — the assessor can determine whether the capability exists through document review, interview, or artifact inspection
- **Provenance:** All KSAs carry `origin_framework: "ATLAS"` and `origin_version: "0.4.2"`, tagged as AI-assisted authoring per ADR-005

---

## Artifacts

- **KSA data:** Updated in `ksas/RSK_ksas.json`, `ksas/ENG_ksas.json`, `ksas/GOV_ksas.json`, `ksas/ANL_ksas.json`
- **Mapping data:** Updated in `mappings/role_ksa_RSK.json`, `mappings/role_ksa_ENG.json`, `mappings/role_ksa_GOV.json`, `mappings/role_ksa_ANL.json`
- **Machine-readable results:** `docs/roadmap/R08-priority-ksa-authoring.json`
- **Authoring script:** `scripts/r08_author_gap_ksas.py`
