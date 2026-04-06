# WIDAI — Workforce Initiative for Data and AI

**The first machine-readable, cross-framework workforce taxonomy built specifically for data and AI.**

[![Version](https://img.shields.io/badge/version-0.8.2-blue)](CHANGELOG.md) [![KSAs](https://img.shields.io/badge/KSAs-1%2C069-brightgreen)](ksas/) [![Domains](https://img.shields.io/badge/domains-12-brightgreen)](ksas/) [![Roles](https://img.shields.io/badge/roles-187-brightgreen)](roles/) [![Frameworks](https://img.shields.io/badge/frameworks-70-orange)](mappings/) [![Scored Pairs](https://img.shields.io/badge/scored%20pairs-2.76M-purple)](strm/)

---

## The Problem

The labor market has had O\*NET for forty years. Cybersecurity has had NICE for a decade. Data and AI — the function that boards are betting their competitive future on — has nothing. No shared language for its workforce. No standard for who these people are, what they should know, or how to measure the gap between where an organization is and where it needs to be.

Every organization defining "AI-ready" workforce requirements starts from scratch, often guided by vendor frameworks that serve commercial interests rather than operational truth. PE firms assess workforce risk without a common unit of measure. Regulators write obligations to roles that don't formally exist. CDOs build hiring plans from job postings rather than structured capability definitions.

WIDAI is the foundation that makes rigorous workforce analysis possible.

---

## What This Is

WIDAI is a structured, computationally validated knowledge base of **1,069 Knowledge, Skills, Abilities, and Tasks (KSAs)** across **12 professional domains**, mapped against **70 source frameworks** with full provenance — covering 187 defined roles in the data and AI function.

Every mapping is computationally scored and independently validated. Not expert opinion. Not manual classification. 536,737 rationale files across 2.76 million scored pairs, auditable from any KSA back to its source framework evidence.

---

## What This Makes Possible

| Use Case | What It Enables |
|---|---|
| **PE Workforce Due Diligence** | Composite Workforce Readiness Score, key-person risk identification, Year 1–3 workforce investment modeling in 30 days |
| **EU AI Act Compliance** | Enforcement begins August 2026 — maps regulatory obligations to the people who must fulfill them across EU AI Act, NIST AI RMF, and ISO 42001 |
| **AI Model Risk Governance** | SR 11-7 three lines of defense with defined roles and recommended staffing ratios |
| **CDAIO Week-1 Assessment** | Map current team, identify top three capability gaps, produce the remediation plan |

---

## Scale

| Framework | Elements | Scored Pairs | Mappings | Rationale Files |
|---|---|---|---|---|
| O\*NET 30.2 | 126 | 34,763 | 5,440 | 5,440 |
| NIST NICE v2.1.0 | 2,148 | 1,082,592 | 181,750 | 181,750 |
| DoD DCWF v5.1 | 2,945 | 1,484,280 | 288,101 | 288,101 |
| UK DDaT | 189 | 95,256 | 28,837 | 28,837 |
| EU AI Act | 62 | 31,248 | 13,481 | 13,481 |
| NIST AI RMF 1.0 | 70 | 35,280 | 19,128 | 19,128 |
| **Total** | **5,540** | **2,763,419** | **536,737** | **536,737** |

Phase 0 validation: 92.2% KSA coverage across 5 PE archetypes. AI-assisted authoring quality: 4.26/5. 19 frameworks cleared for commercial use.

---

## KSA Domain Coverage

| Domain | Code | Knowledge | Skills | Abilities | Tasks | Total |
|---|---|:-:|:-:|:-:|:-:|:-:|
| AI/ML Foundations | AI | 29 | 25 | 18 | 31 | **103** |
| AI Governance & Ethics | AG | 26 | 30 | 28 | 23 | **107** |
| Risk Management | RM | 20 | 28 | 24 | 29 | **101** |
| Data Architecture & Infrastructure | DA | 27 | 30 | 16 | 20 | **93** |
| Data Governance & Policy | DG | 27 | 29 | 13 | 23 | **92** |
| Leadership & Strategy | LS | 28 | 30 | 13 | 18 | **89** |
| Analytics & BI | AB | 26 | 25 | 16 | 21 | **88** |
| Technical Foundations | TF | 22 | 25 | 25 | 15 | **87** |
| Security & Privacy | SP | 19 | 26 | 15 | 24 | **84** |
| Data Quality & Management | DQ | 21 | 29 | 16 | 16 | **82** |
| Regulatory & Compliance | RC | 15 | 29 | 16 | 14 | **74** |
| Operations & Enablement | OP | 21 | 22 | 13 | 13 | **69** |
| **Grand Total** | | **281** | **328** | **197** | **247** | **1,069** |

---

## Role Coverage

187 roles across 10 functional categories:

| Category | Roles |
|---|:-:|
| Leadership | 31 |
| Engineering | 25 |
| Governance | 25 |
| Risk | 24 |
| Data Science & ML | 21 |
| Operations | 15 |
| Development | 15 |
| Analytics | 14 |
| Niche / Specialist | 9 |
| Regulatory | 8 |
| **Total** | **187** |

---

## The Enforcement Pipeline

Every KSA in this dataset was produced through a four-stage quality pipeline. No KSA is present without clearing all four gates.

```
dimension_synthesis.py
        │
        ▼
synthesis_enforcer.py        ← schema validation, STS threshold enforcement
        │
        ▼
Gap Analysis / Expansion     ← evidence-density check, cross-framework coverage
        │
        ▼
adversarial_validator.py     ← 8/8 independent checks must pass
```

The adversarial validator tests for: evidence density, internal consistency, redundancy, specificity, actionability, measurability, framework coverage breadth, and peer comparison. A KSA that passes is not "good enough." It is defensible under adversarial scrutiny — the bar required for regulatory and board-level workforce representations.

All 12 domains. All 48 dimension files. 8/8 checks passing.

---

## Repository Structure

```
widai-dataset/
├── ksas/               # 48 JSON files — 12 domains × 4 dimensions (K/S/A/T)
├── roles/              # 187 role definitions across 10 category files
├── mappings/           # 78 JSON files — 70 framework maps + 8 role-KSA maps
├── docs/               # Synthesis reports, technical documentation, ADRs
├── methodology/        # PE assessment workflow, scoring model, deliverable specs
├── frameworks/         # frameworks.json — all 70 source frameworks with metadata
├── sources/            # Raw source data: DCWF, DDaT, EU AI Act, NICE, NIST AI RMF, O*NET
├── strm/               # STRM pipeline artifacts — semantic similarity scores, gap detection
├── scripts/            # dimension_synthesis.py, synthesis_enforcer.py, adversarial_validator.py
├── schema/             # role_record.json — canonical record schema
├── career_tracks/
├── job_descriptions/
├── tests/
└── widai_manifest.json
```

**Start here:**
- KSA definitions → `ksas/[DOMAIN]_[dimension].json`
- Role definitions → `roles/[CATEGORY].json`
- Framework mappings → `mappings/`
- Quality methodology → `docs/` and `methodology/`
- Pipeline scripts → `scripts/`

---

## Framework Coverage

70 frameworks mapped. Six are computationally scored via the STRM pipeline with full semantic similarity scores and rationale files:

> O\*NET · NIST NICE · DoD DCWF · UK DDaT · EU AI Act · NIST AI RMF

The remaining 64 frameworks are mapped for coverage and provenance. Full list in [`frameworks/frameworks.json`](frameworks/frameworks.json).

**Selected frameworks:** 80000_HOURS · AICPA · AWS · BCG · BLS_SOC · CDMC · CMMI_DMM · COBIT_2019 · DAMA_DMBOK · DCAM · DELOITTE · EU_AI_ACT · EVIDENCE_ACT · FDA · FED_SR_11_7 · FORRESTER · GARTNER · GDPR · HBR · HIPAA · IAPP · IBM · IDC · IEEE · IIA · ISACA · ISO_23894 · ISO_27001 · ISO_27701 · ISO_38505 · ISO_42001 · ISO_8000 · KPMG · LINKEDIN · MCKINSEY · MICROSOFT · MIT_SLOAN · NIST_AI_RMF · NIST_NICE · O\*NET · OCC · STANFORD_HAI · TDWI · WEF · and 26 more.

---

## The Moat

No other dataset maps a single role to obligations under multiple regulatory and professional frameworks simultaneously. An AI Governance Manager in WIDAI carries context from EU AI Act Article 14, NIST AI RMF GOVERN functions, ISO 42001 controls, DAMA DMBOK knowledge areas, and SFIA skills — all in one record, all with source provenance, all computationally scored.

That cross-framework simultaneity — not any single framework's depth — is what makes WIDAI the foundation for regulatory compliance mapping, workforce due diligence, and AI governance staffing that isn't just defensible in principle but auditable in practice.

---

## Status

**Version 0.8.2** — all 12 domains complete, all KSAs validated.

**What exists:** 1,069 KSAs · 187 roles · 70 framework mappings · 2.76M scored pairs · 536,737 rationale files · full provenance chain from every KSA to source evidence.

**What does not exist yet:** Full role-KSA mappings at target depth · populated regulatory context fields · a pilot engagement partner · an API.

See [`CHANGELOG.md`](CHANGELOG.md) for full version history and [`docs/`](docs/) for roadmap and architecture decision records.

---

## Attribution & Licensing

See [`ATTRIBUTION.md`](ATTRIBUTION.md) for full source framework attribution. See [`CONTRIBUTING.md`](CONTRIBUTING.md) for contribution guidelines.

19 frameworks have been cleared for commercial use. Framework-specific licensing constraints apply to derived works — consult `ATTRIBUTION.md` before commercial deployment.

---

*WIDAI is an independent research initiative. It is not affiliated with, endorsed by, or derived from any vendor's commercial workforce product.*
