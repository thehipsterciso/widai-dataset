#!/usr/bin/env python3
"""
R08: Priority KSA Authoring for Gap Roles
==========================================
Authors KSAs for the 5 roles identified by R01 as having Partial readiness
(role exists in ATLAS but no KSAs mapped). These roles appeared in PE due
diligence archetypes and directly impact the R04 scoring model's ability
to produce meaningful assessments.

Gap roles:
  1. Model Risk Manager (ATLAS-RSK-0108) — Financial Services archetype
  2. MLOps Engineer (ATLAS-ENG-0041) — SaaS/Technology archetype
  3. DataOps Engineer (ATLAS-ENG-0037) — SaaS/Technology archetype
  4. Data Protection Officer (ATLAS-GOV-0016) — Healthcare archetype
  5. Clinical Data Manager (ATLAS-ANL-0092) — Healthcare archetype

This script:
  - Adds new KSAs to the appropriate category KSA files
  - Adds role-KSA mappings to the appropriate mapping files
  - Updates counts in both file types
  - Produces an R08 results summary

Quality target: 4.0+/5 per R02 validated AI-assisted authoring standard.
"""

import json
import os
from datetime import date

ATLAS_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VERSION = "0.4.2"

# ============================================================
# KSA DEFINITIONS — 5 gap roles, 43 total KSAs
# ============================================================

