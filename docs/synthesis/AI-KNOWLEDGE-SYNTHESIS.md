# AI Knowledge — Phase 1D Synthesis Analysis

**Domain:** AI/ML Foundations (AI)
**Dimension:** Knowledge
**Date:** 2026-04-03
**Pre-synthesis count:** 40 (29 Phase 1A baseline + 11 post-STRM additions)
**Post-synthesis count:** 34

## Evidence Summary

- **Total mappings:** 23,238 across 6 frameworks
- **Phase 1A entries (K-001 to K-029):** All have STRM evidence (1/6 to 6/6 coverage)
- **Post-STRM entries (K-030 to K-040):** 0/6 coverage (added after STRM runs)

### High Watermark (unique FDE count at STS thresholds)

| Framework | >=0.45 | >=0.50 | >=0.55 | >=0.60 |
|-----------|--------|--------|--------|--------|
| O*NET 30.2 | 16 | 9 | 3 | 1 |
| NIST NICE v2.1.0 | — | 329 WIDAI-relevant | — | — |
| DoD DCWF v5.1 | — | 438 WIDAI-relevant | — | — |
| DDaT | — | 26 WIDAI-relevant | — | — |
| EU AI Act | — | 30 WIDAI-relevant | — | — |
| NIST AI RMF 1.0 | — | 52 WIDAI-relevant | — | — |

### Strongest STRM Hits

| Entry | Strong | Max STS | Top framework evidence |
|-------|--------|---------|----------------------|
| AI-K-029 | 3 | 0.7249 | DCWF [3397] AI capabilities, [5909] AI limitations |
| AI-K-027 | 2 | 0.7244 | DCWF [5915] latest ML/AI tools, [7049] latest AI tools |
| AI-K-024 | 1 | 0.7182 | AIRMF-MG-3.2 pre-trained model monitoring |
| AI-K-005 | 1 | 0.7051 | DCWF [7010] container orchestration |
| AI-K-021 | 1 | 0.7020 | DCWF [6935] cloud service models |

## Duplicate Identification (Phase 1A)

Five groups of near-duplicate entries identified within the Phase 1A baseline:

### Group 1: Model Serving / Deployment
- **K-004:** ML model serving patterns (REST API, batch, streaming, edge)
- **K-023:** Model deployment strategies (batch, real-time, edge, A/B, canary, shadow)
- **Action:** Merge → single entry covering serving architecture AND deployment strategies
- **Evidence:** K-004 (407 mappings, max 0.6091) + K-023 (1,139 mappings, max 0.6363)

### Group 2: Containerization
- **K-005:** Containerization (Docker, Kubernetes) for ML
- **K-025:** Containerization + IaC for ML (GPU mgmt, distributed training, reproducible environments)
- **Action:** Merge → single entry. K-025 subsumes K-005.
- **Evidence:** K-005 (482 mappings, max 0.7051) + K-025 (413 mappings, max 0.6755)

### Group 3: Model Monitoring
- **K-007:** Model monitoring (drift detection, distribution monitoring, latency/throughput)
- **K-024:** Model monitoring requirements (drift, degradation, alerting, retraining triggers)
- **Action:** Merge → single entry. K-024 subsumes K-007.
- **Evidence:** K-007 (610 mappings, max 0.6883) + K-024 (1,405 mappings, max 0.7182)

### Group 4: Cloud Platforms
- **K-015:** Cloud data platform services across major providers
- **K-018:** Cloud AI/ML platform services (SageMaker, Vertex AI, Azure ML)
- **K-021:** Cloud data platform infrastructure (managed compute, serverless, object storage, streaming)
- **Action:** Merge K-015 + K-021 → single cloud data platform entry. Keep K-018 separate (ML-specific services).
- **Evidence:** K-015 (530, max 0.6932) + K-021 (573, max 0.7020) nearly identical scope. K-018 (1,166, max 0.6626) is ML-specific.

### Group 5: ML Platform Components
- **K-016:** ML platform components (feature stores, registries, experiment tracking, serving)
- **K-022:** ML pipeline orchestration (feature stores, experiment tracking, model registries, trade-offs)
- **Action:** Merge → single entry.
- **Evidence:** K-016 (543, max 0.6785) + K-022 (1,540, max 0.6583)

**Net effect:** 29 Phase 1A entries − 5 merges = 24 distinct Phase 1A entries

## Post-STRM Entry Evaluation (K-030 to K-040)

These entries have 0/6 STRM coverage because they were added after STRM runs. Evaluation against framework evidence to determine if concepts ARE surfaced by frameworks (mapped to other entries) or represent genuine gaps:

| Entry | Concept | Framework evidence | Verdict |
|-------|---------|-------------------|---------|
| K-030 | AI risk management frameworks | NIST AI RMF GV-1.x, MG-1.x; EU AI Act O-001, O-002 | **KEEP** — distinct from K-029 |
| K-031 | AI ethics and fairness | EU AI Act bias elements; NIST AI RMF fairness | **KEEP** — distinct concept |
| K-032 | AI governance and regulatory | NIST AI RMF GV functions; EU AI Act compliance | **KEEP** — distinct concept |
| K-033 | AI security and adversarial ML | DCWF AI security [5922]; NIST AI RMF security | **KEEP** — distinct concept |
| K-034 | Human-AI interaction design | EU AI Act C-003 (0.6804); NIST AI RMF GV-3.2 | **KEEP** — distinct from K-008/K-010 |
| K-035 | AI supply chain risk | NIST AI RMF GV-6.1, GV-6.2, MG-3.1 | **KEEP** — distinct concept |
| K-036 | AI lifecycle management | NIST AI RMF MG functions; EU AI Act modification | **KEEP** — governance-level lifecycle, distinct from K-006/K-017 ops |
| K-037 | AI TEVV methodology | EU AI Act O-004, O-005; NIST AI RMF MP-3.4, MS-2.13 | **KEEP** — distinct from K-028 (research design) |
| K-038 | AI data governance for ML | EU AI Act O-006, O-028; NIST AI RMF data elements | **KEEP** — AI-specific, cross-domain audit passes (distinct from DG) |
| K-039 | AI business value assessment | NIST AI RMF MP-1.3 (0.6260) | **KEEP** — distinct from K-029 (capabilities vs. assessment methods) |
| K-040 | Multimodal AI systems | No framework evidence | **REMOVE** — per ADR-014 Principle 5 |

**Net effect:** 10 kept, 1 removed

## Final Count

24 (Phase 1A deduplicated) + 10 (validated post-STRM) = **34 entries**

## Entry Mapping: Current → Proposed

| Proposed | Source | Action |
|----------|--------|--------|
| AI-K-001 | K-001 | Preserve (ML algorithms) |
| AI-K-002 | K-002 | Preserve (statistical inference) |
| AI-K-003 | K-003 | Preserve (feature engineering) |
| AI-K-004 | K-004 + K-023 | Merge (model serving + deployment) |
| AI-K-005 | K-005 + K-025 | Merge (containerization + IaC) |
| AI-K-006 | K-006 | Preserve (ML pipeline frameworks) |
| AI-K-007 | K-007 + K-024 | Merge (model monitoring) |
| AI-K-008 | K-008 | Preserve (LLM) |
| AI-K-009 | K-009 | Preserve (RAG) |
| AI-K-010 | K-010 | Preserve (agentic AI) |
| AI-K-011 | K-011 | Preserve (NLP taxonomy) |
| AI-K-012 | K-012 | Preserve (transformer arch) |
| AI-K-013 | K-013 | Preserve (CV taxonomy) |
| AI-K-014 | K-014 | Preserve (CNN/ViT) |
| AI-K-015 | K-015 + K-021 | Merge (cloud data platforms) |
| AI-K-016 | K-016 + K-022 | Merge (ML platform components) |
| AI-K-017 | K-017 | Preserve (MLOps) |
| AI-K-018 | K-018 | Preserve (cloud AI/ML services) |
| AI-K-019 | K-019 | Preserve (GPU/accelerated compute) |
| AI-K-020 | K-020 | Preserve (data storage) |
| AI-K-021 | K-026 | Renumber (DataOps) |
| AI-K-022 | K-027 | Renumber (AI research frontiers) |
| AI-K-023 | K-028 | Renumber (experimental design) |
| AI-K-024 | K-029 | Renumber (AI capability landscape) |
| AI-K-025 | K-030 | Renumber (AI risk management) |
| AI-K-026 | K-031 | Renumber (AI ethics/fairness) |
| AI-K-027 | K-032 | Renumber (AI governance/regulatory) |
| AI-K-028 | K-033 | Renumber (AI security/adversarial) |
| AI-K-029 | K-034 | Renumber (human-AI interaction) |
| AI-K-030 | K-035 | Renumber (AI supply chain risk) |
| AI-K-031 | K-036 | Renumber (AI lifecycle management) |
| AI-K-032 | K-037 | Renumber (AI TEVV) |
| AI-K-033 | K-038 | Renumber (AI data governance for ML) |
| AI-K-034 | K-039 | Renumber (AI business value) |
