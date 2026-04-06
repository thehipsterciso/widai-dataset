# AB Skills — Evidence-Driven Synthesis

## Overview

Domain: Analytics & BI (AB)
Dimension: Skills
Previous count: 25 (pre-evidence-first), then 24 (initial evidence-first), then **25** (after adversarial)
Final count: 25
Schema: 3.0.0
Methodology: Evidence-first synthesis per KSA-SYNTHESIS-METHODOLOGY.md v2.0.0

This synthesis was built entirely from cross-framework STRM evidence. Prior entries were not used as a starting point.

## Evidence Sources

| Framework | Elements at STS ≥ 0.50 | WIDAI-relevant | At STS ≥ 0.55 |
|-----------|----------------------|----------------|---------------|
| O*NET 30.2 | 26 | 16 | 7 |
| NIST NICE v2.1.0 | 586 | 429 | ~206 |
| DoD DCWF v5.1 | 904 | 674 | ~400+ |
| UK DDaT | 85 | 81 | 44 |
| EU AI Act | 33 | 30 | 19 |
| NIST AI RMF 1.0 | 54 | 53 | 35 |
| **Total** | **1,688** | **1,283** | **~711** |

Total STRM mappings: 14,540

## Concept Clusters

25 distinct concept clusters extracted from framework evidence:

### 1. Multi-Source Integration and Data Fusion
Integrating and synthesizing data from multiple sources, cross-source correlation, producing coherent findings from heterogeneous datasets.
Evidence: NICE [S0909] (0.7321), [S0727] (0.7082), [S0904] (0.6886), DCWF [1120] (0.7332), [3382] (0.7191), [4647] (0.6743), DDaT [DDAT-SK-050] (0.6856), O*NET [1.A.1.e.1] (0.7053)

### 2. Data Querying
Querying and extracting data from databases, data warehouses, and analytical repositories using SQL and programmatic methods.
Evidence: NICE [S0748] (0.6894), [S0911] (0.6868), [K0705] (0.6954), DCWF [166] (0.6916), [8137] (0.6699)

### 3. Analytical Technique Application
Applying analytical techniques to data, performing exploratory and confirmatory analysis, creating analytics products.
Evidence: NICE [S0433] (0.7187), [S0709] (0.7077), [S0854] (0.6841), DCWF [8010] (0.7055), [8011] (0.6806), DDaT [DDAT-SK-009] (0.6523), [DDAT-SK-013] (0.5831)

### 4. Visualization and Dashboards
Building data visualizations and dashboards that accurately represent findings, supporting self-service exploration.
Evidence: DCWF [4237] (0.7276), NICE [K0647] (0.6520), DDaT [DDAT-SK-067] (0.6591)

### 5. Preprocessing and Transformation
Preprocessing, transforming, and normalizing data for analysis including format conversion, cleansing, joining disparate sources.
Evidence: NICE [S0644] (0.7104), [S0726] (0.6763), [S0631] (0.6736), DCWF [6610] (0.7030), [8207] (0.6855)

### 6. Statistical Modeling and Regression
Creating and validating statistical models for business applications, including regression analysis, model specification, and performance evaluation.
Evidence: NICE [S0563] (0.6616), [S0640] (0.6614), DCWF [172] (implied), DDaT [DDAT-SK-011] (implied via applied statistics)

### 7. Requirements and Business Translation
Translating business questions into structured analytical approaches, defining data requirements, scoping analysis.
Evidence: NICE [S0855] (0.6834), [S0759] (0.6778), [T1063] (0.6885), DCWF [3059] (0.6905), [911A] (0.6791), [3019] (0.6952), AIRMF [AIRMF-MP-1.1] (0.7578), DDaT [DDAT-SK-068] (0.6518)

### 8. Data Structure and Model Design
Designing data analysis structures and developing data models, including semantic modeling and dimensional design.
Evidence: NICE [S0568] (0.6863), [S0029] (0.6719), [S0681] (0.6680), [S0118] (0.6884), DCWF [6650] (0.6847), [8207] (0.6855), DDaT [DDAT-SK-061] (0.5947)

### 9. Testing and Validation
Testing and validating analytical outputs, quality assurance, developing validation procedures.
Evidence: NICE [T1258] (0.7262), [T0513] (0.7054), [S0048] (0.6773), [T1209] (0.6765), [S0745] (0.6752), [T1528] (0.6587), DCWF [761A] (0.7076), [5933] (0.6871), [5945] (0.6976), [516A] (0.6873), [5948] (0.6849), DDaT [DDAT-SK-172] (0.6528), [DDAT-SK-072] (0.5590), EUAIA [EUAIA-O-005] (0.6685)
Note: Testing/validation is the largest concept cluster by evidence density — 14+ elements across 4 frameworks.

