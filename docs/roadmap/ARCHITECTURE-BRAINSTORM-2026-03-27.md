# ATLAS Architecture Brainstorm: KSA Data Model Redesign

**Date:** 2026-03-27
**Trigger:** Manual review exposed order-of-magnitude KSA depth failure + fundamental shared-pool design flaw
**Scope:** Everything downstream of the KSA identity model

---

## What Broke and Why

The ATLAS KSA model was built role-centric when it should have been built pool-centric. Every decision since has compounded this error.

**The architectural claim (from the manifest):** "KSAs are independent entities. Roles reference KSAs via relationship tables in /mappings/."

**The architectural reality:**
- 364 KSAs, 364 role-KSA mappings. Perfect 1:1. Zero sharing.
- Every KSA ID embeds the role it was created for: `GOV-01.01-K-001` belongs to the CDAIO by name.
- No KSA from any category is referenced by any role in another category.
- Semantically identical KSAs exist as separate entries (AI impact assessment appears in both GOV and RSK with slightly different wording and completely different IDs).

The manifest says one thing. The data says the opposite. That's the structural failure.

### Why This Happened

The authoring process was role-first: "What does a CDAIO need to know?" → author 15-19 KSAs for that role → assign IDs prefixed with the role → move to next role. This produces clean-looking output. It also produces a model where "Knowledge of AI governance frameworks" exists as 4 separate KSAs because 4 roles need it, each with their own copy under their own ID prefix.

The NICE framework — the only comparable reference — works completely differently. NICE has a shared pool where `K0001` through `K0622` are independent items. Work roles reference into the pool. A single Knowledge item appears in dozens of roles. The KSA doesn't "belong" to any role. It exists independently, and roles claim it.

This is the model ATLAS should follow. It was not a novel insight — it was the obvious design if anyone had looked at the reference framework's actual structure before building.

---

## The Five Questions That Define the Correct Architecture

### Q1: What makes a KSA unique?

A KSA is a single assessable unit of capability. Two KSA statements describe the same capability if and only if **the same interview question or evidence request** would assess them both. If a PE assessor would ask a materially different question to evaluate two statements, they are different KSAs.

**Example — same KSA:**
- "Knowledge of AI regulatory frameworks including the EU AI Act" (currently in GOV)
- "Knowledge of AI regulatory requirements including the EU AI Act" (currently in RSK)
→ Same interview question: "Walk me through the EU AI Act's risk classification structure and your organization's compliance approach." → **One KSA, referenced by both roles.**

**Example — different KSAs:**
- "Knowledge of machine learning model validation techniques for production deployment" (ENG context)
- "Knowledge of machine learning model validation for regulatory compliance and audit" (RSK context)
→ Different interview questions: The ENG version asks about cross-validation, test sets, A/B testing. The RSK version asks about SR 11-7 compliance, model documentation, independent validation. → **Two KSAs.**

**The decision rule:** If the assessment rubric is the same, it's one KSA. If the rubric diverges, it's two.

### Q2: Where do shared KSAs live?

Current model: KSAs live in category files (`GOV_ksas.json`, `RSK_ksas.json`). This forces category ownership.

**Proposed model: KSAs live in domain files, not category files.**

A "domain" is a knowledge cluster that spans roles and categories. Domains are NOT the same as role categories. A domain like "AI Governance & Ethics" contains KSAs referenced by GOV roles (AI Governance Manager), RSK roles (AI Risk and Ethics Specialist), and LDR roles (AI Innovation Lead).

**Proposed domain taxonomy:**

| Code | Domain | Description | Est. KSA Count |
|------|--------|-------------|----------------|
| DG | Data Governance & Policy | Governance frameworks, policy development, stewardship principles, organizational accountability | 40-55 |
| DA | Data Architecture & Infrastructure | Data modeling, platforms, storage, integration, pipeline design, cloud infrastructure | 40-55 |
| DQ | Data Quality & Management | Quality frameworks, MDM, metadata, data lifecycle, cataloging, lineage | 30-45 |
| AI | AI/ML Foundations | ML theory, model types, training, evaluation, NLP, CV, feature engineering, MLOps | 45-60 |
| AG | AI Governance & Ethics | Responsible AI, bias, fairness, transparency, AI regulation, model risk oversight | 35-50 |
| SP | Security & Privacy | Data protection, cybersecurity, privacy law, access control, encryption, incident response | 35-45 |
| AB | Analytics & BI | Statistical methods, visualization, reporting, BI tools, data storytelling, exploratory analysis | 30-40 |
| LS | Leadership & Strategy | Executive communication, organizational change, strategic planning, stakeholder management, budgeting | 30-40 |
| OP | Operations & Enablement | Program management, process optimization, training, adoption, change management | 25-35 |
| RC | Regulatory & Compliance | Specific regulations (GDPR, EU AI Act, CCPA, HIPAA), compliance monitoring, audit preparation | 35-45 |
| RM | Risk Management | Risk assessment, model risk, third-party risk, audit, controls, risk quantification | 30-40 |
| TF | Technical Foundations | Programming, databases, cloud platforms, DevOps, APIs, version control | 35-45 |

