"""
WIDAI Role-KSA Evaluation — LLM Agent Implementations
Passes 2, 3, 4, and rebuttal logic.
"""

import json
import re
from typing import Dict, List, Any, Optional
import anthropic

from evaluation_config import (
    LLM_MODEL,
    PASS_2_TEMPERATURE,
    PASS_3_TEMPERATURE,
    PASS_4_TEMPERATURE,
    MAX_RETRIES_PER_PASS,
    PROMPT_PASS_2,
    PROMPT_PASS_3,
    PROMPT_PASS_3_REBUTTAL,
    PROMPT_PASS_4,
    VALID_SCOPE_FITS,
    VALID_SENIORITY_FITS,
    VALID_DECISIONS,
    VALID_ADVERSARIAL_OUTCOMES,
)


class EvaluationError(Exception):
    """Raised when an evaluation pass fails after retries."""
    pass


class LLMAgentExecutor:
    """Base class for LLM agent passes."""

    def __init__(self):
        """Initialize Anthropic client."""
        self.client = anthropic.Anthropic()

    def _call_llm(
        self, prompt: str, temperature: float = 0.0, max_retries: int = MAX_RETRIES_PER_PASS
    ) -> str:
        """Call Claude LLM and return response text."""
        for attempt in range(max_retries):
            try:
                message = self.client.messages.create(
                    model=LLM_MODEL,
                    max_tokens=2000,
                    temperature=temperature,
                    messages=[{"role": "user", "content": prompt}],
                )
                return message.content[0].text
            except Exception as e:
                if attempt < max_retries - 1:
                    print(f"LLM call failed, retrying: {e}")
                else:
                    raise

    def _extract_json(self, text: str) -> Dict[str, Any]:
        """Extract JSON from text response. Handles markdown code blocks."""
        # Try to find JSON in code blocks first
        code_block_match = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", text, re.DOTALL)
        if code_block_match:
            json_str = code_block_match.group(1)
        else:
            # Try to find raw JSON
            json_match = re.search(r"\{.*\}", text, re.DOTALL)
            if json_match:
                json_str = json_match.group(0)
            else:
                raise ValueError(f"No JSON found in response: {text[:200]}")

        return json.loads(json_str)

    def _validate_pass_2_output(self, output: Dict[str, Any]) -> bool:
        """Validate Pass 2 output structure."""
        required_fields = {"scope_fit", "seniority_fit", "preliminary_decision", "rationale"}
        if not all(field in output for field in required_fields):
            return False
        if output["scope_fit"] not in VALID_SCOPE_FITS:
            return False
        if output["seniority_fit"] not in VALID_SENIORITY_FITS:
            return False
        if output["preliminary_decision"] not in VALID_DECISIONS:
            return False
        if not isinstance(output["rationale"], str) or len(output["rationale"]) < 50:
            return False
        return True

    def _validate_adversarial_output(self, output: Dict[str, Any]) -> bool:
        """Validate Pass 3/4 adversarial output structure."""
        required_fields = {"outcome", "challenge"}
        if not all(field in output for field in required_fields):
            return False
        if output["outcome"] not in VALID_ADVERSARIAL_OUTCOMES:
            return False
        if not isinstance(output["challenge"], str) or len(output["challenge"]) < 20:
            return False
        return True


