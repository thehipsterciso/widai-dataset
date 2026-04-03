# AG Knowledge — Phase 1D Synthesis Analysis

**Domain:** AI Governance & Ethics (AG)
**Dimension:** Knowledge
**Date:** 2026-04-03
**Pre-synthesis count:** 25 (14 Phase 1A baseline + 11 post-STRM additions)
**Post-synthesis count:** 19

## Evidence Summary

- **Total mappings:** 15,619 across 6 frameworks
- **Phase 1A entries (K-001 to K-014):** All have STRM evidence (5/6 to 6/6 coverage)
- **Post-STRM entries (K-015 to K-025):** 0/6 coverage (added after STRM runs)

### High Watermark (unique FDE count at STS thresholds)

| Framework | >=0.45 | >=0.50 | >=0.55 | >=0.60 |
|-----------|--------|--------|--------|--------|
| O*NET 30.2 | 13 | 5 | 1 | 0 |
| NIST NICE v2.1.0 | 595 | 410 | 235 | 110 |
| DoD DCWF v5.1 | 865 | 500 | 237 | 101 |
| DDaT | 46 | 16 | 5 | 0 |
| EU AI Act | 61 | 60 | 57 | 38 |
| NIST AI RMF 1.0 | 70 | 70 | 65 | 47 |

### Strongest STRM Hits

| Entry | Strong | Max STS | Top framework evidence |
|-------|--------|---------|----------------------|
| AG-K-004 | 4 | 0.7449 | EUAIA-O-037 AI interaction disclosure |
| AG-K-008 | 4 | 0.7363 | EUAIA-O-017 high-risk compliance |
| AG-K-002 | 3 | 0.7485 | AIRMF-GV-2.1 risk management roles |
| AG-K-006 | 2 | 0.7209 | EUAIA-C-003 human oversight |
| AG-K-005 | 1 | 0.7230 | EUAIA-C-007 deployer registration |
| AG-K-007 | 1 | 0.7207 | EUAIA-C-003 human oversight |
| AG-K-014 | 1 | 0.7031 | AIRMF-MG-3.2 pre-trained model monitoring |

## Duplicate Identification (Phase 1A)

Five groups of near-duplicate entries identified:

### Group 1: Explainability Methods
- **K-001:** Model interpretability and explainability methods (SHAP, LIME, partial dependence plots)
- **K-012:** AI explainability methods (SHAP, LIME, counterfactual explanations, attention visualization)
- **Action:** Merge → single entry covering all explainability techniques
- **Evidence:** K-001 (1,425 mappings) + K-012 (1,449 mappings)

### Group 2: AI Governance Structures
- **K-002:** AI governance structures (model risk management, lifecycle oversight, accountability)
- **K-006:** AI governance framework components (system registries, tiered review, impact assessment)
- **Action:** Merge → single entry covering governance structures and framework components
- **Evidence:** K-002 (1,377 mappings, 3 strong) + K-006 (1,760 mappings, 2 strong)

### Group 3: AI Risk Taxonomy
- **K-003:** AI risk taxonomy (model risk, algorithmic bias, opacity, adversarial vulnerability, data poisoning)
- **K-010:** AI risk categories (performance, bias/fairness, explainability, robustness, safety, privacy, compliance)
- **Action:** Merge → single entry covering full AI risk taxonomy
- **Evidence:** K-003 (1,012 mappings) + K-010 (432 mappings)

### Group 4: Responsible AI Principles
- **K-004:** Responsible AI principles and operationalization (fairness metrics, explainability, human oversight)
- **K-007:** Responsible AI principles and audit methods (fairness metric selection, bias test design)
- **Action:** Merge → single entry covering principles, operationalization, and audit
- **Evidence:** K-004 (1,386 mappings, 4 strong) + K-007 (1,378 mappings, 1 strong)

### Group 5: AI Regulatory Requirements
- **K-005:** AI regulatory frameworks (EU AI Act risk classification, conformity assessment)
- **K-008:** AI regulatory compliance requirements (EU AI Act conformity, prohibited uses, documentation)
- **K-013:** AI regulatory requirements (EU AI Act prohibited use, high-risk obligations, documentation)
- **Action:** Merge → single entry covering regulatory framework, compliance, and documentation
- **Evidence:** K-005 (1,067 mappings, 1 strong) + K-008 (1,101 mappings, 4 strong) + K-013 (590 mappings)

