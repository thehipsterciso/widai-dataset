"""
WIDAI Role-KSA Evaluation — Artifact Writer
Validates and writes evaluation artifacts, summaries, and mappings.
"""

import json
import os
import re
from datetime import datetime
from typing import Dict, List, Any, Optional
from pathlib import Path

from evaluation_config import (
    SCHEMA_VERSION,
    PIPELINE_VERSION,
    ROLE_KSA_EVAL_DIR,
    MAPPINGS_DIR,
    KSA_ID_SANITIZE,
    VALID_SCOPE_FITS,
    VALID_SENIORITY_FITS,
    VALID_DECISIONS,
    VALID_ADVERSARIAL_OUTCOMES,
    VALID_CONFIDENCE_LEVELS,
    VALID_KSA_DIMENSIONS,
    LLM_MODEL,
)


class ArtifactValidationError(Exception):
    """Raised when artifact validation fails."""
    pass


class ArtifactWriter:
    """Writes and validates KSA evaluation artifacts."""

    @staticmethod
    def sanitize_ksa_id(ksa_id: str) -> str:
        """Sanitize KSA id for use as filename."""
        sanitized = ksa_id
        for char, replacement in KSA_ID_SANITIZE.items():
            sanitized = sanitized.replace(char, replacement)
        return sanitized

    @staticmethod
    def _validate_artifact(artifact: Dict[str, Any]) -> List[str]:
        """Validate artifact against schema. Return list of errors (empty if valid)."""
        errors = []

        # Schema version
        if artifact.get("schema_version") != SCHEMA_VERSION:
            errors.append(f"schema_version must be '{SCHEMA_VERSION}'")

        # Role and KSA IDs
        if not re.match(r"WIDAI-[A-Z]+-\d+", artifact.get("role_id", "")):
            errors.append(f"role_id must match pattern WIDAI-[A-Z]+-[0-9]+")
        if not artifact.get("ksa_id"):
            errors.append("ksa_id is required")

        # KSA dimension
        if artifact.get("ksa_dimension") not in VALID_KSA_DIMENSIONS:
            errors.append(f"ksa_dimension must be one of {VALID_KSA_DIMENSIONS}")

        # Pass 1 scoring
        pass_1 = artifact.get("pass_1_scoring", {})
        if not isinstance(pass_1.get("composite_score"), (int, float)):
            errors.append("pass_1_scoring.composite_score must be a float")
        elif not (0.0 <= pass_1["composite_score"] <= 1.0):
            errors.append("pass_1_scoring.composite_score must be between 0.0 and 1.0")
        if pass_1.get("signal_strength") not in {"strong", "moderate", "weak", "none"}:
            errors.append("pass_1_scoring.signal_strength must be one of strong/moderate/weak/none")

        # Pass 2 evaluation
        pass_2 = artifact.get("pass_2_evaluation", {})
        if pass_2.get("scope_fit") not in VALID_SCOPE_FITS:
            errors.append(f"pass_2_evaluation.scope_fit must be one of {VALID_SCOPE_FITS}")
        if pass_2.get("seniority_fit") not in VALID_SENIORITY_FITS:
            errors.append(f"pass_2_evaluation.seniority_fit must be one of {VALID_SENIORITY_FITS}")
        if pass_2.get("preliminary_decision") not in VALID_DECISIONS:
            errors.append(f"pass_2_evaluation.preliminary_decision must be one of {VALID_DECISIONS}")
        rationale = pass_2.get("rationale", "")
        if not isinstance(rationale, str) or len(rationale) < 50:
            errors.append("pass_2_evaluation.rationale must be a string > 50 characters")

        # Pass 3 adversarial
        pass_3 = artifact.get("pass_3_adversarial_internal", {})
        if pass_3.get("outcome") not in VALID_ADVERSARIAL_OUTCOMES:
            errors.append(f"pass_3_adversarial_internal.outcome must be one of {VALID_ADVERSARIAL_OUTCOMES}")
        if pass_3.get("ruling") and pass_3.get("ruling") not in VALID_DECISIONS:
            errors.append(f"pass_3_adversarial_internal.ruling must be one of {VALID_DECISIONS}")

        # Pass 4 adversarial
        pass_4 = artifact.get("pass_4_adversarial_external", {})
        if pass_4.get("outcome") not in VALID_ADVERSARIAL_OUTCOMES:
            errors.append(f"pass_4_adversarial_external.outcome must be one of {VALID_ADVERSARIAL_OUTCOMES}")
        if pass_4.get("ruling") and pass_4.get("ruling") not in VALID_DECISIONS:
            errors.append(f"pass_4_adversarial_external.ruling must be one of {VALID_DECISIONS}")
        evidence = pass_4.get("evidence", "")
        if pass_4.get("outcome") == "overturned" and (not isinstance(evidence, str) or len(evidence) < 20):
            errors.append("pass_4_adversarial_external.evidence must be substantive when overturned")

        # Final decision
        if artifact.get("final_decision") not in VALID_DECISIONS:
            errors.append(f"final_decision must be one of {VALID_DECISIONS}")
        if artifact.get("decision_confidence") not in VALID_CONFIDENCE_LEVELS:
            errors.append(f"decision_confidence must be one of {VALID_CONFIDENCE_LEVELS}")
        final_rationale = artifact.get("decision_rationale", "")
        if not isinstance(final_rationale, str) or len(final_rationale) < 50:
            errors.append("decision_rationale must be a string > 50 characters")

        # Adversarial disagreements
        if artifact.get("adversarial_disagreements") not in {0, 1, 2}:
            errors.append("adversarial_disagreements must be 0, 1, or 2")

        # Metadata
        metadata = artifact.get("metadata", {})
        if not metadata.get("evaluated_at"):
            errors.append("metadata.evaluated_at is required")
        if not metadata.get("model"):
            errors.append("metadata.model is required")

        return errors

    def write_artifact(self, role_dir: str, ksa_id: str, artifact: Dict[str, Any]) -> None:
        """
        Validate and write artifact atomically.
        Raises ArtifactValidationError if validation fails (does not write).
        """
        errors = self._validate_artifact(artifact)
        if errors:
            raise ArtifactValidationError(f"Artifact validation failed: {'; '.join(errors)}")

        # Create role directory if needed
        os.makedirs(role_dir, exist_ok=True)

        # Write atomically to temp, then rename
        filename = self.sanitize_ksa_id(ksa_id) + ".json"
        target_path = os.path.join(role_dir, filename)
        tmp_path = target_path + ".tmp"

        try:
            # Write to temp file
            with open(tmp_path, "w") as f:
                json.dump(artifact, f, indent=2)

            # Rename (atomic on POSIX)
            os.rename(tmp_path, target_path)
        except Exception as e:
            # Clean up temp file if it exists
            if os.path.exists(tmp_path):
                os.remove(tmp_path)
            raise

    def compute_summary(self, role: Dict[str, Any], role_dir: str) -> Dict[str, Any]:
        """
        Read all KSA artifacts in role directory and compute aggregated summary.
        """
        # Scan for artifact files
        artifacts = []
        if os.path.exists(role_dir):
            for filename in os.listdir(role_dir):
                if filename.endswith(".json") and filename != "summary.json":
                    artifact_path = os.path.join(role_dir, filename)
                    with open(artifact_path) as f:
                        artifacts.append(json.load(f))

        summary = {
            "schema_version": SCHEMA_VERSION,
            "role_id": role.get("role_id"),
            "role_name": role.get("canonical_title", ""),
            "category_code": role.get("category_code", ""),
            "evaluated_at": datetime.utcnow().isoformat() + "Z",
            "total_evaluated": len(artifacts),
            "included": 0,
            "excluded": 0,
            "inclusion_rate": 0.0,
            "confidence_breakdown": {"high": 0, "medium": 0, "low": 0},
            "domain_breakdown": {},
            "dimension_breakdown": {
                "Knowledge": {"included": 0, "excluded": 0},
                "Skills": {"included": 0, "excluded": 0},
                "Abilities": {"included": 0, "excluded": 0},
                "Tasks": {"included": 0, "excluded": 0},
            },
            "score_distribution": {
                "avg_composite_included": 0.0,
                "avg_composite_excluded": 0.0,
                "score_gap": 0.0,
            },
            "adversarial_summary": {
                "pass3_overturns": 0,
                "pass4_overturns": 0,
                "both_overturned": 0,
                "final_reversals": 0,
            },
            "strm_coverage": ["dcwf", "ddat"],  # Update based on actual data
            "strm_gap_notes": "No DAMA, Evidence Act, or CDAIO-specific frameworks present in STRM data.",
            "pipeline_version": PIPELINE_VERSION,
        }

        # Aggregate metrics
        included_scores = []
        excluded_scores = []

        for artifact in artifacts:
            decision = artifact.get("final_decision")
            confidence = artifact.get("decision_confidence")
            dimension = artifact.get("ksa_dimension")
            domain = artifact.get("ksa_domain")
            composite_score = artifact.get("pass_1_scoring", {}).get("composite_score", 0.0)

            # Count decision
            if decision == "include":
                summary["included"] += 1
                included_scores.append(composite_score)
            else:
                summary["excluded"] += 1
                excluded_scores.append(composite_score)

            # Confidence breakdown
            if confidence in summary["confidence_breakdown"]:
                summary["confidence_breakdown"][confidence] += 1

            # Dimension breakdown
            if dimension in summary["dimension_breakdown"]:
                if decision == "include":
                    summary["dimension_breakdown"][dimension]["included"] += 1
                else:
                    summary["dimension_breakdown"][dimension]["excluded"] += 1

            # Domain breakdown
            if domain not in summary["domain_breakdown"]:
                summary["domain_breakdown"][domain] = {"included": 0, "excluded": 0}
            if decision == "include":
                summary["domain_breakdown"][domain]["included"] += 1
            else:
                summary["domain_breakdown"][domain]["excluded"] += 1

            # Adversarial tracking
            disagreements = artifact.get("adversarial_disagreements", 0)
            pass_3_outcome = artifact.get("pass_3_adversarial_internal", {}).get("outcome")
            pass_4_outcome = artifact.get("pass_4_adversarial_external", {}).get("outcome")

            if pass_3_outcome == "overturned":
                summary["adversarial_summary"]["pass3_overturns"] += 1
            if pass_4_outcome == "overturned":
                summary["adversarial_summary"]["pass4_overturns"] += 1
            if disagreements == 2:
                summary["adversarial_summary"]["both_overturned"] += 1
                # Check if decision was reversed
                pass_2_decision = artifact.get("pass_2_evaluation", {}).get("preliminary_decision")
                if pass_2_decision != artifact.get("final_decision"):
                    summary["adversarial_summary"]["final_reversals"] += 1

        # Compute inclusion rate
        if summary["total_evaluated"] > 0:
            summary["inclusion_rate"] = summary["included"] / summary["total_evaluated"]

        # Compute score gaps
        if included_scores:
            summary["score_distribution"]["avg_composite_included"] = sum(included_scores) / len(
                included_scores
            )
        if excluded_scores:
            summary["score_distribution"]["avg_composite_excluded"] = sum(excluded_scores) / len(
                excluded_scores
            )
        summary["score_distribution"]["score_gap"] = (
            summary["score_distribution"]["avg_composite_included"]
            - summary["score_distribution"]["avg_composite_excluded"]
        )

        return summary

    def write_summary(self, role_dir: str, summary: Dict[str, Any]) -> None:
        """Write summary.json for a role."""
        os.makedirs(role_dir, exist_ok=True)
        summary_path = os.path.join(role_dir, "summary.json")
        with open(summary_path, "w") as f:
            json.dump(summary, f, indent=2)

    def generate_mapping_file(
        self, category_code: str, roles: List[Dict[str, Any]], output_path: str
    ) -> None:
        """
        Generate role_ksa_{category}.json from artifacts.
        Includes only 'include' decisions.
        """
        mapping = {
            "schema_version": SCHEMA_VERSION,
            "category_code": category_code,
            "generated_at": datetime.utcnow().isoformat() + "Z",
            "roles": [],
        }

        for role in roles:
            role_id = role.get("role_id")
            role_dir = os.path.join(ROLE_KSA_EVAL_DIR, role_id)

            # Collect included KSAs for this role
            included_ksas = []
            if os.path.exists(role_dir):
                for filename in os.listdir(role_dir):
                    if filename.endswith(".json") and filename != "summary.json":
                        artifact_path = os.path.join(role_dir, filename)
                        with open(artifact_path) as f:
                            artifact = json.load(f)
                            if artifact.get("final_decision") == "include":
                                included_ksas.append(
                                    {
                                        "ksa_id": artifact.get("ksa_id"),
                                        "ksa_text": artifact.get("ksa_text"),
                                        "ksa_dimension": artifact.get("ksa_dimension"),
                                        "ksa_domain": artifact.get("ksa_domain"),
                                        "composite_score": artifact.get("pass_1_scoring", {}).get(
                                            "composite_score"
                                        ),
                                        "decision_confidence": artifact.get("decision_confidence"),
                                    }
                                )

            mapping["roles"].append(
                {
                    "role_id": role_id,
                    "role_name": role.get("canonical_title"),
                    "included_ksas": included_ksas,
                }
            )

        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, "w") as f:
            json.dump(mapping, f, indent=2)

    def regenerate_roadmap(self, evaluations_dir: str) -> None:
        """
        Scan all role directories and generate ROADMAP.md.
        """
        roadmap_lines = [
            "# WIDAI Role-KSA Evaluation — Progress Roadmap",
            f"Generated: {datetime.utcnow().isoformat()}Z",
            f"Pipeline Version: {PIPELINE_VERSION}",
            "",
            "## Summary",
        ]

        # Count status
        complete = 0
        in_progress = 0
        pending = 0
        total_roles = 0

        role_statuses = []

        if os.path.exists(evaluations_dir):
            for role_dir_name in sorted(os.listdir(evaluations_dir)):
                role_path = os.path.join(evaluations_dir, role_dir_name)
                if not os.path.isdir(role_path):
                    continue

                total_roles += 1

                # Check for summary.json
                summary_path = os.path.join(role_path, "summary.json")
                if os.path.exists(summary_path):
                    complete += 1
                    with open(summary_path) as f:
                        summary = json.load(f)
                    status = "complete"
                    evaluated = summary.get("total_evaluated")
                    included = summary.get("included")
                    inc_rate = summary.get("inclusion_rate", 0)
                    pass3_overturns = summary.get("adversarial_summary", {}).get("pass3_overturns", 0)
                    pass4_overturns = summary.get("adversarial_summary", {}).get("pass4_overturns", 0)
                else:
                    # Count artifacts
                    artifact_count = len(
                        [f for f in os.listdir(role_path) if f.endswith(".json") and f != "summary.json"]
                    )
                    if artifact_count > 0:
                        in_progress += 1
                        status = "in-progress"
                        evaluated = artifact_count
                        included = artifact_count  # Placeholder
                        inc_rate = "—"
                        pass3_overturns = "—"
                        pass4_overturns = "—"
                    else:
                        pending += 1
                        status = "pending"
                        evaluated = "—"
                        included = "—"
                        inc_rate = "—"
                        pass3_overturns = "—"
                        pass4_overturns = "—"

                # Extract role info from directory name or load from file
                role_id = role_dir_name
                role_name = role_dir_name  # Fallback
                category = "UNK"
                if "-" in role_id:
                    parts = role_id.split("-")
                    if len(parts) >= 2:
                        category = parts[1]

                role_statuses.append(
                    {
                        "role_id": role_id,
                        "role_name": role_name,
                        "category": category,
                        "status": status,
                        "evaluated": evaluated,
                        "included": included,
                        "inc_rate": inc_rate,
                        "pass3_overturns": pass3_overturns,
                        "pass4_overturns": pass4_overturns,
                    }
                )

        roadmap_lines.append(f"- Total roles: {total_roles}")
        roadmap_lines.append(f"- Complete: {complete} ({100*complete/max(total_roles, 1):.1f}%)")
        roadmap_lines.append(f"- In-progress: {in_progress}")
        roadmap_lines.append(f"- Pending: {pending}")
        roadmap_lines.append("")
        roadmap_lines.append("## Role Status")
        roadmap_lines.append("")
        roadmap_lines.append(
            "| Role ID | Role Name | Category | Status | KSAs Eval | Included | Inc.Rate | Pass3 | Pass4 |"
        )
        roadmap_lines.append("|---------|-----------|----------|--------|----------|----------|-----------|------|-------|")

        for rs in role_statuses:
            roadmap_lines.append(
                f"| {rs['role_id']} | {rs['role_name']} | {rs['category']} | {rs['status']} | {rs['evaluated']} | {rs['included']} | {rs['inc_rate']} | {rs['pass3_overturns']} | {rs['pass4_overturns']} |"
            )

        roadmap_path = os.path.join(evaluations_dir, "ROADMAP.md")
        with open(roadmap_path, "w") as f:
            f.write("\n".join(roadmap_lines))
