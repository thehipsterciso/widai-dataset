# R04: PE Workforce Due Diligence Assessment Methodology

**Document Status:** Published
**Version:** 1.0.0
**Date:** 2026-03-27
**Author:** WIDAI Methodology Team
**Applicable To:** PE acquisition due diligence (target company data/AI workforce assessment)
**Engagement Model:** 30-day assessment, $50-75K per engagement

---

## What This Assessment Answers

When a PE firm evaluates a data or AI-enabled company, three workforce questions determine deal success:

1. **Does this team have the people to execute the value creation plan?**
   Can they build the ML model? Implement the governance program? Scale the platform? Or do they need to hire, and if so, how quickly can we find people in a tight market?

2. **What will it cost to close the gaps?**
   Which roles are missing? How hard to hire? Will a consultant bridge be faster? Can we develop existing people? How much time will integration planning take?

3. **Who are the key person risks?**
   Are there irreplaceable people? If the CDO leaves, does the deal die? Or is the team distributed? How much does it cost to retain the critical people?

The WIDAI PE Assessment answers all three questions with defensible, evidence-based scoring. It's not a gut feel, and it's not subjective. Every score traces back to observable evidence: certifications, work history, documented experience, and measurable KSA requirements.

---

## How It Works: The 30-Day Process

The assessment runs in 5 phases over 30 days. The timeline is designed to fit PE acquisition diligence windows (typical: 60-120 day process; workforce assessment happens in parallel with financial and legal DD).

### Phase 1: Scoping & Kickoff (Days 1-3)

We start with your value creation plan. What are the 3-5 things that drive value in this deal? (Examples: "Build real-time pricing ML model," "Implement data governance for regulatory compliance," "Consolidate three companies' data platforms.")

From there, we map the plan to workforce requirements. Using WIDAI, we select a reference architecture—a baseline organizational model for a company of this size and maturity level. (A 15-person early-stage analytics team has different needs than a 50-person scaled operation.)

We also send a data request to the target company: org chart, role descriptions, team profiles, and optional evidence artifacts (certifications, resumes, work samples). This is the data we'll assess against.

**Deliverable:** Architecture selection memo and data request package.

### Phase 2: Data Collection & Role Mapping (Days 4-10)

The target company returns org data. We map each person to WIDAI roles—not by job title alone, but by responsibilities and scope. "Data Engineer" in one company might map to a senior platform role; in another, an individual contributor role. We get specific.

For each person, we compile capability evidence: certifications, work history, projects they've shipped, technical depth. The evidence is what we score, not a subjective interview impression.

For high-criticality roles with weak evidence, we recommend optional interviews (30-45 minutes each, typically 3-5 people). These aren't performance evaluations—they're technical depth checks. How well does the ML lead understand the company's model architecture? Can the CDO articulate the governance operating model?

**Deliverable:** Complete role mapping and capability evidence matrix.

### Phase 3: Assessment Scoring (Days 11-20)

This is where the model runs. For each role, we score four dimensions:

**Coverage:** Is the role filled? At what seniority? Full-time or fractional? We calculate: (actual headcount / required headcount) × seniority adjustment × FTE adjustment. If you need 2 FTE Data Engineers and have 1.5 FTE at correct seniority, your coverage score is 75.

**Capability:** Does the person have the KSAs required for the role? KSA = Knowledge, Skill, or Ability. An ML Engineer needs to know model risk frameworks, can build neural networks, and can troubleshoot in production. We score capability based on evidence: certifications (+40%), work experience (+35%), credentials (+30%). The evidence must exist; we don't infer capability.

**Criticality:** How important is this role to the value creation plan? Not generic importance—specific to your deal. If real-time pricing is the thesis, ML engineers are criticality 5 (single point of failure). BI developers are criticality 2 (supporting). This is deal-specific.

**Concentration Risk:** How much unique knowledge does this person hold? Data architecture? Governance decisions? Legacy system expertise? If the person leaves, is the deal delayed? We score this based on: unique knowledge concentration, difficulty of replacement (how long to hire someone with that expertise), and tenure risk (how likely are they to leave?).

