#!/usr/bin/env python3
"""
WIDAI Role-KSA Evaluation Pipeline — Main Orchestrator
Evaluates 187 WIDAI work roles against 1,069 KSAs using a 4-pass pipeline.

No pre-filtering. Every KSA evaluated for every role.
Resumable at KSA granularity.
"""

import json
import sys
import os
import argparse
import logging
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional

from evaluation_config import (
    BASE_DIR,
    ROLE_KSA_EVAL_DIR,
    LOGS_DIR,
    ROLES_DATA_DIR,
    KSAS_DATA_DIR,
    SCHEMA_VERSION,
    PIPELINE_VERSION,
    LLM_MODEL,
)
from scoring import Pass1ScoringAgent
from agents import (
    Pass2EvaluationAgent,
    Pass3AdversarialAgent,
    Pass4AdversarialAgent,
    EvaluationError,
)
from artifact_writer import ArtifactWriter, ArtifactValidationError


def setup_logging(log_dir: str) -> logging.Logger:
    """Set up logging to file and console."""
    os.makedirs(log_dir, exist_ok=True)
    timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    log_file = os.path.join(log_dir, f"evaluation_{timestamp}.log")

    logger = logging.getLogger("evaluation")
    logger.setLevel(logging.DEBUG)

    fh = logging.FileHandler(log_file)
    fh.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    logger.addHandler(fh)
    logger.addHandler(ch)

    return logger


def load_all_roles() -> Dict[str, Dict[str, Any]]:
    """Load all 187 WIDAI roles from category files."""
    roles = {}
    for category_file in os.listdir(ROLES_DATA_DIR):
        if not category_file.endswith(".json"):
            continue

        path = os.path.join(ROLES_DATA_DIR, category_file)
        with open(path) as f:
            category_data = json.load(f)
            if "roles" in category_data:
                for role in category_data["roles"]:
                    role_id = role.get("role_id")
                    if role_id:
                        roles[role_id] = role

    return roles


def load_all_ksas() -> Dict[str, Dict[str, Any]]:
    """Load all 1,069 KSAs from domain files."""
    ksas = {}
    for ksa_file in os.listdir(KSAS_DATA_DIR):
        if not ksa_file.endswith(".json") or ksa_file == "_legacy_id_map.json":
            continue

        path = os.path.join(KSAS_DATA_DIR, ksa_file)
        with open(path) as f:
            category_data = json.load(f)
            if "entries" in category_data:
                for entry in category_data["entries"]:
                    # KSA structure: ksa_id, type (dimension), statement (text), domain_code
                    ksa_id = entry.get("ksa_id")
                    if ksa_id:
                        ksas[ksa_id] = {
                            "id": ksa_id,
                            "text": entry.get("statement", ""),
                            "dimension": entry.get("type", ""),  # Knowledge, Skills, Abilities, Tasks
                            "domain": entry.get("domain_code", ""),
                        }

    return ksas


def get_role_directory(role_id: str) -> str:
    """Get the directory for a role's artifacts."""
    return os.path.join(ROLE_KSA_EVAL_DIR, role_id)


def get_completed_artifacts(role_dir: str) -> set:
    """Get set of KSA ids that already have artifacts."""
    if not os.path.exists(role_dir):
        return set()
    return {
        f[:-5]  # Remove .json
        for f in os.listdir(role_dir)
        if f.endswith(".json") and f != "summary.json"
    }


def load_included_ksas_from_artifacts(role_dir: str, ksas: Dict[str, Dict]) -> List[Dict[str, Any]]:
    """Load KSAs already marked as 'include' for this role."""
    included = []
    if not os.path.exists(role_dir):
        return included

    for filename in os.listdir(role_dir):
        if not filename.endswith(".json") or filename == "summary.json":
            continue

        artifact_path = os.path.join(role_dir, filename)
        with open(artifact_path) as f:
            artifact = json.load(f)
            if artifact.get("final_decision") == "include":
                ksa_id = artifact.get("ksa_id")
                included.append(
                    {
                        "id": ksa_id,
                        "text": artifact.get("ksa_text", ""),
                        "dimension": artifact.get("ksa_dimension", ""),
                        "domain": artifact.get("ksa_domain", ""),
                    }
                )

    return included


