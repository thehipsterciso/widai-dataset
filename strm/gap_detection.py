#!/usr/bin/env python3
"""
WIDAI Gap Detection Script
==========================

Retroactive per-FDE gap signal detection for all STRM rationale files.
Reads existing multi-method scores from rationale JSON files and applies
gap detection criteria to populate the gap_signal field.

This script does NOT re-run ML pipelines. All scores are already captured
in the rationale files from the original scoring runs.

Gap Signal Criteria (three independent triggers):

  1. DOMAIN MISMATCH (NLI contradiction > threshold)
     NLI detects that the FDE and matched KSA operate in different
     professional domains despite STS surface similarity.
     - Critical: contradiction > 0.80 AND relationship is Equal or Superset
     - Moderate: contradiction > 0.50

  2. THRESHOLD FRAGILITY (STS barely above classification boundary)
     The match is classified as a relationship but STS is within the
     margin zone, indicating weak coverage.
     - Moderate: STS 0.50-0.55 classified as Superset/Equal
     - Low: STS 0.55-0.60 classified as Equal (jumped a tier)

  3. VOCABULARY INFLATION (bi-encoder >> STS gap)
     Bi-encoder candidate selection was driven by shared vocabulary
     rather than functional alignment. The functionally correct KSA
     may not have been in the top-5 candidates.
     - Moderate: gap > 0.15 with STS < 0.60
     - Low: gap > 0.12

Severity levels:
  - critical:  Domain mismatch on Equal/Superset classification
  - moderate:  Any single moderate-level trigger
  - low:       Informational flags only

Output: Updated rationale files with gap_signal populated, plus a
        per-STRM gap detection summary JSON.

Usage:
    python3 gap_detection.py                  # all STRMs
    python3 gap_detection.py eu_ai_act        # single STRM
    python3 gap_detection.py --dry-run        # analysis only, no file writes
"""

import json
import os
import sys
import glob
from datetime import date
from collections import defaultdict

TODAY = date.today().isoformat()

STRM_DIRS = {
    "onet":       {"rationale": "onet/rationale",       "strm_id": "STRM-001-ONET"},
    "nice":       {"rationale": "nice/rationale",       "strm_id": "STRM-002-NICE"},
    "dcwf":       {"rationale": "dcwf/rationale",       "strm_id": "STRM-003-DCWF"},
    "ddat":       {"rationale": "ddat/rationale",       "strm_id": "STRM-004-DDAT"},
    "eu_ai_act":  {"rationale": "eu_ai_act/rationale",  "strm_id": "STRM-005-EU-AI-ACT"},
}

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


def extract_scores(rationale):
    """Extract scoring data from a rationale file."""
    sj = rationale.get("strength_justification", {})
    pm = sj.get("primary_method")
    sm = sj.get("secondary_methods")

    if not pm or not sm:
        return None

    nli = sm.get("nli_cross_encoder", {})
    bienc = sm.get("biencoder_cosine", {})

    return {
        "sts_raw": pm.get("raw_score_0_1", 0),
        "sts_strength": pm.get("mapped_strength_0_10", 0),
        "contradiction": nli.get("contradiction", 0),
        "entailment": nli.get("entailment", 0),
        "neutral": nli.get("neutral", 0),
        "bienc_cosine": bienc.get("cosine_similarity_0_1", 0),
        "bertscore_f1": sm.get("bertscore", {}).get("f1", 0),
        "jaccard": sm.get("jaccard_token", {}).get("similarity_0_1", 0),
    }


