# Ensemble Brainstorm — WIDAI Roadmap
## Use-Case-Driven Five-Pass Analysis

**Date:** 2026-03-26
**Author:** Thomas Jones / The Hipster CISO
**Method:** Ensemble Brainstorm — Five-Pass Algorithm for Strategic Thinking
**Goal:** Build a dependency-driven roadmap for WIDAI, the first machine-readable, cross-framework workforce taxonomy for data and AI.

**Primary Use Cases Under Analysis:**
1. PE Workforce Due Diligence Standard (SOI: 20/25)
2. EU AI Act Compliance Role Mapping (SOI: 20/25)
3. Model Risk Governance Organizational Design (SOI: 20/25)
4. Agentic AI Workforce Design (SOI: 20/25)
5. CDAIO First-90-Days Toolkit (SOI: 15/25)
6. Cyber Insurance Workforce Risk Scoring (SOI: 20/25)

**Research Sources:** Five parallel research briefs conducted 2026-03-26 covering PE due diligence practices, EU AI Act compliance tooling, model risk governance for AI, agentic AI workforce design, and competitive taxonomy landscape. All findings cited below.

---

## PASS 1 — Forward Decomposition (Use Case Lens)

### What has to be true for each use case to work?

#### UC1: PE Workforce Due Diligence

**Market reality from research:** $2.6T in PE deal value annually (2025). 60% of deal value depends on operational execution requiring strong talent. Yet 60% of CEO replacements occur within Year 1 post-acquisition — suggesting pre-close talent assessment is failing. Current practice: resume collection, subjective interviews, psychometric assessments on leadership. Data/AI workforce assessment is nascent — Protiviti's seven-dimension AI maturity model is the closest thing, but it's a consulting framework, not a product.

**What WIDAI needs:**
- P1.1: Role coverage sufficient for typical data/AI team mapping (15-30 roles in a mid-market target)
- P1.2: A maturity scoring model that produces a defensible number (not a framework, a score)
- P1.3: Assessment methodology deliverable within 30-60 day deal timelines
- P1.4: Compensation/cost data for Year 1-3 investment modeling
- P1.5: Credibility with PE operating partners — at minimum one completed pilot assessment

**Gap between current state and need:** Roles exist (187). KSAs partially exist (37 of 187 roles). No scoring model. No assessment methodology. No compensation data. No pilot partner.

#### UC2: EU AI Act Compliance Role Mapping

**Market reality from research:** As of March 2026, only 8 of 27 EU member states have designated competent authorities. High-risk AI requirements enforce August 2, 2026 — five months from now. 79% of enterprises cite AI governance talent scarcity as a barrier. Existing tools (Credo AI, Vanta, OneTrust, Daiki) focus on compliance workflow automation — none provide workforce role mapping. The cross-framework mapping gap is confirmed: no tool bridges EU AI Act operators → internal organizational roles → NIST AI RMF → ISO 42001.

**What WIDAI needs:**
- P1.6: Role-to-regulation mapping for EU AI Act articles (14, 4, 43, 72, 25, 50)
- P1.7: Regulatory context fields populated for all governance and compliance roles
- P1.8: Provider/Deployer role distinction mapped to WIDAI roles
- P1.9: Cross-framework compliance mapping (EU AI Act + ISO 42001 + NIST AI RMF — the three frameworks organizations must navigate simultaneously)
- P1.10: Update cadence that tracks implementing acts and enforcement guidance

**Gap:** Schema now includes regulatory_context with EU AI Act fields, NIST AI RMF functions, jurisdictions, and ISO 42001 controls. Fields exist but are unpopulated. No obligation-to-role mapping methodology exists.

#### UC3: Model Risk Governance Organizational Design

**Market reality from research:** 72% of financial institutions have AI in production; only 9% have mature governance. Treasury's new FS AI RMF (February 2026) has 230+ control objectives. Banks are centralizing GenAI governance even when data/analytics are decentralized. Emerging roles: AI Model Risk Assessor, VP AI Risk Management. Big Four (KPMG, Deloitte, EY) are offering model risk consulting but not publishing machine-readable organizational design frameworks.

**What WIDAI needs:**
- P1.11: SR 11-7 roles fully defined in WIDAI (Model Owner, Model Developer, Model Validator, Model Risk Manager, AI Auditor)
- P1.12: Three-lines-of-defense organizational pattern with independence requirements
- P1.13: Staffing ratios (models per validator, analysts per line of defense) scalable from 5 to 500 models
- P1.14: Regulatory mapping to SR 11-7, OCC 2011-12, FS AI RMF, ISO 42001, EU AI Act
- P1.15: Financial services industry context (regulated environment, examination readiness)

