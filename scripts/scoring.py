"""
WIDAI Role-KSA Evaluation — Pass 1: Python Scoring Agent
No LLM. Pure programmatic scoring against STRM data.

Loads ALL available STRM frameworks automatically by scanning strm/.
Every framework with a strm_mapping.json is included in scoring.
No hardcoded framework list — if a new framework is added to strm/, it
appears in Pass 1 output automatically.
"""

import json
import os
from typing import Dict, List, Any, Optional
from evaluation_config import (
    METRIC_WEIGHTS,
    SIGNAL_THRESHOLDS,
    STRM_DIR,
    SCHEMA_VERSION,
)


class Pass1ScoringAgent:
    """Computes Pass 1 score block from STRM data. Loads all available frameworks."""

    def __init__(self):
        self.strm_data = self._load_all_strm_frameworks()

    def _load_all_strm_frameworks(self) -> Dict[str, Dict[str, List[Dict[str, Any]]]]:
        """
        Auto-discover and load all STRM frameworks.
        Scans strm/ for subdirectories containing strm_mapping.json.
        Returns {framework_name: {ksa_id: [mappings]}}
        """
        strm_by_framework = {}

        if not os.path.isdir(STRM_DIR):
            print(f"Warning: STRM directory not found: {STRM_DIR}")
            return strm_by_framework

        for entry in sorted(os.listdir(STRM_DIR)):
            framework_dir = os.path.join(STRM_DIR, entry)
            mapping_file = os.path.join(framework_dir, "strm_mapping.json")

            if not os.path.isdir(framework_dir) or not os.path.isfile(mapping_file):
                continue

            framework_name = entry  # e.g. "dcwf", "nice", "nist_ai_rmf"
            try:
                with open(mapping_file) as f:
                    data = json.load(f)

                if "mappings" not in data:
                    print(f"Warning: {mapping_file} has no 'mappings' key — skipping")
                    continue

                mappings_by_ksa: Dict[str, List[Dict[str, Any]]] = {}
                for mapping in data["mappings"]:
                    ksa_id = mapping.get("ref_id")
                    if ksa_id:
                        if ksa_id not in mappings_by_ksa:
                            mappings_by_ksa[ksa_id] = []
                        mappings_by_ksa[ksa_id].append(mapping)

                strm_by_framework[framework_name] = mappings_by_ksa
                print(f"  Loaded STRM: {framework_name} ({len(data['mappings']):,} mappings, "
                      f"{len(mappings_by_ksa):,} unique KSAs)")

            except Exception as e:
                print(f"Warning: Failed to load STRM for {framework_name}: {e}")

        return strm_by_framework

    def score_ksa_for_role(self, ksa_id: str, role_id: str) -> Dict[str, Any]:
        """
        Compute Pass 1 score block for a KSA-role pair.
        Includes scores from ALL loaded frameworks.
        Returns valid score block with 0.0 composite if no STRM data.
        """
        pass_1_block = {
            "composite_score": 0.0,
            "signal_strength": "none",
            "framework_scores": {},
            "top_anchors": [],
            "frameworks_with_signal": [],
            "frameworks_no_signal": [],
            "metrics_used": [],
            "metrics_absent": list(METRIC_WEIGHTS.keys()),
        }

        all_anchors = []

        for framework, mappings_by_ksa in self.strm_data.items():
            if ksa_id not in mappings_by_ksa:
                pass_1_block["frameworks_no_signal"].append(framework)
                continue

            mappings = mappings_by_ksa[ksa_id]
            if not mappings:
                pass_1_block["frameworks_no_signal"].append(framework)
                continue

            metrics = self._aggregate_metrics(mappings)
            available = {k: v for k, v in metrics.items() if v is not None}

            if not available:
                pass_1_block["frameworks_no_signal"].append(framework)
                continue

            framework_composite = self._compute_composite_score(available)
            top_element = self._get_top_element(mappings)

            framework_scores = {
                "composite": framework_composite,
                **metrics,
            }
            if top_element:
                framework_scores["top_element_id"] = top_element["id"]
                framework_scores["top_element_label"] = top_element["label"]
                all_anchors.append({
                    "framework": framework,
                    "element_id": top_element["id"],
                    "element_label": top_element["label"],
                    "score": framework_composite,
                })

            pass_1_block["framework_scores"][framework] = framework_scores
            pass_1_block["frameworks_with_signal"].append(framework)

        # Overall composite = max across all frameworks
        if pass_1_block["framework_scores"]:
            overall_composite = max(
                fs["composite"] for fs in pass_1_block["framework_scores"].values()
            )
        else:
            overall_composite = 0.0

        pass_1_block["composite_score"] = overall_composite
        pass_1_block["signal_strength"] = self._classify_signal_strength(overall_composite)
        pass_1_block["top_anchors"] = sorted(all_anchors, key=lambda x: x["score"], reverse=True)[:5]

        # Track metrics coverage
        if pass_1_block["framework_scores"]:
            seen = set()
            for fs in pass_1_block["framework_scores"].values():
                for m in METRIC_WEIGHTS.keys():
                    if fs.get(m) is not None:
                        seen.add(m)
            pass_1_block["metrics_used"] = sorted(seen)
            pass_1_block["metrics_absent"] = sorted(m for m in METRIC_WEIGHTS.keys() if m not in seen)

        return pass_1_block

    def _aggregate_metrics(self, mappings: List[Dict[str, Any]]) -> Dict[str, Optional[float]]:
        """Average metrics across all mappings for this KSA in a framework."""
        buckets: Dict[str, List[float]] = {m: [] for m in METRIC_WEIGHTS.keys()}

        for mapping in mappings:
            # Canonical field name mapping from STRM raw fields
            if mapping.get("sts_raw") is not None:
                buckets["cross_encoder_sts"].append(mapping["sts_raw"])
            if mapping.get("bienc_score") is not None:
                buckets["bi_encoder_cosine"].append(mapping["bienc_score"])
            # Additional metrics if present in data
            for alt_name, canonical in [
                ("nli_score", "nli_score"),
                ("bertscore", "bertscore"),
                ("jaccard", "jaccard"),
            ]:
                if mapping.get(alt_name) is not None:
                    buckets[canonical].append(mapping[alt_name])

        return {
            metric: (sum(vals) / len(vals) if vals else None)
            for metric, vals in buckets.items()
        }

    def _compute_composite_score(self, available_metrics: Dict[str, float]) -> float:
        """Weighted composite with renormalization for absent metrics."""
        weight_sum = sum(METRIC_WEIGHTS.get(m, 0) for m in available_metrics)
        if weight_sum == 0:
            return 0.0
        composite = sum(
            v * (METRIC_WEIGHTS.get(m, 0) / weight_sum)
            for m, v in available_metrics.items()
        )
        return min(1.0, max(0.0, composite))

    def _classify_signal_strength(self, score: float) -> str:
        if score >= SIGNAL_THRESHOLDS["strong"]:
            return "strong"
        elif score >= SIGNAL_THRESHOLDS["moderate"]:
            return "moderate"
        elif score >= SIGNAL_THRESHOLDS["weak"]:
            return "weak"
        return "none"

    def _get_top_element(self, mappings: List[Dict[str, Any]]) -> Optional[Dict[str, str]]:
        """Get highest-strength element from a framework's mappings for this KSA."""
        if not mappings:
            return None
        top = max(mappings, key=lambda m: m.get("strength", 0))
        return {
            "id": top.get("fde_id", ""),
            "label": top.get("fde_name") or top.get("fde_description", ""),
        }
