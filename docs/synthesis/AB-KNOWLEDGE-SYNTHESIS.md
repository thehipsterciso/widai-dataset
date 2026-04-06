# AB Knowledge — Evidence-Driven Synthesis

## Overview

Domain: Analytics & BI (AB)
Dimension: Knowledge
Previous count: 29 (pre-evidence-first), then 25 (initial evidence-first), then **26** (after adversarial)
Final count: 26
Schema: 3.0.0
Methodology: Evidence-first synthesis per KSA-SYNTHESIS-METHODOLOGY.md v2.0.0

This synthesis was built entirely from cross-framework STRM evidence. Prior entries were not used as a starting point. Concepts were extracted from framework element descriptions, clustered, written as entries, then subjected to 3 adversarial passes with full element-by-element coverage mapping.

## Evidence Sources

| Framework | Elements at STS ≥ 0.50 | WIDAI-relevant | At STS ≥ 0.55 |
|-----------|----------------------|----------------|---------------|
| O*NET 30.2 | 4 | 1 | 0 |
| NIST NICE v2.1.0 | 274 | 195 | 121 |
| DoD DCWF v5.1 | 326 | 241 | 118 |
| UK DDaT | 22 | 21 | 3 |
| EU AI Act | 14 | 12 | 2 |
| NIST AI RMF 1.0 | 17 | 16 | 4 |
| **Total** | **657** | **486** | **~248** |

Total STRM mappings: 7,874

## Concept Clusters

26 distinct concept clusters extracted from the framework evidence:

### 1. Statistical Foundations
Descriptive statistics, inferential statistics, probability, statistical processes.
Evidence: O*NET [2.C.4.a], NICE [K1219], [K1339], [S0646], DCWF [75B], [6710], [6790A], DDaT [DDAT-SK-011]

### 2. Sampling Methodology
Sampling design, representativeness, margin of error, sample size.
Evidence: DCWF [6790A], EU AI Act [EUAIA-O-007], DDaT [DDAT-SK-011]

### 3. Mathematical Modeling and Quantitative Methods
Mathematical models, applied math, model design and validation.
Evidence: NICE [K1170], [K1086], [K1095], DCWF [5907], [8059], O*NET [2.C.4.a], DDaT [DDAT-SK-011]

### 4. Regression Analysis
OLS, GLM, tree-based methods, regularization, model diagnostics.
Evidence: DCWF [6651], [21A], NICE [K1170]

### 5. Data Analysis Tools and Platforms
Analytical software, automated analysis tools, computational environments.
Evidence: NICE [K1096], [K1100], [K0768], DCWF [4106], [3920]

### 6. Data Visualization
Visualization tools, chart design, visual encoding, communication through visuals.
Evidence: NICE [K0647], DDaT [DDAT-SK-067], [DDAT-SK-011]

### 7. Database Systems and Query Languages
DBMS principles, SQL, database theory, query optimization, database administration.
Evidence: NICE [K0992], [K0991], [K0704], [K0705], [K0707], [K0706], [K0867], [K0750], DCWF [34], [32], [910], [3092]

### 8. Data Collection and Gathering
Data sourcing, monitoring tools, systematic data acquisition.
Evidence: NICE [K1146], [K1247], [K1253], DCWF [3603], [7014]

### 9. Data Aggregation and Correlation
Combining data sources, statistical relationships, event correlation.
Evidence: NICE [K1144], [K1322], [K0817], [S0904], [S0909], DCWF [3382]

### 10. Data Processing and Transformation
Data manipulation, mapping, format conversion, cleansing.
Evidence: NICE [K1280], [K1148], [K1097], [K1246], [S0748], DCWF [6690]

### 11. Data Classification and Profiling
Data types, characteristics, taxonomies, fitness assessment.
Evidence: NICE [K0866], [K1281], [K1143], DCWF [1126]

### 12. Anomaly Detection and Continuous Monitoring
Automated anomaly detection, alerting, continuous monitoring systems.
Evidence: NICE [K1298] (STS 0.6634), [K1125] (STS 0.6102)

