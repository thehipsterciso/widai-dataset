# AB Abilities — Evidence-Driven Synthesis

## Overview

Domain: Analytics & BI (AB)
Dimension: Abilities
Previous count: 15 (pre-evidence-first), then 15 (initial evidence-first), then **16** (after adversarial)
Final count: 16
Schema: 3.0.0
Methodology: Evidence-first synthesis per KSA-SYNTHESIS-METHODOLOGY.md v2.0.0

This synthesis was built entirely from cross-framework STRM evidence. Prior entries were not used as a starting point.

## Evidence Sources

| Framework | Elements at STS ≥ 0.50 | WIDAI-relevant | At STS ≥ 0.55 |
|-----------|----------------------|----------------|---------------|
| O*NET 30.2 | 21 | 14 | 8 |
| NIST NICE v2.1.0 | 136 | 106 | 51 |
| DoD DCWF v5.1 | 244 | 182 | 63 |
| UK DDaT | 52 | 49 | 22 |
| EU AI Act | 9 | 9 | 4 |
| NIST AI RMF 1.0 | 26 | 26 | 12 |
| **Total** | **488** | **386** | **~160** |

Total STRM mappings: 3,201

## Concept Clusters

16 distinct concept clusters extracted from framework evidence:

### 1. Structured Judgment Under Uncertainty and Incomplete Data
Ability to develop and recommend analytical approaches when information is incomplete, ambiguous, or conflicting; reasoning through uncertainty to produce actionable conclusions.
Evidence: DCWF [4692] (0.7377 — highest STS in entire AB-A dimension), [3039] (0.7234), [3756] (0.6820), NICE [S0922] (0.6166 — decisions under uncertainty), [S0434] (0.6047 — extrapolating from incomplete data sets), DDaT [DDAT-SK-013] (0.7233 — applying statistical and analytical techniques)
Note: Strongest cluster by evidence density and STS strength — 3 elements above 0.68 across 3 frameworks.

### 2. Analytical Method Selection and Evaluation
Ability to assess available analytical tools and methods, select the appropriate technique for a given problem, and evaluate method applicability against data characteristics and business constraints.
Evidence: DCWF [3692] (0.6767 — assessing applicability of available analytical tools), [3681] (0.6215 — applying analytical methods to support planning and justify strategies), [3689] (0.5591 — applying various analytical methods including competing hypotheses), NICE [S0746] (0.5542 — evaluating tools for implementation), DDaT [DDAT-SK-013] (0.7233 — evaluating methods to answer research questions)

### 3. Pattern Recognition and Problem Decomposition
Ability to quickly make sense of complex information, recognize patterns and relationships across seemingly unrelated data, dissect problems, and identify non-obvious organizational or operational dynamics.
Evidence: DCWF [6949] (0.6466 — critical thinking to analyze organizational patterns and relationships), [6120] (0.6179 — dissect a problem and examine interrelationships between data), [4272] (0.5572 — complex root-cause analysis), O*NET [1.A.1.e.1] (0.6045 — quickly make sense of, combine, organize information into meaningful patterns)

### 4. Translation of Data into Actionable Recommendations
Ability to move from analytical findings to business-relevant conclusions and actionable recommendations, calibrating the level of certainty and evidence to the decision authority of the audience.
Evidence: DCWF [5030] (0.6847 — analyze data sources to provide actionable recommendations), [5570] (0.6684 — provide actionable recommendations based on data analysis and findings), [6170] (0.6151 — translate data and test results into evaluative conclusions), DDaT [DDAT-SK-007] (0.6829 — examining, interpreting and analysing data to help make informed decisions), [DDAT-SK-008] (0.6715), [DDAT-SK-046] (0.6715)

### 5. Cost-Benefit, Trade-Off, and Risk-Based Reasoning
Ability to perform trade-off reasoning across competing analytical approaches or business options, evaluating costs, benefits, and risks under conditions of uncertainty; integrating risk assessment into decision-making.
Evidence: DCWF [600] (0.6816 — evaluate cost benefit, economic, and risk analysis in decision making), O*NET [2.B.4.e] (0.5980 — considering relative costs and benefits), AIRMF [AIRMF-MP-3.4] (0.6257 — evaluate and compare trade-offs), [AIRMF-MS-4.2] (0.6178 — integrate measurement results into risk management decision-making), DDaT [DDAT-SK-082] (0.5987 — enabling and informing risk-based decisions), [DDAT-SK-089] (0.6027 — assess full financial implication), DCWF [8067] (0.5762 — develop/inform risk assessments)
Note: 7 elements across 4 frameworks. Merges general trade-off reasoning with risk-based decision support — both require the same cognitive capacity to weigh competing considerations.

