<p align="center">
  <img src="docs/assets/widai-at-a-glance.svg" alt="WIDAI — 187 roles, 12 KSA domains, 70+ frameworks, one standard" width="100%"/>
</p>

# WIDAI — Workforce Initiative for Data and AI

**The first machine-readable, cross-framework workforce taxonomy built specifically for data and AI.**

Here is the question every organization building with data and AI eventually runs into — and the one nobody has standardized an answer for: *who do we need, what should they know, and how do we measure the gap between where we are and where we need to be?*

There are frameworks that describe cybersecurity roles. Frameworks that describe general occupations. Frameworks that describe IT skills. Not one of them was built for the discipline that now underpins every enterprise strategy but has no shared language for its workforce. Think about that for a second. The labor market has had O\*NET for forty years. Cybersecurity has had NICE for a decade. Data and AI — the function that boards are betting their competitive future on — has nothing.

WIDAI fills that gap. It defines 187 roles across the full data and AI organization, maps knowledge, skills, abilities, and tasks across 12 knowledge domains using a shared-pool model, and unifies 70+ source frameworks — NIST NICE, O\*NET, SFIA, DAMA DMBOK, ESCO, EU AI Act, ISO 42001, SR 11-7, and dozens more — into a single dataset with full source provenance.

Every mapping traces back to where it came from. Every role carries context from every framework that describes it. One taxonomy that speaks every framework's language simultaneously.

---

## The Problem Nobody Talks About Honestly

Organizations are making consequential workforce decisions — hiring data teams, restructuring AI functions, assessing regulatory readiness, evaluating acquisition targets — and they are doing it with frameworks that were never designed for this work. They translate between NICE and O\*NET and SFIA manually, on whiteboards, in spreadsheets that live on one person's laptop. They map regulatory obligations to roles in someone's head. They assess team capability against standards that do not exist in any formal sense.

This is not a tooling gap. It is an infrastructure gap. And the people closest to it — the CDIAOs, the CISOs, the PE operating partners running diligence on a data-heavy target — already know it. They just do not have a better option. So they do what everyone does when the standard does not exist: they build something ad hoc, it works well enough for this engagement, and then it dies on the vine because it was never designed to be reusable.

What if someone built the reusable version? Not a product that locks you into a vendor's taxonomy. Not a consulting engagement that produces a deliverable and walks away. An open, evidence-based reference dataset that any tool, any methodology, any assessment can build on top of.

That is what WIDAI is.

<p align="center">
  <img src="docs/assets/market-opportunity.svg" alt="Market opportunity across PE, EU AI Act, Model Risk, and Agentic AI" width="100%"/>
</p>

---

## What Does This Actually Make Possible?

Let me be specific, because the last thing any of us need is another framework pitch that sounds impressive and delivers nothing.

### PE Workforce Due Diligence

You are an operating partner evaluating a data-heavy acquisition target. Today you assess the workforce through interviews, reference checks, and gut feel. The team that will determine whether the value creation plan succeeds or fails gets evaluated with less rigor than the financial model.

WIDAI enables a standardized assessment that maps the target's data/AI team against a reference taxonomy, produces a composite Workforce Readiness Score, identifies key-person risks, and models the Year 1–3 workforce investment — delivered in 30 days, priced as deal-level trivial.

<p align="center">
  <img src="docs/assets/example-assessment-output.svg" alt="Example PE assessment output — Workforce Readiness Score with dimension breakdowns" width="100%"/>
</p>

One PE firm adoption cascades to assessments across every portfolio company. No other use case has that multiplier.

### EU AI Act Compliance — Before August 2026

The EU AI Act enforcement deadline is five months away. Organizations that deploy high-risk AI systems need to demonstrate human oversight, risk management, and governance structures staffed by people with defined competencies. Most of them cannot answer the question: *which roles in my organization satisfy which obligations?*

WIDAI maps regulatory obligations to the people who must fulfill them — across EU AI Act, NIST AI RMF, and ISO 42001 simultaneously. Not a compliance workflow tool. A workforce blueprint that tells you which two hires cover the most regulatory surface area if your budget is limited.

### AI Model Risk Governance (SR 11-7)

Financial institutions governing AI models under SR 11-7 need three lines of defense with independence requirements, but no published reference architecture maps the organizational design. WIDAI provides it — defined roles, staffing ratios, cross-regulatory context. The reference architecture that consulting firms charge seven figures to build custom, delivered as a reusable standard.

