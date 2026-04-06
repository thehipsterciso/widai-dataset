"""
WIDAI Role-KSA Evaluation Pipeline Configuration
Version 2.0 — No pre-filtering. All 1,069 KSAs evaluated for every role.

Single source of truth for all tunable parameters, model settings, weights, and prompts.
"""

import os

# ==================== Model Configuration ====================
LLM_MODEL = "claude-sonnet-4-5"
PASS_2_TEMPERATURE = 0.0
PASS_3_TEMPERATURE = 0.1
PASS_4_TEMPERATURE = 0.1
MAX_RETRIES_PER_PASS = 2

# ==================== Scoring Weights ====================
# Weights for Pass 1 metrics. Must sum to 1.0 when all metrics present.
# When metrics are absent, weights are renormalized across available metrics.
METRIC_WEIGHTS = {
    "cross_encoder_sts": 0.40,
    "bertscore": 0.20,
    "nli_score": 0.20,
    "bi_encoder_cosine": 0.15,
    "jaccard": 0.05,
}

# Signal strength classification thresholds (Pass 1 output)
SIGNAL_THRESHOLDS = {
    "strong": 0.65,
    "moderate": 0.45,
    "weak": 0.25,
    # Below 0.25 = "none"
}

# ==================== File and Path Configuration ====================
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
DOCS_DIR = os.path.join(BASE_DIR, "docs")
ROLE_KSA_EVAL_DIR = os.path.join(DOCS_DIR, "role_ksa_evaluations")
MAPPINGS_DIR = os.path.join(BASE_DIR, "mappings")
LOGS_DIR = os.path.join(BASE_DIR, "logs")

# STRM data location (check for consolidated or per-framework)
STRM_MAPPING_FILE = os.path.join(BASE_DIR, "strm", "dcwf", "strm_mapping.json")
STRM_DDAT_FILE = os.path.join(BASE_DIR, "strm", "ddat", "strm_mapping.json")
STRM_DIR = os.path.join(BASE_DIR, "strm")

# Source data files
ROLES_DATA_DIR = os.path.join(BASE_DIR, "roles")
KSAS_DATA_DIR = os.path.join(BASE_DIR, "ksas")

# KSA filename sanitization (if KSA ids contain characters invalid for filenames)
KSA_ID_SANITIZE = {"/": "_", "\\": "_", ":": "_", "*": "_", "?": "_", '"': "_", "<": "_", ">": "_", "|": "_"}

# ==================== Prompt Templates ====================
PROMPT_PASS_2 = """You are a rigorous competency evaluator. Your task is to assess whether a Knowledge, Skill, Ability, or Task (KSA) is appropriate for inclusion in a specific work role's competency profile.

**Role Context:**
- Role ID: {role_id}
- Role Name: {role_name}
- Role Category: {role_category}
- Role Description: {role_description}

**KSA Under Evaluation:**
- KSA ID: {ksa_id}
- KSA Text: {ksa_text}
- Dimension: {ksa_dimension}
- Domain: {ksa_domain}

**STRM Signal Data (from Pass 1):**
- Composite Score: {composite_score}
- Signal Strength: {signal_strength}
- Top Anchors: {top_anchors_text}
- Metrics Used: {metrics_used}

Your task is to evaluate this KSA on four dimensions:

1. **Scope Fit:** Does this KSA describe a competency that belongs within the functional scope of this role? A Data Engineer and a Privacy Compliance role may both touch data, but the ownership and nature differ. Determine whether this KSA's subject matter is in-scope for the role's primary function, not merely adjacent to it.

2. **Seniority Fit:** Does the level of the KSA (foundational, practitioner, advanced, strategic) match the expected seniority level of this role? A task written for an individual contributor may not be appropriate for a Chief Data Officer.

3. **Semantic Accuracy:** Does the STRM signal reflect genuine semantic alignment, or does it inflate due to shared terminology without shared meaning? Explicitly assess whether the top anchors represent genuine alignment or surface-level keyword overlap.

4. **Preliminary Decision:** Based on the three assessments, determine whether this KSA should be **included** or **excluded** from this role's profile. No abstentions. No partial decisions.

You must return a JSON object with this exact structure:

{{
  "scope_fit": "in_scope|out_of_scope|edge_case",
  "seniority_fit": "appropriate|too_senior|too_junior",
  "preliminary_decision": "include|exclude",
  "rationale": "Substantive rationale (minimum 50 characters) explaining: (1) basis for scope fit assessment, (2) basis for seniority fit assessment, (3) how STRM signal supported or complicated the decision, (4) specific reason for the final decision."
}}

Your rationale must be detailed and specific. Vague statements like "This KSA is relevant" are not acceptable. Name specific reasons and acknowledge the STRM signal explicitly.

Return ONLY the JSON object. No markdown, no preamble, no explanation outside the JSON."""

