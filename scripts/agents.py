"""
WIDAI Role-KSA Evaluation — Passes 2, 3, 4: Prompt Templates and Response Schemas

These passes are executed by Cowork task sessions (Claude Max), not by Python directly.
This module provides:
  - Prompt templates (formatted with role/KSA context)
  - Response schema documentation
  - Response parsers for validating Cowork output

Passes 2-4 require no Anthropic API key. They run through the existing Claude subscription
via Cowork task sessions that read pass1_batch.json and write evaluation artifacts.
"""

from typing import Dict, Any, List, Optional
from evaluation_config import PROMPT_PASS_2, PROMPT_PASS_3, PROMPT_PASS_4


class EvaluationError(Exception):
    pass


# ==================== Response Schemas ====================

PASS_2_RESPONSE_SCHEMA = {
    "scope_fit": "in_scope | out_of_scope | edge_case",
    "seniority_fit": "appropriate | too_senior | too_junior",
    "preliminary_decision": "include | exclude",
    "rationale": "string — specific, minimum 2 sentences, must reference STRM signal",
}

PASS_3_RESPONSE_SCHEMA = {
    "outcome": "upheld | overturned",
    "challenge": "string — specific challenge to the Pass 2 decision, or null if upheld",
    "rebuttal": "string — Pass 2 agent rebuttal if overturned, else null",
    "ruling": "include | exclude",
}

PASS_4_RESPONSE_SCHEMA = {
    "outcome": "upheld | overturned",
    "challenge": "string — external evidence challenge, or null if upheld",
    "evidence": "string — job market / certification body evidence cited",
    "ruling": "include | exclude",
}

FINAL_ARTIFACT_SCHEMA = {
    "schema_version": "2.0",
    "role_id": "string",
    "role_name": "string",
    "ksa_id": "string",
    "ksa_text": "string",
    "ksa_dimension": "Knowledge | Skills | Abilities | Tasks",
    "ksa_domain": "string (2-letter domain code)",
    "pass_1_scoring": "object — from pass1_batch.json",
    "pass_2_evaluation": "object — scope_fit, seniority_fit, preliminary_decision, rationale",
    "pass_3_adversarial_internal": "object — outcome, challenge, rebuttal, ruling",
    "pass_4_adversarial_external": "object — outcome, challenge, evidence, ruling",
    "final_decision": "include | exclude",
    "decision_confidence": "high | medium | low",
    "decision_rationale": "string",
    "adversarial_disagreements": "int (0, 1, or 2)",
    "metadata": {
        "evaluated_at": "ISO timestamp",
        "pipeline_version": "string",
    },
}


# ==================== Prompt Formatters ====================

def format_pass2_prompt(role: Dict[str, Any], ksa: Dict[str, Any], pass1: Dict[str, Any]) -> str:
    """Format the Pass 2 evaluation prompt for a Cowork task session."""
    return PROMPT_PASS_2.format(
        role_id=role.get("role_id", ""),
        role_name=role.get("canonical_title", ""),
        role_category=role.get("category_code", ""),
        role_description=role.get("description", ""),
        ksa_id=ksa.get("id", ""),
        ksa_text=ksa.get("text", ""),
        ksa_dimension=ksa.get("dimension", ""),
        ksa_domain=ksa.get("domain", ""),
        composite_score=pass1.get("composite_score", 0),
        signal_strength=pass1.get("signal_strength", "none"),
        top_anchors=_format_anchors(pass1.get("top_anchors", [])),
    )


def format_pass3_prompt(
    role: Dict[str, Any],
    ksa: Dict[str, Any],
    pass2: Dict[str, Any],
    included_ksas: List[Dict[str, Any]],
) -> str:
    """Format the Pass 3 adversarial internal prompt."""
    included_list = "\n".join(
        f"  - {k.get('id')}: {k.get('text', '')[:80]}..."
        for k in included_ksas[:20]  # Show first 20 for context
    ) or "  (none yet)"
    return PROMPT_PASS_3.format(
        role_id=role.get("role_id", ""),
        role_name=role.get("canonical_title", ""),
        role_description=role.get("description", ""),
        included_ksas_list=included_list,
        ksa_id=ksa.get("id", ""),
        ksa_text=ksa.get("text", ""),
        ksa_dimension=ksa.get("dimension", ""),
        ksa_domain=ksa.get("domain", ""),
        pass2_decision=pass2.get("preliminary_decision", ""),
        pass2_rationale=pass2.get("rationale", ""),
    )


