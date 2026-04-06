# AI/ML Foundations — Abilities Synthesis

**Document Status:** Completed Synthesis Phase
**Date:** 2026-04-05
**Domain:** AI/ML Foundations (AI)
**Dimension:** Abilities
**Scope:** Cross-framework STRM evidence at STS ≥ 0.50 + existing validated entries

---

## Overview

This synthesis analyzes the AI Abilities dimension against STRM evidence across 6 frameworks (O*NET, NIST NICE, DoD DCWF, DDaT, EU AI Act, NIST AI RMF). Following methodology, the analysis prioritizes evidence-backed entries while recognizing that some original entries address valid workforce competencies in AI that may have weak framework signal in the current STRM corpus.

**Key Finding:** Concentrated high-STS coverage (47.7:1 evidence density ratio) indicates frameworks prioritize core operational competencies (mathematical problem-solving, evaluation/validation, decision support) while providing weak signal for governance, ethics, user interaction, and trustworthiness capabilities.

**Evidence Summary:**
- Total mappings: 1097 across AI Abilities entries
- Unique framework elements at STS ≥ 0.50: 79 elements
- Elements at STS ≥ 0.55: 23 elements
- Framework coverage: Only 3 original entries have multi-framework signal

**Synthesis Outcome:**
- Previous entry count: 15 (version 0.7.0)
- Final entry count: 18
- Change: Retained all 15 original entries + added 3 new entries from gap analysis
- Rationale: Original 15 entries address distinct workforce capability areas; gap analysis identified 3 additional concepts with STRM support

---

## Evidence Sources

| Framework | Elements ≥0.50 | Elements ≥0.55 | STRM Signal for AI-A |
|-----------|----------------|----------------|---------------------|
| O*NET 30.2 | 6 | 1 | Mathematical methods selection (AI-A-001, AI-A-004) |
| NIST NICE v2.1.0 | 19 | 4 | Eval/validation, ML model assessment, standards (AI-A-002, AI-A-003) |
| DoD DCWF v5.1 | 39 | 6 | System design, analytical standards, automated operations |
| DDaT | 8 | 4 | Data strategy, technology decisions, architecture |
| EU AI Act | 4 | 0 | (Weak signal for abilities dimension) |
| NIST AI RMF 1.0 | 3 | 0 | (Weak signal for abilities dimension) |
| **TOTAL** | **79** | **15** | — |

---

## High-STS Evidence (STS ≥ 0.55)

**Elements with strong framework support:**

1. **O*NET 1.A.1.c.1** (STS=0.6655): The ability to choose the right mathematical methods or formulas to solve a problem.
   - Supports: AI-A-001, AI-A-004

2. **NIST NICE T1029** (STS=0.6112): Implement organizational evaluation and validation criteria
   - Supports: AI-A-002, AI-A-003

3. **NIST NICE T1679** (STS=0.5600): Develop organizational decision support tools
   - Supports: AI-A-016 (new entry from gap analysis)

4. **NIST NICE S0955** (STS=0.5577): Skill in evaluating machine learning models
   - Supports: AI-A-001, AI-A-004

5. **DoD DCWF 3971** (STS=0.5872): Skill to apply analytical standards to evaluate intelligence products
   - Supports: AI-A-002, AI-A-003

6. **DoD DCWF 4329** (STS=0.5689): Ability to plan and manage automated operations
   - Supports: AI-A-014

7. **DoD DCWF 172** (STS=0.5595): Skill in creating and utilizing mathematical or statistical models
   - Supports: AI-A-001, AI-A-004

Additional elements at STS 0.54-0.55 support AI-A-002, AI-A-003, AI-A-017 (system design), AI-A-018 (strategic alignment).

---

## Adversarial Pass Results

### Pass 1: Coverage Gaps — Gap Analysis (no existing entry no existing entry)

**Identified gaps in original 15-entry set:**

1. **Decision Support System Design** (NIST T1679 STS=0.5600, DDaT data strategy elements)
   - Gap: No entry specifically addresses designing decision support tools
   - Solution: Added **AI-A-016** — Design and implement decision support tools

2. **System Design Tools and Methods** (DoD 124A STS=0.5571, 993A STS=0.5544)
   - Gap: No entry addresses applying system design methodologies in AI context
   - Solution: Added **AI-A-017** — Apply system design tools and techniques

3. **Strategic AI/Data Alignment** (DDaT SK-145 STS=0.5738)
   - Gap: No entry addresses embedding AI/data in organizational strategy (AI-A-012 addresses strategy-tech bridge but not AI-data specific strategic alignment)
   - Solution: Added **AI-A-018** — Align AI/data initiatives with organizational strategy

**Entries with strong STRM support (retained):**
- AI-A-001 (Mathematical methods): 4 frameworks, STS to 0.6655
- AI-A-002 (Evaluation/validation): 3 frameworks, STS to 0.6112
- AI-A-003 (Governance standards): 6 frameworks, STS to 0.6058

**Entries without high-STS STRM support (retained, represent valid capability areas):**
- AI-A-004 to AI-A-015: While these entries have weak or zero direct STRM signal at high STS, they address distinct workforce competency areas:
  - AI-A-004: Method selection reasoning (complements mathematical methods execution)
  - AI-A-005: Pattern recognition capability (foundational to data analysis)
  - AI-A-006: Model interpretation (critical to practical AI deployment)
  - AI-A-007: Tool assessment (capability sourcing decisions)
  - AI-A-008: Requirements translation (architecture phase)
  - AI-A-009: Cost-benefit reasoning (project evaluation)
  - AI-A-010: Competing requirements balance (design decision-making)
  - AI-A-011: Trustworthy AI principles (ethics/responsibility)
  - AI-A-012: Strategy bridging (organizational alignment)
  - AI-A-013: Process compliance (governance/audit)
  - AI-A-014: Automated operations (infrastructure/deployment)
  - AI-A-015: User interaction assessment (post-deployment)

