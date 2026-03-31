# ADR-015: STRM — O*NET Database 30.2

**Status:** Accepted
**Date:** 2026-03-31
**Author:** Thomas Jones / The Hipster CISO
**STRM ID:** STRM-001-ONET
**Priority:** 1 (Tier 1 — Foundational)
**Governed by:** ADR-014 (STRM-Based KSA Enrichment Methodology)

## Framework Selection Rationale

O*NET is the first framework in the STRM execution sequence for three reasons:

1. **Largest competency database in existence.** 923 occupations, 169 leaf-level content model elements across Knowledge, Skills, Abilities, and Work Activities. This provides the broadest possible baseline validation of ATLAS coverage.
2. **Highest ATLAS role reference count.** 25 of 187 ATLAS roles reference O*NET — more than any other framework.
3. **Methodology establishment.** As the first STRM, O*NET sets the quality standard and operational rhythm for all subsequent framework STRMs.

## Use Case Summary

**Target audience:** ATLAS framework developers, PE assessment practitioners, and data/AI workforce planners who need to understand how ATLAS KSAs relate to the U.S. government's occupational competency taxonomy.

**Rationale type:** Semantic (primary), Functional (secondary). O*NET uses occupation-general language; ATLAS uses domain-specific language. Semantic rationale evaluates whether differently-worded concepts describe the same competency. Functional rationale used for cognitive abilities and work activities where behavioral outcomes matter more than vocabulary.

**Scope:** 126 of 169 O*NET leaf-level elements evaluated. 43 elements excluded (Psychomotor Abilities, Physical Abilities, Sensory Abilities, Physical Work Activities) — irrelevant to data/AI knowledge work.

## Summary Statistics

| Metric | Value |
|--------|-------|
| Total FDEs in scope | 126 |
| Intersects with | 82 (65.1%) |
| No relationship | 23 (18.3%) |
| Superset of | 17 (13.5%) |
| Equal | 4 (3.2%) |
| Subset of | 0 (0.0%) |
| Mean strength (where applicable) | 5.2 / 10 |
| Gap signals | 6 thematic clusters |

## Key Findings

### 1. ATLAS Domain Coverage is Technically Comprehensive

103 of 126 in-scope O*NET elements have documented relationships with ATLAS KSAs. The gap signals cluster around foundational professional skills, not domain-specific technical gaps. This validates the v0.5.2 domain pool expansion: the baseline KSA enrichment (Phase 1A) successfully addressed the critical depth deficiency for core data/AI competencies.

### 2. Relationship Pattern is Analytically Coherent

The dominance of "Intersects with" (65%) correctly reflects the structural relationship between a general-purpose occupational taxonomy (O*NET) and a domain-specific professional framework (ATLAS). O*NET defines competencies at occupation-general breadth; ATLAS defines them at data/AI-specific depth. The intersection captures this accurately.

Zero "Subset of" relationships is expected and correct: no individual ATLAS KSA is broader than an O*NET content model element, because ATLAS KSAs are domain-scoped while O*NET elements are occupation-general.

### 3. Four Equal Relationships Confirm Core Coverage

O*NET Work Activities that map as "Equal" to ATLAS KSAs:

- **Analyzing Data or Information** ↔ AB-T-001 (Strength: 8)
- **Developing Objectives and Strategies** ↔ LS-S-001 (Strength: 8)
- **Developing and Building Teams** ↔ LS-S-004 (Strength: 8)
- **Coaching and Developing Others** ↔ LS-S-007 (Strength: 9)

These confirm that ATLAS covers the most relevant O*NET work activities at equivalent or greater depth.

### 4. Gap Signals Are Structural, Not Domain-Specific

Six gap clusters identified, all in foundational professional skills rather than data/AI domain knowledge:

| Gap | Severity | Theme |
|-----|----------|-------|
| ONET-GAP-001 | Moderate | Foundational communication skills |
| ONET-GAP-002 | Moderate | Continuous professional development |
| ONET-GAP-003 | Low | Service orientation |
| ONET-GAP-004 | Moderate | Project/time management |
| ONET-GAP-005 | Low | Conflict resolution |
| ONET-GAP-006 | Low | Ethical reasoning foundations |

These gaps reflect a design decision, not an oversight: ATLAS v0.5.2 prioritized domain-specific competencies over foundational professional skills. Whether foundational skills belong in ATLAS is a synthesis-phase question — it depends on whether other frameworks (particularly DCWF, DDAT, NICE) define them for data/AI roles and whether ATLAS's target audience expects them.

### 5. No ATLAS Domain is Systematically Underrepresented

The O*NET mapping produced intersections across all 12 ATLAS domains. No domain was absent from the mapping results. This confirms the domain taxonomy design (ADR-013) provides comprehensive coverage of O*NET's occupation-relevant concept space.

## Anomalies

None identified. The mapping results are consistent with the analytical expectations documented in the use case.

## QA/QC Result

**PASS.** All 126 FDEs evaluated with documented rationale. Relationship types and strength scores are analytically coherent. Gap issues are complete with synthesis recommendations. See `strm/onet/qa_qc_report.json` for full QA/QC details.

## Deliverables

| # | Deliverable | Location |
|---|-------------|----------|
| 1 | Canonical source citation | `sources/onet_30_2_citation.json` |
| 1a | Raw database (working copy) | `sources/onet_30_2/db_30_2_text/` |
| 2 | Use case document | `strm/onet/use_case.json` |
| 3 | STRM mapping data | `strm/onet/strm_mapping.json` |
| 4 | Per-FDE rationale | Embedded in mapping notes (126 FDEs) |
| 5 | Gap issue register | `strm/issues/STRM-001-ONET-gaps.json` |
| 6 | This ADR | `docs/roadmap/adr/ADR-015-strm-onet.md` |
| 7 | QA/QC report | `strm/onet/qa_qc_report.json` |

## Note on Per-FDE Rationale Files

ADR-014 specifies per-FDE rationale as independent file objects. For STRM-001-ONET, rationale is embedded in the `notes` field of each mapping entry in `strm_mapping.json`. This is a pragmatic decision for the first STRM: 126 individual rationale files would add significant file management overhead without improving the analytical record, because the `notes` field provides the same information (triggering FDE, domains searched, nearest miss, secondary matches, gap signals) in a more navigable structure. If subsequent STRMs have more complex rationale requirements, independent files will be used.

## References

- O*NET Database 30.2 (February 2026), National Center for O*NET Development, CC BY 4.0
- NIST IR 8477: Mapping Relationships Between Documentary Standards, Regulations, Frameworks, and Guidelines
- ADR-014: STRM-Based KSA Enrichment Methodology
- Phase 1B Framework Prioritization (`docs/roadmap/phase-1b-framework-prioritization.md`)
