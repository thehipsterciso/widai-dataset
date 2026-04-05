# AB Tasks — Evidence-Driven Synthesis

## Overview

Domain: Analytics & BI (AB)
Dimension: Tasks
Previous count: 30 (pre-evidence-first)
Final count: 21
Schema: 3.0.0
Methodology: Evidence-first synthesis per KSA-SYNTHESIS-METHODOLOGY.md v2.0.0

This synthesis was built entirely from cross-framework STRM evidence. Prior entries were not used as a starting point. The reduction from 30 to 21 reflects the evidence: several prior entries described highly specific analytical methods (segmentation, time series, geospatial) that lack standalone framework evidence and are properly subsumed into broader task clusters. Other prior entries (self-service BI, semantic models, BI asset maintenance) described implementation-level specifics not distinguished by the framework evidence.

## Evidence Sources

| Framework | Elements at STS ≥ 0.50 | WIDAI-relevant | At STS ≥ 0.55 |
|-----------|----------------------|----------------|---------------|
| O*NET 30.2 | 9 | 8 | 2 |
| NIST NICE v2.1.0 | 189 | 156 | 62 |
| DoD DCWF v5.1 | 423 | 344 | 148 |
| UK DDaT | 59 | 56 | 26 |
| EU AI Act | 15 | 14 | 6 |
| NIST AI RMF 1.0 | 24 | 24 | 12 |
| **Total** | **719** | **602** | **~256** |

Total STRM mappings: 7,694

## Concept Clusters

21 distinct task concept clusters extracted from framework evidence:

### 1. Execute Analytical Studies and Deliver Findings
Plan, scope, conduct, and deliver analytical work in response to business requirements, including methodology selection, analysis execution, and findings delivery with documented assumptions and limitations.
Evidence: DCWF [8081] (0.7042 — document and disseminate analytic findings), [2730] (0.6857 — provide analyses for effectiveness assessment), [5907] (0.6347 — plan, coordinate, execute complex studies using advanced data modeling), [5894] (0.6133 — lead development of solutions for data analytical objectives), [4373] (0.6236 — utilize analytical constructs), NICE [T1798] (0.6500 — provide analysis and support), DDaT [DDAT-SK-086] (0.6589 — evaluation delivery), [DDAT-SK-019] (0.6363 — business analysis), AIRMF [AIRMF-MP-3.1] (0.6089 — assess and document potential benefits)

### 2. Collect and Integrate Data from Multiple Sources
Gather data from databases, APIs, external sources, and organizational systems; identify data consolidation opportunities; and integrate information across disparate sources to support analytical workflows.
Evidence: DCWF [3603] (0.6225 — methods for gathering information and producing intelligence), [5890] (0.6199 — identify data consolidation opportunities across database systems), [3382] (0.6073 — methods to integrate and summarize information from sources), [166] (0.6057 — conducting queries and developing algorithms), NICE [T1568] (0.6301 — implement cross-domain solutions), [S0909] (0.5739 — integrating information from multiple sources)

### 3. Transform, Clean, and Prepare Data for Analysis
Preprocess, transform, normalize, and clean data, including joining disparate sources, handling missing values, format conversion, and validating data integrity before analytical use.
Evidence: NICE [S0644] (0.6229 — performing transformation analytics), [K1322] (0.5972 — data aggregation tools and techniques), DCWF [6690] (0.5991 — transformation analytics), [5844] (0.5779 — data acquisition, cleaning, transformation for ML conduits), [8207] (0.5749 — utilize data structures to organize and manipulate)

### 4. Apply Analytical and Statistical Techniques to Data
Apply established and emerging analytical methods to data, including exploratory analysis, confirmatory analysis, quantitative techniques, and technique validation.
Evidence: DCWF [8010] (0.6928 — apply analytic techniques to validate information in reporting), [4373] (0.6236 — utilize analytical constructs), [2251] (0.6148 — apply analytic techniques), DDaT [DDAT-SK-013] (0.6073 — applying statistical and analytical techniques), [DDAT-SK-007] (0.5912 — examining, interpreting and analysing data), NICE [S0433] (0.6106 — creating analytics), [S0877] (0.5505 — performing quantitative analysis), DCWF [6790A] (0.5594 — utilize quantitative techniques)

