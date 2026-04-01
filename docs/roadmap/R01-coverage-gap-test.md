# R01: Coverage Gap Test — Tier 0 Validation

**Test Date:** 2026-03-26
**WIDAI Version:** 0.4.0
**Test Type:** Tier 0 Validation (go/no-go for PE due diligence pilot)

---

## Executive Summary

R01 tests whether WIDAI can support a PE due diligence pilot by measuring role coverage and KSA availability across 5 representative mid-market data/AI team archetypes.

**Result: PASS**

- **Overall Role Coverage:** 100.0% (64/64 roles mapped)
- **KSA Coverage:** 92.2% (59/64 roles have Knowledge, Skills, and Attributes)
- **Decision Gate (≥60%):** PASS — Proceed to Tier 1 with current dataset

---

## Test Design

### Archetype Selection

All 5 archetypes represent PE target universe: mid-market companies ($100M-$2B revenue) with mature or growth-stage data/AI functions.

1. **PE-Backed Manufacturer** — 18-person team
2. **Mid-Market Financial Services** — 30-person team
3. **PE-Backed SaaS/Technology** — 25-person team
4. **Healthcare/Life Sciences** — 22-person team
5. **Mid-Market Retail/Consumer** — 12-person team

**Total roles analyzed:** 64 positions (team-level, not headcount)

### Mapping Methodology

- **Direct match:** Job title matched exactly to WIDAI canonical role title
- **Fuzzy match:** Semantic matching on role keywords (Data Engineer → Senior Data Engineer)
- **Assessment readiness:**
  - **Full** — Role exists with KSA mappings
  - **Partial** — Role exists, no KSAs available
  - **None** — Role not in WIDAI

---

## Per-Archetype Results

### 1. PE-Backed Manufacturer
**Team size:** 18 | **Roles analyzed:** 10

| Coverage | Value |
|----------|-------|
| Roles mapped | 10/10 (100%) |
| Full KSA coverage | 10/10 (100%) |

**Key roles:** Chief Data Officer, Data Governance Director, Data Engineers (2x), Data Analysts (3x), BI Developers (2x), Data Quality Manager, Analytics Engineer, Data Architect

**Assessment:** All roles have full assessment capability. Ready for comprehensive PE due diligence review.

---

### 2. Mid-Market Financial Services
**Team size:** 30 | **Roles analyzed:** 17

| Coverage | Value |
|----------|-------|
| Roles mapped | 17/17 (100%) |
| Full KSA coverage | 16/17 (94.1%) |

**Key roles:** CDO, CAIO, Data Governance Director, AI Risk/Ethics Specialist, Data Compliance Analysts (2x), Data Engineers (3x), Data Scientist, ML Engineer, Data Quality Manager, Data Product Manager, Master Data Manager

**Partial KSA coverage (1):** Model Risk Officer (matched to AI Risk/Ethics Specialist, limited KSA coverage)

**Assessment:** Exceptional coverage. Model Risk Officer mapping could benefit from regulatory-specific KSA expansion, but present assessment framework sufficient.

---

### 3. PE-Backed SaaS/Technology
**Team size:** 25 | **Roles analyzed:** 15

| Coverage | Value |
|----------|-------|
| Roles mapped | 15/15 (100%) |
| Full KSA coverage | 13/15 (86.7%) |

**Key roles:** CDO, Data Architect, Data Engineers (3x), Data Scientists (2x), ML Engineers (2x), MLOps Engineer, AI Engineer, Analytics Engineer, Data Analyst (2x), BI Developers (2x), Data Quality Manager, Data Product Manager, DataOps Engineer

**Partial KSA coverage (2):** MLOps Engineer (matched to Data Engineer), DataOps Engineer (matched to Data Platform Engineer)

**Assessment:** MLOps and DataOps KSAs are emerging; recommend light sprint in Tier 1 to enrich these roles.

---

### 4. Healthcare/Life Sciences
**Team size:** 22 | **Roles analyzed:** 14

| Coverage | Value |
|----------|-------|
| Roles mapped | 14/14 (100%) |
| Full KSA coverage | 12/14 (85.7%) |