### Agentic AI Workforce Design

Agent Supervisor. Agent Orchestrator. AI Trust Engineer. Human-AI Teaming Specialist. These roles are being created ad hoc at enterprises right now, without a shared vocabulary, without defined competencies, without any framework reference. WIDAI provides the first structured role definitions for a workforce category that does not exist in any established framework. Zero other sources define these roles. That is not a claim — it is an observable fact.

### CDAIO Week 1 Assessment

You just got hired as a Chief Data and AI Officer. The operating partner expects a team assessment by Week 2 and a hiring plan by Week 3. You do not need a 187-role taxonomy to study. You need a tool that produces answers on the timeline you are accountable to. WIDAI's assessment methodology was designed for exactly this — map the current team, identify the three biggest gaps, produce the plan.

---

## Why This Doesn't Already Exist

<p align="center">
  <img src="docs/assets/competitive-position.svg" alt="Competitive positioning — WIDAI occupies a category of one" width="100%"/>
</p>

Lightcast processes billions of job postings and has compensation data updated biweekly. Excellent at that. Eightfold builds proprietary organizational taxonomies for individual enterprises. Excellent at that too. NICE defines cybersecurity roles with granular KSAs. O\*NET covers the general labor market with standardized occupational data. Each does its thing extremely well.

None of them maps a single role to obligations under multiple regulatory and professional frameworks simultaneously. That cross-framework mapping — where an AI Governance Manager carries context from EU AI Act Article 14, NIST AI RMF GOVERN functions, ISO 42001 controls, DAMA DMBOK knowledge areas, and SFIA skills, all in one record, all with source provenance — is the feature that does not exist anywhere else.

It is also genuinely difficult to replicate, because it requires not just data access but the kind of judgment about how these frameworks relate to each other that only comes from having worked across them for two decades. That is the moat. Not the data. The judgment encoded in the data.

---

## How The Scoring Actually Works

Every claim in this dataset is evidence-based. WIDAI uses NIST IR 8477 Set Theory Relationship Mapping (STRM) as the formal methodology for mapping external frameworks against the KSA pool. Each framework element is scored computationally using a multi-method pipeline — not expert opinion, not manual classification, not vibes.

<p align="center">
  <img src="docs/assets/strm-methodology.svg" alt="STRM scoring methodology — multi-method computational pipeline" width="100%"/>
</p>

The primary method is Cross-Encoder Semantic Textual Similarity (STS), which processes both texts jointly through cross-attention — the current state of the art for semantic similarity in NLP research. Four secondary methods provide independent validation: BERTScore (token-level contextual matching with Precision/Recall/F1 directionality), NLI Cross-Encoder (entailment vs. contradiction probabilities), Bi-Encoder Cosine Similarity, and Jaccard Token Overlap as a lexical baseline.

Every scored pair produces a rationale file with all five method scores, interpretive significance reasoning for each method, the NIST relationship type classification, and full source provenance. 126 rationale files for the first framework mapping alone. That is the level of evidentiary rigor this dataset is built on.

Why does this matter? Because when a PE operating partner asks "how did you determine that this role maps to these obligations?", the answer is not "an expert said so." The answer is a traceable chain of computational evidence with multiple independent validation methods. That is the difference between a reference dataset and an opinion.

---

## Execution Roadmap

Every roadmap item has been scored on impact, overlooked probability, and dependency weight. The sequence is determined by structural dependencies — what must be true before the next thing can be built — not by which use case sounds most appealing in a strategy meeting.

<p align="center">
  <img src="docs/assets/roadmap-timeline.svg" alt="Roadmap from validation to scale — five phases, dependency-driven" width="100%"/>
</p>

**Phase 0 — Validate (Complete).** Four parallel tests executed: coverage gap (PASS, 92.2%), AI-assisted KSA quality (PASS, 4.26/5), license audit (CONDITIONAL, 19 frameworks GREEN), consistency audit (PASS, 8.2/10). All assumptions validated. Phase 1 cleared for execution. [Full results →](docs/roadmap/PHASE-0-VALIDATION-SPRINT-RESULTS.md)

