# DG Tasks — Re-Synthesis Analysis

## Domain: Data Governance & Policy
## Dimension: Tasks
## Date: 2026-04-03

## Overview

DG Tasks contains 15 Phase 1A baseline entries (origin_version 0.5.0). No post-STRM entries exist. Re-synthesis focuses on identifying internal duplicates within the Phase 1A baseline.

Total STRM mappings: 8,032 across 6 frameworks.

## Evidence Matrix

| KSA ID | FW Cov | Strong | Total | Max STS |
|--------|--------|--------|-------|---------|
| DG-T-001 | 5/6 | 0 | 214 | 0.5833 |
| DG-T-002 | 6/6 | 1 | 446 | 0.7158 |
| DG-T-003 | 6/6 | 0 | 288 | 0.5981 |
| DG-T-004 | 6/6 | 0 | 295 | 0.6877 |
| DG-T-005 | 6/6 | 0 | 928 | 0.6270 |
| DG-T-006 | 6/6 | 0 | 695 | 0.6883 |
| DG-T-007 | 6/6 | 1 | 1,245 | 0.7207 |
| DG-T-008 | 6/6 | 0 | 625 | 0.5903 |
| DG-T-009 | 6/6 | 0 | 646 | 0.6457 |
| DG-T-010 | 6/6 | 0 | 309 | 0.5834 |
| DG-T-011 | 6/6 | 0 | 82 | 0.5757 |
| DG-T-012 | 5/6 | 0 | 74 | 0.5507 |
| DG-T-013 | 6/6 | 0 | 579 | 0.6349 |
| DG-T-014 | 6/6 | 0 | 1,039 | 0.6755 |
| DG-T-015 | 6/6 | 0 | 567 | 0.6318 |

T-007 (post-deployment AI monitoring standards) has the richest evidence — 1,245 mappings, 1 strong match (DCWF [5868] at 0.7207). T-014 (strategy engagements) has the second highest with 1,039 mappings. T-011 and T-012 have the thinnest evidence (82 and 74 mappings respectively) but serve clear stewardship-level functions.

## Phase 1A Duplicate Analysis

No duplicates identified. Multiple pairs were examined and determined to represent tasks at legitimately different organizational levels or with distinct functional scopes.

### Pairs Examined and Preserved

**T-006 vs. T-011 — Enterprise Catalog vs. Domain Catalog Maintenance**
- T-006: "Establish and maintain the enterprise data catalog, business glossary, and metadata management program" (enterprise governance level)
- T-011: "Maintain the business glossary definitions, data asset catalog entries, and data lineage documentation for the assigned data domain" (domain steward level)
- **Decision:** Keep separate. T-006 is the enterprise program establishment and maintenance task. T-011 is the domain steward's operational maintenance within their assigned domain. Different organizational scope, different role holders. Legacy_ids confirm: T-006 from GOV-01.02 (governance program), T-011 from GOV-01.06 (data steward).

**T-008 vs. T-012 — Council Operation vs. Council Participation**
- T-008: "Operate the Data Governance Council, including scheduling, agenda preparation, issue tracking, decision logging" (council operator)
- T-012: "Participate in the data governance council and stewardship community, representing the assigned domain's interests" (domain representative)
- **Decision:** Keep separate. T-008 is the governance lead's operational task (runs the council). T-012 is the domain steward's participation task (represents their domain). Different roles with different accountability. Legacy_ids confirm: T-008 from GOV-01.04 (governance program manager), T-012 from GOV-01.06 (data steward).

**T-002 vs. T-014 — Strategy Development vs. Strategy Engagements**
- T-002: "Develop and maintain the enterprise data and AI strategy" (enterprise owner, ongoing)
- T-014: "Conduct data and AI strategy engagements, including current state assessment, future state design, gap analysis" (advisory, project-based)
- **Decision:** Keep separate. T-002 is the ongoing enterprise ownership task (develop AND maintain). T-014 is a discrete engagement pattern (assessment, design, gap analysis, roadmap). Different workflow patterns, different deliverable cadences. Legacy_ids confirm: T-002 from GOV-01.01 (CDAIO), T-014 from LDR-08.04 (advisory/consulting).

**T-013 vs. T-015 — Access Review/Approval vs. Access Processing**
- T-013: "Review and approve data access requests, data sharing agreements, and data use authorizations" (governance decision)
- T-015: "Process data access requests per defined procedures, including request validation, approval routing, provisioning" (operational processing)
- **Decision:** Keep separate. T-013 is the governance decision (review, approve — requires domain judgment). T-015 is the operational workflow (validate, route, provision, document — procedural execution). Different cognitive demands, different role levels.

**T-004 vs. T-008/T-009 — Program Establishment vs. Component Operation**
- T-004: "Establish and operate the enterprise data governance program, including council structure, policy library, stewardship network, data domain ownership registry, and governance metrics" (composite, program-level)
- T-008: Council operation (component)
- T-009: Stewardship network management (component)
- **Decision:** Keep all three. T-004 is the composite program-level task. T-008 and T-009 are detailed operational tasks for specific components. WIDAI maintains tasks at multiple granularity levels — the composite serves senior role descriptions, the components serve operational job analysis.

## Result

DG Tasks: 15 → 15 entries (validated, no changes needed)
