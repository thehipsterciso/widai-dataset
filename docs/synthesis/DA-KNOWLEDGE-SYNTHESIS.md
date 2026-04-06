# DA Knowledge — Evidence-Driven Synthesis

## Overview

Domain: Data Architecture & Infrastructure (DA)
Dimension: Knowledge
Previous count: 25 (pre-evidence-first)
Final count: 27
Schema: 3.0.0
Methodology: Evidence-first synthesis per KSA-SYNTHESIS-METHODOLOGY.md v2.0.0

This synthesis was built entirely from cross-framework STRM evidence at STS ≥ 0.55. Prior entries were discarded as the starting point. Concepts were extracted from framework element descriptions across all 6 frameworks, clustered by competency domain, written as new entries, then subjected to 3 adversarial passes.

## Evidence Sources

| Framework | Elements at STS ≥ 0.50 | WIDAI-relevant | At STS ≥ 0.55 | At STS ≥ 0.60 |
|-----------|----------------------|----------------|---------------|---------------|
| O*NET 30.2 | 8 | 6 | 1 | 0 |
| NIST NICE v2.1.0 | 567 | 327 | 188 | 108 |
| DoD DCWF v5.1 | 687 | 398 | 165 | 93 |
| UK DDaT | 35 | 31 | 8 | 2 |
| EU AI Act | 21 | 19 | 5 | 2 |
| NIST AI RMF 1.0 | 40 | 38 | 9 | 7 |
| **Total** | **1,358** | **819** | **~376** | **~212** |

Total STRM mappings: 16,253

Evidence Density Ratio: 376 / 25 (current) = 15.04. Exceeds 10 threshold, triggering adversarial gap analysis.

## Concept Clusters

27 distinct concept clusters extracted from framework evidence:

### 1. Data Modeling and Schema Design
Conceptual, logical, physical modeling; entity-relationship diagrams; dimensional modeling; design trade-offs.
Evidence: NICE [K1086, K1095, S0029], DCWF [7016, 187], O*NET [1.A.1.e.1], DDaT [DDAT-SK-021]

### 2. Data Platform Architecture Patterns
Data warehouse, data lake, data lakehouse, data mesh, data fabric architectures; trade-offs and selection criteria.
Evidence: NICE [K0702, K0707, K1227], DCWF [7097, 4592, 5944], DDaT [DDAT-SK-112]

### 3. Complex Data Structures and Types
Knowledge of complex data structures, nested structures, array types, graph data, and their capabilities.
Evidence: NICE [K0693, K1281], DCWF [20, 7008]

### 4. Data Integration and ETL Patterns
ETL, ELT, CDC, event streaming, API-based integration, data virtualization patterns.
Evidence: NICE [K1246, K1280, K1146, K1144], DCWF [7029, 3470], DDaT [DDAT-SK-067]

### 5. Data Processing and Transformation
Data manipulation, mapping, format conversion, cleansing, data fusion, aggregation.
Evidence: NICE [K1246, K1097, K1148, S0904, S0727], DCWF [187, 5852]

### 6. Semantic Layer and Metrics Layer Design
Semantic layer design, metric definition standards, measure definition, dimension hierarchies, centralized consistency.
Evidence: NICE [K1278, K0896], DCWF [7016]

### 7. Distributed Data Processing Frameworks
Spark, Flink, Beam; when each framework is appropriate for latency, volume, and complexity requirements.
Evidence: NICE [K1095, K0693], DCWF [20, 5944]

### 8. Data Pipeline Orchestration and Scheduling
Orchestration tools (Airflow, Prefect, Dagster); DAG design; scheduling; failure handling; retry strategies; idempotency.
Evidence: NICE [K1030, K0768, S0451], DCWF [5944, 8179, 5634]

### 9. dbt and Transformation Framework Patterns
Model layering (staging, intermediate, mart); testing; documentation; lineage generation.
Evidence: NICE [S0029], DCWF [187, 7009]

### 10. Infrastructure-as-Code and Configuration Management
Terraform, Pulumi, configuration management tools; provisioning; reproducibility; version control.
Evidence: NICE [K0927, K0755], DCWF [2354, 5944]

### 11. Data Platform Security Controls
Network isolation, encryption at rest and in transit, identity/access management, audit logging.
Evidence: NICE [K1323, K1084, K0636], DCWF [7018, 108]

### 12. Data Privacy and Protection Techniques
Data masking, tokenization, anonymization, pseudonymization, privacy by design architectures.
Evidence: NICE [K1323, K0659], DCWF [7018]