### 5. Build Data Visualizations and Dashboards
Create visualizations, dashboards, performance reports, and analytical display products that accurately represent findings and support self-service exploration.
Evidence: DCWF [4237] (0.7030 — develop dashboards to better visualize data), [4221] (0.5990 — construct log aggregation solutions and analysis platforms), [76A] (0.6012 — monitor measures of system performance), NICE [T1581] (0.6333 — create system performance reports), [T1240] (0.5800 — create knowledge management reports)

### 6. Design Analytical Systems, Data Models, and Architectures
Design data management systems, analytical architectures, data models, prototypes, and wireframes to support analytical capabilities and business requirements.
Evidence: DCWF [5908] (0.6594 — prepare database design and architecture reports), [5966] (0.6145 — create prototypes, wireframes, storyboards), [124A] (0.6089 — apply system design tools), [502B] (0.5815 — develop enterprise architecture), [530A] (0.5521 — develop design documentation), NICE [T1491] (0.6316 — design data management systems), [T1565] (0.6101 — configure database management systems), DDaT [DDAT-SK-157] (0.5763 — systems design to meet business needs), [DDAT-SK-056] (0.5714 — data integration design)

### 7. Manage and Maintain Databases and Analytical Infrastructure
Monitor, maintain, and optimize databases and analytical infrastructure for performance, including DBMS administration, software maintenance, and operational support.
Evidence: DCWF [712] (0.6799 — monitor and maintain databases for optimal performance), [684] (0.6447 — maintain DBMS software), [709A] (0.6495 — modify and maintain existing software), [811] (0.5698 — provide ongoing optimization and problem solving support), [209] (0.5565 — maintaining directory services), NICE [T0137] (0.6475 — maintain DBMS software), [T1402] (0.6310 — manage databases and data management systems), [S0843] (0.5760 — maintaining data)
Note: Strongest cluster for database-specific tasks — 8 elements across 2 frameworks at STS ≥ 0.56.

### 8. Deploy and Manage Continuous Monitoring and Alerting Systems
Implement, operate, and maintain continuous monitoring infrastructure, including configuring telemetry, performing data assessments, triaging triggered events, and coordinating incident response.
Evidence: DCWF [4307] (0.7294 — monitor data and perform triage on triggered events, highest STS in AB-T dimension), [3063] (0.6886 — monitor system operations and react to events), [5951] (0.6163 — select and implement telemetry within CI/CD pipeline), [554A] (0.6087 — diagnose and resolve incidents), NICE [T1956] (0.6333 — conduct continuous monitoring data assessments), [T1945] (0.6079 — prepare continuous monitoring reports), [S0451] (0.6035 — deploying continuous monitoring technologies), [T1967] (0.5967 — coordinate responses to flagged issues), [T1953] (0.5904 — establish continuous monitoring reporting requirements), EUAIA [EUAIA-O-011] (0.5773 — designing AI monitoring and logging systems)
Note: Strongest cluster by evidence density in AB-T dimension — 10 elements across 3 frameworks.

### 9. Test and Validate Analytical Outputs and Data Pipelines
Create and execute testing procedures, validate analytical results, develop automated test frameworks, and perform quality assurance on analytical outputs and data infrastructure.
Evidence: DCWF [7002] (0.6204 — assist teams manage test data), [5934] (0.5863 — develop framework for automated test and evaluation), [516] (0.5796 — develop system testing and validation procedures), [516A] (0.5791 — develop testing and validation procedures), DDaT [DDAT-SK-072] (0.5837 — designing and executing tests), NICE [T1138] (0.5833 — create testing and validation procedures), [T1312] (0.5745 — conduct test and evaluation activities), AIRMF [AIRMF-MS-2.13] (0.5620 — assess TEVV process effectiveness)

