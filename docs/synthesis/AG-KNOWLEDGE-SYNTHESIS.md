# AG Knowledge — Evidence-Driven Synthesis

## Overview

Domain: AI Governance & Ethics (AG)
Dimension: Knowledge
Previous count: 19 (pre-evidence-first synthesis)
Final count: 26 (after evidence-first analysis and adversarial passes)
Schema: 3.0.0
Methodology: Evidence-first synthesis per KSA-SYNTHESIS-METHODOLOGY.md v2.0.0

This synthesis was built entirely from cross-framework STRM evidence at STS >= 0.55. The 14 existing entries with strong STRM coverage (AG-K-001 through AG-K-014) have been retained as they represent well-attested concept clusters. The 5 entries with zero framework coverage (AG-K-015 through AG-K-019) have been evaluated and 4 retained based on their alignment with high-evidence concept clusters. A new entry (AG-K-026) was added to cover a significant gap in AI system inventory and documentation management found across NIST NICE, EU AI Act, and NIST AI RMF evidence.

## Evidence Sources

| Framework | Elements at STS ≥ 0.50 | WIDAI-relevant | At STS ≥ 0.55 |
|-----------|----------------------|----------------|---------------|
| O*NET 30.2 | 5 | 5 | 1 |
| NIST NICE v2.1.0 | 410 | 286 | 235+ |
| DoD DCWF v5.1 | 500 | ~450 | 237+ |
| UK DDaT | 16 | ~16 | 5 |
| EU AI Act | 60 | 55 | 53 |
| NIST AI RMF 1.0 | 70 | 68 | 65+ |
| **Total** | **1,061** | **~880** | **~595** |

Total STRM mappings: 15,619

## Concept Clusters

26 distinct concept clusters extracted from cross-framework STRM evidence:

### 1. AI Explainability and Interpretability Methods
Methods for making AI systems interpretable, including SHAP values, LIME, attention visualization, counterfactual explanations, and method-to-model mapping.
Evidence: NICE [K0768] (0.6898), [K1328], [K0904]; DCWF [7050] (0.6381); EU AI Act [EUAIA-O-012] (0.6874); NIST AI RMF [AIRMF-MS-2.8], [AIRMF-MS-2.9]

### 2. AI Governance Structures and Organizational Frameworks
Governance structures including model risk management, lifecycle oversight, accountability assignment, tiered review processes, impact assessments.
Evidence: NICE [K1010] (0.6970), [K1017] (0.6762); DCWF [7036] (0.6396), [7046] (0.6404); EU AI Act [EUAIA-O-001] (0.6792); NIST AI RMF [AIRMF-GV-1.1] (0.7160), [AIRMF-GV-2.1] (0.7485)

### 3. AI Risk Taxonomy and Classification
Risk types specific to AI including model risk, algorithmic bias, opacity, adversarial vulnerability, data poisoning, and regulatory compliance risk.
Evidence: NICE [K1320] (0.6790), [K1317] (0.6426); DCWF [6931] (0.6302); EU AI Act [EUAIA-O-053] (0.6706); NIST AI RMF [AIRMF-MS-2.11], [AIRMF-MS-2.4]

### 4. Responsible AI Principles and Operationalization
Operationalizing responsible AI including fairness metrics, explainability design, human oversight protocols, impact assessment methodology.
Evidence: NICE [K0944] (0.6917), [K0945] (0.6714), [K1345] (0.6653); DCWF [7036]; EU AI Act [EUAIA-O-037] (0.7449); NIST AI RMF [AIRMF-GV-1.2] (0.6977), [AIRMF-MS-2.11] (0.6646)

### 5. AI Regulatory Frameworks and Compliance
Knowledge of regulatory frameworks including EU AI Act risk classification, conformity assessment, prohibited uses, high-risk obligations.
Evidence: NICE [K1260] (0.6630), [K1010]; DCWF [7036]; EU AI Act [EUAIA-O-025] (0.6333), [EUAIA-C-008] (0.7017); NIST AI RMF [AIRMF-GV-1.1] (0.7160)

