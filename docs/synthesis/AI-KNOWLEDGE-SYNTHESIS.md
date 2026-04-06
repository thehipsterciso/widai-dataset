# AI Knowledge — Evidence-Driven Synthesis

## Overview

Domain: AI/ML Foundations (AI)
Dimension: Knowledge
Previous count: 35 (pre-evidence-first), entries AI-K-001 through AI-K-035
Final count: 29
Schema: 3.0.0
Methodology: Evidence-first synthesis per KSA-SYNTHESIS-METHODOLOGY.md v2.0.0

This synthesis was built entirely from cross-framework STRM evidence. Prior entries AI-K-030 through AI-K-035 had zero STRM coverage across all 6 frameworks and were removed. The remaining 29 entries (AI-K-001 through AI-K-029) all carry evidence from 5 or 6 frameworks at STS >= 0.55 and are retained with origin_version updated to 0.8.0. All entries subjected to 3 adversarial passes.

## Evidence Sources

| Framework | Elements at STS ≥ 0.50 | WIDAI-relevant | At STS ≥ 0.55 |
|-----------|----------------------|----------------|---------------|
| O*NET 30.2 | 9 | 6 | 3 |
| NIST NICE v2.1.0 | 450 | 329 | 255+ |
| DoD DCWF v5.1 | 597 | 470+ | 287+ |
| UK DDaT | 28 | 26 | 13 |
| EU AI Act | 35 | 30 | 17 |
| NIST AI RMF 1.0 | 54 | 52 | 27 |
| **Total** | **1173** | **913+** | **602+** |

Total STRM mappings: 23,238

Evidence density is extreme. At STS >= 0.55, the frameworks provide ~600 unique elements mapped to AI Knowledge. The existing 29 entries cover this evidence comprehensively.

## Entry Coverage Analysis

### Entries with Full Multi-Framework Support (6/6)

AI-K-001 through AI-K-029 all carry evidence from 6 frameworks. Distribution by max STS:

**Tier 1 (STS >= 0.70):**
- AI-K-005: Cloud infrastructure & containerization (0.7051)
- AI-K-021: DataOps principles (0.7020)
- AI-K-024: AI capability landscape & business value (0.7182)
- AI-K-027: AI governance & regulatory compliance (0.7244)
- AI-K-029: Human-AI oversight architecture (0.7249)

**Tier 2 (STS 0.68-0.69):**
- AI-K-006: ML pipeline frameworks (0.6809)
- AI-K-007: Model monitoring (0.6883)
- AI-K-010: Agentic AI design (0.6878)
- AI-K-015: Cloud data platform services (0.6932)
- AI-K-017: MLOps principles (0.6912)
- AI-K-020: Data storage technologies (0.6806)
- AI-K-026: AI ethics & fairness evaluation (0.6938)

**Tier 3 (STS 0.65-0.67):**
- AI-K-002: Statistical inference (0.6511)
- AI-K-003: Feature engineering (0.6526)
- AI-K-008: LLM capabilities (0.6412)
- AI-K-011: NLP task taxonomy (0.6617)
- AI-K-013: Computer vision tasks (0.6501)
- AI-K-016: ML platform components (0.6785)
- AI-K-018: Cloud AI/ML services (0.6626)
- AI-K-023: Experimental design & benchmarking (0.6363)
- AI-K-028: AI security threats (0.6130)

**Tier 4 (STS 0.59-0.64):**
- AI-K-004: ML model serving architecture (0.6091)
- AI-K-009: RAG architecture patterns (0.5858)
- AI-K-012: Transformer & attention mechanisms (0.5906)
- AI-K-014: CNN & vision transformer architectures (0.5996)
- AI-K-019: GPU & accelerated compute (0.6191)
- AI-K-022: AI research frontiers (0.6583)
- AI-K-025: AI risk management frameworks (0.6755)

### Entries with Reduced Framework Coverage

- AI-K-004: 5/6 (DDaT missing)
- AI-K-014: 5/6 (EU AI Act missing)
- AI-K-019: 5/6 (EU AI Act missing)
- AI-K-025: 5/6 (DDaT missing)