NEW_KSAS = {
    "RSK": {
        "work_role_id": "WR-RSK-06.05",
        "work_role_title": "Model Risk Manager",
        "role_id": "ATLAS-RSK-0108",
        "ksas": [
            {
                "ksa_id": "RSK-06.05-K-001",
                "type": "Knowledge",
                "statement": "Knowledge of model risk management regulatory requirements, including Federal Reserve SR 11-7, OCC Bulletin 2011-12, and their supervisory expectations for model definition, materiality thresholds, model governance, and independent validation.",
                "origin_framework": "ATLAS",
                "origin_version": VERSION
            },
            {
                "ksa_id": "RSK-06.05-K-002",
                "type": "Knowledge",
                "statement": "Knowledge of model validation methodologies, including conceptual soundness review, outcomes analysis, benchmarking, sensitivity analysis, back-testing, and the distinction between challenger model and champion model approaches.",
                "origin_framework": "ATLAS",
                "origin_version": VERSION
            },
            {
                "ksa_id": "RSK-06.05-K-003",
                "type": "Knowledge",
                "statement": "Knowledge of model inventory management practices, including model tiering by materiality and complexity, risk classification, lifecycle tracking from development through retirement, and the documentation standards required at each stage.",
                "origin_framework": "ATLAS",
                "origin_version": VERSION
            },
            {
                "ksa_id": "RSK-06.05-K-004",
                "type": "Knowledge",
                "statement": "Knowledge of AI and machine learning-specific model risk considerations, including data drift, concept drift, black-box explainability requirements, and how traditional model risk frameworks must adapt for non-parametric, ensemble, and foundation models.",
                "origin_framework": "ATLAS",
                "origin_version": VERSION
            },
            {
                "ksa_id": "RSK-06.05-S-001",
                "type": "Skill",
                "statement": "Skill in designing and maintaining a model risk governance framework, including policy development, role and responsibility definition, escalation protocols, exception management, and board-level model risk reporting.",
                "origin_framework": "ATLAS",
                "origin_version": VERSION
            },
            {
                "ksa_id": "RSK-06.05-S-002",
                "type": "Skill",
                "statement": "Skill in evaluating model validation findings and remediation plans, assessing whether identified model limitations are acceptable given the model's use case, materiality, and the organization's risk appetite.",
                "origin_framework": "ATLAS",
                "origin_version": VERSION
            },
            {
                "ksa_id": "RSK-06.05-T-001",
                "type": "Task",
                "statement": "Establish and maintain the enterprise model inventory, ensuring all models — including AI/ML models, vendor models, and end-user computing models — are registered, tiered by risk, and subject to appropriate validation cadence.",
                "origin_framework": "ATLAS",
                "origin_version": VERSION
            },
            {
                "ksa_id": "RSK-06.05-T-002",
                "type": "Task",
                "statement": "Conduct or oversee periodic model risk assessments, produce aggregate model risk reporting for senior management and the board, and ensure timely escalation of material model risk findings to appropriate governance bodies.",
                "origin_framework": "ATLAS",
                "origin_version": VERSION
            },
            {
                "ksa_id": "RSK-06.05-T-003",
                "type": "Task",
                "statement": "Define and enforce model development standards, including documentation requirements, testing protocols, approval gates, ongoing monitoring expectations, and the criteria for model retirement or replacement.",
                "origin_framework": "ATLAS",
                "origin_version": VERSION
            }
        ]
    },
    "ENG_mlops": {
        "category": "ENG",
        "work_role_id": "WR-ENG-02.06",
        "work_role_title": "MLOps Engineer",
        "role_id": "ATLAS-ENG-0041",
        "ksas": [
            {
                "ksa_id": "ENG-02.06-K-001",
                "type": "Knowledge",
                "statement": "Knowledge of ML pipeline orchestration tools and patterns, including feature stores, experiment tracking, model registries, and the architectural trade-offs between managed and self-hosted ML platforms.",
                "origin_framework": "ATLAS",
                "origin_version": VERSION
            },
            {
                "ksa_id": "ENG-02.06-K-002",
                "type": "Knowledge",
                "statement": "Knowledge of model deployment strategies, including batch inference, real-time serving, edge deployment, A/B testing, canary releases, and shadow deployments, and the infrastructure requirements and failure modes of each.",
                "origin_framework": "ATLAS",
                "origin_version": VERSION
            },
            {
                "ksa_id": "ENG-02.06-K-003",
                "type": "Knowledge",
                "statement": "Knowledge of model monitoring requirements, including data drift detection, prediction drift, performance degradation metrics, and the alerting thresholds and retraining triggers appropriate for different model types and serving patterns.",
                "origin_framework": "ATLAS",
                "origin_version": VERSION
            },
            {
                "ksa_id": "ENG-02.06-K-004",
                "type": "Knowledge",
                "statement": "Knowledge of containerization and infrastructure-as-code as applied to ML workloads, including GPU resource management, distributed training job scheduling, and reproducible environment management across development and production.",
                "origin_framework": "ATLAS",
                "origin_version": VERSION
            },
            {
                "ksa_id": "ENG-02.06-S-001",
                "type": "Skill",
                "statement": "Skill in designing and implementing CI/CD pipelines for ML models, including automated testing at unit, integration, and model quality levels, artifact versioning, and deployment automation with rollback capability.",
                "origin_framework": "ATLAS",
                "origin_version": VERSION
            },
            {
                "ksa_id": "ENG-02.06-S-002",
                "type": "Skill",
                "statement": "Skill in diagnosing and resolving ML infrastructure failures, including training job crashes, serving latency spikes, resource contention across shared clusters, and data pipeline breakdowns that affect model inputs.",
                "origin_framework": "ATLAS",
                "origin_version": VERSION
            },
            {
                "ksa_id": "ENG-02.06-T-001",
                "type": "Task",
                "statement": "Build and maintain automated ML pipelines from feature engineering through model training, validation, deployment, and monitoring, ensuring reproducibility and auditability at every stage.",
                "origin_framework": "ATLAS",
                "origin_version": VERSION
            },
            {
                "ksa_id": "ENG-02.06-T-002",
                "type": "Task",
                "statement": "Implement model monitoring and observability systems that detect data drift, prediction drift, and performance degradation, triggering alerts or automated retraining workflows when defined thresholds are exceeded.",
                "origin_framework": "ATLAS",
                "origin_version": VERSION
            }
        ]
    },
    "ENG_dataops": {
        "category": "ENG",
        "work_role_id": "WR-ENG-02.07",
        "work_role_title": "DataOps Engineer",
        "role_id": "ATLAS-ENG-0037",
        "ksas": [
            {
                "ksa_id": "ENG-02.07-K-001",
                "type": "Knowledge",
                "statement": "Knowledge of DataOps principles and practices, including pipeline automation, environment management, data testing strategies, configuration-as-code, and the distinction between DataOps, DevOps, and MLOps as complementary disciplines.",
                "origin_framework": "ATLAS",
                "origin_version": VERSION
            },
            {
                "ksa_id": "ENG-02.07-K-002",
                "type": "Knowledge",
                "statement": "Knowledge of data pipeline orchestration tools and scheduling patterns, including dependency graph management, failure handling, retry strategies, idempotency requirements, and SLA-driven monitoring.",
                "origin_framework": "ATLAS",
                "origin_version": VERSION
            },
            {
                "ksa_id": "ENG-02.07-K-003",
                "type": "Knowledge",
                "statement": "Knowledge of data quality testing frameworks, including schema validation, data contract enforcement, freshness checks, volume anomaly detection, and referential integrity verification within automated pipelines.",
                "origin_framework": "ATLAS",
                "origin_version": VERSION
            },
            {
                "ksa_id": "ENG-02.07-S-001",
                "type": "Skill",
                "statement": "Skill in implementing automated data pipeline testing — unit tests for individual transformations, integration tests for end-to-end data flows, and regression tests that validate output consistency across pipeline changes.",
                "origin_framework": "ATLAS",
                "origin_version": VERSION
            },
            {
                "ksa_id": "ENG-02.07-S-002",
                "type": "Skill",
                "statement": "Skill in designing data pipeline observability systems, including lineage tracking, execution monitoring, cost attribution, and root-cause analysis tooling for pipeline failures and data quality incidents.",
                "origin_framework": "ATLAS",
                "origin_version": VERSION
            },
            {
                "ksa_id": "ENG-02.07-T-001",
                "type": "Task",
                "statement": "Build and maintain automated data pipelines with version-controlled transformations, automated testing, environment parity between development and production, and deployment processes that enable rapid iteration without production risk.",
                "origin_framework": "ATLAS",
                "origin_version": VERSION
            },
            {
                "ksa_id": "ENG-02.07-T-002",
                "type": "Task",
                "statement": "Implement and operate data observability infrastructure that provides pipeline lineage, execution history, data quality metrics, and proactive alerting for anomalies and SLA violations.",
                "origin_framework": "ATLAS",
                "origin_version": VERSION
            },
            {
                "ksa_id": "ENG-02.07-T-003",
                "type": "Task",
                "statement": "Manage data environment provisioning and configuration, ensuring development, staging, and production environments maintain parity and that pipeline promotions follow defined testing and approval workflows.",
                "origin_framework": "ATLAS",
                "origin_version": VERSION
            }
        ]
    },
    "GOV": {
        "work_role_id": "WR-GOV-01.07",
        "work_role_title": "Data Protection Officer",
        "role_id": "ATLAS-GOV-0016",
        "ksas": [
            {
                "ksa_id": "GOV-01.07-K-001",
                "type": "Knowledge",
                "statement": "Knowledge of data protection law, including GDPR, CCPA/CPRA, and sector-specific privacy regulations, with emphasis on the legal bases for processing, data subject rights, cross-border transfer mechanisms, and enforcement precedent.",
                "origin_framework": "ATLAS",
                "origin_version": VERSION
            },
            {
                "ksa_id": "GOV-01.07-K-002",
                "type": "Knowledge",
                "statement": "Knowledge of the Data Protection Officer's statutory role, responsibilities, and independence requirements under GDPR Articles 37-39, including reporting lines, conflict-of-interest prohibitions, and the distinction between advisory and decision-making authority.",
                "origin_framework": "ATLAS",
                "origin_version": VERSION
            },
            {
                "ksa_id": "GOV-01.07-K-003",
                "type": "Knowledge",
                "statement": "Knowledge of Data Protection Impact Assessment methodology, including the conditions that make assessments mandatory, techniques for evaluating risk to individuals, and how to document residual risk and mitigation measures to supervisory authority standards.",
                "origin_framework": "ATLAS",
                "origin_version": VERSION
            },
            {
                "ksa_id": "GOV-01.07-K-004",
                "type": "Knowledge",
                "statement": "Knowledge of privacy-by-design and privacy-by-default principles, including their application to system architecture, data minimization, purpose limitation, storage limitation, and consent management design patterns.",
                "origin_framework": "ATLAS",
                "origin_version": VERSION
            },
            {
                "ksa_id": "GOV-01.07-S-001",
                "type": "Skill",
                "statement": "Skill in conducting and reviewing Data Protection Impact Assessments, identifying processing activities that present high risk to individuals, and recommending proportionate technical and organizational measures to mitigate identified risks.",
                "origin_framework": "ATLAS",
                "origin_version": VERSION
            },
            {
                "ksa_id": "GOV-01.07-S-002",
                "type": "Skill",
                "statement": "Skill in advising on data processing agreements, standard contractual clauses, binding corporate rules, and other cross-border data transfer mechanisms, ensuring compliance with applicable jurisdictional requirements and supervisory guidance.",
                "origin_framework": "ATLAS",
                "origin_version": VERSION
            },
            {
                "ksa_id": "GOV-01.07-T-001",
                "type": "Task",
                "statement": "Monitor organizational compliance with data protection obligations, conduct internal audits of processing activities, maintain the register of processing activities, and report compliance posture to senior management and supervisory authorities as required.",
                "origin_framework": "ATLAS",
                "origin_version": VERSION
            },
            {
                "ksa_id": "GOV-01.07-T-002",
                "type": "Task",
                "statement": "Serve as the designated point of contact for supervisory authorities and data subjects exercising their rights, managing inquiries, access requests, erasure requests, and complaints within statutory timeframes.",
                "origin_framework": "ATLAS",
                "origin_version": VERSION
            },
            {
                "ksa_id": "GOV-01.07-T-003",
                "type": "Task",
                "statement": "Advise on data protection implications of new projects, systems, and processing activities, ensuring privacy considerations are integrated into design and procurement decisions before processing begins.",
                "origin_framework": "ATLAS",
                "origin_version": VERSION
            }
        ]
    },
    "ANL": {
        "work_role_id": "WR-ANL-05.05",
        "work_role_title": "Clinical Data Manager",
        "role_id": "ATLAS-ANL-0092",
        "ksas": [
            {
                "ksa_id": "ANL-05.05-K-001",
                "type": "Knowledge",
                "statement": "Knowledge of clinical data management principles, including Good Clinical Practice requirements, ICH E6(R2) guidelines, and the regulatory expectations for data integrity, audit trails, and traceability in clinical trial submissions.",
                "origin_framework": "ATLAS",
                "origin_version": VERSION
            },
            {
                "ksa_id": "ANL-05.05-K-002",
                "type": "Knowledge",
                "statement": "Knowledge of electronic data capture systems and clinical data management platforms, including database design, edit check programming, query management workflows, and the validation requirements for 21 CFR Part 11 and Annex 11 compliance.",
                "origin_framework": "ATLAS",
                "origin_version": VERSION
            },
            {
                "ksa_id": "ANL-05.05-K-003",
                "type": "Knowledge",
                "statement": "Knowledge of clinical data standards, including CDISC standards (CDASH, SDTM, ADaM), MedDRA coding conventions, WHO Drug Dictionary, and the submission dataset requirements for FDA and EMA regulatory filings.",
                "origin_framework": "ATLAS",
                "origin_version": VERSION
            },
            {
                "ksa_id": "ANL-05.05-S-001",
                "type": "Skill",
                "statement": "Skill in designing clinical trial databases, including case report form development, edit check logic specification, data validation rules, and the traceability documentation required for regulatory inspection and audit.",
                "origin_framework": "ATLAS",
                "origin_version": VERSION
            },
            {
                "ksa_id": "ANL-05.05-S-002",
                "type": "Skill",
                "statement": "Skill in managing clinical data quality processes, including medical coding review, query resolution, discrepancy management, and the reconciliation of clinical data across electronic data capture, safety databases, and central laboratory systems.",
                "origin_framework": "ATLAS",
                "origin_version": VERSION
            },
            {
                "ksa_id": "ANL-05.05-T-001",
                "type": "Task",
                "statement": "Design, build, and validate clinical trial databases in electronic data capture systems, including CRF specifications, edit check logic, user acceptance testing, and documentation of compliance with study protocol and applicable regulatory requirements.",
                "origin_framework": "ATLAS",
                "origin_version": VERSION
            },
            {
                "ksa_id": "ANL-05.05-T-002",
                "type": "Task",
                "statement": "Manage ongoing data quality during clinical trials, including query generation and resolution, serious adverse event reconciliation, medical coding review, and database lock preparation with documented clean-point verification.",
                "origin_framework": "ATLAS",
                "origin_version": VERSION
            },
            {
                "ksa_id": "ANL-05.05-T-003",
                "type": "Task",
                "statement": "Produce clinical data management documentation, including data management plans, data review plans, CRF completion guidelines, and database lock reports required for regulatory submission packages.",
                "origin_framework": "ATLAS",
                "origin_version": VERSION
            }
        ]
    }
}

