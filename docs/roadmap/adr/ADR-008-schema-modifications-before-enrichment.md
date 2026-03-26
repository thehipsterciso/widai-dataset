# ADR-008: Schema Modifications Before Data Enrichment

**Status:** Proposed
**Date:** 2026-03-26
**Author:** Thomas Jones / The Hipster CISO
**Derived From:** Field-by-Field Assessment (7 KEEP WITH MODIFICATIONS verdicts), Ensemble Brainstorm Pass 1 (Forward Decomposition — foundational dependencies)

---

## Context

The ATLAS role schema (`role_record.json`) defines 25+ fields for each role record. A Field-by-Field Assessment conducted prior to the Ensemble Brainstorm identified 12 schema modifications needed — 7 classified as "KEEP WITH MODIFICATIONS" — that should be implemented before large-scale data enrichment proceeds.

The rationale is structural: enriching data into a schema that will change creates rework. Fields populated in the current schema format would need migration after schema changes. Modifying first avoids this waste.

Seven modifications have been implemented in the current schema:

1. **`secondary_domains`** — Changed to enum matching `functional_domain` values. Ensures domain classification consistency.
2. **`category_code`** — Added as proper enum with 10 values (GOV, ENG, DEV, DSM, ANL, RSK, OPS, LDR, NICHE, REG) plus mapping documentation. Previously implicit in file organization.
3. **`introduced_in_version`** — Replaced `in_atlas_v030` boolean with versioned string. Supports proper version tracking as the dataset evolves.
4. **`seniority_level`** — Restructured from flat string to array of objects with provenance. Acknowledges that different frameworks define seniority differently for the same role.
5. **`abilities`** — Added `importance_score` and `level_score`. Enables quantified assessment and gap analysis.
6. **`regulatory_context`** — Added `nist_ai_rmf_functions` and `jurisdictions`. Supports UC2 (EU AI Act), UC3 (Model Risk), and cross-regulatory analysis (R11).
7. **`dama_context` → `framework_specific_context`** — Renamed and restructured with dama/nist/togaf/mlops sub-objects. Supports cross-framework mapping for any professional framework, not just DAMA.

## Decision

**Schema modifications are confirmed as correct sequencing — modify the schema before populating data. The 7 implemented modifications are accepted. The remaining 5 modifications from the Field-by-Field Assessment should be evaluated and implemented during Tier 0 validation.**

The remaining modifications were not implemented in the initial batch. During R24 (KSA quality consistency audit, Tier 0), these should be assessed:

- Whether additional schema changes are needed based on what the five-pass analysis revealed about product requirements
- Whether the 7 implemented changes introduced any inconsistencies with existing data
- Whether new fields are needed for product-specific requirements (e.g., assessment scoring fields for UC1, obligation mapping fields for UC2)

## Rationale

**Modify-before-enrich is standard practice.** Database schema migration before data population is accepted engineering practice. The cost of populating fields that will change is always higher than the cost of finalizing the schema first. With 187 roles and 322 KSAs, a schema migration after enrichment would require touching every record.

**The modifications directly enable use case requirements.** Each change maps to specific use case needs:

| Modification | Use Cases Enabled |
|-------------|------------------|
| `secondary_domains` enum | UC1 (team mapping — roles spanning multiple domains) |
| `category_code` enum | All (query efficiency, category-based processing) |
| `introduced_in_version` | UC4 (new agentic AI roles need version tracking) |
| `seniority_level` with provenance | UC1 (assessment needs framework-aware seniority), UC5 (career pathing) |
| `abilities` scoring | UC1 (quantified assessment), UC2 (compliance gap scoring) |
| `regulatory_context` expansion | UC2 (EU AI Act), UC3 (SR 11-7), UC6 (cyber insurance) |
| `framework_specific_context` | All (cross-framework mapping — ADR-006 differentiator) |

**The modifications preserve backward compatibility.** Existing data is not invalidated — the changes add structure (new fields, new sub-objects) rather than removing existing fields. Roles with current data remain valid; they simply have additional empty fields to populate during enrichment.

## Consequences

**Positive:**
- Prevents rework during enrichment phase
- Schema now supports all six use case requirements identified in the five-pass analysis
- framework_specific_context generalization supports future framework additions without schema changes
- regulatory_context expansion handles multi-jurisdictional compliance scenarios

**Negative:**
- Schema complexity increased — 25+ fields with nested objects creates a steeper learning curve for anyone working with the data
- The 7 changes were implemented before the roadmap was formally reviewed (this was an execution sequencing error in the project) — they are correct changes but should have followed ADR documentation
- Additional schema changes may still be needed — the schema is not frozen

**Risks:**
- R05 (license audit) reveals that certain framework mappings in `framework_specific_context` cannot be commercially distributed. Mitigation: the field structure is framework-agnostic — specific sub-objects can be removed without architectural changes.
- Schema validation tooling (R23) lags behind schema changes, allowing invalid data to enter the dataset. Mitigation: update validate.py as part of each schema modification, not as a separate effort.

## References

- Field-by-Field Assessment: 7 KEEP WITH MODIFICATIONS verdicts
- ATLAS schema: role_record.json (current state includes all 7 modifications)
- Ensemble Brainstorm — ATLAS Roadmap, Pass 1: Foundation layer dependency map
- ATLAS Goal Definition: "12 schema modifications from the Field-by-Field Assessment"
