#!/usr/bin/env python3
"""
WIDAI Role-KSA Evaluation Pipeline — Main Orchestrator
Evaluates 187 WIDAI work roles against 1,069 KSAs using a 4-pass pipeline.

No pre-filtering. Every KSA evaluated for every role.
Resumable at KSA granularity.

EXECUTION MODEL
---------------
Pass 1 (--score-only): Pure Python scoring. Runs here. No LLM.
Passes 2-4: Routed to Cowork task sessions. See docs/ROLE_KSA_PIPELINE_ARCHITECTURE.md.

USAGE
-----
  python evaluate_role_ksas.py --score-only --role WIDAI-ENG-0028
      Run Pass 1 for one role. Writes pass1_batch.json.

  python evaluate_role_ksas.py --score-only --all
      Run Pass 1 for all 187 roles sequentially.

  python evaluate_role_ksas.py --status
      Show completion state across all 187 roles.
"""

import json
import sys
import os
import argparse
import logging
from datetime import datetime, timezone
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
)
from scoring import Pass1ScoringAgent


def setup_logging(log_dir: str) -> logging.Logger:
    os.makedirs(log_dir, exist_ok=True)
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    log_file = os.path.join(log_dir, f"evaluation_{timestamp}.log")
    logger = logging.getLogger("evaluation")
    logger.setLevel(logging.DEBUG)
    fh = logging.FileHandler(log_file)
    fh.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    logger.addHandler(fh)
    logger.addHandler(ch)
    return logger


def load_all_roles() -> Dict[str, Dict[str, Any]]:
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
    ksas = {}
    for ksa_file in os.listdir(KSAS_DATA_DIR):
        if not ksa_file.endswith(".json") or ksa_file == "_legacy_id_map.json":
            continue
        path = os.path.join(KSAS_DATA_DIR, ksa_file)
        with open(path) as f:
            category_data = json.load(f)
            if "entries" in category_data:
                for entry in category_data["entries"]:
                    ksa_id = entry.get("ksa_id")
                    if ksa_id:
                        ksas[ksa_id] = {
                            "id": ksa_id,
                            "text": entry.get("statement", ""),
                            "dimension": entry.get("type", ""),
                            "domain": entry.get("domain_code", ""),
                        }
    return ksas


def get_role_directory(role_id: str) -> str:
    return os.path.join(ROLE_KSA_EVAL_DIR, role_id)


def get_completed_artifacts(role_dir: str) -> set:
    if not os.path.exists(role_dir):
        return set()
    return {
        f[:-5]
        for f in os.listdir(role_dir)
        if f.endswith(".json") and f not in ("summary.json", "pass1_batch.json")
    }


def run_pass1_for_role(
    role: Dict[str, Any],
    all_ksas: Dict[str, Dict[str, Any]],
    pass1_agent: Pass1ScoringAgent,
    logger: logging.Logger,
) -> str:
    """
    Run Pass 1 for all 1,069 KSAs against a role.
    Writes docs/role_ksa_evaluations/{role_id}/pass1_batch.json.
    Returns path to the written file.
    """
    role_id = role.get("role_id")
    role_dir = get_role_directory(role_id)
    os.makedirs(role_dir, exist_ok=True)

    batch_path = os.path.join(role_dir, "pass1_batch.json")

    # Load existing batch to support resume
    existing = {}
    if os.path.exists(batch_path):
        with open(batch_path) as f:
            existing_data = json.load(f)
            existing = {item["ksa_id"]: item for item in existing_data.get("scored_ksas", [])}
        logger.info(f"  Resuming: {len(existing)} KSAs already scored")

    scored_ksas = list(existing.values())
    pending = [k for k in all_ksas.keys() if k not in existing]
    logger.info(f"  Scoring {len(pending)} KSAs for {role_id}...")

    for i, ksa_id in enumerate(pending):
        if i % 100 == 0 and i > 0:
            logger.info(f"    {i}/{len(pending)} scored")
        ksa = all_ksas[ksa_id]
        pass1_result = pass1_agent.score_ksa_for_role(ksa_id, role_id)
        scored_ksas.append({
            "ksa_id": ksa_id,
            "ksa_text": ksa.get("text", ""),
            "ksa_dimension": ksa.get("dimension", ""),
            "ksa_domain": ksa.get("domain", ""),
            "pass_1_scoring": pass1_result,
        })

    # Sort by composite score descending — highest signal first
    scored_ksas.sort(
        key=lambda x: x.get("pass_1_scoring", {}).get("composite_score", 0),
        reverse=True
    )

    batch = {
        "schema_version": SCHEMA_VERSION,
        "pipeline_version": PIPELINE_VERSION,
        "role_id": role_id,
        "role_name": role.get("canonical_title", ""),
        "role_category": role.get("category_code", ""),
        "role_description": role.get("description", ""),
        "scored_at": datetime.now(timezone.utc).isoformat(),
        "total_ksas": len(scored_ksas),
        "scored_ksas": scored_ksas,
        "next_step": (
            f"Pass 1 complete for {role_id}. "
            f"Spawn a Cowork task session to run Passes 2-4. "
            f"Input: {batch_path}"
        ),
    }

    tmp_path = batch_path + ".tmp"
    with open(tmp_path, "w") as f:
        json.dump(batch, f, indent=2)
    os.replace(tmp_path, batch_path)

    logger.info(f"  pass1_batch.json written: {len(scored_ksas)} KSAs scored")
    return batch_path


