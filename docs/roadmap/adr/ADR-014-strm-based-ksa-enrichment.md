# ADR-014: STRM-Based KSA Enrichment Methodology

**Status:** Accepted
**Date:** 2026-03-31
**Author:** Thomas Jones / The Hipster CISO
**Supersedes:** Enrichment approach in ADR-012 (Section 4: Dataset Enrichment Sprint)
**Informed by:** NIST IR 8477 (February 2024), SCF Set Theory Relationship Mapping practice

## Context

ADR-012 identified a critical KSA depth deficiency (8.95 KSAs/role versus NICE benchmark of 133) and prescribed a Dataset Enrichment Sprint to bring all mapped roles to 40+ KSAs. ADR-013 restructured the KSA data model to a shared domain-based pool, enabling cross-role KSA sharing.

The remaining question was *how* to execute the enrichment — how to determine what new KSAs to author, which existing KSAs to validate, and how to ensure cross-cutting KSAs emerge from evidence rather than assumption.

Initial approach considered: AI-assisted bulk authoring against each domain pool, validated by the Adversarial Quality Gate (AQG-v1). This approach was rejected during adversarial review on 2026-03-31 for the following reasons:

1. **No provenance chain.** Bulk-authored KSAs trace to "we thought it should be there," not to an external framework requirement. When a PE operating partner asks "why does this KSA exist," the answer must be traceable to source evidence.
2. **No systematic gap identification.** Without formal framework comparison, gaps are identified by intuition — the same failure mode that produced the original 8.95 KSAs/role depth deficiency.
3. **No cross-cutting evidence.** Common KSAs that carry across multiple roles should be identified by multiple independent frameworks confirming the same competency, not by a single authoring pass assuming which KSAs are shared.
4. **Optimization for motion over quality.** Bulk authoring optimizes for speed of pool population. The KSA pool is the core intellectual property of WIDAI — every commercial product scores against it. It requires the same methodological rigor applied to the roadmap itself.

## Decision

Adopt NIST IR 8477 Set Theory Relationship Mapping (STRM) as the formal methodology for KSA enrichment. Map the WIDAI KSA pool against each source framework individually, accumulate evidence, then synthesize the enriched pool from the aggregate findings.

### Methodology: NIST IR 8477 Set Theory Relationship Mapping

Per NIST IR 8477 Section 4.3, STRM is "a relationship style derived from the branch of mathematics known as set theory. Each mapping done with this style includes both a rationale for the mapping and a relationship type."

**Three rationale options** (per-mapping, not global):

1. **Syntactic** — How similar is the wording? Word-for-word analysis, not interpretation.
2. **Semantic** — How similar are the meanings? Involves interpretation of language.
3. **Functional** — How similar are the results of executing the two concepts?

Strictness order: Syntactic (most strict) → Semantic → Functional (least strict). The rationale type is a per-framework decision documented in each use case, not a project default.

**Five relationship types:**

1. **Subset of** — Concept A is a subset of Concept B. B contains everything A does and more.
2. **Intersects with** — Some overlap, but each includes content the other does not.
3. **Equal** — A and B are the same, although not necessarily identical.
4. **Superset of** — A is a superset of B. A contains everything B does and more.
5. **No relationship** — Unrelated; content does not overlap.

The relationship type and rationale must be used together.

**WIDAI enhancement:** Strength of Relationship (1–10 scale) is added as a seventh column. This is an WIDAI extension not prescribed by NIST IR 8477 but adopted from SCF practice to support quantitative analysis during synthesis.

### Document Orientation

- **Focal Document** — The source framework being mapped (NICE, SFIA, DAMA DMBOK, etc.). Each element from the focal document is evaluated.
- **Reference Document** — The WIDAI KSA Pool (version-pinned). Each focal element is mapped against the reference pool.

This orientation matches SCF practice. A focal document element with "No relationship" to any WIDAI KSA indicates a gap in the WIDAI pool.

### STRM Deliverable Format

Per NIST IR 8477 Table 5, adapted for JSON serialization:

| Column | Description |
|--------|-------------|
| Focal Document Element (ID) | Identifier from the source framework |
| Focal Document Element Description | Full text of the framework element |
| Rationale | Syntactic, Semantic, or Functional |
| Relationship | Subset of, Intersects with, Equal, Superset of, No relationship |
| Reference Document Element (ID) | WIDAI KSA ID (or null for No relationship) |
| Reference Document Element Description | Full WIDAI KSA statement (or null) |
| Strength of Relationship | 1–10 (WIDAI extension; null for No relationship) |