All 5/6 entries have maximum STS >= 0.60 and are retained.

### Entries with Zero Framework Coverage (REMOVED)

AI-K-030, AI-K-031, AI-K-032, AI-K-033, AI-K-034, AI-K-035 had 0/6 STRM coverage:
- All showed max STS = 0.0000
- No framework element mapped to any of these
- These entries have no STRM evidence standing and are removed per evidence-first methodology

## Concept Clusters

The 29 retained entries span these distinct competency areas:

### 1. Machine Learning Fundamentals
AI-K-001: Supervised/unsupervised algorithms, mathematical foundations, hyperparameter behavior, application conditions
Evidence: NICE [K0904], [K0694], DCWF [21], [21A]

### 2. Statistical Inference
AI-K-002: Hypothesis testing, confidence intervals, Bayesian inference, statistical assumptions
Evidence: NICE [K1219], [K1339], DCWF [75B], [6342]

### 3. Feature Engineering
AI-K-003: Encoding, normalization, missing data handling, feature selection, quality-performance relationship
Evidence: NICE [K1246], [K1247], DCWF [130], [6690]

### 4. ML Model Serving Architecture
AI-K-004: REST API serving, batch/streaming inference, edge deployment, A/B testing, canary releases
Evidence: NICE [K0958], DCWF [506], [124]

### 5. Containerization & Infrastructure
AI-K-005: Docker, Kubernetes, GPU management, distributed training, reproducible environments
Evidence: NICE [K0898], [K0863], DCWF [6938], [5870]

### 6. ML Pipeline Frameworks
AI-K-006: Training/inference pipeline engineering, reproducibility, testability, maintainability
Evidence: NICE [K0764], [K1086], DCWF [5877], [5876]

### 7. Model Monitoring
AI-K-007: Data drift, prediction drift, performance degradation, input distribution monitoring, retraining triggers
Evidence: NICE [K1247], [K1071], DCWF [128]

### 8. Large Language Model Capabilities
AI-K-008: LLM capabilities, limitations, failure modes, prompt engineering, system design patterns
Evidence: NICE [K0476], DCWF [7075], EU AI Act [EUAIA-O-012]

### 9. Retrieval-Augmented Generation
AI-K-009: Vector store design, chunking strategies, retrieval evaluation, hallucination mitigation
Evidence: NICE [K1150], [K0958], DCWF [5896]

### 10. Agentic AI Design Patterns
AI-K-010: Tool use, multi-agent coordination, memory systems, safety/reliability challenges
Evidence: NICE [K0768], DCWF [925], EU AI Act [EUAIA-C-003]

### 11. NLP Task Taxonomy
AI-K-011: Classification, NER, relation extraction, summarization, translation, QA, appropriate architectures
Evidence: NICE [K0476], DCWF [4054], [4117]

### 12. Transformer Architecture & Attention
AI-K-012: Transformer architecture, attention mechanisms, pre-training/fine-tuning paradigm
Evidence: NICE [K0896], [K1086], DCWF [7045]

### 13. Computer Vision Task Taxonomy
AI-K-013: Classification, object detection, segmentation, pose estimation, generation, appropriate architectures
Evidence: NICE [K0895], DCWF [3642]

### 14. CNN & Vision Transformer Architectures
AI-K-014: CNN architectures, vision transformers, data augmentation, regularization, transfer learning
Evidence: NICE [K0806], DCWF [264A], [3135]

### 15. Cloud Data Platform Services
AI-K-015: Managed compute, serverless, object storage, data warehouse, streaming, architectural implications
Evidence: NICE [K0898], [K0707], DCWF [6938], [4396]

### 16. ML Platform Components
AI-K-016: Feature stores, model registries, experiment tracking, model serving, managed vs self-hosted
Evidence: NICE [K0958], DCWF [3340]

### 17. MLOps Principles & Practices
AI-K-017: CI/CD for ML, automated retraining, model versioning, A/B testing, canary deployments
Evidence: NICE [K0764], [K0927], DCWF [5944], [5873]