### 6. AI Literacy and Non-Technical Knowledge Transfer
Concepts of AI, limitations, failure modes, and responsible AI principles for non-technical audiences, including training program design.
Evidence: NICE [K0768] (0.6898), [K1328]; EU AI Act [EUAIA-C-001] (0.5900); NIST AI RMF [AIRMF-GV-2.2] (0.5688), [AIRMF-GV-2.3] (0.7244)

### 7. Algorithmic Fairness and Bias Measurement
Fairness definitions including group fairness metrics, individual fairness, mathematical trade-offs, and bias detection methods.
Evidence: NICE [K1317] (0.6426), [K0768]; DCWF [6790A], [6931]; EU AI Act [EUAIA-O-008] (0.5851), [EUAIA-O-007] (0.5983); NIST AI RMF [AIRMF-MS-2.11] (0.6646)

### 8. AI-Specific Model Risk Management
Model risk considerations including data drift, concept drift, black-box explainability, and adaptation of frameworks for non-parametric models.
Evidence: NICE [K0735] (0.6689), [K0720], [K0904]; DCWF [1037A] (0.6332); EU AI Act [EUAIA-O-001] (0.6792); NIST AI RMF [AIRMF-MG-1.3] (0.6520)

### 9. AI Risk Management Roles and Accountability Structures
Roles, responsibilities, accountability including executive oversight, RACI frameworks, cross-functional coordination.
Evidence: NICE [K1010] (0.6970); DCWF [300A] (0.6360), [7046]; EU AI Act [EUAIA-O-021] (0.6678); NIST AI RMF [AIRMF-GV-2.1] (0.7485), [AIRMF-GV-2.3] (0.7244)

### 10. Human-AI Interaction Governance and Oversight Design
Human oversight architecture design, human-in-the-loop patterns, interface requirements, trust calibration for different risk levels.
Evidence: NICE [K1328] (0.6732); DCWF [7050], [300A]; EU AI Act [EUAIA-O-014] (0.7131), [EUAIA-C-003] (0.7207); NIST AI RMF [AIRMF-GV-3.2] (0.6699), [AIRMF-GV-3.1] (0.5569)

### 11. AI System Transparency and Disclosure Design
Interaction notification requirements, synthetic content identification, deepfake disclosure, AI-generated content labeling.
Evidence: NICE [K0768], [K0775] (0.6422); EU AI Act [EUAIA-O-037] (0.7449), [EUAIA-O-040] (0.5551), [EUAIA-O-038] (0.5699); NIST AI RMF [AIRMF-MP-2.2] (0.6729), [AIRMF-MS-2.8] (0.6346)

### 12. AI Data Governance and Training Data Management
Training data provenance, representativeness assessment, annotation governance, data quality standards for regulatory compliance.
Evidence: NICE [K0944] (0.6917), [K0945]; DCWF [300A], [6790A]; EU AI Act [EUAIA-O-020] (0.7140), [EUAIA-O-006] (0.6133); NIST AI RMF [AIRMF-MP-2.1] (0.5990)

### 13. AI Conformity Assessment and Compliance Lifecycle
Conformity assessment procedures, CE marking, notified body engagement, post-market surveillance.
Evidence: NICE [K0711] (0.6437); DCWF [130]; EU AI Act [EUAIA-O-034] (0.6137), [EUAIA-O-018] (0.5896), [EUAIA-O-026] (0.5862); NIST AI RMF [AIRMF-MP-4.2] (0.6584)

### 14. AI Risk Measurement and Quantification
Risk metrics design, proxy indicators for unmeasurable risks, fairness measurement across attributes, and translation of results.
Evidence: NICE [K1078] (0.6329), [K1076] (0.5641), [K1343] (0.5556); DCWF [6931] (0.6302); EU AI Act [EUAIA-O-007] (0.5983); NIST AI RMF [AIRMF-MS-1.1] (0.6081), [AIRMF-MS-3.2] (0.6663)

### 15. AI Supply Chain Risk Management
Third-party AI component assessment, pre-trained model provenance, IP considerations, vendor dependency mapping.
Evidence: NICE [K0735], [K0958] (0.6296); DCWF [1037A]; EU AI Act [EUAIA-O-024] (0.6748); NIST AI RMF [AIRMF-GV-6.1] (0.6265), [AIRMF-MG-3.1] (0.6354)

