# ADR-015: STRM — O*NET Database 30.2

**Status:** Accepted
**Date:** 2026-03-31
**Author:** Thomas Jones / The Hipster CISO
**STRM ID:** STRM-001-ONET
**Priority:** 1 (Tier 1 — Foundational)
**Governed by:** ADR-014 (STRM-Based KSA Enrichment Methodology)

## Framework Selection Rationale

O*NET is the first framework in the STRM execution sequence for three reasons:

1. **Largest competency database in existence.** 923 occupations, 169 leaf-level content model elements across Knowledge, Skills, Abilities, and Work Activities. This provides the broadest possible baseline validation of WIDAI coverage.
2. **Highest WIDAI role reference count.** 25 of 187 WIDAI roles reference O*NET — more than any other framework.
3. **Methodology establishment.** As the first STRM, O*NET sets the quality standard and operational rhythm for all subsequent framework STRMs.

## Use Case Summary

**Target audience:** WIDAI framework developers, PE assessment practitioners, and data/AI workforce planners who need to understand how WIDAI KSAs relate to the U.S. government's occupational competency taxonomy.

**Rationale type:** Semantic (primary), Functional (secondary). O*NET uses occupation-general language; WIDAI uses domain-specific language. Semantic rationale evaluates whether differently-worded concepts describe the same competency. Functional rationale used for cognitive abilities and work activities where behavioral outcomes matter more than vocabulary.

**Scope:** 126 of 169 O*NET leaf-level elements evaluated. 43 elements excluded (Psychomotor Abilities, Physical Abilities, Sensory Abilities, Physical Work Activities) — irrelevant to data/AI knowledge work.

## Scoring Methodology

Strength of relationship scores are computed using a multi-method computational scoring pipeline. The primary scoring method is Cross-Encoder Semantic Textual Similarity (STS), the industry-standard approach for pairwise sentence-level concept comparison. Four secondary methods provide audit trail evidence and future analytical flexibility.

### Primary Method: Cross-Encoder STS

| Attribute | Value |
|-----------|-------|
| Model | `cross-encoder/stsb-roberta-base` |
| Training data | STS-Benchmark (human-annotated sentence similarity, 0–5 scale) |
| Mechanism | Both text descriptions fed jointly through a single transformer; cross-attention captures inter-text relationships. Outputs a calibrated 0–1 similarity score. |
| Score mapping | Raw score (0–1) × 10, rounded to nearest integer = `strength_of_relationship` (0–10) |

Cross-encoders are the highest-accuracy method available for scoring known sentence pairs (Reimers & Gurevych, 2019). Unlike bi-encoders, which encode each text independently, cross-encoders process both texts simultaneously — enabling the model to capture cross-abstraction semantic relationships that independent encoding structurally misses.

### Secondary Methods

Four additional methods are computed for every scored pair and documented in each per-FDE rationale file. These provide audit evidence, cross-validation signals, and future analytical flexibility.

| Method | Model | What It Measures | Role |
|--------|-------|-----------------|------|
| BERTScore | `roberta-large` | Token-level contextual embedding matching. Produces Precision (FDE coverage of KSA tokens), Recall (KSA coverage by FDE tokens), and F1 (harmonic mean). | Audit trail — shows which tokens matched and how well. P/R directionality validates relationship type assignments. |
| NLI Cross-Encoder | `cross-encoder/nli-deberta-v3-base` | Natural Language Inference classification: entailment, neutral, contradiction probabilities. | Directional implication signal — indicates whether one description logically entails the other. |
| Bi-Encoder Cosine | `all-MiniLM-L6-v2` | Independent sentence embeddings with cosine similarity. | Baseline comparison — fast, scalable, but lower accuracy than cross-encoder for cross-domain pairs. |
| Jaccard Token | N/A (lexical) | Set intersection / union of lowercased word tokens. | Hand-traceable lexical baseline — fully reproducible without any ML dependencies. |

### NIST Alignment (IR 8278Ar1 §3.2.12)

The NIST OLIR specification defines strength as an integer 0–10 with no prescribed methodology. The STS cross-encoder's 0–1 output maps linearly to this scale. The resulting scores align with the NIST descriptive bands:

- 10: Equal relationship
- 7–9: Much more similar than dissimilar
- 4–6: Roughly as similar as dissimilar
- 1–3: Much more dissimilar than similar
- 0: Not related

### Reproducibility

The scoring pipeline (`strm/onet/strm_scoring_pipeline.py`) produces identical results for identical inputs. All models are deterministic for pinned versions. Each per-FDE rationale file contains the complete audit trail: primary STS raw score and mapped strength, plus all four secondary method outputs with model identifiers and descriptions.

## Summary Statistics