From these four dimensions, we compute three composite scores:

- **Team Capability Index (TCI):** Weighted average of coverage × capability across all roles, weighted by criticality. Tells you: Is the team ready to execute?

- **Key Person Risk Score (KPRS):** Aggregate concentration risk. Identifies the highest-risk person and flags the top 3-5 dependencies. Tells you: Who can't be replaced?

- **Gap Severity Index (GSI):** Number and criticality-weight of missing roles against your reference architecture. Tells you: How many people do you need to hire?

Finally, we compute your **Workforce Readiness Score (WRS):** a single composite (0-100) combining all three indices. WRS is what your investment committee sees.

WRS bands:
- **Critical (0-39):** Team not ready. Deal thesis at risk. Red flag.
- **At-Risk (40-59):** Baseline capability. Significant gaps. Requires mitigation plan.
- **Adequate (60-74):** Team ready. Gaps are manageable. Standard execution.
- **Strong (75-89):** Team well-prepared. Low risk. Green light.
- **Exceptional (90-100):** Rare. Exceptional team. Workforce is a strategic asset.

**Deliverable:** WRS score, component scores, and scoring rationale.

### Phase 4: Analysis & Deliverable Production (Days 21-28)

We analyze gaps and develop the hiring roadmap. Which roles are missing? Rank them by (gap severity × criticality × market scarcity). The top 5-7 roles become your critical hiring priorities. For each, we provide a WIDAI-sourced job description seed, estimated hiring timeline (tight market = 6+ months for senior roles), and alternative staffing options (consultant bridge, internal upskilling, outsourcing).

We also identify key person mitigation strategies. For each high-concentration-risk person, we recommend: retention incentives (24-month bonus or equity vest), knowledge documentation (runbooks, architecture docs, mentoring), succession planning (develop internal backup), or external support (consultant bridge during backfill).

We produce four deliverables:

1. **Executive Summary** (1-2 pages): WRS score, three key findings, go/no-go signal, top 3 hiring priorities, key person risk summary. Designed for board presentation.

2. **Workforce Capability Map** (5-10 pages): Org chart with WIDAI role overlays, capability heat map, KSA coverage breakdown, strengths and gaps narrative.

3. **Gap Analysis & Hiring Priority Plan** (3-5 pages): All gaps ranked by impact, recommended hiring sequence, WIDAI job description seeds, estimated timelines, alternative approaches.

4. **Key Person Risk Assessment** (2-3 pages): Top 5 concentration risks, mitigation strategies by person, retention plan, succession roadmap.

**Deliverable:** Complete assessment package (13-20 pages, 4 PDFs).

### Phase 5: Delivery & Discussion (Days 29-30)

We present the assessment to your investment committee. 90 minutes: methodology overview, WRS score with interpretation, component scores, key findings, hiring plan, key person risk summary, next steps. Then Q&A.

The presentation is designed for PE context. We talk in your language: value drivers, execution risk, deal thesis, workforce risk signals. We don't overcomplicate with data science jargon.

---

## The Scoring Model: Why It's Defensible

Every PE operating partner we spoke with said the same thing: "Your biggest risk is that I'll challenge your score and you won't have evidence."

The WIDAI model is built to withstand challenge.

### Evidence Traceability

Every score traces to observable evidence. Coverage scores are based on org charts (objective headcount). Capability scores are based on certifications (verifiable), work history (documented), or interviews (recorded notes). If a person scores 75 on capability, you can ask: "What evidence supports that?" And we can point to: "She has AWS ML certification, shipped 3 production models at previous company, and can articulate the company's model governance framework."

There's no "I have a feeling this person is good." There's: "Here's the evidence, here's the standard, here's the score."

### KSA-Based Scoring

Our KSA requirements come from WIDAI, which synthesizes from NICE (U.S. government cybersecurity workforce framework), O*NET (Department of Labor), SFIA (international standards), and other authoritative sources. These aren't made-up requirements; they're industry standards.

