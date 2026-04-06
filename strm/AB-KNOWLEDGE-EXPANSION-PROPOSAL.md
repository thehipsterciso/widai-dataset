# AB Knowledge Domain — Expansion Proposal

**Date:** 2026-04-03
**Current state:** 10 KSAs (AB-K-001 through AB-K-010)
**Proposed state:** 29 KSAs
**Method:** Cross-framework synthesis of 250 analytics-relevant knowledge elements from NICE (128) and DCWF (122) at STS ≥ 0.50, clustered by distinct concept, filtered to AB domain scope

---

## Why 29

The high watermark analysis shows NICE carries 128 and DCWF carries 122 analytics-relevant knowledge elements at meaningful STS against the current 10 AB-K KSAs. After removing concepts that belong to other WIDAI domains (DA for data architecture, DG for governance, DQ for quality) and deduplicating cross-framework overlaps, 28 distinct knowledge concept clusters emerge. Written at WIDAI's compound-statement granularity, these produce 29 KSAs — in line with AI Knowledge (29 KSAs) and proportional to the conceptual surface area of analytics and BI as a professional discipline.

The current 10 are not wrong. They are compressed. This proposal decompresses them and fills the gaps the synthesis identified.

---

## Proposed AB Knowledge KSAs (29)

### Statistical Foundations (4 KSAs — was 2)

**AB-K-001** Knowledge of descriptive statistics, including measures of central tendency, dispersion, distribution shape, and correlation, and how to interpret each in a business context.
*STATUS: UNCHANGED from current AB-K-001*
*Evidence: NICE K1144 (STS 0.6863), K1339 (0.6457), K1219 (0.6450); DCWF 6710 (0.6441), 75B (0.6402)*

**AB-K-002** Knowledge of inferential statistics, including hypothesis testing, confidence intervals, p-values, effect sizes, and the distinction between statistical significance and practical significance.
*STATUS: NEW — extracted from current AB-K-008's compound scope*
*Evidence: NICE K1219 "statistical processes" (0.6649), K1339 "statistical principles" (0.6457); DCWF 75B "statistics" (0.6402)*

**AB-K-003** Knowledge of probability theory and distributions, including common parametric and non-parametric distributions, their properties, and selection criteria for modeling business phenomena.
*STATUS: NEW — gap signal. Current AB-K-001 mentions "distribution shape" but doesn't cover distribution theory.*
*Evidence: NICE K1170 "mathematical models" (0.6780); DCWF 75 "mathematics including statistics" (0.5387)*

**AB-K-004** Knowledge of sampling methodology, including probability and non-probability sampling designs, sample size determination, margin of error calculation, and the impact of sampling choices on inference validity.
*STATUS: NEW — gap signal identified in v0.6.2 synthesis as "survey and primary data collection methodology"*
*Evidence: NICE K1342 "training, validation, and test data sets" (0.6381); DCWF 7006A "test design activities" (0.6339)*

### Analytical Methods (5 KSAs — was 2)

**AB-K-005** Knowledge of common analytical frameworks, including cohort analysis, funnel analysis, segmentation, time series decomposition, and root cause analysis, and when to apply each to business questions.
*STATUS: REFINED from current AB-K-003 — removed A/B test interpretation (now in experimentation cluster), added root cause analysis*
*Evidence: NICE K1101 "analytics" (0.6672), K0968 "analytic standards and frameworks" (0.6442), K0957 "root cause analysis" (0.6493); DCWF 4106 "analytic tools and techniques" (0.6327)*

**AB-K-006** Knowledge of regression methods, including ordinary least squares, generalized linear models, mixed effects models, and regularization approaches, and their assumptions and diagnostic procedures.
*STATUS: NEW — decomposed from current AB-K-008 which packed regression, survival, Bayesian, and simulation into one statement*
*Evidence: NICE K1170 "mathematical models" (0.6780), K1096 "data analysis tools" (0.6625); DCWF 21A "statistical/machine learning algorithms" (0.6151)*

**AB-K-007** Knowledge of time series forecasting methods, including ARIMA, exponential smoothing, seasonal decomposition, and the evaluation of forecast accuracy, and how to communicate forecast uncertainty to business stakeholders.
*STATUS: NEW — decomposed from current AB-K-004 which merged forecasting with clustering and regression*
*Evidence: NICE K1338 "simulation testing" (0.6395), K0817 "event correlation" (0.6494); DCWF 6931 "methods and techniques for analyzing risk" (0.6769)*

