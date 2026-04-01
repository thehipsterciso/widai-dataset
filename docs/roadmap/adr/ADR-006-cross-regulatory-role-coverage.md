# ADR-006: Cross-Regulatory Role Coverage as Primary Differentiator

**Status:** Proposed
**Date:** 2026-03-26
**Author:** Thomas Jones / The Hipster CISO
**Derived From:** Ensemble Brainstorm Pass 3 (Perspective Rotation — CISO Persona B, Gartner Analyst Persona C), Scoring Item R11

---

## Context

WIDAI unifies 70+ source frameworks (NICE, O*NET, SFIA, DAMA DMBOK, ESCO, and others) into a single taxonomy. This cross-framework architecture is a design decision made early in the project. What has not been explicitly decided is how to leverage that architecture commercially — whether it is a background feature or the headline differentiator.

The five-pass analysis surfaced a specific capability that no competitor provides: showing how a single role satisfies obligations under multiple regulatory and professional frameworks simultaneously.

## Decision

**Cross-regulatory role coverage — the ability to map one WIDAI role to obligations under EU AI Act, SR 11-7, NIST AI RMF, ISO 42001, NICE, and other frameworks simultaneously — is WIDAI's primary commercial differentiator and should be prioritized in product design, marketing, and data enrichment.**

R11 (cross-regulatory role coverage analysis) is classified as a Roadmap Anchor and placed in Tier 2. Its output becomes a core feature of every WIDAI product:

- **PE Due Diligence (UC1):** "This team's AI Governance Manager covers 4 of 6 relevant regulatory frameworks. Your gap is here."
- **EU AI Act Compliance (UC2):** "These 3 roles collectively satisfy Articles 14, 43, and 72. Here's what they also cover under NIST AI RMF."
- **Model Risk Governance (UC3):** "Your Model Validator role satisfies SR 11-7 independence requirements AND EU AI Act Article 43 conformity assessment."
- **CDAIO Toolkit (UC5):** "Your first two hires should cover maximum regulatory surface area. Here are the two roles that span the most frameworks."

## Rationale

**The CISO persona articulated the need precisely.** Pass 3's CISO at a financial services firm said: "I'm trying to staff for three regulations simultaneously: EU AI Act, SR 11-7 adaptation for AI models, and our cyber insurance renewal. I have budget for maybe two new hires. What I need isn't a list of 50 roles I should have — it's a priority map that tells me which two hires cover the most regulatory surface area."

This is a question no existing tool can answer. Lightcast has labor market data but no regulatory mapping. Credo AI has compliance workflows but no workforce mapping. NICE has cybersecurity roles but no data/AI roles. Each framework lives in its own silo. WIDAI is the only dataset designed to bridge them.

**The Gartner Analyst persona confirmed competitive uniqueness.** Persona C stated: "What nobody has — and what I'd actually cite in a research note — is a machine-readable, cross-framework reference taxonomy specifically for data and AI that maps to O*NET, ESCO, NICE, SFIA, and DAMA simultaneously." The cross-framework mapping is what makes WIDAI citable, not the role count.

**The feature is architecturally native.** WIDAI's entity-separated architecture with source provenance on every mapping was designed for exactly this. The `framework_specific_context` field (added in the schema modifications) carries DAMA, NIST, TOGAF, and MLOps sub-objects per role. The `regulatory_context` field carries EU AI Act, NIST AI RMF, and jurisdictional mappings. The infrastructure exists; the data needs population.

**This differentiator is defensible.** Replicating WIDAI's cross-framework mapping requires: (1) licensing or accessing all source frameworks, (2) creating a normalized entity model that accommodates different framework ontologies, (3) building provenance tracking for every mapping, and (4) validating the mappings against practitioners in each framework domain. This represents 20+ years of domain expertise encoded in architectural decisions. A competitor would need to rebuild not just the data but the judgment calls that produced the data model.

## Consequences

**Positive:**
- Provides a clear, communicable differentiator for every audience persona ("WIDAI is the only tool that shows you cross-regulatory role coverage")
- Makes every product more valuable — cross-regulatory coverage is additive to every use case
- Creates a moat: replicating this requires both the technical architecture and the domain expertise to populate it correctly
- Directly serves the constraint most personas articulated: limited budget, multiple compliance obligations

**Negative:**
- Populating cross-framework mappings for all 187 roles is a significant data enrichment effort — must be prioritized by use case, not attempted comprehensively at once
- Cross-regulatory claims must be validated by practitioners in each regulatory domain — the validation dependency is multiplied by the number of frameworks
- The differentiator is only as strong as the data quality behind it — one incorrect mapping damages credibility across the entire cross-framework claim

**Risks:**
- Framework licensing conflicts (ADR-008 related, R05). If SFIA or DAMA DMBOK licensing restricts how WIDAI uses their framework content in commercial products, cross-framework mapping may need to exclude those sources. Mitigation: R05 (license audit) is in Tier 0 specifically to surface this risk early.
- Regulatory frameworks evolve independently. EU AI Act implementing acts, SR 11-7 updates, NIST AI RMF revisions — each change requires cross-framework mapping updates. Mitigation: quarterly update cadence commitment, starting with the frameworks that change most frequently.

## References

- Ensemble Brainstorm — WIDAI Roadmap, Pass 3: CISO Persona B ("which two hires cover the most regulatory surface area")
- Ensemble Brainstorm — WIDAI Roadmap, Pass 3: Gartner Analyst Persona C ("category of one")
- Ensemble Brainstorm — WIDAI Roadmap, Scoring: R11 (cross-regulatory role coverage analysis — Roadmap Anchor)
- WIDAI Goal Definition: "unifies 70+ source frameworks"
- WIDAI schema: regulatory_context and framework_specific_context field structures
