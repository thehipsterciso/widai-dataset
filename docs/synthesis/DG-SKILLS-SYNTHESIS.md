# DG Skills — Re-Synthesis Analysis

## Domain: Data Governance & Policy
## Dimension: Skills
## Date: 2026-04-03

## Overview

DG Skills contains 9 Phase 1A baseline entries (origin_version 0.5.0). No post-STRM entries exist. Re-synthesis focuses on identifying internal duplicates within the Phase 1A baseline using cross-framework evidence.

Total STRM mappings: 13,426 across 6 frameworks.

## Evidence Matrix

| KSA ID | FW Cov | Strong | Total | Max STS |
|--------|--------|--------|-------|---------|
| DG-S-001 | 6/6 | 0 | 778 | 0.6121 |
| DG-S-002 | 6/6 | 17 | 2,423 | 0.8143 |
| DG-S-003 | 6/6 | 0 | 1,574 | 0.6857 |
| DG-S-004 | 6/6 | 0 | 1,150 | 0.6123 |
| DG-S-005 | 6/6 | 0 | 930 | 0.5989 |
| DG-S-006 | 6/6 | 0 | 1,978 | 0.6613 |
| DG-S-007 | 6/6 | 0 | 877 | 0.6458 |
| DG-S-008 | 6/6 | 3 | 1,827 | 0.7015 |
| DG-S-009 | 6/6 | 2 | 1,889 | 0.7141 |

All 9 entries have 6/6 framework coverage. S-002 (strategic alignment) is the evidence anchor — 17 strong matches, max STS 0.8143 from AIRMF-MP-1.4. This is the highest single-entry strong match count and max STS observed in any DG dimension.

## Phase 1A Duplicate Analysis

### Duplicate Group 1: S-003 + S-006 → Data Stewardship Programs

**S-003:** "Skill in designing data stewardship programs that assign clear ownership, accountability, and service level agreements for enterprise data domains."

**S-006:** "Skill in designing and running data stewardship programs, including steward selection, training, responsibility definition, and performance measurement."

**Overlap analysis:** Both are stewardship program skills. S-003 focuses on the design dimension — ownership assignment, accountability structures, SLAs. S-006 covers both design AND running — steward selection, training, responsibilities, and performance measurement. The "designing" in S-006 explicitly subsumes S-003's design scope (you cannot design steward selection, training, and responsibility definition without addressing ownership and accountability). S-006 adds the operational dimension (running, performance measurement) that S-003 lacks.

**Evidence confirmation:** S-003 has 1,574 mappings, S-006 has 1,978. They share many framework matches: NICE T1142 (validate data programs, 0.7023) maps to both, NICE S0933 (designing controls, 0.6664) maps to both, DCWF [5867] (data management policies, 0.6668) maps to both, DDaT-SK-076 (design sessions with stakeholders) maps to both. Framework elements do not distinguish between "designing stewardship ownership" and "designing stewardship selection/training" — they treat stewardship program design as a single concept.

**Decision:** Merge S-003 into S-006. The consolidated entry preserves the full stewardship lifecycle — design (ownership, accountability, SLAs) AND operation (selection, training, performance measurement).

### Duplicate Group 2: S-004 + S-005 → Data Governance Council Management

**S-004:** "Skill in building and managing a Data Governance Council, including membership design, decision authority, meeting cadence, escalation processes, and conflict resolution."

**S-005:** "Skill in operating data governance councils, including agenda management, issue escalation, decision documentation, and multi-stakeholder conflict resolution."

**Overlap analysis:** S-004 covers building and managing the council (structural design + ongoing management). S-005 covers operating the council (day-to-day operational execution). Both mention escalation and conflict resolution. In practice, the person who builds a governance council runs it — "managing" (S-004) and "operating" (S-005) describe the same ongoing responsibility at different levels of abstraction. Membership design (S-004) and agenda management (S-005) are sequential steps in the same workflow.

**Evidence confirmation:** S-004 has 1,150 mappings, S-005 has 930. They share overlapping framework matches: NICE T1679 (organizational decision support tools, 0.6457) maps to both, DCWF [5631] (multi-stakeholder analysis, 0.6835) maps to both, DDaT-SK-113 (managing data projects) maps to both. The evidence confirms these represent a single skill applied across the council lifecycle.

**Decision:** Merge S-004 and S-005 into a single council governance skill covering the full lifecycle — building (membership, authority), operating (agenda, cadence, issue tracking), and managing (escalation, documentation, conflict resolution).

## Entries Preserved Without Change

| Entry | Statement Summary | Rationale |
|-------|------------------|-----------|
| S-001 | Executive/board communication in business terms | Unique communication skill. Distinct audience (C-suite/board), distinct framing (financial/business language). |
| S-002 | Strategic alignment of data/AI programs | Unique strategic skill. Strongest evidence in all DG dimensions (17 strong, 0.8143 max STS). |
| S-007 | Governance program effectiveness measurement | Unique measurement/reporting skill. Maturity scores, compliance rates, issue metrics, participation rates. |
| S-008 | Business glossary/data dictionary authoring | Unique documentation skill. Distinct from metadata management (K-004) — this is the writing/maintaining skill, not the platform knowledge. |
| S-009 | Data/AI strategy recommendations and roadmaps | Unique advisory skill. Prioritized roadmaps, capability plans, org design recommendations. |

## Entry Mapping

| Old ID | Action | New ID | Notes |
|--------|--------|--------|-------|
| DG-S-001 | Preserved | DG-S-001 | Executive communication |
| DG-S-002 | Preserved | DG-S-002 | Strategic alignment |
| DG-S-003 | Merged → S-006 | DG-S-003 | Stewardship programs (consolidated) |
| DG-S-004 | Merged with S-005 | DG-S-004 | Governance council (consolidated) |
| DG-S-005 | Absorbed → S-004 | — | Absorbed into consolidated S-004 |
| DG-S-006 | Absorbed S-003 | DG-S-003 | Renumbered (was S-006, now S-003) |
| DG-S-007 | Preserved | DG-S-005 | Renumbered (was S-007) |
| DG-S-008 | Preserved | DG-S-006 | Renumbered (was S-008) |
| DG-S-009 | Preserved | DG-S-007 | Renumbered (was S-009) |

## Result

DG Skills: 9 → 7 entries (2 merges, 0 removals)