### 10. Document Analytical Methodologies, Findings, and Compliance Requirements
Produce analytical documentation including methodology descriptions, data source records, findings reports, and regulatory/compliance documentation that meets evidence standards for audit and executive decision support.
Evidence: DCWF [8081] (0.7042 — document and disseminate analytic findings), [4170] (0.5797 — accurately document results), [4000] (0.6362 — create and maintain planning documents), [5640] (0.6025 — utilize technical documentation), NICE [S0391] (0.5756 — creating technical documentation), [T1562] (0.5754 — document system requirements), EUAIA [EUAIA-O-009] (0.6004 — technical documentation for regulatory compliance), [EUAIA-O-042] (0.5713 — downstream integration documentation), AIRMF [AIRMF-MP-1.1] (0.6008 — AI system context documentation), [AIRMF-MP-2.2] (0.5613 — documenting system knowledge limits)

### 11. Present Analytical Findings and Create Decision Support Materials
Communicate analytical results to executive and business stakeholders, demonstrating how data and analytics initiatives address organizational challenges, and produce decision support materials.
Evidence: DCWF [5869] (0.6237 — demonstrate to executive stakeholders how analytics address challenges), [5570] (0.5883 — provide actionable recommendations based on analysis), NICE [S0783] (0.6372 — creating decision support materials), DDaT [DDAT-SK-031] (0.5561 — communicating data, turning complex data into clear solutions)

### 12. Coordinate Cross-Functional Analytical Projects and Knowledge Sharing
Lead and coordinate analytical work across organizational boundaries, facilitate data sharing, promote best practices, and ensure collected data is available to consumers.
Evidence: DCWF [5886] (0.6398 — facilitate cross-sharing of best practices for data usage), [5850] (0.6427 — assist teams identify, curate, manage data), [8028] (0.6029 — collaborate with analysts to ensure data available), [794A] (0.5813 — promote knowledge sharing), [3994] (0.5899 — coordinate and disseminate information), DDaT [DDAT-SK-161] (0.5551 — team dynamics and collaboration), [DDAT-SK-009] (0.6168 — help organization adopt analysis techniques)

### 13. Gather Stakeholder Requirements and Translate to Analytical Specifications
Elicit, analyze, and validate stakeholder analytical needs, define data requirements and information specifications, and prototype analytical solutions iteratively.
Evidence: DCWF [400] (0.5789 — analyze and define data requirements and specifications), [2093] (0.5528 — collaborate with customer to define information requirements), [5888] (0.5550 — identify and document customer requirements when on-boarding data), NICE [T1392] (0.5966 — develop user experience requirements), DDaT [DDAT-SK-019] (0.6363 — business analysis, translating requirements into solutions), DDaT [DDAT-SK-068] (implied — defining and managing business needs)

### 14. Perform Cost-Benefit, Trade-Off, and Risk Analysis
Conduct risk analysis, feasibility studies, trade-off analysis, and cost-benefit evaluation to support decision-making, including financial implications assessment.
Evidence: DCWF [458] (0.5919 — conduct risk analysis, feasibility study, trade-off analysis), [537A] (0.5887 — develop methods to monitor and measure risk), [537] (0.5711 — develop methods to monitor risk and compliance), DDaT [DDAT-SK-089] (0.6308 — assess full financial implications), NICE [S0783] (0.6372 — creating decision support materials)

### 15. Design and Execute Scenario, Sensitivity, and Simulation Analyses
Plan and conduct scenario analyses, sensitivity analyses, and simulation exercises, including varying assumptions systematically and determining methods for quantitative measurement.
Evidence: DCWF [5873] (0.6458 — determine methods and metrics for quantitative/qualitative measurement of AI risks), [855] (0.6001 — support design and execution of exercise scenarios), NICE [T1311] (0.5965 — design and execute exercise scenarios), [S0114] (0.5796 — performing sensitivity analysis), DCWF [8067] (0.5534 — develop risk assessments), AIRMF [AIRMF-GV-1.3] (0.5768 — design risk management processes)