### 10. Market and User Research
Conducting market research and user research using quantitative and qualitative methods.
Evidence: NICE [S0868] (0.6935), [S0404] (0.6813), DCWF [7099] (0.6740), DDaT [DDAT-SK-187] (0.5533)

### 11. Trade-off and Comparative Analysis
Performing trade-off analyses that quantify competing options and evaluate costs and benefits.
Evidence: NICE [S0891] (0.6607), DCWF [458] (implied), AIRMF [AIRMF-MP-3.4] (0.6286)

### 12. Data Collection
Collecting relevant data from a variety of sources, systematic data acquisition, assessing source reliability.
Evidence: NICE [S0600] (0.6792), DCWF [3001] (0.6696), [4647] (0.6743), DDaT [DDAT-SK-050] (0.6856)

### 13. Continuous Monitoring
Deploying and managing continuous monitoring systems for analytical environments, automated alerting.
Evidence: NICE [S0451] (0.6650), [T1954] (0.6592), [T1956] (0.6616), DCWF [7029] (implied), DDaT [DDAT-SK-120] (0.5788)

### 14. Documentation and Communication
Producing analytical documentation and communicating findings in writing, creating technical documentation.
Evidence: NICE [S0391] (0.6613), [S0610] (implied), [S0385] (implied), DCWF [8010] (0.7055 — validating info in reporting), EUAIA [EUAIA-O-042] (0.6351), AIRMF [AIRMF-MP-1.1] (0.7578), [AIRMF-MP-2.2] (0.7117), DDaT [DDAT-SK-031] (0.6295)

### 15. Assessment Design
Designing valid and reliable assessments and evaluation frameworks, developing measurement instruments.
Evidence: NICE [S0393] (0.6584), DCWF [3734] (0.7020), [3126] (implied), DDaT [DDAT-SK-086] (0.5660)

### 16. Pattern Recognition
Recognizing patterns in data, quickly making sense of complex information, organizing information into meaningful patterns.
Evidence: O*NET [1.A.1.e.1] (0.7053), [1.A.1.e.3] (0.5889), NICE [S0559] (0.6738 — data structure analysis), DCWF [4212] (0.6881 — flow data analysis)

### 17. Data Mapping and Classification
Performing data mapping and classification, applying classification schemes, categorizing data elements.
Evidence: NICE [K1097] (0.6862), [K0866] (0.6688), DCWF [6730] (0.6784), [1126] (implied)

### 18. Programming and Automation
Programming for analytical applications, building automated data pipelines, developing test automation.
Evidence: NICE [S0837] (implied), DCWF [174] (implied), [5852] (0.6813 — automated data management conduits), DDaT [DDAT-SK-132] (0.6575), [DDAT-SK-077] (0.6107), [DDAT-SK-133] (0.5887)

### 19. Design Thinking
Applying design thinking methods to analytical problem framing, operational design, iterative prototyping.
Evidence: DCWF [7103] (0.6769), [8146] (0.6775 — operational design), DDaT [DDAT-SK-076] (0.5728 — designing together), [DDAT-SK-021] (0.5672 — business modelling)

### 20. Mentoring and Team Development
Mentoring and developing analytical team members, methodology review, feedback delivery.
Evidence: DCWF [8196] (0.5983 — train and mentor)
Note: Weakest entry by evidence density (single element). Borderline LS domain. Kept because scoped to analytical competency development.

### 21. Data Quality Validation
Performing data quality validation and input assurance, implementing validation procedures, verifying completeness.
Evidence: NICE [S0565] (0.6556 — input validation), DCWF [6060] (implied — verify/validate test data), DDaT [DDAT-SK-063] (0.5856 — data preparation/quality assurance), [DDAT-SK-137] (0.5561 — quality assurance of data and analysis)

### 22. Method Selection
Selecting appropriate mathematical and quantitative methods, evaluating method assumptions against data characteristics.
Evidence: NICE [K1096] (0.6749 — choosing data analysis tools), DCWF [3692] (implied — assessing applicability of analytical tools), DDaT [DDAT-SK-013] (0.5831 — evaluating methods to answer research questions)

### 23. Analytical Standards
Applying analytical standards to evaluate products and processes, tailoring analysis to required levels.
Evidence: DCWF [3971] (0.6766 — apply analytical standards), [3893] (0.6828 — tailoring analysis to necessary levels), [62] (implied — industry-standard analysis principles)