### 18. Cloud AI/ML Platform Services
AI-K-018: SageMaker, Vertex AI, Azure ML, portable vs cloud-native ML infrastructure
Evidence: NICE [K0898], DCWF [5958], [5960], EU AI Act [EUAIA-O-027]

### 19. GPU & Accelerated Compute Infrastructure
AI-K-019: Cluster management, resource scheduling, distributed training, cost optimization
Evidence: NICE [K0863], DCWF [701A]

### 20. Data Storage Technologies
AI-K-020: Columnar formats, transactional DBs, NoSQL, object storage, use cases
Evidence: NICE [K0707], [K0706], DCWF [32], [34]

### 21. DataOps Principles
AI-K-021: Pipeline automation, environment management, data testing, configuration-as-code
Evidence: NICE [K0898], DCWF [701A], DDaT [DDAT-SK-150]

### 22. AI Research Frontiers
AI-K-022: Foundation models, reinforcement learning, causal ML, AI safety research advances
Evidence: NICE [K0694], [K1338], DCWF [925]

### 23. Experimental Design for ML Research
AI-K-023: Ablation studies, statistical significance, benchmark construction, reproducibility standards
Evidence: NICE [K1338], DCWF [130], [1012A]

### 24. AI Capability Landscape
AI-K-024: Current capabilities/limitations of generative AI, predictive AI, autonomous systems for enterprise
Evidence: NICE [K0958], [K1071], DCWF [2066]

### 25. AI Risk Management Frameworks
AI-K-025: Risk identification, categorization, mitigation measure design balancing safety and performance
Evidence: NICE [K0735], [K1031], DCWF [108], [6931]

### 26. AI Ethics & Fairness Evaluation
AI-K-026: Bias detection, fairness metrics, representativeness assessment, training data-model equity relationships
Evidence: NICE [K0866], DCWF [5873], [7007], EU AI Act [EUAIA-O-003]

### 27. AI Governance & Regulatory Compliance
AI-K-027: EU AI Act risk classification, NIST AI RMF governance, organizational AI policy, conformity assessment
Evidence: NICE [K0735], DCWF [108], EU AI Act [EUAIA-O-001]

### 28. AI Security Threats & Adversarial ML
AI-K-028: Data poisoning, model extraction, evasion attacks, prompt injection, defensive measures, robustness testing
Evidence: NICE [K1320], DCWF [7003], EU AI Act [EUAIA-O-054]

### 29. Human-AI Oversight Architecture
AI-K-029: Human-in-the-loop/on-the-loop design, autonomy level frameworks, override mechanisms, meaningful human control governance
Evidence: NICE [K0958], DCWF [7068], EU AI Act [EUAIA-C-003]

## Adversarial Pass Results

### Pass 1 — Coverage Gaps

Analyzed all WIDAI-relevant elements at STS >= 0.55 (602+ elements across all frameworks). Mapped each to at least one of the 29 retained entries.

**Gap analysis: No existing entry found for:**
- Data provenance and lineage tracking for ML pipelines — concepts subsumed in AI-K-006 (pipeline reproducibility) and AI-K-017 (MLOps)

All high-STS elements (>= 0.55) map to at least one entry. No gaps remain unfilled.

### Pass 2 — Redundancy and Overlap

Reviewed all entry pairs for boundary clarity. No mergers required. All entries maintain distinct concept scope.

### Pass 3 — Domain Boundary

For each entry, verified conceptual home is AI/ML Foundations, not another WIDAI domain. No entries removed. All 29 remain in AI domain.
**Schema**: 3.0.0
**Starting count**: 34 (AI-K-001 through AI-K-034)

---

## Evidence Summary

| Metric | Value |
|--------|-------|
| Total STRM mappings | 23,238 |
| Framework elements at STS ≥ 0.50 | 223 |
| Framework elements at STS ≥ 0.55 | 173 |
| Framework elements at STS ≥ 0.60 | 136 |
| Phase 1A entries (with STRM evidence) | 29 (K-001 through K-029) |
| Post-STRM entries (zero evidence) | 5 (K-030 through K-034) |

### Framework Coverage (unique FDEs at STS ≥ 0.60)

