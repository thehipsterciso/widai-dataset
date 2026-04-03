# AB Knowledge Domain — Cross-Framework Synthesis

**Date:** 2026-04-03
**Domain:** AB (Analytics & Business Intelligence)
**Dimension:** Knowledge
**KSAs Analyzed:** 10 (AB-K-001 through AB-K-010)
**Frameworks:** O*NET 30.2, NIST NICE v2.1.0, DoD DCWF v5.1, DDaT, EU AI Act, NIST AI RMF 1.0

---

## Executive Finding

All 10 AB Knowledge KSAs show **zero strong classifications** (Equal or Subset Of) across all 6 source frameworks. Every mapping is classified as "Intersects With" — a moderate semantic relationship. This is not a pipeline defect. It is the defining structural signal for this domain.

The highest STS score across 7,874 total AB-K mappings is **0.6863** (AB-K-009 against NICE K1144: "Knowledge of data correlation tools and techniques"). The Subset Of threshold is 0.70. No AB-K statement reaches it.

**What this means:** The Analytics & BI knowledge domain as WIDAI defines it does not exist as a cohesive unit in any of the 6 source frameworks processed to date. These frameworks acknowledge analytics concepts — they intersect with them broadly — but none of them articulates analytics knowledge at the granularity WIDAI requires. WIDAI is operating in original territory here. The AB Knowledge structure is genuinely additive to the workforce taxonomy landscape.

---

## Evidence Matrix

| KSA ID | Statement (truncated) | FW Coverage | Strong | Moderate | Total | Max STS |
|--------|----------------------|:-----------:|:------:|:--------:|:-----:|:-------:|
| AB-K-001 | Descriptive statistics (central tendency, dispersion, correlation) | 6/6 | 0 | 504 | 504 | 0.6584 |
| AB-K-002 | Data visualization best practices (chart selection, cognitive load) | 6/6 | 0 | 504 | 504 | 0.6607 |
| AB-K-003 | Common analytical frameworks (cohort, funnel, segmentation) | 6/6 | 0 | 701 | 701 | 0.6672 |
| AB-K-004 | Advanced analytical methods (regression, forecasting, clustering) | 6/6 | 0 | 847 | 847 | 0.6818 |
| AB-K-005 | A/B testing and experimentation design | 6/6 | 0 | 826 | 826 | 0.6381 |
| AB-K-006 | BI platform capabilities (Power BI, Tableau, Looker) | 6/6 | 0 | 1394 | 1394 | 0.6343 |
| AB-K-007 | BI governance (report certification, lifecycle, access control) | 6/6 | 0 | 558 | 558 | 0.6798 |
| AB-K-008 | Statistical modeling methods (OLS, GLM, Bayesian, survival) | 6/6 | 0 | 457 | 457 | 0.6780 |
| AB-K-009 | Causal inference methods (DiD, IV, RDD, propensity score) | 6/6 | 0 | 931 | 931 | 0.6863 |
| AB-K-010 | Embedded/augmented analytics (AI-assisted insights, NLQ) | 6/6 | 0 | 1152 | 1152 | 0.6730 |

---

## Per-Framework Coverage

| Framework | KSAs Hit | Total Mappings | Strong | Character |
|-----------|:--------:|:--------------:|:------:|-----------|
| O*NET 30.2 | 10/10 | 81 | 0 | Generic occupational — "Knowledge of statistics" matches broadly but never at AB-K granularity |
| NIST NICE v2.1.0 | 10/10 | 2,813 | 0 | Richest match source. NICE has data analysis/correlation/visualization KSAs but at tool-level, not methodology-level |
| DoD DCWF v5.1 | 10/10 | 4,049 | 0 | Highest mapping volume. Test & evaluation concepts match experimentation design. Analytics as intelligence activity |
| DDaT | 10/10 | 454 | 0 | Capability-level descriptions ("Strategic data planning") that touch all 10 KSAs broadly but none deeply |
| EU AI Act | 10/10 | 169 | 0 | Regulatory lens — "Data and data governance" maps to everything at low-moderate STS. No analytics specificity |
| NIST AI RMF 1.0 | 10/10 | 308 | 0 | AI evaluation and trustworthiness concepts overlap with testing/metrics but not analytics methodology |

---

## Why Zero Strong Matches — Structural Analysis

Three forces converge to produce this result:

### 1. Granularity Mismatch
Source frameworks describe analytics knowledge at the **tool/capability level**: "Knowledge of analytics," "Knowledge of data analysis tools and techniques," "Knowledge of statistical processes." WIDAI's AB-K statements describe analytics knowledge at the **method/principle level**: specific statistical methods, specific experimental designs, specific inference techniques. The source frameworks name the room. WIDAI names what's in it.

### 2. Domain Boundary Difference
The 6 processed frameworks are cybersecurity-centric (NICE, DCWF), government digital capability (DDaT), occupational (O*NET), or regulatory (EU AI Act, NIST AI RMF). None of them is an analytics or BI workforce framework. Analytics appears in them as a supporting competency, not a primary domain. The frameworks that would produce strong matches — if they exist as structured workforce taxonomies — would be something like a "NICE for Data Scientists" or an analytics-specific professional body standard.

### 3. Compound Specificity
WIDAI's AB-K statements deliberately compound multiple specific concepts. AB-K-009 names difference-in-differences, instrumental variables, regression discontinuity, propensity score matching, AND their identification assumptions — in a single KSA. No source framework element packs that density. The best matches are single-concept elements ("Knowledge of data correlation tools and techniques") that overlap with one piece of the compound statement.

---

## Near-Miss Analysis

189 mappings score STS ≥ 0.60 (approaching the 0.70 Subset threshold). Distribution by KSA:

| KSA | Near-Misses (≥0.60) | Closest Match | Best STS |
|-----|:-------------------:|---------------|:--------:|
| AB-K-001 | 10 | NICE K1144: "data correlation tools and techniques" | 0.6584 |
| AB-K-002 | 5 | NICE K0647: "data visualization tools and techniques" | 0.6607 |
| AB-K-003 | 11 | NICE K1101: "analytics" | 0.6672 |
| AB-K-004 | 35 | NICE K1101: "analytics" | 0.6818 |
| AB-K-005 | 19 | NICE K1342: "training, validation, and test data sets" | 0.6381 |
| AB-K-006 | 12 | NICE K0646: "system optimization techniques" | 0.6343 |
| AB-K-007 | 15 | NICE K0992: "database maintenance principles and practices" | 0.6798 |
| AB-K-008 | 13 | NICE K1170: "mathematical models" | 0.6780 |
| AB-K-009 | 21 | NICE K1144: "data correlation tools and techniques" | 0.6863 |
| AB-K-010 | 48 | NICE K1005: "intelligence collection capabilities and applications" | 0.6730 |

**Key observations:**
- NICE dominates the near-miss list. It is the richest source of analytics-adjacent knowledge elements among the 6 frameworks.
- AB-K-004 (advanced analytical methods) and AB-K-010 (embedded analytics) have the most near-misses — these are the KSAs where source frameworks come closest to expressing what WIDAI articulates.
- AB-K-005 (A/B testing) has the lowest best STS (0.6381) — experimentation design is the most distinctive WIDAI contribution in this domain.
- AB-K-006 (BI platforms) matches against database and security concepts, not BI-specific elements — confirming that BI platform knowledge is genuinely absent from these frameworks.

---

## MVP Assessment

### Current Structure Verdict: Sound

All 10 AB-K KSAs demonstrate the same structural pattern: universal framework coverage (6/6), zero strong matches, moderate intersection density. This means every KSA is semantically related to workforce concepts in these frameworks but none is redundant with them. There are no KSAs that should be merged or removed based on this evidence.

### Strength Tiers (by evidence density and max STS)

**Tier 1 — Strongest Evidence (highest max STS, most near-misses):**
- AB-K-009: Causal inference methods (0.6863) — strongest single match across all AB-K
- AB-K-004: Advanced analytical methods (0.6818, 35 near-misses) — broadest near-miss footprint
- AB-K-007: BI governance (0.6798) — strong affinity with database/asset management concepts
- AB-K-008: Statistical modeling (0.6780) — connects to mathematical models, analytics
- AB-K-010: Embedded analytics (0.6730, 48 near-misses) — largest near-miss count

**Tier 2 — Moderate Evidence:**
- AB-K-003: Common analytical frameworks (0.6672)
- AB-K-002: Data visualization (0.6607)
- AB-K-001: Descriptive statistics (0.6584)

**Tier 3 — Most Distinctive (lowest max STS = most original):**
- AB-K-005: A/B testing and experimentation (0.6381) — most novel contribution
- AB-K-006: BI platform capabilities (0.6343) — most distinctive from source frameworks

### Gap Signals — What's Missing from AB Knowledge

The synthesis reveals what the source frameworks emphasize that AB-K does not currently cover:

1. **Data quality and profiling knowledge** — NICE has rich data quality, data profiling, and data cleansing elements that AB-K lacks. An analytics professional needs to understand data quality assessment before analysis begins. *Candidate: AB-K-011.*

2. **Metrics and KPI design** — Multiple frameworks reference "measures of effectiveness" and "measures of performance" (DCWF 2066). AB-K covers analytical methods but not the knowledge of how to design, validate, and govern metrics themselves. *Candidate: AB-K-012.*

3. **Data storytelling and communication** — AB-K-002 covers visualization best practices but does not address the broader skill of translating analytical findings into business narratives, executive communication, and decision support framing. *Candidate: AB-K-013.*

4. **Survey and primary data collection methodology** — Source frameworks reference data gathering extensively. AB-K assumes data exists. Knowledge of survey design, sampling methodology, and primary data collection is absent. *Candidate: AB-K-014.*

5. **Analytics ethics and bias** — EU AI Act and NIST AI RMF emphasize trustworthiness, fairness, and bias detection. AB-K does not currently address knowledge of statistical bias types, fairness metrics, or the ethical dimensions of analytical decision-making. *Candidate: AB-K-015.*

### Recommended Next Steps

1. **Validate gap candidates** — Run the 5 proposed KSAs through the existing 6 STRMs to confirm they fill genuine gaps (they should produce higher STS scores than existing AB-K against the relevant FDEs).
2. **Queue DAMA DMBOK STRM** — DAMA DMBOK is the next Tier 2 framework in the pipeline and is the most analytics-adjacent framework remaining. It will provide the first strong test of whether AB-K statements can achieve Subset/Equal classifications against a data-centric standard.
3. **Cross-domain check** — Several AB-K KSAs (especially AB-K-008 statistical modeling and AB-K-009 causal inference) may overlap with DS (Data Science) domain knowledge. Verify no duplication exists before expanding AB-K.

---

## Methodology Notes

- Synthesis script: `scripts/ab_k_synthesis.py`
- Top match analysis: `scripts/ab_k_top_matches.py`
- Full evidence JSON: `strm/ab_knowledge_synthesis.json`
- Pipeline thresholds: Equal ≥ 0.82 STS + NLI gate, Subset ≥ 0.70 + NLI gate, Intersects ≥ 0.35
- All 6 STRM mapping files processed (317MB total JSON)
- 7,874 AB-K mappings extracted and analyzed
