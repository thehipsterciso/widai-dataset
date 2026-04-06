# ADR-012: KSA Depth Correction — External Benchmarking and Quality Gates

**Status:** Accepted
**Date:** 2026-03-27
**Author:** Thomas Jones / The Hipster CISO
**Supersedes:** Portions of ADR-005 (quality gates), ADR-010 (R02 validation interpretation)

## Context

On 2026-03-27, manual review of R08 output (42 KSAs across 5 gap roles) revealed a critical depth deficiency in the WIDAI KSA model. Comparison against the NIST NICE Framework v2.1.0 — the only comparable machine-readable workforce taxonomy with published KSA-per-role data — showed WIDAI roles operating at approximately 6.7% of industry-standard depth.

**The evidence:**

| Metric | WIDAI | NICE v2.1.0 | Gap |
|--------|-------|-------------|-----|
| Mean KSAs/role | 8.95 | 133.3 | 14.9x |
| Min KSAs/role | 4 | 68 | 17.0x |
| Max KSAs/role | 18 | 206 | 11.4x |

This gap was not detected by the Phase 0 validation sprint because:

1. **R02** validated statement quality (4.26/5) but never validated statement quantity or role depth
2. **R24** validated structural consistency (8.2/10) but never compared depth against external benchmarks
3. **R01** measured role coverage (92.2%) as binary presence/absence of any KSA mappings, not depth adequacy
4. **ADR-005** defined quality gates for AI-assisted authoring that included no minimum depth threshold

The failure propagated through R08 (authored at the flawed depth) and undermines R04's Coverage dimension (trivially achievable against a thin reference set).

Full root cause analysis: [`docs/roadmap/R02-FAILURE-ASSESSMENT.md`](../R02-FAILURE-ASSESSMENT.md)

## Decision

Implement four corrective measures before any further roadmap execution:

### 1. KSA Depth Coverage Index (DCI)

Define a mathematical metric that benchmarks role depth against the NICE framework reference distribution. The metric must:

- Express current depth as a ratio of industry benchmark depth
- Account for domain differences (data/AI roles may legitimately differ from cybersecurity roles in KSA distribution)
- Produce a per-role score and a dataset-wide aggregate
- Set a minimum threshold below which a role is flagged as "insufficient depth"

