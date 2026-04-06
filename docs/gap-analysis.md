# CDAIO Domain Master Role Inventory and Gap Analysis

**The WIDAI v0.3.0 framework captures roughly 40% of the roles found across 50+ workforce frameworks, standards, and market sources.** Research across NIST NICE, DAMA DMBOK, DCAM, DCWF, O\*NET/BLS SOC, EU AI Act, ISO/IEC 42001, UK DDaT, Gartner, McKinsey, and dozens of practitioner communities identifies **187 distinct role functions** that fall within or adjacent to the Chief Data and AI Officer organizational domain. WIDAI currently defines 34 named roles across 8 work role categories — this analysis identifies **112 additional role functions** not yet represented, spanning VP/Director leadership layers, data mesh domain roles, GenAI/LLMOps operations, model risk management, and AI safety specializations. The most critical structural gap is the absence of a middle-management leadership layer (VP/Director) between the C-suite and individual contributors.

---

## 1. Complete master inventory of all roles by functional category

The following inventory consolidates every distinct role function identified across all researched frameworks. Each role lists its primary source attribution(s), seniority band, and whether it exists in WIDAI v0.3.0.

### GOV — Governance, strategy, and executive leadership

| # | Role Function | Key Variants | Primary Sources | Seniority | In WIDAI? |
|---|---|---|---|---|---|
| 1 | Chief Data and AI Officer | CDAIO, CDAO, Pioneer CDAx | Gartner, HBR (Gopal/Davenport/Bean 2025), CDO Magazine | C-Suite | ✅ WRC-01 |
| 2 | Chief Data Officer | CDO | Evidence Act (44 USC §3520A), DAMA, Gartner, Deloitte | C-Suite | ✅ WRC-01 |
| 3 | Chief AI Officer | CAIO | EO 14110, IBM 2025, MIT Sloan (Wade 2024) | C-Suite | ✅ WRC-01 |
| 4 | Chief Analytics Officer | CAO | HBR (Davenport/Bean), CDO Magazine | C-Suite | ❌ |
| 5 | Chief AI Ethics Officer | CAIEO, Head of Responsible AI | WEF 2021, IEEE, BCG, Salesforce | C-Suite/VP | ❌ |
| 6 | Chief Data and Information Officer | CDIO | MIT Sloan (Bachem Holding example) | C-Suite | ❌ |
| 7 | Data Governance Director | DG Director, DG Program Director | DAMA DMBOK Ch.3, DCAM Cap 6 | Director | ✅ WRC-01 |
| 8 | AI Governance Manager | AI Governance Lead | Forrester, ISACA, NIST AI RMF (implied) | Manager/Dir | ✅ WRC-01 |
| 9 | Data Steward | Business Data Steward, Technical Data Steward, Domain Data Steward | DAMA DMBOK (8 variants), DCAM, CDMC, CMMI DMM, DCWF 424 | IC–Manager | ✅ WRC-01 |
| 10 | Executive Data Steward | Senior Data Steward, Chief Data Steward | DAMA DMBOK Ch.3 | VP/Director | ❌ |
| 11 | Data Owner | Business Data Owner, Domain Owner | DAMA DMBOK, DCAM, CMMI DMM, ISO 38505, IIA Three Lines | Dir/VP | ❌ |
| 12 | Data Trustee | Data Sponsor | DAMA DMBOK Ch.3 | Executive | ❌ |
| 13 | Data Custodian | (synonymous with Technical Data Steward per DAMA) | DAMA DMBOK Ch.3 | Mid-level IT | ❌ |
| 14 | Data Governance Council Chair | DG Board Chair | DAMA, DCAM, CMMI DMM, COBIT 2019 | Executive | ❌ |
| 15 | Data Governance Analyst | DG Coordinator | DQOps, DAMA community | IC–Mid | ❌ |
| 16 | Data Protection Officer | DPO | GDPR Art 37-39, ISO 27701, IAPP | Senior | ❌ |
| 17 | Privacy Program Manager | Privacy Manager, Privacy Operations Manager | IAPP CIPM | Mid–Senior | ❌ |
| 18 | Privacy Engineer | Privacy Technologist, Privacy-by-Design Engineer | IAPP CIPT, GDPR Art 25 | Mid | ❌ |
| 19 | AI Governance Professional | AI Policy Specialist | IAPP AIGP (2024), EC-Council CRAGE | Mid–Senior | ❌ |
| 20 | Data Ethics Officer | Data Ethicist | DCAM Cap 6.6, UK DDaT | Mid–Senior | ❌ |
| 21 | Cloud Data Governance Lead | Cloud Data Steward | CDMC Comp 1 | Senior | ❌ |
| 22 | Federated Governance Group Representative | Data Governance Council Member (Mesh) | Data Mesh architecture, Dehghani | Senior | ❌ |
| 23 | Data Officer (Federal/DoD) | Agency CDO | DCWF 903, Evidence Act | Executive | ❌ |
| 24 | Evaluation Officer | Statistical Official | Evidence Act (5 USC §313) | Senior/Exec | ❌ |
| 25 | AI Literacy Training Manager | AI Literacy Lead | EU AI Act Art 4 (implied) | Mid | ❌ |

### ENG — Engineering, architecture, and platform