PROMPT_PASS_3 = """You are an adversarial agent tasked with challenging a preliminary competency evaluation. Your role is NOT to re-evaluate from scratch, but to actively find faults with the reasoning provided.

**Role Context:**
- Role ID: {role_id}
- Role Name: {role_name}
- Role Category: {role_category}
- Role Description: {role_description}

**KSAs Already Included for This Role (for consistency checking):**
{included_ksas_list}

**KSA Under Challenge:**
- KSA ID: {ksa_id}
- KSA Text: {ksa_text}
- Dimension: {ksa_dimension}

**Pass 2 Decision (preliminary):**
- Decision: {pass_2_decision}
- Scope Fit: {pass_2_scope_fit}
- Seniority Fit: {pass_2_seniority_fit}
- Rationale: {pass_2_rationale}

Your task is to challenge this decision using four specific angles:

1. **Seniority Calibration Consistency:** Is the seniority boundary being applied uniformly? If a similar strategic KSA was already included on grounds of scope fit, why is this one excluded on seniority grounds (or vice versa)?

2. **Scope Boundary Consistency:** Is the scope definition being applied uniformly across the already-included KSAs? Are there precedents that contradict the current decision?

3. **Practitioner Recognition Test:** Would a senior practitioner in this role immediately recognize this competency as genuinely required? If yes and it's excluded, that's a strong signal to overturn.

4. **Rationale Integrity Check:** Is the Pass 2 rationale self-consistent? Does it rely on surface-level pattern matching rather than genuine functional analysis?

Return a JSON object with this exact structure:

{{
  "outcome": "upheld|overturned",
  "challenge": "Detailed explanation of what was checked and what was found. If upheld, explain why the decision stands. If overturned, identify the specific inconsistency or failure discovered."
}}

If you return "overturned", the Pass 2 agent will be asked to provide a rebuttal. Your challenge must be specific enough to force genuine re-evaluation, not vague criticism.

Return ONLY the JSON object. No markdown, no preamble."""

PROMPT_PASS_3_REBUTTAL = """The adversarial agent has challenged your previous evaluation with this critique:

{pass_3_challenge}

You must now:
1. Acknowledge the specific challenge points
2. Provide a substantive rebuttal explaining why your original reasoning stands, OR accept the override
3. Issue a final ruling: include or exclude

Return a JSON object with this exact structure:

{{
  "rebuttal": "Your detailed response to the challenge. If accepting the override, explain why the challenge is valid.",
  "ruling": "include|exclude"
}}

This ruling supersedes your original preliminary decision. It will be recorded as the final internal consistency decision.

Return ONLY the JSON object."""

PROMPT_PASS_4 = """You are an external ground truth validator. Your task is to assess whether a competency inclusion decision is consistent with how the real-world industry and practitioner community understand this role.

**Role Context:**
- Role ID: {role_id}
- Role Name: {role_name}
- Role Category: {role_category}

**KSA Under Validation:**
- KSA ID: {ksa_id}
- KSA Text: {ksa_text}
- Domain: {ksa_domain}

**Pass 2 Decision:** {pass_2_decision}
**Pass 3 Outcome:** {pass_3_outcome}

Your task is to challenge this decision using four ground truth checks:

1. **Job Posting Signal:** Do job postings for this role (or closely equivalent titles) regularly mention this competency or skill area? Absence from job postings for a senior role is meaningful evidence for exclusion. Consistent presence is evidence for inclusion.

2. **Practitioner Self-Report Signal:** Do practitioners who hold or have held this role (observable from professional profiles, conference talks, published writing, community discussions) report needing or using this competency?

3. **Standards Body Signal:** Does the relevant standards body or certification framework include this competency in their definition of the role? Reference NIST, ISACA, DAMA, CDAIO Program, relevant certifications (CISSP, CISM, CDMP, etc.). Be specific.

4. **Gap Analysis:** If this KSA were excluded, would a practitioner notice a meaningful gap? Would they say "I use this regularly" or "that's someone else's job"?

Perform web searches as needed to ground your assessment in real-world evidence. Return a JSON object with this exact structure:

{{
  "outcome": "upheld|overturned",
  "challenge": "Detailed explanation of ground truth findings. Be specific about which checks were conducted and what was found.",
  "evidence": "Named sources. Job title patterns, standards bodies, frameworks, practitioner communities. Not a restatement of the KSA.",
  "ruling": "include|exclude"
}}

Your evidence field must cite at least one named source. It cannot be generic background knowledge.

Return ONLY the JSON object."""

PROMPT_FINAL_RULING = """You are making a final ruling on a disputed competency evaluation. All four passes have completed, and the adversarial agents have provided their challenges.

**Role:** {role_name} ({role_id})
**KSA:** {ksa_text} ({ksa_id})

**Pass 2 Preliminary Decision:** {pass_2_decision}
**Pass 3 (Internal Consistency) Outcome:** {pass_3_outcome} {pass_3_ruling_note}
**Pass 4 (External Ground Truth) Outcome:** {pass_4_outcome}

**Adversarial Disagreement Count:** {adversarial_disagreements}

Your task: Determine the final decision.

Rules:
- If 0 disagreements: Pass 2 decision stands, confidence = high
- If 1 disagreement: You make the final call, confidence = medium
- If 2 disagreements: You must reverse the Pass 2 decision UNLESS you can provide extraordinary documented justification for holding it. Confidence = low if held against both.

Return a JSON object with this exact structure:

{{
  "final_decision": "include|exclude",
  "decision_confidence": "high|medium|low",
  "decision_rationale": "Substantive explanation of the final ruling, addressing all passes and any overturns."
}}

Return ONLY the JSON object."""

# ==================== Schema Constraints ====================
VALID_SCOPE_FITS = {"in_scope", "out_of_scope", "edge_case"}
VALID_SENIORITY_FITS = {"appropriate", "too_senior", "too_junior"}
VALID_DECISIONS = {"include", "exclude"}
VALID_ADVERSARIAL_OUTCOMES = {"upheld", "overturned"}
VALID_CONFIDENCE_LEVELS = {"high", "medium", "low"}
VALID_KSA_DIMENSIONS = {"Knowledge", "Skills", "Abilities", "Tasks"}

# ==================== Constants ====================
SCHEMA_VERSION = "2.0"
PIPELINE_VERSION = "1.0"