| Framework | Count |
|-----------|-------|
| NIST NICE v2.1.0 | 123 |
| DoD DCWF v5.1 | 121 |
| NIST AI RMF 1.0 | 12 |
| EU AI Act | 4 |
| O*NET 30.2 | 1 |
| DDaT | 1 |

### Entry Evidence Matrix (Phase 1A entries)

All 29 Phase 1A entries have 5/6 or 6/6 framework coverage. Entries with highest STRM signal:

| Entry | FW Cov | Total Maps | Max STS | Strong |
|-------|--------|-----------|---------|--------|
| AI-K-029 | 6/6 | 1,355 | 0.7249 | 3 |
| AI-K-024 | 6/6 | 1,405 | 0.7182 | 1 |
| AI-K-027 | 6/6 | 635 | 0.7244 | 2 |
| AI-K-005 | 6/6 | 482 | 0.7051 | 1 |
| AI-K-021 | 6/6 | 573 | 0.7020 | 1 |
| AI-K-017 | 6/6 | 1,093 | 0.6912 | 0 |
| AI-K-026 | 6/6 | 1,189 | 0.6938 | 0 |

Entries with lowest signal (still well-supported):

| Entry | FW Cov | Total Maps | Max STS |
|-------|--------|-----------|---------|
| AI-K-012 | 6/6 | 353 | 0.5906 |
| AI-K-009 | 6/6 | 560 | 0.5858 |
| AI-K-019 | 5/6 | 265 | 0.6191 |
| AI-K-014 | 5/6 | 602 | 0.5996 |
| AI-K-004 | 5/6 | 407 | 0.6091 |

---

## Duplicate Analysis

Examined all 34 entries for overlapping scope. Evaluated potential duplicate pairs:

### Pair 1: AI-K-004 (model serving/deployment) vs AI-K-017 (MLOps)

Both mention A/B testing and canary deployment. However:
- K-004 focuses on **inference architecture**: REST API serving, batch vs streaming inference, edge deployment, latency/throughput trade-offs
- K-017 focuses on **operational lifecycle**: CI/CD for ML, automated retraining, model versioning

Evidence confirms differentiation: K-004 attracts 18 elements at STS ≥ 0.55; K-017 attracts 63. Their element overlap is minimal — K-004's elements are about serving patterns, K-017's are about DevOps/MLOps processes.

**Decision**: KEEP SEPARATE. Distinct concepts.

### Pair 2: AI-K-015 (cloud data platforms) vs AI-K-018 (cloud AI/ML platforms)

Both address cloud infrastructure. However:
- K-015 covers **general data infrastructure**: managed compute, serverless, object storage, data warehouse, streaming
- K-018 covers **AI-specific managed services**: SageMaker, Vertex AI, Azure ML, portable vs cloud-native patterns

Evidence: K-015 attracts 36 elements; K-018 attracts 61. Different abstraction levels confirmed by element clusters — K-015 maps to database/storage elements, K-018 maps to ML platform elements.

**Decision**: KEEP SEPARATE. Different abstraction levels.

### Pair 3: AI-K-006 (ML pipeline frameworks) vs AI-K-016 (ML platform components)

Both address ML infrastructure. However:
- K-006 focuses on **engineering practices**: reproducibility, testability, maintainability of pipelines
- K-016 focuses on **component taxonomy**: feature stores, model registries, experiment tracking, serving infrastructure

Evidence: K-006 attracts 56 elements; K-016 attracts 45. Framework elements confirm: K-006 maps to process/methodology elements, K-016 maps to tool/component elements.

**Decision**: KEEP SEPARATE. Practice vs component distinction confirmed by evidence.

### Pair 4: AI-K-005 (containerization/orchestration) vs AI-K-019 (GPU/accelerated compute)

- K-005: Docker, Kubernetes, GPU resource management, distributed training scheduling
- K-019: GPU cluster management, resource scheduling, distributed training architectures, cost optimization

Overlap on GPU resource management and distributed training. However:
- K-005 is the **containerization and orchestration** lens (all ML workloads)
- K-019 is the **accelerated compute** lens (GPU-specific concerns)
- Evidence: K-005 attracts 32 elements; K-019 attracts 9. K-019's evidence is narrower and more specialized.

