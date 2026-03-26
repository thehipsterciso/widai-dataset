# ATLAS Documentation Index

**Version:** 0.4.0 (Development)  
**Last Updated:** 2026-03-26  
**Scope:** Chief Data and AI Officer (CDAIO) Domain Workforce Framework

---

## What Is ATLAS?

ATLAS is a unified workforce framework that maps 187+ roles across the CDAIO domain, unifying 15+ workforce frameworks (NICE, O*NET, SFIA, ESCO, DDaT, DAMA DMBOK, EU AI Act, ISO 42001, SR 11-7, and others) into a single JSON schema with full provenance tracking.

- **187 roles** across 10 functional categories (governance, engineering, data science, analytics, risk/ethics, operations, leadership, etc.)
- **322 independent KSAs** (Knowledge, Skills, Abilities) organized by category
- **15+ source frameworks** unified through deterministic role mappings
- **Full provenance tracking** for every field, framework, and relationship
- **Regulatory context** for EU AI Act, ISO 42001, SR 11-7, and sector-specific requirements

---

## Documentation Structure

### Core Architecture & Design

**[Master Schema Design](master-schema-design.md)** (45 KB, comprehensive)
- Complete unified JSON schema for 187-role dataset
- All fields across 15+ frameworks mapped to schema properties
- Design decisions and rationale
- Fully populated example (Database Administrator role)
- Cross-framework identifier systems and mapping strategies

**[Field-by-Field Assessment](field-by-field-assessment.md)** (54 KB, operational detail)
- Every schema field analyzed for use case value
- Assessment of which fields are load-bearing vs. optional
- Prioritization by strategic importance
- Field recommendations (keep, modify, consolidate)

**[NICE Boundary Scoping](nice-boundary-scoping.md)** (29 KB, framework boundaries)
- How NICE Framework handles adjacent/boundary roles
- Which roles ATLAS includes and why
- How ATLAS applies NICE's precedent for related roles
- Integration patterns for NICE-ATLAS role mapping

**[Gap Analysis](gap-analysis.md)** (42 KB, coverage assessment)
- Full inventory of 187 roles across 10 categories
- Coverage assessment against 15+ frameworks
- Identified gaps and priority areas
- Curation roadmap for remaining work

---

### Use Case & Market Discovery

**[Axis 3 & Axis 4 Discovery](axis3-axis4-discovery.md)** (85 KB, exhaustive enumeration) ← **START HERE FOR COMMERCIAL INSIGHT**
- **AXIS 3:** 50+ distinct outputs (deliverables, tools, data products) the framework produces
- **AXIS 4:** Organizational contexts (ownership, size, industry, maturity, regulatory, geography) where ATLAS creates value
- Non-obvious outputs identified (cost-of-vacancy analysis, regulatory mapping, CDAIO org charts, skill forecasting, network analysis)
- Highest-value buyer profiles and lowest-hanging-fruit contexts
- Strategic implications for go-to-market positioning

**[Axis 3 & Axis 4 Summary](axis3-axis4-summary.md)** (8 KB, executive brief)
- Executive summary of discovery findings
- Key findings on outputs and contexts
- Strategic implications for product and GTM
- Next steps for validation and refinement

---

## File Structure

```
atlas-dataset/
├── roles/                    One file per category (GOV.json, ENG.json, etc.)
├── ksas/                     Independent KSA entities by category
├── frameworks/               Reference data for 70 source frameworks
├── mappings/                 Relationship tables (role↔KSA, role↔framework)
├── career_tracks/            Career progression paths (future)
├── job_descriptions/         Per-role JD templates (future)
├── schema/                   JSON Schema definitions
├── docs/                     Documentation (you are here)
│   ├── master-schema-design.md        Complete unified schema + examples
│   ├── field-by-field-assessment.md   Every field evaluated
│   ├── nice-boundary-scoping.md       Framework boundary decisions
│   ├── gap-analysis.md                Coverage and priorities
│   ├── axis3-axis4-discovery.md       50+ outputs × 40+ contexts
│   ├── axis3-axis4-summary.md         Executive summary
│   └── README.md                      This file
├── scripts/                  Validation and build tooling
└── atlas_manifest.json       Index (no payload)
```

---

## Current State Metrics

| Metric | Count | Status |
|--------|-------|--------|
| **Roles** | 187 | Complete (v0.4.0) |
| **Categories** | 10 | Complete |
| **Independent KSAs** | 322 | Complete |
| **Role–KSA Relationships** | 322 | Complete |
| **Source Frameworks** | 70 | Complete |
| **Role–Framework Mappings** | 333 | Ongoing (new frameworks added regularly) |
| **Data Governance Maturity** | 5.0 | Validated schema, referential integrity checks |

---

## Validation

```bash
python3 scripts/validate.py
```

Checks performed:
- JSON structural integrity (all files valid JSON)
- Referential integrity (every ksa_id and role_id in mappings resolves)
- Duplicate detection (no duplicate roles, KSAs, or framework mappings)
- Manifest completeness (index matches actual files)