**Gap:** RSK category has 24 roles and 35 KSAs. Some SR 11-7 roles likely exist. Regulatory context fields exist but are empty. No organizational design patterns or staffing ratios.

#### UC4: Agentic AI Workforce Design

**Market reality from research:** 79% of organizations report some agentic AI adoption. Only 11% have production systems. Gartner predicts 40%+ of agentic AI projects will be canceled by end of 2027 — governance failure is the primary driver. "AI Agent Orchestrator" identified as "most important job of 2026" (Eightfold.ai). Singapore MAIG launched January 2026 — world's first governance framework for agentic AI. No existing workforce framework (NICE, O*NET, SFIA, ESCO) includes agentic AI roles.

**What WIDAI needs:**
- P1.16: New role definitions for Agent Supervisor, Agent Orchestrator, AI Trust Engineer, AI Memory Engineer, AI Agent Developer
- P1.17: Skills mapping grounded in real deployment patterns (not theoretical)
- P1.18: Transition paths from existing roles (ML Engineer → Agent Developer, SRE → Trust Engineer)
- P1.19: Governance framework alignment (Singapore MAIG, NIST AI RMF, EU AI Act implications)
- P1.20: Quarterly update capability — this space is evolving faster than any other

**Gap:** These roles do not exist in WIDAI today. NICHE category has 9 roles and 0 KSAs. This is greenfield — first-mover advantage is time-limited.

#### UC5: CDAIO First-90-Days Toolkit

**What WIDAI needs:**
- P1.21: Assessment methodology that can be run in the first week
- P1.22: Gap analysis producing actionable org design recommendations
- P1.23: Industry-customizable templates (manufacturing vs. financial services vs. technology)
- P1.24: 90-day roadmap generator based on assessment results

**Gap:** Depends on role coverage and KSA completeness. The assessment methodology is the product — the dataset enables it.

#### UC6: Cyber Insurance Workforce Risk Scoring

**Market reality from research:** No commercial product or published methodology exists for quantitative workforce adequacy scoring in cyber insurance. Underwriters assess technical controls (MFA, EDR, backups) but not the people who operate them. The $14B+ cyber insurance market has no standardized workforce risk assessment. This is a confirmed white space.

**What WIDAI needs:**
- P1.25: Security, governance, and risk roles with sufficient granularity for staffing adequacy assessment
- P1.26: Benchmarking data (expected staffing levels by org profile)
- P1.27: Scoring model simple enough for underwriting (15-20 questions)
- P1.28: Partnership with one carrier or MGA for methodology validation

### Dependency Map (Use-Case Driven)

**Foundation layer (enables all use cases):**
- Schema modifications (done — 7 implemented)
- KSA coverage for roles used by the first 2-3 use cases
- Regulatory context population for governance/compliance roles

**UC1 (PE Due Diligence) depends on:**
- Sufficient role coverage for typical team mapping (~30-50 roles)
- A scoring/assessment methodology (the product, not the dataset)
- One pilot partner

**UC2 (EU AI Act) depends on:**
- Regulatory context field population
- Obligation-to-role mapping methodology
- Legal practitioner validation
- URGENT: August 2026 enforcement deadline — 5 months

**UC3 (Model Risk) depends on:**
- RSK category KSA completeness
- SR 11-7 role definitions with regulatory context
- Org design patterns (deliverable, not dataset)

**UC4 (Agentic AI) depends on:**
- New role creation (greenfield)
- Research grounding in real deployments
- Speed — this is a first-mover window

**UC5 (CDAIO Toolkit) depends on:**
- UC1 + UC2 + UC3 methodology components assembled into a toolkit

**UC6 (Cyber Insurance) depends on:**
- Security/governance role coverage (overlaps UC2 and UC3)
- Partnership with carrier/MGA
- Benchmarking data (requires real-world validation)

---

## PASS 2 — Reverse Induction (Use Case Failure Modes)

### What would cause each use case to fail completely?

#### UC1: PE Due Diligence Fails If...

**F1: The assessment takes too long for deal timelines.** PE due diligence is 30-60 days. If WIDAI-based assessment requires extensive customization per target, it misses the window. Current consulting assessments (Mercer, EY) work because they have standardized processes. WIDAI needs a standardized methodology, not a custom engagement.

**F2: The maturity score isn't defensible.** Research shows 72% of deal teams overestimate target capability. If WIDAI scores can't withstand challenge from the target company's management team ("your score is wrong because..."), the product dies after one failed engagement. Scoring must be calibrated against real outcomes.