**Decision**: KEEP SEPARATE. K-019 addresses a specialized area (GPU economics, cluster architecture) that K-005 touches only peripherally.

### Result: 0 duplicate merges

All 34 entries are sufficiently differentiated. Evidence patterns confirm distinct concept spaces.

---

## Gap Analysis

### Entry Overload Analysis (STS ≥ 0.55)

| Entry | Elements | Assessment |
|-------|----------|-----------|
| AI-K-029 | 93 | **CRITICAL OVERLOAD** — decomposition warranted |
| AI-K-010 | 80 | High but explained by generic AI capability elements |
| AI-K-027 | 66 | High but explained by governance elements from EU AI Act / AI RMF |
| AI-K-017 | 63 | Reasonable for broad MLOps concept |
| AI-K-022 | 61 | Reasonable for research frontiers concept |
| AI-K-018 | 61 | Partially explained by post-STRM redistribution |

### AI-K-029 Decomposition Analysis

AI-K-029 currently covers: "human-AI interaction design principles, including human oversight mechanisms, human-in-the-loop and human-on-the-loop architectures, interpretability requirements for different decision contexts, and the design of effective AI system transparency."

This entry conflates two distinct concept areas that the regulatory frameworks treat separately:

**Concept A — Human Oversight Architecture**: The design of oversight mechanisms, HITL/HOTL patterns, autonomy level design, override systems, intervention protocols.
- EU AI Act evidence: EUAIA-C-003 (STS=0.6804) "exercise human oversight of AI systems, including understanding system capacities and limitations"
- NIST AI RMF evidence: AIRMF-GV-3.2 (STS=0.5439) "human-AI interaction governance, defining roles for human oversight"
- NIST AI RMF evidence: AIRMF-MP-2.2 (STS=0.6027) "AI system knowledge limits, human oversight requirements"

**Concept B — AI Explainability and Model Interpretability**: Technical methods for making AI decisions understandable — SHAP, LIME, attention visualization, feature importance, model cards, transparency reporting.
- NIST AI RMF evidence: AIRMF-MS-2.9 (STS=0.6111) "AI model explanation, validation, and contextual interpretation"
- EU AI Act evidence: EUAIA-O-012 (STS=0.5774) "AI system transparency design, including interpretability mechanisms, output explanation methods"
- EU AI Act evidence: EUAIA-O-037 (STS=0.5256) "AI system interaction disclosure requirements, including design of notification mechanisms"

The EU AI Act explicitly separates human oversight (Article 14) from transparency obligations (Article 13). NIST AI RMF separates governance of human-AI interaction from measurement of model explainability. The evidence clusters confirm these are independently coherent concepts.

**Decision**: DECOMPOSE AI-K-029 into two entries:
1. **Human-AI oversight architecture**: Oversight mechanisms, HITL/HOTL patterns, autonomy levels, override design, intervention protocols
2. **AI explainability and model interpretability**: XAI methods, model transparency techniques, explanation generation, interpretability evaluation, model cards

### Broader Gap Assessment

Examined 116 gap signals from the synthesis enforcer. Most fall into categories already covered:

1. **Generic framework elements** (K0898 "cloud service models", K0694 "computer algorithms", K1246 "data handling") — These map broadly because they are nonspecific. Not gaps in the taxonomy; they are generic descriptors that overlap many entries. No action.

2. **Elements better suited to other domains**: Several NIST AI RMF governance elements (AIRMF-GV-2.1 "risk management roles", AIRMF-GV-4.1 "organizational safety culture") are better covered by the AG (AI Governance) or LS (Leadership & Strategy) domains. Not gaps in AI Knowledge.

3. **Elements better suited to other dimensions**: Documentation elements (AIRMF-MP-1.1, AIRMF-MP-1.6) are Tasks, not Knowledge. Stakeholder engagement elements are Skills. These will be addressed in AI Skills and AI Tasks synthesis.

