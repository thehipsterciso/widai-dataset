# How NIST NICE scopes boundary roles — and what it means for ATLAS

The NIST NICE Framework deliberately includes roles that are not exclusively cybersecurity, using a risk-management rationale: **any work that contributes to an organization's cybersecurity risk management objectives falls within scope**. SP 800-181 Rev 1 explicitly states the framework is "not meant to imply that the work roles and content included in the NICE Framework apply only to those fully embedded in the cybersecurity domain." This design choice — inclusive of adjacent roles, framed through a domain-specific lens — provides a direct template for ATLAS, but also comes with documented tradeoffs: a 2023 GAO review found that NICE's broad scope created adoption challenges, and major federal data agencies (BLS, Census, O*NET) do not reference it because it doesn't translate to traditional labor market metrics. ATLAS should adopt NICE's inclusive philosophy but with sharper boundary language and a formal core/adjacent/enabled tiering system to avoid the same pitfalls.

---

## Thirteen of fourteen investigated roles appear in NICE

The NICE Framework includes an extensive set of boundary roles — positions that exist across all IT organizations but are framed through a cybersecurity lens. Only Technical Writer lacks a standalone work role (though technical writing tasks are distributed across other roles). Here is the complete mapping:

| Role | In NICE? | Work Role Category | DCWF/OPM ID | NICE v2.0+ ID | Cybersecurity Framing |
|------|----------|-------------------|-------------|---------------|----------------------|
| System Administrator | Yes | Implementation & Operation | 451 | IO-WRL-005 | "Maintaining systems in adherence with organizational security policies and procedures" |
| Database Administrator | Yes | Implementation & Operation | 421 | IO-WRL-002 | "Secure storage, query, protection, and utilization of data" |
| Software Developer | Yes | Design & Development | 621 | DD-WRL-003 | Renamed "Secure Software Development" in v2.0+ |
| Network Operations Specialist | Yes | Implementation & Operation | 441 | IO-WRL-004 | Network security controls, firewalls, network segmentation |
| IT Project Manager | Yes | Oversight & Governance | 802 | OG-WRL-011 | Renamed "Secure Project Management" in v2.0+ |
| Data Analyst | Yes | Implementation & Operation | 422 | IO-WRL-001 | "Analyzing data to provide cybersecurity and privacy insight" |
| Privacy Officer | Yes | Oversight & Governance | 732 | OG-WRL-008 | Privacy compliance as a cybersecurity function |
| Risk Manager | Yes | Oversight & Governance | — | — | Demonstrated as extensible "new work role" in SP 800-181r1 Table 4 |
| Cyber Legal Advisor | Yes | Oversight & Governance | 731 | OG-WRL-006 | "Cybersecurity legal advice and recommendations" |
| Technical Writer | No | — | — | — | Tasks distributed across other roles |
| IT Support/Help Desk | Yes | Implementation & Operation | 411 | IO-WRL-007 | Initial incident reporting; endpoint security enforcement |
| Enterprise Architect | Yes | Design & Development | 651 | DD-WRL-002 | Security requirements in enterprise architecture |
| Executive Cyber Leadership | Yes | Oversight & Governance | 901 | OG-WRL-007 | Establishing vision for cybersecurity operations |

The **v2.0+ naming convention is revealing**. NICE renamed several boundary roles to make the cybersecurity nexus explicit: "Software Developer" became "Secure Software Development," "IT Project Manager" became "Secure Project Management," and role names shifted from nouns to verb phrases to avoid confusion with generic job titles. This signaling strategy — domain-qualifying the role name — is a practical technique ATLAS should adopt.

The **Implementation and Operation** category (formerly "Operate and Maintain") is almost entirely composed of boundary roles: 6 of its 7 work roles are general IT positions framed through cybersecurity. **Oversight and Governance** is second-most boundary-heavy, containing management, legal, privacy, and education roles that exist in many non-security contexts. By contrast, **Protection and Defense** and **Investigation** contain almost exclusively "pure" cybersecurity roles (incident response, digital forensics, vulnerability analysis).

---

## NICE's scope boundary language relies on risk management, not role purity