When we score capability, we're comparing against these standards. A Chief Data Officer must have Knowledge of enterprise data strategy frameworks, Ability to lead through organizational resistance, and Skills in data governance design. These are testable, observable qualities—not vague concepts.

### Criticality Assignment (Deal-Specific)

Some assessments use generic criticality: "All CDOs are critical." That's weak. Our model makes criticality specific to your deal thesis.

Your value creation plan says: "Build real-time pricing ML model." From that, we ask: which roles are on the critical path? ML engineer: yes, criticality 5. Data engineer: yes, criticality 4 (pipeline required). BI developer: no, criticality 1 (reporting is not path). Finance analyst: no, criticality 1 (orthogonal to ML).

This specificity is what makes the score defensible in the target company conversation. You can explain why ML engineers matter for your thesis, and why you're not obsessing over analytics-only roles.

### Concentration Risk (Measurable Components)

Key person risk is the most subjective dimension—but we make it measurable.

We score three components:
- **Unique knowledge concentration:** What % of the organization's knowledge domain does this person hold exclusively? (0-100%)
- **Replacement difficulty:** How long to backfill this role? (1-2 months = Low, 3-6 months = Moderate, 6-12+ months = High)
- **Tenure risk:** Years in role, tenure in company, external market heat for their skills, equity incentives, stated intent to leave. (0-1.0 multiplier)

Concentration Risk Score = unique knowledge % × replacement difficulty × tenure risk × 100.

If someone scores 80/100 on concentration risk, you can unpack it: "This person holds 70% of data architecture knowledge, it would take 8 months to replace them (specialist role in tight market), and they've been in-role only 18 months (early-tenure flight risk)."

That's defensible. It's not gut feel.

---

## What You Get: The 4 Deliverables

### 1. Executive Summary (1-2 pages)

This is your investment committee document. It has:
- WRS score and band classification
- What that means in plain language
- TCI, KPRS, GSI component breakdown
- Three key findings (examples: "Data engineering is strong," "CDO is key person risk," "ML capability is absent—critical hire")
- Go/no-go signal: Proceed with standard planning / Proceed with caution / Recommend renegotiating
- Top 3 hiring priorities with estimated timelines
- Key person risk summary (top 1-2 risks and mitigation)
- Next steps: when to hire, when to retain, when to develop internal candidates

The entire executive summary is designed to be read in 5 minutes and answered the three questions we started with.

### 2. Workforce Capability Map (5-10 pages)