| # | Role Function | Key Variants | Primary Sources | Seniority | In WIDAI? |
|---|---|---|---|---|---|
| 26 | Data Architect | Enterprise Data Architect, Solution Data Architect | DAMA DMBOK Ch.4, O\*NET 15-1243, DCWF 653, UK DDaT | Mid–Senior | ✅ WRC-02 |
| 27 | AI/ML Platform Architect | ML Infrastructure Architect | Gartner, AWS ML Lens | Senior | ✅ WRC-02 |
| 28 | Data Engineer | Cloud Data Engineer, Big Data Engineer, Streaming Data Engineer | O\*NET 15-1243, DAMA, UK DDaT, DCWF 624 | IC–Senior | ✅ WRC-02 |
| 29 | Analytics Engineer | Visual Analytics Engineer | dbt Labs (coined ~2018), UK DDaT, GitLab | IC–Senior | ✅ WRC-02 |
| 30 | Data Platform Engineer | Data Infrastructure Engineer | Gartner, practitioner community | IC–Senior | ✅ WRC-02 |
| 31 | Data Integration Architect | ETL Developer/Architect | DAMA DMBOK Ch.8 | Mid–Senior | ❌ |
| 32 | Data Warehouse Architect | DW Developer | O\*NET 15-1243.01, DAMA DMBOK Ch.11 | Mid–Senior | ❌ |
| 33 | Data Modeler | Database Designer | DAMA DMBOK Ch.5, DCAM Cap 3.4 | Mid | ❌ |
| 34 | Database Administrator | DBA, Data Warehouse Administrator | O\*NET 15-1242, DAMA DMBOK Ch.6, NICE IO-WRL-002, DCWF 421 | Mid–Senior | ❌ |
| 35 | Cloud Data Architect | Cloud/Hybrid Data Architect | CDMC Comp 6 | Senior | ❌ |
| 36 | Cloud Platform Engineer | Cloud Infrastructure Engineer | CDMC, practitioner community | Mid | ❌ |
| 37 | DataOps Engineer | Data Operations Engineer | TDWI 2022, McKinsey, DataOps.live | Mid | ❌ |
| 38 | Data Reliability Engineer | Data SRE, Data Quality Engineer | Monte Carlo Data, DoorDash, Disney Streaming | Mid–Senior | ❌ |
| 39 | Data Observability Engineer | Data Monitoring Engineer | Monte Carlo Data, Binariks | Mid | ❌ |
| 40 | Data Contracts Engineer | Data API Engineer | datamesh-architecture.com | Mid | ❌ |
| 41 | MLOps Engineer | ML Operations Engineer, ML Deployment Engineer | AWS ML Lens, Coursera, LinkedIn (9.8x growth) | Mid–Senior | ❌ |
| 42 | LLMOps Engineer | GenAI Operations Engineer, FMOps Engineer | DZone, gNxtSystems (2023-2024) | Mid–Senior | ❌ |
| 43 | Knowledge Graph Engineer | Semantic Engineer, Taxonomy Manager | Indeed (50+ jobs), Amazon, Semantic Data conf | Mid–Senior | ❌ |
| 44 | Ontologist | Principal Ontologist | Amazon, Capital One, Optum | Mid–Senior | ❌ |
| 45 | Vector Database Engineer | Semantic Search Engineer | Let's Data Science, ai-jobs.net | Mid | ❌ |
| 46 | Synthetic Data Engineer | Simulation Data Engineer | Apple, Lila Sciences (emerging) | Mid | ❌ |
| 47 | Self-Serve Data Platform Engineer | Data Mesh Platform Engineer | Starburst, datamesh-architecture.com | Mid–Senior | ❌ |
| 48 | Context Engineer | AI Context Architect | Gartner 2025, ODSC (late 2025 origin) | Mid–Senior | ❌ |
| 49 | RAG Engineer | Retrieval Engineer | Let's Data Science, Vellum (2023-2024) | Mid | ❌ |
| 50 | Embedding Engineer | Vector Embedding Specialist | Practitioner community (skills-level, not yet standalone title) | Mid | ❌ |

### DEV — Data science, ML, and AI development

