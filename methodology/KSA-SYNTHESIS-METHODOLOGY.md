# KSA Synthesis Methodology

**Document Status:** Active
**Version:** 2.0.0
**Date:** 2026-04-05
**Applicable To:** All domain×dimension KSA synthesis across the WIDAI dataset

---

## Purpose

This document defines the process for building KSA entries from cross-framework STRM evidence. It replaces all prior synthesis instructions.

---

## The One Rule

**Existing entries have no standing.** The STRM rationale files across 6 scored frameworks are the only source of truth. Every synthesis starts from evidence and builds forward. Prior entries are not validated, preserved, or used as a starting point. They are discarded. The evidence produces whatever it produces.

---

## Evidence Sources

Six frameworks have been fully scored through NIST IR 8477 Set Theory Relationship Mapping (STRM):

| STRM ID | Framework | Elements |
|---------|-----------|----------|
| STRM-001 | O*NET 30.2 | Occupational knowledge, skills, abilities |
| STRM-002 | NIST NICE v2.1.0 | Cybersecurity workforce KSAs |
| STRM-003 | DoD DCWF v5.1 | Defense cyber workforce KSAs/tasks |
| STRM-004 | UK DDaT | Digital, Data and Technology skills |
| STRM-005 | EU AI Act | Regulatory obligations mapped to competencies |
| STRM-006 | NIST AI RMF 1.0 | AI risk management competencies |

Each framework element has been scored against every WIDAI KSA entry using a multi-method pipeline (cross-encoder STS primary, with BERTScore, NLI, bi-encoder cosine, and Jaccard secondary). Rationale files live in `strm/{framework}/rationale/`.

---

## Process Per Domain×Dimension

### Phase 1: Evidence Extraction

Run `dimension_synthesis.py` to extract all cross-framework evidence:

```bash
python3 scripts/dimension_synthesis.py --domain {DOMAIN} --dimension {DIMENSION} \
  > /tmp/{DOMAIN}_{DIMENSION}_synthesis.txt
```

Read the FULL output. The sections that matter:

1. **Top WIDAI-relevant elements per framework** — These are the actual concepts that frameworks associate with this domain×dimension. Each element has a description, an STS score, and a list of which current KSA IDs it mapped to. **Ignore the KSA IDs.** The descriptions are what matter — they are the raw concepts.

2. **High watermark** — How many unique framework elements exist at various STS thresholds. This is the evidence density.

3. **Evidence matrix** — Shows which current entries have STRM coverage and which don't. Entries with 0/6 coverage were added without STRM evidence. They have no privileged status.

### Phase 2: Concept Extraction

From the framework element descriptions across all 6 frameworks, extract the distinct **concepts** that appear. A concept is a coherent knowledge area, skill, ability, or task type that multiple framework elements describe from different angles.

Work framework by framework. For each framework's top elements:
- Read each element description
- Ask: what workforce concept does this describe, in the context of the {DOMAIN} domain?
- Write down the concept in plain language
- Note which framework elements support it

**Critical:** Do not look at or reference existing WIDAI entries during this step. You are extracting what the frameworks say, not confirming what already exists.

### Phase 3: Concept Clustering

Take the full list of extracted concepts across all 6 frameworks. Cluster them:

- Concepts that describe the same underlying competency from different frameworks → one cluster
- Concepts that are genuinely distinct → separate clusters
- Cross-framework corroboration strengthens a cluster (same concept appearing in 3+ frameworks is strong signal)
- Single-framework concepts at high STS are still valid if they represent a real competency for this domain

The number of clusters is the number of KSA entries. This number is an output. It is never predetermined.

### Phase 4: Write KSA Entries

For each concept cluster, write one KSA entry:

- Statement must capture the specific concept the cluster represents
- Statement must be scoped to the domain (Analytics & BI concepts for AB, not generic concepts that belong in another domain)
- Each entry must be supportable by at least one framework element at STS ≥ 0.50
- Use schema 3.0.0 format, sequential IDs, origin_framework "WIDAI", origin_version "0.8.0"

