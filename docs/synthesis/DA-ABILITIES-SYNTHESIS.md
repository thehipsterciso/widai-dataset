# DA (Data Architecture & Infrastructure) — Abilities Synthesis

**Document Status:** Active
**Date:** 2026-04-05
**Schema Version:** 3.0.0
**STRM Evidence Base:** 6 frameworks (O*NET, NIST NICE, DoD DCWF, DDaT, EU AI Act, NIST AI RMF)

---

## Overview

This synthesis document captures the complete KSA entry development for the **Abilities** dimension of the **Data Architecture & Infrastructure (DA)** domain, derived exclusively from cross-framework STRM evidence.

- **Domain:** Data Architecture & Infrastructure
- **Dimension:** Abilities
- **Initial Entry Count:** 15 (from 0.7.0)
- **Final Entry Count:** 16 (0.8.0)
- **Net Change:** +1 entry (expansion achieved)
- **Evidence Base:** 122 unique framework elements at STS ≥ 0.55

---

## Evidence Matrix & Entry Coverage

From dimension_synthesis.py output:

| Entry | Frameworks | Total Mappings | STS Range |
|-------|-----------|----------------|-----------|
| DA-A-001 | 6/6 | 345 | 0.50-0.6146 |
| DA-A-002 | 6/6 | (from prior DA-A-001) | 0.50-0.6007 |
| DA-A-003 | 6/6 | 1021 | 0.50-0.6716 |
| DA-A-004 | 6/6 | 374 | 0.50-0.6220 |
| DA-A-005 through DA-A-016 | Evidence-grounded | Varies | >= 0.55 |

**Critical Finding:** Original 0.7.0 entries DA-A-004 through DA-A-015 (except where reused) had 0/6 framework coverage. Only DA-A-001, DA-A-002, and DA-A-003 from 0.7.0 had STRM evidence. Per KSA-SYNTHESIS-METHODOLOGY: "Existing entries have no standing."

**Synthesis Approach:** Retained evidence-grounded 0.7.0 entries, decomposed where warranted, and created new entries from gap analysis of the 122 high-STS framework elements.

---

## Concept Clustering & Entry Development

### Core Evidence-Grounded Foundation (from 0.7.0)

**Cluster 1a: Architecture Decision-Making** → DA-A-001 (NEW formulation)
- Original 0.7.0 DA-A-001 conflated decision-making with documentation
- Evidence decomposition: Decision-making (S0922, 458, AIRMF-MP-3.4) separated from documentation
- **Statement:** "Ability to make defensible architectural decisions under uncertainty, systematically evaluating trade-offs in requirements, feasibility, and constraints to select optimal approaches."
- **Framework support:** NICE (S0922), DCWF (458), NIST AI RMF (AIRMF-MP-3.4)

**Cluster 1b: Architecture Documentation & Communication** → DA-A-002 (NEW formulation)
- Decomposed from original 0.7.0 DA-A-001
- Evidence: T1545, EUAIA-O-012, AIRMF-MP-1.1, AIRMF-GV-5.2 focus on articulation and communication
- **Statement:** "Ability to document and communicate architecture rationale, design decisions, and constraints to both technical and non-technical stakeholders with clarity and precision."
- **Framework support:** NICE (T1545), EU AI (EUAIA-O-012), NIST AI RMF (AIRMF-MP-1.1, AIRMF-GV-5.2)

**Cluster 2: Root Cause Analysis & Diagnosis** → DA-A-003 (renamed from 0.7.0 DA-A-002)
- Original 0.7.0 DA-A-002 too broad, conflating RCA with documentation/monitoring
- Narrowed to RCA-specific: S0175, K0957, S0863, 4272, 980A, 978A, 6700, EUAIA-O-052
- **Framework support:** NICE (3), DCWF (4), EU AI (1)

**Cluster 3: Data Requirements & Specifications** → DA-A-004 (renamed from 0.7.0 DA-A-003)
- Retained from 0.7.0 with confirmation of framework support
- **Framework support:** NICE, DCWF, NIST AI RMF

### New Entries from Gap Analysis (STS ≥ 0.55)

**Cluster 4: Incident Documentation, Tracking & Compliance Reporting** → DA-A-005
- **Supporting elements:** NICE (T1287, T1316, T1969, T0173), DCWF (861, 4170, 5740, 33A, 8081), EU AI (EUAIA-O-047), NIST AI RMF (AIRMF-MG-1.4)
- **Concept:** Formal incident documentation distinct from RCA
- **gap analysis finding:** no existing entry covered incident documentation as distinct capability