SP 800-181 Rev 1 never defines rigid inclusion/exclusion criteria. Instead, it uses three key design principles to establish scope.

**First, the risk-management test.** The framework defines its scope as "what an organization needs to achieve cybersecurity risk management objectives." Any work contributing to confidentiality, integrity, or availability falls within scope. This is deliberately broad — it pulls in system administrators (who implement access controls), developers (who write secure code), and project managers (who ensure security is built into project lifecycles).

**Second, the "work not people" principle.** SP 800-181r1 Section 3.4 states: "Work Role names are not synonymous with job titles. A single Work Role (e.g., Software Developer) may apply to those with many varying job titles. Conversely, multiple roles could be combined to create a particular job." The framework describes **work**, not people — a System Administrator may perform only some NICE-defined tasks, and that's by design.

**Third, the modularity attribute.** Section 1.1 states: "The NICE Framework enables organizations to communicate about other types of workforces within an enterprise and across organizations or sectors (e.g., privacy, risk management, software engineering/development)." This explicitly names adjacent domains as within scope.

The clearest articulation comes from NICE Director Rodney Petersen in the 2020 Rev 1 release: "The 'cybersecurity workforce' includes those whose primary focus is on cybersecurity **as well as those in the workforce who need specific cybersecurity-related knowledge and skills in order to perform their work** in a way that enables organizations to properly manage the cybersecurity-related risks to the enterprise."

The NSF's 2024 Cybersecurity Workforce Data Initiative report formalized this into a three-tier taxonomy that NICE itself lacks: **core** (primary work activity aligns with NICE), **involved** (cybersecurity is not primary but is significant), and **adjacent** (tasks are related but the worker isn't identified as core or involved). This taxonomy emerged precisely because NICE's own boundary language was too imprecise for labor market measurement.

---

## NICE coexists with other frameworks architecturally rather than by exclusion

NICE does not reference DAMA DMBOK, COBIT, ITIL, or TOGAF anywhere in SP 800-181r1 or its supplementary publications. Its official "Cybersecurity Skills and Workforce Frameworks" environmental scan lists 40+ related frameworks globally but includes none of these IT/data management standards. NICE's approach to overlap is **additive and architectural**: rather than saying "Database Administrator is handled by DAMA," it includes DBA but frames it through cybersecurity (secure storage, access controls, data protection). The same DBA can simultaneously be described by DAMA DMBOK for data management competencies and by NICE for security competencies — the frameworks operate at different conceptual levels.

**The one explicit scope transfer** occurred in v2.0 (2025): military-specific Cyberspace Effects and Cyberspace Intelligence categories (12 work roles) were removed from NICE and transferred to the DoD DCWF. This is the only documented case of NICE saying specific roles belong elsewhere.

A formal **NICE-to-O*NET crosswalk** exists, developed by Georgetown CSET in collaboration with the NICE Program Office (released January 2024). It maps cybersecurity-related O*NET-SOC codes to NICE Work Role Categories. The relationship is many-to-many: a single SOC code like 15-1212 ("Information Security Analysts") maps to multiple NICE Work Roles, and vice versa. The crosswalk developers note significant limitations: "O*NET codes do not directly correspond to the categories in the NICE framework, so some of the category correspondences are imperfect."

NICE also maps to **SFIA** (Skills Framework for the Information Age) for proficiency levels and to the **NIST Cybersecurity Framework** (CSF v2.0) via the OLIR program. CyberSeek identifies five categories of **"feeder roles"** — networking, software development, systems engineering, financial/risk analysis, and security intelligence/IT support — that serve as on-ramps to cybersecurity careers, representing a practical acknowledgment of adjacent roles.

---

## Six distinct strategies for handling boundary roles across frameworks

Analyzing DAMA DMBOK, UK DDaT, DoD DCWF, SFIA, e-CF, and IEEE SWECOM reveals six fundamentally different approaches to the boundary problem.