Domain scoping rule: If a concept cluster's framework elements are primarily about a different WIDAI domain (e.g., database administration concepts appearing in AB evidence because of semantic similarity to BI platform knowledge), that concept belongs in the other domain, not here. Only write entries for concepts that are genuinely about this domain's competency space.

### Phase 5: Adversarial Analysis — 3 Passes

After writing the initial entry set, run 3 adversarial passes. Each pass asks different questions:

**Pass 1 — Coverage Gaps:**
Go back to the framework elements. For each element at STS ≥ 0.55, can you point to a specific entry that covers that concept? If an element describes a concept that no entry covers, and that concept belongs in this domain, you have a gap. Add an entry.

**Pass 2 — Redundancy and Overlap:**
For each pair of entries that seem related, articulate the specific distinction. If you cannot clearly state what concept Entry A covers that Entry B does not (and vice versa), they are duplicates. Merge them.

**Pass 3 — Domain Boundary:**
For each entry, ask: is this concept more naturally home in a different WIDAI domain? If yes, remove it. The 12 domains are: AB (Analytics & BI), AG (AI Governance), AI (AI & ML), DA (Data Architecture), DG (Data Governance), DQ (Data Quality), LS (Leadership & Strategy), OP (Operations), RC (Regulatory Compliance), RM (Risk Management), SP (Security & Privacy), TF (Technology Foundations).

After all 3 passes, the entry set is final.

### Phase 6: Write Synthesis Doc

File: `docs/synthesis/{DOMAIN}-{DIMENSION_UPPER}-SYNTHESIS.md`

Required sections:
- **Overview** — domain, dimension, evidence density, final count
- **Evidence Sources** — what frameworks contributed, element counts at key STS thresholds
- **Concept Clusters** — list every cluster with its supporting framework elements
- **Adversarial Pass Results** — what each pass found and changed
- **Final Entry List** — all entries with their concept labels

This doc must contain gap analysis language (the adversarial validator checks for it).

### Phase 7: Write JSON

File: `ksas/{DOMAIN}_{DIMENSION}.json`

Schema 3.0.0. Sequential IDs. `count` field must equal `len(entries)`. No `legacy_ids`.

### Phase 8: Validate

```bash
python3 scripts/adversarial_validator.py \
  --domain {DOMAIN} \
  --dimension {DIMENSION} \
  --synthesis-file /tmp/{DOMAIN}_{DIMENSION}_synthesis.txt \
  --json-file ksas/{DOMAIN}_{DIMENSION}.json \
  --synthesis-doc docs/synthesis/{DOMAIN}-{DIMENSION_UPPER}-SYNTHESIS.md \
  --original-count {COUNT_BEFORE_THIS_SESSION}
```

All 8 checks pass or you fix and re-run.

---

## Domain Completion

After all 4 dimensions of a domain are synthesized:

1. Cross-validate — verify totals are consistent, no concept appears in both Knowledge and Skills without justification, Tasks reference capabilities that exist in the other 3 dimensions
2. Update `CHANGELOG.md` — one entry per domain with methodology narrative
3. Update `widai_manifest.json` — `statistics.total_unique_ksas` with new global total
4. Commit
5. **Stop and present results for review** before starting the next domain

---

## What This Process Prevents

Previous synthesis attempts failed by:

1. **Treating existing entries as the starting point** — reading current JSON first, then checking evidence against it. This anchors to the status quo and produces rubber-stamp validations that find "0 gaps" regardless of evidence density.

2. **Counting BROAD_MAPPING signals as noise** — generic framework elements that map to many entries were dismissed as "not real gaps." In reality, a framework element mapping to 9 entries with none at high STS often means the concept exists in the evidence but has no dedicated entry.

3. **Preserving entries without STRM evidence** — entries added through subject-matter reasoning (not STRM scoring) were validated by finding tangential framework elements that "support" them. This is confirmation bias. An entry either emerged from evidence or it didn't.

4. **Optimizing for count stability** — treating unchanged counts as a sign of quality rather than a sign of incomplete analysis.

The corrected process starts from evidence, builds forward, and lets the output be whatever the evidence produces.