def run_4_pass_pipeline(
    role: Dict[str, Any],
    ksa: Dict[str, Any],
    pass_1_agent: Pass1ScoringAgent,
    pass_2_agent: Pass2EvaluationAgent,
    pass_3_agent: Pass3AdversarialAgent,
    pass_4_agent: Pass4AdversarialAgent,
    included_ksas: List[Dict[str, Any]],
    logger: logging.Logger,
) -> Optional[Dict[str, Any]]:
    """
    Run the full 4-pass evaluation pipeline for a single KSA-role pair.
    Returns the complete artifact dict, or None if evaluation failed.
    """
    ksa_id = ksa.get("id")
    role_id = role.get("role_id")

    try:
        # PASS 1: Scoring
        logger.debug(f"Pass 1 (scoring) for {role_id} x {ksa_id}")
        pass_1_result = pass_1_agent.score_ksa_for_role(ksa_id, role_id)

        # PASS 2: LLM Evaluation
        logger.debug(f"Pass 2 (evaluation) for {role_id} x {ksa_id}")
        pass_2_result = pass_2_agent.run(role, ksa, pass_1_result)

        # PASS 3: Adversarial Internal
        logger.debug(f"Pass 3 (adversarial internal) for {role_id} x {ksa_id}")
        pass_3_result = pass_3_agent.run(role, ksa, pass_2_result, included_ksas)

        # Handle rebuttal if Pass 3 overturned
        if pass_3_result.get("outcome") == "overturned":
            logger.debug(f"Pass 3 overturned, running rebuttal for {role_id} x {ksa_id}")
            rebuttal = pass_3_agent.run_rebuttal(
                role, ksa, pass_2_result, pass_3_result.get("challenge")
            )
            pass_3_result["rebuttal"] = rebuttal.get("rebuttal")
            pass_3_result["ruling"] = rebuttal.get("ruling")
        else:
            pass_3_result["rebuttal"] = None
            pass_3_result["ruling"] = pass_2_result.get("preliminary_decision")

        # PASS 4: Adversarial External
        logger.debug(f"Pass 4 (adversarial external) for {role_id} x {ksa_id}")
        pass_4_result = pass_4_agent.run(role, ksa, pass_2_result, pass_3_result)

        # Compute final decision
        pass_3_overturned = pass_3_result.get("outcome") == "overturned"
        pass_4_overturned = pass_4_result.get("outcome") == "overturned"
        adversarial_disagreements = (1 if pass_3_overturned else 0) + (1 if pass_4_overturned else 0)

        if adversarial_disagreements == 0:
            # Both upheld — use Pass 2 decision (or Pass 3 ruling if it overturned)
            if pass_3_overturned:
                final_decision = pass_3_result.get("ruling")
            else:
                final_decision = pass_2_result.get("preliminary_decision")
            decision_confidence = "high"
        elif adversarial_disagreements == 1:
            # One overturned — Pass 2 agent makes final call
            # For now, use the overturned agent's ruling
            if pass_3_overturned:
                final_decision = pass_3_result.get("ruling")
            else:
                final_decision = pass_4_result.get("ruling")
            decision_confidence = "medium"
        else:  # Both overturned
            # Must reverse Pass 2 decision or justify strongly
            # For now, accept the override
            final_decision = pass_4_result.get("ruling")  # or pass_3
            decision_confidence = "low"

        # Assemble artifact
        artifact = {
            "schema_version": SCHEMA_VERSION,
            "role_id": role_id,
            "role_name": role.get("canonical_title", ""),
            "ksa_id": ksa_id,
            "ksa_text": ksa.get("text", ""),
            "ksa_dimension": ksa.get("dimension", ""),
            "ksa_domain": ksa.get("domain", ""),
            "pass_1_scoring": pass_1_result,
            "pass_2_evaluation": pass_2_result,
            "pass_3_adversarial_internal": pass_3_result,
            "pass_4_adversarial_external": pass_4_result,
            "final_decision": final_decision,
            "decision_confidence": decision_confidence,
            "decision_rationale": f"All passes evaluated. {adversarial_disagreements} adversarial disagreements. Final decision: {final_decision}.",
            "adversarial_disagreements": adversarial_disagreements,
            "metadata": {
                "evaluated_at": datetime.utcnow().isoformat() + "Z",
                "model": LLM_MODEL,
                "pipeline_version": PIPELINE_VERSION,
            },
        }

        return artifact

    except EvaluationError as e:
        logger.error(f"Evaluation error for {role_id} x {ksa_id}: {e}")
        return None
    except Exception as e:
        logger.exception(f"Unexpected error for {role_id} x {ksa_id}: {e}")
        return None


