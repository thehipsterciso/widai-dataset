# WIDAI Repository Audit: File-by-File Alignment Assessment

**Date:** 2026-03-27
**Trigger:** Architecture restructuring to shared-pool KSA model (ADR-013)
**Scope:** Every file in the repository

---

## Verdict Categories

- **KEEP** — Aligned with new architecture, no changes needed
- **UPDATE** — Sound content, needs modifications for new architecture
- **REWRITE** — Structure or claims fundamentally affected, must be rebuilt
- **REMOVE** — Deprecated, built on flawed model, or residual artifact
- **NEW** — Must be created for new architecture

---

## Root Files

| File | Verdict | Reason |
|------|---------|--------|
| `.DS_Store` | REMOVE | Should not be in repo (already in .gitignore but committed) |
| `.github/workflows/consistency.yml` | UPDATE | DCI/AQG steps added; needs to reference new file paths after migration |
| `.github/workflows/validate.yml` | KEEP | Runs validate.py, which will be updated separately |
| `.gitignore` | KEEP | Already covers OS/IDE/build artifacts |
| `ATTRIBUTION.md` | KEEP | Source attribution, unaffected by KSA restructuring |
| `CHANGELOG.md` | UPDATE | Needs v0.5.0 entry documenting architectural restructuring |
| `CONTRIBUTING.md` | UPDATE | References old KSA file structure and manifest update procedures |
| `README.md` | REWRITE | Claims "364 KSAs", "R08 complete", Phase 0 "PASS" — all invalidated or restructured |
| `widai_manifest.json` | REWRITE | Statistics, file inventory, architecture description all changing |

## Documentation

| File | Verdict | Reason |
|------|---------|--------|
| `docs/README.md` | UPDATE | May reference old structure |
| `docs/TECHNICAL.md` | REWRITE | Architecture section, KSA ID format, repo structure diagram, category counts — everything changes |
| `docs/assets/*.svg` (4 files) | KEEP | Visual assets; claims in graphics (187 roles, 322 KSAs) will lag but graphics are expensive to regenerate — note as known drift |
| `docs/axis3-axis4-discovery.md` | KEEP | Historical schema research, unaffected |
| `docs/axis3-axis4-summary.md` | KEEP | Historical schema research |
| `docs/field-by-field-assessment.md` | KEEP | Historical schema assessment |
| `docs/gap-analysis.md` | KEEP | Historical gap analysis |
| `docs/master-schema-design.md` | KEEP | Historical schema design |
| `docs/nice-boundary-scoping.md` | KEEP | Scope definition, still valid |

## Roadmap Documents

| File | Verdict | Reason |
|------|---------|--------|
| `docs/roadmap/ARCHITECTURE-BRAINSTORM-2026-03-27.md` | KEEP | Current session output |
| `docs/roadmap/PHASE-0-VALIDATION-SPRINT-RESULTS.md` | UPDATE | Add corrective note: R02 validated quality but not depth; R01 measured binary coverage |
| `docs/roadmap/R01-coverage-gap-test.json` | KEEP | Historical results, factually accurate for what it tested |
| `docs/roadmap/R01-coverage-gap-test.md` | UPDATE | Add note: "coverage" was binary presence, not depth-adequate |
| `docs/roadmap/R02-FAILURE-ASSESSMENT.md` | KEEP | Current session output |
| `docs/roadmap/R02-ai-authored-ksas.json` | KEEP | Historical — the authored KSA statements will be migrated into pool |
| `docs/roadmap/R02-ksa-quality-test.json` | KEEP | Historical results, quality scores still valid |
| `docs/roadmap/R02-ksa-quality-test.md` | UPDATE | Add corrective note about missing depth dimension |
| `docs/roadmap/R05-dependency-analysis.json` | KEEP | License analysis, unaffected |
| `docs/roadmap/R05-dependency-analysis.md` | KEEP | License analysis, unaffected |
| `docs/roadmap/R05-license-audit.json` | KEEP | License audit, unaffected |
| `docs/roadmap/R05-license-audit.md` | KEEP | License audit, unaffected |
| `docs/roadmap/R08-priority-ksa-authoring.json` | REMOVE | Built on flawed 1:1 model, superseded by ADR-012 |
| `docs/roadmap/R08-priority-ksa-authoring.md` | REMOVE | Built on flawed 1:1 model, superseded by ADR-012 |
| `docs/roadmap/R24-ksa-consistency-audit.json` | KEEP | Quality scores still valid for statement consistency |
| `docs/roadmap/R24-ksa-consistency-audit.md` | UPDATE | Add note about structural limitations (tested consistency, not depth/sharing) |
| `docs/roadmap/ensemble-brainstorm-atlas.md` | KEEP | Original brainstorm, still valuable |
| `docs/roadmap/r01_analysis.py` | KEEP | Historical analysis script |
| `docs/roadmap/aqg-analysis.json` | REMOVE | Generated from old structure, will be regenerated |
| `docs/roadmap/dci-analysis.json` | REMOVE | Generated from old structure, will be regenerated |