**F3: Compensation data is missing.** The Year 1-3 workforce investment model is one of five deliverables and the one that speaks the financial language of PE. Without market compensation data, this deliverable is hollow. Current state: no compensation data, no data partnerships. Research confirms Lightcast has this data (32,000+ skills, market data updated biweekly). Partnership or licensing required.

**F4: No PE operating partner will pilot.** Research confirms: "gut feel and superficial reference checks" is the norm. Breaking that norm requires someone willing to try something new. Without Thomas's network producing one pilot partner, this use case is permanently theoretical.

#### UC2: EU AI Act Compliance Fails If...

**F5: WIDAI is slower than enforcement.** August 2, 2026 is five months away. Credo AI, Vanta, OneTrust are shipping compliance tools NOW. If WIDAI's regulatory role mapping isn't available before enforcement, the compliance tools win the market and role mapping becomes a feature of their platforms, not a standalone product.

**F6: The mapping is too generic.** Research shows organizations need role mapping specific to their AI Act operator type (Provider vs. Deployer). A generic "AI Governance Manager handles Article 14" isn't useful — the mapping must be contextual, specifying different role requirements for different operator types.

**F7: Legal practitioners don't validate it.** The EU AI Act is being interpreted through implementing acts and national guidance. A role mapping not validated by someone with regulatory expertise is a liability, not a tool. Thomas has cybersecurity/data governance background but not EU regulatory law.

#### UC3: Model Risk Governance Fails If...

**F8: Banks won't accept a non-consulting framework.** Research shows Big Four (KPMG, Deloitte, EY) dominate this space. Banks buy from consultants, not taxonomies. WIDAI must either partner with a consultancy or position as the reference framework that consultancies build on.

**F9: SR 11-7 purists reject AI-adapted interpretations.** Research reveals tension: some banks argue regulators should narrow SR 11-7 scope to exclude AI. If WIDAI's AI adaptation of SR 11-7 organizational design is seen as non-standard, regulated institutions won't adopt it.

**F10: Staffing ratios have no empirical basis.** How many model validators per AI model? Without real-world data, any number WIDAI proposes is aspirational. Research confirms the governance-practice gap: 72% have AI in production, 9% have mature governance. The data to calibrate staffing ratios may not exist yet.

#### UC4: Agentic AI Fails If...

**F11: Role definitions become stale within 12 months.** Research confirms: deployment timelines compressed from 6-8 months to 6-10 weeks in one year. 40% of agentic AI projects will be canceled by 2027. The roles defined today may not exist in their current form in 18 months.

**F12: Cloud providers define their own role frameworks.** Microsoft already publishes a five-pillar enterprise governance framework for agents. AWS, Google will follow. If vendor-specific role definitions fragment the market, a vendor-neutral taxonomy has less adoption surface.

**F13: "Agent washing" makes the category incoherent.** Research confirms: Gartner estimates only ~130 of thousands of "agentic AI vendors" are genuine. If the market can't distinguish real agentic AI from rebranded chatbots, role definitions for agent management lose their target.

#### UC6: Cyber Insurance Fails If...

**F14: Underwriters won't add workforce assessment to their process.** Research confirms: the underwriting application is already lengthy. Adding 15-20 workforce questions faces resistance unless a correlation between workforce adequacy and loss experience can be shown — and that data doesn't exist yet.

**F15: Organizations game the assessment.** Self-reported workforce data is inherently unreliable. Without verification mechanisms, the scoring is decorative.

### Hidden Constraints Surfaced

- **HC1: Time urgency varies dramatically by use case.** UC2 has a 5-month deadline. UC4 has a 12-18 month first-mover window. UC1 has no external deadline but needs pilot validation. UC3 and UC6 are longer-cycle.
- **HC2: Different use cases need different parts of the dataset.** UC1 needs role coverage + KSAs. UC2 needs regulatory context. UC3 needs RSK category depth. UC4 needs new roles entirely. Trying to complete the entire dataset before serving any use case is a serialization trap.
- **HC3: Compensation data requires external partnership.** No amount of dataset authoring solves this — it requires a commercial relationship with Lightcast, BLS, or similar.
- **HC4: Legal/regulatory validation requires domain expertise Thomas may not have.** EU AI Act interpretation and SR 11-7 adaptation need practitioner review, not just framework design.
- **HC5: The consulting channel may be required.** Banks buy from consultants. PE firms buy from advisors. If WIDAI is positioned as a raw dataset or taxonomy, the market may not recognize it as a product. The product surface matters as much as the data.

---

## PASS 3 — Perspective Rotation (Adversarial Personas)

### Persona A: PE Operating Partner (Validates/Challenges UC1)

"I manage a portfolio of eight companies. Three have meaningful data/AI teams. Show me what your assessment looks like on one of them — not hypothetically, but actually. Run it. Show me the output. If the one-page summary tells me something I didn't know about my own portfolio company, I'll use it on the next acquisition.