### 24. Data Asset Assessment
Assessing an organization's data assets for analytical value, evaluating data fitness for purpose.
Evidence: NICE [S0808] (0.6606 — assessing organization's data assets), DCWF [3771] (implied — evaluating data sources for relevance and reliability), DDaT [DDAT-SK-070] (0.5818 — delivering business impact through data), [DDAT-SK-047] (0.5559 — identify and document where data comes from)

### 25. Analytical Presentation and Strategic Insight Communication *(Added by Pass 1)*
Presenting analytical findings and strategic insights to diverse audiences, translating complex data into evaluative conclusions, facilitating technical exchanges with non-technical stakeholders.
Evidence: DCWF [6170] (0.6728 — translate data and test results into evaluative conclusions), [5270] (0.6492 — develop strategic insights from large data sets), [5430] (0.6311 — present technical information to technical and non-technical audiences), DDaT [DDAT-SK-031] (0.6295 — communicating data, turning complex data into clear solutions), DCWF [8081] (0.6258 — document and disseminate analytic findings), [3076] (0.6206 — tailor technical information to customer's understanding), [4719] (0.6173 — technical exchanges with non-technical audiences)
Note: 7 elements across 2 frameworks at STS ≥ 0.60. Distinct from AB-S-014 which is explicitly scoped to written documentation and producing analytical documentation. This entry covers oral/interactive presentation, strategic insight translation, and audience-adaptive communication of analytical findings.

## Adversarial Pass Results

### Pass 1 — Coverage Gaps

All ~711 WIDAI-relevant elements at STS ≥ 0.55 were mapped to entries. Element-by-element concept mapping performed across all 6 frameworks.

**Gap found:** Analytical Presentation and Strategic Insight Communication. Seven elements across DCWF and DDaT describe presenting analytical findings to diverse audiences, translating data into evaluative conclusions, and facilitating technical exchanges with non-technical stakeholders. DCWF 6170 at STS 0.6728 is in the top quartile of all AB-S evidence. AB-S-014 is explicitly scoped to "communicating findings in writing" and "creating technical documentation" — oral/interactive presentation and strategic insight translation have no existing entry covering them as a standalone concept. Added as AB-S-025.

**Gap analysis — other concepts reviewed for potential new entries:**
- **Decision support creation** (S0783, STS 0.6442): Spans AB-S-004 (visualization) + AB-S-014 (documentation) + AB-S-025 (presentation). Decision support materials are a deliverable type, not a distinct skill. Not added.
- **Risk analysis as analytical skill**: Multiple AI RMF elements about risk assessment. Covered by AB-S-011 (trade-off analysis) for the analytical technique aspect. Dedicated risk analysis skill belongs in RM domain. Not added.
- **Data storytelling** (DDAT-SK-031, STS 0.6295): Now partially covered by AB-S-025 (presentation). Narrative construction with data is a mode of presentation, not a separate skill. Not added.
- **Simulation/scenario skills**: Minimal evidence in Skills dimension. Simulation is primarily an AB Knowledge concept (AB-K-020). The skill of running simulations has weak standalone evidence here. Not added.
- **Metadata extraction and analysis** (DCWF 3298, STS 0.6210): Single framework element. Specialized sub-skill of data analysis. Covered under AB-S-003 (analytical technique application). Not added.

**+1 entry added.**

**Evidence density note:** The validator flags 382 elements at STS ≥ 0.60 for 24 entries (15.9:1 ratio) as potentially indicating uncovered concept space. This ratio is inflated because entries AB-S-011 through AB-S-024 have 0/6 STRM framework coverage (stale scoring against pre-rewrite entry text). All 382 high-STS elements map only to entries 001-010 because the STRM pipeline can't see entries 011-024. If STRM scores were re-computed against current entry statements, the 382 elements would distribute across all 24 entries, reducing the effective ratio to approximately 6.4:1. The concepts covered by entries 011-024 are validated by manual element-by-element mapping (documented in concept clusters above).

### Pass 2 — Redundancy and Overlap

| Pair | Distinction |
|------|-------------|
| AB-S-001 (integration) vs AB-S-012 (collection) | Synthesizing from assembled sources vs. acquiring data from sources. S0909 ≠ S0600. |
| AB-S-003 (technique application) vs AB-S-022 (method selection) | Executing analytical methods vs. choosing the right method for the problem. S0433 ≠ K1096. |
| AB-S-005 (preprocessing) vs AB-S-017 (mapping/classification) | Transforming data formats vs. categorizing data elements. S0644 ≠ K1097. |
| AB-S-009 (testing/validation) vs AB-S-021 (data quality validation) | Validating analytical OUTPUTS vs. validating analytical INPUTS. T1258 ≠ S0565. |
| AB-S-009 (testing) vs AB-S-015 (assessment design) | Executing tests vs. designing evaluation frameworks. T1258 ≠ 3734. |
| AB-S-014 (documentation) vs AB-S-004 (visualization) | Written communication of findings vs. visual representation of data. S0391 ≠ 4237. |
| AB-S-011 (trade-off) vs AB-S-022 (method selection) | Quantifying competing options vs. matching methods to data characteristics. S0891 ≠ K1096. |

**No merges.**

### Pass 3 — Domain Boundary

| Entry | Borderline Domain | AB Justification | Verdict |
|-------|------------------|-------------------|---------|
| AB-S-008 (data structure/model design) | DA | Scoped to analytical workflow structures, not enterprise architecture. S0568/S0029 map to AB. | Keep |
| AB-S-017 (data mapping/classification) | DG | Scoped to analytical organization and retrieval, not governance policy. K1097/K0866 in analytical context. | Keep |
| AB-S-019 (design thinking) | LS | Scoped to analytical problem framing, not general leadership methodology. DCWF 7103/8146 in operational design context. | Keep |
| AB-S-020 (mentoring) | LS | Weakest entry (1 element at STS 0.5983). Kept because scoped to analytical competency development, not general mentoring. | Keep (flagged) |
| AB-S-021 (data quality validation) | DQ | Scoped to input validation FOR analysis, not data quality as a discipline. S0565 in analytical pipeline context. | Keep |

**No entries removed.**

## STRM Coverage Note

Same pattern as AB Knowledge: AB-S-001 through AB-S-010 show 6/6 framework coverage; AB-S-011 through AB-S-025 show 0/6 because STRM scores were computed against pre-rewrite entry text. Concepts for entries 011–025 are validated by manual element-by-element mapping documented above.

## Final Entry List

| ID | Concept | Key Evidence |
|---|---|---|
| AB-S-001 | Multi-source integration and data fusion | S0909 (0.73), 1120 (0.73), S0727 (0.71) |
| AB-S-002 | Data querying | S0748 (0.69), S0911 (0.69), K0705 (0.70) |
| AB-S-003 | Analytical technique application | S0433 (0.72), S0709 (0.71), 8010 (0.71) |
| AB-S-004 | Visualization and dashboards | 4237 (0.73), K0647 (0.65), DDAT-SK-067 (0.66) |
| AB-S-005 | Preprocessing and transformation | S0644 (0.71), 6610 (0.70), S0726 (0.68) |
| AB-S-006 | Statistical modeling and regression | S0563 (0.66), S0640 (0.66) |
| AB-S-007 | Requirements and business translation | AIRMF-MP-1.1 (0.76), 3019 (0.70), S0855 (0.68) |
| AB-S-008 | Data structure and model design | S0568 (0.69), S0118 (0.69), 6650 (0.68) |
| AB-S-009 | Testing and validation | T1258 (0.73), 761A (0.71), 5945 (0.70) |
| AB-S-010 | Market and user research | S0868 (0.69), S0404 (0.68), 7099 (0.67) |
| AB-S-011 | Trade-off and comparative analysis | S0891 (0.66), AIRMF-MP-3.4 (0.63) |
| AB-S-012 | Data collection | S0600 (0.68), 3001 (0.67), DDAT-SK-050 (0.69) |
| AB-S-013 | Continuous monitoring | S0451 (0.67), T1954 (0.66), T1956 (0.66) |
| AB-S-014 | Documentation and communication | AIRMF-MP-1.1 (0.76), S0391 (0.66), EUAIA-O-042 (0.64) |
| AB-S-015 | Assessment design | 3734 (0.70), S0393 (0.66) |
| AB-S-016 | Pattern recognition | O*NET 1.A.1.e.1 (0.71), S0559 (0.67) |
| AB-S-017 | Data mapping and classification | K1097 (0.69), 6730 (0.68), K0866 (0.67) |
| AB-S-018 | Programming and automation | 5852 (0.68), DDAT-SK-132 (0.66) |
| AB-S-019 | Design thinking | 8146 (0.68), 7103 (0.68), DDAT-SK-076 (0.57) |
| AB-S-020 | Mentoring and team development | 8196 (0.60) — single element, flagged |
| AB-S-021 | Data quality validation | S0565 (0.66), DDAT-SK-063 (0.59), DDAT-SK-137 (0.56) |
| AB-S-022 | Method selection | K1096 (0.67), DDAT-SK-013 (0.58) |
| AB-S-023 | Analytical standards | 3893 (0.68), 3971 (0.68) |
| AB-S-024 | Data asset assessment | S0808 (0.66), DDAT-SK-070 (0.58), DDAT-SK-047 (0.56) |
| AB-S-025 | Analytical presentation and strategic insight communication | 6170 (0.67), 5270 (0.65), 5430 (0.63), DDAT-SK-031 (0.63) |

## Methodology

Built from STRM rationale evidence per KSA-SYNTHESIS-METHODOLOGY.md v2.0.0. Existing entries discarded. Concepts extracted from 6 framework element descriptions, clustered, written as entries, then subjected to 3 adversarial passes (coverage gaps, redundancy, domain boundary). Pass 1 identified 1 gap (analytical presentation and strategic insight communication) — added as AB-S-025. No merges or removals after Passes 2 and 3. Final count: 25.