This is the integration planning document. It has:
- Org chart with WIDAI role overlays (color-coded: green = strong, yellow = moderate, red = gap)
- Team summary table (every person, with coverage/capability/criticality scores and recommendation)
- Role-level heat map (what percentage of each WIDAI role's KSAs is covered by the team?)
- Strengths narrative (where is the team excellent?)
- Gaps narrative (where are the vulnerabilities?)
- Integration implications (who stays, who develops, who needs to be replaced, what's the timeline?)

This is what your CHRO uses to make people decisions: who to promote, who to train, who to replace, where to hire.

### 3. Gap Analysis & Hiring Priority Plan (3-5 pages)

This is your recruiting roadmap. It has:
- Priority matrix: all gaps ranked by (1 - coverage) × criticality × market_scarcity
- Top 5-7 critical hires with detailed profiles: required seniority, key KSAs, market difficulty, hiring timeline
- WIDAI job description seeds (copy-paste ready; customizable for your company)
- Gantt chart: when to start recruiting which roles
- Resource plan: internal recruiting capacity, external agencies, consultant bridges
- Alternative approaches for hard-to-fill roles (internal upskilling, fractional/contract, outsourcing)

Your CHRO will use this to staff the integration team and plan recruiting.

### 4. Key Person Risk Assessment (2-3 pages)

This is your deal risk management document. Confidential—for PE firm and integration team only. It has:
- Top 5 concentration risk profiles: name, role, concentration risk score, unique knowledge areas, impact if they leave, identified backup
- Mitigation strategies: retention incentives (what to offer, when), knowledge documentation (what to document), succession planning (who to develop as backup), external support (consultant bridge)
- Retention strategy overview: total estimated cost over 24 months
- Succession roadmap: timeline to reduce concentration risk over 12 months

This informs your retention strategy, earnout structure, and integration planning.

---

## Reference Architectures: Benchmarking Your Team

We don't score in a vacuum. Every assessment uses a reference architecture—a baseline organizational model for companies of your size and maturity.

We have four reference architectures:

### Early-Stage (5-15 people)
Early-stage analytics function. Maybe the first data hire was 2 years ago. Platform is basic. No dedicated ML.

Expected roles: CDO/data lead, 1-2 data engineers, 1 BI developer, 0.5 governance specialist.

### Growth-Stage (15-30 people)
Operationalized data. Platform handles multi-team adoption. ML is in pilots or early production.

Expected roles: CDO, 2 data engineers, 1-2 data scientists, 2 BI developers, governance director, data quality manager.

### Scaled (30-60 people)
Advanced data platform. Production ML. Enterprise governance. Investment in optimization.

Expected roles: CAIO/CDO, VP engineering, 4 senior engineers, 2 ML leaders + 3 ML engineers, BI leads + developers, governance director, data product manager, compliance/privacy.

### Enterprise (60+ people)
Optimized. Strategic AI. Model governance. Portfolio-level data strategy.

Expected roles: CAIO, CDO, VP engineering, VP data science, VP analytics, model risk officer, governance director, master data manager, specialized roles (privacy, DataOps, etc.).

When we assess your company, we first identify which architecture it should map to based on size and maturity. Then we score your team against that baseline. If you're a 25-person growth-stage company and you have all the roles in the Growth reference architecture, you're in great shape. If you're missing the data science function, that's a critical gap for growth-stage.

This reference framework makes scoring consistent and comparable. Two different PE firms can both use WIDAI on similar-size targets and get comparable scores.

---

## What This Assessment Does NOT Do

We're transparent about limitations.

### 1. No Compensation Data (Yet)

We don't include "Year 1-3 workforce investment model" (salary costs, benefits, hiring costs, budget required). That's intentional. Compensation data is sensitive, market-specific, and requires updated data partnerships. We're building this for Phase 3. For now, if you need compensation modeling, we recommend pairing our assessment with: (a) your CHRO's market data, (b) Radford/Mercer surveys for benchmarks, or (c) Lightcast/Emsi for market scarcity pricing.

### 2. Not a Performance Evaluation

Assessment scores are NOT "how good is this person at their job." They measure readiness against the value creation plan. A VP of Sales might score low on data capability (because VP of Sales isn't a data role) but be excellent at their actual job. The assessment is silent on that.

### 3. Not a Psychometric Assessment

We don't measure cultural fit, personality, leadership style, or how well people work together. Those matter—and they should be part of diligence. But they're not in this assessment. Use 360-degree reviews, cultural assessments, and management interviews for those dimensions.

### 4. Not a Substitute for Management Interviews

The assessment enables management interviews; it doesn't replace them. After you see the assessment, you'll want to interview the CDAO, top engineers, and potential key person risks. The assessment tells you who to talk to and what questions to ask.

### 5. Not an Org Design Recommendation

We'll tell you what roles you're missing and who should stay. We won't tell you "you should reorganize into two teams" or "reporting should change." That's a decision you and your integration team make, informed by the assessment.

### 6. Limited Domain-Specific Insights

The assessment is generic across industries. If the target is a healthcare company with specialized privacy requirements (HIPAA), we'll flag data privacy as important—but we won't assess domain-specific healthcare data governance. Add industry-specific assessment layers if needed.

---

## Pricing & Engagement Model

**Price Range:** $50-75K per assessment
**Engagement Duration:** 30 days
**Payment Terms:** 50% upfront, 50% upon delivery

### Why This Price?

PE firms spend $500K-5M on financial due diligence, legal, technology assessment, etc. A $50-75K workforce assessment is noise against deal size. But it's premium against what currently exists (which is nothing—most PE firms do gut-feel workforce assessment).

We price based on value: the assessment answers three deal-critical questions and informs millions of dollars in value creation decisions. Compared to the cost of getting a hire wrong (ramp-up time, productivity loss, rework), the assessment pays for itself on the first critical hire.

### Engagement Scope

The scope includes:

- Phase 1-5 delivery (scoping, data collection, scoring, analysis, presentation)
- 30 days total calendar time
- All four deliverables (executive summary, capability map, gap analysis, key person risk)
- Up to 5 optional interviews with target company key people
- One investment committee presentation (90 minutes)

Out of scope (additional fee if needed):

- Compensation modeling (Year 1-3 investment plan) — separate engagement, $15-25K
- Extended post-close support or integration consulting — separate engagement
- Video interviews with target company (if >5 people) — additional fee per person
- Regulatory review or specialized assessment layers — additional fees as discussed

### Timeline Compatibility

The 30-day engagement fits PE deal timelines:
- Days 1-10 (weeks 1-2): Financial, legal, technology due diligence ramps up
- Days 11-20 (weeks 3): Investment committee preliminary review
- Days 21-30 (weeks 4): Final negotiation and closing

The workforce assessment is available before final committee vote and can inform valuation or earnout structure.

### Deal Structure & Earnouts

Some PE firms use workforce assessment to inform earnout structure. (Example: "If key person risk is high, create 12-month retention earnout; if low, shorter earnout.") The assessment can inform these decisions.

---

## How to Engage

### Step 1: Share the Value Creation Plan

Send us your operating plan or value creation thesis for the target company. 3-5 pages is plenty. What are you trying to build or transform? What data/AI role does that play?

### Step 2: Confirm Scope & Timeline

We confirm: which teams to assess (e.g., "data engineering, ML, analytics, governance — not business intelligence"), reference architecture selection (we recommend based on size/maturity), and timeline (30 days from data receipt).

### Step 3: Target Company Data Request

We send a data request package (org chart template, role description template, team profile template, evidence checklist). This goes from your firm to the target company.

### Step 4: Assessment Execution

We run phases 1-5 in parallel with your financial/legal/tech diligence. By Day 30, we deliver the full package and present to investment committee.

### Step 5: Post-Close (Optional)

90-day check-in: we validate assessments and help adjust hiring roadmap based on actual market conditions (sometimes hard-to-find roles become easier; sometimes tight market makes hiring slower).

---

## Quality Assurance & Limitations

Every assessment is reviewed for:

- **Evidence traceability:** Can we justify every score with evidence?
- **Scoring consistency:** Are we applying the same rigor to all roles?
- **PE relevance:** Are findings useful for deal decisions?
- **Defensibility:** Can we explain findings to the target company if needed?

We also maintain a confidence level for each assessment. Confidence factors:

- **Data quality:** Complete org chart, role descriptions, evidence artifacts = high confidence. Partial data = medium confidence.
- **Interview coverage:** Technical depth interviews with 3-5 key people = higher confidence. Desk-based assessment only = lower confidence.
- **Market knowledge:** For common roles (data engineers, analysts), we have strong market data. For specialized roles (MLOps engineers, chief risk officers), market data is less robust.

Every deliverable notes confidence levels so you know where to weight the findings.

---

## Who We Are

WIDAI is a curated dataset of 187 data/AI workforce roles and 497 KSAs (knowledge, skills, abilities, and tasks) across 12 knowledge domains, synthesized from NICE, O*NET, SFIA, DAMA, and other authoritative frameworks. We created the PE assessment methodology to translate WIDAI into actionable business value for PE firms evaluating data/AI teams.

We're not recruiting firms, consultants, or organizational design experts. We're data and workforce taxonomy experts who built a methodology to answer three specific PE questions. We partner with your CHRO, integration team, and recruiting partners—not replace them.

---

## Questions?

Contact: WIDAI Methodology Team
Email: methodology@widai.cdaio.gov

---

**Last Updated:** 2026-03-27
**Next Review:** 2026-06-27 (post-first-assessment feedback)