### 13. Root Cause and Diagnostic Analysis
Diagnostic techniques, causal investigation, fault identification.
Evidence: NICE [K0957] (STS 0.6493), DCWF [978A] (STS 0.6380), [128] (STS 0.6422)

### 14. Analytical Risk Quantification
Risk assessment techniques, risk metrics for business analytics.
Evidence: NICE [K1078] (STS 0.6571), DCWF [6931] (STS 0.6769 — highest DCWF element), [108]

### 15. Testing and Validation of Analytical Outputs
Validation methods, evaluation requirements, independent testing, quality assurance.
Evidence: NICE [K0772], [K1341], [K1165], [K1158], [K1342], [K1284], [K0881], [K0711], [S0842], DCWF [130], [6430], [7006A], [7004A], [3126], [1012A], [7004], [7044], DDaT [DDAT-SK-072], AI RMF [AIRMF-MP-2.3], [AIRMF-MS-2.1]
Note: Testing/validation is the single largest concept cluster by evidence density — 20+ elements across 4 frameworks.

### 16. Analytic Frameworks and Structured Analysis
Established frameworks, structured analytical methods, analytical constructs.
Evidence: NICE [K0968], [K0767], [K0727], DCWF [121], [3446], [62], [3689], [3692]

### 17. Performance Measurement and KPI Design
Measures of effectiveness, metric design, organizational performance tracking.
Evidence: DCWF [2066], [3606], [7038], DDaT [DDAT-SK-112]

### 18. Reporting and Information Management
Reporting standards, information management practices, knowledge management, communication systems.
Evidence: NICE [K1004], [K0999], [K0775], [K0864], [K1088], [T1240], DCWF [230], [135], [3181]

### 19. Research Methodology and Multi-Source Synthesis
Systematic investigation, information integration from diverse sources.
Evidence: NICE [S0900], DCWF [4491], [3505], [3603], [4490], [3382], [4407]

### 20. Simulation and Scenario Analysis
Simulation testing, scenario modeling, outcome prediction under uncertainty.
Evidence: NICE [K1338], DCWF [8059], [874], [506]

### 21. Business Modeling and Analytical Requirements
Translating business needs to analytical approaches, requirements analysis.
Evidence: DDaT [DDAT-SK-021], DCWF [16], [5925], NICE [K1286]

### 22. Data Model Design
Conceptual, logical, physical models, dimensional modeling, schema design for analytics.
Evidence: NICE [K1086], [K1095], [S0568], DCWF [7016], [7015], DDaT [DDAT-SK-056]

### 23. Algorithms and Computational Methods
Algorithm selection, computational approaches for analytical problem solving.
Evidence: NICE [K0694], [S0558], DCWF [21], [166], [4554]

### 24. Machine Learning Fundamentals for Analytics
ML principles applied to analytical problems, predictive analytics foundations.
Evidence: NICE [K0904], DCWF [21A], [7011], [7049], [7038], AI RMF [AIRMF-MS-2.9]

### 25. Privacy-Preserving Analytical Techniques
De-identification, anonymization, maintaining analytical utility under privacy constraints.
Evidence: NICE [K1323] (STS 0.6506)
Note: Single-framework evidence but at high STS. Borderline SP domain but scoped to maintaining analytical utility.

### 26. Data Asset Management and Valuation for Analytics *(Added by Pass 1)*
Data inventory, catalog practices, provenance tracking, organizational data landscape assessment, data valuation for analytical purposes.
Evidence: NICE [K0766] (STS 0.6373), [K0804] (STS 0.5875), [K1278] (STS 0.5830), [K0699] (STS 0.5775), [S0808] (STS 0.5556)
Note: 5 elements across STS 0.55–0.64. Distinct from data collection (008 — acquiring data), data classification (011 — profiling datasets), and database systems (007 — DBMS knowledge). This is organizational-level knowledge of data as a strategic asset for analytics. Borderline DG but scoped to analytical value assessment.

## Adversarial Pass Results