**Inclusion by reframing (DAMA DMBOK).** DAMA acknowledges that IT professionals like DBAs and system administrators perform data management work, but gives them a domain-specific identity: "Data Custodian." The custodian is explicitly defined as "responsible for the safe custody, transport, storage and technical management of data." This three-way model — data management roles (stewards), technical/IT roles reframed as custodians, and business roles (owners) — lets DAMA claim adjacent roles without pretending they are primarily data management positions. ATLAS could adopt this pattern: reframe Cloud Infrastructure Engineers as "Data Platform Custodians" rather than claiming they are data professionals.

**Maximum inclusion under one umbrella (UK DDaT).** The UK Government Digital and Data Profession Capability Framework covers 150+ roles across digital, data, and technology, including Software Developer, Business Analyst, Infrastructure Engineer, and Security Architect in the same framework. It organizes by function rather than domain purity. Role groups exist for navigation, not as boundaries. This works in the UK government context because the framework serves a single employer with unified workforce planning needs, but the sheer breadth can make it unwieldy for narrower purposes.

**Explicit expansion with designated categories (DoD DCWF).** The DCWF started with 54 cyber-focused work roles and expanded to 73 by formally adding new workforce elements: Software Engineering, AI/Data, and "Enablers" (legal, acquisition, training, leadership). DCWF is the most aggressively expansionist framework studied. It now covers ~175,000 DoD personnel. The **Enablers** element is particularly instructive — it provides a designated category for support/boundary roles that facilitate domain work without being technical practitioners. Positions can be coded with up to **3 work roles simultaneously**, allowing boundary roles to span elements.

**Explicit exclusion with named related disciplines (IEEE SWECOM).** The Software Engineering Competency Model explicitly names 7 disciplines that are related but excluded: Computer Engineering, Computer Science, General Management, Mathematics, Project Management, Quality Management, and Systems Engineering. This is the most boundary-clear approach but also the narrowest. ISO/IEC 27021 takes a similar approach, tightly scoping to ISMS professionals under ISO 27001.

**Boundary dissolution through skills-based composition (SFIA).** SFIA defines 140+ professional skills across 7 levels of responsibility and deliberately avoids defining roles, jobs, or organizational boundaries. Skills compose into any role an organization needs. The framework states: "The intention is not to draw a hard boundary around these skills." SFIA provides "views" that group skills for contexts like cybersecurity, AI, or data without creating hard barriers. This is elegant but requires organizations to do significant customization work.

**Pragmatic inclusion of non-unique competences (European e-CF).** The e-CF includes competences like Risk Management and Problem Management that "may be found in other professions but are very important in an ICT context," while explicitly excluding generic competences like Communications or General Management that are "comprehensively articulated in other structures." The selection rationale is explicitly described as "not a scientific choice, but a pragmatic process engaging a broad cross-section of stakeholders who prioritise competence inclusion based upon industry knowledge and experience."

---

## The documented costs of getting scope wrong

The literature identifies clear penalties for both overly narrow and overly broad frameworks. **CIPD research** states directly: "If a framework is too broad, it will fail to provide adequate guidance. If it is too detailed, the entire process becomes excessively bureaucratic and time-consuming and may lose credibility."

The NICE Framework itself illustrates the broad-scope problem. The **2023 GAO review** (GAO-23-105945) found that NICE focus group participants cited "challenges with the program, such as an unclear scope." More critically, the **NSF CWDI report** documented that "because of these limitations, some federal agencies do not reference the NICE Framework in their work, most notably major providers of nationally representative labor market and education data, including the Census Bureau, Bureau of Labor Statistics, Department of Labor's O*NET, and Department of Education." The framework's breadth made it untranslatable to traditional labor market measurement — a significant practical consequence.

On the narrow side, IEEE SWECOM's exclusion of project management and general management competencies limits its utility for organizations that need to staff complete software teams, not just individual contributors. ISO/IEC 27021's tight scoping to ISMS professionals makes it irrelevant for the majority of cybersecurity work that happens outside formal ISMS contexts.

Best practice guidance converges on several principles. **Restrict scope to measurable, relevant competencies** — CIPD recommends no more than 12 competencies per role. **Let purpose drive scope** — a framework for hiring decisions needs different boundaries than one for workforce planning. **Use layered scope** rather than binary in/out decisions. And critically, **plan for evolution** — both SFIA (3-year update cycles) and O*NET (continuous updates) demonstrate that frameworks must be regularly refreshed.

