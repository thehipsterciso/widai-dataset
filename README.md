# ATLAS Dataset

**A Workforce Framework for Talent, Leadership, and Skills in Data and AI**

ATLAS defines the roles, knowledge, skills, and abilities (KSAs) that constitute the Chief Data and AI Officer (CDAIO) organizational domain. It unifies 15+ workforce frameworks — NIST NICE, O\*NET, SFIA, DAMA DMBOK, DCWF, DDaT, ESCO, EU AI Act, ISO 42001, SR 11-7, LinkedIn, IAPP, ISACA, and others — into a single, version-controlled dataset with full source provenance.

## Current state

| Metric | Count |
|--------|-------|
| Roles | 187 |
| Categories | 10 |
| Independent KSAs | 322 |
| Role–KSA relationships | 322 |
| Source frameworks | 70 |
| Role–framework mappings | 333 |

**Version:** 0.4.0 (development)

## Architecture

The dataset uses entity-separated flat files with foreign key references. `role_id` is the primary key for roles. `ksa_id` is the primary key for KSAs. Relationship tables in `/mappings/` connect them.

```
atlas-dataset/
  roles/              One file per category_code (GOV.json, ENG.json, ...)
  ksas/               Independent KSA entities by category
  frameworks/         Reference data for each source framework
  mappings/           Relationship tables (role↔KSA, role↔framework)
  career_tracks/      Career progression paths (future)
  job_descriptions/   Per-role JD templates (future)
  schema/             JSON Schema definitions
  docs/               Architecture decisions and research
  scripts/            Validation and build tooling
  atlas_manifest.json Index of everything — no payload
```

### Why this structure

KSAs are independent entities, not role properties. A single KSA can belong to multiple roles. Two frameworks can describe the same KSA differently. The relationship tables capture all of this without duplicating the KSA itself.

This follows the patterns established by NICE (Tasks own KSAs, roles reference Tasks) and SFIA (skills exist independently, roles are assembled from skills). The disagreement between frameworks about how to describe a competency is analytically valuable — we record it rather than reconciling it.

Each directory represents a node type. Each mapping file represents an edge type. The structure loads directly into Neo4j or any graph database without transformation.

### Categories

| Code | Title | Roles |
|------|-------|-------|
| GOV | Governance, Strategy, and Executive Leadership | 25 |
| ENG | Engineering, Architecture, and Platform | 25 |
| DEV | Data Science, ML, and AI Development | 15 |
| DSM | Data Stewardship and Master Data | 21 |
| ANL | Analytics and Business Intelligence | 14 |
| RSK | Risk, Ethics, Safety, Compliance, and Audit | 24 |
| OPS | Operations, Monitoring, and Reliability | 15 |
| LDR | Leadership and Management (VP/Director) | 31 |
| REG | Regulatory and Standards Compliance | 8 |
| NICHE | Niche and Emerging Specializations | 9 |

## Validation

```bash
python3 scripts/validate.py
```

Checks JSON integrity, referential integrity (every ksa_id and role_id in mapping files resolves), duplicate detection, and manifest completeness. Runs automatically on push/PR via GitHub Actions.

## Scope

Covers the full data and AI profession. Explicitly excludes the CISO and cybersecurity workforce, which is covered by NIST NICE. Boundary roles (Database Administrator, Privacy Officer, etc.) are included with domain-qualified framing, following the NICE precedent for adjacent roles.

## Documentation

- [Master Schema Design](docs/master-schema-design.md) — unified JSON schema for cross-framework role records
- [Field-by-Field Assessment](docs/field-by-field-assessment.md) — use case analysis for every schema field
- [Gap Analysis](docs/gap-analysis.md) — 187-role inventory and coverage assessment
- [NICE Boundary Scoping](docs/nice-boundary-scoping.md) — how NICE handles adjacent roles and what it means for ATLAS

## License

Copyright 2026 Thomas Jones. All rights reserved.