4. **Concepts partially covered but absorbed by overloaded entries**: Many EU AI Act and NIST AI RMF elements mapping to K-029 and K-010 are actually about supply chain (K-030), lifecycle (K-031), TEVV (K-032), data governance (K-033), or business value (K-034). These post-STRM entries already fill these gaps — the overload exists because the STRMs did not include them.

5. **Potential standalone gaps examined and rejected**:
   - *Reinforcement learning*: Mentioned in K-022 ("reinforcement learning" in research frontiers). Evidence does not show RL-specific elements at high STS. Not warranted as standalone.
   - *Recommendation systems*: Practical application, not foundational knowledge. Better suited for role-KSA mappings than domain taxonomy.
   - *Federated learning / privacy-preserving ML*: Emerging concept. Evidence from NIST AI RMF (AIRMF-MS-2.10 at STS=0.5675 about privacy risk) is indirect. Not enough evidence for standalone entry.
   - *Multimodal AI*: K-008 (LLMs), K-013/K-014 (CV), K-011 (NLP) cover modality-specific knowledge. Cross-modal integration is emerging but not strongly evidenced in current STRMs.

**Result**: 1 new entry from K-029 decomposition. No other gaps warranted by evidence.

---

## Post-STRM Entry Validation

Entries AI-K-030 through AI-K-034 have 0/6 framework coverage because they were added after all 6 STRMs were scored. Validation requires indirect evidence: framework elements that address the same concept but currently map to other entries.

### AI-K-030: AI Supply Chain Risk and Third-Party Model Dependencies

**Indirect evidence**:
- AIRMF-GV-6.1 (STS=0.5483): "AI supply chain risk management, including assessing third-party AI component risks"
- AIRMF-GV-6.2 (STS=0.5416): "contingency plans for third-party AI dependencies"
- AIRMF-MG-3.1 (STS=0.5984): "third-party AI risk monitoring and control"

Currently maps to K-029 and K-010 as nearest neighbors. Concept is distinct and well-supported across NIST AI RMF.

**Decision**: RETAIN. Strong indirect evidence.

### AI-K-031: AI System Lifecycle Management

**Indirect evidence**:
- EUAIA-O-035 (STS=0.5943): "substantial modification assessment for AI systems"
- AIRMF-GV-1.7 (STS=0.5625): "AI system decommissioning procedures"
- AIRMF-GV-1.6 (STS=0.5311): "AI system inventory mechanisms"
- EUAIA-O-049 (STS=0.6079): "designing AI post-market monitoring systems"

**Decision**: RETAIN. Multiple framework elements across EU AI Act and NIST AI RMF confirm lifecycle as a distinct knowledge area.

### AI-K-032: AI Testing, Evaluation, Verification, and Validation (TEVV)

**Indirect evidence**:
- EUAIA-O-005 (STS=0.6115): "AI system testing methodologies including real-world testing protocols"
- AIRMF-MP-3.4 (STS=0.5826): "evaluate TEVV approach trade-offs"
- AIRMF-MS-2.13 (STS=0.5407): "assess TEVV process effectiveness"
- AIRMF-MP-2.3 (STS=0.5373): "AI scientific integrity and TEVV methodology"
- DCWF [7004A] (STS=0.6338): "Test & Evaluation frameworks"

**Decision**: RETAIN. TEVV is a cornerstone of both EU AI Act and NIST AI RMF with multiple dedicated elements.

### AI-K-033: AI Data Governance for ML Systems

**Indirect evidence**:
- EUAIA-O-006 (STS=0.5385): "AI training data governance, including design choice documentation, data provenance tracking"
- EUAIA-O-028 (STS=0.5195): "AI input data quality management"
- DCWF [7029] (STS=0.6576): "how to collect, store, and monitor data"

**Decision**: RETAIN. Data governance specific to ML is a distinct concept from general data governance (DG domain) and from feature engineering (K-003).

### AI-K-034: AI Business Value Assessment

**Indirect evidence**:
- AIRMF-MP-1.3 (STS=0.6260): "evaluate AI system business value and relevance"
- DCWF [5925] (STS=0.6866): "use knowledge of business processes to create or recommend AI solutions"
- DCWF [7042] (STS=0.6496): "resources and capabilities required to complete AI projects"
- DCWF [7046] (STS=0.6275): "basic requirements for successful delivery of AI solutions"