def format_pass4_prompt(
    role: Dict[str, Any],
    ksa: Dict[str, Any],
    pass2: Dict[str, Any],
    pass3: Dict[str, Any],
) -> str:
    """Format the Pass 4 adversarial external prompt."""
    return PROMPT_PASS_4.format(
        role_id=role.get("role_id", ""),
        role_name=role.get("canonical_title", ""),
        role_description=role.get("description", ""),
        ksa_id=ksa.get("id", ""),
        ksa_text=ksa.get("text", ""),
        ksa_domain=ksa.get("domain", ""),
        pass2_decision=pass2.get("preliminary_decision", ""),
        pass2_rationale=pass2.get("rationale", ""),
        pass3_outcome=pass3.get("outcome", "upheld"),
        pass3_challenge=pass3.get("challenge") or "No challenge raised.",
    )


# ==================== Response Parsers ====================

def parse_pass2_response(response_text: str) -> Dict[str, Any]:
    """Parse and validate a Pass 2 JSON response."""
    import json
    result = json.loads(response_text)
    for required in ("scope_fit", "seniority_fit", "preliminary_decision", "rationale"):
        if required not in result:
            raise EvaluationError(f"Pass 2 response missing field: {required}")
    if result["preliminary_decision"] not in ("include", "exclude"):
        raise EvaluationError(f"Pass 2 invalid decision: {result['preliminary_decision']}")
    return result


def parse_pass3_response(response_text: str) -> Dict[str, Any]:
    """Parse and validate a Pass 3 JSON response."""
    import json
    result = json.loads(response_text)
    for required in ("outcome", "ruling"):
        if required not in result:
            raise EvaluationError(f"Pass 3 response missing field: {required}")
    if result["outcome"] not in ("upheld", "overturned"):
        raise EvaluationError(f"Pass 3 invalid outcome: {result['outcome']}")
    return result


def parse_pass4_response(response_text: str) -> Dict[str, Any]:
    """Parse and validate a Pass 4 JSON response."""
    import json
    result = json.loads(response_text)
    for required in ("outcome", "evidence", "ruling"):
        if required not in result:
            raise EvaluationError(f"Pass 4 response missing field: {required}")
    if result["outcome"] not in ("upheld", "overturned"):
        raise EvaluationError(f"Pass 4 invalid outcome: {result['outcome']}")
    return result


def compute_final_decision(
    pass2: Dict[str, Any],
    pass3: Dict[str, Any],
    pass4: Dict[str, Any],
) -> tuple:
    """
    Compute final decision and confidence from all three pass results.
    Returns (final_decision, confidence, adversarial_disagreements).
    """
    p3_overturned = pass3.get("outcome") == "overturned"
    p4_overturned = pass4.get("outcome") == "overturned"
    disagreements = (1 if p3_overturned else 0) + (1 if p4_overturned else 0)

    if disagreements == 0:
        decision = pass3.get("ruling", pass2.get("preliminary_decision"))
        confidence = "high"
    elif disagreements == 1:
        decision = pass3.get("ruling") if p3_overturned else pass4.get("ruling")
        confidence = "medium"
    else:
        # Both overturned — reverse the Pass 2 decision
        decision = pass4.get("ruling", pass3.get("ruling"))
        confidence = "low"

    return decision, confidence, disagreements


# ==================== Helpers ====================

def _format_anchors(anchors: List[Dict[str, Any]]) -> str:
    if not anchors:
        return "  No STRM anchors found."
    lines = []
    for a in anchors[:3]:
        lines.append(
            f"  - {a.get('framework', '?')}/{a.get('element_id', '?')}: "
            f"{a.get('element_label', '')[:60]} (score: {a.get('score', 0):.3f})"
        )
    return "\n".join(lines)