---

## Where the data profession ends remains contested

There is no academic or practitioner consensus on where "data professional" ends and "adjacent professional" begins. The **EU Data Market Monitoring Tool** provides perhaps the most useful formal definition: data professionals are "workers who collect, store, manage, and/or analyse, interpret, and visualise data as their primary or as a relevant part of their activity." The "primary or relevant part" language creates a two-tier inclusion model parallel to NICE's approach.

The boundary between data and IT is particularly porous. Database administrators sit squarely at this boundary — classified as IT professionals by most technology taxonomies but as core data infrastructure by DAMA DMBOK. Data engineers overlap significantly with software engineers; some companies use hybrid titles like "Data Software Engineer." The **EDISON Data Science Framework** (the most comprehensive existing data science workforce framework, developed at the University of Amsterdam) addresses this by building from competences upward to profiles rather than from job titles downward, using 5 core competence groups: Data Analytics, Data Management, Data Science Engineering, Research Methods, and Business Process Management.

Gartner's research signals convergence rather than clearer boundaries. Their prediction that "by 2028, the use of AI will result in 50% of all new employees having backgrounds other than STEM" suggests the data/AI workforce boundary is expanding, not contracting. The concept of **T-shaped professionals** — deep expertise in one discipline plus broad cross-disciplinary knowledge — further complicates neat categorization. A backend engineer with deep ML pipeline expertise is both a software engineer and a data professional simultaneously.

---

## ATLAS boundary roles parallel NICE's pattern precisely

For each candidate boundary role, the analysis below applies NICE's risk-management test adapted for data/AI: **does the role contribute to the organization's data and AI objectives, even if it is not primarily a data/AI role?**

**Database Administrator — Include as core.** The DBA is to data/AI what the System Administrator is to cybersecurity: a role that exists across all IT organizations but that is foundational to the domain's objectives. DAMA DMBOK already claims this role as "Data Custodian." DBAs implement data security, optimize query performance for analytics, manage data storage infrastructure, and enforce data governance policies. In a data organization, the DBA is not adjacent — they are infrastructure. ATLAS should include DBA with a domain-specific framing emphasizing data platform management, data quality at the storage layer, and governance enforcement.

**Cloud Infrastructure Engineer — Include with scoping notes.** Analogous to NICE's Network Operations Specialist. Cloud infrastructure engineers who manage data platforms (data lakes, warehouses, streaming infrastructure) perform data-specific work. ATLAS should include a "Data Platform Operations" work role that captures the data-relevant subset of cloud infrastructure work, following NICE's pattern of framing a general IT role through a domain lens.

**Software Engineer / Backend Engineer — Include with domain qualifier.** This parallels NICE's treatment of Software Developer, which was renamed "Secure Software Development" in v2.0+. Software engineers who build data pipelines, ML systems, or data products perform data/AI work. ATLAS should include a "Data Systems Development" or "AI Systems Development" work role. Not all software engineers belong in ATLAS — only those whose work directly serves data/AI objectives.

**IT Project Manager — Include with domain qualifier.** Direct parallel to NICE's "Secure Project Management" (OG-WRL-011). ATLAS should include "Data/AI Project Management" for project managers who manage data initiatives, ML deployments, or analytics programs. The NICE v2.0+ renaming pattern provides the template.

**Business Analyst — Include with scoping notes.** Business analysts who translate business requirements into data requirements, define data product specifications, or work on analytics use cases perform data-adjacent work. This is analogous to how NICE includes roles in its Oversight and Governance category. ATLAS should include a "Data Requirements Analysis" work role.

**Information Security Analyst — Include with scoping notes.** This is the mirror image of NICE including Data Analyst for "cybersecurity and privacy insight." Security analysts who focus on data security, data classification, data loss prevention, or AI security perform data-relevant work. ATLAS should include a "Data Security" work role, acknowledging overlap with NICE.