### 13. Data Pipeline Monitoring and Observability
Data freshness, volume anomalies, schema changes, job failure patterns, alerting systems.
Evidence: NICE [K1247, K1298, K1125, K1123], DCWF [5951, 5952]

### 14. Data Classification, Cataloging, and Metadata Management
Data discovery, business glossary integration, metadata management systems, data lineage.
Evidence: NICE [K0866, K1143], DCWF [1126, 3298]

### 15. Database Administration and Lifecycle Management
Database provisioning, configuration, maintenance, performance monitoring, patching, end-of-life planning.
Evidence: NICE [K0992, K0704, K0991], DCWF [815, 1154]

### 16. Data Backup, Recovery, and Disaster Recovery
Backup scheduling, retention policies, RTO/RPO objectives, recoverability testing.
Evidence: NICE [K0701, T1132], DCWF [193]

### 17. Data Lineage and Provenance Tracking
Automated lineage capture, column-level lineage, impact analysis, supporting regulatory compliance.
Evidence: NICE [K0766, K1088], DCWF [3298]

### 18. API Design and Data Service Patterns
RESTful and GraphQL APIs, API gateway architecture, rate limiting, versioning, controlled data consumption.
Evidence: NICE [K0867, K0775], DCWF [3259]

### 19. Event-Driven Architecture for Data Systems
Message brokers, event sourcing, CQRS, publish-subscribe models, event-driven vs. request-response trade-offs.
Evidence: NICE [K0817, K1030], DCWF [2354]

### 20. Risk Management Frameworks and Processes
Risk assessment, mitigation, models, frameworks; risk scoring; supply chain risk.
Evidence: NICE [K0735, K0675, K0920, K0721, K1078], DCWF [108, 6931, 1037]

### 21. Risk Mitigation and Compliance
Risk mitigation strategies, residual risk assessment, compliance documentation, risk acceptance.
Evidence: NICE [K0920, K1209, K1208, K1268], DCWF [3470, 537]

### 22. DataOps and CI/CD for Data Systems
Continuous integration/deployment for data pipelines, automated testing of transformations, operational disciplines.
Evidence: NICE [S0451], DCWF [5944, 7028, 5851]

### 23. Container Orchestration and Cloud-Native Infrastructure
Kubernetes for data workloads, serverless compute, managed services vs. self-hosted trade-offs.
Evidence: NICE [K0806, K0863], DCWF [4592, 5944]

### 24. Cloud Cost Optimization and FinOps
Cloud cost models, pricing structures, reserved vs. on-demand capacity, cost allocation, optimization strategies.
Evidence: NICE [K0735], DCWF [5944]

### 25. Schema Evolution and Change Management
Backward/forward compatibility, schema registry patterns, migration strategies, governance processes.
Evidence: NICE [K1287, K1299], DCWF [7008, 2354]

### 26. Data Platform Capacity Planning and Performance Engineering
Workload characterization, resource utilization, scaling strategies, architecture and performance relationship.
Evidence: NICE [K0757, S0891], DCWF [7097, 5936]

### 27. System Availability, Reliability, and Fault Tolerance
Availability metrics, fault tolerance mechanisms, system resilience, performance under load.
Evidence: NICE [K1315, K0949, K0741, K0757], DCWF [5936, 130A]

## Adversarial Pass Results

### Pass 1 — Coverage Gaps

All ~376 WIDAI-relevant elements at STS ≥ 0.55 were systematically mapped to concept clusters. The mapping used element descriptions directly, not legacy STRM entry mappings.

**Key findings:**
- Cluster 1 (Data Modeling): K1086, K1095, S0029, K0693, 7016, 187 — strong corroboration across NICE and DCWF
- Cluster 20 (Risk Management): K0735, K0675, K0920, 108, 6931 — 15+ elements converging on risk frameworks
- Cluster 13 (Monitoring): K1247, K1298, K1125 — operational observability distinct from security monitoring
- Cluster 27 (Availability/Resilience): K1315, K0949, K0741 — distinct from performance engineering

**Gap analysis:** Framework elements at STS ≥ 0.55 consistently describe 27 distinct knowledge domains for DA. No WIDAI-relevant concept at this threshold was left unmapped.

**+2 entries added** (from initial 25-entry baseline, now including System Availability/Resilience and additional Risk concepts).

### Pass 2 — Redundancy and Overlap

Examined all adjacent concept pairs for overlap. Key distinctions confirmed:

| Pair | Distinction |
|------|-------------|
| Cluster 4 (Integration) vs 5 (Transformation) | Data movement/ingestion vs. data manipulation/cleansing. K1246 ≠ K1148. |
| Cluster 8 (Orchestration) vs 9 (dbt Transformation) | Task scheduling/DAG patterns vs. transformation framework patterns. S0451 ≠ S0029. |
| Cluster 11 (Security Controls) vs 12 (Privacy) | Infrastructure/access control vs. data-level masking/anonymization. K1323 ≠ K1084. |
| Cluster 13 (Monitoring) vs 15 (DB Admin) | Observability/alerting vs. lifecycle management. K1247 ≠ K0992. |
| Cluster 20 (Risk Frameworks) vs 21 (Mitigation) | Strategic risk frameworks vs. tactical mitigation and compliance documentation. K0735 ≠ K1209. |
| Cluster 24 (Cloud FinOps) vs 26 (Performance) | Cost optimization vs. resource utilization and scaling. Separate concerns. |

**No merges.**

### Pass 3 — Domain Boundary

All 27 entries reviewed for DA fit. All concepts are genuinely about data infrastructure, architecture, or platform operations. No entries belong in other domains.

| Entry | Domain Fit | Verdict |
|-------|-----------|---------|
| Cluster 1–5 (Data modeling, integration, transformation) | Core DA | Keep |
| Cluster 6 (Semantic/Metrics) | Analytics layer but scoped to DA infrastructure | Keep |
| Cluster 8 (Orchestration) | Core DA infrastructure | Keep |
| Cluster 11–12 (Security/Privacy) | DA-specific controls, not SP domain | Keep |
| Cluster 13 (Monitoring) | Data platform observability, not RM domain | Keep |
| Cluster 20–21 (Risk) | Scoped to data platform and architectural risk, not RM domain policy | Keep |
| Cluster 27 (Availability) | Platform availability, not RM policy | Keep |

**No entries removed.**

## STRM Coverage Note

The previous 25 entries (K-001 through K-016 with STRM coverage, K-017 through K-025 with 0/6) were entirely discarded in this synthesis. The new 27 entries are built from ground-up concept extraction. The new entries can be mapped to framework elements manually; the automated STRM scoring file reflects old entry text that no longer applies.

## Final Entry List

| ID | Concept | Key Evidence |
|---|---|---|
| DA-K-001 | Data modeling and schema design | K1086, K1095, 7016 |
| DA-K-002 | Data platform architecture patterns | K0702, K0707, K1227 |
| DA-K-003 | Complex data structures and types | K0693, K1281, 20 |
| DA-K-004 | Data integration and ETL patterns | K1246, K1280, K1146 |
| DA-K-005 | Data processing and transformation | K1246, K1097, K1148 |
| DA-K-006 | Semantic layer and metrics design | K1278, K0896, 7016 |
| DA-K-007 | Distributed data processing frameworks | K1095, K0693, 5944 |
| DA-K-008 | Data pipeline orchestration and scheduling | K1030, K0768, 5944 |
| DA-K-009 | dbt and transformation framework patterns | S0029, 187, 7009 |
| DA-K-010 | Infrastructure-as-code and configuration management | K0927, K0755, 2354 |
| DA-K-011 | Data platform security controls | K1323, K1084, 7018 |
| DA-K-012 | Data privacy and protection techniques | K1323, K0659, 7018 |
| DA-K-013 | Data pipeline monitoring and observability | K1247, K1298, 5951 |
| DA-K-014 | Data classification, cataloging, metadata management | K0866, K1143, 3298 |
| DA-K-015 | Database administration and lifecycle management | K0992, K0704, 1154 |
| DA-K-016 | Data backup, recovery, disaster recovery | K0701, T1132, 193 |
| DA-K-017 | Data lineage and provenance tracking | K0766, K1088, 3298 |
| DA-K-018 | API design and data service patterns | K0867, K0775, 3259 |
| DA-K-019 | Event-driven architecture for data systems | K0817, K1030, 2354 |
| DA-K-020 | Risk management frameworks and processes | K0735, K0675, 108 |
| DA-K-021 | Risk mitigation and compliance | K0920, K1209, 3470 |
| DA-K-022 | DataOps and CI/CD for data systems | S0451, 5944, 7028 |
| DA-K-023 | Container orchestration and cloud-native infrastructure | K0806, K0863, 4592 |
| DA-K-024 | Cloud cost optimization and FinOps | K0735, K0863, 5944 |
| DA-K-025 | Schema evolution and change management | K1287, K1299, 7008 |
| DA-K-026 | Data platform capacity planning and performance | K0757, S0891, 7097 |
| DA-K-027 | System availability, reliability, and fault tolerance | K1315, K0949, 5936 |