| Metric | Value |
|--------|-------|
| Total FDEs in scope | 126 |
| Intersects with | 82 (65.1%) |
| No relationship | 23 (18.3%) |
| Superset of | 17 (13.5%) |
| Equal | 4 (3.2%) |
| Subset of | 0 (0.0%) |
| Computed mean strength (where applicable) | 4.18 / 10 |
| Gap signals | 6 thematic clusters |

### By Relationship Type

| Type | Count | Mean Strength (STS) | Range |
|------|-------|---------------------|-------|
| Equal | 4 | 4.60 | 3.6 – 6.3 |
| Superset of | 17 | 4.15 | 2.3 – 5.9 |
| Intersects with | 82 | 4.16 | 0.7 – 6.9 |
| No relationship | 23 | 0 | N/A |

## Key Findings

### 1. WIDAI Domain Coverage is Technically Comprehensive

103 of 126 in-scope O*NET elements have documented relationships with WIDAI KSAs. The gap signals cluster around foundational professional skills, not domain-specific technical gaps. This validates the v0.5.2 domain pool expansion: the baseline KSA enrichment (Phase 1A) successfully addressed the critical depth deficiency for core data/AI competencies.

### 2. Relationship Pattern is Analytically Coherent

The dominance of "Intersects with" (65%) correctly reflects the structural relationship between a general-purpose occupational taxonomy (O*NET) and a domain-specific professional framework (WIDAI). O*NET defines competencies at occupation-general breadth; WIDAI defines them at data/AI-specific depth. The intersection captures this accurately.

Zero "Subset of" relationships is expected and correct: no individual WIDAI KSA is broader than an O*NET content model element, because WIDAI KSAs are domain-scoped while O*NET elements are occupation-general.

### 3. Cross-Abstraction Scoring Validates Methodology

The multi-method scoring pipeline addresses the fundamental challenge of comparing a general occupational taxonomy to a domain-specific professional framework. Cross-encoder STS processes both descriptions jointly through cross-attention, enabling it to capture semantic relationships that independent encoding methods (bi-encoders, lexical overlap) systematically underestimate for cross-abstraction pairs. The secondary methods (BERTScore, NLI, bi-encoder cosine, Jaccard) provide independent audit evidence for every scored pair, enabling future recalibration or methodology refinement without re-running the primary analysis.

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

These gaps reflect a design decision, not an oversight: WIDAI v0.5.2 prioritized domain-specific competencies over foundational professional skills. Whether foundational skills belong in WIDAI is a synthesis-phase question — it depends on whether other frameworks (particularly DCWF, DDAT, NICE) define them for data/AI roles and whether WIDAI's target audience expects them.

### 5. No WIDAI Domain is Systematically Underrepresented

The O*NET mapping produced intersections across all 12 WIDAI domains. No domain was absent from the mapping results. This confirms the domain taxonomy design (ADR-013) provides comprehensive coverage of O*NET's occupation-relevant concept space.

## Anomalies

None identified. The mapping results are consistent with the analytical expectations documented in the use case.

## QA/QC Result

**PASS.** All 126 FDEs evaluated with documented rationale. Relationship types and strength scores are computationally derived with full audit trails. Gap issues are complete with synthesis recommendations. See `strm/onet/qa_qc_report.json` for full QA/QC details.

## Deliverables

| # | Deliverable | Location |
|---|-------------|----------|
| 1 | Canonical source citation | `sources/onet_30_2_citation.json` |
| 1a | Raw database (working copy) | `sources/onet_30_2/db_30_2_text/` |
| 2 | Use case document | `strm/onet/use_case.json` |
| 3 | STRM mapping data | `strm/onet/strm_mapping.json` |
| 4 | Per-FDE rationale files (126) | `strm/onet/rationale/{fde-id}.json` |
| 5 | Scoring pipeline | `strm/onet/strm_scoring_pipeline.py` |
| 6 | Scoring summary | `strm/onet/scoring_summary.json` |
| 7 | Gap issue register | `strm/issues/STRM-001-ONET-gaps.json` |
| 8 | This ADR | `docs/roadmap/adr/ADR-015-strm-onet.md` |
| 9 | QA/QC report | `strm/onet/qa_qc_report.json` |

## References

- O*NET Database 30.2 (February 2026), National Center for O*NET Development, CC BY 4.0
- NIST IR 8477: Mapping Relationships Between Documentary Standards, Regulations, Frameworks, and Guidelines
- NIST IR 8278Ar1: National OLIR Program — Submission Guidance for OLIR Developers
- Reimers, N. & Gurevych, I. (2019). Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks. EMNLP.
- Zhang, T. et al. (2020). BERTScore: Evaluating Text Generation with BERT. ICLR.
- ADR-014: STRM-Based KSA Enrichment Methodology
- Phase 1B Framework Prioritization (`docs/roadmap/phase-1b-framework-prioritization.md`)