### 16. Manage Data Classification, Metadata, and Data Catalogs
Extract, analyze, and maintain metadata; apply data classification standards; create and maintain data catalogs and dictionaries.
Evidence: DCWF [3298] (0.6126 — extract, analyze, and use metadata), [1126] (0.6066 — data classification standards and methodologies), [2639] (0.5505 — perform content and metadata analysis), [5864] (0.5793 — create data catalogs and dictionaries), [120] (0.5666 — knowledge of sources, characteristics, uses of data assets)

### 17. Define, Maintain, and Govern Metrics and KPI Definitions
Establish performance measurement requirements, define metrics and KPIs, and partner with business areas to ensure measurement consistency across the organization.
Evidence: DDaT [DDAT-SK-112] (0.5839 — partner with business areas to set metrics for organizational objectives), DCWF [5865] (0.5608 — create metrics that characterize data usability and accuracy), NICE [T1965] (0.5596 — establish performance measurement requirements for monitoring), DCWF [8098] (0.5527 — evaluate reporting to support decisions)

### 18. Build and Maintain Automated Analytical Data Pipelines
Develop, deploy, and maintain automated data processing and analytical pipelines, including data management conduits, telemetry implementation, and analytical code automation.
Evidence: DCWF [5852] (0.6397 — build automated data management conduits), [5951] (0.6163 — select and implement telemetry within CI/CD), [7060] (0.5538 — designing approach for automated data labeling and lifecycle), DDaT [DDAT-SK-077] (0.5721 — developing code for analysis), [DDAT-SK-132] (implied — pipeline automation)

### 19. Evaluate Regulatory and Policy Impacts on Analytical Operations
Assess the impact of legal, regulatory, policy, and procedural changes on analytical operations and reporting requirements, updating processes and documentation accordingly.
Evidence: NICE [T1549] (0.5616 — evaluate impact of legal, regulatory changes), AIRMF [AIRMF-GV-1.1] (0.5877 — AI-related legal and regulatory requirements), EUAIA [EUAIA-O-047] (0.5670 — AI serious incident management and regulatory reporting), DCWF [607] (0.5726 — evaluate effectiveness of laws and regulations), [1027A] (0.5549 — interpret and apply applicable laws)

### 20. Assess Data Quality, Completeness, and Fitness for Analytical Use
Profile data to evaluate quality, completeness, consistency, and fitness for purpose, documenting quality impacts on analytical conclusions.
Evidence: DCWF [5936] (0.5597 — evaluate reliability, availability, maintainability data), [3771] (implicit in quality assessment), DDaT [DDAT-SK-063] (implied — data preparation and quality assurance), NICE [S0423] (0.6029 — analyzing processes to ensure conformance with requirements)

### 21. Develop and Maintain Data and Analytics Strategy
Create and maintain organizational data and analytics strategy aligned to business objectives, ensure technology and data architecture support strategic outcomes.
Evidence: DDaT [DDAT-SK-150] (0.6204 — develop organizational data strategy), [DDAT-SK-145] (0.6129 — ensure digital/data/technology shapes strategy), [DDAT-SK-122] (0.5767 — ensure technical architecture optimises outcomes), [DDAT-SK-168] (0.5718 — ensure technical architecture reflects requirements)
Note: Predominantly DDaT-sourced evidence. Borderline SP (Strategic Planning) domain but scoped to analytical capability strategy.

## Adversarial Pass Results

### Pass 1 — Coverage Gaps

All ~256 WIDAI-relevant elements at STS ≥ 0.55 were mapped to entries. Element-by-element concept mapping performed across all 6 frameworks.