def process_role(
    role: Dict[str, Any],
    all_ksas: Dict[str, Dict[str, Any]],
    pass_1_agent: Pass1ScoringAgent,
    pass_2_agent: Pass2EvaluationAgent,
    pass_3_agent: Pass3AdversarialAgent,
    pass_4_agent: Pass4AdversarialAgent,
    artifact_writer: ArtifactWriter,
    reprocess_flag: bool = False,
    logger: Optional[logging.Logger] = None,
) -> int:
    """
    Process a single role: evaluate all KSAs against it.
    Returns number of KSAs successfully evaluated.
    """
    if logger is None:
        logger = logging.getLogger("evaluation")

    role_id = role.get("role_id")
    role_dir = get_role_directory(role_id)

    # Check if already complete
    summary_path = os.path.join(role_dir, "summary.json")
    if os.path.exists(summary_path) and not reprocess_flag:
        logger.info(f"Role {role_id} already complete, skipping")
        return 0

    # Load current state
    completed_ksas = get_completed_artifacts(role_dir)
    pending_ksas = [k for k in all_ksas.keys() if k not in completed_ksas]

    logger.info(
        f"Role {role_id}: {len(completed_ksas)} complete, {len(pending_ksas)} pending"
    )

    # Load included KSAs for consistency checking in Pass 3
    included_ksas = load_included_ksas_from_artifacts(role_dir, all_ksas)

    # Process pending KSAs
    successful = 0
    for i, ksa_id in enumerate(pending_ksas):
        if i % 50 == 0 and i > 0:
            logger.info(f"  Progress: {i}/{len(pending_ksas)} ({100*i/len(pending_ksas):.1f}%)")

        ksa = all_ksas[ksa_id]
        artifact = run_4_pass_pipeline(
            role,
            ksa,
            pass_1_agent,
            pass_2_agent,
            pass_3_agent,
            pass_4_agent,
            included_ksas,
            logger,
        )

        if artifact:
            try:
                artifact_writer.write_artifact(role_dir, ksa_id, artifact)
                successful += 1
                # Add to included list if it's an include decision
                if artifact.get("final_decision") == "include":
                    included_ksas.append(
                        {
                            "id": ksa_id,
                            "text": artifact.get("ksa_text", ""),
                            "dimension": artifact.get("ksa_dimension", ""),
                            "domain": artifact.get("ksa_domain", ""),
                        }
                    )
            except ArtifactValidationError as e:
                logger.error(f"Artifact validation failed for {role_id} x {ksa_id}: {e}")

    logger.info(f"Role {role_id}: {successful}/{len(pending_ksas)} successfully evaluated")

    # Write summary
    summary = artifact_writer.compute_summary(role, role_dir)
    artifact_writer.write_summary(role_dir, summary)
    logger.info(f"Summary written for {role_id}")

    # Regenerate roadmap
    artifact_writer.regenerate_roadmap(ROLE_KSA_EVAL_DIR)

    return successful


