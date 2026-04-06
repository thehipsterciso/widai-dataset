# ADR-009: Agentic AI Roles as Strategic First-Mover Play

**Status:** Proposed
**Date:** 2026-03-26
**Author:** Thomas Jones / The Hipster CISO
**Derived From:** Ensemble Brainstorm Pass 1 (Forward Decomposition — UC4), Pass 2 (Reverse Induction — F11/F12/F13), Research Brief: Agentic AI Workforce Design

---

## Context

Agentic AI represents the fastest-moving segment in the data/AI landscape. Research findings as of March 2026:

- 79% of organizations report some agentic AI adoption; only 11% have production systems
- Gartner predicts 40%+ of agentic AI projects will be canceled by end of 2027 — governance failure is the primary driver
- "AI Agent Orchestrator" identified as "most important job of 2026" (Eightfold.ai)
- Singapore launched the world's first governance framework for agentic AI (MAIG, January 2026)
- No existing workforce framework — NICE, O*NET, SFIA, ESCO — includes agentic AI roles

Five new roles were identified as candidates for WIDAI: Agent Supervisor, Agent Orchestrator, AI Trust Engineer, AI Memory Engineer, AI Agent Developer. These roles do not exist in any established framework. WIDAI has genuine first-mover opportunity.

The tension: first-mover advantage is time-limited, but the space is volatile. Defining roles that become obsolete within 18 months damages credibility. Waiting until the space stabilizes means losing the window.

## Decision

**Agentic AI role definitions (R10) are placed in Tier 3, not Tier 1. They are developed after the beachhead product validates and after stable use cases (PE due diligence, compliance) establish WIDAI's credibility. But they are developed before full-scale infrastructure (Tier 4).**

The sequencing logic:

1. **Not Tier 1** because the roles are greenfield and volatile. Building the beachhead on a foundation that Gartner predicts has a 40%+ failure rate is an existential risk for a solo-operator project.
2. **Not Tier 4** because the first-mover window closes. If WIDAI waits for full infrastructure build before defining agentic AI roles, Microsoft, AWS, and Google will have published their own vendor-specific frameworks and the market fragments.
3. **Tier 3** because by that point (Weeks 17-24), WIDAI has credibility from a validated pilot (UC1), compliance market presence (UC2), and a proven methodology for role definition. Adding agentic AI roles from that position is an expansion of a credible framework, not an unproven launch.

### Design Constraints for Agentic AI Roles

When R10 is executed, the role definitions must:

- **Ground in real deployment patterns, not theoretical.** Research confirmed: there are ~130 genuine agentic AI vendors out of thousands claiming the label. Role definitions must reference actual production deployments, not vendor marketing.
- **Be vendor-neutral.** Microsoft's five-pillar enterprise governance framework for agents will tempt vendor-specific framing. WIDAI roles must abstract above vendor implementations.
- **Include explicit version dating and deprecation policy.** These roles will evolve. Each definition carries a "defined as of" date and a review cadence (quarterly recommended).
- **Map transition paths from existing roles.** ML Engineer → Agent Developer, SRE → AI Trust Engineer, Data Governance Lead → Agent Supervisor. These paths leverage WIDAI's existing role definitions and make agentic AI roles feel like evolution, not invention.
- **Align with Singapore MAIG and emerging governance frameworks.** The Singapore Model AI Governance Framework for Generative AI (January 2026) is the first government framework addressing agentic AI governance. NIST AI RMF will follow. WIDAI definitions should be interoperable with these frameworks from day one.

## Rationale

**First-mover advantage is real but conditional.** WIDAI can be the first framework to define agentic AI workforce roles in a structured, machine-readable taxonomy. This creates:

- Citation priority: when analysts write about agentic AI workforce planning, WIDAI is the reference
- Vocabulary ownership: WIDAI role names become the default terms
- Framework lock-in: organizations that adopt WIDAI role definitions for agentic AI teams use WIDAI for everything else

But this advantage only holds if the definitions are credible. Credibility requires: grounding in real deployments, validation by practitioners, and a track record (the beachhead product provides this).

**The volatility risk is manageable with the right design.** Pass 2 identified F11 (role definitions become stale within 12 months) as the primary failure mode. The mitigation is version dating — every agentic AI role definition is explicitly time-stamped and carries a quarterly review commitment. This is not a weakness; it's a feature. A framework that acknowledges and manages role evolution is more credible than one that pretends its definitions are permanent.

**The NICHE category is empty.** The WIDAI dataset has a NICHE category with 9 scaffold-only roles and 0 KSAs. Agentic AI roles naturally fit this category. The investment is additive (new roles) not competitive (displacing existing roles). It can proceed without disrupting ongoing enrichment of other categories.

**Content extraction value.** Every piece of agentic AI role research is potential newsletter and LinkedIn content. The Hipster CISO's audience is actively grappling with agentic AI staffing decisions. R16 (content extraction — Watch List) activates naturally when R10 produces publishable analysis.

## Consequences

**Positive:**
- Establishes WIDAI as the first framework with structured agentic AI role definitions
- Creates high-value content for newsletter audience (Persona 1 and 3 especially)
- Fills the empty NICHE category with commercially relevant roles
- Transition path mapping leverages existing WIDAI roles, demonstrating cross-role coherence

**Negative:**
- Quarterly update commitment creates ongoing maintenance obligation
- Volatility risk: some defined roles may not survive market evolution (the "agent washing" problem — F13)
- Tier 3 timing (Weeks 17-24) may miss the peak urgency window if adoption accelerates faster than expected

**Risks:**
- Cloud providers publish their own role frameworks, fragmenting the market before WIDAI enters (F12). Mitigation: vendor-neutral positioning is the counter. WIDAI maps across vendor frameworks, not within them — the same cross-framework differentiator that works for regulatory frameworks (ADR-006) works here.
- "Agent washing" makes the category incoherent (F13). Mitigation: WIDAI definitions must include inclusion/exclusion criteria — what makes a role "agentic AI" vs. "AI operations." Gartner's ~130 genuine vendor estimate provides a starting heuristic for scope.

## References

- Ensemble Brainstorm — WIDAI Roadmap, Pass 1: UC4 analysis
- Ensemble Brainstorm — WIDAI Roadmap, Pass 2: F11, F12, F13 failure modes
- Research Brief: Agentic AI Workforce Design (79% adoption, 40% cancellation prediction, Singapore MAIG)
- Ensemble Brainstorm — WIDAI Roadmap, Scoring: R10 (Watch List classification)
- Eightfold.ai: "AI Agent Orchestrator" as emerging role category
- Singapore IMDA: Model AI Governance Framework for Generative AI, January 2026