What I see that you might not: this isn't a taxonomy product, it's a services product. I don't buy taxonomies. I buy assessments. The taxonomy is your cost of goods. Price the assessment at $50-75K — that's noise against deal size. Deliver in 30 days. If the first one works, I'll mandate it across the portfolio. That's eight assessments in Year 1.

Your biggest risk is trying to sell me the dataset when what I need is the answer. I don't care about 187 roles. I care about three questions: does this team have the people to execute the value creation plan, what will it cost to fill the gaps, and who are the key person risks."

**Surfaced:** Package the assessment as a service, not a data product. Price it as deal-level trivial ($50-75K). The pilot IS the product. One successful pilot cascades to 8+ engagements through a single PE firm.

### Persona B: CISO at a Financial Services Firm (Validates/Challenges UC2, UC3, UC6)

"I'm trying to staff for three regulations simultaneously: EU AI Act, SR 11-7 adaptation for AI models, and our cyber insurance renewal. I have budget for maybe two new hires. What I need isn't a list of 50 roles I should have — it's a priority map that tells me which two hires cover the most regulatory surface area. Does WIDAI have that?

Where WIDAI could be genuinely useful: the cross-framework mapping. I'm translating between NICE (my team's current framework), SR 11-7 (what the Fed expects), and EU AI Act (what our European operations need). If WIDAI can show me one role that satisfies obligations under all three, that's worth more than 187 individual role definitions.

What concerns me: the regulatory context fields. If they're populated by framework analysis and not validated by someone who's been through a regulatory examination, I can't use them as evidence. My examiners will ask where this came from, and 'a cross-framework taxonomy built by one person' isn't the answer they'll accept."

**Surfaced:** Cross-regulatory role coverage (one role satisfying multiple regulatory obligations simultaneously) is a killer feature nobody else provides. But regulatory context must be validated by practitioners, not just populated from framework analysis. The compliance use cases need a review/validation step that involves actual regulatory practitioners.

### Persona C: Gartner Analyst Covering Data & AI Workforce (Validates/Challenges Competitive Position)

"I've tracked this space for a decade. Here's what I see:

Lightcast has the market data. They update biweekly, they have 32,000+ skills, they process billions of job postings. You can't compete on data freshness or market coverage. What Lightcast doesn't have is cross-framework standardization or regulatory context. They're a labor market intelligence platform, not a governance framework.

Eightfold and Gloat build organization-specific taxonomies. They're powerful but proprietary. Every customer gets a different taxonomy. There's no standard to benchmark against.

What nobody has — and what I'd actually cite in a research note — is a machine-readable, cross-framework reference taxonomy specifically for data and AI that maps to O*NET, ESCO, NICE, SFIA, and DAMA simultaneously. If WIDAI does that, it's in a category of one. But I won't cite a dataset. I'll cite a product that organizations use and can testify to. I need case studies before I write about this."

**Surfaced:** WIDAI's competitive position is confirmed: category of one in cross-framework, machine-readable, data/AI-specific taxonomy. Lightcast is complementary (market data), not competitive (different layer). But analyst coverage requires case studies. Getting to case studies requires getting to production use. The recognition goal depends on the adoption goal.

### Persona D: Newly Hired CDAIO at a PE-Backed Manufacturer (Validates UC1, UC5)

"I start Monday. The operating partner wants a 90-day plan by end of Week 2. I have a data team of 11 people — three data engineers, two analysts, someone who does a bit of everything with ML, a data governance lead, and four people whose titles don't match what they actually do.

What I need right now isn't a 187-role taxonomy. I need a way to map these 11 people to something standardized, identify the three biggest gaps, and present a hiring plan to the operating partner that's defensible.

If WIDAI could give me: (1) a quick assessment tool that maps my current team in under a day, (2) a gap analysis against a reference architecture for my company size and industry, and (3) a hiring priority list with job descriptions ready to post — I'd pay for that today. Before the taxonomy is complete. Before the API exists. I don't need perfect coverage. I need useful coverage for the roles I actually have."

**Surfaced:** The minimum viable product is much smaller than the full dataset. 30-50 roles with KSAs, a lightweight assessment tool, and reference org design templates by company size would serve this persona today. Perfect is the enemy of shipped.

### Disagreement Map