JSON is the authoritative format (consistent with repo convention). Each STRM mapping is stored as a JSON file in `strm/` following this structure.

### Execution Process

#### Phase 1A: Baseline KSA Enrichment

Before STRM mapping begins, the WIDAI KSA pool requires a first-pass enrichment from its current 363 KSAs to a reasonable baseline. At current depth (5–19 KSAs per role), STRM would produce overwhelmingly "No relationship" results — confirming what is already known (the pool is thin) without producing actionable signal.

The first-pass enrichment uses domain expertise and high-level framework knowledge to flesh out each of the 12 domain pools. This pass is explicitly acknowledged as pre-validation — the STRM phase will validate, correct, and refine what is authored here.

#### Phase 1B: Framework Prioritization

Assess WIDAI source frameworks for STRM relevance — which frameworks contain KSA-equivalent concept types (knowledge, skills, abilities, tasks, competencies) at sufficient granularity to map against the WIDAI pool. This determines the execution sequence.

Prioritization criteria:
- Does the framework define KSA-equivalent concepts? (Not all 70+ do.)
- Does the framework provide machine-readable or extractable element data?
- How many WIDAI roles does the framework cover?
- Strategic relevance to WIDAI use cases (PE assessment, EU AI Act, Model Risk)

Framework prioritization is documented in the roadmap. The prioritized list is not revised once STRM execution begins — it is executed in order.

#### Phase 1C: Per-Framework STRM Cycle

For each framework in priority order:

**Step 1 — Use Case Documentation (IR 8477 Section 3)**

Per NIST IR 8477 Section 3, document before mapping:
1. Target audience for this specific STRM
2. Why someone would use this mapping
3. Concept types being mapped from each source
4. Direction of the mapping
5. Exhaustiveness level
6. Rationale type selection and justification

**Step 2 — Canonical Source Acquisition**

Obtain the exact version of the framework document. Store a canonical copy in `sources/` (or a version-pinned citation with access date if the source cannot be redistributed due to licensing). Checksum where applicable.

**Step 3 — STRM Mapping Execution**

For each Focal Document Element, evaluate against every relevant WIDAI KSA. Document: rationale, relationship type, strength, and per-mapping reasoning.

Per-FDE rationale is stored as independent file objects to preserve full resolution. Rationale is not compressed into a single cell or array element. This is the evidentiary record — it must withstand scrutiny.

**Step 4 — Gap Issue Registration**

Every "No relationship" finding for a framework element that is in scope (i.e., should be covered by WIDAI) is registered as a discrete issue. Each issue includes:
- The FDE that has no match
- Domains searched
- Nearest miss (closest WIDAI KSA, if any)
- Suggested domain for the missing KSA
- Authoring guidance for the synthesis phase

Issues are tracked in `strm/issues/` as independent files.

**Step 5 — QA/QC Gate**

The STRM deliverable is reviewed before proceeding to the next framework:
- All FDEs evaluated (no blanks)
- All relationships have documented rationale
- Relationship types are consistent with the selected rationale type
- "No relationship" findings have complete issue context
- Summary statistics are computed and reviewed

**Step 6 — ADR Documentation**

Each framework STRM produces an ADR documenting:
- Framework selection rationale (from prioritization)
- Use case (from Step 1)
- Summary statistics (relationship type distribution, strength distribution)
- Key findings and anomalies
- Gap count and thematic analysis
- Reference to the STRM data file and canonical source

The STRM cycle does not proceed to the next framework until the current framework's QA/QC is complete and ADR is committed.

#### Phase 1D: Synthesis (Rules Defined After Evidence)

After all framework STRMs are complete:
- Accumulated gap issues are analyzed across all frameworks
- Cross-cutting KSAs are identified from multi-framework alignment evidence
- Synthesis rules are defined based on the evidence patterns observed — not before
- The enriched KSA pool is constructed from the synthesis findings
- Cross-STRM consistency is validated (transitivity check: if Framework A element X = WIDAI KSA Y, and Framework B element Z = WIDAI KSA Y, then X and Z should be equivalent)