# ============================================================
# APPLY CHANGES
# ============================================================

def load_json(path):
    with open(path, 'r') as f:
        return json.load(f)

def save_json(path, data):
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)
    print(f"  ✓ Updated {os.path.relpath(path, ATLAS_ROOT)}")

def update_ksa_file(category_code, new_ksas):
    """Add KSAs to the category KSA file and update counts."""
    path = os.path.join(ATLAS_ROOT, 'ksas', f'{category_code}_ksas.json')
    data = load_json(path)

    # Add new KSAs
    data['ksas'].extend(new_ksas)

    # Recount by type
    k_count = sum(1 for k in data['ksas'] if k['type'] == 'Knowledge')
    s_count = sum(1 for k in data['ksas'] if k['type'] == 'Skill')
    t_count = sum(1 for k in data['ksas'] if k['type'] == 'Task')
    a_count = sum(1 for k in data['ksas'] if k['type'] == 'Ability')

    data['ksa_count'] = len(data['ksas'])
    data['knowledge_count'] = k_count
    data['skill_count'] = s_count
    data['task_count'] = t_count
    if a_count > 0:
        data['ability_count'] = a_count

    save_json(path, data)
    return len(new_ksas)

def update_mapping_file(category_code, work_role_id, work_role_title, ksa_ids):
    """Add role-KSA mappings to the category mapping file."""
    path = os.path.join(ATLAS_ROOT, 'mappings', f'role_ksa_{category_code}.json')
    data = load_json(path)

    new_mappings = []
    for ksa_id in ksa_ids:
        new_mappings.append({
            "work_role_id": work_role_id,
            "work_role_title": work_role_title,
            "ksa_id": ksa_id,
            "source_framework": "ATLAS",
            "source_version": VERSION,
            "relationship_type": "requires"
        })

    data['relationships'].extend(new_mappings)
    data['relationship_count'] = len(data['relationships'])

    save_json(path, data)
    return len(new_mappings)