class Pass2EvaluationAgent(LLMAgentExecutor):
    """Pass 2: LLM Evaluation Agent"""

    def run(
        self,
        role: Dict[str, Any],
        ksa: Dict[str, Any],
        pass_1_block: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Run Pass 2 evaluation."""
        # Format top anchors text
        if pass_1_block["top_anchors"]:
            top_anchors_lines = []
            for anchor in pass_1_block["top_anchors"]:
                top_anchors_lines.append(
                    f"  - {anchor['framework'].upper()}: {anchor['element_label']} (score: {anchor['score']:.4f})"
                )
            top_anchors_text = "\n".join(top_anchors_lines)
        else:
            top_anchors_text = "None"

        prompt = PROMPT_PASS_2.format(
            role_id=role.get("role_id"),
            role_name=role.get("canonical_title", ""),
            role_category=role.get("category_code", ""),
            role_description=role.get("description", ""),
            ksa_id=ksa.get("id"),
            ksa_text=ksa.get("text", ""),
            ksa_dimension=ksa.get("dimension", ""),
            ksa_domain=ksa.get("domain", ""),
            composite_score=f"{pass_1_block['composite_score']:.4f}",
            signal_strength=pass_1_block["signal_strength"],
            top_anchors_text=top_anchors_text,
            metrics_used=", ".join(pass_1_block["metrics_used"]) if pass_1_block["metrics_used"] else "none",
        )

        for attempt in range(MAX_RETRIES_PER_PASS):
            response_text = self._call_llm(prompt, temperature=PASS_2_TEMPERATURE)
            try:
                output = self._extract_json(response_text)
                if self._validate_pass_2_output(output):
                    return output
                else:
                    print(f"Pass 2 validation failed, retrying: {output}")
                    # Retry with validation error feedback
                    prompt += f"\n\nValidation error: Output did not meet all constraints. Please verify: scope_fit in {VALID_SCOPE_FITS}, seniority_fit in {VALID_SENIORITY_FITS}, decision in {VALID_DECISIONS}, rationale > 50 chars."
            except Exception as e:
                print(f"Pass 2 JSON parsing failed: {e}")
                if attempt < MAX_RETRIES_PER_PASS - 1:
                    prompt += f"\n\nError: {e}. Please return ONLY valid JSON."

        raise EvaluationError(
            f"Pass 2 failed after {MAX_RETRIES_PER_PASS} retries for KSA {ksa['id']}"
        )


class Pass3AdversarialAgent(LLMAgentExecutor):
    """Pass 3: Adversarial Agent 1 (Internal Consistency Challenge)"""

    def run(
        self,
        role: Dict[str, Any],
        ksa: Dict[str, Any],
        pass_2_result: Dict[str, Any],
        included_ksas: List[Dict[str, Any]],
    ) -> Dict[str, Any]:
        """Run Pass 3 adversarial challenge."""
        # Format included KSAs list
        if included_ksas:
            included_lines = []
            for inc_ksa in included_ksas[:20]:  # Limit to recent 20 for context
                included_lines.append(
                    f"  - {inc_ksa['id']} ({inc_ksa['dimension']}): {inc_ksa['text'][:60]}..."
                )
            included_ksas_text = "\n".join(included_lines)
            if len(included_ksas) > 20:
                included_ksas_text += f"\n  ... and {len(included_ksas) - 20} more"
        else:
            included_ksas_text = "None yet for this role."

        prompt = PROMPT_PASS_3.format(
            role_id=role.get("role_id"),
            role_name=role.get("canonical_title", ""),
            role_category=role.get("category_code", ""),
            role_description=role.get("description", ""),
            included_ksas_list=included_ksas_text,
            ksa_id=ksa.get("id"),
            ksa_text=ksa.get("text", ""),
            ksa_dimension=ksa.get("dimension", ""),
            pass_2_decision=pass_2_result.get("preliminary_decision"),
            pass_2_scope_fit=pass_2_result.get("scope_fit"),
            pass_2_seniority_fit=pass_2_result.get("seniority_fit"),
            pass_2_rationale=pass_2_result.get("rationale"),
        )

        for attempt in range(MAX_RETRIES_PER_PASS):
            response_text = self._call_llm(prompt, temperature=PASS_3_TEMPERATURE)
            try:
                output = self._extract_json(response_text)
                if self._validate_adversarial_output(output):
                    output["ruling"] = None  # Will be filled in if overturned (rebuttal phase)
                    return output
                else:
                    print(f"Pass 3 validation failed, retrying")
            except Exception as e:
                print(f"Pass 3 JSON parsing failed: {e}")
                if attempt < MAX_RETRIES_PER_PASS - 1:
                    prompt += f"\n\nError: {e}. Please return ONLY valid JSON with 'outcome' and 'challenge' fields."

        raise EvaluationError(
            f"Pass 3 failed after {MAX_RETRIES_PER_PASS} retries for KSA {ksa['id']}"
        )

    def run_rebuttal(
        self,
        role: Dict[str, Any],
        ksa: Dict[str, Any],
        pass_2_result: Dict[str, Any],
        pass_3_challenge: str,
    ) -> Dict[str, Any]:
        """Run Pass 2 agent rebuttal to Pass 3 challenge."""
        prompt = PROMPT_PASS_3_REBUTTAL.format(
            pass_3_challenge=pass_3_challenge,
        )

        # Prepend the full Pass 2 context
        full_prompt = f"""You are reconsidering your previous evaluation with new adversarial feedback.

Previous evaluation:
- Decision: {pass_2_result['preliminary_decision']}
- Scope Fit: {pass_2_result['scope_fit']}
- Seniority Fit: {pass_2_result['seniority_fit']}
- Rationale: {pass_2_result['rationale']}

{prompt}"""

        for attempt in range(MAX_RETRIES_PER_PASS):
            response_text = self._call_llm(full_prompt, temperature=PASS_2_TEMPERATURE)
            try:
                output = self._extract_json(response_text)
                required_fields = {"rebuttal", "ruling"}
                if all(field in output for field in required_fields):
                    if output["ruling"] in VALID_DECISIONS:
                        return output
            except Exception as e:
                print(f"Rebuttal JSON parsing failed: {e}")
                if attempt < MAX_RETRIES_PER_PASS - 1:
                    full_prompt += f"\n\nError: {e}. Please return JSON with 'rebuttal' and 'ruling' fields."

        raise EvaluationError(f"Rebuttal failed after {MAX_RETRIES_PER_PASS} retries for KSA {ksa['id']}")


class Pass4AdversarialAgent(LLMAgentExecutor):
    """Pass 4: Adversarial Agent 2 (External Ground Truth Challenge)"""

    def run(
        self,
        role: Dict[str, Any],
        ksa: Dict[str, Any],
        pass_2_result: Dict[str, Any],
        pass_3_result: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Run Pass 4 external validation."""
        prompt = PROMPT_PASS_4.format(
            role_id=role.get("role_id"),
            role_name=role.get("canonical_title", ""),
            role_category=role.get("category_code", ""),
            ksa_id=ksa.get("id"),
            ksa_text=ksa.get("text", ""),
            ksa_domain=ksa.get("domain", ""),
            pass_2_decision=pass_2_result.get("preliminary_decision"),
            pass_3_outcome=pass_3_result.get("outcome"),
        )

        for attempt in range(MAX_RETRIES_PER_PASS):
            response_text = self._call_llm(prompt, temperature=PASS_4_TEMPERATURE)
            try:
                output = self._extract_json(response_text)
                required_fields = {"outcome", "challenge", "evidence", "ruling"}
                if all(field in output for field in required_fields):
                    if output["outcome"] in VALID_ADVERSARIAL_OUTCOMES and output["ruling"] in VALID_DECISIONS:
                        return output
            except Exception as e:
                print(f"Pass 4 JSON parsing failed: {e}")
                if attempt < MAX_RETRIES_PER_PASS - 1:
                    prompt += f"\n\nError: {e}. Please return JSON with 'outcome', 'challenge', 'evidence', and 'ruling' fields."

        raise EvaluationError(
            f"Pass 4 failed after {MAX_RETRIES_PER_PASS} retries for KSA {ksa['id']}"
        )