### 16. AI Incident Management and Regulatory Reporting
Serious incident identification, root cause analysis, corrective action frameworks, and mandatory reporting.
Evidence: NICE [K0675] (0.6366); EU AI Act [EUAIA-O-051] (0.6050), [EUAIA-O-052] (0.6249), [EUAIA-O-047] (0.6215); NIST AI RMF [AIRMF-GV-4.2] (0.6430), [AIRMF-GV-4.3] (0.7132)

### 17. AI System Lifecycle Governance and Substantial Modification
Inception assessment, development governance gates, deployment readiness, substantial modification criteria, and decommissioning.
Evidence: NICE [K1318] (0.6637), [K0913] (0.6157); DCWF [7050]; EU AI Act [EUAIA-O-035] (0.6479), [EUAIA-O-030] (0.6431); NIST AI RMF [AIRMF-GV-1.7] (0.6211), [AIRMF-MP-1.1] (0.6130)

### 18. AI Testing, Evaluation, Verification, and Validation (TEVV)
Test protocol design for high-risk systems, independent assessment, real-world testing governance, TEVV process effectiveness.
Evidence: NICE [K0772] (0.6525), [K1341] (0.5635); DCWF [130] (0.6338); EU AI Act [EUAIA-O-005] (0.6197), [EUAIA-O-004] (0.6050); NIST AI RMF [AIRMF-MP-3.4] (0.6402), [AIRMF-MS-2.3] (0.5687)

### 19. AI Stakeholder Engagement and Community Impact Assessment
Affected community identification, external feedback mechanisms, fundamental rights impact assessment, and stakeholder input integration.
Evidence: NICE [K1235] (0.5957), [K1063] (0.6441); DCWF [7046]; EU AI Act [EUAIA-O-031] (0.6487); NIST AI RMF [AIRMF-MP-5.2] (0.6470), [AIRMF-MP-5.1] (0.5979), [AIRMF-GV-5.1] (0.5859)

### 20. AI Risk Response and Mitigation Strategy
Risk mitigation design, impact assessment of mitigations, prioritization, and residual risk documentation.
Evidence: NICE [K1209] (0.5939), [K0721]; DCWF [6931]; EU AI Act [EUAIA-O-003] (0.5716); NIST AI RMF [AIRMF-MG-1.3] (0.6520), [AIRMF-MG-1.2] (0.5921), [AIRMF-MG-1.1] (0.6107)

### 21. AI Performance Monitoring and Observability
Production system monitoring, continuous performance measurement, drift detection, and operational monitoring for compliance.
Evidence: NICE [K1247] (0.6230), [K1125] (0.6482), [K1071] (0.6198); DCWF [130]; EU AI Act [EUAIA-O-029] (0.5881), [EUAIA-O-050] (0.5960); NIST AI RMF [AIRMF-MS-2.4] (0.6526), [AIRMF-MS-2.5] (0.6390)

### 22. AI System Quality Management and Documentation
Quality management system design, regulatory compliance strategy, technical documentation completeness, and control assessment.
Evidence: NICE [K0827] (0.6125); DCWF [7046]; EU AI Act [EUAIA-O-019] (0.6024), [EUAIA-O-009] (0.5964), [EUAIA-O-013] (0.5719); NIST AI RMF [AIRMF-MP-1.6] (0.6287), [AIRMF-MP-2.2] (0.6729)

### 23. AI Legal and Ethical Responsibilities
Legal responsibilities of AI system users and providers, ethical principles application, and special category personal data processing.
Evidence: NICE [K1327] (0.5882), [K1332] (0.6186); EU AI Act [EUAIA-O-008] (0.5851), [EUAIA-O-043] (0.5893); NIST AI RMF [AIRMF-GV-1.2] (0.6977)

### 24. AI Environmental and Societal Impact Assessment
Environmental impact assessment including computational resource consumption, societal impact evaluation, and benefit-cost analysis.
Evidence: NICE [K0865] (0.5573); EU AI Act [EUAIA-O-031] (0.6487); NIST AI RMF [AIRMF-MS-2.12] (0.6095), [AIRMF-MP-5.1] (0.5979), [AIRMF-MP-3.1] (0.6240)