**AB-K-008** Knowledge of clustering and segmentation methods, including k-means, hierarchical clustering, DBSCAN, and latent class analysis, and how to validate and interpret cluster solutions for business application.
*STATUS: NEW — decomposed from current AB-K-004*
*Evidence: NICE K1322 "data aggregation" (0.6693), K0866 "data classification" (0.6298); DCWF 121 "structured analysis principles" (0.6190)*

**AB-K-009** Knowledge of multivariate analysis techniques, including principal component analysis, factor analysis, and discriminant analysis, and their application to dimensionality reduction and variable selection.
*STATUS: NEW — gap signal. No current AB-K covers dimensionality reduction or feature selection from the analytics perspective.*
*Evidence: NICE K1096 "data analysis tools" (0.6726), K1100 "analytical tools" (0.6713); DCWF 62 "analysis principles and methods" (0.5656)*

### Causal & Experimental Methods (3 KSAs — was 2)

**AB-K-010** Knowledge of A/B testing and experimentation design, including sample size calculation, randomization methods, guardrail metric selection, and statistical significance interpretation.
*STATUS: UNCHANGED from current AB-K-005*
*Evidence: NICE K1342 (0.6381), K0772 "systems testing and evaluation" (0.6318); DCWF 7006A (0.6339), 130 (0.6328), 6430 (0.6324)*

**AB-K-011** Knowledge of causal inference methods, including difference-in-differences, instrumental variables, regression discontinuity, and propensity score matching, and the identification assumptions each requires.
*STATUS: UNCHANGED from current AB-K-009*
*Evidence: NICE K1144 (0.6863), K0817 (0.6494); DCWF 6931 (0.6769)*

**AB-K-012** Knowledge of advanced experimentation approaches, including multi-armed bandits, Bayesian optimization, sequential testing, and switchback designs, and when each is preferred over classical A/B testing.
*STATUS: NEW — gap signal. Current AB-K-005 covers classical A/B only. Modern analytics orgs use adaptive experimentation.*
*Evidence: NICE K1338 "simulation testing" (0.6395), K1298 "anomaly detection" (0.6634); DCWF 7011 "performance analysis models" (0.6250)*

### Data Visualization & Communication (3 KSAs — was 1)

**AB-K-013** Knowledge of data visualization best practices, including chart type selection, cognitive load principles, color accessibility, and the difference between exploratory and explanatory visualization.
*STATUS: UNCHANGED from current AB-K-002*
*Evidence: NICE K0647 "data visualization tools" (0.6607); DCWF 7031 "how to structure and display data" (0.5994)*

**AB-K-014** Knowledge of data storytelling principles, including narrative structure for analytical findings, audience-appropriate framing, the use of context and comparison to drive interpretation, and the distinction between informing and persuading with data.
*STATUS: NEW — gap signal identified in v0.6.2 synthesis. DCWF explicitly has 7032 "how to use data to tell a story."*
*Evidence: DCWF 7032 "how to use data to tell a story" (0.5830), 3603 "methods of producing intelligence" (0.6244); NICE K1004 "reporting policies" (0.6098)*

**AB-K-015** Knowledge of dashboard design principles, including information hierarchy, interactive filtering patterns, real-time vs. batch refresh trade-offs, and the design of self-service analytical experiences.
*STATUS: NEW — current AB-K-006 combines platform capabilities with dashboard design. This separates the design knowledge.*
*Evidence: NICE K0647 (0.6607), K1247 "data monitoring" (0.6565); DCWF 7031 (0.5994), 3181 "reporting databases and tools" (0.5638)*

### BI Platforms & Architecture (3 KSAs — was 1)

**AB-K-016** Knowledge of BI platform capabilities and architecture, including data connectivity, semantic layer design, calculated field logic, and the trade-offs between different platform approaches (e.g., Power BI, Tableau, Looker, MicroStrategy).
*STATUS: REFINED from current AB-K-006 — narrowed to platform architecture, separated governance and performance*
*Evidence: NICE K0707 "database systems and software" (0.6308), K0705 "query language capabilities" (0.6525); DCWF 34 "database systems" (0.6251)*

**AB-K-017** Knowledge of BI performance optimization, including query tuning, data model design patterns (star schema, snowflake, wide table), incremental refresh strategies, and aggregation table design.
*STATUS: NEW — decomposed from current AB-K-006's compound scope*
*Evidence: NICE K0646 "system optimization techniques" (0.6343), K0064 "performance tuning" (0.5569); DCWF 96 "performance tuning" (0.5534)*