def detect_gap_signals(scores, relationship):
    """Apply gap detection criteria. Returns list of gap signal dicts."""
    signals = []
    sts = scores["sts_raw"]
    contra = scores["contradiction"]
    bienc = scores["bienc_cosine"]
    bienc_gap = bienc - sts

    # ── Criterion 1: Domain Mismatch (NLI contradiction) ──
    if contra > 0.80 and relationship in ("Equal", "Superset of"):
        signals.append({
            "criterion": "domain_mismatch",
            "severity": "critical",
            "detail": (
                f"NLI contradiction {contra:.1%} on {relationship} classification. "
                f"The matched KSA operates in a different professional domain "
                f"than the obligation/competency requires. STS {sts:.3f} passed "
                f"the threshold but secondary signals contradict the match."
            ),
            "scores": {
                "nli_contradiction": round(contra, 4),
                "sts_raw": round(sts, 4),
                "relationship": relationship,
            }
        })
    elif contra > 0.50:
        signals.append({
            "criterion": "domain_mismatch",
            "severity": "moderate",
            "detail": (
                f"NLI contradiction {contra:.1%} suggests semantic tension "
                f"between the FDE and matched KSA. The competency domains "
                f"may be adjacent but not functionally aligned."
            ),
            "scores": {
                "nli_contradiction": round(contra, 4),
                "sts_raw": round(sts, 4),
                "relationship": relationship,
            }
        })

    # ── Criterion 2: Threshold Fragility ──
    if sts < 0.55 and relationship in ("Superset of", "Equal"):
        signals.append({
            "criterion": "threshold_fragility",
            "severity": "moderate",
            "detail": (
                f"STS {sts:.3f} barely clears classification threshold "
                f"for {relationship}. This match is fragile and may "
                f"indicate insufficient KSA coverage for this competency area."
            ),
            "scores": {
                "sts_raw": round(sts, 4),
                "threshold": 0.50 if relationship == "Superset of" else 0.65,
                "margin": round(sts - (0.50 if relationship == "Superset of" else 0.65), 4),
            }
        })
    elif 0.55 <= sts < 0.60 and relationship == "Equal":
        signals.append({
            "criterion": "threshold_fragility",
            "severity": "low",
            "detail": (
                f"STS {sts:.3f} classified as Equal but closer to Superset "
                f"threshold. Classification may be over-generous."
            ),
            "scores": {
                "sts_raw": round(sts, 4),
                "threshold": 0.65,
                "margin": round(sts - 0.65, 4),
            }
        })

    # ── Criterion 3: Vocabulary Inflation ──
    if bienc_gap > 0.15 and sts < 0.60:
        signals.append({
            "criterion": "vocabulary_inflation",
            "severity": "moderate",
            "detail": (
                f"Bi-encoder/STS gap {bienc_gap:.3f} with low STS {sts:.3f}. "
                f"Candidate selection was likely driven by shared vocabulary "
                f"rather than functional alignment. The functionally correct "
                f"KSA may not have been in the top-5 candidates."
            ),
            "scores": {
                "biencoder_cosine": round(bienc, 4),
                "sts_raw": round(sts, 4),
                "gap": round(bienc_gap, 4),
            }
        })
    elif bienc_gap > 0.12:
        signals.append({
            "criterion": "vocabulary_inflation",
            "severity": "low",
            "detail": (
                f"Bi-encoder/STS gap {bienc_gap:.3f} suggests some vocabulary-"
                f"driven inflation in candidate selection."
            ),
            "scores": {
                "biencoder_cosine": round(bienc, 4),
                "sts_raw": round(sts, 4),
                "gap": round(bienc_gap, 4),
            }
        })

    return signals


def compute_overall_severity(signals):
    """Compute the highest severity across all signals."""
    if not signals:
        return None
    severities = [s["severity"] for s in signals]
    if "critical" in severities:
        return "critical"
    if "moderate" in severities:
        return "moderate"
    return "low"


def build_gap_signal(signals):
    """Build the gap_signal object for a rationale file."""
    if not signals:
        return None

    severity = compute_overall_severity(signals)
    criteria = [s["criterion"] for s in signals]

    return {
        "severity": severity,
        "criteria_triggered": sorted(set(criteria)),
        "signal_count": len(signals),
        "signals": signals,
        "detection_date": TODAY,
        "detection_method": "Retroactive multi-method signal analysis (gap_detection.py)"
    }


def process_strm(strm_key, dry_run=False):
    """Process all rationale files for a single STRM."""
    config = STRM_DIRS[strm_key]
    rationale_dir = os.path.join(SCRIPT_DIR, config["rationale"])
    strm_id = config["strm_id"]

    files = sorted(glob.glob(os.path.join(rationale_dir, "*.json")))
    if not files:
        print(f"  WARNING: No rationale files found in {rationale_dir}")
        return None

    results = {
        "strm_id": strm_id,
        "strm_key": strm_key,
        "total_elements": len(files),
        "elements_with_gaps": 0,
        "severity_counts": {"critical": 0, "moderate": 0, "low": 0},
        "criterion_counts": {"domain_mismatch": 0, "threshold_fragility": 0, "vocabulary_inflation": 0},
        "flagged_elements": [],
        "files_updated": 0,
    }

    for fp in files:
        with open(fp) as f:
            rationale = json.load(f)

        scores = extract_scores(rationale)
        if not scores:
            continue

        relationship = rationale.get("relationship", "")
        fde_id = rationale.get("fde_id", rationale.get("focal_document_element", ""))
        ref_id = rationale.get("reference_document_element", "")

        signals = detect_gap_signals(scores, relationship)
        gap_signal = build_gap_signal(signals)

        if gap_signal:
            results["elements_with_gaps"] += 1
            severity = gap_signal["severity"]
            results["severity_counts"][severity] += 1
            for criterion in gap_signal["criteria_triggered"]:
                results["criterion_counts"][criterion] += 1

            results["flagged_elements"].append({
                "fde_id": fde_id,
                "ref_id": ref_id,
                "relationship": relationship,
                "severity": severity,
                "criteria": gap_signal["criteria_triggered"],
                "sts_raw": scores["sts_raw"],
                "nli_contradiction": scores["contradiction"],
                "bienc_cosine": scores["bienc_cosine"],
            })

        # Update rationale file
        if not dry_run:
            rationale["gap_signal"] = gap_signal
            with open(fp, "w") as f:
                json.dump(rationale, f, indent=2)
            if gap_signal:
                results["files_updated"] += 1

    # Sort flagged elements by severity then contradiction
    severity_order = {"critical": 0, "moderate": 1, "low": 2}
    results["flagged_elements"].sort(
        key=lambda x: (severity_order.get(x["severity"], 3), -x["nli_contradiction"])
    )

    return results