### Pass 1 — Coverage Gaps

All ~248 WIDAI-relevant elements at STS ≥ 0.55 were mapped to entries. The mapping used element concept descriptions, not STRM KSA ID mappings (entries 011–025 have 0/6 STRM coverage because STRM scores were computed against pre-rewrite entry text — the concepts are real but the current statements don't register in the old scoring).

**Gap found:** Data Asset Management and Valuation. Five NICE elements (K0766, K0804, K1278, K0699, S0808) describe knowledge of managing and valuing data as organizational assets. K0766 at STS 0.6373 is in the top quartile of all AB-K evidence. No existing entry covers this concept. Added as AB-K-026.

**Borderline concepts reviewed and not added:**
- Knowledge management (K0864, K1088, T1240, DCWF 230, 3464): 5 elements at STS 0.55–0.60. Currently folded into AB-K-018 (Reporting and Information Management) via "information management principles." Not distinct enough for a standalone entry.
- Data warehousing (K0702, DCWF 7015): Covered across AB-K-007 (database systems) and AB-K-022 (data model design — dimensional modeling).
- NLP/Text analytics (K0965, DCWF T1846): 2 elements at moderate STS. More AI domain than AB.
- Process maturity (K0869, DCWF 4517): Covered under AB-K-016 (analytic frameworks).

**+1 entry added.**

### Pass 2 — Redundancy and Overlap

All related pairs examined. Closest pairs with confirmed distinctions:

| Pair | Distinction |
|------|-------------|
| AB-K-001 (statistics) vs AB-K-002 (sampling) | Broad statistical foundations vs. specific sampling design methodology. DCWF 6790A calls out sampling as distinct. |
| AB-K-003 (mathematical modeling) vs AB-K-004 (regression) | General modeling methods vs. specific regression method family. K1170 ≠ 6651. |
| AB-K-003 (math modeling) vs AB-K-020 (simulation) | Modeling constructs vs. scenario-based outcome prediction under uncertainty. |
| AB-K-005 (analysis tools) vs AB-K-023 (algorithms) | Platform capabilities vs. computational methods. K1096 ≠ K0694. |
| AB-K-007 (database systems) vs AB-K-022 (data model design) | DBMS/SQL/query optimization vs. conceptual/logical/physical modeling for analytics. K0992 ≠ K1086. |
| AB-K-008 (data collection) vs AB-K-019 (research methodology) | Acquiring data vs. systematic multi-source investigation and synthesis. K1146 ≠ S0900. |
| AB-K-009 (aggregation) vs AB-K-010 (processing) | Combining data across sources vs. transforming/cleansing data. K1322 ≠ K1280. |
| AB-K-011 (classification) vs AB-K-026 (data asset mgmt) | Profiling individual datasets for fitness vs. organizational-level data inventory and valuation. |
| AB-K-017 (KPI design) vs AB-K-018 (reporting) | What to measure vs. how to communicate findings. 2066 ≠ K1004. |
| AB-K-024 (ML for analytics) vs AB-K-023 (algorithms) | ML-specific principles (training, bias/variance, model selection) vs. general computational methods. K0904 ≠ K0694. |

**No merges.**

### Pass 3 — Domain Boundary

All 26 entries reviewed for AB domain fit:

| Entry | Borderline Domain | AB Justification | Verdict |
|-------|------------------|-------------------|---------|
| AB-K-007 (database systems) | DA | SQL and DBMS for analytical querying — foundational AB. 12 framework elements. | Keep |
| AB-K-011 (classification/profiling) | DQ | Scoped to determining data fitness for analysis, not data quality governance. | Keep |
| AB-K-014 (risk quantification) | RM | Analytical techniques FOR risk assessment, not risk management as a discipline. DCWF 6931 at STS 0.6769. | Keep |
| AB-K-022 (data model design) | DA | Dimensional modeling for analytical query performance, not enterprise architecture. | Keep |
| AB-K-024 (ML for analytics) | AI | Scoped to ML applied within analytical workflows, not ML system development. | Keep |
| AB-K-025 (privacy-preserving) | SP | Scoped to maintaining analytical utility under privacy constraints. Single-source (K1323, STS 0.6506). Weakest by evidence density. | Keep (flagged) |
| AB-K-026 (data asset mgmt) | DG | Scoped to analytical value assessment, not data governance policy. | Keep |

**No entries removed.**

## STRM Coverage Note

The evidence matrix shows AB-K-001 through AB-K-010 at 6/6 framework coverage and AB-K-011 through AB-K-026 at 0/6. This is because STRM rationale scores were computed against pre-rewrite entry text. The rewritten statements are semantically different enough that the old scores don't map to them. The concepts for entries 011–026 are validated by manual element-by-element mapping (documented above), not by the automated evidence matrix.

## Final Entry List

| ID | Concept | Key Evidence |
|---|---|---|
| AB-K-001 | Statistical foundations | K1219, K1339, S0646, 75B, 6710 |
| AB-K-002 | Sampling methodology | 6790A, EUAIA-O-007, DDAT-SK-011 |
| AB-K-003 | Mathematical modeling and quantitative methods | K1170, K1086, 5907, 8059 |
| AB-K-004 | Regression analysis | 6651, 21A, K1170 |
| AB-K-005 | Data analysis tools and platforms | K1096, K1100, K0768, 4106 |
| AB-K-006 | Data visualization | K0647, DDAT-SK-067, DDAT-SK-011 |
| AB-K-007 | Database systems and query languages | K0992, K0991, K0704–K0707, 34, 32, 910 |
| AB-K-008 | Data collection and gathering | K1146, K1247, K1253, 3603 |
| AB-K-009 | Data aggregation and correlation | K1144, K1322, K0817, S0904 |
| AB-K-010 | Data processing and transformation | K1280, K1148, K1097, K1246 |
| AB-K-011 | Data classification and profiling | K0866, K1281, K1143, 1126 |
| AB-K-012 | Anomaly detection and continuous monitoring | K1298 (0.6634), K1125 (0.6102) |
| AB-K-013 | Root cause and diagnostic analysis | K0957 (0.6493), 978A (0.6380), 128 (0.6422) |
| AB-K-014 | Analytical risk quantification | K1078 (0.6571), 6931 (0.6769), 108 |
| AB-K-015 | Testing and validation of analytical outputs | 20+ elements across 4 FW |
| AB-K-016 | Analytic frameworks and structured analysis | K0968, K0767, 121, 3446, 62 |
| AB-K-017 | Performance measurement and KPI design | 2066, 3606, 7038, DDAT-SK-112 |
| AB-K-018 | Reporting and information management | K1004, K0999, K0775, K0864, K1088 |
| AB-K-019 | Research methodology and multi-source synthesis | S0900, 4491, 3505, 4490 |
| AB-K-020 | Simulation and scenario analysis | K1338, 8059, 874, 506 |
| AB-K-021 | Business modeling and analytical requirements | DDAT-SK-021, 16, 5925, K1286 |
| AB-K-022 | Data model design | K1086, K1095, S0568, 7016, DDAT-SK-056 |
| AB-K-023 | Algorithms and computational methods | K0694, S0558, 21, 166 |
| AB-K-024 | Machine learning fundamentals for analytics | K0904, 21A, 7011, 7049, AIRMF-MS-2.9 |
| AB-K-025 | Privacy-preserving analytical techniques | K1323 (0.6506) |
| AB-K-026 | Data asset management and valuation | K0766 (0.6373), K0804, K1278, K0699, S0808 |

## Methodology

Built from STRM rationale evidence per KSA-SYNTHESIS-METHODOLOGY.md v2.0.0. Existing entries discarded. Concepts extracted from 6 framework element descriptions, clustered, written as entries, then subjected to 3 adversarial passes (coverage gaps, redundancy, domain boundary). Pass 1 identified 1 gap (data asset management) — added as AB-K-026. No merges or removals after Passes 2 and 3. Final count: 26.
