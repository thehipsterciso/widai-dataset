# ADR-013: Shared-Pool KSA Architecture

**Status:** Accepted
**Date:** 2026-03-27
**Author:** Thomas Jones / The Hipster CISO
**Supersedes:** KSA identity model in ADR-005; enrichment approach in ADR-012

## Context

The ATLAS KSA data model was built with role-centric ownership: each KSA is authored for a specific role, given an ID that embeds the role (`GOV-01.01-K-001`), stored in a category-based file, and mapped 1:1 to exactly one role. The manifest claims "KSAs are independent entities" — but the implementation contradicts this at every level.

Audit findings (2026-03-27):
- 364 KSAs, 364 role-KSA mappings. Perfect 1:1 cardinality. Zero sharing.
- Every KSA ID encodes the role it was created for. Cross-role reference is structurally impossible without violating naming conventions.
- Semantic duplicates exist across categories (AI impact assessment, regulatory compliance, fairness evaluation appear in near-identical form under different IDs in GOV and RSK).
- No KSA from any category is referenced by any role in another category.

This model cannot support workforce assessment at industry-standard depth. Enriching to 40-80 KSAs per role under the current model would require authoring ~1,400 mostly-duplicate statements. The correct approach — used by NICE, O*NET, and SFIA — is a shared pool where KSAs exist independently and roles reference them many-to-many.

Full analysis: [`docs/roadmap/ARCHITECTURE-BRAINSTORM-2026-03-27.md`](../ARCHITECTURE-BRAINSTORM-2026-03-27.md)

## Decision

Restructure the KSA data model from role-centric ownership to a shared domain-based pool with many-to-many role mappings.

### 1. Domain-Based KSA Pool

KSAs are organized by knowledge domain, not role category. A "domain" is a knowledge cluster that spans roles and categories.

| Code | Domain |
|------|--------|
| DG | Data Governance & Policy |
| DA | Data Architecture & Infrastructure |
| DQ | Data Quality & Management |
| AI | AI/ML Foundations |
| AG | AI Governance & Ethics |
| SP | Security & Privacy |
| AB | Analytics & BI |
| LS | Leadership & Strategy |
| OP | Operations & Enablement |
| RC | Regulatory & Compliance |
| RM | Risk Management |
| TF | Technical Foundations |

Each domain has its own file in `ksas/` (e.g., `DG_ksas.json`). A KSA belongs to exactly one domain. Roles reference KSAs from any domain.

*Alternatives considered:*
- Keep category-based files, just fix IDs: Preserves the structural barrier to cross-category sharing. The file organization communicates ownership even if the IDs don't.
- Organize by KSA type (knowledge.json, skills.json, tasks.json): Follows NICE exactly but loses domain grouping, making authoring and review harder.
- Single flat pool file: Too large to maintain as the pool grows.

### 2. Role-Independent KSA IDs

Format: `{DOMAIN_CODE}-{TYPE}-{SEQUENCE}`

Examples: `DG-K-001`, `AI-S-012`, `RC-T-003`, `LS-A-005`

No role information in the ID. Any role can reference any KSA. The ID carries domain context (useful for browsing) and type information (useful for distribution analysis).

*Alternatives considered:*
- Flat sequential IDs (K0001, S0001): Matches NICE exactly but loses domain context. Harder to browse and debug.
- UUID-based IDs: Maximum flexibility but zero human readability.
- Keep role-prefixed IDs and add cross-references: Preserves the conceptual flaw. The ID communicates ownership regardless of what the mapping allows.

### 3. Many-to-Many Mapping with Context

Mapping schema:
```json
{
  "work_role_id": "WR-GOV-01.01",
  "ksa_id": "DG-K-001",
  "relationship_type": "requires",
  "proficiency_context": "strategic"
}
```

The `proficiency_context` field differentiates how roles use the same KSA:
- **strategic** — executive/oversight application (CDAIO, CDO)
- **operational** — day-to-day execution (Data Steward, Data Engineer)
- **technical** — deep implementation (ML Engineer, Data Architect)
- **oversight** — audit/compliance review (Auditor, Risk Manager)

This replaces the old model's implicit differentiation (separate KSAs with slightly different wording for each role).

Mapping files remain organized by role category (`role_ksa_GOV.json`) but contain KSA IDs from any domain.

### 4. KSA Uniqueness Rule

Two KSA statements describe the same capability if and only if the same assessment question would evaluate both. If a PE assessor would ask a materially different question, they are different KSAs.

This is the decision rule for deduplication during migration and for all future authoring.

### 5. Legacy Audit Trail

A `ksas/_legacy_id_map.json` file maps every old role-coupled ID to its new domain-based ID. No old KSA is untraceable.

## Consequences

**Positive:**
- Shared pool eliminates semantic duplication. One KSA for "Knowledge of AI governance frameworks" instead of 4 near-identical copies.
- Many-to-many mapping enables realistic depth. Each role references 40-80 KSAs from the pool without authoring duplicates.
- Cross-category reference becomes natural. An ENG role can reference a DG (governance) KSA and an SP (security) KSA.
- Assessment consistency improves. The same KSA produces the same rubric regardless of which role it's assessed through.
- Maintenance burden drops. Updating a shared concept means updating one record, not N copies.

**Negative:**
- Breaking change. Every KSA ID changes. Every role-KSA mapping is rewritten. Downstream consumers of the current IDs must migrate.
- Migration complexity. 364 KSAs must be deduplicated, domain-assigned, and re-IDed. Error surface area is non-trivial.
- Domain taxonomy is a judgment call. 12 domains may not be optimal. Boundary KSAs between domains require a decision about primary domain.
- `proficiency_context` is new and unvalidated. The four-level model (strategic/operational/technical/oversight) may need refinement after pilot use.

## Migration Plan

1. Read all 364 existing KSAs across 8 category files
2. Identify semantic duplicates using the assessability rule
3. Assign each unique KSA to its primary domain
4. Generate new domain-based IDs
5. Create 12 domain pool files
6. Create `_legacy_id_map.json`
7. Rewrite all 8 `role_ksa_*.json` files with new IDs and many-to-many cardinality
8. Author new KSAs to fill domain gaps (target: ~450-550 unique pool)
9. Map each of 42 roles to 40-80 KSAs from the pool
10. Update manifest, README, TECHNICAL.md, CHANGELOG
11. Remove deprecated files (old KSA files, R08 outputs, generated analysis)
12. Run consistency check, DCI, and AQG against new structure
13. Commit as v0.5.0

## References

- [`docs/roadmap/ARCHITECTURE-BRAINSTORM-2026-03-27.md`](../ARCHITECTURE-BRAINSTORM-2026-03-27.md)
- [`docs/roadmap/REPO-AUDIT-2026-03-27.md`](../REPO-AUDIT-2026-03-27.md)
- [`docs/roadmap/R02-FAILURE-ASSESSMENT.md`](../R02-FAILURE-ASSESSMENT.md)
- ADR-005: AI-Assisted KSA Authoring (quality gates superseded)
- ADR-012: KSA Depth Correction (enrichment approach superseded)
- NIST NICE Framework v2.1.0 (shared-pool reference model)