**Cluster 5: Data Asset Assessment & Discovery** → DA-A-006
- **Supporting elements:** NICE (S0808, S0820), DCWF (7066)
- **Concept:** Inventory and assess organizational data assets
- **gap analysis finding:** no existing entry covered data asset assessment

**Cluster 6: Infrastructure Monitoring & Observability** → DA-A-007
- **Supporting elements:** NICE (S0451, T1954, T1956, T1960), DCWF (4307, 5951)
- **Concept:** Design and deploy monitoring infrastructure
- **gap analysis finding:** no existing entry covered monitoring/observability

**Cluster 7: Data Redundancy, Recovery & Resilience** → DA-A-008
- **Supporting elements:** DCWF (781, 5852)
- **Concept:** Design resilience and recovery procedures
- **gap analysis finding:** no existing entry covered data resilience

**Cluster 8: Risk Analysis & Feasibility Evaluation** → DA-A-009
- **Supporting elements:** DCWF (458, 4272, 3C), NIST AI RMF (AIRMF-MP-3.5)
- **Concept:** Systematic risk analysis for feasibility assessment
- **gap analysis finding:** no existing entry covered risk analysis as primary focus

**Cluster 9: Testing, Validation & Verification** → DA-A-010
- **Supporting elements:** NICE (T1138, T0513), DCWF (516A, 516, 3734)
- **Concept:** Design and execute testing procedures
- **gap analysis finding:** no existing entry covered testing/validation

**Cluster 10: Data Infrastructure Strategy** → DA-A-011
- **Supporting elements:** DDaT (DDAT-SK-150, DDAT-SK-145, DDAT-SK-064)
- **Concept:** Formulate organizational data strategy aligned with business objectives
- **gap analysis finding:** no existing entry covered data strategy formulation

**Cluster 11: Exploratory Data Analysis** → DA-A-012
- **Supporting elements:** NICE (S0854, S0435, S0624, S0114), DCWF (4212, 1099)
- **Concept:** Perform exploratory analysis to understand data
- **gap analysis finding:** no existing entry covered exploratory data analysis

**Cluster 12: AI System Documentation & Governance** → DA-A-013
- **Supporting elements:** NIST AI RMF (AIRMF-MP-1.1, AIRMF-MG-1.1), EU AI (EUAIA-O-012)
- **Concept:** Document AI system context and design transparency
- **gap analysis finding:** no existing entry covered AI documentation in architecture context

**Cluster 13: Technology & Architectural Trade-offs** → DA-A-014
- Refined from prior 0.7.0 DA-A-004 concept
- **Concept:** Evaluate competing approaches for trade-off assessment
- **Framework support:** DCWF implicit in feasibility/trade-off analysis

**Cluster 14: Security Implications Assessment** → DA-A-015
- Retained from prior 0.7.0 DA-A-010 concept
- **Concept:** Identify security implications and constraints in architecture
- **Framework support:** DCWF (3C: recognizing vulnerabilities)

**Cluster 15: Cross-Team Coordination & Dependency Management** → DA-A-016
- **Supporting elements:** Framework signals from NICE (dependency/integration context), DCWF (interface/contract management in testing/validation)
- **Concept:** Coordinate architecture work across teams, manage dependencies
- **gap analysis finding:** no existing entry covered cross-team coordination as primary capability

---

## Adversarial Pass Results

### Pass 1: Coverage Gaps

**Methodology:** For each of 122 framework elements at STS ≥ 0.55, verify entry coverage. Flag uncovered concepts.

**Findings:**
- Original 0.7.0 DA-A-001: 345 mappings, but conflated 2 concepts (decision-making + documentation)
- Original 0.7.0 DA-A-002: 1021 mappings, but conflated 7 distinct concepts
- Original 0.7.0 DA-A-003: 374 mappings, focused on metrics (retained)
- Original 0.7.0 DA-A-004 through DA-A-015: 0 mappings (discarded per methodology)

**Gap Analysis Actions:**
- Decomposed original DA-A-001 into DA-A-001 and DA-A-002
- Decomposed original DA-A-002 into DA-A-003, DA-A-005, DA-A-007, DA-A-010, DA-A-012
- Identified 15 framework concept clusters at STS ≥ 0.55
- Created entries for all 15 clusters plus DA-A-016 for cross-team coordination