def print_status(all_roles: Dict[str, Dict[str, Any]]) -> None:
    """Print completion status and exit."""
    print("\n" + "=" * 80)
    print("WIDAI ROLE-KSA EVALUATION — STATUS REPORT")
    print("=" * 80 + "\n")

    complete = 0
    in_progress = 0
    pending = 0

    print(f"{'Role ID':<20} {'Status':<15} {'Artifacts':<10}")
    print("-" * 80)

    for role_id in sorted(all_roles.keys()):
        role_dir = get_role_directory(role_id)
        summary_path = os.path.join(role_dir, "summary.json")

        if os.path.exists(summary_path):
            complete += 1
            status = "COMPLETE"
            with open(summary_path) as f:
                summary = json.load(f)
            artifacts = str(summary.get("total_evaluated", "?"))
        else:
            artifact_count = len(
                [f for f in os.listdir(role_dir) if f.endswith(".json") and f != "summary.json"]
            ) if os.path.exists(role_dir) else 0
            if artifact_count > 0:
                in_progress += 1
                status = "IN-PROGRESS"
                artifacts = str(artifact_count)
            else:
                pending += 1
                status = "PENDING"
                artifacts = "0"

        print(f"{role_id:<20} {status:<15} {artifacts:<10}")

    print("-" * 80)
    print(f"\nSUMMARY:")
    print(f"  Total Roles: {len(all_roles)}")
    print(f"  Complete: {complete} ({100*complete/len(all_roles):.1f}%)")
    print(f"  In-Progress: {in_progress}")
    print(f"  Pending: {pending}")
    print(f"  Expected Total Evaluations: {len(all_roles) * 1069}")
    print()


def main():
    parser = argparse.ArgumentParser(
        description="WIDAI Role-KSA Evaluation Pipeline"
    )
    parser.add_argument(
        "--role",
        type=str,
        help="Process a single role (e.g., WIDAI-ENG-0028)",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Process all 187 roles sequentially",
    )
    parser.add_argument(
        "--status",
        action="store_true",
        help="Print completion status and exit",
    )
    parser.add_argument(
        "--reprocess",
        type=str,
        help="Force reprocess a role even if summary.json exists",
    )

    args = parser.parse_args()

    # Setup logging
    logger = setup_logging(LOGS_DIR)
    logger.info("=" * 80)
    logger.info("WIDAI Role-KSA Evaluation Pipeline Started")
    logger.info(f"Pipeline Version: {PIPELINE_VERSION}")
    logger.info(f"Schema Version: {SCHEMA_VERSION}")
    logger.info(f"LLM Model: {LLM_MODEL}")
    logger.info("=" * 80)

    # Load data
    logger.info("Loading roles and KSAs...")
    all_roles = load_all_roles()
    all_ksas = load_all_ksas()
    logger.info(f"Loaded {len(all_roles)} roles and {len(all_ksas)} KSAs")

    # Handle --status
    if args.status:
        print_status(all_roles)
        return

    # Initialize agents and writer
    pass_1_agent = Pass1ScoringAgent()
    pass_2_agent = Pass2EvaluationAgent()
    pass_3_agent = Pass3AdversarialAgent()
    pass_4_agent = Pass4AdversarialAgent()
    artifact_writer = ArtifactWriter()

    # Process roles
    if args.reprocess:
        role = all_roles.get(args.reprocess)
        if not role:
            logger.error(f"Role not found: {args.reprocess}")
            sys.exit(1)
        logger.info(f"Reprocessing role {args.reprocess}")
        process_role(
            role,
            all_ksas,
            pass_1_agent,
            pass_2_agent,
            pass_3_agent,
            pass_4_agent,
            artifact_writer,
            reprocess_flag=True,
            logger=logger,
        )
    elif args.role:
        role = all_roles.get(args.role)
        if not role:
            logger.error(f"Role not found: {args.role}")
            sys.exit(1)
        logger.info(f"Processing role {args.role}")
        process_role(
            role,
            all_ksas,
            pass_1_agent,
            pass_2_agent,
            pass_3_agent,
            pass_4_agent,
            artifact_writer,
            logger=logger,
        )
    elif args.all:
        logger.info("Processing all 187 roles...")
        for i, (role_id, role) in enumerate(sorted(all_roles.items())):
            logger.info(f"[{i+1}/{len(all_roles)}] Processing {role_id}")
            process_role(
                role,
                all_ksas,
                pass_1_agent,
                pass_2_agent,
                pass_3_agent,
                pass_4_agent,
                artifact_writer,
                logger=logger,
            )
    else:
        parser.print_help()
        sys.exit(1)

    logger.info("=" * 80)
    logger.info("Pipeline completed")
    logger.info("=" * 80)


if __name__ == "__main__":
    main()
