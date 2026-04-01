# ADR-011: PE Assessment Scoring Model Design

**Status:** Accepted
**Date:** 2026-03-27
**Author:** Thomas Jones / The Hipster CISO

## Context

R04 requires a scoring model that produces a defensible number for PE operating partners evaluating data/AI workforce capability in acquisition targets. The number must survive challenge from the target company's management team ("your score is wrong because...") and be explainable to an investment committee in under 5 minutes.

Existing approaches (Mercer talent assessment, EY workforce diligence, Protiviti AI maturity) use subjective consultant judgment or self-reported surveys. None produce a score anchored in observable evidence against a standardized competency framework.

## Decision

Design a four-dimension scoring model (Coverage, Capability, Criticality, Concentration Risk) that aggregates to three composite indices (TCI, KPRS, GSI) and one Workforce Readiness Score (WRS). Every score traces to observable evidence against WIDAI KSA requirements.

### Key Design Choices

**1. Evidence-based, not subjective.** Capability scores are computed against WIDAI KSA requirements using observable evidence (certifications, documented experience, work product review). No "rate this person 1-5" subjective scales.

*Alternatives considered:* Subjective expert assessment (faster but not defensible), self-reported maturity models (easier but gameable), psychometric assessment (valid but out of scope and adds weeks).

**2. Deal-specific criticality, not generic importance.** Criticality (1-5) is scored against the specific value creation plan, not a generic "how important is a Data Engineer." A Data Engineer is criticality-5 if the deal thesis depends on building a new data platform and criticality-2 if the thesis is purely cost optimization.

*Alternatives considered:* Generic role criticality rankings (simpler but miss deal context), value-creation-plan-agnostic scoring (more standardized but less useful to PE).

**3. Four deliverables without compensation data.** Year 1-3 workforce investment model deferred as modular add-on. Assessment ships without Lightcast/BLS compensation data rather than blocking on a partnership.

*Alternatives considered:* Wait for compensation data (blocks product), use BLS averages as proxy (misleading — role-market data varies dramatically by geography and industry), include aspirational estimates (not defensible).

**4. Reference architectures by company profile.** Five reference architectures (Early-Stage through Enterprise) provide the benchmark against which gaps are measured. Selection is the primary customization lever — not methodology changes.

*Alternatives considered:* Custom reference architecture per engagement (expensive, not scalable), single universal reference (doesn't account for company size/maturity), industry-specific references (insufficient data to calibrate yet — future enhancement).

**5. WRS as single composite score.** TCI (50% weight), KPRS (30% weight), GSI (20% weight) produce one number. Bands: Critical (<40), At-Risk (40-60), Adequate (60-75), Strong (75-90), Exceptional (>90).

*Alternatives considered:* No single score (harder for investment committees), equal weighting (capability matters more than gaps in PE context), letter grades (less precise, feels academic).

## Consequences

**Positive:**
- Defensible: every number traces to evidence. Target company can challenge inputs but not the methodology.
- Standardized: same process every time. Enables consistency across multiple assessments per PE firm.
- Fast: 30-day delivery fits PE deal windows.
- Modular: compensation modeling can be added without redesigning the core methodology.

**Negative:**
- Without compensation data, the assessment cannot answer "what will it cost to close the gaps?" with precision. This is the PE operating partner's second most important question.
- Reference architectures are based on practitioner judgment, not empirical calibration. First 3-5 assessments will refine them.
- Capability scoring from evidence (certifications, experience) is a proxy for actual competence. Work product review improves accuracy but adds time.
- KSA coverage varies by WIDAI category — some roles have deeper assessment criteria than others.

## References

- Ensemble Brainstorm, UC1: PE Workforce Due Diligence
- Ensemble Brainstorm, Persona A: PE Operating Partner
- ADR-002: PE Due Diligence as Beachhead Product
- ADR-003: Ship on Current Data Coverage (validated by R01)
- ADR-007: Assessment Service, Not Dataset Product
- R01: Coverage Gap Test (92.2% coverage validates data supports pilot)
- `methodology/pe-assessment-scoring-model.json`
- `methodology/pe-assessment-workflow.json`
- `methodology/pe-assessment-deliverables.json`
- `methodology/R04-pe-assessment-methodology.md`