**Total estimated unique KSAs: 410-555**

Each role maps to KSAs across 3-7 domains. The CDAIO might reference KSAs from DG, AG, LS, RC, RM, and SP. A Data Engineer references DA, TF, DQ, and OP. The mapping is many-to-many and domain-crossing by design.

### Q3: What does the KSA ID scheme look like?

Current: `GOV-01.01-K-001` → embeds category + role + type + sequence. Role-coupled.

**Proposed: `DG-K-001`** → embeds domain + type + sequence. Role-independent.

Format: `{DOMAIN_CODE}-{TYPE}-{SEQUENCE}`

Where:
- `DOMAIN_CODE`: Two-letter domain code from taxonomy above
- `TYPE`: K (Knowledge), S (Skill), T (Task), A (Ability)
- `SEQUENCE`: Zero-padded 3-digit number within domain+type

Examples:
- `DG-K-001` → Data Governance domain, Knowledge item #1
- `AI-S-012` → AI/ML Foundations domain, Skill item #12
- `RC-T-003` → Regulatory & Compliance domain, Task item #3
- `LS-A-005` → Leadership & Strategy domain, Ability item #5

This scheme:
- Carries domain context (useful for browsing and debugging)
- Has no role coupling (any role can reference any KSA)
- Preserves type information
- Sorts cleanly within domain
- Scales to 999 items per domain+type combination

### Q4: How does the mapping model change?

Current mapping model (from `role_ksa_GOV.json`):
```json
{
  "work_role_id": "WR-GOV-01.01",
  "work_role_title": "Chief Data and AI Officer (CDAIO)",
  "ksa_id": "GOV-01.01-K-001",
  "source_framework": "ATLAS",
  "source_version": "0.3.0",
  "relationship_type": "requires"
}
```

**Proposed mapping model:**
```json
{
  "work_role_id": "WR-GOV-01.01",
  "ksa_id": "DG-K-001",
  "relationship_type": "requires",
  "proficiency_context": "strategic",
  "source_version": "0.5.0"
}
```

Changes:
- `ksa_id` references the domain-based pool ID
- `proficiency_context` added: indicates HOW the role uses this KSA (strategic, operational, technical, oversight). This is how you differentiate a CDAIO's relationship to "Knowledge of AI governance" from a Data Steward's relationship — same KSA, different context.
- `work_role_title` removed from mapping (derivable from role file — denormalization removed)
- `source_framework` removed from mapping (belongs on the KSA itself, not the relationship)

**Mapping file organization:** One file per role category (same as now), but KSA IDs can reference any domain. `role_ksa_GOV.json` will contain KSA IDs from DG, AG, LS, RC, RM — whatever the GOV roles need.

### Q5: How much of the current data survives?

| Component | Status | Action |
|-----------|--------|--------|
| **Roles** (213 across 10 categories) | **Preserved** | No changes needed. Role identity model is sound. |
| **Frameworks** (70 sources) | **Preserved** | No changes needed. |
| **Framework mappings** (roles_to_*.json) | **Preserved** | No changes needed. |
| **KSA statements** (364 current) | **Preserved but reorganized** | Deduplicate (~15-25% redundancy), re-ID to domain scheme, file into domain pool files. |
| **KSA IDs** | **Replaced** | Old role-coupled IDs deprecated. New domain-based IDs assigned. |
| **Role-KSA mappings** | **Rewritten** | Update KSA references to new IDs. Add proficiency_context. Enable many-to-many. |
| **Manifest** | **Rewritten** | New file structure, new counts, new statistics. |
| **DCI + AQG scripts** | **Updated** | Adapt to shared-pool model. DCI now measures pool coverage, not unique-per-role count. |

**Estimated work:**
- Deduplication: 364 current KSAs → ~280-310 unique after dedup
- Domain reorganization: Assign each unique KSA to its primary domain
- Pool enrichment: Author ~150-250 new KSAs to fill domain gaps (reach ~500 total)
- Mapping expansion: Each of 42 mapped roles gets 40-80 KSA references from the pool
- Total mappings: ~1,680-3,360 relationships (vs. current 364)