**Minimum depth target:** 40 KSAs per role (conservative floor — approximately 30% of NICE mean, accounting for WIDAI's narrower domain scope per role). Roles with regulatory assessment implications (DPO, Model Risk Manager) target 60+.

*Alternatives considered:*
- Match NICE mean exactly (~133/role): Unrealistic for initial correction. NICE covers broader cybersecurity domain with more shared Knowledge items across roles. Data/AI roles are more specialized.
- Percentage-of-NICE target (50%): Still potentially too thin for assessment utility. 40 minimum establishes a floor, not a ceiling.
- No fixed target, peer-reviewed judgment only: Insufficient — the failure originated from judgment without external anchor.

### 2. Adversarial Quality Gate (AQG)

Build a multi-pass review process modeled on the ensemble brainstorm algorithm's adversarial structure:

- **Pass 1 — Breadth Scan:** For a given role, enumerate all knowledge domains, skill categories, and task areas from source frameworks. Produce a domain coverage map.
- **Pass 2 — Depth Challenge:** For each domain identified in Pass 1, challenge whether the current KSA set adequately covers it. Identify gaps.
- **Pass 3 — External Benchmark:** Compare KSA count and distribution against the closest NICE analog (or O*NET, SFIA equivalent). Flag any dimension where WIDAI is <25% of benchmark depth.
- **Pass 4 — Assessability Test:** For each KSA, verify it is observable and scorable in a PE due diligence context. Remove or rewrite KSAs that are too abstract to assess.
- **Pass 5 — Adversarial Review:** Assume the role of a skeptical PE operating partner. Ask: "If I hired against this KSA set, would I miss any critical capability?" Document and fill any gaps surfaced.

*Alternatives considered:*
- Single-pass quality check (current approach): Failed. Caught statement quality issues but missed depth entirely.
- External human review only: Too slow for 42+ roles. Build the automated gate first, then layer human review for high-stakes roles.
- Statistical sampling: Insufficient — every role needs depth validation, not a sample.

### 3. External Benchmarking Requirement

All future validation tests must include at least one external framework benchmark comparison. Internal-only validation (comparing WIDAI to WIDAI) is formally prohibited for any gate that determines "readiness" or "coverage."

This applies retroactively to R02, which must be supplemented with a depth dimension before its validation result can be cited in future ADRs.

### 4. Dataset Enrichment Sprint

Bring all 42 currently-mapped roles to the minimum depth threshold (40+ KSAs per role). This is the immediate corrective action — the three items above are the structural prevention.

**Enrichment approach:**
- Use the AI-assisted workflow (ADR-005) with the new AQG applied to every role
- Source from all mapped frameworks per role (NICE, O*NET, SFIA, DAMA DMBOK, regulatory texts)
- Tag all new KSAs with `origin_version: "0.5.0"` and `quality_gate: "AQG-v1"`
- Target: ~1,680+ total KSA mappings (42 roles × 40 minimum)

*Alternatives considered:*
- Enrich only the 5 R08 gap roles: Insufficient — all 42 roles share the same depth deficiency.
- Wait for pilot feedback: The pilot (R03) would deliver flawed assessment data. Correct before shipping.
- Incremental enrichment over multiple sprints: Acceptable for roles beyond the initial 42, but the 42 mapped roles must reach threshold before R03.

## Consequences

**Positive:**
- Assessment credibility: A role with 40-80 KSAs provides genuine discriminating power in PE due diligence. A role with 8 KSAs does not.
- External defensibility: Benchmarking against NICE gives WIDAI a citable comparison point for methodology discussions.
- Structural prevention: The AQG and DCI metric prevent recurrence systematically rather than relying on manual catch.
- R04 recalibration: Coverage dimension scores become meaningful when the reference set has adequate depth.

**Negative:**
- Timeline impact: Dataset enrichment adds 2-4 weeks to Phase 1 timeline. R03 (pilot engagement) is delayed.
- Volume of work: ~1,300+ new KSAs must be authored, reviewed, and validated. Even with AI-assisted workflow, this is substantial.
- Benchmark limitations: NICE is cybersecurity-focused; direct comparison to data/AI roles requires judgment about domain scope differences.
- Version discontinuity: KSAs authored pre-correction (v0.4.x) will coexist with post-correction KSAs (v0.5.0) until full rewrite.

## Roadmap Impact

| Item | Impact |
|------|--------|
| R03 (Pilot Engagement) | **Blocked** until enrichment sprint completes |
| R04 (Scoring Model) | Coverage dimension must be recalibrated post-enrichment |
| R07 (Regulatory Context) | Unaffected — proceeds in parallel |
| R08 (Gap KSA Authoring) | **Superseded** — 42 KSAs will be replaced by enriched set |
| R12 (Methodology Docs) | Must document DCI metric and AQG process |
| New: R25 (Enrichment Sprint) | Added to roadmap — Tier 1 priority, blocks R03 |
| New: R26 (DCI + AQG Pipeline) | Added to roadmap — Tier 1 priority, CI/CD integration |

## References

- [`docs/roadmap/R02-FAILURE-ASSESSMENT.md`](../R02-FAILURE-ASSESSMENT.md) — Full root cause analysis
- ADR-005: AI-Assisted KSA Authoring (quality gates now supplemented by AQG)
- ADR-010: Validation Sprint (R02 interpretation corrected)
- ADR-011: PE Assessment Scoring Model (Coverage dimension affected)
- NIST NICE Framework v2.1.0: https://niccs.cisa.gov/workforce-development/nice-framework
- R01, R02, R08, R24: Phase 0/1 validation and authoring results
