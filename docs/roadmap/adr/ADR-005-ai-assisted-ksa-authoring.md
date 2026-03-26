# ADR-005: AI-Assisted KSA Authoring as Primary Acceleration Strategy

**Status:** Proposed
**Date:** 2026-03-26
**Author:** Thomas Jones / The Hipster CISO
**Derived From:** Ensemble Brainstorm Pass 4 (Constraint Inversion — Constraint 2), Scoring Item R02

---

## Context

ATLAS has 187 defined roles. 37 have complete KSA (Knowledge, Skills, Abilities) mappings. 150 remain scaffold-only — role definitions without the competency data that enables assessment, gap analysis, and competency evaluation.

At the current authoring rate, completing all 150 roles manually would require an estimated 6-12 months of sustained effort. For a solo-operator project, this is the single largest bottleneck on the roadmap. Every use case — PE due diligence, EU AI Act compliance, model risk governance, CDAIO toolkit — depends on KSA coverage for its relevant roles.

Constraint Inversion (Pass 4) tested the assumption that Thomas must author every KSA manually. The finding: AI-assisted authoring can potentially compress the timeline from months to weeks, shifting the bottleneck from authoring to review.

## Decision

**KSA authoring will use an AI-assisted workflow: Claude drafts KSAs based on the existing 37-role reference set and source framework data; Thomas reviews, refines, and approves.**

Before scaling this approach, a quality validation test (R02) must be completed:

1. Author KSAs for 5 roles using AI assistance
2. Blind-compare quality against the 37 manually-authored roles
3. Evaluate on: completeness, accuracy against source frameworks, consistency with existing KSA style, and usefulness for assessment
4. If quality is comparable (defined as: no systematic deficiencies that would require rewriting rather than editing), adopt the AI-assisted workflow for all remaining roles
5. If quality falls short, identify specific failure modes and iterate on the authoring process before scaling

## Rationale

**The bottleneck is production, not expertise.** The 37 existing KSA sets establish a clear pattern — structure, depth, source framework references, and assessment applicability. The knowledge required to author KSAs is available in the source frameworks (NICE, O*NET, SFIA, DAMA DMBOK, ESCO). The constraint is the time required to synthesize this knowledge into ATLAS's format, not the availability of the knowledge itself.

**AI-assisted authoring rebalances Thomas's time toward high-value activities.** Thomas's irreplaceable contribution is judgment: deciding which source framework interpretation to privilege, how to weight competing KSA definitions, and whether the resulting competency model maps to real-world practice. Drafting — the mechanical synthesis of source framework content into ATLAS format — is the commodity step. Shifting drafting to AI and review to Thomas produces higher throughput without sacrificing the quality judgment that makes ATLAS credible.

**The reference set enables quality calibration.** Unlike greenfield authoring, AI-assisted KSA production has a built-in benchmark: the 37 existing roles. This means quality can be measured, not assumed. The R02 test is designed to produce a go/no-go signal before committing to the approach at scale.

**The timeline impact is significant.** If AI-assisted authoring works:

| Scenario | Authoring Time | Review Time | Total per Role | 150 Roles |
|----------|---------------|-------------|----------------|-----------|
| Manual only | 2-4 hours | N/A | 2-4 hours | 300-600 hours |
| AI draft + human review | 15 min (draft) | 30-60 min (review) | 45-75 min | 112-187 hours |

A 3-5x speedup shifts the full KSA completion timeline from "blocks the roadmap for months" to "completes alongside product development."

### Quality Gates

AI-assisted KSAs are not auto-published. Each role goes through:

1. **AI draft** against source framework data and existing KSA reference set
2. **Thomas review** for accuracy, completeness, and practical applicability
3. **Consistency check** against the authoring methodology documentation (R12)
4. **Provenance tagging** — each KSA records whether it was human-authored, AI-assisted, or AI-drafted with human review

The provenance tagging is important for credibility. When ATLAS reaches external adoption, users should know the authoring methodology. Transparency about AI assistance — done well and with quality controls — is a credibility asset, not a liability.

## Consequences

**Positive:**
- Compresses KSA authoring timeline by 3-5x
- Frees Thomas's time for methodology design, market development, and validation — activities that only he can do
- Creates a repeatable workflow for ongoing role additions (agentic AI roles, emerging roles)
- Provenance tagging demonstrates responsible AI use — consistent with Thomas's positioning

**Negative:**
- Risk of subtle quality degradation that only surfaces when KSAs are used in real assessments — mitigated by the R02 quality test before scaling
- AI-drafted KSAs may converge on similar patterns, reducing the variation that makes a taxonomy useful for distinguishing between similar roles — requires active monitoring during review
- Dependence on AI tooling for ongoing authoring creates a process dependency

**Risks:**
- R02 quality test fails — AI-drafted KSAs are systematically lower quality. Mitigation: identify specific failure modes. If failures are limited to certain role types (e.g., highly specialized NICHE roles), use AI assistance for standard roles and reserve manual authoring for complex roles.
- Provenance tagging creates perception of "AI-generated content." Mitigation: frame as "AI-assisted with human expert review" — emphasize the review, not the draft.

## References

- Ensemble Brainstorm — ATLAS Roadmap, Pass 4: Constraint 2 ("Thomas operates alone")
- Ensemble Brainstorm — ATLAS Roadmap, Scoring: R02 (AI-assisted KSA authoring quality test — Roadmap Anchor)
- Ensemble Brainstorm — ATLAS Roadmap, Pass 4: Assumption Test Queue
- Current KSA distribution: 37 roles with KSAs across GOV(73), ENG(53), DEV(46), DSM(38), RSK(35), ANL(30), LDR(24), OPS(23); NICHE(0), REG(0)
