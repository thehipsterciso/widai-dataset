# Phase 1B: Framework Prioritization for STRM

**Date:** 2026-03-31
**Author:** Thomas Jones / The Hipster CISO
**Governs:** ADR-014 Phase 1C execution sequence
**KSA Pool Version:** 0.5.2 (497 KSAs, 12 domains)

## Assessment Criteria (per ADR-014)

Each of 70 source frameworks assessed against four criteria:

1. **KSA-Equivalent Concepts** — Does the framework define competencies, skills, knowledge areas, tasks, work activities, or similar construct types that can be mapped against WIDAI KSAs using STRM relationship types?
2. **Extractable Elements** — Does the framework provide machine-readable or manually extractable element data at sufficient granularity for per-element STRM mapping?
3. **WIDAI Coverage Breadth** — How many WIDAI roles reference this framework? (Proxy for domain coverage.)
4. **Strategic Use Case Relevance** — Does this framework directly serve WIDAI commercial use cases (PE Assessment, EU AI Act Compliance, Model Risk Governance, Agentic AI Workforce Design)?

## Classification Results

### Category A: STRM-Eligible (Defines KSA-Equivalent Concepts)

These frameworks contain concept types (competencies, skills, tasks, knowledge areas, work activities, capability definitions) that are directly mappable using STRM.

| Framework | Refs | License | Concept Types | Strategic Relevance |
|-----------|------|---------|---------------|---------------------|
| O*NET | 25 | GREEN | Knowledge, Skills, Abilities, Tasks, Work Activities, Work Context | PE Assessment (occupational benchmarking), all use cases |
| DAMA_DMBOK | 26 | RED | Competencies per knowledge area, activities, concepts | All data governance use cases |
| DCWF | 15 | GREEN | Work roles, competencies, tasks | PE Assessment, workforce design |
| NIST_NICE | 4 | GREEN | Knowledge, Skills, Abilities, Tasks (KSATs) | Workforce design, PE assessment |
| EU_AI_ACT | 10 | GREEN | Obligations, competency requirements (Art. 4 literacy), conformity requirements | EU AI Act Compliance (primary) |
| DDAT | 8 | GREEN | Skills, skill levels, role definitions | PE Assessment (UK context), workforce design |
| NIST_AI_RMF | 6 | GREEN | Functions, categories, subcategories with implied competencies | Model Risk Governance, AI governance |
| CDMC | 8 | YELLOW | Data management capabilities, maturity criteria | Data governance use cases |
| DCAM | 7 | YELLOW | Capability components, maturity criteria | PE Assessment (data maturity) |
| ISO_42001 | 8 | RED | AI management system requirements, competence requirements (Clause 7.2) | EU AI Act Compliance, AI governance |
| Data_Mesh | 10 | GREEN | Domain ownership capabilities, data product competencies | Architecture and organizational design |
| FED_SR_11_7 | 4 | GREEN | Model risk management expectations, effective challenge competencies | Model Risk Governance (primary) |
| CMMI_DMM | 6 | RED | Process areas, capability levels, specific practices | Data governance maturity |
| GDPR | 2 | GREEN | DPO competence requirements (Art. 37.5), organizational obligations | Regulatory compliance |
| IAPP | 6 | YELLOW | DPO competency framework, privacy professional skills | Regulatory compliance, privacy roles |
| BLS_SOC | 3 | GREEN | Occupational tasks, detailed work activities | PE Assessment (labor market) |
| ISACA | 3 | RED | AAIR certification domains, COBIT competencies | AI governance, audit |
| FDA | 2 | GREEN | Regulatory competency expectations for data integrity | Regulated industry compliance |
| OCC | 1 | GREEN | Model risk supervisory expectations | Model Risk Governance |
| HIPAA | 1 | GREEN | Security rule competency requirements | Regulated industry compliance |
| Evidence_Act | 3 | GREEN | Evidence-based decision-making competencies | Federal data strategy |
| Executive_Order | 2 | GREEN | AI workforce competency directives | Federal AI workforce |
| Singapore_MAIG | 1 | GREEN | Model AI governance implementation competencies | AI governance (APAC) |
| DBT_Labs | 1 | GREEN | Analytics engineering role definitions, skill expectations | Analytics engineering |
| AICPA | 1 | YELLOW | AI competency framework, trust services criteria | Audit, AI assurance |
| IEEE | 4 | RED | AI ethics standards, systems engineering competencies | AI governance standards |
| IIA | 3 | YELLOW | Internal audit competency framework for AI/data | Audit, governance |
| COBIT_2019 | 1 | RED | Governance and management objectives, enabler competencies | IT governance |
| EC_Council | 1 | YELLOW | Cybersecurity certification competencies | Security roles |
| ISO_27001 | 1 | RED | Information security competence requirements | Security governance |
| ISO_27701 | 1 | RED | Privacy information management competence requirements | Privacy governance |
| ISO_23894 | 1 | RED | AI risk management competencies | AI risk management |
| ISO_5338 | 1 | RED | AI lifecycle process competencies | AI engineering |
| ISO_38505 | 1 | RED | Data governance competence requirements | Data governance |
| ISO_8000 | 3 | RED | Data quality competencies | Data quality |

