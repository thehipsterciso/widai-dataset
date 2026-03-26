# ADR-002: PE Workforce Due Diligence as Beachhead Product

**Status:** Proposed
**Date:** 2026-03-26
**Author:** Thomas Jones / The Hipster CISO
**Derived From:** Ensemble Brainstorm Pass 1 (Forward Decomposition), Pass 3 (Perspective Rotation — PE Operating Partner Persona), Pass 4 (Constraint Inversion)

---

## Context

ATLAS has six viable use cases, five of which scored 20/25 on the Strategic Opportunity Index. Selecting the wrong beachhead delays market entry, wastes execution capacity, and may position ATLAS in a market that doesn't value its differentiation.

The use cases were evaluated not only on SOI score but on three additional dimensions surfaced by the five-pass analysis:

1. **Cascading adoption potential.** Does one customer create multiple downstream users?
2. **Alignment with Thomas's existing audience and positioning.** Does this require building a new audience or serving the existing one?
3. **Data readiness.** Can current ATLAS data support a minimum viable engagement?

## Decision

**PE Workforce Due Diligence (UC1) is the beachhead product. All other use cases are sequenced after UC1 validates or are developed concurrently where they share foundations.**

The PE assessment is a service product, not a data product. Five deliverables per engagement:

1. Current-state capability map (roles mapped to ATLAS taxonomy)
2. Maturity score (quantified, defensible, benchmarked)
3. Integration complexity estimate (role overlap, culture alignment proxies)
4. Year 1-3 workforce investment model (cost to close gaps)
5. Key person risk flags (single-point-of-failure roles)

Target pricing: $50-75K per assessment — trivial against deal size, premium against the nothing that currently exists.

## Rationale

**Cascading adoption is the decisive factor.** The PE Operating Partner persona (Pass 3) articulated the mechanism: "If the first one works, I'll mandate it across the portfolio. That's eight assessments in Year 1." No other use case has this multiplier. A single PE firm adoption produces 5-15 portfolio company assessments. Each portfolio company assessment puts ATLAS in front of a CDAIO (Persona 3), who becomes a potential UC5 (toolkit) customer. The adoption chain is: PE partner → portfolio companies → CDIAOs → newsletter audience.

**Existing audience alignment.** PE operating partners are Persona 2 in The Hipster CISO's audience segmentation. This is not a cold market — it's the market Thomas is already building credibility with through the newsletter.

**Data readiness.** Constraint Inversion (Pass 4) tested whether current data supports a pilot. Finding: a mid-market data/AI team of 15-30 people maps to 20-40 ATLAS roles, and the GOV (25 roles, 73 KSAs), ENG (25 roles, 53 KSAs), DEV (15 roles, 46 KSAs), and DSM (21 roles, 38 KSAs) categories provide KSA coverage for the majority of typical team members. A pilot is feasible on current data with acknowledged gaps.

**Competitive white space.** Research confirmed: current PE due diligence for data/AI talent relies on "gut feel and superficial reference checks" (Protiviti 2025 AI maturity research). No standardized, quantified methodology exists. ATLAS fills a gap that the market hasn't even formalized as a product category.

**Revenue funds the roadmap.** At $50-75K per engagement, two completed assessments fund Lightcast data partnerships (compensation data for UC1 investment modeling), regulatory practitioner review (validation for UC2 and UC3), and continued KSA authoring. The beachhead product self-funds the roadmap expansion.

### Alternatives Considered

**EU AI Act Compliance (UC2):** Higher urgency (August 2026 deadline) but lower cascading adoption. One compliance engagement serves one organization. The market is also crowded with compliance workflow tools (Credo AI, Vanta, OneTrust) — ATLAS's differentiation (workforce role mapping) is a feature of their platforms, not a standalone category. Pursued in Tier 2, not as beachhead.

**Agentic AI Roles (UC4):** Strongest first-mover advantage but highest volatility. Gartner predicts 40%+ of agentic AI projects canceled by end of 2027. Building the beachhead on a category that may fragment creates existential risk. Pursued in Tier 3 after stable use cases validate.

**CDAIO Toolkit (UC5):** Natural fit for Thomas's practitioner credibility but depends on components from UC1-UC3. It's an assembly product, not a foundation product.

## Consequences

**Positive:**
- Creates the fastest path to market validation with real revenue
- Produces case study material that enables analyst engagement (Gartner Persona C requirement)
- Each engagement generates data about coverage gaps, directly informing KSA authoring priority
- Revenue from first engagements funds subsequent roadmap phases

**Negative:**
- Concentrates risk on a single market segment — if PE operating partners don't adopt, the beachhead fails
- Requires sales/relationship development capability, not just data/product development
- The $50-75K price point requires a consultative sale, not a self-serve product — limiting scale until the methodology is productized

**Risks:**
- No pilot partner materializes from Thomas's network. Mitigation: R03 (pilot identification) is in Tier 1 specifically so this risk surfaces early. If no partner by end of Tier 1, pivot to UC2 (compliance) as beachhead, leveraging the August 2026 deadline urgency.

## References

- Ensemble Brainstorm — ATLAS Roadmap, Pass 1: UC1 analysis ($2.6T PE deal value, 60% CEO replacement rate)
- Ensemble Brainstorm — ATLAS Roadmap, Pass 3: PE Operating Partner persona
- Ensemble Brainstorm — ATLAS Roadmap, Pass 4: Constraint 1 analysis (ship on current data)
- ATLAS Goal Definition, Section: Who ATLAS Serves (PE Operating Partners as Primary)
- ATLAS Use Case Discovery and Prioritization, UC1 scoring (20/25)
