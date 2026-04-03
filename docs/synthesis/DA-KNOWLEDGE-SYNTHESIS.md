# DA Knowledge — Phase 1D Synthesis Analysis

**Domain:** Data Architecture & Infrastructure (DA)
**Dimension:** Knowledge
**Date:** 2026-04-03
**Pre-synthesis count:** 28 (16 Phase 1A baseline + 12 post-STRM additions)
**Post-synthesis count:** 25

## Evidence Summary

- **Total mappings:** 16,253 across 6 frameworks
- **Phase 1A entries (K-001 to K-016):** All have STRM evidence (14 at 6/6, 2 at 5/6)
- **Post-STRM entries (K-017 to K-028):** 0/6 coverage (added after STRM runs)

### High Watermark (unique FDE count at STS thresholds)

| Framework | >=0.45 | >=0.50 | >=0.55 | >=0.60 |
|-----------|--------|--------|--------|--------|
| O*NET 30.2 | 17 | 8 | 1 | 0 |
| NIST NICE v2.1.0 | 912 | 567 | 301 | 108 |
| DoD DCWF v5.1 | 1,145 | 687 | 313 | 93 |
| DDaT | 63 | 35 | 15 | 2 |
| EU AI Act | 32 | 21 | 9 | 2 |
| NIST AI RMF 1.0 | 55 | 40 | 20 | 7 |

### Strongest STRM Hits

| Entry | Strong | Max STS | Top framework evidence |
|-------|--------|---------|----------------------|
| DA-K-014 | 1 | 0.7406 | Vendor/third-party risk management |
| DA-K-002 | 1 | 0.7059 | NICE K1278 data vaulting principles |
| DA-K-013 | 0 | 0.6846 | Pipeline orchestration/scheduling |
| DA-K-012 | 0 | 0.6808 | Data platform security controls |
| DA-K-011 | 0 | 0.6768 | Infrastructure-as-code |

## Duplicate Identification (Phase 1A)

### Duplicate Group 1: Semantic Layer / Metrics Layer (K-001 + K-010)
- **K-001:** "Knowledge of semantic layer design, including measure definition, dimension hierarchy design, slowly changing dimension handling, and the relationship between semantic model design and report performance."
- **K-010:** "Knowledge of metrics layer concepts, including semantic layer design, metric definition standards, and how centralized metric definitions prevent inconsistency across reporting tools."
- **Resolution:** Merge. Both cover semantic layer design and metric definitions. K-001 adds dimension hierarchy and SCD handling; K-010 adds centralized metric consistency.

### Duplicate Group 2: Data Modeling / Dimensional Modeling (K-002 + K-008)
- **K-002:** "Knowledge of data modeling techniques including conceptual, logical, and physical modeling, entity-relationship modeling, dimensional modeling, and data vault methodology."
- **K-008:** "Knowledge of dimensional modeling principles, including star schema, snowflake schema, slowly changing dimensions, and the design trade-offs between normalization and query performance."
- **Resolution:** Merge. K-008 is a detailed subset of K-002's "dimensional modeling" component. Enriched entry combines general modeling techniques with dimensional specifics.

### Duplicate Group 3: Pipeline Orchestration (K-007 + K-013)
- **K-007:** "Knowledge of data pipeline orchestration tools (e.g., Airflow, Prefect, Dagster) and how to design DAGs that are observable, recoverable, and maintainable."
- **K-013:** "Knowledge of data pipeline orchestration tools and scheduling patterns, including dependency graph management, failure handling, retry strategies, idempotency requirements, and SLA-driven monitoring."
- **Resolution:** Merge. Both about pipeline orchestration tools. K-007 names specific tools and DAG design; K-013 adds operational patterns (failure handling, retries, idempotency, SLAs).

**Net effect:** 16 Phase 1A entries, 3 merges = 13 distinct Phase 1A entries

## Post-STRM Entry Evaluation (K-017 to K-028)

| Entry | Concept | Verdict |
|-------|---------|---------|
| K-017 | DataOps practices and CI/CD for data pipelines | **KEEP** — distinct operational discipline |
| K-018 | Database administration and lifecycle management | **KEEP** — distinct from platform architecture |
| K-019 | Data classification, cataloging, metadata management | **KEEP** — distinct concept |
| K-020 | Data privacy/protection techniques (masking, tokenization, etc.) | **KEEP** — distinct from K-012 security controls (K-012 = infrastructure security, K-020 = data-level privacy) |
| K-021 | Container orchestration, cloud-native data infrastructure | **KEEP** — distinct from K-011 IaC (K-011 = provisioning tools, K-021 = container/serverless patterns) |
| K-022 | Backup, recovery, disaster recovery | **KEEP** — distinct operational concept |
| K-023 | Data lineage and provenance tracking | **KEEP** — distinct concept |
| K-024 | API design and data service patterns | **KEEP** — distinct from K-004 integration patterns (K-004 = data movement, K-024 = API/service layer) |
| K-025 | Event-driven architecture patterns | **KEEP** — distinct from K-004 integration (K-004 lists event streaming; K-025 goes deeper into event sourcing, CQRS, pub-sub architecture) |
| K-026 | Cloud cost models and FinOps | **KEEP** — distinct concept |
| K-027 | Schema evolution and change management | **KEEP** — distinct concept |
| K-028 | Capacity planning and performance engineering | **KEEP** — distinct concept |

**Net effect:** 12 kept, 0 merged

## Final Count

13 (Phase 1A after 3 merges) + 12 (validated post-STRM) = **25 entries**

## Entry Mapping: Current → Proposed

| Proposed | Source | Action |
|----------|--------|--------|
| DA-K-001 | K-001 + K-010 | Merge (semantic layer + metrics layer) |
| DA-K-002 | K-002 + K-008 | Merge (data modeling + dimensional modeling) |
| DA-K-003 | K-003 | Preserve (data platform architecture patterns) |
| DA-K-004 | K-004 | Preserve (data integration patterns) |
| DA-K-005 | K-005 | Preserve (data pipeline design patterns) |
| DA-K-006 | K-006 | Preserve (distributed processing frameworks) |
| DA-K-007 | K-007 + K-013 | Merge (pipeline orchestration tools + scheduling patterns) |
| DA-K-008 | K-009 | Renumber (dbt/transformation frameworks) |
| DA-K-009 | K-011 | Renumber (infrastructure-as-code) |
| DA-K-010 | K-012 | Renumber (data platform security controls) |
| DA-K-011 | K-014 | Renumber (vendor/third-party risk management) |
| DA-K-012 | K-015 | Renumber (pipeline monitoring) |
| DA-K-013 | K-016 | Renumber (data platform access management) |
| DA-K-014 | K-017 | Renumber (DataOps/CI-CD) |
| DA-K-015 | K-018 | Renumber (database administration) |
| DA-K-016 | K-019 | Renumber (classification/cataloging/metadata) |
| DA-K-017 | K-020 | Renumber (data privacy/protection) |
| DA-K-018 | K-021 | Renumber (container orchestration/cloud-native) |
| DA-K-019 | K-022 | Renumber (backup/recovery/DR) |
| DA-K-020 | K-023 | Renumber (data lineage/provenance) |
| DA-K-021 | K-024 | Renumber (API design/data services) |
| DA-K-022 | K-025 | Renumber (event-driven architecture) |
| DA-K-023 | K-026 | Renumber (cloud cost/FinOps) |
| DA-K-024 | K-027 | Renumber (schema evolution/change management) |
| DA-K-025 | K-028 | Renumber (capacity planning/performance engineering) |