**Net effect:** 14 Phase 1A entries − 6 removed by merges = 8 distinct Phase 1A entries

## Post-STRM Entry Evaluation (K-015 to K-025)

| Entry | Concept | Framework evidence | Verdict |
|-------|---------|-------------------|---------|
| K-015 | AI risk management roles/accountability | AIRMF-GV-2.1 (0.7485) RACI structures; AIRMF-GV-2.3 (0.7244) exec governance | **KEEP** — distinct from merged governance group (roles vs structures) |
| K-016 | Human-AI interaction governance | EUAIA-O-014 (0.7131) human-machine interface; AIRMF-GV-3.2 | **KEEP** — distinct concept |
| K-017 | AI transparency/disclosure requirements | EUAIA-O-037 (0.7449) disclosure requirements | **KEEP** — regulatory disclosure, distinct from explainability methods |
| K-018 | AI data governance requirements | EUAIA-O-020 (0.7140) data management; EUAIA-O-006 training data | **KEEP** — distinct concept |
| K-019 | AI conformity assessment/compliance lifecycle | EUAIA-O-023 (0.7181) authorized representative; EUAIA-O-034 | **KEEP** — procedural compliance, distinct from regulatory knowledge |
| K-020 | AI risk measurement/quantification | AIRMF-MS-1.1, MS-1.2 risk measurement | **KEEP** — measurement methods, distinct from risk taxonomy |
| K-021 | AI supply chain risk | AIRMF-GV-6.1, GV-6.2 third-party risk | **KEEP** — distinct concept |
| K-022 | AI incident management/regulatory reporting | EUAIA-O-047 incident management; EUAIA-O-052 | **KEEP** — distinct concept |
| K-023 | AI system lifecycle governance | Various lifecycle elements across frameworks | **KEEP** — distinct from roles and structures |
| K-024 | AI TEVV methodology (governance perspective) | AIRMF-MS-2.13; AIRMF-MS-2.9 (0.7086) | **KEEP** — distinct concept |
| K-025 | AI stakeholder engagement/community impact | AIRMF-GV-5.1; AIRMF-MP-5.1 | **KEEP** — distinct concept |

**Net effect:** 11 kept, 0 removed

## Final Count

8 (Phase 1A deduplicated) + 11 (validated post-STRM) = **19 entries**

## Entry Mapping: Current → Proposed

| Proposed | Source | Action |
|----------|--------|--------|
| AG-K-001 | K-001 + K-012 | Merge (AI explainability methods) |
| AG-K-002 | K-002 + K-006 | Merge (AI governance structures/frameworks) |
| AG-K-003 | K-003 + K-010 | Merge (AI risk taxonomy) |
| AG-K-004 | K-004 + K-007 | Merge (responsible AI principles/audit) |
| AG-K-005 | K-005 + K-008 + K-013 | Merge (AI regulatory requirements) |
| AG-K-006 | K-009 | Renumber (AI literacy) |
| AG-K-007 | K-011 | Renumber (algorithmic fairness math) |
| AG-K-008 | K-014 | Renumber (ML-specific model risk) |
| AG-K-009 | K-015 | Renumber (risk management roles) |
| AG-K-010 | K-016 | Renumber (human-AI interaction governance) |
| AG-K-011 | K-017 | Renumber (transparency/disclosure) |
| AG-K-012 | K-018 | Renumber (AI data governance) |
| AG-K-013 | K-019 | Renumber (conformity assessment) |
| AG-K-014 | K-020 | Renumber (risk measurement) |
| AG-K-015 | K-021 | Renumber (supply chain risk) |
| AG-K-016 | K-022 | Renumber (incident management) |
| AG-K-017 | K-023 | Renumber (lifecycle governance) |
| AG-K-018 | K-024 | Renumber (TEVV methodology) |
| AG-K-019 | K-025 | Renumber (stakeholder engagement) |