The synthesis methodology is explicitly not defined in this ADR. Defining synthesis rules before evidence collection would bias the STRM evaluation. Synthesis rules will be documented in a separate ADR after the last framework STRM is QA'd.

### Deliverables Per Framework

| # | Deliverable | Location |
|---|-------------|----------|
| 1 | Canonical source document (or version-pinned citation) | `sources/` |
| 2 | Use case document (IR 8477 Section 3) | `strm/{framework}/use_case.json` |
| 3 | STRM mapping data (Table 5 + Strength) | `strm/{framework}/strm_mapping.json` |
| 4 | Per-FDE rationale files | `strm/{framework}/rationale/` |
| 5 | Gap issue register | `strm/issues/` |
| 6 | ADR | `docs/roadmap/adr/ADR-0XX-strm-{framework}.md` |
| 7 | QA/QC report | `strm/{framework}/qa_qc_report.json` |

*Alternatives considered:*
- Single monolithic mapping file per framework: Loses rationale resolution. Impossible to review or challenge individual mappings.
- Excel format (matching SCF): Human-friendly but inconsistent with WIDAI repo convention. JSON is machine-readable, diffable in git, and queryable for synthesis.
- No independent rationale files: Reduces deliverable count but compresses the most important part of the process — the reasoning — into a field that will be skimmed, not read.

### Principles

1. **No synthesis before all frameworks are mapped.** Gap issues are registered, not resolved, during STRM execution.
2. **No rushing through framework evaluations.** Each STRM is a complete, QA'd deliverable. Quality over motion.
3. **No deviation from NIST IR 8477 methodology.** Strength scoring is an additive enhancement. The five relationship types, three rationale options, and use case documentation requirements are followed as specified.
4. **Rationale and reasoning are preserved at full resolution.** Per-FDE rationale files are not a nice-to-have. They are the evidentiary foundation of every KSA in the enriched pool.
5. **Every KSA in the enriched pool traces to STRM evidence.** If a KSA cannot point to at least one framework STRM finding that justifies its existence, it does not belong in the pool.

## Consequences

**Positive:**
- Every KSA in the enriched pool has a provenance chain through STRM mappings to source frameworks.
- Cross-cutting KSAs emerge from multi-framework evidence, not assumption.
- Gap identification is systematic and exhaustive — not intuition-driven.
- The STRM deliverables are permanent, auditable artifacts that defend WIDAI methodology to any audience (PE operating partners, regulatory practitioners, analysts).
- Adopting NIST IR 8477 gives WIDAI methodological credibility — mapped using the U.S. government's published standard for framework relationship mapping.

**Negative:**
- Timeline extends significantly. Each framework STRM is a multi-session effort. 10+ frameworks at this depth could require 10+ dedicated working sessions.
- Deliverable volume is substantial — 7 deliverable types per framework across 10+ frameworks.
- First-pass enrichment (Phase 1A) remains domain-expertise-driven, not STRM-validated. It is acknowledged as pre-validation baseline, not final state.
- Synthesis rules are undefined until all evidence is collected. This is intentional but means the final KSA pool composition is not predictable at the start of the process.

## Roadmap Impact

| Item | Impact |
|------|--------|
| R03 (Pilot Engagement) | **Remains blocked** until enrichment completes via synthesis |
| R04 (Scoring Model) | Coverage dimension recalibration deferred to post-synthesis |
| R08 (KSA Authoring) | **Superseded** — KSA authoring now driven by STRM evidence |
| ADR-012 Section 4 | **Superseded** — enrichment sprint replaced by STRM-based enrichment |
| New: Phase 1A | Baseline enrichment before STRM (domain-expertise first pass) |
| New: Phase 1B | Framework prioritization for STRM sequencing |
| New: Phase 1C | Per-framework STRM cycle (10+ iterations) |
| New: Phase 1D | Post-evidence synthesis |

## References

- NIST IR 8477: Mapping Relationships Between Documentary Standards, Regulations, Frameworks, and Guidelines (February 2024). https://doi.org/10.6028/NIST.IR.8477
- NIST OLIR Program: https://csrc.nist.gov/projects/olir
- SCF Set Theory Relationship Mapping practice: https://securecontrolsframework.com/set-theory-relationship-mapping-strm/
- ADR-012: KSA Depth Correction (superseded in part)
- ADR-013: Shared-Pool KSA Architecture
- R02 Failure Assessment: Root cause analysis of depth deficiency