**Gap analysis — concepts reviewed for potential new entries:**
- **Analytical governance and platform management** (DCWF 5862 at 0.5764, 5897 at 0.5690): Creating governance structures for AI/analytical solutions and managing compliance with data handling requirements. Currently partially covered by AB-T-016 (classification/metadata) and AB-T-010 (documentation). The governance TASK — maintaining content lifecycle, access controls, certification workflows — has moderate evidence but is operationally distinct from classification. However, the evidence density is thin (2 elements) and the concept is better placed in DG (Data Governance). Not added.
- **Business process improvement through analytics** (DDaT DDAT-SK-022 at 0.5905): Creating artefacts and analyzing business processes. Covered by the combination of AB-T-001 (execute studies) and AB-T-013 (requirements gathering). Not distinct enough as a standalone task. Not added.
- **Mentoring and team development** (weak evidence): No task-specific framework elements describe mentoring in the AB context at competitive STS. The concept is valid but belongs in LS (Leadership & Staff Development). Not added.
- **Incident management coordination** (DCWF 1155 at 0.5643, 823 at 0.5561): Managing service level and incident processes. Covered by AB-T-008 (continuous monitoring, which includes event triage and incident response). Not added.

**No new entries added.**

### Pass 2 — Redundancy and Overlap

| Pair | Distinction |
|------|-------------|
| AB-T-001 (execute studies) vs AB-T-004 (apply techniques) | Full analytical lifecycle (scope→execute→deliver) vs. specific technical method application. 5907 ≠ 8010. |
| AB-T-002 (data collection) vs AB-T-003 (transformation) | Acquiring data from sources vs. cleaning/transforming acquired data. 3603 ≠ S0644. |
| AB-T-005 (visualization/dashboards) vs AB-T-011 (presentation) | Building visual products vs. communicating findings to stakeholders. 4237 ≠ 5869. |
| AB-T-006 (system design) vs AB-T-007 (database management) | Creating new architectures vs. maintaining existing infrastructure. 5908 ≠ 712. |
| AB-T-008 (monitoring) vs AB-T-009 (testing/validation) | Ongoing operational monitoring vs. discrete validation of analytical outputs. 4307 ≠ 7002. |
| AB-T-010 (documentation) vs AB-T-011 (presentation) | Written documentation vs. stakeholder communication and decision support materials. 4000 ≠ 5869. |
| AB-T-012 (coordination) vs AB-T-013 (requirements) | Cross-functional facilitation vs. eliciting specific analytical specifications. 5886 ≠ 400. |
| AB-T-014 (cost-benefit/risk) vs AB-T-015 (scenario analysis) | Comparing known alternatives vs. systematically varying assumptions. 458 ≠ T1311. |
| AB-T-016 (classification/metadata) vs AB-T-020 (data quality) | Categorizing and cataloging data vs. assessing data fitness for use. 3298 ≠ 5936. |
| AB-T-017 (metrics/KPI) vs AB-T-020 (data quality) | Defining organizational measures vs. assessing data fitness. DDAT-SK-112 ≠ 5936. |

**No merges.**

### Pass 3 — Domain Boundary

| Entry | Borderline Domain | AB Justification | Verdict |
|-------|------------------|-------------------|---------|
| AB-T-006 (system design) | DA | Scoped to analytical architecture design, not enterprise data architecture. 5908/T1491 describe analytical system design. | Keep |
| AB-T-007 (database management) | DA | Scoped to analytical infrastructure maintenance. 712 (monitor databases for optimal performance) is operational AB work. | Keep |
| AB-T-012 (coordination/knowledge sharing) | LS | Scoped to analytical knowledge sharing and data project coordination. 5886 is about data usage practices. | Keep |
| AB-T-016 (classification/metadata) | DG | Scoped to analytical organization and retrieval, not data governance policy. 3298/1126 in analytical context. | Keep |
| AB-T-019 (regulatory evaluation) | RM | Scoped to impact on analytical operations specifically. AIRMF-GV-1.1 addresses analytical requirements. | Keep |
| AB-T-21 (strategy) | SP | Scoped to data/analytics strategy. Predominantly DDaT-sourced. Weakest by cross-framework corroboration. | Keep (flagged) |

**No entries removed.**

## STRM Coverage Note

AB-T-001 through AB-T-011 show 6/6 framework coverage; AB-T-012 through AB-T-021 show 0/6 because STRM scores were computed against pre-rewrite entry text. Concepts for entries 012–021 are validated by manual element-by-element mapping documented above.