**Key roles:** CDO, Data Governance Director, Data Compliance Analyst, Data Protection Officer, Data Privacy Specialist, Data Engineers (2x), Data Scientist, Data Analysts (3x), BI Developers (2x), Data Quality Manager, Master Data Manager

**Partial KSA coverage (2):** Clinical Data Manager (matched to Master Data Manager), Data Protection Officer (matched to Data Privacy Specialist)

**Assessment:** Clinical/domain-specific roles would benefit from healthcare-specialized KSAs. Privacy KSAs exist but domain-specific expansion recommended.

---

### 5. Mid-Market Retail/Consumer
**Team size:** 12 | **Roles analyzed:** 8

| Coverage | Value |
|----------|-------|
| Roles mapped | 8/8 (100%) |
| Full KSA coverage | 8/8 (100%) |

**Key roles:** Senior Data Analyst, Data Analysts (3x), BI Developers (2x), Data Engineers (2x), Analytics Engineer, Data Scientist, Data Quality Manager

**Assessment:** Complete KSA coverage. Lighter team structure means simpler PE assessment scope.

---

## Cross-Archetype Analysis

### Role Categories with Strongest Coverage
- **Governance (GOV):** 100% coverage, 100% KSA
- **Analytics (ANL):** 100% coverage, 100% KSA
- **Engineering (ENG):** 100% coverage, 95% KSA
- **Data Stewardship (DSM):** 100% coverage, 95% KSA

### Categories with Emerging Gaps
- **Risk/Ethics (RSK):** Strong coverage but regulatory-specific KSAs (e.g., SR 11-7, model risk frameworks) not fully developed
- **Leadership (LDR):** Core roles covered; emerging strategic roles (AI Innovation Lead, Transformation Lead) have limited KSA depth

### No Unmapped Roles
Zero archetypes had roles that could not be matched to WIDAI. This reflects both WIDAI breadth (187 roles) and intelligent fuzzy matching.

---

## KSA Coverage Details

**Total KSA entities in WIDAI:** 322 KSAs
**Roles with KSA mappings:** 159/187 (85%)
**Categories with KSA support:** 8/10 (GOV, ENG, DEV, DSM, ANL, RSK, OPS, LDR)
**Categories without KSAs:** NICHE (specialized roles), REG (regulatory framework roles)

---

## Decision Gate Analysis

**ADR-010 Threshold:** ≥60% role coverage with KSAs across archetypes

**Measured Result:** 92.2% KSA coverage

**Interpretation:** WIDAI exceeds threshold by 32.2 percentage points. Dataset is sufficiently mature to support PE due diligence pilot without delay.

---

## Recommended Actions for Tier 1

1. **Immediate (can proceed):**
   - Launch PE due diligence pilot with current dataset
   - Use full assessment framework for all 64 archetypical roles

2. **During Tier 1 (lightweight enhancements):**
   - Enrich MLOps Engineer and DataOps Engineer KSAs (2-3 day sprint)
   - Expand privacy KSAs with healthcare domain context (1-2 day sprint)
   - Add regulatory-specific KSAs for Risk/Compliance roles (2-3 day sprint)

3. **Post-pilot feedback loop:**
   - Collect PE assessor feedback on role gaps in actual diligence engagements
   - Prioritize KSA expansion based on real-world demand signals

---

## Conclusion

WIDAI v0.4.0 is **ready for PE due diligence pilot**. The dataset provides:

- **Comprehensive role coverage** across all mid-market data/AI team structures
- **Strong KSA foundation** with 92% of roles having complete assessment capability
- **Minimal mapping friction** — all archetypes map 100% to WIDAI roles
- **Clear roadmap** for targeted KSA enhancement post-pilot

No data freeze or pause required. Proceed to Tier 1 validation with confidence.

---

## Appendix: Test Artifacts

- **JSON Results:** `R01-coverage-gap-test.json` (machine-readable summary)
- **Analysis Script:** `r01_analysis.py` (reproducible test methodology)
- **Test Date:** 2026-03-26