**Total Category A: 34 frameworks**

### Category B: NOT STRM-Eligible (No KSA-Equivalent Concepts)

These frameworks are job posting aggregators, consultancy research, publications, vendor documentation, or community references. They describe the market or cite practices but do not define formal competency constructs mappable via STRM.

| Framework | Refs | Reason for Exclusion |
|-----------|------|---------------------|
| PRACTITIONER_COMMUNITY | 47 | Aggregate community practices, not a documentary standard |
| LINKEDIN | 15 | Job posting aggregator — describes market demand, not competencies |
| GARTNER | 14 | Analyst research — describes market, not competencies |
| DELOITTE | 7 | Consultancy research |
| CDO_MAGAZINE | 6 | Industry publication |
| MCKINSEY | 6 | Consultancy research |
| INDEED | 4 | Job posting aggregator |
| AWS | 4 | Vendor certification/documentation — describes product skills, not workforce competencies |
| WIDAI | 4 | Self-reference |
| BCG | 3 | Consultancy research (paywalled) |
| FORRESTER | 3 | Analyst research |
| MIT_SLOAN | 3 | Academic publication |
| MONTE_CARLO_DATA | 3 | Vendor-specific tooling documentation |
| ODSC | 3 | Conference/community |
| SCALE_AI | 3 | Vendor research |
| TDWI | 3 | Publication/training organization |
| AIJOBS.NET | 2 | Job posting aggregator |
| DQOPS | 2 | Tool vendor documentation |
| HBR | 2 | Publication |
| IBM | 2 | Vendor documentation |
| MICROSOFT | 2 | Vendor documentation |
| STANFORD_HAI | 2 | Academic research |
| 80000_HOURS | 1 | Career advice/research organization |
| CONVERSATION_DESIGN_INSTITUTE | 1 | Training organization |
| COURSERA | 1 | Training platform |
| DATAOPS.LIVE | 1 | Tool vendor |
| DATAVERSITY | 1 | Publication |
| DZONE | 1 | Publication |
| GITLAB | 1 | Vendor documentation |
| GLASSDOOR | 1 | Job posting aggregator |
| IDC | 1 | Analyst research |
| KPMG | 1 | Consultancy research |
| THOUGHTWORKS | 1 | Technology consultancy |
| VELLUM | 1 | AI tool vendor |
| WEF | 1 | Forum/publication |

**Total Category B: 35 frameworks (plus WIDAI self-reference = 36)**

### Note on Category B

Category B frameworks are not wasted — they informed the original role definitions and will continue to serve as market validation signals. They are excluded from STRM because STRM requires a documentary standard with enumerable concept elements. "Data engineers should know Spark" from a LinkedIn job posting is market signal, not a mappable competency definition.

## Prioritized STRM Execution Sequence

From the 34 eligible frameworks, execution priority is determined by strategic use case alignment, license accessibility, and coverage breadth. Frameworks are grouped into tiers; within each tier, execution order is fixed.

### Tier 1 — Foundational (Execute First)

These frameworks define competencies directly, have GREEN licenses, and anchor the most WIDAI use cases. They establish the STRM methodology rhythm and produce the highest-value gap identification.

| Priority | Framework | Rationale |
|----------|-----------|-----------|
| 1 | **O*NET** | Largest competency database in existence. 25 WIDAI role refs. Directly defines K, S, A, T, Work Activities. GREEN license. Anchors PE Assessment use case via occupational benchmarking. |
| 2 | **NIST NICE** | The model WIDAI emulates for KSA structure. 4 refs but comprehensive cyber-adjacent competencies. GREEN license. Validates the KSA taxonomy design itself. |
| 3 | **DCWF** | US federal data/AI workforce competency framework. 15 refs. GREEN license. Direct competitor/complement to WIDAI scope. |
| 4 | **DDAT** | UK equivalent to DCWF. 8 refs. GREEN license. International validation and gap identification. |

