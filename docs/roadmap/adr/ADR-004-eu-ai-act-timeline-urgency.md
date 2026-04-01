# ADR-004: EU AI Act Compliance as Urgent Parallel Track

**Status:** Proposed
**Date:** 2026-03-26
**Author:** Thomas Jones / The Hipster CISO
**Derived From:** Ensemble Brainstorm Pass 1 (Forward Decomposition — UC2), Pass 2 (Reverse Induction — F5/F6/F7), Research Brief: EU AI Act Compliance Tooling

---

## Context

The EU AI Act's high-risk AI system requirements enforce on August 2, 2026 — five months from this writing. As of March 2026, research confirms:

- Only 8 of 27 EU member states have designated competent authorities
- 79% of enterprises cite AI governance talent scarcity as a barrier to compliance
- Existing compliance tools (Credo AI, Vanta, OneTrust, Daiki) focus on workflow automation — none provide workforce role mapping
- No tool bridges the three frameworks organizations must navigate simultaneously: EU AI Act obligations → internal organizational roles → NIST AI RMF → ISO 42001

The cross-framework role mapping gap — specifically, mapping regulatory obligations to the people who must fulfill them — is confirmed as an unserved need.

However, the beachhead product decision (ADR-002) selects PE Due Diligence, not EU AI Act compliance. This creates tension: UC2 has the most urgent external deadline but is not the beachhead.

## Decision

**EU AI Act compliance role mapping (UC2) is positioned as a Tier 2 deliverable, not the beachhead, but its foundational work (regulatory context field population) begins in Tier 1 as shared infrastructure with UC1.**

Specifically:

- **Tier 1 (Weeks 3-8):** R07 — populate regulatory context fields for GOV and RSK category roles. This work directly serves UC2 (compliance mapping) AND UC1 (PE assessments of regulated targets) AND UC3 (model risk governance). It is not UC2-specific work; it is shared foundational enrichment.
- **Tier 2 (Weeks 9-16):** R06 — EU AI Act obligation-to-role mapping. R14 — regulatory practitioner validation. R11 — cross-regulatory role coverage analysis. These produce the UC2-specific deliverable.
- **Target:** Shippable EU AI Act role mapping product by July 2026, one month before enforcement.

## Rationale

**Why not beachhead:** EU AI Act compliance has high urgency but lower cascading adoption than PE due diligence. One compliance engagement serves one organization's European operations. It does not cascade into portfolio-wide mandates. The compliance tool market is also crowded — WIDAI's differentiation (workforce role mapping) risks being absorbed as a feature of existing compliance platforms rather than establishing a standalone category.

**Why urgent parallel, not deferred:** The August 2026 deadline is real and immovable. Organizations with EU operations are making compliance decisions now. If WIDAI's role mapping is not available before enforcement, the market window closes — not permanently, but the urgency-driven early adopters will have solved their problems with less rigorous approaches. The cost of missing this window is not fatal but is significant.

**Why the timeline works:** Tier 0 validation (2 weeks) + Tier 1 foundations (6 weeks) = Week 8. Tier 2 begins Week 9 with regulatory context fields already populated. R06 (obligation mapping) and R14 (practitioner validation) run for 8 weeks, producing a deliverable by Week 16 — approximately late July 2026, one week before August 2 enforcement.

This timeline is tight but not impossible because:

1. The schema already includes regulatory_context fields (added in the schema modifications). The data architecture supports this use case; the fields just need population.
2. Regulatory context population (R07) serves multiple use cases simultaneously, so the work is not UC2-exclusive overhead.
3. The obligation-to-role mapping (R06) is a structured analysis exercise, not a software build — it can be executed in parallel with other Tier 2 items.

### Failure Mode F5 Is the Binding Constraint

Pass 2 identified F5: "WIDAI is slower than enforcement." If the timeline slips beyond August 2026, UC2 loses its urgency premium. The decision to begin regulatory context work in Tier 1 (not Tier 2) is specifically designed to mitigate F5 by front-loading the foundational work.

### Regulatory Practitioner Validation Is Non-Negotiable

Pass 2 (F7) and Pass 3 (CISO Persona B) both flagged the same risk: regulatory context populated without practitioner validation is a liability, not a tool. The CISO persona stated: "If they're populated by framework analysis and not validated by someone who's been through a regulatory examination, I can't use them as evidence."

R14 (regulatory practitioner validation) is therefore a hard dependency for UC2 delivery, not a quality improvement. The deliverable does not ship without it.

## Consequences

**Positive:**
- Captures the urgency-driven early adopter market before enforcement
- Regulatory context work benefits UC1 (PE assessments of regulated targets) and UC3 (model risk governance) simultaneously
- Demonstrates WIDAI's cross-framework mapping capability — the feature no competitor provides
- Creates newsletter content with built-in urgency ("5 months to compliance — do you have the right people?")

**Negative:**
- Tight timeline creates execution pressure — any Tier 0 delays compress Tier 2 proportionally
- Requires finding and engaging a regulatory practitioner for validation (R14) within the timeline — this is a dependency on an external person Thomas may not yet know
- Parallel execution with UC1 pilot work may exceed solo-operator capacity

**Risks:**
- Timeline slips past August 2026. Mitigation: regulatory context field population (R07) has value beyond the compliance deadline — it serves UC1 and UC3 regardless. The sunk work is not wasted.
- No regulatory practitioner available for validation. Mitigation: begin practitioner outreach in Tier 1 (not Tier 2) to maximize lead time. Consider fractional legal/regulatory advisors specializing in EU AI Act.

## References

- Ensemble Brainstorm — WIDAI Roadmap, Pass 1: UC2 analysis (August 2026 deadline, 8/27 member states ready)
- Ensemble Brainstorm — WIDAI Roadmap, Pass 2: F5, F6, F7 failure modes
- Ensemble Brainstorm — WIDAI Roadmap, Pass 3: CISO Persona B (regulatory validation requirement)
- Research Brief: EU AI Act Compliance Tooling (Credo AI, Vanta, OneTrust landscape)
- EU AI Act enforcement timeline: Regulation (EU) 2024/1689, Article 113