**Phase 1 — First Product (In Progress).** PE assessment methodology fully specified. KSA architecture restructured from role-centric to shared domain pool (12 knowledge domains, many-to-many mappings). STRM framework mapping cycle active — each framework produces per-element rationale files with multi-method computational scoring. Four Tier 1 frameworks complete: O\*NET 30.2 (126 elements), NIST NICE v2.1.0 (2,148 elements), DoD DCWF v5.1 (2,945 elements), and UK DDaT (189 elements). Two Tier 2 frameworks complete: EU AI Act (62 elements) and NIST AI RMF 1.0 (70 elements) — both regulatory/standards frameworks mapped using the dual-provenance outcome→competency methodology with Functional rationale. 5,540 total elements scored across US, international, and regulatory frameworks. 32 gap signals with cross-framework corroboration accumulating. [STRM progress →](docs/README.md)

**Phase 2 — Compliance + Validation.** EU AI Act obligation-to-role mapping ships before August 2026 enforcement. Cross-regulatory role coverage analysis produces the differentiating feature. Regulatory practitioners validate the mappings.

**Phase 3 — Expand.** Agentic AI role definitions. SR 11-7 organizational design patterns. CDAIO assessment toolkit. Built on the credibility established by a validated pilot and compliance market presence.

**Phase 4 — Scale.** API. Graph database. Full KSA coverage. Funded by Phases 1–3 revenue.

> Nineteen Architectural Decision Records document the reasoning behind every major decision — what was chosen, what was considered, and what the consequences are. [Full roadmap analysis and ADRs →](docs/roadmap/)

---

## Current State — Honest Assessment

WIDAI is in active development at version 0.5.8. Transparency about where things stand is a feature, not a disclaimer.

**What exists today:** 187 roles defined across 10 categories. KSAs organized across 12 domain pools with active enrichment through STRM framework mappings. 70+ source frameworks with provenance. Shared-pool KSA architecture with many-to-many role mappings. Entity-separated architecture designed for graph database ingestion. Multi-method computational scoring pipeline producing per-element rationale files. Six framework STRMs complete — four Tier 1: O\*NET 30.2 (126 rationale files), NIST NICE v2.1.0 (2,148 rationale files), DoD DCWF v5.1 (2,945 rationale files), UK DDaT (189 rationale files); plus two Tier 2: EU AI Act (62 rationale files) and NIST AI RMF 1.0 (70 rationale files) — both regulatory/standards frameworks with Functional rationale and dual-provenance methodology. 5,540 total rationale files. 32 gap signals registered across six STRMs with cross-framework corroboration accumulating.

**What has been validated:** Phase 0 testing confirmed that current coverage supports a PE assessment pilot (92.2% KSA coverage across 5 archetypes), that AI-assisted authoring meets quality standards (4.26/5), and that a clean commercial pathway exists (19 frameworks GREEN for commercial use). The hypothesis is tested, not assumed.

**What does not exist yet:** Full role-KSA mappings at target depth — requires STRM completion across remaining Tier 1–4 frameworks and Phase 1D synthesis. Populated regulatory context fields. A pilot engagement partner. An API.

The honest version is always the marketing version when the fundamentals are sound. And they are.

---

## How Decisions Get Made

This project does not operate on intuition. The roadmap was produced through a structured five-pass analysis — Forward Decomposition, Reverse Induction, Perspective Rotation, Constraint Inversion, and Second-Order Mapping — applied against six priority use cases.