## Final Entry List

| ID | Concept | Key Evidence |
|---|---|---|
| AB-T-001 | Execute analytical studies and deliver findings | 8081 (0.70), 2730 (0.69), T1798 (0.65), DDAT-SK-086 (0.66) |
| AB-T-002 | Collect and integrate data from sources | 3603 (0.62), 5890 (0.62), T1568 (0.63), 3382 (0.61) |
| AB-T-003 | Transform, clean, and prepare data | S0644 (0.62), 6690 (0.60), 5844 (0.58) |
| AB-T-004 | Apply analytical and statistical techniques | 8010 (0.69), DDAT-SK-013 (0.61), 4373 (0.62), 2251 (0.61) |
| AB-T-005 | Build visualizations and dashboards | 4237 (0.70), T1581 (0.63), T1240 (0.58) |
| AB-T-006 | Design analytical systems and architectures | 5908 (0.66), T1491 (0.63), 5966 (0.61), 124A (0.61) |
| AB-T-007 | Manage and maintain databases and infrastructure | 712 (0.68), T0137 (0.65), T1402 (0.63), 684 (0.64) |
| AB-T-008 | Continuous monitoring and alerting | 4307 (0.73), 3063 (0.69), T1956 (0.63), T1945 (0.61) |
| AB-T-009 | Test and validate analytical outputs | 7002 (0.62), DDAT-SK-072 (0.58), T1138 (0.58), 5934 (0.59) |
| AB-T-010 | Document methodologies, findings, and compliance | 8081 (0.70), 4000 (0.64), EUAIA-O-009 (0.60), AIRMF-MP-1.1 (0.60) |
| AB-T-011 | Present findings and create decision support | 5869 (0.62), S0783 (0.64), DDAT-SK-031 (0.56) |
| AB-T-012 | Coordinate cross-functional projects and knowledge sharing | 5850 (0.64), 5886 (0.64), 8028 (0.60), DDAT-SK-009 (0.62) |
| AB-T-013 | Gather requirements and translate to specifications | 400 (0.58), T1392 (0.60), DDAT-SK-019 (0.64) |
| AB-T-014 | Cost-benefit, trade-off, and risk analysis | 458 (0.59), DDAT-SK-089 (0.63), S0783 (0.64) |
| AB-T-015 | Scenario, sensitivity, and simulation analysis | 5873 (0.65), T1311 (0.60), 855 (0.60), S0114 (0.58) |
| AB-T-016 | Data classification, metadata, and catalogs | 3298 (0.61), 1126 (0.61), 5864 (0.58), 2639 (0.55) |
| AB-T-017 | Define and govern metrics and KPIs | DDAT-SK-112 (0.58), 5865 (0.56), T1965 (0.56) |
| AB-T-018 | Build automated analytical pipelines | 5852 (0.64), 5951 (0.62), DDAT-SK-077 (0.57) |
| AB-T-019 | Evaluate regulatory/policy impacts on analytics | T1549 (0.56), AIRMF-GV-1.1 (0.59), EUAIA-O-047 (0.57) |
| AB-T-020 | Assess data quality and fitness for use | S0423 (0.60), 5936 (0.56) |
| AB-T-021 | Develop data and analytics strategy | DDAT-SK-150 (0.62), DDAT-SK-145 (0.61), DDAT-SK-122 (0.58) |

## Methodology

Built from STRM rationale evidence per KSA-SYNTHESIS-METHODOLOGY.md v2.0.0. Existing entries discarded. Concepts extracted from 6 framework element descriptions, clustered, written as entries, then subjected to 3 adversarial passes (coverage gaps, redundancy, domain boundary). No gaps, merges, or removals after adversarial analysis. Final count: 21. Count went down from 30 because prior entries included highly specific analytical method tasks (segmentation, time series, geospatial) and BI-specific implementation tasks (semantic models, self-service BI) that lack standalone framework evidence and are subsumed into broader clusters.