def print_status(all_roles: Dict[str, Dict[str, Any]]) -> None:
    print("\n" + "=" * 80)
    print("WIDAI ROLE-KSA EVALUATION — STATUS REPORT")
    print("=" * 80 + "\n")
    complete = in_progress = pass1_only = pending = 0
    print(f"{'Role ID':<22} {'Status':<18} {'Artifacts':<12} {'Pass1'}")
    print("-" * 80)
    for role_id in sorted(all_roles.keys()):
        role_dir = get_role_directory(role_id)
        summary_path = os.path.join(role_dir, "summary.json")
        batch_path = os.path.join(role_dir, "pass1_batch.json")
        if os.path.exists(summary_path):
            complete += 1
            status = "COMPLETE"
            with open(summary_path) as f:
                s = json.load(f)
            artifacts = str(s.get("total_evaluated", "?"))
            p1 = "✓"
        else:
            artifact_count = len(get_completed_artifacts(role_dir))
            has_batch = os.path.exists(batch_path)
            p1 = "✓" if has_batch else "—"
            if artifact_count > 0:
                in_progress += 1
                status = "EVALUATING"
                artifacts = str(artifact_count)
            elif has_batch:
                pass1_only += 1
                status = "PASS1-DONE"
                artifacts = "0"
            else:
                pending += 1
                status = "PENDING"
                artifacts = "0"
        print(f"{role_id:<22} {status:<18} {artifacts:<12} {p1}")
    print("-" * 80)
    print(f"\nSUMMARY:")
    print(f"  Total Roles:          {len(all_roles)}")
    print(f"  Complete:             {complete} ({100*complete/len(all_roles):.1f}%)")
    print(f"  Evaluating (in-prog): {in_progress}")
    print(f"  Pass 1 done (queued): {pass1_only}")
    print(f"  Pending:              {pending}")
    print(f"  Expected evaluations: {len(all_roles) * 1069:,}")
    print()


def main():
    parser = argparse.ArgumentParser(description="WIDAI Role-KSA Evaluation Pipeline")
    parser.add_argument("--role", type=str, help="Process a single role (e.g., WIDAI-ENG-0028)")
    parser.add_argument("--all", action="store_true", help="Process all 187 roles")
    parser.add_argument("--status", action="store_true", help="Print completion status and exit")
    parser.add_argument("--score-only", action="store_true", help="Run Pass 1 only (no LLM)")
    parser.add_argument("--reprocess", type=str, help="Force reprocess a role")
    args = parser.parse_args()

    logger = setup_logging(LOGS_DIR)
    logger.info("=" * 80)
    logger.info("WIDAI Role-KSA Evaluation Pipeline")
    logger.info(f"Pipeline Version: {PIPELINE_VERSION} | Schema Version: {SCHEMA_VERSION}")
    logger.info("=" * 80)

    logger.info("Loading roles and KSAs...")
    all_roles = load_all_roles()
    all_ksas = load_all_ksas()
    logger.info(f"Loaded {len(all_roles)} roles and {len(all_ksas)} KSAs")

    if args.status:
        print_status(all_roles)
        return

    if args.score_only:
        pass1_agent = Pass1ScoringAgent()
        roles_to_process = []
        if args.role:
            role = all_roles.get(args.role)
            if not role:
                logger.error(f"Role not found: {args.role}")
                sys.exit(1)
            roles_to_process = [role]
        elif args.all or args.reprocess:
            target = args.reprocess or None
            roles_to_process = (
                [all_roles[target]] if target else list(all_roles.values())
            )
        else:
            parser.print_help()
            sys.exit(1)

        for i, role in enumerate(roles_to_process):
            role_id = role.get("role_id")
            logger.info(f"[{i+1}/{len(roles_to_process)}] Pass 1: {role_id}")
            batch_path = run_pass1_for_role(role, all_ksas, pass1_agent, logger)
            logger.info(f"  Written: {batch_path}")

        logger.info("Pass 1 complete. Cowork task sessions handle Passes 2-4.")
        return

    # Full 4-pass mode is handled by Cowork task sessions, not Python directly.
    print("\nFull 4-pass evaluation runs through Cowork task sessions.")
    print("Run Pass 1 first: python evaluate_role_ksas.py --score-only --role WIDAI-ENG-0028")
    print("Then Cowork reads pass1_batch.json and runs Passes 2-4.")
    sys.exit(0)


if __name__ == "__main__":
    main()