---

## What Changes in the File System

### Current structure:
```
ksas/
  ANL_ksas.json      (38 KSAs, category-organized)
  DEV_ksas.json      (46 KSAs)
  DSM_ksas.json      (38 KSAs)
  ENG_ksas.json      (69 KSAs)
  GOV_ksas.json      (82 KSAs)
  LDR_ksas.json      (24 KSAs)
  OPS_ksas.json      (23 KSAs)
  RSK_ksas.json      (44 KSAs)
```

### Proposed structure:
```
ksas/
  DG_ksas.json       (Data Governance & Policy)
  DA_ksas.json       (Data Architecture & Infrastructure)
  DQ_ksas.json       (Data Quality & Management)
  AI_ksas.json       (AI/ML Foundations)
  AG_ksas.json       (AI Governance & Ethics)
  SP_ksas.json       (Security & Privacy)
  AB_ksas.json       (Analytics & BI)
  LS_ksas.json       (Leadership & Strategy)
  OP_ksas.json       (Operations & Enablement)
  RC_ksas.json       (Regulatory & Compliance)
  RM_ksas.json       (Risk Management)
  TF_ksas.json       (Technical Foundations)
  _legacy_id_map.json (old ID → new ID mapping for audit trail)
```

The mapping files stay organized by role category (GOV, ENG, etc.) because the roles haven't changed. Only the KSA IDs they reference change.

---

## Depth Targets Under the Shared-Pool Model

With a shared pool, reaching 40-80 KSAs per role is structurally realistic:

- **~15-20 foundational KSAs** shared across nearly all roles (professional communication, data concepts, ethical principles, organizational awareness)
- **~15-25 domain KSAs** per domain the role touches (a role spanning 3 domains = 45-75 domain KSAs)
- **~5-10 role-specific KSAs** for capabilities unique to that role's function

A CDAIO (spans 5-6 domains) might map to 60-80 KSAs. A Data Analyst (spans 2-3 domains) might map to 40-50.

**The DCI metric recalibrates:** Instead of measuring unique KSAs per role, it measures pool references per role. The NICE benchmark comparison remains valid — NICE roles have 68-206 references into their shared pool.

---

## What This Means for the Roadmap

1. **R08 output is deprecated.** The 42 KSAs authored under the old scheme will be deduplicated and re-ID'd into the pool. Their statements survive; their identities don't.
2. **R02 gets a structural revalidation.** The quality test validated statement quality (4.26/5). That finding stands. But the validation now needs a depth dimension AND a sharing dimension.
3. **R04 scoring model becomes viable.** With 40-80 KSAs per role instead of 8-19, the Coverage dimension has genuine discriminating power.
4. **R03 (pilot) remains blocked** until the pool is built and roles are mapped to adequate depth.
5. **ADR-012 stands** but is supplemented by **ADR-013** (shared-pool architecture decision).

---

## Risk Assessment

**Risk 1: Over-sharing.** If too many KSAs are marked as shared, roles lose distinctiveness. The assessment can't differentiate a Data Architect from a Data Engineer.
→ **Mitigation:** The proficiency_context field on mappings preserves role-specific interpretation. And role-specific KSAs (the 5-10 unique ones per role) provide differentiation.

**Risk 2: Domain taxonomy is wrong.** 12 domains might be too many, or the boundaries might be wrong.
→ **Mitigation:** Domains are a file organization choice, not a data model constraint. Reorganizing domains later means moving KSAs between files, not changing IDs or mappings.

**Risk 3: Migration introduces errors.** Re-IDing 364 KSAs and rewriting 364+ mappings has surface area for bugs.
→ **Mitigation:** The `_legacy_id_map.json` maintains the audit trail. Consistency checker validates referential integrity.

**Risk 4: Enrichment quality.** Authoring ~200 new KSAs for pool depth could repeat the R02 problem (thin, generic statements).
→ **Mitigation:** The AQG runs against the enriched pool. Every new KSA must pass the assessability test.

---

## Decision Required

This restructuring changes the KSA identity model, file organization, mapping cardinality, and count statistics. It does NOT change roles, frameworks, or the PE assessment methodology. The statements authored to date survive — their containers change.

The alternative is to keep the current model and just add more role-specific KSAs, which would mean authoring ~1,400 unique statements (many of them near-duplicates) and maintaining a dataset where the same knowledge exists under 5 different IDs.

The shared-pool model is the correct architecture. NICE uses it. O*NET uses it. SFIA uses it. Every mature competency framework uses it. ATLAS should have been built this way from the start.