| Question | Persona A (PE) | Persona B (CISO) | Persona C (Analyst) | Persona D (CDAIO) |
|----------|----------------|-------------------|---------------------|---------------------|
| Is WIDAI a product or a dataset? | Product (assessment service) | Product (compliance tool) | Dataset (reference standard) | Product (toolkit) |
| What's the right scope to launch? | One use case, nailed | Cross-regulatory mapping | Full taxonomy | 30-50 roles, good enough |
| What creates credibility? | Completed pilot | Regulatory validation | Case studies + analyst citation | Immediate usability |
| What's the biggest risk? | Too slow to pilot | Unvalidated regulatory claims | No adoption evidence | Too complex to use quickly |
| What would they pay for? | $50-75K/assessment | Compliance subscription | N/A (cites, doesn't buy) | $5-10K toolkit license |

**Key disagreement:** Persona A and D agree WIDAI should ship a narrow, usable product now. Persona C says the full taxonomy is the moat. Persona B says regulatory validation is non-negotiable. The resolution: ship narrow, validate with practitioners, build toward completeness — in that order.

---

## PASS 4 — Constraint Inversion

### Constraint 1: The dataset must be complete before products ship

**If removed:** Which use cases could ship on current data (37 roles with KSAs, concentrated in GOV, ENG, DEV, DSM)?

Analysis of typical mid-market data/AI team (11-30 people):
- Data Engineers (ENG): covered
- Data Scientists (DEV): covered
- Analytics team (ANL): partially covered (14 roles, no KSA file? — need to verify)
- Data Governance (GOV): covered (25 roles, 73 KSAs)
- ML/AI (DEV): covered
- Leadership (LDR): partially covered (31 roles, 24 KSAs)
- Model Risk (RSK): partially covered (24 roles, 35 KSAs)
- Operations (OPS): partially covered (15 roles, 23 KSAs)

**Finding:** A PE due diligence assessment targeting a mid-market data/AI team of 15-30 people likely maps to 20-40 WIDAI roles. Of those, GOV, ENG, DEV, and DSM categories have KSAs. RSK, OPS, and LDR have partial KSAs. NICHE and REG have none.

**Decision point:** A pilot assessment could run today against current data, with acknowledged gaps in NICHE and REG categories. The pilot itself generates the evidence of what's missing — informing KSA authoring priority.

**Cost of this constraint:** Every month spent completing the dataset before piloting is a month of deferred market validation. If the PE use case hypothesis is wrong, complete data doesn't save it.

### Constraint 2: Thomas operates alone

**If removed:** Research confirmed that KSA authoring is the critical bottleneck (150 roles remaining). With a team of 3, you parallelize by category and compress 12 months to 4.

**What this reveals:** AI-assisted authoring is the leverage point. If Claude can produce KSAs at 80%+ quality that Thomas reviews and refines, the bottleneck shifts from authoring to review. That's a 3-5x speedup.

**Test now:** Author KSAs for 5 roles in a category with AI assistance. Measure quality against the 37 manually-authored roles. If quality is comparable, the KSA completion timeline compresses from months to weeks.

**Is this constraint real?** Partially. Thomas is sole author for quality and credibility. But AI tooling can draft, and Thomas reviews. The constraint is real for market development, partnerships, and validation — it's testable for data production.

### Constraint 3: No external revenue or partnerships

**If removed:** Lightcast partnership provides compensation data (fills the financial modeling gap in UC1). Legal practitioner on retainer validates regulatory context (fills the credibility gap in UC2 and UC3). One PE firm pilot at $50K funds the first quarter of operations.

**What this reveals:** The circular dependency (need revenue to buy data, need data to generate revenue) breaks at the pilot. A PE operating partner willing to pilot at $50K — on current data, with acknowledged gaps — funds the partnerships that fill the gaps.

**Is this constraint real?** It's real until the first pilot. After that, it's self-funding.

### Assumption Test Queue (Prioritized)

| Test | When | How | Decision It Informs |
|------|------|-----|---------------------|
| Can current 37 KSA-covered roles support a PE assessment pilot? | NOW | Map 3 real team structures against coverage | Ship UC1 pilot or wait for more KSAs |
| Can AI-assisted KSA authoring match manual quality? | NOW | Author 5 roles, blind-compare to manual | KSA completion timeline |
| Is there a PE operating partner in Thomas's network willing to pilot? | NOW | Direct outreach to Persona 2 audience | UC1 viability |
| Does EU AI Act role mapping have a market before August 2026? | Within 30 days | Test positioning with Persona 3 audience (CISOs, CDIAOs) | UC2 priority and timeline |
| Can regulatory context fields be validated by practitioners? | Within 60 days | Find EU AI Act / SR 11-7 practitioner for review | UC2 and UC3 credibility |

---

## PASS 5 — Second-Order Mapping

### If WIDAI succeeds (any use case reaches production adoption):

**Enables (not on roadmap):**
- WIDAI role IDs become a lingua franca in data/AI hiring. Job postings reference WIDAI codes. This creates a network effect — but also a maintenance obligation. Every role definition change affects downstream users.
- The PE assessment methodology becomes replicable. Other advisors request WIDAI licensing. This is the consulting toolkit use case (UC5/White Space 6) emerging organically.
- WIDAI data feeds the hc-enterprise-kg knowledge graph, creating a connected intelligence layer across Thomas's entire content and advisory ecosystem.
- The Hipster CISO newsletter gets exclusive, data-backed content from WIDAI research — competitive moat for content quality.

**Requires (not planned for):**
- Versioning and backward compatibility commitments. If someone builds on WIDAI v0.4.0, what happens when v1.0 changes role IDs?
- Data licensing framework. Open base taxonomy (like O*NET) with premium products on top? Or fully proprietary? This decision affects adoption velocity vs. revenue.
- Support infrastructure. Even one PE firm using WIDAI in production creates support obligations (questions, customization requests, bug reports).
- Liability considerations. If WIDAI-based assessments inform hiring/firing decisions or investment committee recommendations, accuracy becomes a legal concern.

### If WIDAI partially succeeds (most likely scenario):

**Partial success looks like:** One PE pilot completed. 2-3 CDIAOs using informally. 80% KSA coverage. No API — still flat files. No analyst coverage. Regulatory context partially populated.

**What partial success produces:**
- A validated methodology proof point that's sufficient for case study material
- Dataset that powers newsletter content for all three audience personas (the research IS content)
- Credibility signal for AI Integrity Agency positioning
- Reusable entity set for hc-enterprise-kg knowledge graph
- A clear signal about which use case has the most traction — informing where to double down

**What partial success requires that full success doesn't:**
- Conscious content extraction strategy — every piece of WIDAI research is potential newsletter/LinkedIn content
- Integration with existing Thomas Jones assets (newsletter, knowledge graph, LinkedIn positioning)
- Decision about whether partial success is the destination or a waypoint

### Liability Flags

- **L1: Source framework licensing.** O*NET is public domain. SFIA is copyrighted. DAMA DMBOK is copyrighted. NICE is public domain. EU AI Act text is freely available. Research confirmed no unified license audit has been done. Must be completed before any commercial use.
- **L2: Regulatory context accuracy.** If WIDAI says "AI Governance Manager owns Article 14 obligations" and a regulator disagrees, the organization that relied on WIDAI has a governance failure. Disclaimer + practitioner validation required.
- **L3: Assessment accuracy in hiring/investment decisions.** PE firms using WIDAI scores to inform deal decisions creates liability. Assessment methodology documentation must include limitations and confidence intervals.
- **L4: Agentic AI role durability.** Defining roles in a space evolving quarterly means some definitions will become obsolete. Version dating and deprecation policy required.

---

## SCORING AND CLASSIFICATION

### Consolidated Item Inventory (Use-Case Driven)

| ID | Item | Pass | Impact | Overlooked | Dependency | Classification |
|----|------|------|--------|------------|------------|----------------|
| R01 | Coverage gap test: map 3-5 real team structures against current data | P4 | High | High | High | **Roadmap Anchor** |
| R02 | AI-assisted KSA authoring quality test (5 roles) | P4 | High | High | High | **Roadmap Anchor** |
| R03 | PE pilot partner identification and outreach | P3,P4 | High | High | High | **Roadmap Anchor** |
| R04 | PE assessment methodology design (scoring model, deliverable templates) | P1,P3 | High | Medium | High | **Front of Queue** |
| R05 | Source framework license audit | P5 | High | High | High | **Roadmap Anchor** |
| R06 | EU AI Act obligation-to-role mapping | P1 | High | Medium | Medium | **Standard** |
| R07 | Regulatory context field population (GOV, RSK categories first) | P1,P2 | High | Low | High | **Front of Queue** |
| R08 | KSA authoring for priority roles (informed by R01 gap test) | P1 | High | Low | Medium | **Standard** |
| R09 | SR 11-7 three-lines-of-defense org design pattern | P1 | High | Medium | Medium | **Standard** |
| R10 | Agentic AI role definitions (5 new roles) | P1 | High | High | Low | **Watch List** |
| R11 | Cross-regulatory role coverage analysis (one role → multiple obligations) | P3 | High | High | Medium | **Roadmap Anchor** |
| R12 | Methodology documentation (how roles are selected, how KSAs are authored, how frameworks are weighted) | P3 | High | High | Medium | **Roadmap Anchor** |
| R13 | Compensation data partnership strategy (Lightcast/BLS) | P2,P4 | Medium | High | Low | **Watch List** |
| R14 | Regulatory practitioner validation (EU AI Act + SR 11-7) | P2,P3 | High | High | Medium | **Roadmap Anchor** |
| R15 | CDAIO assessment toolkit assembly (combines UC1-UC3 components) | P1 | Medium | Low | High | **Front of Queue** |
| R16 | Content extraction: turn WIDAI research into newsletter/LinkedIn | P5 | Medium | High | Low | **Watch List** |
| R17 | Versioning and backward compatibility policy | P5 | Medium | High | Low | **Watch List** |
| R18 | Data licensing model decision (open base + premium vs. proprietary) | P5 | High | High | Low | **Watch List** |
| R19 | API / data access layer | P1 | Medium | Low | Low | **Standard** |
| R20 | Neo4j / graph ingestion pipeline | P1 | Medium | Low | Low | **Standard** |
| R21 | Cyber insurance scoring methodology | P1 | Medium | High | Low | **Watch List** |
| R22 | NICHE and REG KSA files (currently zero) | P2 | Medium | Medium | Low | **Standard** |
| R23 | Schema validation tooling (validate.py → full schema) | P1 | Medium | Medium | Medium | **Standard** |
| R24 | KSA quality consistency audit across existing categories | P2 | High | High | High | **Roadmap Anchor** |
| R25 | Quick assessment interface ("map my team in under a day") | P3 | High | High | Medium | **Roadmap Anchor** |

### Dependency Chain (Topological Sort)

**Tier 0 — Tests that determine the roadmap itself (run NOW, inform everything):**
- R01: Coverage gap test (do current roles support a pilot?)
- R02: AI-assisted KSA quality test (can we accelerate authoring?)
- R05: License audit (can we commercially distribute?)
- R24: KSA quality audit (is existing data consistent enough to build on?)

**Tier 1 — Foundations for first product (PE Assessment):**
- R03: PE pilot partner identification
- R04: PE assessment methodology design
- R07: Regulatory context population (GOV, RSK first — enables UC2 and UC3)
- R12: Methodology documentation

**Tier 2 — First product delivery + compliance positioning:**
- R08: KSA authoring for priority roles (informed by R01 results)
- R06: EU AI Act obligation-to-role mapping
- R11: Cross-regulatory role coverage analysis
- R14: Regulatory practitioner validation
- R25: Quick assessment interface

**Tier 3 — Expansion from validated beachhead:**
- R09: SR 11-7 org design pattern
- R10: Agentic AI role definitions
- R15: CDAIO toolkit assembly
- R22: NICHE/REG KSAs

**Tier 4 — Scale infrastructure:**
- R19: API
- R20: Neo4j pipeline
- R23: Schema validation tooling

**Watch List (tracked, trigger-dependent):**
- R13: Compensation data partnership (triggered by UC1 pilot demand)
- R16: Content extraction (triggered by any research output)
- R17: Versioning policy (triggered by first external adoption)
- R18: Data licensing decision (triggered by first commercial inquiry)
- R21: Cyber insurance methodology (triggered by insurer interest)

---

## ROADMAP SUMMARY

### Phase 0: Validation Sprint (Weeks 1-2) — ✅ COMPLETE
Run R01, R02, R05, R24 in parallel. These four items determine the shape of everything that follows. If R01 shows current data supports a pilot, we build toward UC1 immediately. If R02 shows AI-assisted authoring works, the KSA completion timeline compresses. If R05 finds licensing issues, the commercial model changes. If R24 finds quality inconsistencies, we fix before scaling.

**Result:** All four tests passed. Go decision for Phase 1. KSA depth deficiency discovered post-sprint (ADR-012), leading to architectural correction (ADR-013, v0.5.0) and methodology redesign (ADR-014).

### Phase 1: KSA Enrichment via STRM (Revised 2026-03-31, ADR-014)

Phase 1 was originally scoped as "First Product (Weeks 3-8)" with direct KSA authoring (R08). ADR-012 identified a depth deficiency. ADR-014 supersedes the enrichment approach with NIST IR 8477 Set Theory Relationship Mapping, replacing bulk authoring with a framework-by-framework evidence-based methodology.

**Phase 1 is now four sub-phases:**

#### Phase 1A: Baseline KSA Enrichment
First-pass enrichment of the 12 domain KSA pools from current depth (5-19 KSAs/role, 363 total) to a reasonable baseline using domain expertise. This pass is explicitly pre-validation — STRM will validate, correct, and refine. The goal is sufficient pool depth for STRM to produce meaningful signal (not overwhelmingly "No relationship").

**Parallel work (not blocked by STRM):**
- R04: PE Assessment Methodology — ✅ COMPLETE
- R07: Regulatory context population (GOV, RSK categories)
- R12: Methodology documentation

#### Phase 1B: Framework Prioritization
Assess which of the 70+ WIDAI source frameworks contain KSA-equivalent concept types at sufficient granularity for STRM. Not all do — many are role-level references only (e.g., LinkedIn job postings, Glassdoor titles). Produce a prioritized execution sequence.

**Criteria:** KSA-equivalent concept types, machine-readable data availability, WIDAI role coverage breadth, strategic relevance to use cases.

**Deliverable:** Prioritized framework list documented here.

#### Phase 1C: Per-Framework STRM Cycle
For each framework in priority order, execute the full STRM cycle:

1. **Use case documentation** (NIST IR 8477 Section 3) — audience, purpose, concept types, rationale type, direction, exhaustiveness
2. **Canonical source acquisition** — exact version stored in `sources/` or version-pinned citation
3. **STRM mapping execution** — every focal document element mapped against WIDAI KSA pool per Table 5 format + Strength column (WIDAI extension)
4. **Per-FDE rationale files** — independent file objects preserving full reasoning at mapping-level resolution
5. **Gap issue registration** — every "No relationship" logged with context (nearest miss, suggested domain, authoring guidance)
6. **QA/QC gate** — complete review before proceeding to next framework
7. **ADR documentation** — summary statistics, key findings, anomalies, gap thematic analysis

**Seven deliverables per framework. No framework STRM proceeds until the prior one is QA'd and committed.**

**STRM format** (per NIST IR 8477 Table 5 + WIDAI extension):

| Column | Source |
|--------|--------|
| Focal Document Element (ID) | NIST IR 8477 |
| Focal Document Element Description | NIST IR 8477 |
| Rationale (Syntactic / Semantic / Functional) | NIST IR 8477 |
| Relationship (Subset of / Intersects with / Equal / Superset of / No relationship) | NIST IR 8477 |
| Reference Document Element (ID) — WIDAI KSA ID | NIST IR 8477 |
| Reference Document Element Description — WIDAI KSA Statement | NIST IR 8477 |
| Strength of Relationship (1-10) | WIDAI extension (from SCF practice) |

**Principles governing Phase 1C:**
- No synthesis before all frameworks are mapped
- No rushing through framework evaluations — quality over motion
- No deviation from NIST IR 8477 methodology
- Rationale preserved at full resolution (independent file objects)
- Every enriched KSA must trace to STRM evidence

#### Phase 1D: Synthesis
After all framework STRMs are complete and QA'd:

- Accumulated gap issues analyzed across all frameworks
- Cross-cutting KSAs identified from multi-framework alignment evidence
- Synthesis rules defined from observed evidence patterns — **not before**
- Enriched KSA pool constructed from synthesis findings
- Cross-STRM consistency validated (transitivity checks)
- Synthesis methodology documented in its own ADR

**The synthesis rules are intentionally undefined at this stage.** Defining them before evidence collection would bias the STRM evaluation. The rules emerge from the data.

**Phase 1 produces:** An externally validated, STRM-backed KSA pool at industry-standard depth with full provenance chain from every KSA to its source framework evidence.

### Phase 2: First Product + Compliance (Post-Synthesis)
PE pilot engagement (R03 — unblocked by enrichment completion). EU AI Act obligation mapping (R06). Cross-regulatory analysis (R11). Regulatory practitioner validation (R14). Quick assessment interface (R25). R04 Coverage dimension recalibrated against enriched pool.

### Phase 3: Expansion
SR 11-7 org design (R09), agentic AI roles (R10), CDAIO toolkit (R15). Informed by pilot feedback and compliance market validation.

### Phase 4: Scale
API, graph database, full KSA coverage, analyst engagement. Funded by Phase 2-3 revenue.

### New Repository Structure (Phase 1C onward)

```
atlas-dataset/
├── sources/                          # Canonical source documents (version-pinned)
├── strm/                             # STRM deliverables
│   ├── {framework}/
│   │   ├── use_case.json             # IR 8477 Section 3 documentation
│   │   ├── strm_mapping.json         # Table 5 + Strength mapping data
│   │   ├── rationale/                # Per-FDE reasoning files
│   │   └── qa_qc_report.json         # QA/QC evidence
│   └── issues/                       # Accumulated gap issues across all STRMs
├── ksas/                             # Domain-based KSA pools (enriched post-synthesis)
├── mappings/                         # Role-KSA mappings (rebuilt post-synthesis)
├── roles/                            # Role definitions
├── frameworks/                       # Framework metadata
├── methodology/                      # R04, R12 methodology docs
├── docs/roadmap/adr/                 # Architectural Decision Records
└── ...
```