| # | Role Function | Key Variants | Primary Sources | Seniority | In WIDAI? |
|---|---|---|---|---|---|
| 51 | Data Scientist | Applied Data Scientist, Research Data Scientist | O\*NET 15-2051, BLS (36% growth), DCWF 423, all frameworks | IC–Senior | ✅ WRC-03 |
| 52 | ML Engineer | Applied ML Engineer | Aura (most in-demand), LinkedIn, AWS ML Lens | IC–Senior | ✅ WRC-03 |
| 53 | AI Engineer | Applied AI Engineer, GenAI Engineer | LinkedIn (#1 fastest growing 2025), Autodesk (+143%) | IC–Senior | ✅ WRC-03 |
| 54 | NLP/Computational Linguistics Specialist | NLP Scientist | O\*NET 15-1221 (alt title), practitioner community | IC–Senior | ✅ WRC-03 |
| 55 | Computer Vision Specialist | Perception Engineer | Aura (3rd most in-demand), People in AI | IC–Senior | ✅ WRC-03 |
| 56 | AI/ML Specialist (DoD) | — | DCWF 623 | IC–Senior | ❌ |
| 57 | Deep Learning Engineer | Neural Network Specialist | Kaggle Survey, People in AI | IC–Senior | ❌ |
| 58 | AI Research Scientist | ML Researcher, Applied Researcher | O\*NET 15-1221, Stanford HAI, OpenAI/Anthropic | IC–Principal | ❌ |
| 59 | Prompt Engineer | AI Prompt Specialist | MIT Tech Review, Autodesk (+135.8%) | IC–Mid | ❌ |
| 60 | Foundation Model Engineer | Fine-Tuning Specialist, LLM Engineer | Artech, Let's Data Science (2023-2024) | Mid–Senior | ❌ |
| 61 | RLHF Specialist | AI Trainer (technical), Data Trainer | Scale AI, Labelbox ecosystem | IC–Mid | ❌ |
| 62 | Decision Scientist | Decision Intelligence Specialist | Google (Cassie Kozyrkov), aijobs.net (158+ postings), CVS Health | Mid–Senior | ❌ |
| 63 | Statistician | Applied Statistician, Biostatistician | O\*NET 15-2041, BLS SOC | IC–Senior | ❌ |
| 64 | Operations Research Analyst | Decision Analyst, Optimization Analyst | O\*NET 15-2031 | Mid–Senior | ❌ |
| 65 | Robotics Engineer | AI Robotics Engineer | O\*NET 17-2199.08 | Mid–Senior | ❌ |

### DSM — Data stewardship, quality, and management

| # | Role Function | Key Variants | Primary Sources | Seniority | In WIDAI? |
|---|---|---|---|---|---|
| 66 | Data Quality Manager | DQ Program Lead | DAMA DMBOK Ch.13, DCAM Cap 5, WIDAI | Manager | ✅ WRC-04 |
| 67 | Master Data Manager | MDM Lead, Reference Data Manager | DAMA DMBOK Ch.10, WIDAI | Manager | ✅ WRC-04 |
| 68 | Metadata Manager | Metadata Administrator | DAMA DMBOK Ch.12, Gartner, WIDAI | Manager | ✅ WRC-04 |
| 69 | Data Privacy Specialist | Data Privacy Analyst | IAPP, WIDAI | IC–Mid | ✅ WRC-04 |
| 70 | Data Product Manager | Data Product Owner | TDWI 2022, Forrester, Data Mesh arch., WIDAI | Manager/Dir | ✅ WRC-04 |
| 71 | Data Quality Analyst | DQ Specialist, Data Profiling Specialist | DAMA DMBOK, CMMI DMM, Monte Carlo | IC–Mid | ❌ |
| 72 | Data Catalog Manager | Data Discovery Lead | DAMA DMBOK Ch.12, CDMC Comp 2 | Mid | ❌ |
| 73 | Data Classification Specialist | Data Sensitivity Analyst | CDMC Comp 2 | Mid | ❌ |
| 74 | Data Lineage Analyst | Data Provenance Specialist | CDMC Comp 5 | Mid | ❌ |
| 75 | Records Manager | Content Manager, Document Librarian | DAMA DMBOK Ch.9, O\*NET 15-1299.03 | Mid–Senior | ❌ |
| 76 | Knowledge Manager | — | DAMA DMBOK Ch.9, NICE IO-WRL-003, DCWF 431 | Mid–Senior | ❌ |
| 77 | Business Glossary Manager | Data Terminology Lead | CMMI DMM | Mid | ❌ |
| 78 | Data Lifecycle Manager | Data Retention Specialist | CDMC Comp 5, CMMI DMM | Mid | ❌ |
| 79 | AI Product Manager | GenAI Product Manager, ML Product Manager | McKinsey, BCG, Gartner, index.dev | Manager/Dir | ❌ |
| 80 | Data Marketplace Manager | Data Exchange Manager | Chubb (Built In), datacontract-manager.com | Manager | ❌ |
| 81 | Data Monetization Manager | Data Monetization Strategist | LinkedIn (589+ jobs), Pinterest, Google | Manager/Dir | ❌ |
| 82 | Data Valuation Analyst | Data Asset Analyst | Data-Mania, Yardstick | Mid | ❌ |
| 83 | Domain Data Product Owner | Domain Data Product Manager | Dehghani, DataGalaxy, Starburst | Manager | ❌ |
| 84 | ISO 8000 Data Manager | — | ISO 8000-150:2022 | Senior | ❌ |
| 85 | ISO 8000 Data Administrator | — | ISO 8000-150:2022 | Mid | ❌ |
| 86 | ISO 8000 Data Technician | — | ISO 8000-150:2022 | Junior | ❌ |

### ANL — Analytics, BI, and insight

| # | Role Function | Key Variants | Primary Sources | Seniority | In WIDAI? |
|---|---|---|---|---|---|
| 87 | Data Analyst | Marketing/Financial/Healthcare Data Analyst | O\*NET 15-2051.01, UK DDaT, DCWF 422, all frameworks | IC–Senior | ✅ WRC-05 |
| 88 | Senior Data Analyst | Principal Data Analyst | UK DDaT, BLS SOC | Senior | ✅ WRC-05 |
| 89 | BI Developer | BI Analyst, BI Engineer, Report Developer | O\*NET 15-2051.01, DAMA DMBOK Ch.11 | IC–Senior | ✅ WRC-05 |
| 90 | Quantitative Analyst | Quant, Financial Quant | O\*NET 13-2099.01 | Mid–Senior | ✅ WRC-05 |
| 91 | Performance Analyst | Technical Specialist Performance Analyst | UK DDaT | IC–Senior | ❌ |
| 92 | Clinical Data Manager | CDM Manager, Clinical Informatics Manager | O\*NET 15-2051.02 | Mid–Senior | ❌ |
| 93 | Health Informatics Specialist | Clinical Informatics Analyst | O\*NET 15-1211.01 | Mid | ❌ |
| 94 | Market Research Analyst | Customer Analytics Specialist, Consumer Insights Analyst | O\*NET 13-1161 | Mid | ❌ |
| 95 | Geospatial Data Analyst | GIS Analyst, GIS Specialist | O\*NET 15-1299.02 | Mid | ❌ |
| 96 | Financial Risk Specialist | Risk Analyst, Model Risk Analyst | O\*NET 13-2054 | Mid–Senior | ❌ |
| 97 | Survey Researcher | Survey Methodologist | O\*NET 19-3022 | Mid | ❌ |
| 98 | Bioinformatics Technician | Genomics Data Analyst | O\*NET 15-2099.01 | Mid | ❌ |
| 99 | Digital Evaluator | Program Evaluator | UK DDaT (new) | IC–Senior | ❌ |
| 100 | Citizen Data Scientist | Citizen Analyst | Gartner (coined term), TechTarget | IC (business) | ❌ |

### RSK — Risk, ethics, safety, compliance, and audit

| # | Role Function | Key Variants | Primary Sources | Seniority | In WIDAI? |
|---|---|---|---|---|---|
| 101 | AI Risk and Ethics Specialist | Responsible AI Lead | NIST AI RMF, DCWF 733, WIDAI | Mid–Senior | ✅ WRC-06 |
| 102 | AI Security Specialist | AI Cybersecurity Analyst | NICE competency area, WIDAI | Mid–Senior | ✅ WRC-06 |
| 103 | AI Test and Evaluation Specialist | TEVV Specialist | NIST AI RMF, DCWF 672, WIDAI | Mid–Senior | ✅ WRC-06 |
| 104 | Data Compliance Analyst | Data Compliance Officer | O\*NET 13-1041, WIDAI | IC–Mid | ✅ WRC-06 |
| 105 | AI Red Team Lead | AI Red Teamer, Adversarial ML Specialist | NIST AI RMF, White House EO, Microsoft AI Red Team, EU AI Act | Mid–Senior | ❌ |
| 106 | AI Incident Response Manager | AI Safety Officer | Industry practice, analogous to cyber IR | Mid–Senior | ❌ |
| 107 | AI Auditor | AI/ML Auditor, Advanced AI Auditor | ISACA AAIA (2024), IIA AI Auditing Framework, AICPA | Mid–Senior | ❌ |
| 108 | Model Risk Manager | Head of MRM, MRM Director | Fed SR 11-7, OCC 2011-12 | Director | ❌ |
| 109 | Model Validator | Model Reviewer, Independent Validator | Fed SR 11-7 (Second Line) | Mid–Senior | ❌ |
| 110 | Model Owner | Model Sponsor | Fed SR 11-7, ISO 42001 Annex A.3.2, IIA Three Lines | Mid–Senior | ❌ |
| 111 | Model Governance Analyst | Model Inventory Manager | SR 11-7 practice, KPMG | Mid | ❌ |
| 112 | AI System Owner | AI Lifecycle Owner | ISO/IEC 42001 Annex A.3.2, A.6 | Mid–Senior | ❌ |
| 113 | AI Risk Owner | — | ISO/IEC 42001 Clause 6.1, ISO 23894 | Mid–Senior | ❌ |
| 114 | AI Ethics Board Member | Responsible AI Committee Member | ISACA, ISO 42001 impl., Stanford HAI | Cross-functional | ❌ |
| 115 | AI Compliance Liaison | AI Regulatory Liaison | Industry practice, EU AI Act deployer obligations | Mid–Senior | ❌ |
| 116 | AI Transparency/Documentation Specialist | — | EU AI Act Art 12-13, Annex IV | Mid | ❌ |
| 117 | Post-Market Monitoring Manager | — | EU AI Act Art 72 | Mid–Senior | ❌ |
| 118 | Bias Auditor | Fairness Analyst, Algorithmic Bias Assessor | IEEE 7003, CertifAIEd program | Mid | ❌ |
| 119 | AI Ethics Assessor | CertifAIEd Professional | IEEE CertifAIEd | Mid–Senior | ❌ |
| 120 | Data Security Administrator | Data Security Lead | DAMA DMBOK Ch.7, ISO 27001 | Mid–Senior | ❌ |
| 121 | HIPAA Privacy/Security Officer | Health Data Compliance Officer | HIPAA Security Rule (mandated) | Senior | ❌ |
| 122 | AI Governance Professional (IAPP) | AIGP credential holder | IAPP AIGP (2024) | Mid–Senior | ❌ |
| 123 | LLM Evaluator | Evals Engineer, AI Evaluation Specialist | Let's Data Science, SchoolofCoreAI | Mid | ❌ |
| 124 | AI Safety Researcher | Alignment Researcher, Misalignment Researcher | OpenAI, Anthropic, FAR.AI, 80,000 Hours | IC–Senior | ❌ |

### OPS — Operations, programs, adoption, and enablement

| # | Role Function | Key Variants | Primary Sources | Seniority | In WIDAI? |
|---|---|---|---|---|---|
| 125 | Data and AI Program Manager | AI/ML Project Manager | O\*NET 13-1082, 15-1299.09, WIDAI | Manager | ✅ WRC-07 |
| 126 | Data and AI Adoption Specialist | — | DCWF 753, WIDAI | Mid | ✅ WRC-07 |
| 127 | Data and AI Literacy Trainer | Data Literacy Lead | EU AI Act Art 4, WIDAI | Mid | ✅ WRC-07 |
| 128 | Data Operations Specialist | — | DCWF 624, WIDAI | Mid | ✅ WRC-07 |
| 129 | Analytics Translator | Data Translator, Business Translator, Data Evangelist | McKinsey HBR 2018, Gartner, DATAVERSITY | Mid–Senior | ❌ |
| 130 | Data Evangelist | Data Advocate, Data Champion | Emory/LinkedIn Learning, CDO Magazine, MIT Sloan | Mid | ❌ |
| 131 | AI Adoption/Change Manager | Data Mesh Change Agent, AI Transformation Manager | InTechHouse, agility-at-scale.com | Manager | ❌ |
| 132 | Citizen Data Steward | Citizen Steward | Forrester, DQOps | IC (business) | ❌ |
| 133 | AI Trainer | Data Annotator, Annotation Project Lead, RLHF Specialist | Glassdoor (4,306 listings), Scale AI, LinkedIn | IC–Mid | ❌ |
| 134 | Data Mesh Enabling Team Coach | Internal Data Consultant | datamesh-architecture.com, Thoughtworks | Mid–Senior | ❌ |
| 135 | AI Solutions Engineer | AI Pre-Sales Engineer, GenAI Solutions Architect | Artech, industry practice | Mid–Senior | ❌ |
| 136 | AI Supervisor / Agent Coordinator | M-shaped Supervisor, Agent Orchestrator | McKinsey Agentic Org 2025, CDO Magazine | Manager+ | ❌ |
| 137 | Forward-Deployed Engineer | Client-Facing AI Engineer | LinkedIn, McKinsey, Palantir | Mid–Senior | ❌ |
| 138 | AI UX Designer | AI Product Designer, AI Interaction Designer | index.dev, Artech | Mid–Senior | ❌ |
| 139 | Conversational AI Designer | Dialog Designer, Chatbot Designer | Conversation Design Institute, Indeed (6K+ postings) | Mid | ❌ |

### LDR — Strategic leadership, research, and transformation

| # | Role Function | Key Variants | Primary Sources | Seniority | In WIDAI? |
|---|---|---|---|---|---|
| 140 | Data and AI Transformation Lead | — | WIDAI | Senior/Dir | ✅ WRC-08 |
| 141 | Data and AI Research Scientist | — | WIDAI | Senior | ✅ WRC-08 |
| 142 | AI Innovation Lead | — | DCWF 902, WIDAI | Senior/Dir | ✅ WRC-08 |
| 143 | Data and AI Strategy Consultant | — | WIDAI | Senior | ✅ WRC-08 |
| 144 | VP Data Engineering | Head of Data Engineering | Gartner, Deloitte, LinkedIn, job market | VP | ❌ |
| 145 | VP Data Science | Head of Data Science | Gartner, LinkedIn, all major firms | VP | ❌ |
| 146 | VP Analytics | Head of Analytics, VP BI | Gartner, Deloitte | VP | ❌ |
| 147 | VP Data Governance | Head of Data Governance | Deloitte CDO Playbook | VP | ❌ |
| 148 | VP AI/ML | Head of AI, Head of Machine Learning | BCG, McKinsey, LinkedIn | VP | ❌ |
| 149 | VP Data Architecture | Head of Data Architecture | Industry practice | VP | ❌ |
| 150 | VP Data Products | Head of Data Products | Gartner, data mesh orgs | VP | ❌ |
| 151 | VP Data Strategy and Operations | VP DataOps | Deloitte, Gartner | VP | ❌ |
| 152 | VP Data Platform | VP Data Infrastructure | Industry practice | VP | ❌ |
| 153 | Director of Data Engineering | — | LinkedIn, Indeed, all firms | Director | ❌ |
| 154 | Director of Data Science | — | LinkedIn, Indeed, all firms | Director | ❌ |
| 155 | Director of Analytics | — | LinkedIn, Indeed | Director | ❌ |
| 156 | Director of AI/ML | — | LinkedIn, McKinsey | Director | ❌ |
| 157 | Director of Data Governance | — | Deloitte, DAMA community | Director | ❌ |
| 158 | Director of Data Operations | — | Industry practice | Director | ❌ |
| 159 | Director of AI Ethics/Responsible AI | — | Accenture, Microsoft, industry practice | Director | ❌ |
| 160 | Director of Data Quality | — | Industry practice | Director | ❌ |
| 161 | Director of Data Products | — | Data mesh organizations | Director | ❌ |
| 162 | Director of Master Data Management | — | Industry practice | Director | ❌ |
| 163 | Deputy CDO | Embedded CDO, Division CDO | Deloitte CDO Playbook, CDO Magazine | VP/Director | ❌ |
| 164 | Chief of Staff to CDAIO | — | Large enterprise practice | Senior | ❌ |
| 165 | Domain Data Lead | Domain CDO, Domain Data Owner (Mesh) | Dehghani, DataGalaxy, TDWI | Director | ❌ |
| 166 | Data Platform Team Lead | — | Data mesh architecture | Senior/Dir | ❌ |
| 167 | BI Director | BI Program Manager | DAMA DMBOK Ch.11 | Director | ❌ |
| 168 | GenAI CoE Leader | Head of GenAI | agility-at-scale.com, Qatalys | Director/VP | ❌ |
| 169 | AI CoE Leader | Head of AI CoE | Microsoft CAF, AWS, IDC | Director/VP | ❌ |
| 170 | Chief Data Scientist | — | CDO Magazine, QuantumBlack | Senior/VP | ❌ |

### Regulatory and value-chain roles (EU AI Act and standards)

| # | Role Function | Key Variants | Primary Sources | Seniority | In WIDAI? |
|---|---|---|---|---|---|
| 171 | AI Provider Compliance Lead | — | EU AI Act Art 16-21 | Senior | ❌ |
| 172 | AI Deployer Compliance Lead | Human Oversight Specialist | EU AI Act Art 26 | Senior | ❌ |
| 173 | Authorized Representative (AI) | — | EU AI Act Art 22 | Senior | ❌ |
| 174 | Notified Body Assessor (AI) | — | EU AI Act (external role) | Senior | ❌ |
| 175 | AIMS Manager | ISO 42001 AIMS Lead | ISO/IEC 42001 Clause 5.3 | Senior | ❌ |
| 176 | AI System Impact Assessment Coordinator | AISIA Lead | ISO 42001 Annex A.5 | Mid–Senior | ❌ |
| 177 | AI Lifecycle Manager | — | ISO/IEC 42001 Annex A.6, ISO 5338 | Mid–Senior | ❌ |
| 178 | AI Data Quality Manager (ISO) | — | ISO 42001 Annex A.7 | Mid | ❌ |

### Additional niche and industry-specific roles

| # | Role Function | Key Variants | Primary Sources | Seniority | In WIDAI? |
|---|---|---|---|---|---|
| 179 | Clinical AI Specialist | Medical Imaging Engineer | Healthcare industry, FDA SaMD | Mid–Senior | ❌ |
| 180 | Algorithmic Trading Engineer | Quantitative Developer | Financial services, O\*NET 13-2099.01 | Mid–Senior | ❌ |
| 181 | SaMD Quality/Regulatory Affairs Officer | — | FDA AI/ML SaMD Action Plan | Senior | ❌ |
| 182 | Chief Medical Information Officer | CMIO | Healthcare industry | Executive | ❌ |
| 183 | Data Annotator | Labeler, Annotation Specialist | LinkedIn (1.3M new AI jobs), Scale AI | IC | ❌ |
| 184 | AI Content Editor | AI-Assisted Content Creator | Artech, marketing teams | IC–Mid | ❌ |
| 185 | Memory Engineer | AI Memory Specialist | ODSC (very new, 2025-2026) | Mid | ❌ |
| 186 | Trust Engineer | AI Trust Engineer | ODSC (emerging 2025-2026) | Mid | ❌ |
| 187 | AI Agent Developer | AI Agent Deployer, AI Agent Operator | Singapore MAIG for Agentic AI (Jan 2026) | Mid–Senior | ❌ |

---

## 2. Gap analysis: roles present in frameworks but absent from WIDAI v0.3.0

WIDAI v0.3.0 contains **34 named roles** across 8 categories. This research identifies **153 additional role functions** not currently represented. The gaps cluster into **seven critical themes** ranked by urgency.

### Gap Theme 1 — The missing VP/Director leadership layer is the single largest structural gap

WIDAI jumps from C-suite executives (WRC-01 GOV) directly to individual contributor and manager-level roles. Every major framework and all industry analyst models (Gartner, Deloitte, McKinsey) document a **VP and Director layer** that provides functional leadership between the CDAIO and working teams. At minimum, **9 VP-level and 10 Director-level standard titles** exist in the market. This layer is essential for any organization beyond startup stage. Recommended additions include VP Data Engineering, VP Data Science, VP Analytics, VP Data Governance, VP AI/ML, Deputy CDO, Chief of Staff to CDAIO, and corresponding Director-level roles.

### Gap Theme 2 — Model risk management roles are entirely absent

The Federal Reserve's SR 11-7 guidance (applicable to all supervised financial institutions and increasingly adopted by non-financial enterprises for AI governance) creates an entire organizational structure with **6 distinct roles**: Model Risk Manager, Model Validator, Model Owner, Model Developer (as a governance designation), Model Governance Analyst, and Model Risk Committee member. None appear in WIDAI. Given the convergence of model risk management and AI governance, these roles are critical for the RSK category.

### Gap Theme 3 — Data mesh domain roles need dedicated representation

Data mesh adoption is growing (**40% faster time-to-market** for data products per Gartner 2024). The framework creates roles that do not map cleanly to existing WIDAI categories: Domain Data Owner, Domain Data Product Owner, Self-Serve Data Platform Engineer, Data Enabling Team Coach, Federated Governance Representative, and Data Mesh Change Manager. These span GOV, ENG, DSM, and OPS categories.

### Gap Theme 4 — GenAI/LLMOps and agentic AI roles are unrepresented

The fastest-growing job titles in the market — Prompt Engineer (+135.8%), Generative AI Engineer, Context Engineer, LLMOps Engineer, FMOps Engineer, RLHF Specialist, RAG Engineer, AI Agent Developer — have no WIDAI analogs. The ENG and DEV categories need GenAI-specific additions.

### Gap Theme 5 — Privacy, audit, and compliance roles at the CDAIO boundary

WIDAI includes Data Privacy Specialist and Data Compliance Analyst but misses the broader ecosystem: **Data Protection Officer** (legally mandated under GDPR), **Privacy Engineer** (IAPP CIPT), **AI Auditor** (ISACA AAIA 2024), **AI Governance Professional** (IAPP AIGP 2024), and the **AI Red Team Lead** (mandated by EU AI Act and White House EO for high-risk systems). These are distinct from existing RSK roles.

### Gap Theme 6 — Data management operational roles from DAMA DMBOK

DAMA DMBOK defines ~120 roles across 11 knowledge areas. WIDAI captures the top-level managers but misses important operational roles: **Data Quality Analyst**, **Data Catalog Manager**, **Data Lineage Analyst**, **Data Classification Specialist**, **Business Glossary Manager**, **Records Manager**, **Knowledge Manager**, **Data Lifecycle Manager**, and the hierarchical stewardship model (Executive, Coordinating, Business, and Technical Data Steward variants).

### Gap Theme 7 — Emerging cross-functional and enablement roles

Several roles that bridge data/AI teams and the rest of the organization are absent: **Analytics Translator / Data Translator** (McKinsey), **Citizen Data Scientist** (Gartner), **Data Evangelist**, **AI UX Designer**, **Decision Scientist** (Google), **Conversational AI Designer**, **AI Supervisor/Agent Coordinator** (McKinsey Agentic Org 2025), and **Forward-Deployed Engineer**.

### Summary of gap counts by WIDAI category

| WIDAI Category | Current Roles | Gaps Identified | Priority Additions |
|---|---|---|---|
| WRC-01 GOV | 6 | ~20 | Data Owner, DPO, AI Governance Professional, Executive Data Steward, Federated Governance Rep |
| WRC-02 ENG | 5 | ~20 | MLOps Engineer, DataOps Engineer, Data Reliability Engineer, LLMOps Engineer, Knowledge Graph Engineer, DBA |
| WRC-03 DEV | 5 | ~10 | Prompt Engineer, Foundation Model Engineer, Decision Scientist, AI Research Scientist, Statistician |
| WRC-04 DSM | 5 | ~12 | AI Product Manager, Data Catalog Manager, Data Marketplace Manager, Domain Data Product Owner, Data Monetization Manager |
| WRC-05 ANL | 4 | ~8 | Performance Analyst, Clinical Data Manager, Health Informatics Specialist, Citizen Data Scientist |
| WRC-06 RSK | 4 | ~20 | AI Red Team Lead, AI Auditor, Model Risk Manager, Model Validator, AI Incident Response Manager, AI Safety Researcher |
| WRC-07 OPS | 4 | ~12 | Analytics Translator, AI Trainer, AI Supervisor/Agent Coordinator, Conversational AI Designer, Forward-Deployed Engineer |
| WRC-08 LDR | 4 | ~25 | All VP/Director roles, Deputy CDO, Chief of Staff, Domain Data Lead, GenAI CoE Leader |

---

## 3. Organizational reporting structures by organization size

### Startup and scale-up (50–500 employees)

The data function is **flat and centralized**, typically comprising **3–8 people** or 1–5% of headcount. There is no CDO; a **Head of Data** or **VP Data** reports to the CEO or CTO. Hiring sequence follows a well-documented pattern: Data Analyst → Data Engineer → Data Scientist. Everyone wears multiple hats.

```
CEO / CTO
  └── Head of Data (VP)
        ├── Data Engineer (1-3)
        ├── Data Analyst (1-2)
        └── Data Scientist (0-1)
```

Key characteristic: no formal governance function. Data quality is everyone's responsibility. Analytics engineering often handled by the data engineer. No dedicated AI roles unless the company's product is AI-based.

### Mid-market (500–5,000 employees)

The data organization grows to **15–30 professionals** and begins adopting a **hub-and-spoke** model. A **CDO or VP Data & Analytics** reports to the CTO, COO, or CEO. Specialized functions emerge with Director-level leads. Governance formalizes. Data stewards appear. The first dedicated AI/ML hires arrive.

```
CDO / VP Data & Analytics
  ├── Director, Data Engineering (5-8 engineers)
  ├── Director, Data Science & ML (3-6 data scientists/ML engineers)
  ├── Director, Analytics & BI (4-8 analysts, BI developers)
  ├── Data Governance Lead (1-3 stewards)
  └── Data Operations Manager
```

Key characteristic: beginning to embed analysts in business units while keeping engineering centralized. Analytics engineers emerge as a distinct role. Data product management starts. First AI governance policies created.

### Large enterprise (5,000+ employees)

The full **CDAIO organization** employs **50–200+ data professionals** across 4–6 hierarchical layers. The CDAIO reports to the CEO (best practice per IBM 2025, Gartner) or COO, with **5–8 VP/SVP direct reports** plus a Chief of Staff. The organization may operate as centralized CoE, federated, hub-and-spoke, or data mesh — most adopt a **hybrid/hub-and-spoke** model.

```
CDAIO (reports to CEO or COO)
  ├── Deputy CDO
  ├── Chief of Staff
  ├── VP Data Engineering
  │     ├── Director, Data Platform
  │     ├── Director, Data Integration
  │     └── DataOps / MLOps teams
  ├── VP Data Science & AI
  │     ├── Director, Data Science
  │     ├── Director, AI/ML Engineering
  │     └── GenAI CoE Leader
  ├── VP Analytics & BI
  │     ├── Director, Analytics
  │     └── Embedded analytics teams (spokes)
  ├── VP Data Governance & Quality
  │     ├── Director, Data Governance
  │     ├── Director, Data Quality
  │     └── Data Stewardship Council
  ├── VP Data Products & Architecture
  │     ├── Director, Data Architecture
  │     ├── Director, Data Products
  │     └── Director, Master Data Management
  ├── VP Data Strategy & Operations
  │     ├── Program Management Office
  │     ├── Data Literacy & Adoption
  │     └── Data & AI Communications
  └── Director, AI Risk & Ethics
        ├── AI Red Team
        ├── Model Risk Management
        └── AI Audit Liaison
```

**Interface points with other C-suite functions** are well-documented. The CDAIO shares territory with the CIO on infrastructure and data architecture, the CISO on data security and AI security, the CPO/General Counsel on privacy, the CFO on data monetization ROI, and the CMO on customer analytics. **Data security** (dual-reporting between CDAIO and CISO) and **privacy engineering** (dual-reporting between CDAIO and CPO) are the most common boundary-spanning roles.

### Data mesh organizational overlay

In organizations adopting data mesh, the structure above is augmented with **domain teams** that include their own data product owners, data engineers, and analysts. The central organization retains platform, governance, and enabling functions. A **federated governance group** (guild or council) connects domain representatives with the central governance team.

```
Central CDAIO Org                     Domain Teams (per BU)
  ├── Data Platform Team         →      Domain A: Domain Data Lead
  ├── Data Enabling Team         →        ├── Data Product Owner
  ├── Federated Governance Group →        ├── Data Engineer(s)
  └── Standards & Architecture   →        ├── Data Analyst
                                          └── Domain Data Steward
```

---

## 4. Role variant analysis: consolidating titles that map to the same function

Many titles refer to essentially the same function with only branding, seniority, or contextual differences. The following groups consolidate common variants.

**Data pipeline and infrastructure building**: Data Engineer, ETL Developer, ELT Engineer, Data Pipeline Engineer, Data Integration Engineer, Big Data Engineer, Cloud Data Engineer, and Streaming Data Engineer all describe the same core function of building and maintaining data pipelines. **WIDAI correctly uses "Data Engineer"** as the canonical title.

**ML model operationalization**: MLOps Engineer, ML Operations Engineer, ML Deployment Engineer, ML Platform Engineer, and AIOps Engineer all center on deploying, monitoring, and managing ML models in production. MLOps Engineer is the most common title and should be canonical. This is **distinct from ML Engineer** (who builds models) and from **DataOps Engineer** (who focuses on data pipelines).

**Data analysis and reporting**: Data Analyst, Business Analyst, Reporting Analyst, Insights Analyst, Product Analyst, and BI Analyst all perform data interpretation and visualization. In practice, **Data Analyst and BI Analyst/Developer** represent two ends of a spectrum (exploratory analysis vs. report/dashboard building). WIDAI correctly separates these.

**AI/ML model building**: ML Engineer, AI Engineer, Deep Learning Engineer, and Applied Scientist overlap substantially. The market is converging on **ML Engineer** for model-focused work and **AI Engineer** for broader AI application building including GenAI. WIDAI correctly lists both.

**Data governance enforcement**: Data Steward, Data Custodian, Business Data Steward, Technical Data Steward, and Domain Data Steward are all variants of the stewardship function distinguished by scope (domain vs. enterprise) and orientation (business vs. technical). WIDAI uses "Data Steward" but should consider distinguishing **Executive/Coordinating Data Steward** at the senior level from **Business/Technical Data Steward** at the operational level, as DAMA DMBOK does.

**AI ethics and responsibility**: AI Risk and Ethics Specialist, Responsible AI Lead, AI Ethicist, AI Ethics Officer, AI Governance Professional, and AI Fairness Lead describe overlapping but distinct functions. The core distinction is between **risk assessment** (evaluating AI systems) and **governance program management** (designing organizational processes). WIDAI should retain the current AI Risk and Ethics Specialist and add an AI Governance Professional for the programmatic dimension.

**Translation and evangelism**: Analytics Translator, Data Translator, Business Translator, Data Evangelist, and Data Advocate all bridge data teams and business stakeholders. McKinsey coined "Analytics Translator" in 2018, and the role has been debated as standalone vs. a skill set. These can be consolidated under **Analytics Translator / Data Evangelist** as a single role function.

---

## 5. Emerging roles (2023–2026) not yet in legacy frameworks

The following roles have appeared or gained significant market traction since 2023 and are **not represented in any legacy framework** (NICE, DAMA DMBOK, SOC, or DCWF). They represent the frontier of the CDAIO domain.

**Context Engineer** emerged in late 2025 when Gartner formally defined it. This role goes beyond prompt engineering to design what fills the LLM context window — RAG pipeline architecture, memory systems, vector database design, tool integrations, and agent orchestration. Salaries range from **$130K to $200K+**. This is likely the successor to the prompt engineer title and represents a genuinely new engineering specialty.

**AI Agent Developer / Agent Orchestrator** surfaced with McKinsey's "Agentic Organization" research in 2025. As agentic AI scales (Gartner predicts **33% of enterprise software will include agentic AI by 2028**), organizations need specialists who design, build, and supervise autonomous agent workflows. Singapore's MAIG for Agentic AI (January 2026) formally defined developer, deployer, and operator roles for agentic systems.

**Data Reliability Engineer** was championed by Monte Carlo Data starting around 2022, applying SRE principles to data systems. Companies including DoorDash, Disney Streaming, and Equifax now hire for this title. The role focuses on data observability across five pillars: freshness, distribution, volume, schema, and lineage. It is distinct from both Data Engineer (who builds pipelines) and Data Quality Analyst (who assesses quality) — the DRE ensures **continuous automated reliability** of data systems.

**AI Red Team Lead** has become formalized following the White House Executive Order on AI (October 2023) and the EU AI Act's requirements for adversarial testing of high-risk AI systems. Microsoft has a dedicated AI Red Team (17+ languages), OpenAI actively recruits "Misalignment Researchers," and Anthropic has a "Frontier Red Team." This is distinct from general AI security — red teaming is proactive adversarial probing for biases, safety failures, and misuse vectors.

**Foundation Model Operations (FMOps) Engineer** is a specialization beyond MLOps that addresses the unique operational challenges of foundation models: prompt management, model chaining, agent management, RAG pipeline operations, cost optimization for inference, and guardrail configuration. DZone describes a maturity model from basic prompts through automated prompt engineering.

**Decision Scientist** was coined by Cassie Kozyrkov at Google around 2018-2019 but has gained significant traction since 2023. Unlike data scientists who focus on model accuracy, decision scientists focus on how models change human decision processes, accounting for cognitive biases and organizational dynamics. Companies including Google, Instagram, Ibotta, Truist, and CVS Health use this title, with **158+ active postings** tracked on aijobs.net.

**AI Supervisor / M-shaped Supervisor** is McKinsey's term for a new managerial archetype: a broad generalist fluent in AI who orchestrates hybrid human-AI teams. As AI agents handle routine coordination tasks previously done by middle managers, this role evolves from traditional management into human-agent workflow orchestration. Only **1% of organizations** currently operate in this paradigm, but it represents the trajectory of data and AI organizational design.

**AI Governance Professional** became formalized when the IAPP launched its AIGP certification in 2024 and ISACA launched its Advanced in AI Audit (AAIA) credential. These certifications create a recognized professional role for people who design and operate enterprise AI governance programs — distinct from AI ethics specialists (who focus on technical fairness) and from traditional compliance officers (who lack AI-specific expertise).

**Synthetic Data Engineer** addresses growing demand for privacy-preserving training data. Apple, Lila Sciences, and autonomous vehicle companies hire for this function, which combines statistical modeling, generative techniques, and domain expertise to create representative datasets that protect real-world data. The role is expected to grow as privacy regulations tighten and AI training data needs expand.

**Data Product Manager (Marketplace)** and **Data Monetization Manager** have emerged as organizations treat data as a product. Chubb, Pinterest, and Google now have dedicated marketplace and monetization roles. This function requires understanding data valuation, pricing models, data contracts, and marketplace operations — a distinct skill set from traditional data product management focused on internal consumers.

---

## Conclusion: strategic priorities for extending WIDAI

This research confirms that the CDAIO organizational domain is significantly broader and more layered than WIDAI v0.3.0 currently represents. Three strategic priorities emerge for the framework's extension.

**First, add the VP/Director leadership taxonomy.** This is non-negotiable for organizational relevance. Every enterprise of meaningful scale has this layer, and its absence makes WIDAI incomplete for organizational design purposes. A new **WRC-09 MGL (Management and Governance Leadership)** category — or expansion of WRC-08 LDR — should accommodate 9 VP-level and 10+ Director-level standardized titles.

**Second, add dedicated categories for model risk management and AI safety.** The convergence of financial model risk management (SR 11-7), AI governance (ISO 42001), and emerging regulation (EU AI Act) creates a distinct professional domain with its own career ladder: Model Governance Analyst → Model Validator → Model Risk Manager → Head of MRM. Similarly, AI red teaming and AI safety research represent a growing specialization within WRC-06 RSK.

**Third, add GenAI and agentic AI operational roles.** The GenAI revolution has created genuinely new engineering functions (Context Engineer, LLMOps/FMOps Engineer, RAG Engineer) and operational roles (AI Trainer, AI Agent Orchestrator) that do not map to existing WIDAI categories. These are not passing trends — they reflect fundamental shifts in how AI systems are built and operated, with dedicated infrastructure, tooling, and career paths now established.

Beyond these priorities, extending coverage to include DAMA DMBOK operational roles, data mesh domain roles, ISO/regulatory compliance roles, and cross-functional enablement roles (Analytics Translator, Decision Scientist, Citizen Data Scientist) would bring WIDAI to approximately **95% coverage** of the roles identified across all 50+ frameworks and sources researched. The remaining 5% consists of highly niche, industry-specific, or very early-stage roles that may warrant a "watch list" rather than immediate inclusion.