**Legal/Compliance Officer — Include with domain qualifier.** Direct parallel to NICE's "Cyber Legal Advisor" (OG-WRL-006). Data privacy law (GDPR, CCPA, AI Act) creates a specialized legal function. ATLAS should include "Data/AI Legal and Compliance" for practitioners focused on data regulations.

**Change Manager / Organizational Development — Include with scoping notes.** This has no direct NICE parallel but is analogous to NICE's inclusion of "Cyber Workforce Development and Management" (OG-WRL-005) and "Cybersecurity Curriculum Development" (OG-WRL-002). Data adoption and data literacy programs require change management. ATLAS should include a "Data Adoption and Literacy" work role.

**Technical Writer — Exclude as standalone; distribute tasks.** NICE's approach is instructive: no standalone Technical Writer work role exists, but technical writing tasks appear across multiple roles. ATLAS should follow this pattern. Data governance documentation, data dictionary maintenance, and AI model documentation are tasks assigned to other roles (Data Governance Manager, Data Architect, ML Engineer), not a separate work role.

**UX Designer — Include with scoping notes.** No direct NICE parallel, but this follows NICE's pattern of including roles where domain-specific design matters. UX designers who design data visualization interfaces, AI interaction patterns, or dashboard experiences perform data/AI-specific work. ATLAS should include a "Data/AI Experience Design" work role, acknowledging this is a specialized subset of UX.

---

## A recommended scope framework for ATLAS

Drawing on NICE's inclusive philosophy, the NSF CWDI tiering model, DAMA's reframing strategy, the e-CF's pragmatic inclusion principle, and the documented failure modes of both too-narrow and too-broad frameworks, the following scope framework is recommended.

**Boundary language for ATLAS.** The ATLAS framework describes work that contributes to an organization's data and AI objectives, including the collection, storage, management, governance, analysis, interpretation, visualization, and ethical use of data, and the design, development, deployment, and oversight of AI and machine learning systems. The framework encompasses practitioners whose primary function is data and AI work, as well as practitioners in adjacent roles who perform data/AI-relevant tasks as a significant component of their work. Work roles in ATLAS are not synonymous with job titles or occupations. A single work role may apply to practitioners with many different job titles, and a single job may span multiple ATLAS work roles.

**Three-tier inclusion model.** ATLAS should formally define three tiers:

- **Tier 1 — Core data/AI roles.** Roles where data/AI work is the primary function (>50% of work activities). Examples: Data Engineer, Data Scientist, ML Engineer, Data Architect, Data Governance Manager, Analytics Engineer, AI/ML Researcher. These roles receive full ATLAS work role definitions with comprehensive Task, Knowledge, and Skill statements.

- **Tier 2 — Adjacent roles with defined ATLAS equivalency.** Roles where data/AI work is a significant secondary function (roughly 20–50% of work activities). Examples: Database Administrator, Cloud Infrastructure Engineer (data platforms), Software Engineer (data systems), IT Project Manager (data projects), Business Analyst (data requirements), Information Security Analyst (data security), Legal/Compliance Officer (data regulations), UX Designer (data/AI interfaces), Change Manager (data adoption). These roles **retain their industry-standard titles exactly as defined by their native frameworks** — ATLAS does not redefine, rename, or claim ownership of them. Instead, ATLAS publishes a formal **equivalency mapping** that identifies which ATLAS work role categories and KSA clusters are activated when a practitioner in one of these roles is operating in a data and AI context. A DBA remains a DBA. When that DBA is managing a data warehouse, enforcing data classification policies, or supporting a data governance program, ATLAS can articulate the specific knowledge, skills, and tasks that apply — without asserting that the DBA belongs to the data profession rather than the IT profession. The equivalency relationship is additive, not substitutive. Organizations already using DAMA DMBOK, NICE, COBIT, or ITIL to describe these roles can layer ATLAS equivalencies on top without disrupting existing role definitions, job architectures, or workforce planning systems.

- **Tier 3 — Data/AI-enabled roles.** All other roles that require data/AI literacy competencies but do not perform data/AI work as a primary or significant secondary function. Examples: Marketing Manager (using analytics), HR Professional (using people analytics), Finance Analyst (using data tools). ATLAS defines competency areas for these roles (data literacy, AI literacy, data ethics awareness) but does not define full work role profiles.