| Decision | Record | Core Reasoning |
|----------|--------|----------------|
| Sequence by dependencies, not priority | [ADR-001](docs/roadmap/adr/ADR-001-dependency-driven-roadmap-sequencing.md) | Priority rankings create serialization traps. |
| PE due diligence as first product | [ADR-002](docs/roadmap/adr/ADR-002-pe-due-diligence-as-beachhead.md) | One PE firm adoption cascades to 8+ portfolio assessments. |
| Ship on current data, don't wait | [ADR-003](docs/roadmap/adr/ADR-003-ship-on-current-data-coverage.md) | Every month of deferred piloting is a month of deferred market validation. |
| EU AI Act as urgent parallel track | [ADR-004](docs/roadmap/adr/ADR-004-eu-ai-act-timeline-urgency.md) | August 2026 enforcement. The compliance window does not wait. |
| AI-assisted authoring with quality gates | [ADR-005](docs/roadmap/adr/ADR-005-ai-assisted-ksa-authoring.md) | 3–5x speedup. Contingent on quality validation. |
| Cross-regulatory mapping as differentiator | [ADR-006](docs/roadmap/adr/ADR-006-cross-regulatory-role-coverage.md) | The feature nobody else provides. |
| Assessment service, not dataset product | [ADR-007](docs/roadmap/adr/ADR-007-product-positioning-assessment-service.md) | Every buyer persona buys answers, not data access. |
| Shared-pool KSA architecture | [ADR-013](docs/roadmap/adr/ADR-013-shared-pool-ksa-architecture.md) | Domain-based KSA pool with many-to-many role mappings. |
| STRM-based KSA enrichment | [ADR-014](docs/roadmap/adr/ADR-014-strm-based-ksa-enrichment.md) | NIST IR 8477 adopted for evidence-based enrichment. |
| STRM — O\*NET 30.2 complete | [ADR-015](docs/roadmap/adr/ADR-015-strm-onet.md) | Multi-method scoring pipeline established. |
| STRM — NIST NICE v2.1.0 complete | [ADR-016](docs/roadmap/adr/ADR-016-strm-nice.md) | 2,148 elements scored. Cybersecurity boundary defined. |
| STRM — DoD DCWF v5.1 complete | [ADR-017](docs/roadmap/adr/ADR-017-strm-dcwf.md) | 2,945 elements scored. Federal data/AI workforce validated. |
| STRM — UK DDaT complete | [ADR-018](docs/roadmap/adr/ADR-018-strm-ddat.md) | 189 elements scored. International cross-validation. Tier 1 complete. |
| STRM — EU AI Act complete | [ADR-019](docs/roadmap/adr/ADR-019-strm-eu-ai-act.md) | 62 elements scored. First regulatory framework. Functional rationale. Tier 2 lead. |

> All 19 ADRs with full context, rationale, and alternatives considered: [`docs/roadmap/adr/`](docs/roadmap/adr/)

---

## Who Should Be Paying Attention

**If you evaluate data/AI teams as part of PE deal diligence or portfolio management** — you are the user this was designed to serve first. A pilot engagement produces value for both sides: you get a structured assessment methodology backed by a reference taxonomy, WIDAI gets market validation. That is a trade worth making.

**If you are navigating the EU AI Act and cannot answer which roles satisfy which obligations** — the compliance mapping ships before August 2026 enforcement. If your organization is in scope, this is the workforce blueprint that does not currently exist anywhere else.

**If you are a CDAIO or CISO in the first 90 days of a new role** — you are building the assessment and organizational design that WIDAI is being built to support. Your feedback on what is useful, what is missing, and what is wrong is more valuable than any framework analysis.

**If you study workforce taxonomies, role evolution, or organizational design for data/AI teams** — the dataset is available for research collaboration.

> Interested? Open an issue, or reach out through [The Hipster CISO](https://thehipsterciso.substack.com).

---

## Technical Documentation

The narrative above tells you why WIDAI exists and where it is going. The technical documentation tells you how it is built.

| Document | What It Covers |
|----------|----------------|
| [Architecture and Data Model](docs/TECHNICAL.md) | Entity-separated flat files, schema design, graph-ready structure |
| [Master Schema Design](docs/master-schema-design.md) | 25+ field JSON schema with nested regulatory and framework context |
| [STRM Framework Mappings](strm/) | NIST IR 8477 Set Theory Relationship Mappings with per-element rationale |
| [PE Assessment Methodology](methodology/R04-pe-assessment-methodology.md) | Scoring model, engagement workflow, deliverable specifications |
| [Framework Prioritization](docs/roadmap/phase-1b-framework-prioritization.md) | 70 frameworks assessed, 4-tier STRM execution sequence |
| [Roadmap Analysis](docs/roadmap/ensemble-brainstorm-widai.md) | Full five-pass strategic analysis with research citations |
| [All ADRs](docs/roadmap/adr/) | 17 Architectural Decision Records |

---

## About

WIDAI is built by [Thomas Jones](https://www.linkedin.com/in/yourprofilehere) — The Hipster CISO. Twenty years of executive leadership spanning cybersecurity, data governance, and AI strategy. Carnegie Mellon CDAIO Program. The person who spent two decades protecting enterprise data is uniquely qualified to unlock its value — because security, data governance, and AI strategy are the same discipline viewed from different altitudes. That convergence is where this project lives.

> [The Hipster CISO on Substack](https://thehipsterciso.substack.com) · [GitHub](https://github.com/thehipsterciso)

---

<p align="center">
  <sub>Version 0.5.6 · Copyright 2026 Thomas Jones · All rights reserved</sub>
</p>