## ADRs

| File | Verdict | Reason |
|------|---------|--------|
| `ADR-001` through `ADR-011` | KEEP | Historical record; decisions stand as documented. ADR-005 and ADR-010 are contextually affected but their text is accurate for what they decided at the time. |
| `ADR-012-ksa-depth-correction.md` | UPDATE | Add note that shared-pool architecture (ADR-013) supersedes the "enrich each role independently" approach |
| `adr/README.md` | UPDATE | Add ADR-013 entry |

## KSA Files

| File | Verdict | Reason |
|------|---------|--------|
| `ksas/ANL_ksas.json` | REMOVE | Replaced by domain pool files |
| `ksas/DEV_ksas.json` | REMOVE | Replaced by domain pool files |
| `ksas/DSM_ksas.json` | REMOVE | Replaced by domain pool files |
| `ksas/ENG_ksas.json` | REMOVE | Replaced by domain pool files |
| `ksas/GOV_ksas.json` | REMOVE | Replaced by domain pool files |
| `ksas/LDR_ksas.json` | REMOVE | Replaced by domain pool files |
| `ksas/OPS_ksas.json` | REMOVE | Replaced by domain pool files |
| `ksas/RSK_ksas.json` | REMOVE | Replaced by domain pool files |

**New files to create:** 12 domain-based pool files (DG, DA, DQ, AI, AG, SP, AB, LS, OP, RC, RM, TF) + `_legacy_id_map.json`

## Mapping Files

| File | Verdict | Reason |
|------|---------|--------|
| `mappings/role_ksa_*.json` (8 files) | REWRITE | New KSA IDs, many-to-many cardinality, proficiency_context field |
| `mappings/roles_to_*.json` (70 files) | KEEP | Role-framework mappings are sound and unaffected |

## Methodology

| File | Verdict | Reason |
|------|---------|--------|
| `methodology/R04-pe-assessment-methodology.md` | UPDATE | Coverage dimension discussion needs context about pool depth |
| `methodology/pe-assessment-scoring-model.json` | UPDATE | Coverage calculation may need adjustment |
| `methodology/pe-assessment-workflow.json` | KEEP | Workflow unaffected |
| `methodology/pe-assessment-deliverables.json` | KEEP | Deliverables unaffected |

## Roles

| File | Verdict | Reason |
|------|---------|--------|
| `roles/*.json` (10 files) | KEEP | Role model is sound and unaffected |

## Schema

| File | Verdict | Reason |
|------|---------|--------|
| `schema/role_record.json` | KEEP | Role schema, not KSA schema |
| NEW: `schema/ksa_record.json` | NEW | Needs creation — define KSA schema for domain pool model |
| NEW: `schema/role_ksa_mapping.json` | NEW | Needs creation — define mapping schema with proficiency_context |

## Scripts

| File | Verdict | Reason |
|------|---------|--------|
| `scripts/adversarial_quality_gate.py` | REWRITE | Adapt to domain-based KSAs, shared-pool model |
| `scripts/check_consistency.py` | UPDATE | Adapt file path references to new ksas/ structure |
| `scripts/check_ksa_depth.py` | UPDATE | Adapt to shared-pool model; DCI now measures pool references |
| `scripts/coverage_gap_test.py` | KEEP | R01 test, still valid for binary coverage checks |
| `scripts/ksa_quality_audit.py` | KEEP | R24 audit, still valid for statement quality |
| `scripts/r08_author_gap_ksas.py` | REMOVE | Built on flawed 1:1 model |
| `scripts/update_framework_licensing.py` | KEEP | Framework tool, unaffected |
| `scripts/validate.py` | UPDATE | Adapt to new file structure |
| NEW: `scripts/migrate_to_domain_pool.py` | NEW | Migration script for the restructuring |

## Frameworks

| File | Verdict | Reason |
|------|---------|--------|
| `frameworks/frameworks.json` | KEEP | Unaffected |

---

## Summary

| Verdict | Count | Files |
|---------|-------|-------|
| KEEP | ~90 | Roles, frameworks, role-framework mappings, historical docs, ADRs 1-11 |
| UPDATE | ~15 | README, CHANGELOG, CONTRIBUTING, TECHNICAL, manifest, consistency scripts, select roadmap docs |
| REWRITE | ~11 | README, TECHNICAL, manifest, 8 role_ksa mappings, AQG script |
| REMOVE | ~13 | 8 old KSA files, R08 outputs, generated analysis JSONs, r08 script, .DS_Store |
| NEW | ~16 | 12 domain KSA pool files, legacy ID map, 2 schemas, migration script |

**Total affected:** ~55 of ~130 files
**Total untouched:** ~75 files (roles, frameworks, role-framework mappings, historical research docs)
