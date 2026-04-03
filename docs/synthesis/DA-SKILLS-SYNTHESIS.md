# DA Skills — Phase 1D Synthesis Analysis

**Domain:** Data Architecture & Infrastructure (DA)
**Dimension:** Skills
**Date:** 2026-04-03
**Pre-synthesis count:** 20 (9 Phase 1A baseline + 11 post-STRM additions)
**Post-synthesis count:** 19

## Evidence Summary

- **Total mappings:** 11,498 across 6 frameworks
- **Phase 1A entries (S-001 to S-009):** All have STRM evidence (all 6/6)
- **Post-STRM entries (S-010 to S-020):** 0/6 coverage

### Strongest STRM Hits

| Entry | Strong | Max STS | Top framework evidence |
|-------|--------|---------|----------------------|
| DA-S-009 | 3 | 0.7216 | Pipeline observability |
| DA-S-001 | 2 | 0.7068 | Architecture artifacts |
| DA-S-002 | 1 | 0.7136 | Platform technology evaluation |
| DA-S-003 | 1 | 0.7071 | Data modeling standards |

## Duplicate Identification (Phase 1A)

### Duplicate Group 1: Pipeline Monitoring / Observability (S-005 + S-009)
- **S-005:** "Skill in designing and implementing data pipeline monitoring, including lineage tracking, data freshness alerting, volume anomaly detection, and schema drift detection."
- **S-009:** "Skill in designing data pipeline observability systems, including lineage tracking, execution monitoring, cost attribution, and root-cause analysis tooling for pipeline failures and data quality incidents."
- **Resolution:** Merge. Both cover pipeline monitoring/observability with overlapping lineage tracking scope. S-005 adds data quality signals; S-009 adds operational observability and RCA.

**Net effect:** 9 Phase 1A entries, 1 merge = 8 distinct Phase 1A entries

## Post-STRM Entry Evaluation (S-010 to S-020)

All 11 validated. No merges with Phase 1A or among themselves. Each fills a distinct skill gap:

| Entry | Concept | Verdict |
|-------|---------|---------|
| S-010 | Automated pipeline testing | **KEEP** — distinct from S-005/S-009 monitoring |
| S-011 | Heterogeneous source integration | **KEEP** — implementation skill, distinct from K-004 knowledge |
| S-012 | Infrastructure failure root cause analysis | **KEEP** — distinct diagnostic skill |
| S-013 | Schema evolution management | **KEEP** — distinct operational skill |
| S-014 | Database performance tuning | **KEEP** — distinct from S-006 pipeline tuning |
| S-015 | Capacity planning and scaling | **KEEP** — distinct operational skill |
| S-016 | Data catalog/metadata implementation | **KEEP** — distinct from K-019 knowledge |
| S-017 | Data migration execution | **KEEP** — distinct project skill |
| S-018 | Backup/DR implementation | **KEEP** — distinct operational skill |
| S-019 | Data API/service layer design | **KEEP** — distinct from K-024 knowledge |
| S-020 | Architecture communication to stakeholders | **KEEP** — distinct interpersonal skill |

## Final Count

8 (Phase 1A after 1 merge) + 11 (validated post-STRM) = **19 entries**

## Entry Mapping: Current → Proposed

| Proposed | Source | Action |
|----------|--------|--------|
| DA-S-001 | S-001 | Preserve (architecture artifacts) |
| DA-S-002 | S-002 | Preserve (platform technology evaluation) |
| DA-S-003 | S-003 | Preserve (data modeling standards) |
| DA-S-004 | S-004 | Preserve (ML infrastructure design) |
| DA-S-005 | S-005 + S-009 | Merge (pipeline monitoring + observability) |
| DA-S-006 | S-006 | Preserve (pipeline performance tuning) |
| DA-S-007 | S-007 | Preserve (IaC deployment) |
| DA-S-008 | S-008 | Preserve (platform cost management) |
| DA-S-009 | S-010 | Renumber (automated pipeline testing) |
| DA-S-010 | S-011 | Renumber (heterogeneous source integration) |
| DA-S-011 | S-012 | Renumber (infrastructure failure RCA) |
| DA-S-012 | S-013 | Renumber (schema evolution management) |
| DA-S-013 | S-014 | Renumber (database performance tuning) |
| DA-S-014 | S-015 | Renumber (capacity planning/scaling) |
| DA-S-015 | S-016 | Renumber (data catalog/metadata) |
| DA-S-016 | S-017 | Renumber (data migration) |
| DA-S-017 | S-018 | Renumber (backup/DR) |
| DA-S-018 | S-019 | Renumber (data API/service layer) |
| DA-S-019 | S-020 | Renumber (architecture communication) |
