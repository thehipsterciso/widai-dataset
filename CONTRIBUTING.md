# ATLAS Commit Discipline Guide

This document is not a generic open source contributing guide. It is a **commit discipline system** designed to prevent the gap between what ATLAS actually contains and what its documentation claims.

The problem: work gets committed (new roles added, KSAs modified, frameworks remapped), but documentation doesn't follow. The README says 187 roles when there are actually 189. The manifest claims 322 KSAs but the actual count is 318. ADRs describe decisions that nobody validated. The roadmap claims a milestone is complete but the work isn't in the codebase.

This discipline ensures that every commit updates the documentation it changes, creates the documentation it needs, and validates that everything is consistent before merge.

---

## Every Commit Must Pass This Checklist

Before you push, go through every item below. Mark off as you go. If you skip an item, document why in the commit message (the "Exceptions" section at the bottom).

### A. Update Existing Documentation

These files document ATLAS's current state. If your commit changes any of these aspects, you **must** update these files.

- **[ ] CHANGELOG.md** — Does this commit add, change, or remove anything?
  - New roles? Add version/date entry with role count and category breakdown
  - Modified KSAs? Note the change count and any quality updates
  - Framework mappings added/removed? Document framework_id and mapping count
  - Bug fixes or data corrections? List affected entities
  - *Rule:* Every commit that touches `/roles/`, `/ksas/`, `/mappings/`, or `/frameworks/` needs a CHANGELOG entry. Undocumented commits create drift.

- **[ ] atlas_manifest.json** — Do any counts change?
  - Recount roles in each `/roles/*.json` file; update `directories.roles.files[].role_count`
  - Recount KSAs in each `/ksas/*.json` file; update `directories.ksas.files[].ksa_count`
  - Recount mappings in each `/mappings/*.json` file; update `directories.mappings.files[].mapping_count` or `relationship_count`
  - Update `statistics.total_roles`, `statistics.total_ksas`, `statistics.total_role_ksa_relationships`, `statistics.total_frameworks`
  - Update `statistics.categories[].role_count`, `statistics.categories[].ksa_count`, `statistics.categories[].role_ksa_count` for affected categories
  - Update `version` if this is a release commit
  - *Rule:* The manifest is the single source of truth for "what does ATLAS contain right now". Drift here causes every downstream decision to be made on stale data.

- **[ ] README.md** — Do any statistics, phase descriptions, status claims, or ADR summaries need updating?
  - Update role/KSA/framework counts in the "at-a-glance" section if manifest changed
  - Update Phase descriptions if a phase milestone is being closed
  - Update competitive positioning claims if a framework is added/removed
  - *Rule:* The README is the sales document. If it claims something that the data doesn't support, users lose trust immediately.

- **[ ] ADR statuses** — Does this commit validate, invalidate, or advance an ADR decision?
  - If this commit executes a decision documented in an ADR, change Status from "Proposed" to "Accepted"
  - If this commit provides evidence that an ADR assumption is wrong, add a note to the ADR explaining the invalidation and recommend "Superseded"
  - If this commit partially completes ADR acceptance criteria, update the Status field to "In Progress" and document what remains
  - *Rule:* ADRs that claim to be "Accepted" but point to incomplete work are worse than ADRs that claim to be "Proposed". Precision matters.

- **[ ] ADR acceptance criteria** — Does this commit check off any acceptance criteria checkboxes?
  - Scan the relevant ADR file for an "Acceptance Criteria" section with checkboxes (`- [ ] `)
  - If your commit satisfies a criterion, change `[ ]` to `[x]`
  - If your commit invalidates a criterion, add a comment explaining why
  - *Example:* ADR-003 has criterion "R01 coverage gap test result: PASS". When R01 completes, check that box.

- **[ ] GitHub issues** — Does this commit advance or close an issue?
  - Scan `/docs/roadmap/` and the Issues tab for open tracking items related to your commit
  - Add a comment to the relevant issue noting what this commit accomplishes
  - Use "Closes #XX" in the commit message footer if this commit fully resolves an issue
  - Use "Relates to #XX" if this commit is partial progress
  - *Rule:* Issues without recent comments become orphaned. Comments keep them alive.

- **[ ] Ensemble brainstorm & roadmap** — Does this commit execute a roadmap item?
  - Check `docs/roadmap/` for items matching your work (e.g., R01, R02, R05)
  - If a roadmap item (`R##.json` or `R##-*.md`) exists, add a "Completed" date and summary
  - Update the roadmap status in `docs/roadmap/PHASE-0-VALIDATION-SPRINT-RESULTS.md` (or equivalent phase file)
  - *Example:* If this commit completes R01, update `docs/roadmap/R01-coverage-gap-test.json` with results and date.