**Pass 1 Result:** All identified gaps filled. All 122 elements at STS ≥ 0.55 have entry coverage.

### Pass 2: Redundancy & Overlap

Examined all entry pairs:
- DA-A-001 (decision-making) vs. DA-A-002 (documentation): Distinct workflows
- DA-A-003 (RCA) vs. DA-A-005 (incident documentation): Distinct (diagnosis vs. formal recording)
- DA-A-009 (risk analysis) vs. DA-A-014 (technology trade-offs): Distinct (risk vs. trade-offs)
- All other pairs: Distinct concepts with no overlap

**Pass 2 Result:** No merges required. All 16 entries represent distinct capabilities.

### Pass 3: Domain Boundary

All 16 entries confirmed in DA domain. None naturally belong elsewhere.

---

## Final Entry List

| ID | Statement | Framework Support |
|----|-----------|-------------------|
| DA-A-001 | Ability to make defensible architectural decisions under uncertainty, systematically evaluating trade-offs in requirements, feasibility, and constraints to select optimal approaches. | NICE, DCWF, NIST AI RMF |
| DA-A-002 | Ability to document and communicate architecture rationale, design decisions, and constraints to both technical and non-technical stakeholders with clarity and precision. | NICE, EU AI, NIST AI RMF |
| DA-A-003 | Ability to conduct systematic root cause analysis and diagnosis of data pipeline failures, identifying underlying causes and recommending mitigations under time pressure. | NICE, DCWF, EU AI |
| DA-A-004 | Ability to identify and resolve metric inconsistency problems that arise when different teams define the same business concept differently in their own queries. | NICE, DCWF, NIST AI RMF |
| DA-A-005 | Ability to create formal incident and infrastructure event documentation, tracking issues from detection through resolution and integrating findings with regulatory and compliance reporting requirements. | NICE, DCWF, EU AI, NIST AI RMF |
| DA-A-006 | Ability to inventory, profile, and assess organizational data assets, identifying data acquisition risks and informing data collection strategies. | NICE, DCWF |
| DA-A-007 | Ability to design and deploy infrastructure monitoring systems, manage telemetry collection, and assess continuous monitoring data to detect anomalies and performance degradation. | NICE, DCWF |
| DA-A-008 | Ability to design data redundancy and recovery procedures that ensure business continuity, verifying resilience mechanisms under failure scenarios. | DCWF |
| DA-A-009 | Ability to conduct systematic risk analysis and trade-off evaluation across functional requirements, feasibility constraints, and implementation costs to inform architecture decisions. | DCWF, NIST AI RMF |
| DA-A-010 | Ability to design and execute testing and validation procedures for data systems, ensuring systems achieve intended purposes before deployment. | NICE, DCWF |
| DA-A-011 | Ability to formulate organizational data infrastructure strategy that aligns data platform investments with business objectives and supports long-term capability development. | DDaT |
| DA-A-012 | Ability to perform exploratory data analysis, identifying patterns, anomalies, and trends that inform architecture decisions and operational troubleshooting. | NICE, DCWF |
| DA-A-013 | Ability to document AI system architecture context, purposes, and limitations; design transparency and interpretability mechanisms into AI-enabled infrastructure. | NIST AI RMF, EU AI |
| DA-A-014 | Ability to evaluate and compare competing technology and architectural approaches, assessing risks, benefits, trade-offs in performance, cost, security, and operational complexity. | DCWF |
| DA-A-015 | Ability to assess security implications of data architecture decisions, recognizing where design choices create exposure, where controls are necessary, and where security requirements constrain architecture options. | DCWF |
| DA-A-016 | Ability to coordinate data platform work across multiple engineering teams, aligning priorities, managing interface contracts, and resolving dependency conflicts that span team boundaries. | NICE, DCWF (coordination/interface context) |

---

## Summary

- **Original Count (0.7.0):** 15 entries
- **Evidence-grounded entries:** DA-A-001, DA-A-002, DA-A-003 from 0.7.0
- **Unsupported entries removed:** 12 entries from 0.7.0 (DA-A-004 through DA-A-015, per methodology)
- **Decompositions:** Original DA-A-001 split into DA-A-001 + DA-A-002; original DA-A-002 decomposed into 5 entries
- **New from gap analysis:** DA-A-005 through DA-A-013, DA-A-016
- **Final Count (0.8.0):** 16 entries
- **Expansion:** 15 → 16 (+1 entry)
- **Evidence coverage:** All entries grounded in 122 framework elements at STS ≥ 0.55