### Tier 2 — Strategic (Execute Next)

These frameworks directly serve WIDAI commercial use cases. They are either regulatory requirements or industry-standard capability models.

| Priority | Framework | Rationale |
|----------|-----------|-----------|
| 5 | **EU_AI_ACT** | Primary regulatory driver. 10 refs. GREEN license. August 2026 high-risk deadline. Anchors EU AI Act Compliance use case. |
| 6 | **NIST_AI_RMF** | AI risk management standard. 6 refs. GREEN license. Cross-reference with EU AI Act for compliance mapping. |
| 7 | **FED_SR_11_7** | Model risk management regulatory expectation. 4 refs. GREEN license. Anchors Model Risk Governance use case. |
| 8 | **GDPR** | Data protection competency requirements. 2 refs. GREEN license. Foundation for all privacy/compliance roles. |
| 9 | **DAMA_DMBOK** | Dominant data management competency framework. 26 refs. RED license limits redistribution but mapping is research/analysis. Essential for data governance coverage validation. |

### Tier 3 — Deepening (Execute After Tier 2)

Capability maturity models, international standards, and professional association frameworks that deepen specific domain coverage.

| Priority | Framework | Rationale |
|----------|-----------|-----------|
| 10 | **ISO_42001** | AI management system standard. 8 refs. RED license. Cross-validates EU AI Act competency interpretation. |
| 11 | **DCAM** | Data management capability model. 7 refs. YELLOW license. PE Assessment data maturity use case. |
| 12 | **CDMC** | Chief Data Management Council capabilities. 8 refs. YELLOW license. |
| 13 | **Data_Mesh** | Organizational/architectural capabilities. 10 refs. GREEN license. |
| 14 | **CMMI_DMM** | Data management maturity. 6 refs. RED license. |
| 15 | **IAPP** | Privacy professional competencies. 6 refs. YELLOW license. |
| 16 | **BLS_SOC** | Occupational task data. 3 refs. GREEN license. |

### Tier 4 — Specialized (Execute as Needed)

Sector-specific, jurisdictional, or narrow-scope frameworks that address specific gaps identified during Tier 1–3 execution.

| Priority | Framework | Rationale |
|----------|-----------|-----------|
| 17–19 | FDA, HIPAA, OCC | Sector-specific regulatory requirements |
| 20–21 | Evidence_Act, Executive_Order | US federal workforce directives |
| 22 | Singapore_MAIG | APAC AI governance |
| 23–28 | ISO series (23894, 5338, 38505, 8000, 27001, 27701) | International standards (RED license — citation analysis) |
| 29–34 | ISACA, AICPA, IIA, IEEE, COBIT, EC_Council, DBT_Labs | Professional association / vendor frameworks |

### Execution Constraint

Per ADR-014: "The prioritized list is not revised once STRM execution begins — it is executed in order." Tier 4 frameworks may be deferred if Tier 1–3 STRMs produce sufficient pool coverage (measured by gap density declining below threshold across consecutive frameworks).

## License Considerations for RED Frameworks

Nine STRM-eligible frameworks have RED licenses (ISO standards, DAMA_DMBOK, CMMI_DMM, ISACA, IEEE, COBIT). STRM mapping constitutes analytical research — the mapping data references framework element IDs and descriptions for the purpose of relationship analysis, not redistribution of the framework content. The STRM deliverable documents the analytical relationship, not the source content itself.

For RED-license frameworks:
- Canonical source acquisition stores a version-pinned citation with access date, not the document itself
- STRM data includes FDE IDs and minimal descriptive text necessary for the mapping relationship
- Full framework text is not reproduced in the STRM deliverable
- This approach aligns with SCF practice for proprietary framework STRM (e.g., SCF maps against NIST CSF, ISO 27001, SOC 2 without redistributing those standards)

## Summary Statistics

- **Total source frameworks:** 70
- **STRM-eligible:** 34 (49%)
- **Not eligible:** 36 (51%)
- **GREEN license eligible:** 16 frameworks
- **YELLOW license eligible:** 8 frameworks
- **RED license eligible:** 10 frameworks
- **Tier 1 (foundational):** 4 frameworks
- **Tier 2 (strategic):** 5 frameworks
- **Tier 3 (deepening):** 7 frameworks
- **Tier 4 (specialized):** 18 frameworks