- **[ ] frameworks.json** — If framework references change, update metadata
  - If a new framework is added, insert a new entry into `frameworks.frameworks[]` with:
    - `framework_id`, `framework_name`, `roles_referencing` (count of roles that reference this framework)
    - `license_classification` (GREEN/YELLOW/RED), `commercial_status`, `license_type`
  - If a framework is removed, delete it from `frameworks.json`
  - If mapping counts change, update `roles_referencing` count
  - *Rule:* frameworks.json is the lookup table for all role-to-framework mapping validation. Stale counts cause false positives in consistency checks.

- **[ ] ATTRIBUTION.md** — If new GREEN frameworks are added, add attribution notices
  - If a new GREEN (commercial-use-permitted) framework is introduced, add a section documenting:
    - Framework name and source URL
    - License text or attribution requirements
    - Any restrictions on derivative works
  - If the framework is YELLOW (requires attribution) or RED (citation-only), note those restrictions
  - *Rule:* ATTRIBUTION.md is the legal surface. Incomplete attribution exposes ATLAS to compliance risk.

### B. Create New Documentation

After every commit, ask: **does this change create the need for something that doesn't exist yet?**

The mistake developers make: they add data without asking whether new documentation needs to be created. They validate an ADR without writing a summary. They add 30 new KSAs without documenting the authoring methodology. They hit a snag and create a workaround without tracking the follow-up issue.

- **[ ] New ADR?** — Was a significant architectural or strategic decision just made that isn't documented?
  - If your commit adds roles for a new domain (e.g., agentic AI), does an ADR exist explaining why?
  - If your commit changes the schema, does an ADR exist documenting the change rationale?
  - If your commit diverges from an existing ADR's guidance, create a new ADR explaining the divergence
  - *Where:* Create in `/docs/roadmap/adr/ADR-NNN-decision-name.md` following the existing ADR template

- **[ ] New data file?** — Was analysis performed that should be captured as structured data?
  - If your commit includes manual role-to-framework mapping decisions, does a `.json` file exist documenting those mappings?
  - If your commit updates KSAs based on user feedback, does a feedback analysis file exist?
  - If your commit validates a hypothesis (e.g., "role X maps to framework Y"), should that validation be a `.json` record?
  - *Purpose:* Structured data is machine-readable. CSV tables and markdown documents are not. Use JSON for anything that will be queried programmatically.

- **[ ] New markdown report?** — Was a test or audit completed that needs a human-readable summary?
  - If R01 (coverage gap test) completes, does a results markdown exist?
  - If you audit KSA quality, do results get documented?
  - If you validate a claim in an ADR, should a summary memo be created?
  - *Where:* Create in `/docs/roadmap/` with a clear date and result summary

- **[ ] New graphic/chart?** — Did a key statistic change that's represented visually?
  - If total role count or coverage percentage changed, update the README's "at-a-glance" SVG badge
  - If roadmap timeline shifted, update `docs/assets/roadmap-timeline.svg`
  - If a new framework category is added, update competitive positioning chart
  - *Rule:* Visuals get read 10x more often than tables. If the stat changed, the visual must change too.

- **[ ] New script?** — Was a manual process performed that should be automated?
  - If you manually validated 50 role-to-framework mappings, create a script to validate all mappings
  - If you manually counted roles by category, should that be in `check_consistency.py`?
  - If you created a one-time data cleanup, should it be a script for future use?
  - *Where:* Add to `/scripts/` with a docstring explaining what it validates

- **[ ] New schema update?** — Does the data model need to reflect new fields?
  - If you add a field to role records (e.g., `ai_governance_requirement`), update `/schema/role_record.json`
  - If you add a field to KSAs (e.g., `obsolescence_date`), update `/schema/ksa_record.json`
  - Add examples of the new field in the schema
  - *Rule:* Schema is the contract between code and data. Unsigned changes break downstream tools.

- **[ ] New GitHub issue?** — Did this commit surface a problem or decision that needs tracking?
  - If your commit reveals a data quality issue (e.g., 10 roles have null `seniority`), open an issue tracking the cleanup
  - If your commit enables a follow-up decision, open an issue for it
  - If your commit exposes a gap in documentation, open an issue to fill it
  - *Where:* Use the Issues tab. Reference the issue in the commit message with "Relates to #XX"

### C. Verify Consistency

Before you push, run the consistency check. This catches accidental drift.

- **[ ] Run `python scripts/check_consistency.py`**
  - The script checks all the things humans forget to verify:
    - Manifest counts match actual file counts
    - Framework references exist in frameworks.json
    - All role_ids and ksa_ids in relationships exist in their source files
    - No roles/KSAs are referenced but not defined
  - *Fix any failures before pushing.* Do not bypass this check.

---

## Commit Message Convention

Your commit message communicates to future developers and to the record of what was decided and when.

### Format

