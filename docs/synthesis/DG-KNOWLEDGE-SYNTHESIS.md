# DG Knowledge — Re-Synthesis Analysis

## Domain: Data Governance & Policy
## Dimension: Knowledge
## Date: 2026-04-03

## Overview

DG Knowledge contains 11 Phase 1A baseline entries (origin_version 0.5.0). No post-STRM entries exist — this domain was never expanded. Re-synthesis focuses on identifying internal duplicates within the Phase 1A baseline using cross-framework evidence.

Total STRM mappings: 13,184 across 6 frameworks.

## Evidence Matrix

| KSA ID | FW Cov | Strong | Total | Max STS |
|--------|--------|--------|-------|---------|
| DG-K-001 | 6/6 | 1 | 1,828 | 0.7234 |
| DG-K-002 | 6/6 | 6 | 2,224 | 0.7404 |
| DG-K-003 | 6/6 | 0 | 824 | 0.6301 |
| DG-K-004 | 6/6 | 0 | 1,779 | 0.6919 |
| DG-K-005 | 6/6 | 0 | 586 | 0.5858 |
| DG-K-006 | 6/6 | 0 | 1,210 | 0.6997 |
| DG-K-007 | 6/6 | 0 | 1,239 | 0.6515 |
| DG-K-008 | 6/6 | 2 | 892 | 0.7237 |
| DG-K-009 | 6/6 | 0 | 268 | 0.6721 |
| DG-K-010 | 6/6 | 1 | 1,034 | 0.7007 |
| DG-K-011 | 6/6 | 3 | 1,300 | 0.7299 |

All 11 entries have 6/6 framework coverage. K-002 (enterprise risk management) is the evidence anchor with 6 strong matches (max STS 0.7404 from AIRMF-MP-4.1).

## Phase 1A Duplicate Analysis

### Duplicate Group 1: K-003 + K-007 → Governance Program Design

**K-003:** "Knowledge of data governance operating models, including federated, centralized, and hub-and-spoke structures, and the organizational conditions under which each model is appropriate."

**K-007:** "Knowledge of data governance program design, including operating model options, council structures, policy frameworks, stewardship network models, and escalation path architectures."

**Overlap analysis:** K-003 focuses exclusively on operating model structures (federated, centralized, hub-and-spoke). K-007 covers the full program design scope which explicitly includes "operating model options" alongside council structures, policy frameworks, stewardship networks, and escalation paths. K-007 is a superset of K-003 — every aspect of K-003 (operating model selection based on organizational conditions) is a component of K-007's broader program design scope.

**Evidence confirmation:** Both entries share heavy overlap in framework matches. NICE K0700 (data standardization policies, STS 0.7237) maps to both. DCWF [28] (data administration and standardization, STS 0.7299) maps to both. DDaT-SK-052/053 (data governance standards/processes) map to both. The framework elements do not distinguish between "operating model knowledge" and "program design knowledge" — they treat them as a single concept area.

**Decision:** Merge K-003 into K-007. The consolidated entry preserves K-007's broader program design scope while incorporating K-003's emphasis on organizational conditions driving model selection.

### Duplicate Group 2: K-004 + K-011 → Metadata, Catalog & Business Glossary

**K-004:** "Knowledge of data catalog and metadata management platforms, including active metadata principles, automated lineage tracking, and business glossary governance."

**K-011:** "Knowledge of metadata standards, business glossary conventions, and data catalog tooling used to document and publish data asset definitions."

**Overlap analysis:** Core scope is shared — both address data catalogs, metadata management, and business glossaries. K-004 frames this from a platform/governance perspective (active metadata, lineage tracking, glossary governance). K-011 frames it from a standards/documentation perspective (standards, conventions, tooling for publishing definitions). In practice, metadata management platforms implement metadata standards, and business glossary governance (K-004) encompasses business glossary conventions (K-011). Neither entry addresses a concept absent from the other — the distinction is viewpoint (governance vs. documentation), not substance.

**Evidence confirmation:** K-004 has 1,779 mappings, K-011 has 1,300. They share many top framework matches: NICE K1151 (digital evidence cataloging, 0.7153) maps to both, NICE K0706 (database schema, 0.6978) maps to both, DCWF [3298] (metadata extraction, 0.6810) maps to both, DCWF [5864] (data catalogs/dictionaries, 0.6694) maps to both. K-011 has 3 strong matches vs K-004's 0, but the shared mapping density confirms these are the same concept area.

**Decision:** Merge K-004 and K-011 into a single entry covering metadata management platforms AND standards, including active metadata, lineage tracking, business glossary governance, catalog tooling, and data asset definition publishing.

## Entries Preserved Without Change

| Entry | Statement Summary | Rationale |
|-------|------------------|-----------|
| K-001 | Enterprise data strategy frameworks | Broader than K-003/K-007 — strategy + architecture + interdependencies. Not a duplicate. |
| K-002 | Enterprise risk management, data/AI/tech risk integration | Unique scope. 6 strong matches, highest evidence density. |
| K-005 | Data maturity assessment frameworks (DCAM, DAMA, CMMI-DMM) | Unique scope. Specific to maturity models and investment prioritization. |
| K-006 | AI model lifecycle management | Unique scope. Covers versioning, drift, monitoring, retraining, decommissioning in governance context. |
| K-008 | Data policy authoring | Unique scope. Covers policy structure, enforcement, exceptions, lifecycle. |
| K-009 | Data domain and ownership concepts | Unique scope. Methodological knowledge — how to define domains, assign accountability, resolve disputes. |
| K-010 | Data domain contextual knowledge | Unique scope. Applied knowledge — business purpose, sources, consumers, regulatory classifications for assigned domain. |

## Entry Mapping

| Old ID | Action | New ID | Notes |
|--------|--------|--------|-------|
| DG-K-001 | Preserved | DG-K-001 | Enterprise data strategy frameworks |
| DG-K-002 | Preserved | DG-K-002 | Enterprise risk management |
| DG-K-003 | Merged → K-007 | DG-K-003 | Governance program design (consolidated) |
| DG-K-004 | Merged with K-011 | DG-K-004 | Metadata, catalog & business glossary (consolidated) |
| DG-K-005 | Preserved | DG-K-005 | Data maturity assessment |
| DG-K-006 | Preserved | DG-K-006 | AI model lifecycle |
| DG-K-007 | Absorbed K-003 | DG-K-003 | Renumbered (was K-007, now K-003) |
| DG-K-008 | Preserved | DG-K-007 | Renumbered (was K-008) |
| DG-K-009 | Preserved | DG-K-008 | Renumbered (was K-009) |
| DG-K-010 | Preserved | DG-K-009 | Renumbered (was K-010) |
| DG-K-011 | Merged → K-004 | — | Absorbed into consolidated K-004 |

## Result

DG Knowledge: 11 → 9 entries (2 merges, 0 removals)