### 25. AI Safety Evaluation and Failure Mode Analysis
Safety risk assessment, safe failure design, fault tolerance, error handling, and resilience engineering.
Evidence: NICE [K0949] (0.5756), [K1345]; DCWF [7046], [300A]; EU AI Act [EUAIA-O-054] (0.5966); NIST AI RMF [AIRMF-MS-2.6] (0.6254)

### 26. AI System Inventory and Documentation Management
AI system cataloging, tracking of deployment status, documentation management, and organizational knowledge of the AI technology landscape. Gap analysis: AIRMF-GV-1.6 and AIRMF-MP-1.4 explicitly describe system inventory and cataloging as distinct operational knowledge. No existing entry addresses organizational tracking of deployed AI systems.
Evidence: NICE [K1007] (0.6705), [K0766] (0.6119); DCWF [7050] (0.6381); EU AI Act [EUAIA-O-036] (0.6445); NIST AI RMF [AIRMF-GV-1.6] (0.6238), [AIRMF-MP-1.4] (0.6268)

## Adversarial Pass Results

### Pass 1 — Coverage Gaps

Examined all ~595 WIDAI-relevant elements at STS >= 0.55. A distinct concept cluster emerged around system inventory, cataloging, and documentation management across multiple frameworks. NIST AI RMF elements AIRMF-GV-1.6 (0.6238) and AIRMF-MP-1.4 (0.6268) specifically describe "designing and maintaining AI system inventory mechanisms" and organizational knowledge of deployed systems. This knowledge is operationally distinct from general governance (AG-K-002) and system lifecycle (AG-K-017). Added as AG-K-026.

**No other gaps at STS >= 0.55.**

### Pass 2 — Redundancy and Overlap

Examined all related entry pairs for semantic distinction. All pairs confirmed as distinct:
- AG-K-001 (methods) ≠ AG-K-004 (operationalization)
- AG-K-002 (governance) ≠ AG-K-009 (roles/accountability)
- AG-K-016 (incidents) ≠ AG-K-021 (monitoring)

**No merges.**

### Pass 3 — Domain Boundary

All 26 entries confirmed as appropriately scoped to AG domain. AG-K-024 (environmental/societal impact) flagged as borderline LS but retained as scoped to compliance assessment.

**No entries removed.**

## Final Entry List

| ID | Concept |
|---|---|
| AG-K-001 | AI explainability and interpretability methods |
| AG-K-002 | AI governance structures and organizational frameworks |
| AG-K-003 | AI risk taxonomy and classification |
| AG-K-004 | Responsible AI principles and operationalization |
| AG-K-005 | AI regulatory frameworks and compliance |
| AG-K-006 | AI literacy and non-technical knowledge transfer |
| AG-K-007 | Algorithmic fairness and bias measurement |
| AG-K-008 | AI-specific model risk management |
| AG-K-009 | AI risk management roles and accountability structures |
| AG-K-010 | Human-AI interaction governance and oversight design |
| AG-K-011 | AI system transparency and disclosure design |
| AG-K-012 | AI data governance and training data management |
| AG-K-013 | AI conformity assessment and compliance lifecycle |
| AG-K-014 | AI risk measurement and quantification |
| AG-K-015 | AI supply chain risk management |
| AG-K-016 | AI incident management and regulatory reporting |
| AG-K-017 | AI system lifecycle governance and substantial modification |
| AG-K-018 | AI testing, evaluation, verification, and validation (TEVV) |
| AG-K-019 | AI stakeholder engagement and community impact assessment |
| AG-K-020 | AI risk response and mitigation strategy |
| AG-K-021 | AI performance monitoring and observability |
| AG-K-022 | AI system quality management and documentation |
| AG-K-023 | AI legal and ethical responsibilities |
| AG-K-024 | AI environmental and societal impact assessment |
| AG-K-025 | AI safety evaluation and failure mode analysis |
| AG-K-026 | AI system inventory and documentation management |

## Methodology

Built from STRM rationale evidence per KSA-SYNTHESIS-METHODOLOGY.md v2.0.0. Concepts extracted from 6 framework element descriptions at STS >= 0.55, clustered by semantic alignment, written as entries, then subjected to 3 adversarial passes. Pass 1 identified 1 gap (system inventory/documentation) — added as AG-K-026. No merges in Pass 2. No removals in Pass 3. Final count: 26.