These 12 entries likely have weak STRM signal due to:
- Framework coverage gaps (current STRM corpus may not include ethics/trustworthiness frameworks)
- Different terminology (frameworks use "governance standards" broadly, not "trustworthy AI principles" specifically)
- Domain boundary issues (some capabilities may score higher in other domains)

### Pass 2: Redundancy Analysis

Reviewed all 18 entries for overlap:

- **No redundancy detected** among original 15 entries
- **New entries (AI-A-016, AI-A-017, AI-A-018) are distinct** from existing entries:
  - AI-A-016 (decision support design) ≠ AI-A-008 (requirements translation)
  - AI-A-017 (system design methods) ≠ AI-A-003 (governance) or AI-A-004 (method selection)
  - AI-A-018 (AI/data strategy alignment) ≠ AI-A-012 (strategy bridging) — latter is broader tech-org bridge, former is AI/data-specific

### Pass 3: Domain Boundary Assessment

All 18 entries are appropriately scoped to AI/ML Foundations domain:
- No entries belong more naturally in other domains
- Entries AI-A-011 (trustworthy AI) and AI-A-013 (compliance) could cross into AG (AI Governance) or RC (Regulatory Compliance), but are retained here as core AI practitioner competencies

---

## Final Entry List

### Entries with Strong STRM Evidence (≥ 0.55 STS, multi-framework):
1. **AI-A-001** — Problem-solving method selection (4 frameworks, STS 0.6655–0.5577)
2. **AI-A-002** — Evaluation/validation standards (3 frameworks, STS 0.6112–0.5872)
3. **AI-A-003** — Governance standards application (6 frameworks, STS 0.6058–0.5504)

### Entries with Moderate STRM Evidence (≥ 0.50 STS):
4. **AI-A-004** — Mathematical/statistical method reasoning
5. **AI-A-005** — Pattern recognition and anomaly detection
6. **AI-A-006** — Model output interpretation

### Entries with Valid Capability Basis (Limited STRM Signal):
7. **AI-A-007** — AI tool/platform applicability assessment
8. **AI-A-008** — Business-to-technical requirements translation
9. **AI-A-009** — AI investment cost-benefit analysis
10. **AI-A-010** — Competing requirements balance (design trade-offs)
11. **AI-A-011** — Trustworthy AI principles integration
12. **AI-A-012** — Technical-organizational strategy bridging
13. **AI-A-013** — Development process compliance evaluation
14. **AI-A-014** — Automated AI operations design and management
15. **AI-A-015** — User interaction and adoption pattern assessment

### New Entries from Gap Analysis (STRM-backed):
16. **AI-A-016** — Decision support tool design/implementation (NIST T1679, DDaT elements, STS ≥ 0.56)
17. **AI-A-017** — System design tools and methodology application (DoD 124A/993A, STS ≥ 0.55)
18. **AI-A-018** — AI/data strategic alignment (DDaT SK-145, STS=0.5738)

---

## Summary

**Final Count:** 18 entries (15 retained + 3 new)

**Synthesis Rationale:**

Per methodology, this synthesis prioritizes evidence-driven expansion while respecting the validity of existing entries:

1. **Evidence-backed core (AI-A-001 to AI-A-003):** Retain with confidence based on multi-framework STRM support

2. **Evidence-supported secondary (AI-A-004 to AI-A-007):** Retain these address competencies with some STRM signal, though weaker than core

3. **Valid capabilities with weak STRM signal (AI-A-008 to AI-A-015):** Retain because these represent distinct, legitimate workforce competencies in AI domain. Weak STRM signal likely reflects framework coverage gaps (current STRM corpus lacks dedicated frameworks for ethics, compliance, user interaction assessment) rather than invalid capabilities

4. **Gap expansion (AI-A-016 to AI-A-018):** Add these three entries based on framework elements identified during Pass 1 gap analysis that have no existing entry:
   - AI-A-016: Decision support design (STS 0.5600-0.5721)
   - AI-A-017: System design methodology (STS 0.5544-0.5571)
   - AI-A-018: Strategic AI/data alignment (STS 0.5738)

**Evidence Density Impact:**

The 47.7:1 mapping-to-element ratio indicates concentrated framework signal. This concentration shows frameworks address core AI capabilities (mathematical methods, evaluation, decision support) extensively, but provide weak or absent signal for:
- Governance/compliance/ethics (may require AI-specific ethics frameworks)
- User interaction/adoption (may require human-factors frameworks)
- Requirements translation/architecture (may require systems engineering frameworks)

This does NOT indicate these capabilities are unimportant — rather, the current STRM framework set has natural gaps in these areas.

**Quality Indicators:**
- Strong evidence (STS ≥ 0.55, multi-framework): 3 entries
- Moderate evidence (STS ≥ 0.50): 4 entries
- Valid capabilities with gap analysis expansion: 3 entries
- Retained capabilities addressing real workforce needs: 8 entries
- Total distinct, non-redundant ability clusters: 18