Validation runs automatically on GitHub push/PR via GitHub Actions.

---

## How to Use This Documentation

**If you are:**

- **A product strategist/founder:** Read Axis 3 & Axis 4 Summary → Axis 3 & Axis 4 Discovery
- **A platform architect:** Read Master Schema Design → Field-by-Field Assessment
- **A customer success/sales person:** Read Axis 3 & Axis 4 Summary → relevant case studies
- **A data engineer building integrations:** Read Master Schema Design → validate against sample data in roles/ and ksas/ directories
- **A researcher studying workforce frameworks:** Read NICE Boundary Scoping → Gap Analysis → Master Schema Design
- **An auditor/compliance person:** Read Field-by-Field Assessment → role-to-regulation mappings in Field-by-Field Assessment

---

## Key Insights

### The Schema Solves Three Hard Problems

1. **Fidelity across heterogeneous sources:** O*NET's statistical ratings, NICE's graph model, SFIA's level descriptors, DDaT's proficiency levels, ESCO's multilingual labels, and regulatory obligations (EU AI Act, ISO 42001, SR 11-7) are all preserved without loss of precision.

2. **Provenance transparency:** Every value carries source attribution, version, retrieval date, and confidence. This is essential for audit-ready compliance proof.

3. **Framework independence:** ATLAS does not force reconciliation between frameworks. When SFIA describes a role differently than NICE, both versions are recorded. The disagreement is analytically valuable.

### The Outputs Solve Real Business Problems

ATLAS doesn't deliver a single "role database." It delivers 50+ distinct outputs:

| Output | Buyer | Problem Solved |
|--------|-------|---|
| **Regulatory role-to-obligation mapping** | General Counsel, Chief Compliance Officer | "Who owns compliance with this regulation?" — proves it to auditors |
| **Cost-of-vacancy analysis** | CFO, hiring managers | Quantifies urgency; justifies $50K recruiting spend (costs $500K if unfilled) |
| **CDAIO org chart blueprint** | Boards, CDAO/CAIO/CISO | Only framework defining convergence structure; de-risks governance transition |
| **Compensation benchmarking** | HR, managers | "What should we pay a Data Architect?" — data-backed answer by geography/size |
| **Skill demand forecasting** | CDOs, boards | "What skills will be in-demand 2–3 years?" — forward-looking talent planning |

### The Contexts Determine Value

The same ATLAS dataset creates vastly different value depending on organizational context:

- **PE-backed portfolio company in regulated industry:** Existential value (integration planning, cost optimization, exit prep)
- **Mid-market established enterprise:** High value (governance, compliance, talent optimization)
- **Pre-data startup:** Low value; requires education first

This context-dependence means go-to-market strategy must diagnose context before positioning value prop.

---

## Scope & Boundary

### In Scope
- All roles and functions in the Chief Data and AI Officer organizational domain
- All roles required for data governance, data engineering, AI development, analytics, risk/ethics, operations, leadership
- Boundary roles that cross into data/AI (Database Administrator, Privacy Officer, Chief Information Security Officer where security overlaps AI governance)

### Out of Scope
- Cybersecurity workforce (covered by NIST NICE Cybersecurity Workforce Framework)
- Software engineering roles unrelated to data/AI (covered by standard tech job taxonomies)
- Domain-specific roles (radiologists, traders, researchers) that happen to use data/AI

### Boundary Methodology
Follows NIST NICE precedent: Include roles that are *essential to the domain* or *substantially modified by the domain*. A Database Administrator is included because databases are essential to all data functions. A radiologist who uses AI is not included because the radiologist role exists independently of AI.

---

## Version History

- **v0.4.0** (2026-03-26): Complete schema, use case discovery (Axis 3 & 4), gap analysis, field assessment
- **v0.3.0** (prior): Initial role inventory, 15-framework unification, master schema design
- **v0.2.0** (prior): NICE boundary scoping, initial framework mappings
- **v0.1.0** (prior): Proof of concept, 50-role pilot

---

## License

All content copyright © 2026 Thomas Jones. All rights reserved.

---

## Contact & Attribution

**Created by:** Thomas Jones  
**Background:** 20+ years in cybersecurity, data governance, and AI strategy; pursing Chief Data and AI Officer roles  
**Framework Perspective:** Differentiator is working both sides simultaneously — enterprise protection AND enterprise growth

**Research Methodology:**
- Unified 15+ workforce frameworks through deterministic role mappings
- Extracted and validated schema fields across all frameworks (40 O*NET tables, ESCO API, NICE CPRT, DCWF/DDaT/SFIA documentation, regulatory texts)
- Full provenance tracking enables audit-ready governance proof
- Schema validated with examples from production role data

---

## Next Steps

See Axis 3 & Axis 4 Summary for strategic next steps:
1. Refine buyer personas with PE operating partners and regulated enterprise CDOs
2. Prioritize MVP outputs for highest-value segments
3. Pilot go-to-market positioning and distribution
4. Secure data partnerships for forecasting and benchmarking
5. Validate regulatory mappings with domain experts

