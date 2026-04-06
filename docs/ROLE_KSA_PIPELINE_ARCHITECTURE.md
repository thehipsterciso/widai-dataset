# WIDAI Role-KSA Evaluation Pipeline: Architecture Document

**Version:** 1.0  
**Status:** Planning / Pre-Implementation  
**Last Updated:** 2026-04-06  
**Scope:** 187 WIDAI work roles × 1,069 KSAs = 199,903 evaluations

---

## Table of Contents

1. [Purpose and Goals](#1-purpose-and-goals)
2. [System Overview](#2-system-overview)
3. [Per-KSA Pipeline Detail](#3-per-ksa-pipeline-detail)
4. [Data Schemas](#4-data-schemas)
5. [File and Directory Layout](#5-file-and-directory-layout)
6. [Script Architecture and Responsibilities](#6-script-architecture-and-responsibilities)
7. [Resumability and Fault Tolerance](#7-resumability-and-fault-tolerance)
8. [Scale and Runtime Expectations](#8-scale-and-runtime-expectations)
9. [Quality Guarantees](#9-quality-guarantees)

---

## 1. Purpose and Goals

### 1.1 What This System Builds

The WIDAI Role-KSA Evaluation Pipeline produces a complete, evidence-backed mapping between every work role in the WIDAI taxonomy and the full catalog of Knowledge, Skills, Abilities, and Tasks (KSAs). For each of the 187 WIDAI work roles, every one of the 1,069 KSAs is evaluated to produce a documented include/exclude decision. The final output is a corpus of 199,903 atomic evaluation artifacts — one per role-KSA pair — that together constitute a defensible, auditable role-competency model.


### 1.2 Design Philosophy

The previous approach used a candidate generation query that pre-filtered KSAs before any evaluation agent saw them. That approach was discarded because it was doing hidden quality filtering — making irreversible inclusion/exclusion decisions at the query layer, before any intelligent reasoning was applied. Pre-filtering assumes the scoring layer can be trusted to surface all genuinely relevant KSAs, and that assumption cannot be validated once filtering has already occurred.

The new approach inverts this: **evaluate everything, let agents make the calls.** Every KSA goes through the full four-pass evaluation pipeline for every role. Filtering decisions happen at the agent layer where they can be inspected, challenged, and documented. No KSA is silently discarded before intelligent evaluation begins.

This design choice has real costs — 199,903 evaluations instead of a much smaller candidate set — and that cost is intentional. The value of a complete, unfiltered mapping depends entirely on the confidence that nothing was excluded before the question was even asked.

### 1.3 Goals

**Primary goal:** Produce a complete role-KSA mapping where every include/exclude decision is documented with rationale, scored against STRM signal data, and validated through two independent adversarial passes.

**Quality goal:** Every artifact must contain enough information to audit the decision without re-running the evaluation. A reviewer reading the artifact cold should be able to follow the chain of reasoning from raw STRM scores through adversarial challenges to the final ruling.

**Durability goal:** The pipeline must be safe to run over days or weeks with arbitrary interruptions. No evaluation work should be lost due to process failure, timeout, or manual stop. The pipeline resumes from where it stopped, at KSA granularity, not role granularity.

**Completeness goal:** Upon termination, the status of every role-KSA pair must be knowable — either a complete artifact exists, or the pair is explicitly flagged as pending. There must be no silent gaps.

**Traceability goal:** The STRM data source, the model used for each LLM pass, the timestamp of evaluation, and the schema version must be recorded in every artifact. Future schema changes must be handled through versioning, not in-place mutation.

---

## 2. System Overview

### 2.1 High-Level Data Flow

```
Input Sources
─────────────
widai_roles.json          ← 187 WIDAI work roles with descriptions and categories
ksa_catalog.json          ← 1,069 KSAs with text, dimension, and domain
strm/                     ← STRM similarity scores (per-framework files)
strm_mapping.json         ← Consolidated STRM mapping (all frameworks)

                          │
                          ▼
┌─────────────────────────────────────────────────────┐
│              evaluate_role_ksas.py                  │
│              (main orchestrator)                    │
│                                                     │
│  For each role (187 total):                         │
│    Check resumability state                         │
│    For each KSA (1,069 total):                      │
│      Check if artifact already exists               │
│      If not: run 4-pass evaluation pipeline         │
│      Write artifact to disk                         │
│    Write role summary.json                          │
│    Update ROADMAP.md                                │
└─────────────────────────────────────────────────────┘
                          │
                          ▼
Output Artifacts
────────────────
docs/role_ksa_evaluations/{role_id}/{ksa_id}.json   ← 199,903 artifacts
docs/role_ksa_evaluations/{role_id}/summary.json    ← 187 role summaries
docs/role_ksa_evaluations/ROADMAP.md                ← Live completion tracker
mappings/role_ksa_{category}.json                   ← Generated mapping files
logs/evaluation_{timestamp}.log                     ← Per-run log
```


### 2.2 Four-Pass Pipeline per KSA

Each of the 199,903 role-KSA pairs passes through four sequential stages. No pass is optional. No pass is skipped based on Pass 1 score.

```
For each role-KSA pair:

  ┌──────────────────────────────────────────────┐
  │  PASS 1 — Python Scoring Agent               │
  │  (No LLM. Pure programmatic computation.)    │
  │                                              │
  │  Input:  KSA id, role id                     │
  │  Source: STRM data files                     │
  │  Output: composite score, signal strength,   │
  │          top 3 anchors, per-framework scores  │
  └──────────────────────┬───────────────────────┘
                         │
                         ▼
  ┌──────────────────────────────────────────────┐
  │  PASS 2 — LLM Evaluation Agent               │
  │  (claude-sonnet-4-5, temp=0)                 │
  │                                              │
  │  Input:  role desc, KSA text, Pass 1 block   │
  │  Output: scope_fit, seniority_fit,           │
  │          preliminary_decision, rationale      │
  └──────────────────────┬───────────────────────┘
                         │
                         ▼
  ┌──────────────────────────────────────────────┐
  │  PASS 3 — Adversarial Agent 1                │
  │  (Internal consistency challenge)            │
  │  (claude-sonnet-4-5, temp=0.1)               │
  │                                              │
  │  Input:  role context, KSA, Pass 2 decision  │
  │  Output: upheld | overturned + challenge     │
  │  If overturned: Pass 2 agent rebuts + rules  │
  └──────────────────────┬───────────────────────┘
                         │
                         ▼
  ┌──────────────────────────────────────────────┐
  │  PASS 4 — Adversarial Agent 2                │
  │  (External ground truth challenge)           │
  │  (claude-sonnet-4-5, temp=0.1 + web search) │
  │                                              │
  │  Input:  role context, KSA, Pass 2+3 state  │
  │  Output: upheld | overturned + evidence      │
  └──────────────────────┬───────────────────────┘
                         │
                         ▼
  ┌──────────────────────────────────────────────┐
  │  FINAL DECISION LOGIC                        │
  │                                              │
  │  Both adversarial uphold  → high confidence  │
  │  One overturns            → medium, agent    │
  │                             makes final call │
  │  Both overturn            → low confidence,  │
  │                             must reverse or  │
  │                             justify strongly  │
  └──────────────────────────────────────────────┘
                         │
                         ▼
              Write artifact {ksa_id}.json
```

---

## 3. Per-KSA Pipeline Detail

### 3.1 Pass 1 — Python Scoring Agent

**Type:** Programmatic. No LLM. No network calls.  
**Script:** `scripts/scoring.py`  
**Inputs:** KSA id, role id, STRM data  
**Outputs:** Structured score block (dict), no decision

#### 3.1.1 STRM Data Access

The STRM data may exist in two forms:
- `strm_mapping.json` — a single consolidated file containing all frameworks
- `strm/` directory — per-framework files (e.g., `strm/dcwf.json`, `strm/ddat.json`)

The scoring module must handle both. The lookup key is the KSA id. For each framework present in the STRM data, extract all available metric fields. The canonical field names are:

| Field | Description |
|-------|-------------|
| `cross_encoder_sts` | Cross-encoder semantic textual similarity — highest weight |
| `bertscore` | BERT-based token-level similarity |
| `nli_score` | Natural language inference entailment score |
| `bi_encoder_cosine` | Bi-encoder cosine similarity |
| `jaccard` | Token-level Jaccard overlap |

**Important:** Use the actual field names present in the STRM data. If the STRM data uses different keys, the scoring module must map them. Do not hardcode assumptions about field presence — fields may be absent for some framework-KSA combinations and must be treated as null rather than zero.

#### 3.1.2 Composite Score Computation

The composite score is a weighted average of available metrics. The weights below represent the intended balance; the implementation must skip metrics that are null rather than treating them as 0.

| Metric | Weight |
|--------|--------|
| `cross_encoder_sts` | 0.40 |
| `bertscore` | 0.20 |
| `nli_score` | 0.20 |
| `bi_encoder_cosine` | 0.15 |
| `jaccard` | 0.05 |

When one or more metrics are absent, renormalize weights across the available metrics so they still sum to 1.0. Record which metrics were used and which were absent in the Pass 1 output block.

The composite score is computed per framework first, then a single overall composite is derived as the maximum composite across all frameworks. This prevents a weak cross-framework signal from pulling down a strong single-framework signal.

#### 3.1.3 Signal Strength Classification

| Range | Classification |
|-------|----------------|
| ≥ 0.65 | `strong` |
| 0.45 – 0.64 | `moderate` |
| 0.25 – 0.44 | `weak` |
| < 0.25 | `none` |

Signal strength is informational — it does not gate passage to Pass 2. A KSA with signal strength `none` still proceeds to the LLM evaluation.


#### 3.1.4 Top Anchor Identification

For each framework, identify the top-scoring element (the framework work role or work element that scored highest against this KSA). Across all frameworks, collect up to the top 3 anchors by composite score. These are recorded in the `top_anchors` array and serve as grounding context for the Pass 2 LLM agent.

#### 3.1.5 Pass 1 Output Contract

The Pass 1 output is a structured dict, not a decision. It must contain:
- `composite_score`: float, 0.0–1.0
- `signal_strength`: one of `strong`, `moderate`, `weak`, `none`
- `framework_scores`: dict keyed by framework name, each containing per-metric values and top element
- `top_anchors`: list of up to 3 dicts with framework, element_id, element_label, and score
- `metrics_used`: list of metric names that had values
- `metrics_absent`: list of metric names that were null or missing

Pass 1 must never fail silently. If no STRM data exists for this KSA at all, the composite score is 0.0, signal strength is `none`, framework_scores is empty, and top_anchors is empty. This is a valid state — it means STRM has no information about this KSA, not that the KSA is irrelevant.

---

### 3.2 Pass 2 — LLM Evaluation Agent

**Type:** LLM agent  
**Model:** `claude-sonnet-4-5`  
**Temperature:** 0  
**Script:** `scripts/agents.py`  
**Inputs:** Role description, role name, role category, KSA text, KSA dimension, KSA domain, Pass 1 score block  
**Outputs:** Structured evaluation with preliminary decision and full rationale

#### 3.2.1 Agent Responsibilities

The Pass 2 agent makes the first intelligent include/exclude determination. It receives the full Pass 1 block as context and is expected to use it — specifically the composite score, signal strength, and top anchors — but is not bound by it. A KSA with `signal_strength: none` can still be included if the agent's reasoning supports it.

The agent must evaluate four dimensions and document each explicitly:

**Scope fit:** Does this KSA describe a competency that belongs within the functional scope of this role? A Data Engineer role and a Privacy Compliance role may both touch data, but the nature and ownership of the competency differs. The agent must determine whether the KSA's subject matter is in-scope for this role's primary function, not merely adjacent to it.

**Seniority fit:** Does the level of the KSA (foundational knowledge vs. advanced practitioner judgment vs. strategic leadership) match the expected seniority level of this work role? A task KSA written for an individual contributor is not appropriate for a CDAIO role, even if the subject matter overlaps.

**Semantic accuracy:** Does the STRM signal reflect genuine semantic alignment, or does the score inflate due to shared terminology without shared meaning? The agent must explicitly assess whether the top anchors represent genuine alignment or surface-level keyword overlap. This assessment must be documented in the rationale — it cannot be implied.

**Preliminary decision:** `include` or `exclude`. No abstentions. No partial decisions. The decision must follow from the three prior assessments.

#### 3.2.2 Rationale Requirements

The rationale field is not optional and is not satisfied by a single sentence. A valid rationale must:
- State the basis for the scope fit assessment
- State the basis for the seniority fit assessment
- Acknowledge the STRM signal and explain whether it supported or complicated the decision
- Name the specific reason for the include or exclude determination

Vague rationale examples that are **not acceptable:**
- "This KSA is relevant to the role."
- "The STRM score is moderate, suggesting some alignment."
- "This competency does not appear to be required."

If the agent returns a rationale that does not meet these criteria, the pipeline must retry the prompt with an explicit validation error before proceeding.

#### 3.2.3 Structured Output

Pass 2 output must be machine-parseable. The agent must return a JSON block conforming to the `pass_2_evaluation` schema (see Section 4). The implementation must validate the output structure before proceeding to Pass 3. If the output cannot be parsed as valid JSON with the required fields, retry up to 2 times before failing the evaluation for this pair and flagging it as requiring manual review.

---

### 3.3 Pass 3 — Adversarial Agent 1 (Internal Consistency Challenge)

**Type:** LLM agent  
**Model:** `claude-sonnet-4-5`  
**Temperature:** 0.1  
**Script:** `scripts/agents.py`  
**Inputs:** Role context (description, name, category, a list of KSAs already marked `include` for this role in this run), the current KSA, the Pass 2 decision and rationale  
**Outputs:** `upheld` or `overturned`, with explicit challenge reasoning


#### 3.3.1 Challenge Mandate

Pass 3 is not a rubber stamp. The agent is instructed to actively challenge the Pass 2 decision. Its role is not to re-evaluate from scratch but to find fault with the reasoning provided. The agent's prompt must frame the task as adversarial: *assume the Pass 2 decision may be wrong and find the strongest argument against it.*

The four specific challenges the Pass 3 agent must attempt:

**Seniority calibration consistency:** Is the seniority boundary being applied the same way here as it is for other KSAs already included for this role? If Pass 2 included a high-level strategic KSA earlier in the run and is now excluding a similar one on seniority grounds (or vice versa), Pass 3 must flag this inconsistency. This requires the agent to have visibility into the already-included KSA list for the current role.

**Scope boundary consistency:** Is the scope definition being applied uniformly? If Pass 2 drew the scope boundary at one level of abstraction for previously evaluated KSAs, it must apply the same boundary here.

**Practitioner recognition test:** Would a senior practitioner actively working in this role immediately recognize this competency as genuinely required? If the answer is yes and Pass 2 excluded it, that is a strong signal to overturn.

**Rationale integrity check:** Is the Pass 2 rationale self-consistent? Does it rely on surface-level pattern matching (e.g., "the word 'data' appears in both") rather than genuine functional analysis?

#### 3.3.2 Outcome Requirements

Pass 3 must return one of:
- `upheld`: The agent agrees with Pass 2. The challenge field documents what was checked and why it did not produce an overturn.
- `overturned`: The agent disagrees with Pass 2. The challenge field documents the specific inconsistency or failure found.

If `overturned`, the pipeline must trigger a rebuttal step: the Pass 2 agent receives the Pass 3 challenge and produces a rebuttal and a final ruling. This final ruling supersedes the original Pass 2 preliminary decision and is recorded in `pass_3_adversarial_internal.ruling`.

The rebuttal step follows the same output validation requirements as Pass 2: must parse as JSON, must contain an explicit ruling (`include` or `exclude`) and a substantive rebuttal.

#### 3.3.3 Known-Included KSA List

The Pass 3 agent requires a list of KSAs already marked `include` for this role in the current run. This list is maintained in memory as the pipeline processes KSAs sequentially for a given role. It does not need to be persisted to disk between sessions (it can be reconstructed by scanning existing artifacts on resume). The list should include the KSA id, KSA text (abbreviated), and the dimension of each included KSA to give the consistency checker enough context to detect calibration drift.

---

### 3.4 Pass 4 — Adversarial Agent 2 (External Ground Truth Challenge)

**Type:** LLM agent with optional web search  
**Model:** `claude-sonnet-4-5`  
**Temperature:** 0.1  
**Script:** `scripts/agents.py`  
**Inputs:** Role context, KSA text and domain, Pass 2 decision, Pass 3 outcome  
**Outputs:** `upheld` or `overturned`, with source-grounded reasoning

#### 3.4.1 Challenge Mandate

Pass 4 operates independently of Pass 3. It does not inherit Pass 3's conclusion — it challenges the Pass 2 decision directly using external reference points. The agent's task is to assess whether the decision is consistent with how the real-world industry and practitioner community understand this role.

The four specific ground truth checks the Pass 4 agent must attempt:

**Job posting signal:** Do job postings for this role title (or closely equivalent titles) regularly mention this competency or skill area? Absence of this competency from job postings for a senior role is meaningful evidence for exclusion. Consistent presence is meaningful evidence for inclusion.

**Practitioner self-report signal:** Do practitioners who hold or have held this role (as observable from professional profiles, conference talks, published writing, or community discussions) report needing or using this competency?

**Standards body signal:** Does the relevant standards body or certification framework for this domain include this competency in their definition of the role? Relevant bodies include NIST (for cybersecurity/data roles), ISACA, DAMA, CDAIO Program bodies, and relevant certification frameworks (CISSP, CISM, CDMP, etc.). The agent should be specific — name the framework and, if possible, the section or competency reference.

**Gap analysis:** If this KSA were excluded from the role's profile, would a practitioner in this role notice a meaningful gap? Would they say "yes, I use this regularly" or "no, that's someone else's job"?

#### 3.4.2 Web Search Integration

Pass 4 should use web search capability where available. When web search is enabled, the agent is expected to execute at least one targeted search to ground its external challenge. The search should target job postings, professional role definitions, or standards body documents — not generic background information.

When web search is not available or returns no useful results, the agent must fall back to its training knowledge and document this limitation explicitly in the evidence field. An agent that cannot find external evidence must say so, not fabricate it.


#### 3.4.3 Outcome Requirements

Pass 4 must return `upheld` or `overturned` with explicit evidence. The `evidence` field must cite at least one named source — a job title pattern, a standards body, a framework, or a practitioner community. It must not be a restatement of the KSA or role description.

---

### 3.5 Final Decision Logic

After all four passes complete, the pipeline computes the final decision using the following rules. These rules are deterministic — they are not re-evaluated by another agent.

```
adversarial_disagreements = count of passes 3 and 4 that returned "overturned"

if adversarial_disagreements == 0:
    final_decision = pass_2_preliminary_decision
    (or pass_3_ruling if pass_3 overturned and rebuttal resolved it)
    decision_confidence = "high"

if adversarial_disagreements == 1:
    # One overturned, one upheld
    # The evaluation agent (Pass 2 agent) makes a final ruling
    # This ruling is documented in decision_rationale
    decision_confidence = "medium"

if adversarial_disagreements == 2:
    # Both adversarial passes overturned the Pass 2 decision
    # The evaluation agent must reverse the Pass 2 decision
    # OR provide extraordinary documented justification for holding it
    # If reversed: final_decision changes, confidence = "low" is acceptable
    # If held despite both overturns: confidence = "low", and decision_rationale
    #   must explicitly address both challenges and explain why they were rejected
    decision_confidence = "low"
```

The `adversarial_disagreements` count in the artifact is the raw count of overturns (0, 1, or 2) before the final ruling. It records what the adversarial agents found, not what the final decision was.

---

## 4. Data Schemas

### 4.1 KSA Evaluation Artifact (`{ksa_id}.json`)

One artifact per role-KSA pair. 199,903 total. This is the atomic unit of the entire pipeline.

```json
{
  "schema_version": "2.0",
  "role_id": "WIDAI-ENG-0028",
  "role_name": "Data Engineer",
  "ksa_id": "DA-K-013",
  "ksa_text": "Knowledge of data pipeline design patterns and orchestration frameworks.",
  "ksa_dimension": "Knowledge",
  "ksa_domain": "DA",

  "pass_1_scoring": {
    "composite_score": 0.6359,
    "signal_strength": "strong",
    "framework_scores": {
      "dcwf": {
        "composite": 0.6359,
        "cross_encoder_sts": 0.71,
        "bertscore": 0.62,
        "nli_score": 0.58,
        "bi_encoder_cosine": 0.66,
        "jaccard": 0.43,
        "top_element_id": "WR624",
        "top_element_label": "Data Engineer"
      },
      "ddat": {
        "composite": 0.5812,
        "cross_encoder_sts": 0.64,
        "bertscore": 0.59,
        "nli_score": 0.54,
        "bi_encoder_cosine": 0.61,
        "jaccard": 0.38,
        "top_element_id": "DDAT-DE-2",
        "top_element_label": "Data Engineer (DDaT)"
      }
    },
    "top_anchors": [
      {
        "framework": "dcwf",
        "element_id": "WR624",
        "element_label": "Data Engineer",
        "score": 0.6359
      },
      {
        "framework": "ddat",
        "element_id": "DDAT-DE-2",
        "element_label": "Data Engineer (DDaT)",
        "score": 0.5812
      }
    ],
    "metrics_used": ["cross_encoder_sts", "bertscore", "nli_score", "bi_encoder_cosine", "jaccard"],
    "metrics_absent": []
  },

  "pass_2_evaluation": {
    "scope_fit": "in_scope",
    "seniority_fit": "appropriate",
    "preliminary_decision": "include",
    "rationale": "Pipeline design patterns and orchestration are core to the Data Engineer role. The STRM signal is strong with genuine semantic alignment across both DCWF and DDaT frameworks, not surface-level keyword overlap. The seniority level is appropriate — this is practitioner-level technical knowledge, not foundational or executive. Scope is clearly within the data engineering function."
  },

  "pass_3_adversarial_internal": {
    "outcome": "upheld",
    "challenge": "Examined seniority calibration against 12 previously included KSAs for this role. Pipeline orchestration knowledge is consistent with the technical depth already established. Scope boundary is being applied uniformly — this is not a boundary case. Rationale does not rely on surface-level pattern matching.",
    "rebuttal": null,
    "ruling": "include"
  },

  "pass_4_adversarial_external": {
    "outcome": "upheld",
    "challenge": "Reviewed external alignment. Job postings for Data Engineer roles consistently list orchestration tools (Airflow, Prefect, Dagster) as required. DAMA DMBOK2 includes pipeline design as a core data integration competency. DDaT framework explicitly names this competency at the practitioner level.",
    "evidence": "DAMA DMBOK2 Chapter 8 (Data Integration and Interoperability); DDaT Data Engineer role definition; common job posting patterns across major job boards.",
    "ruling": "include"
  },

  "final_decision": "include",
  "decision_confidence": "high",
  "decision_rationale": "All four passes aligned on include. Strong STRM signal confirmed as genuine. Internal consistency check passed. External ground truth confirms this as a standard Data Engineer competency in both practitioner and standards contexts.",
  "adversarial_disagreements": 0,

  "metadata": {
    "evaluated_at": "2026-04-06T14:23:11Z",
    "model": "claude-sonnet-4-5",
    "pipeline_version": "1.0"
  }
}
```


### 4.2 Field Constraints and Validation Rules

The following constraints apply to all artifact fields. The `artifact_writer.py` module must validate these before writing. Any artifact that fails validation must be flagged and not written — the pipeline should log the failure and mark the pair for retry, not write a malformed artifact.

| Field | Type | Constraints |
|-------|------|-------------|
| `schema_version` | string | Must be `"2.0"` |
| `role_id` | string | Must match pattern `WIDAI-[A-Z]+-[0-9]+` |
| `ksa_id` | string | Must exist in ksa_catalog |
| `ksa_dimension` | string | One of: `Knowledge`, `Skills`, `Abilities`, `Tasks` |
| `pass_1_scoring.composite_score` | float | 0.0 – 1.0 inclusive |
| `pass_1_scoring.signal_strength` | string | One of: `strong`, `moderate`, `weak`, `none` |
| `pass_2_evaluation.scope_fit` | string | One of: `in_scope`, `out_of_scope`, `edge_case` |
| `pass_2_evaluation.seniority_fit` | string | One of: `appropriate`, `too_senior`, `too_junior` |
| `pass_2_evaluation.preliminary_decision` | string | One of: `include`, `exclude` |
| `pass_2_evaluation.rationale` | string | Length > 50 characters (enforces substance) |
| `pass_3_adversarial_internal.outcome` | string | One of: `upheld`, `overturned` |
| `pass_3_adversarial_internal.ruling` | string | One of: `include`, `exclude` |
| `pass_4_adversarial_external.outcome` | string | One of: `upheld`, `overturned` |
| `pass_4_adversarial_external.ruling` | string | One of: `include`, `exclude` |
| `final_decision` | string | One of: `include`, `exclude` |
| `decision_confidence` | string | One of: `high`, `medium`, `low` |
| `decision_rationale` | string | Length > 50 characters |
| `adversarial_disagreements` | int | 0, 1, or 2 |
| `metadata.evaluated_at` | string | Valid ISO 8601 timestamp |
| `metadata.model` | string | Non-empty |

---

### 4.3 Role Summary Schema (`summary.json`)

One summary per role. Written after all 1,069 KSA artifacts for that role are complete.

```json
{
  "schema_version": "2.0",
  "role_id": "WIDAI-ENG-0028",
  "role_name": "Data Engineer",
  "category_code": "ENG",
  "evaluated_at": "2026-04-06T16:44:02Z",
  "total_evaluated": 1069,
  "included": 87,
  "excluded": 982,
  "inclusion_rate": 0.0814,
  "confidence_breakdown": {
    "high": 71,
    "medium": 12,
    "low": 4
  },
  "domain_breakdown": {
    "DA": {
      "included": 14,
      "excluded": 35,
      "avg_score_included": 0.671,
      "avg_score_excluded": 0.238
    },
    "SEC": {
      "included": 8,
      "excluded": 62,
      "avg_score_included": 0.544,
      "avg_score_excluded": 0.181
    }
  },
  "dimension_breakdown": {
    "Knowledge": { "included": 41, "excluded": 268 },
    "Skills": { "included": 28, "excluded": 184 },
    "Abilities": { "included": 12, "excluded": 103 },
    "Tasks": { "included": 6, "excluded": 427 }
  },
  "score_distribution": {
    "avg_composite_included": 0.623,
    "avg_composite_excluded": 0.198,
    "score_gap": 0.425
  },
  "adversarial_summary": {
    "pass3_overturns": 3,
    "pass4_overturns": 2,
    "both_overturned": 1,
    "final_reversals": 1
  },
  "strm_coverage": ["dcwf", "ddat"],
  "strm_gap_notes": "No DAMA, Evidence Act, or CDAIO-specific frameworks present in STRM data. KSAs from governance and AI strategy domains evaluated on LLM reasoning alone with no STRM signal backing.",
  "pipeline_version": "1.0"
}
```

**Notes on summary computation:**

The `score_gap` between included and excluded KSAs is a signal of pipeline calibration health. A large gap (> 0.3) suggests the scoring signal is meaningfully separating relevant from irrelevant. A small gap (< 0.15) suggests the LLM agents are making decisions largely independent of the STRM signal, which may indicate STRM coverage gaps for this role's domain. The `strm_gap_notes` field should document this when notable.

The `adversarial_summary.final_reversals` count is the number of cases where both adversarial agents overturned Pass 2 and the final decision was changed as a result. This is a quality signal: a high reversal rate (> 5% of included decisions) may indicate the Pass 2 agent's calibration needs adjustment.


### 4.4 Role-Category Mapping Schema (`mappings/role_ksa_{category}.json`)

Generated from the completed artifact corpus after all roles in a category are evaluated. One file per category code (e.g., `role_ksa_ENG.json`, `role_ksa_GOV.json`).

```json
{
  "schema_version": "2.0",
  "category_code": "ENG",
  "generated_at": "2026-04-06T18:00:00Z",
  "roles": [
    {
      "role_id": "WIDAI-ENG-0028",
      "role_name": "Data Engineer",
      "included_ksas": [
        {
          "ksa_id": "DA-K-013",
          "ksa_text": "Knowledge of data pipeline design patterns...",
          "ksa_dimension": "Knowledge",
          "ksa_domain": "DA",
          "composite_score": 0.6359,
          "decision_confidence": "high"
        }
      ]
    }
  ]
}
```

The mapping file contains only `include` decisions. It is a derived artifact — it must never be manually edited. If a role evaluation is reprocessed, the relevant mapping file must be regenerated from the artifact corpus.

---

### 4.5 ROADMAP.md Schema

Auto-generated. Updated after each role completes. Not a manual file.

```markdown
# WIDAI Role-KSA Evaluation — Progress Roadmap
Generated: 2026-04-06T18:00:00Z
Pipeline Version: 1.0

## Summary
- Total roles: 187
- Complete: 24 (12.8%)
- In-progress: 1
- Pending: 162

## Role Status

| Role ID | Role Name | Category | Status | KSAs Evaluated | Included | Inc. Rate | Pass3 Overturns | Pass4 Overturns |
|---------|-----------|----------|--------|----------------|----------|-----------|-----------------|-----------------|
| WIDAI-ENG-0028 | Data Engineer | ENG | complete | 1069 | 87 | 8.1% | 3 | 2 |
| WIDAI-ENG-0031 | Data Architect | ENG | complete | 1069 | 94 | 8.8% | 1 | 4 |
| WIDAI-GOV-0012 | Privacy Officer | GOV | in-progress | 412 | 38 | — | — | — |
| WIDAI-GOV-0013 | Compliance Manager | GOV | pending | — | — | — | — | — |
```

---

## 5. File and Directory Layout

### 5.1 Complete Directory Structure

```
widai-dataset/
│
├── data/
│   ├── widai_roles.json                    ← Source: 187 WIDAI work roles
│   ├── ksa_catalog.json                    ← Source: 1,069 KSAs
│   ├── strm_mapping.json                   ← STRM data, consolidated (if present)
│   └── strm/                               ← STRM data, per-framework (if present)
│       ├── dcwf.json
│       ├── ddat.json
│       └── {framework}.json
│
├── docs/
│   ├── ROLE_KSA_PIPELINE_ARCHITECTURE.md   ← This document
│   └── role_ksa_evaluations/
│       ├── ROADMAP.md                      ← Auto-generated progress tracker
│       ├── WIDAI-ENG-0028/
│       │   ├── summary.json                ← Written after all 1,069 artifacts done
│       │   ├── DA-K-013.json               ← One artifact per KSA
│       │   ├── DA-K-014.json
│       │   └── ... (1,069 files total per role)
│       ├── WIDAI-ENG-0031/
│       │   ├── summary.json
│       │   └── ... (1,069 files)
│       └── ... (187 role directories total)
│
├── mappings/
│   ├── role_ksa_ENG.json                   ← Generated: all ENG roles, include-only
│   ├── role_ksa_GOV.json
│   └── role_ksa_{category}.json
│
├── scripts/
│   ├── evaluate_role_ksas.py               ← Main entry point / orchestrator
│   ├── evaluation_config.py                ← Weights, model config, prompt templates
│   ├── scoring.py                          ← Pass 1: pure Python scoring
│   ├── agents.py                           ← Pass 2/3/4: LLM agent implementations
│   └── artifact_writer.py                  ← Artifact writing, validation, summaries
│
└── logs/
    ├── evaluation_20260406_142311.log       ← Per-run log
    └── evaluation_20260407_091500.log
```

### 5.2 File Naming Conventions

**Artifact files:** Named by KSA id exactly as it appears in `ksa_catalog.json`. If KSA ids contain characters invalid for filenames (e.g., `/`), substitute with `_`. The mapping between filename and KSA id must be deterministic and documented in `evaluation_config.py`.

**Log files:** Named `evaluation_{YYYYMMDD}_{HHMMSS}.log`. One per invocation of `evaluate_role_ksas.py`. Logs are never overwritten.

**Summary files:** Named `summary.json` within the role directory. The presence of this file is the canonical signal that a role's evaluation is complete.

### 5.3 File Integrity Rules

- Artifact files are written atomically. Write to a `.tmp` file, validate, then rename. If validation fails, the `.tmp` file is deleted and the failure is logged. The target `.json` file is never written in an invalid state.
- `summary.json` is written only after all 1,069 KSA artifacts for the role have been successfully written and validated.
- `ROADMAP.md` is regenerated from the artifact corpus state at the end of each role's completion — not incrementally updated per-KSA to avoid partial writes.
- `mappings/role_ksa_{category}.json` is regenerated when explicitly requested or at the end of a full `--all` run. It is derived, not primary.

---

## 6. Script Architecture and Responsibilities

### 6.1 `evaluate_role_ksas.py` — Main Orchestrator

**Responsibility:** Entry point. Parses CLI arguments, loads source data, determines which roles and KSAs need processing, drives the per-role and per-KSA loops, handles top-level error recovery.

**CLI interface:**

```
python scripts/evaluate_role_ksas.py [OPTIONS]

Options:
  --role ROLE_ID        Process a single role (e.g., WIDAI-ENG-0028)
  --all                 Process all 187 roles sequentially
  --status              Print completion state and exit (no evaluation)
  --reprocess ROLE_ID   Force reprocess role even if summary.json exists

Examples:
  python scripts/evaluate_role_ksas.py --role WIDAI-ENG-0028
  python scripts/evaluate_role_ksas.py --all
  python scripts/evaluate_role_ksas.py --status
  python scripts/evaluate_role_ksas.py --reprocess WIDAI-GOV-0012
```

**Processing loop (pseudocode):**

```python
def process_role(role):
    role_dir = get_role_dir(role.id)
    
    if summary_exists(role_dir) and not reprocess_flag:
        log(f"Role {role.id} already complete, skipping")
        return
    
    ksa_list = load_ksa_catalog()
    completed_ksas = get_completed_artifacts(role_dir)
    pending_ksas = [k for k in ksa_list if k.id not in completed_ksas]
    
    log(f"Role {role.id}: {len(completed_ksas)} done, {len(pending_ksas)} pending")
    
    included_so_far = load_included_ksas_from_artifacts(role_dir)  # for Pass 3
    
    for ksa in pending_ksas:
        artifact = run_4_pass_pipeline(role, ksa, included_so_far)
        write_artifact(role_dir, ksa.id, artifact)
        if artifact.final_decision == "include":
            included_so_far.append(ksa)
    
    summary = compute_summary(role, role_dir)
    write_summary(role_dir, summary)
    regenerate_roadmap()
```

**--status behavior:** Scans `docs/role_ksa_evaluations/` for all role directories. For each, checks for `summary.json` (complete), counts artifact files (in-progress), or notes absence (pending). Outputs a formatted status table and exits without performing any evaluation.

**--reprocess behavior:** Deletes the existing `summary.json` for the specified role (but does NOT delete existing KSA artifacts). Resumes from the last incomplete KSA. Use when you want to force regeneration of the summary or when new KSAs have been added to the catalog.

---

### 6.2 `evaluation_config.py` — Configuration and Prompt Templates

**Responsibility:** Single source of truth for all tunable parameters, model settings, scoring weights, and prompt templates. No agent or scoring code should contain hardcoded weights, model names, or prompts — all of these live here.

**Contents:**

```python
# Model configuration
LLM_MODEL = "claude-sonnet-4-5"
PASS_2_TEMPERATURE = 0.0
PASS_3_TEMPERATURE = 0.1
PASS_4_TEMPERATURE = 0.1
MAX_RETRIES_PER_PASS = 2

# Scoring weights (must sum to 1.0 when all metrics present)
METRIC_WEIGHTS = {
    "cross_encoder_sts": 0.40,
    "bertscore": 0.20,
    "nli_score": 0.20,
    "bi_encoder_cosine": 0.15,
    "jaccard": 0.05,
}

# Signal strength thresholds
SIGNAL_THRESHOLDS = {
    "strong": 0.65,
    "moderate": 0.45,
    "weak": 0.25,
    # below 0.25 = "none"
}

# KSA filename sanitization map (if KSA ids contain invalid filename chars)
KSA_ID_SANITIZE = {"/": "_"}

# Prompt templates (see below)
PROMPT_PASS_2 = """..."""
PROMPT_PASS_3 = """..."""
PROMPT_PASS_3_REBUTTAL = """..."""
PROMPT_PASS_4 = """..."""
PROMPT_FINAL_RULING = """..."""
```

**Prompt template requirements:**

Each prompt template must include clearly labeled placeholders for all variable inputs. Templates must instruct the model to return JSON conforming to the relevant schema section. Templates must explicitly state the decision constraint (must return include or exclude, not ambiguous language). Templates must be versioned alongside the pipeline version in `schema_version`.

---

### 6.3 `scoring.py` — Pass 1 Python Scoring

**Responsibility:** Implement the Pass 1 scoring logic. No LLM calls. No network calls. Pure Python.

**Public interface:**

```python
def score_ksa_for_role(ksa_id: str, role_id: str, strm_data: dict) -> dict:
    """
    Returns a Pass 1 score block as a dict conforming to the pass_1_scoring schema.
    Never raises on missing data — returns empty/zero values with notes.
    """
```

**Internal logic:**

1. Look up all STRM entries for `ksa_id` across all frameworks in `strm_data`.
2. For each framework, extract all available metrics. Track which are present and which are absent.
3. Compute per-framework composite using renormalized weights.
4. Identify top element per framework (highest composite element, with id and label).
5. Compute overall composite as the max across framework composites.
6. Classify signal strength against thresholds from `evaluation_config.py`.
7. Collect top 3 anchors across frameworks by composite score.
8. Return fully populated score block dict.

**Error handling:** If `ksa_id` is not found in `strm_data` at all, return a valid score block with `composite_score: 0.0`, `signal_strength: "none"`, `framework_scores: {}`, `top_anchors: []`, and a note in `metrics_absent` that STRM data was entirely absent. Do not raise. Do not return `None`.

---

### 6.4 `agents.py` — LLM Agent Implementations

**Responsibility:** Implement all three LLM agent passes (Pass 2, Pass 3, Pass 4) and the rebuttal step. Handle prompt construction, API calls, response parsing, validation, and retry logic.

**Public interface:**

```python
def run_pass_2(role: dict, ksa: dict, pass_1_block: dict) -> dict:
    """Returns pass_2_evaluation dict or raises EvaluationError after retries."""

def run_pass_3(role: dict, ksa: dict, pass_2_result: dict,
               included_ksas: list) -> dict:
    """Returns pass_3_adversarial_internal dict or raises EvaluationError."""

def run_pass_3_rebuttal(role: dict, ksa: dict, pass_2_result: dict,
                        pass_3_challenge: str) -> dict:
    """Returns updated pass_3 dict with rebuttal and final ruling."""

def run_pass_4(role: dict, ksa: dict, pass_2_result: dict,
               pass_3_result: dict) -> dict:
    """Returns pass_4_adversarial_external dict or raises EvaluationError."""
```

**Retry logic:** Each pass attempts up to `MAX_RETRIES_PER_PASS` (from config) on JSON parse failure or schema validation failure. On the retry prompt, include the validation error explicitly so the model can self-correct. If all retries fail, raise `EvaluationError` with the role id, KSA id, pass number, and last response. The orchestrator catches this, logs the failure, and marks the pair as requiring manual review in a separate failures log.

**Web search for Pass 4:** If a web search tool is available in the API session, Pass 4 should be invoked with tool use enabled. The agent prompt must instruct the agent to perform at least one search before formulating its external challenge. If web search is not configured, Pass 4 runs without it and the `evidence` field must note this.


### 6.5 `artifact_writer.py` — Artifact Writing, Validation, and Summaries

**Responsibility:** Assemble the final artifact dict from all four pass outputs, validate it against the schema, write it atomically to disk. Also computes and writes `summary.json` and generates mapping files.

**Public interface:**

```python
def write_artifact(role_dir: str, ksa_id: str, artifact: dict) -> None:
    """
    Validates artifact against schema, writes atomically.
    Raises ArtifactValidationError if validation fails (does not write).
    """

def compute_summary(role: dict, role_dir: str) -> dict:
    """
    Reads all KSA artifacts in role_dir, computes aggregated stats,
    returns summary dict conforming to role summary schema.
    """

def write_summary(role_dir: str, summary: dict) -> None:
    """Writes summary.json. Called only after all KSA artifacts are written."""

def generate_mapping_file(category_code: str, roles: list, output_path: str) -> None:
    """
    Reads all artifacts for all roles in category, extracts include decisions,
    writes role_ksa_{category}.json.
    """

def regenerate_roadmap(evaluations_dir: str) -> None:
    """
    Scans all role directories for completion state,
    writes ROADMAP.md to evaluations_dir root.
    """
```

**Atomic write pattern:**

```python
def write_artifact(role_dir, ksa_id, artifact):
    validate_artifact(artifact)  # raises on failure, nothing written
    
    target_path = os.path.join(role_dir, sanitize_filename(ksa_id) + ".json")
    tmp_path = target_path + ".tmp"
    
    with open(tmp_path, 'w') as f:
        json.dump(artifact, f, indent=2)
    
    # Validate the written file can be read back cleanly
    with open(tmp_path, 'r') as f:
        round_trip = json.load(f)
    validate_artifact(round_trip)
    
    os.rename(tmp_path, target_path)  # atomic on POSIX
```

**Summary computation:** Iterates over all `{ksa_id}.json` files in the role directory. For each, reads the `final_decision`, `decision_confidence`, `pass_1_scoring.composite_score`, `ksa_domain`, `ksa_dimension`, and adversarial outcome fields. Aggregates into the summary structure. Does not re-run any evaluation — purely a read-aggregate-write operation.

---

## 7. Resumability and Fault Tolerance

### 7.1 Design Principle

The pipeline must treat every interruption — whether from a network timeout, API rate limit, process kill, power loss, or manual stop — as a normal operating condition, not an error state. The pipeline should be safe to stop and restart at any point without data loss or duplication. This is not an edge case concern; at 800,000 agent operations over days or weeks, interruption is the expected norm.

### 7.2 Resume Decision Hierarchy

The resume logic operates at three levels, checked in order:

**Level 1 — Role complete:** If `docs/role_ksa_evaluations/{role_id}/summary.json` exists, the role is complete. Skip it entirely unless `--reprocess` is specified.

**Level 2 — Role partially complete:** If the role directory exists but `summary.json` does not, the role was interrupted mid-run. Scan the directory for existing `{ksa_id}.json` files. Build the set of completed KSA ids. Resume from the first KSA in the catalog that does not have a completed artifact.

**Level 3 — Role not started:** Role directory does not exist. Create it and start from the first KSA.

**Important:** Resume at Level 2 must also reconstruct the `included_so_far` list for Pass 3 consistency checking. This is done by reading all completed artifacts in the role directory and collecting those with `final_decision: "include"`. This reconstruction is identical to what would have been in memory during the original run.

### 7.3 Partial Artifact Detection

An artifact is considered complete only if:
1. The file exists at the expected path (not a `.tmp` file)
2. It can be loaded as valid JSON
3. It passes schema validation (all required fields present with valid values)

On resume, the pipeline should run a quick validation pass over completed artifacts rather than trusting file existence alone. If a completed artifact fails validation (corrupted write, schema mismatch), treat the pair as incomplete and re-evaluate.

### 7.4 Interruption Safety

- No state is held only in memory across role boundaries. All progress is on disk.
- Within a role's KSA loop, each KSA's artifact is written to disk before the next KSA begins.
- The `included_so_far` list is always reconstructable from disk — it is never the only copy.
- Log files are opened in append mode. A crashed run's log remains intact and is not overwritten on resume.

### 7.5 Rate Limiting and Backoff

The API will return rate limit errors under sustained load. The implementation must handle these gracefully:

- On any API rate limit error (429 or equivalent), wait with exponential backoff before retry: 60s, 120s, 240s, 480s.
- After 4 consecutive rate limit failures for a single KSA, log the failure, skip the KSA (do not write an artifact), and continue to the next. The skipped KSA will be picked up on the next run.
- On non-rate-limit API errors (500, timeout), retry up to `MAX_RETRIES_PER_PASS` times with a 30s fixed wait. If all retries fail, the same skip-and-continue behavior applies.

Skipped KSAs must be logged clearly with role id, KSA id, pass number, and error type. A post-run report of all skipped pairs should appear in the run log summary.

### 7.6 Log Structure

Each run log (`logs/evaluation_{timestamp}.log`) must contain:

- Run start: timestamp, CLI arguments, total roles/KSAs to process
- Per-role start: role id, role name, pending count, resumed-from state
- Per-KSA completion: role id, KSA id, final decision, confidence, adversarial disagreements, elapsed time for this KSA
- Per-KSA failures: role id, KSA id, pass number, error type, retry count
- Per-role completion: role id, total evaluated, included count, inclusion rate, adversarial overturn counts
- Run summary: total KSAs processed, total failures, total time elapsed, roles completed this run

Log lines must be structured (JSON Lines format preferred) to enable programmatic parsing for post-run analysis.

---

## 8. Scale and Runtime Expectations

### 8.1 Volume

| Dimension | Count |
|-----------|-------|
| Work roles | 187 |
| KSAs | 1,069 |
| Role-KSA pairs (evaluations) | 199,903 |
| Passes per evaluation | 4 |
| Total agent operations | ~800,000 |
| Artifact files generated | 199,903 KSA artifacts + 187 summaries |
| Approximate artifact corpus size | ~3–5 GB (at ~15–25 KB per artifact) |

### 8.2 Runtime Estimates

Runtime depends heavily on API throughput, rate limits, and whether Pass 4 uses web search (which adds latency per call). The estimates below assume sequential processing with no parallelism.

| Scenario | Estimated time per KSA | Estimated total runtime |
|----------|------------------------|------------------------|
| Pass 4 without web search | 8–15 seconds | 18–33 days |
| Pass 4 with web search | 15–30 seconds | 35–70 days |
| With moderate rate limiting | Add 20–40% | — |

**These estimates are informational.** Time to completion is explicitly not a quality constraint for this pipeline. The correct operating model is: start the pipeline, let it run, resume as needed. A run that completes in 60 days with 199,903 high-quality artifacts is strictly better than a run that completes in 5 days with filtered, unauditable results.

### 8.3 Parallelism Considerations

The current design is intentionally sequential within a role. This is because Pass 3 depends on the `included_so_far` list, which grows as KSAs are processed in order. Parallelizing KSAs within a role would require either:
- Pre-loading the list from a previous complete run (not possible for first runs)
- Running Pass 3 without consistency context (degrades quality)
- A two-phase approach: run Passes 1–2 in parallel, then run Passes 3–4 sequentially

The two-phase approach is the recommended path if parallelism is needed in a future iteration. It is not in scope for the initial implementation.

**Roles can be parallelized.** Different roles are fully independent. If multiple API keys or separate processes are used, roles can be distributed across workers. The artifact directory structure and file naming are already compatible with concurrent multi-role processing, as long as each role is owned by exactly one worker at a time.

### 8.4 Storage Requirements

At approximately 20 KB per artifact (average JSON size with full rationale text), the corpus is:
- 199,903 artifacts × 20 KB ≈ 3.8 GB for KSA artifacts
- 187 summaries × ~5 KB ≈ 1 MB for summaries
- Total: approximately 4 GB

This is comfortably within the capacity of any modern filesystem. No special storage architecture is required. Standard filesystem I/O is appropriate.

### 8.5 API Cost Estimates

Each evaluation involves approximately:
- Pass 2: ~1,500 input tokens, ~400 output tokens
- Pass 3: ~2,000 input tokens (includes context), ~400 output tokens
- Pass 4: ~2,500 input tokens, ~500 output tokens
- Rebuttals (estimated ~15% of Pass 3): ~2,000 input, ~400 output

Approximate tokens per evaluation: ~8,000–12,000 input, ~1,500–2,000 output.  
Approximate total tokens: 1.6–2.4 billion input, 300–400 million output.

These are rough estimates. Actual costs will vary based on prompt length, rationale verbosity, and web search usage. A pilot run of a single role (1,069 evaluations) should be used to calibrate actual costs before committing to the full `--all` run.

---

## 9. Quality Guarantees

This section documents what the pipeline is specifically designed to catch and prevent, with reference to the failure modes of the previous approach.

### 9.1 What the Previous Approach Got Wrong

The previous pipeline used a candidate generation query to pre-filter KSAs before any LLM evaluation occurred. The failure was architectural: the filtering step was making consequential quality decisions — "this KSA is not worth evaluating for this role" — without any intelligent reasoning, without any documentation, and without any mechanism to review or challenge what was filtered out.

This created a category of silent error with no upper bound. Every KSA that was filtered out before evaluation is an unknown unknown. There is no way to determine, post-hoc, whether any given filtered KSA was correctly excluded or was a genuine false negative. The candidate generation query was effectively writing final decisions in invisible ink before the named pipeline stages even began.

The new architecture eliminates this class of error entirely by removing the pre-filtering step. Every KSA is evaluated. Every decision is documented. Every exclusion is the result of a four-pass process with two adversarial challenges and a written rationale — not a silent consequence of a query threshold.

### 9.2 Guarantees the New Architecture Provides

**Guarantee 1: Complete coverage.** Every one of the 1,069 KSAs is evaluated against every one of the 187 roles. There is no pre-filter, no candidate threshold, no query that silently discards KSAs before evaluation. Completeness can be verified post-run by confirming that 1,069 artifacts exist in every role directory.

**Guarantee 2: Every decision is documented.** For every role-KSA pair, the artifact records why the decision was made — not just what the decision was. An auditor can reconstruct the reasoning chain from raw STRM scores through adversarial challenge to final ruling without re-running the pipeline.

**Guarantee 3: No silent filtering.** The only place a KSA can be excluded is in the explicit decision fields of the artifact. There is no upstream gating mechanism that can silently prevent a KSA from being evaluated.

**Guarantee 4: Adversarial challenge of every include and every exclude.** Both inclusion and exclusion decisions are challenged by two independent agents with different mandates. Pass 3 challenges internal consistency — is this decision calibrated the same way as prior decisions for this role? Pass 4 challenges external validity — does this decision match how the real world defines this role's competencies? Neither agent is constrained to agree with Pass 2.

**Guarantee 5: Calibration consistency within roles.** Pass 3's internal consistency challenge — which has access to the list of KSAs already included for the role — is specifically designed to catch seniority drift and scope boundary inconsistency within a single role's evaluation. Without this, an agent could apply a strict seniority filter early in a role's evaluation and relax it later (or vice versa) with no mechanism to detect it.

**Guarantee 6: External grounding of every decision.** Pass 4 is explicitly required to ground its challenge in external reference — job posting patterns, practitioner self-report, standards body frameworks, certification body requirements. This prevents the pipeline from producing a role-competency model that is internally consistent but disconnected from real-world practice.

**Guarantee 7: Confidence is earned, not assumed.** The three-tier confidence model (`high`, `medium`, `low`) is derived from the adversarial outcome, not from the Pass 1 score. A KSA with a high composite STRM score that is challenged and overturned by both adversarial agents receives `low` confidence. Confidence reflects the quality of the decision process, not the strength of the similarity signal.

**Guarantee 8: The corpus is durable and auditable.** Artifacts are atomic, validated before writing, and schema-versioned. The pipeline version, model, and timestamp are recorded in every artifact. Future changes to evaluation logic do not retroactively invalidate existing artifacts — they produce new artifacts with a new schema version. The artifact corpus as a whole is a durable record of decisions made at a specific point in time with specific tooling.

### 9.3 What This Architecture Does Not Guarantee

Being honest about limitations is part of what makes the guarantees above credible.

**STRM coverage gaps are documented but not compensated.** If STRM has no data for a given KSA-domain combination, Pass 1 returns a zero score with a `none` signal. The LLM agents in Passes 2–4 proceed with no scoring signal to anchor them. For these KSAs, the evaluation is entirely dependent on LLM reasoning and external challenge. The `strm_gap_notes` field in the role summary documents where this applies.

**Pass 4 external challenge quality depends on web search availability and model knowledge.** When web search is unavailable or returns no results, Pass 4 falls back to model training knowledge. For emerging role definitions or very new KSA domains, training knowledge may be incomplete. The `evidence` field documents this limitation explicitly, but it does not eliminate it.

**LLM consistency across long runs is not guaranteed.** Over a multi-week run, model behavior may vary due to API updates or other factors outside the pipeline's control. The `metadata.model` field captures the model version for each artifact, enabling post-hoc analysis of whether decisions differ systematically across time periods.

**Volume, not accuracy, is guaranteed.** The pipeline guarantees that 199,903 evaluations will be performed and documented. It does not guarantee that every final decision is correct. The adversarial architecture significantly raises the bar for incorrect decisions, but it does not eliminate the possibility. The artifacts provide the evidence needed for human review to identify and correct errors where they occur.

---

## Appendix A: Error Types and Recovery Procedures

| Error Type | Detection Point | Recovery |
|------------|-----------------|----------|
| JSON parse failure (LLM response) | `agents.py` | Retry with explicit error feedback, up to `MAX_RETRIES_PER_PASS` |
| Schema validation failure (LLM response) | `agents.py` | Retry with schema error, up to `MAX_RETRIES_PER_PASS` |
| API rate limit (429) | `agents.py` | Exponential backoff: 60/120/240/480s, then skip and log |
| API server error (500, timeout) | `agents.py` | Fixed 30s retry, up to `MAX_RETRIES_PER_PASS`, then skip and log |
| Artifact validation failure | `artifact_writer.py` | Do not write. Log failure. Mark pair for manual review. |
| Corrupted existing artifact (on resume) | `evaluate_role_ksas.py` | Treat as incomplete. Re-evaluate. Overwrite corrupted file. |
| Missing STRM data for KSA | `scoring.py` | Return valid zero-score block. Log as STRM gap. Continue. |
| Role not found in `widai_roles.json` | `evaluate_role_ksas.py` | Abort with clear error message. Do not proceed. |
| KSA not found in `ksa_catalog.json` | `evaluate_role_ksas.py` | Abort with clear error message. Do not proceed. |

---

## Appendix B: Pilot Run Checklist

Before running `--all`, run a single role end-to-end and verify:

- [ ] All 1,069 KSA artifacts exist in the role directory
- [ ] All artifacts pass schema validation
- [ ] `summary.json` was written with correct counts (total_evaluated == 1069, included + excluded == 1069)
- [ ] `ROADMAP.md` reflects the role as complete
- [ ] Inclusion rate is plausible for the role type (typically 5–15%)
- [ ] `score_gap` in summary > 0.2 (scoring signal is separating decisions)
- [ ] At least some Pass 3 and Pass 4 overturns occurred (adversarial agents are functioning)
- [ ] Log file contains per-KSA completion entries and a run summary
- [ ] Pipeline can be resumed mid-role (interrupt after ~200 KSAs, restart, verify it continues from KSA 201)
- [ ] `--status` output correctly shows the role as complete with accurate statistics
- [ ] Estimated cost per role aligns with budget expectations before scaling to all 187

---

## Appendix C: Schema Version History

| Version | Date | Changes |
|---------|------|---------|
| 2.0 | 2026-04-06 | Initial production schema. Four-pass pipeline. Full adversarial evaluation. No pre-filtering. |

Future schema changes must increment `schema_version`. Existing artifacts must not be mutated to match new schemas — they retain the schema version under which they were produced.

---

*End of document.*  
*Architecture Version: 1.0 — April 2026*
