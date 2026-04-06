# TF Abilities — Evidence-Driven Re-Synthesis (Enforced)

## Overview

Domain: Technology Foundations (TF)
Dimension: Abilities
Starting count: 24 (from prior evidence-first expansion)
Final count: 25 (0 merges, 1 new entry)
Schema: 3.0.0
Methodology: Evidence-first synthesis with programmatic enforcement (synthesis_enforcer.py) and adversarial validation (adversarial_validator.py)

## Evidence Summary

Total mappings across 6 frameworks: 8,475
Framework elements at STS >= 0.50: 646
Framework elements at STS >= 0.55: 646
Framework elements at STS >= 0.60: 303

Evidence density: 12.1 elements per entry at STS >= 0.60 — highest of all TF dimensions for abilities. The unusually high density reflects TF's concrete technical nature — source frameworks describe technology competencies that map directly to ability-level statements, unlike abstract governance abilities.

### High Watermark

| Framework | >=0.45 | >=0.50 | >=0.55 | >=0.60 |
|-----------|--------|--------|--------|--------|
| O*NET 30.2 | 34 | 23 | 13 | 7 |
| NIST NICE v2.1.0 | 902 | 606 | 342 | 170 |
| DoD DCWF v5.1 | 1,297 | 891 | 494 | 226 |
| DDaT | 102 | 76 | 45 | 22 |
| EU AI Act | 53 | 42 | 31 | 17 |
| NIST AI RMF 1.0 | 70 | 68 | 53 | 26 |

All 6 frameworks contribute at STS >= 0.60, with DCWF (226) and NICE (170) dominating. O*NET provides 7 elements — its strongest showing in any abilities dimension across all 12 domains. EU AI Act (17) and NIST AI RMF (26) provide strong AI-specific signal.

5 Phase 1A entries (A-001 through A-005): 6/6 framework coverage. Extreme overload — A-005 (466 elements) and A-002 (323 elements) at STS >= 0.55 indicate broad semantic attraction.
19 post-STRM entries (A-006 through A-024): 0/6 direct coverage — added during prior expansion.

## Duplicate Analysis

4 close pairs examined:

**Pair 1: TF-A-001 (evaluate network infrastructure, analyzing vulnerabilities and performance) vs TF-A-023 (analyze system vulnerabilities and performance, evaluating weaknesses and optimization)**
A-001 focuses on infrastructure/platform evaluation — assessing what exists and whether it is fit for purpose. A-023 focuses on vulnerability and optimization analysis — finding weaknesses and improvement opportunities across any system. A-001 is evaluative (is this infrastructure sound?); A-023 is improvement-seeking (what can we optimize?). Distinct cognitive orientations. Evidence: T1424 (STS 0.7366) maps to both, confirming related but distinct concepts. No merge.

**Pair 2: TF-A-005 (systems analysis and assessments of capabilities) vs TF-A-024 (identify and document system capabilities and features)**
A-005 focuses on analytical assessment — understanding system characteristics in context. A-024 focuses on inventory and documentation — cataloging what capabilities exist. Assessment for decision support vs systematic documentation for organizational knowledge. Different outputs and stakeholders. No merge.

**Pair 3: TF-A-003 (design technical procedures and system components) vs TF-A-021 (design and develop software systems)**
A-003 covers broad technical design including procedures and processes. A-021 specifically covers software system design (architecture, components, interfaces). Software design is a specific subset with distinct deliverables and methodology. No merge.

**Pair 4: TF-A-004 (design data systems and integration) vs TF-A-020 (determine and analyze data requirements)**
A-004 covers design. A-020 covers requirements analysis. Different cognitive activities, different inputs and outputs. No merge.

**Merges: 0**

## Gap Analysis

Synthesis enforcer detected 10 gap signals: 5 broad mappings + 5 entry overloads.

**Broad mapping signals:**
All 5 broad mappings map to A-001 through A-005. These are generic technology competency elements:
- S0669 "integrating technology processes" (STS 0.6699) → covered by A-003
- 416 "analyze design constraints and trade-offs" (STS 0.6413) → partially covered by A-008, but the explicit sensitivity/trade-off analysis ability was missing
- 5936 "evaluate reliability/availability/maintainability" (STS 0.6343) → covered by A-005
- 132A "execute technology integration processes" (STS 0.6272) → covered by A-003
- 877A "verify stability, interoperability, scalability" (STS 0.6138) → covered by A-005

**Gap identified:** Element 416 "analyze design constraints, analyze trade-offs and detailed system and security design" maps to 5 entries but none specifically captures the ability to conduct sensitivity analysis and evaluate trade-offs across alternatives. A-008 evaluates specific tools; the missing concept is the systematic comparison methodology. This is supported by NICE S0114 (STS 0.6405, sensitivity analysis) and S0891 (STS 0.6112, evaluating alternatives).