def main():
    print("=" * 60)
    print("R08: Priority KSA Authoring for Gap Roles")
    print("=" * 60)
    print()

    total_ksas = 0
    total_mappings = 0
    results = []

    # Process each role group
    role_configs = [
        ("RSK", NEW_KSAS["RSK"]),
        ("ENG", NEW_KSAS["ENG_mlops"]),
        ("ENG", NEW_KSAS["ENG_dataops"]),
        ("GOV", NEW_KSAS["GOV"]),
        ("ANL", NEW_KSAS["ANL"]),
    ]

    for category_code, config in role_configs:
        actual_cat = config.get("category", category_code)
        role_title = config["work_role_title"]
        role_id = config["role_id"]
        work_role_id = config["work_role_id"]
        ksas = config["ksas"]
        ksa_ids = [k["ksa_id"] for k in ksas]

        print(f"Processing: {role_title} ({role_id})")

        # Add KSAs
        n_ksas = update_ksa_file(actual_cat, ksas)
        total_ksas += n_ksas

        # Add mappings
        n_maps = update_mapping_file(actual_cat, work_role_id, role_title, ksa_ids)
        total_mappings += n_maps

        k_count = sum(1 for k in ksas if k['type'] == 'Knowledge')
        s_count = sum(1 for k in ksas if k['type'] == 'Skill')
        t_count = sum(1 for k in ksas if k['type'] == 'Task')

        results.append({
            "role_id": role_id,
            "canonical_title": role_title,
            "work_role_id": work_role_id,
            "category": actual_cat,
            "ksa_count": n_ksas,
            "knowledge": k_count,
            "skills": s_count,
            "tasks": t_count,
            "mapping_count": n_maps
        })

        print(f"  → {n_ksas} KSAs authored ({k_count}K/{s_count}S/{t_count}T), {n_maps} mappings created")
        print()

    print("=" * 60)
    print(f"TOTAL: {total_ksas} KSAs authored, {total_mappings} mappings created")
    print(f"Roles completed: {len(results)}")
    print("=" * 60)

    # Write results JSON
    results_data = {
        "test_id": "R08",
        "test_date": str(date.today()),
        "atlas_version": VERSION,
        "description": "Priority KSA authoring for 5 gap roles identified by R01 Coverage Gap Test",
        "authoring_method": "AI-assisted (validated by R02 at 4.26/5 quality)",
        "total_ksas_authored": total_ksas,
        "total_mappings_created": total_mappings,
        "roles_completed": results,
        "impact": {
            "previous_ksa_coverage": "92.2% (59/64 archetype roles with KSAs)",
            "new_ksa_coverage": "100% (64/64 archetype roles with KSAs)",
            "pe_assessment_readiness": "All 5 PE archetypes now have full KSA coverage for scoring"
        }
    }

    results_path = os.path.join(ATLAS_ROOT, 'docs', 'roadmap', 'R08-priority-ksa-authoring.json')
    save_json(results_path, results_data)

    print(f"\nResults written to: docs/roadmap/R08-priority-ksa-authoring.json")

if __name__ == '__main__':
    main()