**Five inclusion criteria.** A role belongs in ATLAS Tier 1 or Tier 2 if it meets at least one of these criteria, adapted from NICE's risk-management test and the e-CF's pragmatic inclusion principle:

1. **The role directly produces, transforms, or governs data or AI assets** as a primary or significant secondary function.
2. **The role's execution quality materially affects data quality, data availability, or AI system performance** — meaning poor execution creates data/AI risks analogous to how NICE frames cybersecurity risks.
3. **The role requires specialized data/AI knowledge** beyond general digital literacy — knowledge that a practitioner in the same role outside a data/AI context would not need.
4. **The role is commonly staffed within data and AI organizational units** — it appears in data teams, analytics teams, AI teams, or data governance functions, even if it also appears elsewhere.
5. **The role has a domain-specific variant** that is meaningfully different from its general form — a "Data Project Manager" faces challenges distinct from a generic IT Project Manager (data quality dependencies, model uncertainty, ethical review requirements).

**Three exclusion criteria.** A role should NOT be included in ATLAS if:

1. **Data/AI work represents less than ~20% of the role's typical activities** and the role has no domain-specific variant.
2. **The role's data/AI competencies are fully and adequately described by general digital literacy** — no specialized data/AI knowledge is needed beyond what any professional should have.
3. **The role is comprehensively articulated in another established framework** and including it in ATLAS would not add meaningful data/AI-specific insight beyond what that framework provides. (Following the e-CF principle of excluding competences "comprehensively articulated in other structures.")

**Naming convention.** Following NICE v2.0+'s strategy of renaming "Software Developer" to "Secure Software Development," ATLAS Tier 2 roles should use domain-qualified names that signal the data/AI lens: "Data Platform Operations" (not "Cloud Infrastructure Engineer"), "Data Systems Development" (not "Software Engineer"), "Data/AI Project Management" (not "IT Project Manager"). This prevents confusion between the general role and its ATLAS-specific profile.

**Cross-framework acknowledgment.** Unlike NICE, which does not reference DAMA DMBOK, COBIT, or ITIL, ATLAS should explicitly acknowledge overlap with related frameworks. Each Tier 2 role profile should include a "Related Frameworks" note identifying where the role also appears (e.g., "Database Administrator also appears in DAMA DMBOK as Data Custodian, in NICE Framework as IO-WRL-002, and in SFIA under Data Management skills"). This transparency helps organizations that use multiple frameworks and avoids the perception that ATLAS is overreaching.

**Evolution mechanism.** ATLAS should include a formal process for role addition, reclassification, and deprecation, with review cycles no longer than 3 years (following SFIA's model). The AI/data field is evolving faster than cybersecurity was when NICE launched — roles like Prompt Engineer, AI Safety Researcher, and Synthetic Data Engineer may need rapid inclusion. The DCWF's expansion from 54 to 73 work roles demonstrates that frameworks that plan for growth serve their communities better than those that try to be comprehensive from day one.

---

## Conclusion

The NICE Framework's most consequential design decision was choosing breadth over purity — including System Administrators, Software Developers, Database Administrators, and Project Managers alongside dedicated cybersecurity analysts and incident responders. This decision was grounded in a sound conceptual principle (cybersecurity risk management requires contributions from many non-specialist roles) but created real practical problems (unclear scope per GAO, untranslatable to labor market data per NSF CWDI, difficulty measuring framework adoption). ATLAS has the advantage of learning from NICE's 15-year evolution. The recommended three-tier model (core, adjacent, enabled) with explicit inclusion/exclusion criteria and domain-qualified naming provides the inclusive coverage that organizational design requires while maintaining the sharp boundaries that labor market measurement, educational curricula, and practitioner identity demand. The critical insight from across all frameworks studied is that **boundary management is not a one-time decision but an ongoing governance function** — ATLAS needs not just initial scope rules but a permanent mechanism for adjudicating what's in, what's out, and what has moved from adjacent to core as the field evolves.