**AB-K-018** Knowledge of semantic layer and metrics layer architecture, including centralized metric definitions, dimension modeling, and the role of metrics stores in ensuring analytical consistency across an organization.
*STATUS: NEW — gap signal. Metrics layers (dbt metrics, Looker LookML, AtScale) are central to modern BI but absent from current AB-K.*
*Evidence: NICE K0968 "analytic standards and frameworks" (0.6442); DCWF 28 "data standardization policies" (0.5720)*

### BI Governance (2 KSAs — was 1)

**AB-K-019** Knowledge of BI governance practices, including report certification, content lifecycle management, access control, and version control for BI assets.
*STATUS: UNCHANGED from current AB-K-007*
*Evidence: NICE K0992 (0.6798), K0991 (0.6748), K0704 (0.6653), K0685 (0.6564); DCWF 7080 (0.6258), 3092 (0.6246)*

**AB-K-020** Knowledge of data literacy program design, including analytical skill assessment, tiered training approaches, self-service enablement strategies, and the organizational change management required to build data-driven decision cultures.
*STATUS: NEW — gap signal. BI governance without data literacy is incomplete. DCWF and DDaT both reference capability building.*
*Evidence: NICE K0881 "learning assessment" (0.6163); DCWF 3126 "assessment techniques" (0.6272); DDaT "Capability building for digital, data and technology" (0.4430)*

### Monitoring & Measurement (3 KSAs — was 0)

**AB-K-021** Knowledge of metrics and KPI design, including leading vs. lagging indicators, metric decomposition trees, measurement validity and reliability, and the governance of metric definitions across business units.
*STATUS: NEW — gap signal identified in v0.6.2 synthesis*
*Evidence: NICE K1247 "data monitoring" (0.6565), K0740 "system performance indicators" (0.5368); DCWF 76 "measures or indicators of system performance" (0.5084), 2066 "measures of effectiveness and measures of performance" (0.6126)*

**AB-K-022** Knowledge of anomaly detection methods for business data, including statistical process control, change point detection, and automated alerting threshold design, and how to distinguish signal from noise in operational metrics.
*STATUS: NEW — NICE explicitly has K1298 "anomaly detection." Current AB-K-010 mentions it as one bullet in embedded analytics.*
*Evidence: NICE K1298 "anomaly detection" (0.6634), K1125 "continuous monitoring" (0.6102); DCWF 978A "root cause analysis techniques" (0.6380)*

**AB-K-023** Knowledge of data profiling and data quality assessment methods, including completeness, consistency, timeliness, and accuracy measurement, and how data quality impacts analytical validity and business decisions.
*STATUS: NEW — gap signal identified in v0.6.2 synthesis. Prerequisite to reliable analytics.*
*Evidence: NICE K1281 "data types and characteristics" (0.6054), K0862 "data remediation" (0.5753), K0866 "data classification" (0.6298); DCWF 1126 "data classification standards" (0.5684)*

### Embedded & Advanced Analytics (3 KSAs — was 1)

**AB-K-024** Knowledge of embedded analytics patterns, including in-application analytics, programmatic report distribution, analytics APIs, and the design considerations for embedding analytical capabilities into operational workflows.
*STATUS: REFINED from current AB-K-010 — separated embedded from augmented analytics*
*Evidence: NICE K0948 "embedded systems" (0.6487), K0768 "automated systems analysis" (0.6674); DCWF 43A "embedded systems" (0.6418)*

**AB-K-025** Knowledge of augmented analytics capabilities, including AI-assisted insight generation, natural language querying, automated anomaly detection, and their impact on self-service BI adoption and analytical workflow.
*STATUS: REFINED from current AB-K-010 — the augmented half*
*Evidence: NICE K1100 "analytical tools" (0.6713), K1005 "intelligence collection capabilities" (0.6730); DCWF 4106 "analytic tools" (0.6616)*

**AB-K-026** Knowledge of geospatial analytics concepts, including spatial data types, geocoding, spatial joins, choropleth and heat map design, and the integration of location intelligence into business analysis.
*STATUS: NEW — NICE explicitly has K1104 "geospatial data analysis." Geospatial is a distinct analytical discipline.*
*Evidence: NICE K1104 "geospatial data analysis" (0.5794); DCWF 4591 (0.6133)*

### Analytics Ethics & Responsibility (2 KSAs — was 0)