```
[ROADMAP_ITEM]: Brief description of the change

Longer context explaining why this change was needed, what it affects,
and what assumptions it validates or invalidates.

[Validation notes: e.g., "R01 coverage test complete, 92.2% KSA coverage"]

Documentation updated: CHANGELOG.md, atlas_manifest.json, ADR-003 status
[Issue references: "Closes #26" or "Relates to #15"]

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>
```

### Examples

**Example 1: Completing a roadmap validation test**

```
R01: Coverage gap test — PASS (92.2% KSA coverage)

Phase 0 Validation Sprint test. Mapped 64 roles across 5 archetypes.
Decision gate (>=60%): PASS — proceed to Tier 1 (validates ADR-003)

Documentation updated: CHANGELOG.md, atlas_manifest.json, ADR-003 status, README.md
Closes #12

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>
```

**Example 2: Adding new roles**

```
LDR+OPS: Add 8 new leader and operations roles for data governance

Added: LDR category (Data Governance Lead, Chief Data Officer variants)
       OPS category (Data Ops Manager, ML Ops Engineer)
Mapped to NIST AI RMF GOVERN and GARTNER CDA frameworks.
All 8 roles meet KSA quality acceptance criteria (R02 baseline).

Documentation updated: CHANGELOG.md, atlas_manifest.json, README.md

Closes #14

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>
```

**Example 3: Bug fix without changing core data**

```
Fix: Correct malformed JSON in DSM_ksas.json (escaped quotes)

The "Data Storytelling" KSA had an improperly escaped quote in the
definition field. This did not affect manifest counts or relationships.

Documentation updated: CHANGELOG.md (added to fixes section)

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>
```

### What to Include

- **Roadmap reference** (if applicable): `R01`, `R02`, `ADR-003`, etc.
- **What changed**: Specific roles added, frameworks updated, KSAs modified
- **Why it changed**: Business reason, validation result, external requirement
- **What it validates/invalidates**: Which ADRs or assumptions does this confirm or challenge?
- **Documentation updated**: Explicit list of files you touched (use `check_consistency.py` output to verify you didn't miss any)
- **Issue references**: GitHub issue numbers

### What NOT to Include

- Vague summaries like "Updated dataset" or "Fixed stuff"
- Changes to count-dependent files without explaining what changed the count
- Validation work without documenting the results
- References to internal decision discussions that aren't in the ADRs

---

## Exceptions & Bypass Conditions

You may skip a checklist item only if:

1. **The item doesn't apply** — You're fixing a typo in a non-data file. You're updating a comment. Document this in the commit message: "No documentation updates needed: comment fix only."

2. **A follow-up commit will handle it** — You're creating a multi-commit feature. Document in the first commit: "Documentation updates deferred to #XX" (and create that issue immediately). Do not ship the feature without the documentation.

3. **An open issue pre-authorizes the bypass** — An open GitHub issue says "defer CHANGELOG update to R02 completion". Reference the issue in the commit message.

**If you bypass a checklist item without documenting why, your commit will be rejected.**

---

## Running the Consistency Check

The `check_consistency.py` script is your safety net. Run it before every push.

```bash
python scripts/check_consistency.py
```

It will output:

```
Checking manifest accuracy...
  ✓ Roles: 187 (matches manifest)
  ✓ KSAs: 322 (matches manifest)
  ✓ Frameworks: 70 (matches manifest)

Checking CHANGELOG currency...
  ✓ No undocumented commits since last CHANGELOG date

Checking framework consistency...
  ✓ All frameworks in mappings exist in frameworks.json
  ✓ All frameworks have commercial_status and license_classification

Checking cross-references...
  ✓ All role_ids in mappings exist in role files
  ✓ All ksa_ids in mappings exist in KSA files

All checks PASSED.
```

If any check fails, the script exits with code 1 and lists the failures. **Fix them before pushing.**

---

## Questions?

- **"Do I really need to update CHANGELOG on every commit?"** — Yes. The CHANGELOG is the audit trail. It's the first place someone looks to understand what changed and when. Missing entries create gaps that future developers can't recover from.

- **"What if I don't know the exact KSA count?"** — Run `check_consistency.py`. It will tell you the count. That's what it's for.

- **"Can I merge without running the consistency check?"** — No. If you try, the GitHub Actions workflow will run it and fail the build.

- **"What if the consistency check is wrong?"** — Open an issue and document why. The check is a tool to catch human error, not a god. But verify your assumption before claiming the check is wrong.

---

## The Rationale Behind This Discipline

Three kinds of changes break datasets:

1. **Code drift** — The README claims 187 roles; you actually have 189.
2. **Decision drift** — An ADR says "ship on 37 KSA-complete roles"; you shipped on 60 without updating the ADR.
3. **Process drift** — You validate that something works, but you never document the validation, so the next person redoes the work.

This discipline catches all three before they escape into production.

The cost of this discipline is 5-10 minutes per commit. The cost of not having it is months of debugging trust issues with downstream tools and decision-makers who don't know whether the dataset reflects reality.

Choose the 5 minutes.