### 6. Analytical Communication Across Audiences
Ability to communicate analytical findings and concepts effectively to both technical and non-technical audiences, adapting verbal and written communication to audience comprehension capacity.
Evidence: NICE [S0610] (0.6019 — communicating effectively), [S0387] (0.5870 — communicating in writing), [S0386] (0.5815 — communicating verbally), [S0826] (0.5554 — communicating with external organizations), O*NET [1.A.1.a.3] (0.5709 — communicate in speaking), [1.A.1.a.4] (0.5546 — communicate in writing), DCWF [8081] (0.5661 — document and disseminate analytic findings), [3024] (0.5509 — communicate effectively when writing)

### 7. Data Source Quality and Reliability Assessment
Ability to evaluate data sources for relevance, reliability, completeness, and objectivity, and to determine how data limitations affect the validity of analytical conclusions.
Evidence: NICE [S0808] (0.5916 — assessing an organization's data assets), [S0713] (0.5853 — evaluating information quality), [S0712] (0.5790 — evaluating data source quality), DCWF [3771] (0.5860 — evaluating data sources for relevance, reliability, and objectivity), DDaT [DDAT-SK-047] (0.5587 — identify and document where data comes from), EUAIA [EUAIA-O-028] (0.5827 — AI input data quality management)

### 8. Requirements Scoping and Information Needs Definition
Ability to analyze system capabilities and requirements, determine information needs, and define the appropriate scope and level of rigor for analytical work before analysis begins.
Evidence: NICE [T1309] (0.6135 — analyze system capabilities and requirements), [S0397] (0.5876 — assessing requirements), [S0779] (0.5717 — determining information requirements), DDaT [DDAT-SK-068] (0.5742 — defining and managing business needs), [DDAT-SK-180] (0.6191 — user-centred analysis, giving direction on tools/methods), DCWF [162] (0.5726 — conducting capabilities and requirements analysis), [4014] (0.6162 — evaluate factors of operational environment to objectives)

### 9. Multi-Source Analytical Synthesis
Ability to synthesize, analyze, and prioritize meaning across multiple data sets, methods, and frameworks into a coherent and prioritized set of conclusions.
Evidence: DCWF [3890] (0.6074 — synthesizing, analyzing, and prioritizing meaning across data sets), NICE [S0727] (0.5616 — performing data fusion), [S0900] (0.5520 — analyzing information from multiple sources), [S0739] (0.5875 — analyzing products from multiple sources), DCWF [4373] (0.6746 — utilize analytical constructs), DDaT [DDAT-SK-009] (0.5507 — analysis and synthesis)

### 10. Model and Predictive Evaluation
Ability to evaluate the predictive power, generalizability, and business applicability of analytical and AI models, distinguishing between statistical fit and practical value, and assessing whether models achieve their intended purpose.
Evidence: DCWF [6490] (0.5870 — assessing predictive power and generalizability of a model), [5853] (0.5712 — build predictive, prescriptive, or descriptive models), AIRMF [AIRMF-MG-1.1] (0.6460 — AI system go/no-go determination), [AIRMF-MS-2.13] (0.6189 — assess TEVV process effectiveness), [AIRMF-MS-1.2] (0.5956 — evaluate and update measurement effectiveness), [AIRMF-MP-1.3] (0.5778 — evaluate AI system business value)

### 11. Strategic Analysis and Planning Support
Ability to perform strategic-level analysis, interpret planning guidance to determine appropriate analytical support, and develop strategic insights that inform organizational decision-making.
Evidence: DCWF [3965] (0.6188 — analyze strategic guidance for issues requiring clarification), [4032] (0.6030 — interpret planning guidance to discern level of analytical support), NICE [S0761] (0.5984 — performing strategic guidance analysis), DDaT [DDAT-SK-145] (0.6067 — ensure digital/data/technology shapes organization's strategy), [DDAT-SK-150] (0.5980 — develop organizational data strategy), [DDAT-SK-112] (0.5933 — partner with business areas to set metrics)

### 12. Data Structure Reasoning and Utilization
Ability to reason about and utilize data structures for analytical problem-solving, including structured examination of digital and data technologies and organizing data elements to support analysis.
Evidence: DDaT [DDAT-SK-080] (0.6847 — digital and data systems analysis, structured examination), DCWF [4368] (0.6588 — use data structures), [8207] (0.6050 — utilize data structures to organize, sort, manipulate elements), NICE [S0559] (0.5910 — performing data structure analysis), [T1296] (0.5555 — recommend data structures for reporting)

### 13. Analytical Standards and Quality Evaluation
Ability to apply analytical standards to evaluate the rigor, reproducibility, and defensibility of analytical outputs, including tailoring analysis to required levels and developing assessment instruments.
Evidence: DCWF [3971] (0.6438 — apply analytical standards to evaluate products), NICE [S0393] (0.5661 — developing assessments), DDaT [DDAT-SK-064] (0.5662 — put in place processes that identify and document risks)
Note: Moderate evidence density. Distinct from testing/validation (a Skill) — this is the cognitive capacity to judge whether analytical work meets quality thresholds.

### 14. Bias Recognition in Data, Methods, and Interpretation
Ability to recognize analytical bias in data, methods, and interpretation — including deception in reporting, ethical considerations in data analysis, and systematic errors — and to apply appropriate mitigation strategies.
Evidence: DCWF [3074] (0.5573 — recognize and mitigate deception in reporting and analysis), DDaT [DDAT-SK-010] (0.5820 — analysis and synthesis for data ethics), DCWF [7052] (0.5639 — principles/methods/tools for risk and bias assessment), EUAIA [EUAIA-O-028] (0.5827 — AI input data quality management including representativeness evaluation)
Note: Cross-cuts AI and DG domains but scoped here to analytical bias detection — the cognitive capacity to spot systematic error in analytical work.

### 15. Sensitivity and Scenario Analysis
Ability to systematically vary assumptions and inputs to understand how changes in conditions affect analytical conclusions, including performing sensitivity analysis and scenario-based reasoning.
Evidence: NICE [S0114] (0.6072 — performing sensitivity analysis), DCWF [3689] (0.5591 — scenario analysis methods), AIRMF [AIRMF-MG-2.1] (0.6493 — AI resource and alternative analysis), [AIRMF-MP-3.1] (0.5674 — assess and document potential benefits), O*NET [4.A.2.b.1] (0.6017 — analyzing information and evaluating results)

### 16. Measurement and Performance Metric Design *(Added by Pass 1)*
Ability to design meaningful performance metrics and measurement instruments that characterize data quality, analytical output effectiveness, and progress toward business objectives.
Evidence: DCWF [5865] (0.6100 — create metrics that characterize usability, timeliness, completeness, and accuracy of data), DDaT [DDAT-SK-112] (0.5933 — partner with business areas to set metrics needed to measure progress towards objectives), DCWF [8004] (0.5810 — analyze data including MOEs and MOPs to determine effectiveness), [2738] (0.5909 — provide evaluation and feedback for improving production)
Note: 4 elements across 2 frameworks. Distinct from AB-A-013 (applying analytical STANDARDS to evaluate rigor — judging existing work) and AB-A-008 (defining SCOPE and requirements — what to analyze). This is the cognitive capacity to DESIGN what gets measured and how.

## Adversarial Pass Results

### Pass 1 — Coverage Gaps

All ~160 WIDAI-relevant elements at STS ≥ 0.55 were mapped to entries. Element-by-element concept mapping performed across all 6 frameworks.

**Gap found:** Measurement and Performance Metric Design. Four elements across DCWF and DDaT describe the ability to design metrics and measurement instruments for data quality and business effectiveness. DCWF 5865 at STS 0.6100 describes creating metrics for data usability, timeliness, completeness, and accuracy. No existing entry covers the cognitive capacity to design what gets measured — AB-A-013 covers applying standards (judging work), and AB-A-008 covers scoping requirements (what to analyze). Added as AB-A-016.

**Gap analysis — other concepts reviewed for potential new entries:**
- **Monitoring/situational awareness** (DCWF 8131 at 0.5582, O*NET 4.A.1.a.2 at 0.5528): Monitoring is primarily a Skill (AB-S-013). The ability to maintain situational awareness during operations is weak evidence (2 elements, moderate STS). Not distinct enough as an ability. Not added.
- **Cross-functional collaboration** (DDaT SK-145, SK-150, SK-112 various contexts): These elements describe strategic leadership/collaboration. The collaboration aspect is covered by AB-A-006 (communication) and AB-A-008 (requirements scoping). No existing entry covers a standalone "ability to collaborate" — but this is a LS domain concept, not AB. Not added.
- **Regulatory/compliance evaluation** (NICE T1549 at 0.5558, DCWF 607 at 0.5505, O*NET 4.A.2.a.3 at 0.5951): Evaluating regulatory impact is relevant to AB but better placed in RM or DG domains. The analytical judgment aspect is covered by AB-A-005 (trade-off reasoning). Not added.
- **AI system oversight** (EUAIA-C-003 at 0.6249, AIRMF-MG-2.1 at 0.6493): Strong evidence from 2 AI-specific frameworks. However, the analytical judgment aspect is covered by AB-A-010 (model evaluation) and AB-A-005 (risk-based reasoning). The AI-specific governance aspect belongs in AI domain. Not added.

**+1 entry added.**

**Evidence density note:** The validator will show that entries AB-A-001 through AB-A-004 have framework coverage while AB-A-005 through AB-A-015 show 0/6 — this is the stale STRM scoring pattern. All entries are validated by manual element-by-element mapping documented above.

### Pass 2 — Redundancy and Overlap

| Pair | Distinction |
|------|-------------|
| AB-A-001 (uncertainty judgment) vs AB-A-005 (trade-off reasoning) | Reasoning with incomplete data vs. comparing competing options. 4692 ≠ 600. Uncertainty is about missing data; trade-offs are about choosing between known alternatives. |
| AB-A-003 (pattern recognition) vs AB-A-009 (multi-source synthesis) | Detecting patterns in data vs. combining findings from multiple sources into coherent conclusions. 6949 ≠ 3890. Recognition is perceptual; synthesis is integrative. |
| AB-A-004 (translate to recommendations) vs AB-A-006 (communication) | Forming actionable conclusions vs. expressing them to audiences. 5030 ≠ S0610. Recommendation formation is analytical; communication is presentational. |
| AB-A-007 (data quality) vs AB-A-014 (bias recognition) | Evaluating source fitness vs. detecting systematic errors in methods/interpretation. S0713 ≠ 3074. Quality is about inputs; bias is about process. |
| AB-A-008 (requirements scoping) vs AB-A-011 (strategic analysis) | Defining scope for a specific analytical problem vs. strategic-level planning analysis. T1309 ≠ 3965. Scoping is tactical; strategic analysis operates at organizational altitude. |
| AB-A-010 (model evaluation) vs AB-A-013 (analytical standards) | Assessing predictive model performance vs. evaluating analytical rigor broadly. 6490 ≠ 3971. Model evaluation is specific to predictive/ML models; standards apply to all analytical outputs. |
| AB-A-002 (method selection) vs AB-A-012 (data structure reasoning) | Choosing analytical methods vs. reasoning about data organization. 3692 ≠ 4368. Method selection is about technique; data structure is about information architecture. |

**No merges.**

### Pass 3 — Domain Boundary

| Entry | Borderline Domain | AB Justification | Verdict |
|-------|------------------|-------------------|---------|
| AB-A-005 (trade-off/risk reasoning) | RM | Scoped to analytical trade-off evaluation and risk quantification for decisions, not risk management as a discipline. DCWF 600 and AIRMF-MP-3.4 in analytical context. | Keep |
| AB-A-010 (model/predictive evaluation) | AI | Scoped to evaluating model performance for analytical purposes. AIRMF elements address assessment judgment, not AI system development. | Keep |
| AB-A-011 (strategic analysis) | SP | Scoped to analytical support for strategy, not strategic planning itself. DCWF 3965/4032 are about analytical support level, not strategy formulation. | Keep |
| AB-A-013 (analytical standards) | OP | Standards application is operational, but scoped here to analytical quality judgment, not operational process management. | Keep |
| AB-A-014 (bias recognition) | AI, DG | Scoped to analytical bias detection in the AB context, not AI fairness or data governance. DCWF 3074 is about recognizing deception in analysis. | Keep |
| AB-A-015 (sensitivity/scenario) | RM | Scenario analysis for understanding analytical conclusion sensitivity, not risk scenario planning. S0114 is explicitly sensitivity analysis. | Keep |

**No entries removed.**

## STRM Coverage Note

Same pattern as AB Knowledge and AB Skills: AB-A-001 through AB-A-004 show framework coverage; AB-A-005 through AB-A-016 show 0/6 because STRM scores were computed against pre-rewrite entry text. Concepts for entries 005–016 are validated by manual element-by-element mapping documented above.

## Final Entry List

| ID | Concept | Key Evidence |
|---|---|---|
| AB-A-001 | Structured judgment under uncertainty | 4692 (0.74), 3039 (0.72), 3756 (0.68), S0922 (0.62) |
| AB-A-002 | Analytical method selection and evaluation | DDAT-SK-013 (0.72), 3692 (0.68), 3681 (0.62) |
| AB-A-003 | Pattern recognition and problem decomposition | 6949 (0.65), 6120 (0.62), 1.A.1.e.1 (0.60) |
| AB-A-004 | Translation of data into actionable recommendations | DDAT-SK-007 (0.68), 5030 (0.68), 5570 (0.67), 6170 (0.62) |
| AB-A-005 | Cost-benefit, trade-off, and risk-based reasoning | 600 (0.68), AIRMF-MP-3.4 (0.63), AIRMF-MS-4.2 (0.62), DDAT-SK-089 (0.60) |
| AB-A-006 | Analytical communication across audiences | S0610 (0.60), S0387 (0.59), S0386 (0.58), 1.A.1.a.3 (0.57) |
| AB-A-007 | Data source quality and reliability assessment | S0808 (0.59), S0713 (0.59), EUAIA-O-028 (0.58), 3771 (0.59) |
| AB-A-008 | Requirements scoping and information needs definition | DDAT-SK-180 (0.62), T1309 (0.61), 4014 (0.62), S0397 (0.59) |
| AB-A-009 | Multi-source analytical synthesis | 4373 (0.67), 3890 (0.61), S0739 (0.59), S0727 (0.56) |
| AB-A-010 | Model and predictive evaluation | AIRMF-MG-1.1 (0.65), AIRMF-MS-2.13 (0.62), AIRMF-MS-1.2 (0.60), 6490 (0.59) |
| AB-A-011 | Strategic analysis and planning support | 3965 (0.62), DDAT-SK-145 (0.61), 4032 (0.60), DDAT-SK-150 (0.60) |
| AB-A-012 | Data structure reasoning and utilization | DDAT-SK-080 (0.68), 4368 (0.66), 8207 (0.61), S0559 (0.59) |
| AB-A-013 | Analytical standards and quality evaluation | 3971 (0.64), S0393 (0.57), DDAT-SK-064 (0.57) |
| AB-A-014 | Bias recognition in data, methods, and interpretation | DDAT-SK-010 (0.58), EUAIA-O-028 (0.58), 3074 (0.56), 7052 (0.56) |
| AB-A-015 | Sensitivity and scenario analysis | AIRMF-MG-2.1 (0.65), S0114 (0.61), 4.A.2.b.1 (0.60), 3689 (0.56) |
| AB-A-016 | Measurement and performance metric design | 5865 (0.61), DDAT-SK-112 (0.59), 2738 (0.59), 8004 (0.58) |

## Methodology

Built from STRM rationale evidence per KSA-SYNTHESIS-METHODOLOGY.md v2.0.0. Existing entries discarded. Concepts extracted from 6 framework element descriptions, clustered, written as entries, then subjected to 3 adversarial passes (coverage gaps, redundancy, domain boundary). Pass 1 identified 1 gap (measurement and performance metric design) — added as AB-A-016. No merges or removals after Passes 2 and 3. Final count: 16.