**AB-K-027** Knowledge of analytical bias types, including selection bias, survivorship bias, confirmation bias, and Simpson's paradox, and how each manifests in business analytics and can mislead decision-making.
*STATUS: NEW — gap signal identified in v0.6.2 synthesis. EU AI Act and NIST AI RMF emphasize fairness/bias.*
*Evidence: NIST AI RMF "AI systems evaluated for trustworthy characteristics" (0.5809); DCWF 7052 "risk and bias assessment" (0.5683), 7041 "remedies against unintended bias" (0.5073)*

**AB-K-028** Knowledge of responsible analytics practices, including the ethical use of behavioral data, privacy-preserving analytical methods (k-anonymity, differential privacy), and the organizational obligation to communicate analytical uncertainty and limitations.
*STATUS: NEW — gap signal. Analytics ethics distinct from AI ethics (covered in AI domain).*
*Evidence: NICE K1323 "data de-identification" (0.6506); DCWF 7052 (0.5683); EU AI Act "Data and data governance" (0.5006)*

### Decision Science (1 KSA — was 0)

**AB-K-029** Knowledge of decision science concepts, including decision frameworks under uncertainty, cost-benefit and trade-off analysis, scenario modeling, and the role of analytical evidence in organizational decision-making processes.
*STATUS: NEW — DCWF explicitly has 3572 "organization decision support tools and methods." Analytics exists to inform decisions.*
*Evidence: DCWF 3572 "organization decision support" (0.5210), 3606 "assess performance and impact" (0.6044); NICE K1286 "Business Impact Analysis" (0.5977), K1020 "organization decision support" (0.5293)*

---

## Mapping from Current to Proposed

| Current | Disposition | Proposed |
|---------|------------|----------|
| AB-K-001 (descriptive stats) | Unchanged | AB-K-001 |
| AB-K-002 (visualization) | Unchanged | AB-K-013 |
| AB-K-003 (analytical frameworks) | Refined | AB-K-005 |
| AB-K-004 (advanced methods) | Decomposed | AB-K-007 (forecasting), AB-K-008 (clustering), AB-K-009 (multivariate) |
| AB-K-005 (A/B testing) | Unchanged | AB-K-010 |
| AB-K-006 (BI platforms) | Decomposed | AB-K-016 (architecture), AB-K-017 (performance), AB-K-018 (metrics layer) |
| AB-K-007 (BI governance) | Unchanged | AB-K-019 |
| AB-K-008 (statistical modeling) | Decomposed | AB-K-002 (inferential), AB-K-003 (probability), AB-K-006 (regression) |
| AB-K-009 (causal inference) | Unchanged | AB-K-011 |
| AB-K-010 (embedded/augmented) | Split | AB-K-024 (embedded), AB-K-025 (augmented) |

**5 current KSAs preserved unchanged**, **2 refined**, **3 decomposed** into 8, **19 net new** (12 decomposition products + 7 genuine gap fills).

---

## Comparison to AI Knowledge Structure

| Metric | AI Knowledge | AB Knowledge (proposed) |
|--------|:-----------:|:----------------------:|
| Total KSAs | 29 | 29 |
| Concept clusters | ~8 (ML, NLP, CV, MLOps, Cloud, Platforms, Research, Strategy) | ~9 (Stats, Methods, Causal, Viz, BI Platform, BI Gov, Monitoring, Advanced, Ethics) |
| Avg elements per cluster | 3.6 | 3.2 |
| Max cluster size | 7 (MLOps/Cloud) | 5 (Analytical Methods) |

---

## Framework Evidence Summary

| Framework | Elements matching current 10 AB-K at STS ≥ 0.50 | Analytics-relevant after filtering |
|-----------|:------------------------------------------------:|:----------------------------------:|
| NICE | 220 | 128 |
| DCWF | 211 | 122 |
| O*NET | 4 | 4 |
| DDaT | 22 | ~10 |
| EU AI Act | 14 | ~5 |
| NIST AI RMF | 17 | ~8 |
| **Combined** | **488** | **~277** |

277 analytics-relevant elements across 6 frameworks → 29 WIDAI KSAs = ~9.6 source elements per KSA. That's well within the typical WIDAI subsumption ratio observed in other domains.

---

## Next Steps

1. **Review and approve** this proposal structure
2. **Write the 29 KSA statements** in full WIDAI format with provenance
3. **Re-run all 6 STRMs** against the expanded AB-K pool to validate improved coverage
4. **Cross-domain audit** — verify no overlap with DA (data architecture), DG (governance), DQ (quality), or AI domain KSAs
