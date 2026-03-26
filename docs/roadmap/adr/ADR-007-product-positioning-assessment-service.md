# ADR-007: Position ATLAS as Assessment Service, Not Dataset Product

**Status:** Proposed
**Date:** 2026-03-26
**Author:** Thomas Jones / The Hipster CISO
**Derived From:** Ensemble Brainstorm Pass 3 (Perspective Rotation — all four personas), Pass 2 (Reverse Induction — HC5)

---

## Context

ATLAS is a dataset — 187 roles, 322 KSAs, structured relationship tables with source provenance. The natural impulse for a dataset project is to sell the dataset: API access, data licensing, flat-file exports.

The five-pass analysis tested this assumption by rotating through four buyer personas and asking what each would pay for. The answer was unanimous: none of them buy datasets.

## Decision

**ATLAS products are positioned as assessment services and compliance tools, not as dataset access or data licensing. The taxonomy is the cost of goods, not the product.**

The dataset remains the foundational asset. But every market-facing deliverable is packaged as a product that produces answers, not data:

| Use Case | Product Positioning | Not Positioned As |
|----------|-------------------|-------------------|
| UC1: PE Due Diligence | Workforce capability assessment ($50-75K/engagement) | Dataset license |
| UC2: EU AI Act | Compliance role mapping tool (subscription) | Framework download |
| UC3: Model Risk | Org design blueprint service | Taxonomy access |
| UC4: Agentic AI | Role definition library + transition mapping | Data export |
| UC5: CDAIO Toolkit | Assessment + planning toolkit ($5-10K license) | API access |

## Rationale

**Every persona said the same thing differently.**

The PE Operating Partner (Persona A): "This isn't a taxonomy product, it's a services product. I don't buy taxonomies. I buy assessments. The taxonomy is your cost of goods." And: "Your biggest risk is trying to sell me the dataset when what I need is the answer."

The CISO (Persona B): Wants "a priority map that tells me which two hires cover the most regulatory surface area" — an answer derived from data, not the data itself.

The Gartner Analyst (Persona C): "I won't cite a dataset. I'll cite a product that organizations use and can testify to."

The CDAIO (Persona D): Wants "a quick assessment tool that maps my current team in under a day, a gap analysis, and a hiring priority list" — three deliverables, none of which are "access to a JSON file."

**Hidden Constraint HC5 confirmed the risk.** Pass 2 surfaced: "Banks buy from consultants, not taxonomies. PE firms buy from advisors. If ATLAS is positioned as a raw dataset or taxonomy, the market may not recognize it as a product." The consulting channel may be required for financial services adoption. The product surface matters as much as the data.

**The pricing implications are material.** A dataset license might command $5-10K/year. An assessment engagement commands $50-75K. A compliance subscription might command $15-25K/year. The same underlying data, packaged as answers instead of access, represents 5-10x revenue per customer.

**This does not preclude data licensing later.** The ATLAS Goal Definition leaves the open-vs-proprietary question deliberately unresolved. The decision here is about initial market positioning, not permanent business model. If the assessment service succeeds and market demand for raw data emerges (from HR platforms, consulting firms, certification bodies), data licensing becomes a Phase 4+ expansion — informed by real pricing signals from assessment customers.

### What This Means for Product Development

Assessment service positioning changes development priorities:

1. **Methodology before API.** The assessment scoring model, deliverable templates, and engagement workflow are higher priority than a REST/GraphQL API. The API serves developers. The methodology serves buyers.
2. **Templates before tooling.** PE assessment report templates, compliance mapping worksheets, and org design blueprints are the product surface. Interactive tooling (R25) enhances delivery but isn't required for the first engagement.
3. **Case studies before analyst coverage.** The Gartner Analyst persona won't cite ATLAS until organizations testify to its value. Case studies from real assessments are the prerequisite for analyst engagement.

## Consequences

**Positive:**
- Aligns with how every target persona actually buys — reduces sales friction
- Commands premium pricing ($50-75K assessment vs. $5-10K license)
- Creates a services moat — methodology expertise is harder to replicate than data access
- Each engagement generates case study material, creating a compound credibility effect

**Negative:**
- Services don't scale linearly — each engagement requires Thomas's time (at least initially)
- The "one person delivering $50-75K assessments" model has a revenue ceiling — eventually requires either productization or team expansion
- Delays the data product / API layer that would enable ecosystem adoption (consulting firms, HR platforms building on ATLAS)

**Risks:**
- The services model traps ATLAS as a consulting practice, never becoming a scalable product. Mitigation: explicit transition plan — Phase 1-2 are services, Phase 3-4 productize the methodology into self-serve tools, Phase 4+ consider data licensing.
- Customers expect consulting-level engagement but ATLAS is a solo operation. Mitigation: clearly defined engagement scope and deliverables (five specific outputs, not open-ended advisory).

## References

- Ensemble Brainstorm — ATLAS Roadmap, Pass 3: All four persona responses
- Ensemble Brainstorm — ATLAS Roadmap, Pass 2: HC5 ("the consulting channel may be required")
- Ensemble Brainstorm — ATLAS Roadmap, Pass 3: Disagreement Map (all personas on product positioning)
- ATLAS Goal Definition: "Pricing and business model" listed as deliberately unresolved