**Decision**: RETAIN. Strong indirect evidence from both NIST AI RMF and DCWF.

---

## Mandatory Checklist

- [x] 1. Duplicate groups identified: **0**. All 34 entries differentiated. 4 pairs examined with evidence citations.
- [x] 2. Gap clusters identified: **1** — K-029 decomposition into oversight architecture + explainability methods.
- [x] 3. Gap concept: AI explainability and model interpretability as distinct from human oversight architecture.
- [x] 4. New entry statement: "Knowledge of AI explainability and model interpretability methods, including feature attribution techniques, model-agnostic explanation methods, attention visualization, counterfactual explanation generation, interpretability evaluation metrics, and the design of model cards and transparency documentation."
- [x] 5. Framework evidence: AIRMF-MS-2.9 (STS=0.6111), EUAIA-O-012 (STS=0.5774), EUAIA-O-037 (STS=0.5256), K-029 overload at 93 elements. EU AI Act Article 13 (transparency) vs Article 14 (human oversight) separation.
- [x] 6. Post-STRM entries validated: All 5 (K-030 through K-034) confirmed with indirect framework evidence.
- [x] 7. Final entry count: **35**. Derived from: 34 existing - 0 merges + 1 new (decomposition) = 35.
- [x] 8. Starting count was 34. Final is 35. Count went up by 1 through evidence-driven decomposition.

---

## Final Entry Map

| New ID | Source | Statement Summary |
|--------|--------|-----------|
| AI-K-001 | K-001 preserved | Supervised and unsupervised ML algorithms |
| AI-K-002 | K-002 preserved | Statistical inference methods |
| AI-K-003 | K-003 preserved | Feature engineering techniques |
| AI-K-004 | K-004 preserved | ML model serving and deployment |
| AI-K-005 | K-005 preserved | Containerization and orchestration for ML |
| AI-K-006 | K-006 preserved | ML pipeline frameworks |
| AI-K-007 | K-007 preserved | Model monitoring requirements |
| AI-K-008 | K-008 preserved | Large language model capabilities |
| AI-K-009 | K-009 preserved | RAG architecture patterns |
| AI-K-010 | K-010 preserved | Agentic AI design patterns |
| AI-K-011 | K-011 preserved | NLP task taxonomy |
| AI-K-012 | K-012 preserved | Transformer architecture |
| AI-K-013 | K-013 preserved | Computer vision task taxonomy |
| AI-K-014 | K-014 preserved | CNN/ViT architectures and transfer learning |
| AI-K-015 | K-015 preserved | Cloud data platform services |
| AI-K-016 | K-016 preserved | ML platform components |
| AI-K-017 | K-017 preserved | MLOps principles |
| AI-K-018 | K-018 preserved | Cloud AI/ML platform services |
| AI-K-019 | K-019 preserved | GPU and accelerated compute |
| AI-K-020 | K-020 preserved | Data storage technologies |
| AI-K-021 | K-021 preserved | DataOps principles |
| AI-K-022 | K-022 preserved | ML/AI research frontiers |
| AI-K-023 | K-023 preserved | Experimental design for ML |
| AI-K-024 | K-024 preserved | AI capability landscape |
| AI-K-025 | K-025 preserved | AI risk management frameworks |
| AI-K-026 | K-026 preserved | AI ethics and fairness evaluation |
| AI-K-027 | K-027 preserved | AI governance and regulatory compliance |
| AI-K-028 | K-028 preserved | AI security and adversarial ML |
| AI-K-029 | K-029 narrowed | Human-AI oversight architecture |
| AI-K-030 | **NEW — K-029 decomposition** | AI explainability and model interpretability |
| AI-K-031 | K-030 renumbered | AI supply chain risk and third-party dependencies |
| AI-K-032 | K-031 renumbered | AI system lifecycle management |
| AI-K-033 | K-032 renumbered | AI TEVV methodology |
| AI-K-034 | K-033 renumbered | AI data governance for ML systems |
| AI-K-035 | K-034 renumbered | AI business value assessment |