def write_summary(all_results, dry_run=False):
    """Write the gap detection summary to a JSON file."""
    summary = {
        "gap_detection_run": {
            "date": TODAY,
            "script": "gap_detection.py",
            "mode": "dry-run" if dry_run else "live",
            "description": (
                "Retroactive per-FDE gap signal detection applied to all STRM "
                "rationale files. Criteria: (1) NLI domain mismatch, "
                "(2) STS threshold fragility, (3) bi-encoder vocabulary inflation."
            ),
        },
        "aggregate": {
            "total_elements": sum(r["total_elements"] for r in all_results),
            "total_gaps": sum(r["elements_with_gaps"] for r in all_results),
            "total_critical": sum(r["severity_counts"]["critical"] for r in all_results),
            "total_moderate": sum(r["severity_counts"]["moderate"] for r in all_results),
            "total_low": sum(r["severity_counts"]["low"] for r in all_results),
        },
        "per_strm": [],
    }

    for r in all_results:
        summary["per_strm"].append({
            "strm_id": r["strm_id"],
            "total_elements": r["total_elements"],
            "elements_with_gaps": r["elements_with_gaps"],
            "gap_rate": round(r["elements_with_gaps"] / r["total_elements"] * 100, 1)
                if r["total_elements"] > 0 else 0,
            "severity_counts": r["severity_counts"],
            "criterion_counts": r["criterion_counts"],
            "critical_elements": [
                e for e in r["flagged_elements"] if e["severity"] == "critical"
            ],
            "moderate_elements": [
                e for e in r["flagged_elements"] if e["severity"] == "moderate"
            ],
        })

    if not dry_run:
        out_path = os.path.join(SCRIPT_DIR, "gap_detection_summary.json")
        with open(out_path, "w") as f:
            json.dump(summary, f, indent=2)
        print(f"\nSummary written to {out_path}")

    return summary


def main():
    args = sys.argv[1:]
    dry_run = "--dry-run" in args
    args = [a for a in args if a != "--dry-run"]

    if args:
        targets = [a for a in args if a in STRM_DIRS]
        if not targets:
            print(f"Unknown STRM(s): {args}. Available: {list(STRM_DIRS.keys())}")
            sys.exit(1)
    else:
        targets = list(STRM_DIRS.keys())

    mode = "DRY RUN" if dry_run else "LIVE (updating files)"
    print(f"WIDAI Gap Detection — {mode}")
    print(f"Date: {TODAY}")
    print(f"Targets: {', '.join(targets)}\n")

    all_results = []
    for strm_key in targets:
        print(f"Processing {STRM_DIRS[strm_key]['strm_id']}...")
        result = process_strm(strm_key, dry_run=dry_run)
        if result:
            all_results.append(result)
            total = result["total_elements"]
            gaps = result["elements_with_gaps"]
            crit = result["severity_counts"]["critical"]
            mod = result["severity_counts"]["moderate"]
            low = result["severity_counts"]["low"]
            print(f"  {total} elements → {gaps} gaps "
                  f"({crit} critical, {mod} moderate, {low} low)")
            if crit > 0:
                print(f"  CRITICAL elements:")
                for e in result["flagged_elements"]:
                    if e["severity"] == "critical":
                        print(f"    {e['fde_id']} -> {e['ref_id']}  "
                              f"NLI-C={e['nli_contradiction']:.1%}  "
                              f"STS={e['sts_raw']:.3f}  "
                              f"Rel={e['relationship']}")
        print()

    summary = write_summary(all_results, dry_run=dry_run)

    # Print aggregate
    agg = summary["aggregate"]
    print("=" * 60)
    print(f"AGGREGATE: {agg['total_elements']} elements, {agg['total_gaps']} gaps")
    print(f"  Critical: {agg['total_critical']}")
    print(f"  Moderate: {agg['total_moderate']}")
    print(f"  Low:      {agg['total_low']}")

    if dry_run:
        print("\nDry run complete. No files were modified.")


if __name__ == "__main__":
    main()