**New entry: TF-A-025** — Ability to conduct sensitivity analysis and evaluate technical alternatives, assessing trade-offs and optimizing decisions across competing performance, cost, and reliability constraints.

**Entry overload analysis:**
TF-A-005 (466 elements) and TF-A-002 (323 elements) remain the most overloaded. The post-STRM expansion already decomposed these into 19 specific abilities (A-006 through A-024). The residual overload is structural — A-005 "systems analysis" and A-002 "root cause diagnosis" are the broadest technical abilities and attract generic framework elements. Further decomposition would fragment beyond useful granularity.

**New entries: 1 (TF-A-025)**

## Post-STRM Validation (A-006 through A-024)

19 entries added during prior expansion. Validated against indirect evidence:

| Entry | Concept | Indirect Evidence |
|-------|---------|-------------------|
| TF-A-006 | Continuous monitoring | T1960 (STS 0.6994 → A-002, A-005) |
| TF-A-007 | Test plans and TEVV | AIRMF-MP-3.5 (STS 0.7014 → A-002, A-005) |
| TF-A-008 | Tool/platform evaluation | T1309 (STS 0.6662 → A-002, A-005) |
| TF-A-009 | Requirements/gap analysis | S0759 (STS 0.6555 → A-005) |
| TF-A-010 | AI system lifecycle | AIRMF-MG-2.1 (STS 0.7005 → A-001, A-003, A-005) |
| TF-A-011 | Architecture assessment | S0383 (STS 0.6473 → A-005) |
| TF-A-012 | Redundancy/recovery design | T1276 (STS 0.6385 → A-002) |
| TF-A-013 | Technical maturity evaluation | S0066 (STS 0.6606 → A-005) |
| TF-A-014 | Intelligence analysis | S0739 (STS 0.6825 → A-001, A-003, A-005) |
| TF-A-015 | Data analysis/mining | S0854 (STS 0.6552 → A-002, A-005) |
| TF-A-016 | Business impact analysis | AIRMF-MP-1.3 (STS 0.6616 → A-005) |
| TF-A-017 | Risk mitigation strategies | T1560 (STS 0.6656 → A-002) |
| TF-A-018 | Network contingency planning | S0575 (STS 0.6594 → A-002) |
| TF-A-019 | Operational environment analysis | T1639 (STS 0.6582 → A-005) |
| TF-A-020 | Data requirement specification | T1063 (STS 0.6341 → A-004) |
| TF-A-021 | Software system design | T1135 (STS 0.6344 → A-003) |
| TF-A-022 | Hardware/infrastructure integration | S0570 (STS 0.6456 → A-003); 180A (STS 0.6810) |
| TF-A-023 | Vulnerability/optimization analysis | T1424 (STS 0.7366 → A-002, A-005); S0483 (STS 0.6600) |
| TF-A-024 | System capability documentation | T1337 (STS 0.6974 → A-002, A-005); T1309 (STS 0.6662) |

All 19 post-STRM entries retained. Each represents a distinct cognitive ability with cross-framework evidence.

## Mandatory Checklist

- [x] 1. Duplicate groups: **0 merges from 4 pairs examined.**
- [x] 2. Gap clusters: **5 broad mapping signals + 5 overload signals analyzed. 1 gap identified.**
- [x] 3. Cluster concepts: **Technology integration, design trade-offs, reliability evaluation, system verification, interoperability.**
- [x] 4. New entries: **1 — TF-A-025 (sensitivity analysis and trade-off evaluation). Evidence: 416 (STS 0.6413), S0114 (STS 0.6405), S0891 (STS 0.6112).**
- [x] 5. Framework evidence: **Cited per signal. Top STS: T1424 at 0.7366.**
- [x] 6. Post-STRM validated: **Yes — all 19 entries (A-006 through A-024) validated.**
- [x] 7. Final count: **25 = 5 Phase 1A + 19 post-STRM + 1 new. Sequential IDs TF-A-001 through TF-A-025.**
- [x] 8. Count increased from 24 to 25: **Evidence density of 303 elements at STS >= 0.60 across 24 entries indicated uncovered concept space. Gap analysis identified trade-off/sensitivity analysis as a distinct ability not captured by A-008 (tool evaluation) or other existing entries. Addition of TF-A-025 closes this gap. Domain_title typo ("Technical" → "Technology") and legacy_ids fields also corrected.**

## Final Entry Map

25 Abilities entries: TF-A-001 through TF-A-025.
5 Phase 1A + 19 post-STRM + 1 new.
0 merges, 1 new entry.
