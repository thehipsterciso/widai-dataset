"""
WIDAI Role-KSA Evaluation — Pass 1: Python Scoring Agent
No LLM. Pure programmatic scoring against STRM data.
"""

import json
from typing import Dict, List, Any, Optional
from evaluation_config import (
    METRIC_WEIGHTS,
    SIGNAL_THRESHOLDS,
    BASE_DIR,
    STRM_MAPPING_FILE,
    STRM_DDAT_FILE,
    SCHEMA_VERSION,
)


class Pass1ScoringAgent:
    """Computes Pass 1 score block from STRM data."""

    def __init__(self):
        """Initialize with STRM data."""
        self.strm_data = self._load_strm_data()

    def _load_strm_data(self) -> Dict[str, List[Dict[str, Any]]]:
        """Load STRM mapping data from files. Handle both consolidated and per-framework."""
        strm_by_framework = {}

        # Try to load consolidated DCWF STRM
        try:
            with open(STRM_MAPPING_FILE) as f:
                dcwf_data = json.load(f)
                if "mappings" in dcwf_data:
                    # Normalize into keyed-by-KSA structure for easier lookup
                    mappings_by_ksa = {}
                    for mapping in dcwf_data["mappings"]:
                        ksa_id = mapping.get("ref_id")
                        if ksa_id:
                            if ksa_id not in mappings_by_ksa:
                                mappings_by_ksa[ksa_id] = []
                            mappings_by_ksa[ksa_id].append(mapping)
                    strm_by_framework["dcwf"] = mappings_by_ksa
        except FileNotFoundError:
            pass
        except Exception as e:
            print(f"Warning: Failed to load DCWF STRM: {e}")

        # Try to load per-framework DDAT STRM
        try:
            with open(STRM_DDAT_FILE) as f:
                ddat_data = json.load(f)
                if "mappings" in ddat_data:
                    mappings_by_ksa = {}
                    for mapping in ddat_data["mappings"]:
                        ksa_id = mapping.get("ref_id")
                        if ksa_id:
                            if ksa_id not in mappings_by_ksa:
                                mappings_by_ksa[ksa_id] = []
                            mappings_by_ksa[ksa_id].append(mapping)
                    strm_by_framework["ddat"] = mappings_by_ksa
        except FileNotFoundError:
            pass
        except Exception as e:
            print(f"Warning: Failed to load DDAT STRM: {e}")

        return strm_by_framework

    def score_ksa_for_role(self, ksa_id: str, role_id: str) -> Dict[str, Any]:
        """
        Compute Pass 1 score block for a given KSA-role pair.

        Returns a dict conforming to the pass_1_scoring schema.
        Never raises on missing data. Returns valid score block with 0.0 composite if no STRM data.
        """
        pass_1_block = {
            "composite_score": 0.0,
            "signal_strength": "none",
            "framework_scores": {},
            "top_anchors": [],
            "metrics_used": [],
            "metrics_absent": list(METRIC_WEIGHTS.keys()),
        }

        # Collect scores from all frameworks
        all_anchors = []  # (framework, element_id, element_label, score)

        for framework, mappings_by_ksa in self.strm_data.items():
            if ksa_id not in mappings_by_ksa:
                continue

            # Get all mappings for this KSA in this framework
            mappings = mappings_by_ksa[ksa_id]

            # Extract metrics from first mapping (assuming consistent structure)
            if not mappings:
                continue

            # Aggregate metrics across mappings for this KSA-framework pair
            metrics_for_framework = self._aggregate_metrics(mappings)
            if not metrics_for_framework:
                continue

            # Compute composite for this framework
            available_metrics = {k: v for k, v in metrics_for_framework.items() if v is not None}
            if available_metrics:
                framework_composite = self._compute_composite_score(available_metrics)
                framework_scores = {
                    "composite": framework_composite,
                    **metrics_for_framework,
                }

                # Identify top element for this framework
                top_element_info = self._get_top_element(mappings)
                if top_element_info:
                    framework_scores["top_element_id"] = top_element_info["id"]
                    framework_scores["top_element_label"] = top_element_info["label"]
                    all_anchors.append(
                        {
                            "framework": framework,
                            "element_id": top_element_info["id"],
                            "element_label": top_element_info["label"],
                            "score": framework_composite,
                        }
                    )

                pass_1_block["framework_scores"][framework] = framework_scores

        # Overall composite is the max across frameworks
        if pass_1_block["framework_scores"]:
            overall_composite = max(
                fs["composite"] for fs in pass_1_block["framework_scores"].values()
            )
        else:
            overall_composite = 0.0

        pass_1_block["composite_score"] = overall_composite
        pass_1_block["signal_strength"] = self._classify_signal_strength(overall_composite)

        # Top 3 anchors
        sorted_anchors = sorted(all_anchors, key=lambda x: x["score"], reverse=True)
        pass_1_block["top_anchors"] = sorted_anchors[:3]

        # Track which metrics were used and which were absent
        if pass_1_block["framework_scores"]:
            all_metrics_seen = set()
            for fs in pass_1_block["framework_scores"].values():
                for metric_key in METRIC_WEIGHTS.keys():
                    if metric_key in fs and fs[metric_key] is not None:
                        all_metrics_seen.add(metric_key)
            pass_1_block["metrics_used"] = sorted(list(all_metrics_seen))
            pass_1_block["metrics_absent"] = sorted([m for m in METRIC_WEIGHTS.keys() if m not in all_metrics_seen])
        else:
            pass_1_block["metrics_used"] = []
            pass_1_block["metrics_absent"] = list(METRIC_WEIGHTS.keys())

        return pass_1_block

    def _aggregate_metrics(self, mappings: List[Dict[str, Any]]) -> Dict[str, Optional[float]]:
        """Extract and average metrics from multiple mappings."""
        metric_values = {metric: [] for metric in METRIC_WEIGHTS.keys()}

        for mapping in mappings:
            # Map from the actual STRM field names to our canonical ones
            metric_values["cross_encoder_sts"].append(mapping.get("sts_raw"))
            metric_values["bi_encoder_cosine"].append(mapping.get("bienc_score"))
            # Note: nli_score, bertscore, jaccard may not be present in all STRM files
            if "nli_score" in mapping:
                metric_values["nli_score"].append(mapping.get("nli_score"))
            if "bertscore" in mapping:
                metric_values["bertscore"].append(mapping.get("bertscore"))
            if "jaccard" in mapping:
                metric_values["jaccard"].append(mapping.get("jaccard"))

        # Average non-None values
        aggregated = {}
        for metric, values in metric_values.items():
            non_none = [v for v in values if v is not None]
            if non_none:
                aggregated[metric] = sum(non_none) / len(non_none)
            else:
                aggregated[metric] = None

        return aggregated

    def _compute_composite_score(self, available_metrics: Dict[str, float]) -> float:
        """Compute weighted composite from available metrics. Renormalize weights if some are absent."""
        if not available_metrics:
            return 0.0

        # Renormalize weights across available metrics
        available_weight_sum = sum(METRIC_WEIGHTS.get(m, 0) for m in available_metrics.keys())
        if available_weight_sum == 0:
            return 0.0

        composite = 0.0
        for metric, value in available_metrics.items():
            original_weight = METRIC_WEIGHTS.get(metric, 0)
            renormalized_weight = original_weight / available_weight_sum
            composite += value * renormalized_weight

        return min(1.0, max(0.0, composite))  # Clamp to [0, 1]

    def _classify_signal_strength(self, composite_score: float) -> str:
        """Classify signal strength based on thresholds."""
        if composite_score >= SIGNAL_THRESHOLDS["strong"]:
            return "strong"
        elif composite_score >= SIGNAL_THRESHOLDS["moderate"]:
            return "moderate"
        elif composite_score >= SIGNAL_THRESHOLDS["weak"]:
            return "weak"
        else:
            return "none"

    def _get_top_element(self, mappings: List[Dict[str, Any]]) -> Optional[Dict[str, str]]:
        """Get the top-scoring element from mappings."""
        # Sort by strength or score, take the top
        sorted_mappings = sorted(
            mappings, key=lambda m: m.get("strength", 0), reverse=True
        )
        if sorted_mappings:
            top = sorted_mappings[0]
            return {
                "id": top.get("fde_id", "unknown"),
                "label": top.get("fde_name", top.get("fde_description", "unknown")),
            }
        return None


def score_ksa_for_role(ksa_id: str, role_id: str) -> Dict[str, Any]:
    """Public interface for Pass 1 scoring."""
    agent = Pass1ScoringAgent()
    return agent.score_ksa_for_role(ksa_id, role_id)
