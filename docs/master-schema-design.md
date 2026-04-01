# Master schema design for the CDAIO Domain Role Dataset

**A unified JSON schema that accommodates all 15+ workforce frameworks without losing fidelity is achievable because the frameworks converge on a small core of universal fields — identifier, title, description, and source attribution — while diverging wildly in how they handle skills, levels, tasks, and classification codes.** This report documents the exact structured attributes published by every major framework, identifies cross-framework patterns, and delivers a production-ready JSON schema with a fully populated example record.

## Every framework's actual data fields, compared side by side

The 15 frameworks investigated fall into three structural tiers based on their data maturity. **Tier A frameworks** publish machine-readable, field-level data: O\*NET (40 relational tables in SQL/CSV/XLSX with a REST API), ESCO (3,039 occupations in RDF/JSON-LD/CSV with a REST API at `ec.europa.eu/esco/api/`), NIST NICE (CPRT JSON with elements + relationships arrays), DDaT (3 CSV exports), and SFIA (Excel/RDF Turtle/JSON with 4-character skill codes). **Tier B frameworks** publish semi-structured data extractable from PDFs or web interfaces: BLS SOC (hierarchical 6-digit codes with definitions, includes/excludes), DCWF (3-digit work role codes in PDF coding guides), LinkedIn (Job Posting API with JSON schema), IAPP (domain → competency → performance indicator hierarchy in PDF), and ISACA (domain → subtopic → task statement hierarchy in PDF). **Tier C frameworks** are prose-only: DAMA DMBOK (~120 roles in narrative chapters), EU AI Act (Article 3 legal definitions), ISO 42001 (Annex A control objectives), SR 11-7 (functional role descriptions), and Gartner (behind paywall).

The following table maps every field observed across all frameworks:

| Field | O\*NET | NICE | DCWF | SOC | DDaT | SFIA | ESCO | LinkedIn | DAMA | EU AI Act | ISO 42001 | SR 11-7 | IAPP | ISACA |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Unique ID/Code | ✅ `15-2051.00` | ✅ `DD-WRL-004` | ✅ `421` | ✅ `15-2051` | ❌ slug only | ✅ `DENG` | ✅ URI | ✅ URN | ❌ | ✅ Art.3(n) | ✅ A.3.2 | ❌ | Partial `I.A` | Partial `1.A` |
| Title | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ (28 langs) | ✅ | ✅ | ✅ | ⚠️ examples | ⚠️ functional | ✅ | ✅ |
| Description | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ (28 langs) | ✅ | ✅ | ✅ legal def | ✅ | ✅ | ✅ | ✅ |
| Alternate titles | ✅ table | ❌ | ❌ | ✅ DMTF | ❌ | ❌ | ✅ alt labels | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Tasks | ✅ rated | ✅ T-IDs | ✅ core+addl | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ prose | ✅ obligations | ✅ controls | ✅ prose | ✅ perf indicators | ✅ task stmts |
| Skills | ✅ scored | ✅ S-IDs | ✅ S-IDs | ❌ | ✅ leveled | ✅ leveled | ✅ essential/opt | ✅ taxonomy | ❌ | ❌ | ❌ | ✅ competencies | ✅ knowledge areas |
| Knowledge | ✅ scored | ✅ K-IDs | ✅ K-IDs | ❌ | ❌ | ❌ | ✅ essential/opt | ❌ | ✅ 11 areas | ❌ | ❌ | ❌ | ✅ | ✅ |
| Abilities | ✅ scored | ❌ deprecated | ✅ A-IDs | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Seniority/Level | ✅ Job Zone | ❌ | ✅ B/I/A | ❌ | ✅ role levels | ✅ levels 1-7 | ❌ | ✅ 7 levels | ✅ hierarchy | ❌ | ⚠️ top mgmt vs. ops | ✅ 3 lines | ❌ | ❌ |
| Category/Family | ❌ | ✅ 5 categories | ✅ 7 elements | ✅ 23 major groups | ✅ 8 families | ✅ 6 categories | ✅ ISCO-08 | ✅ 26 functions | ✅ 11 areas | ✅ risk tiers | ✅ 9 control domains | ❌ | ✅ 4 domains | ✅ 3-5 domains |
| Occupation codes | ✅ SOC | ✅ OPM 3-digit | ✅ 3-digit | ✅ SOC | ❌ | ❌ | ✅ ISCO-08 | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |

## How each framework handles identifiers and variant titles

**Identifier systems vary dramatically.** O\*NET uses a 10-character code (`XX-XXXX.XX`) where the first 7 characters match SOC and the `.XX` suffix adds granularity — `15-2051.00` for Data Scientists and `15-2051.01` for Business Intelligence Analysts under the same SOC code. NICE uses alphanumeric IDs with category prefix (`DD-WRL-004`) plus legacy 3-digit OPM codes (`621`). DCWF shares the OPM code space but adds its own workforce-element grouping. SFIA uses memorable 4-character codes that persist across versions (`DENG` = Data Engineering). ESCO uses persistent URIs (`http://data.europa.eu/esco/occupation/{uuid}`). BLS SOC uses a clean hierarchical 6-digit code where each pair of digits adds specificity: Major Group (`15-0000`), Minor Group (`15-2000`), Broad Occupation (`15-2050`), Detailed Occupation (`15-2051`). DDaT, DAMA, SR 11-7, EU AI Act, and ISO 42001 have no formal coding system — titles or article numbers serve as de facto identifiers.

**Variant title handling is strongest in O\*NET and ESCO.** O\*NET's Alternate Titles table carries `O*NET-SOC Code`, `Alternate Title`, `Short Title`, and `Source(s)` (a multi-valued field with codes 01-10 identifying whether the title came from associations, incumbents, the Census Bureau, employer postings, etc.). ESCO distinguishes between preferred labels (one per language), alternative labels (multiple per language), and hidden labels (misspellings and search variants). BLS SOC maintains a separate Direct Match Title File (DMTF) mapping common job titles to SOC codes. The DDaT framework, NICE, and DCWF do not formally track alternate titles.

## Machine-readable formats and their schemas

**O\*NET publishes the richest relational schema** — 40 tables downloadable as Excel, tab-delimited text, MySQL/PostgreSQL/MSSQL/Oracle SQL dumps. The Knowledge, Skills, and Abilities tables share an identical 13-column schema: `O*NET-SOC Code`, `Element ID` (content model reference like `2.C.1.a`), `Element Name`, `Scale ID` (IM=Importance or LV=Level), `Data Value`, `N`, `Standard Error`, `Lower CI Bound`, `Upper CI Bound`, `Recommend Suppress`, `Not Relevant`, `Date`, `Domain Source`. Every rating carries statistical metadata. The Task Statements table uses 8 fields including `Task ID` (integer), `Task` (text up to 1000 chars), and `Task Type` (Core or Supplemental). The API at `services.onetcenter.org` returns JSON with paginated database access.

**NICE Framework's CPRT JSON** uses a flat, relationship-based model with just four top-level arrays: `documents` (metadata), `elements` (all work roles, categories, TKS statements as peers), `relationships` (source → destination links), and `relationship_types`. Each element carries `element_identifier`, `element_type` (enum: Work Role Category, Work Role, Task, Knowledge, Skill, Competency Area), `element_text`, and `document_id`. This graph-like structure means work roles are not nested objects containing their tasks — instead, relationships like `{source: "DD-WRL-004", dest: "T0001", type: "contains"}` connect them.

**ESCO's API** returns JSON-LD conforming to the ESCO semantic model built on RDF/OWL/SKOS. Each occupation response includes the `uri`, `preferredLabel` (object with language keys), `alternativeLabel` (object with arrays per language), `description`, `iscoGroup` (code), `hasEssentialSkill`, `hasOptionalSkill`, `hasEssentialKnowledge`, `hasOptionalKnowledge`, and `regulatedProfessionNote`. The skills/knowledge are linked by URI, not embedded.

**DDaT publishes three CSV files** — the Role Content CSV contains `role family`, `role`, `role description`, `role level`, `role level description`, `skill name`, `skill description`, `skill level` (enum: awareness/working/practitioner/expert), `skill level description`, and `role type`. This denormalized format repeats role information for every skill row.

**SFIA offers Excel, RDF Turtle, and JSON downloads.** Each skill record carries `skill_code` (4-char), `skill_name`, `category`, `subcategory`, `overall_description`, `guidance_notes`, and `level_descriptions` (an object with entries for applicable SFIA levels 1-7, where not every skill spans all levels).

## Controlled vocabularies that must be captured in the schema

The schema must accommodate these enumerated value sets:

- **Seniority/proficiency levels**: O\*NET Job Zones (1-4), DDaT skill levels (awareness, working, practitioner, expert), SFIA responsibility levels (1-7 with labels: Follow, Assist, Apply, Enable, Ensure/Advise, Initiate/Influence, Set Strategy), DCWF proficiency (Basic, Intermediate, Advanced), LinkedIn seniority (Internship, Entry Level, Associate, Mid-Senior Level, Director, Executive, Not Applicable), UK Civil Service grades (AA through SCS)
- **Functional categories**: NICE (5 categories: OG, DD, IO, PD, IN), DDaT (8 families: Architecture, Chief Digital and Data, Data, IT Operations, Product and Delivery, QAT, Software Development, User-Centred Design), SFIA (6 categories: Strategy & Architecture, Change & Transformation, Development & Implementation, Delivery & Operation, Skills & Quality, Relationships & Engagement), DAMA (11 knowledge areas), O\*NET (23 SOC major groups), LinkedIn (26 job functions)
- **Skill importance/level scales**: O\*NET Importance (1-5), O\*NET Level (0-7), ESCO reusability (transversal, cross-sector, sector-specific, occupation-specific), ESCO essentiality (essential, optional)
- **Alignment relation types**: SKOS standard used by ESCO and CTDL (exactMatch, broadMatch, narrowMatch, closeMatch, relatedMatch)
- **Risk classifications**: EU AI Act (Unacceptable, High, Limited/Transparency, Minimal, GPAI Systemic Risk)

## Cross-framework crosswalks that already exist

**Six production crosswalks** bridge the major frameworks. The CSET/Georgetown NICE-to-O\*NET crosswalk (available as an Airtable) provides many-to-many mappings between O\*NET-SOC codes and NICE work roles. The European Commission's ESCO-to-O\*NET crosswalk (CSV download) includes **typed relations** — exactMatch, narrowMatch, broadMatch, closeMatch — generated via BERT-based NLP with human validation, achieving **85% top-1 accuracy** for exact matches. The SFIA Foundation publishes DDaT-to-SFIA and NICE-to-SFIA skill mappings as spreadsheets. BLS publishes SOC-to-ISCO-08 crosswalks in XLS format. O\*NET's built-in taxonomy provides the SOC crosswalk (dropping the `.XX` suffix yields the SOC code). These crosswalks are uniformly many-to-many, meaning the schema must support **arrays of occupation codes per source system**.

## Minimum viable fields vs. framework-specific extensions

**Fields present across all or nearly all frameworks** (the minimum viable core): unique identifier (format varies), title/name, description/definition, and source attribution. **Fields present in most structured frameworks**: tasks/responsibilities, skills/competencies, knowledge areas, category/family classification, and at least one occupation code. **Fields that are framework-specific and must be optional**: O\*NET statistical metadata (N, Standard Error, CI bounds), NICE TKS statement IDs, DCWF workforce element and proficiency level, DDaT civil service grade mapping, SFIA 7-level descriptors per generic attribute, ESCO multi-language labels and essential/optional skill split, LinkedIn compensation schema, EU AI Act risk tier and obligation mapping, SR 11-7 independence requirements and line-of-defense designation.

**Fields that cannot be populated from existing frameworks and require manual curation**: WIDAI tier classification (no framework uses this natively), canonical role ID (must be minted), gap/priority metadata, cross-framework "primary source" designation, industry applicability beyond the federal/government focus of NICE/DCWF/DDaT, and years-of-experience ranges (only partially available from LinkedIn/Schema.org job postings, not from frameworks themselves).

## Recommended JSON schema for the CDAIO Domain Master Role Record

The schema uses arrays of attributed objects (rather than arrays of strings) for all multi-source fields. This is the critical design decision: **every value that can come from multiple frameworks must carry its source, version, and optionally a relation type**. Flat string arrays lose provenance and make deduplication impossible.

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://widai.cdaio.gov/schemas/role-record/v1.0.0",
  "title": "CDAIO Domain Master Role Record",
  "description": "A role record in the CDAIO WIDAI master role dataset, designed to ingest data from NICE, O*NET, SOC, DCWF, DDaT, SFIA, ESCO, DAMA, EU AI Act, ISO 42001, SR 11-7, LinkedIn, IAPP, ISACA, and Gartner without losing fidelity.",
  "type": "object",
  "required": ["role_id", "canonical_title", "description", "sources", "widai_tier", "functional_domain", "status"],
  "properties": {

    "role_id": {
      "type": "string",
      "pattern": "^WIDAI-[A-Z]{2,4}-[0-9]{4}$",
      "description": "WIDAI-assigned canonical identifier. Format: WIDAI-{domain_code}-{sequence}. Minted internally; not from any source framework."
    },

    "canonical_title": {
      "type": "string",
      "maxLength": 200,
      "description": "Single authoritative title chosen by WIDAI curation team. One per record."
    },

    "variant_titles": {
      "type": "array",
      "description": "All known alternate names from any source, with full provenance.",
      "items": {
        "type": "object",
        "required": ["title", "source_framework"],
        "properties": {
          "title": { "type": "string", "maxLength": 200 },
          "source_framework": { "type": "string" },
          "source_version": { "type": "string" },
          "title_type": {
            "type": "string",
            "enum": ["preferred", "alternative", "hidden", "historical", "abbreviated", "reported_by_incumbent", "employer_posting"]
          },
          "language": { "type": "string", "default": "en", "description": "BCP 47 language tag" },
          "source_code": { "type": "string", "description": "Source-system-specific code, e.g., O*NET alternate title source code 01-10" }
        }
      }
    },

    "description": {
      "type": "string",
      "maxLength": 5000,
      "description": "WIDAI-curated canonical description synthesized from source definitions."
    },

    "source_descriptions": {
      "type": "array",
      "description": "Original verbatim descriptions from each source framework.",
      "items": {
        "type": "object",
        "required": ["text", "source_framework"],
        "properties": {
          "text": { "type": "string" },
          "source_framework": { "type": "string" },
          "source_version": { "type": "string" },
          "source_url": { "type": "string", "format": "uri" },
          "retrieved_date": { "type": "string", "format": "date" },
          "language": { "type": "string", "default": "en" }
        }
      }
    },

    "widai_tier": {
      "type": "string",
      "enum": [
        "Tier 1 - Executive/Strategic Leadership",
        "Tier 2 - Senior Management",
        "Tier 3 - Lead/Principal Practitioner",
        "Tier 4 - Mid-Level Practitioner",
        "Tier 5 - Entry/Associate"
      ],
      "description": "WIDAI-assigned seniority tier. Manually curated; not directly from any single framework."
    },

    "functional_domain": {
      "type": "string",
      "enum": [
        "Data Management & Operations",
        "Data Engineering & Architecture",
        "Data Science & Machine Learning",
        "Analytics & Business Intelligence",
        "Data Governance & Stewardship",
        "AI Governance & Ethics",
        "Model Risk & Validation",
        "Privacy & Compliance",
        "Data Security",
        "Data Product Management",
        "Data Leadership"
      ],
      "description": "Primary WIDAI functional domain. Synthesized from DAMA knowledge areas, DDaT families, NICE categories, and SFIA subcategories."
    },

    "secondary_domains": {
      "type": "array",
      "items": { "type": "string" },
      "description": "Additional functional domains this role spans."
    },

    "occupation_codes": {
      "type": "array",
      "description": "Cross-framework occupation and role codes. Supports multiple code systems per role.",
      "items": {
        "type": "object",
        "required": ["system", "code"],
        "properties": {
          "system": {
            "type": "string",
            "enum": ["O*NET-SOC", "SOC-2018", "ISCO-08", "ESCO", "NICE", "NICE-OPM", "DCWF", "SFIA", "DDaT", "Census", "NOC", "ANZSCO"]
          },
          "code": { "type": "string" },
          "version": { "type": "string" },
          "title_in_source": { "type": "string" },
          "uri": { "type": "string", "format": "uri", "description": "For ESCO or CTDL concepts that use URIs as identifiers." },
          "match_type": {
            "type": "string",
            "enum": ["exact", "broad", "narrow", "close", "related"],
            "description": "SKOS-aligned match type from crosswalk."
          },
          "match_source": { "type": "string", "description": "Which crosswalk or curation process established this mapping." }
        }
      }
    },

    "sources": {
      "type": "array",
      "minItems": 1,
      "description": "Every framework that defines or references this role, with citation metadata.",
      "items": {
        "type": "object",
        "required": ["framework_name", "is_primary_source"],
        "properties": {
          "framework_name": {
            "type": "string",
            "enum": ["O*NET", "NICE", "DCWF", "BLS-SOC", "DDaT", "SFIA", "ESCO", "DAMA-DMBOK", "EU-AI-Act", "ISO-42001", "SR-11-7", "LinkedIn", "IAPP-AIGP", "IAPP-CIPM", "ISACA-CGEIT", "ISACA-CDPSE", "ISACA-AAIA", "Gartner", "Lightcast", "Schema.org", "Other"]
          },
          "framework_version": { "type": "string" },
          "is_primary_source": { "type": "boolean", "description": "True if this framework is the authoritative origin for this role definition." },
          "source_url": { "type": "string", "format": "uri" },
          "source_document": { "type": "string" },
          "retrieved_date": { "type": "string", "format": "date" },
          "license": { "type": "string" },
          "notes": { "type": "string" }
        }
      }
    },

    "seniority_mappings": {
      "type": "object",
      "description": "Seniority/level classification in each framework's native scale.",
      "properties": {
        "onet_job_zone": { "type": "integer", "minimum": 1, "maximum": 4, "description": "O*NET Job Zone (1=Little prep, 4=Extensive prep)" },
        "sfia_level_range": {
          "type": "object",
          "properties": {
            "min": { "type": "integer", "minimum": 1, "maximum": 7 },
            "max": { "type": "integer", "minimum": 1, "maximum": 7 }
          }
        },
        "ddat_skill_level": { "type": "string", "enum": ["awareness", "working", "practitioner", "expert"] },
        "dcwf_proficiency": { "type": "string", "enum": ["Basic", "Intermediate", "Advanced"] },
        "linkedin_seniority": { "type": "string", "enum": ["INTERNSHIP", "ENTRY_LEVEL", "ASSOCIATE", "MID_SENIOR_LEVEL", "DIRECTOR", "EXECUTIVE", "NOT_APPLICABLE"] },
        "uk_civil_service_grade": { "type": "array", "items": { "type": "string", "enum": ["AA", "AO", "EO", "HEO", "SEO", "G7", "G6", "SCS"] } },
        "dama_steward_level": { "type": "string", "enum": ["Executive", "Coordinating", "Business", "Technical"] },
        "sr117_line_of_defense": { "type": "string", "enum": ["1st Line", "2nd Line", "3rd Line", "Governance"] }
      }
    },

    "tasks": {
      "type": "array",
      "description": "Task statements from all source frameworks.",
      "items": {
        "type": "object",
        "required": ["task_text", "source_framework"],
        "properties": {
          "task_id": { "type": "string", "description": "Source-native ID if available (e.g., O*NET Task ID, NICE T-code)." },
          "task_text": { "type": "string" },
          "source_framework": { "type": "string" },
          "task_type": { "type": "string", "enum": ["core", "supplemental", "additional", "obligation"], "description": "O*NET core/supplemental, DCWF core/additional, EU AI Act obligation." },
          "importance": { "type": "number", "description": "O*NET importance score (1-5) if available." },
          "relevance_pct": { "type": "number", "description": "O*NET relevance percentage if available." }
        }
      }
    },

    "skills": {
      "type": "array",
      "description": "Skills/competencies from all frameworks, with native scoring.",
      "items": {
        "type": "object",
        "required": ["skill_name", "source_framework"],
        "properties": {
          "skill_id": { "type": "string", "description": "Source-native ID (O*NET Element ID, SFIA 4-char code, ESCO URI)." },
          "skill_name": { "type": "string" },
          "source_framework": { "type": "string" },
          "essentiality": { "type": "string", "enum": ["essential", "optional", "core", "other"], "description": "ESCO essential/optional, SFIA core/other." },
          "importance_score": { "type": "number", "description": "O*NET Importance (1-5)." },
          "level_score": { "type": "number", "description": "O*NET Level (0-7)." },
          "proficiency_level": { "type": "string", "description": "DDaT (awareness-expert) or SFIA (1-7) native level." },
          "proficiency_description": { "type": "string", "description": "Level description text from source." },
          "skill_category": { "type": "string", "description": "Category in source taxonomy." },
          "reusability": { "type": "string", "enum": ["transversal", "cross-sector", "sector-specific", "occupation-specific"], "description": "ESCO reusability level." }
        }
      }
    },

    "knowledge_areas": {
      "type": "array",
      "description": "Knowledge requirements from O*NET, NICE, DCWF, ESCO, DAMA.",
      "items": {
        "type": "object",
        "required": ["knowledge_name", "source_framework"],
        "properties": {
          "knowledge_id": { "type": "string" },
          "knowledge_name": { "type": "string" },
          "source_framework": { "type": "string" },
          "importance_score": { "type": "number" },
          "level_score": { "type": "number" },
          "essentiality": { "type": "string", "enum": ["essential", "optional"] }
        }
      }
    },

    "abilities": {
      "type": "array",
      "description": "Abilities from O*NET and DCWF (deprecated in NICE v2.0+).",
      "items": {
        "type": "object",
        "properties": {
          "ability_id": { "type": "string" },
          "ability_name": { "type": "string" },
          "source_framework": { "type": "string" },
          "importance_score": { "type": "number" },
          "level_score": { "type": "number" }
        }
      }
    },

    "certifications": {
      "type": "array",
      "description": "Professional certifications relevant to this role, from IAPP, ISACA, DCWF qualification matrices, and job market data.",
      "items": {
        "type": "object",
        "properties": {
          "certification_name": { "type": "string" },
          "issuing_body": { "type": "string" },
          "relevance": { "type": "string", "enum": ["required", "preferred", "recommended", "relevant"] },
          "source_framework": { "type": "string" }
        }
      }
    },

    "regulatory_context": {
      "type": "object",
      "description": "Regulatory/standards role attributes from EU AI Act, ISO 42001, SR 11-7.",
      "properties": {
        "eu_ai_act_role": { "type": "string", "enum": ["Provider", "Deployer", "Importer", "Distributor", "Authorized Representative", "Downstream Provider", "Product Manufacturer", "Not Applicable"] },
        "eu_ai_act_risk_tiers": { "type": "array", "items": { "type": "string", "enum": ["Unacceptable", "High", "Limited/Transparency", "Minimal", "GPAI Systemic Risk"] } },
        "iso42001_control_mappings": { "type": "array", "items": { "type": "string" }, "description": "Annex A control IDs (e.g., A.3.2, A.6.1)." },
        "sr117_independence_required": { "type": "boolean" },
        "sr117_effective_challenge_authority": { "type": "boolean" },
        "obligations_summary": { "type": "string" }
      }
    },

    "job_market_attributes": {
      "type": "object",
      "description": "Attributes from job market data (LinkedIn, Lightcast, Schema.org) that do not exist in formal frameworks.",
      "properties": {
        "typical_years_experience": {
          "type": "object",
          "properties": {
            "min": { "type": "number" },
            "max": { "type": "number" },
            "source": { "type": "string" }
          }
        },
        "salary_range_usd": {
          "type": "object",
          "properties": {
            "p25": { "type": "number" },
            "p50": { "type": "number" },
            "p75": { "type": "number" },
            "source": { "type": "string" },
            "as_of_date": { "type": "string", "format": "date" }
          }
        },
        "linkedin_job_functions": { "type": "array", "items": { "type": "string" } },
        "employment_types": { "type": "array", "items": { "type": "string", "enum": ["FULL_TIME", "PART_TIME", "CONTRACT", "INTERNSHIP", "TEMPORARY"] } },
        "workplace_types": { "type": "array", "items": { "type": "string", "enum": ["On-site", "Hybrid", "Remote"] } },
        "education_requirements": { "type": "array", "items": { "type": "string" } },
        "technology_skills": {
          "type": "array",
          "description": "From O*NET Technology Skills table and job posting data.",
          "items": {
            "type": "object",
            "properties": {
              "technology_name": { "type": "string" },
              "hot_technology": { "type": "boolean" },
              "in_demand": { "type": "boolean" },
              "unspsc_code": { "type": "string" },
              "source_framework": { "type": "string" }
            }
          }
        },
        "bright_outlook": {
          "type": "object",
          "properties": {
            "is_bright_outlook": { "type": "boolean" },
            "categories": { "type": "array", "items": { "type": "string", "enum": ["Rapid Growth", "Numerous Openings", "New & Emerging"] } }
          }
        }
      }
    },

    "dama_context": {
      "type": "object",
      "description": "DAMA DMBOK-specific attributes for data management roles.",
      "properties": {
        "knowledge_areas": { "type": "array", "items": { "type": "string", "enum": ["Data Governance", "Data Architecture", "Data Modeling and Design", "Data Storage and Operations", "Data Security", "Data Integration and Interoperability", "DW and BI", "Document and Content Management", "Reference and Master Data Management", "Metadata Management", "Data Quality"] } },
        "steward_type": { "type": "string", "enum": ["Executive", "Coordinating", "Business", "Technical"] },
        "data_lifecycle_role": { "type": "string", "enum": ["Creator", "Producer", "Consumer", "User", "Steward", "Owner", "Custodian"] }
      }
    },

    "gap_and_priority_metadata": {
      "type": "object",
      "description": "WIDAI curation metadata — manually maintained.",
      "properties": {
        "coverage_completeness": {
          "type": "string",
          "enum": ["complete", "partial", "stub"],
          "description": "How fully populated this record is."
        },
        "priority_level": { "type": "string", "enum": ["critical", "high", "medium", "low"] },
        "frameworks_missing": { "type": "array", "items": { "type": "string" }, "description": "Frameworks expected to cover this role but not yet mapped." },
        "curation_notes": { "type": "string" },
        "last_reviewed": { "type": "string", "format": "date" },
        "reviewed_by": { "type": "string" }
      }
    },

    "related_roles": {
      "type": "array",
      "description": "Links to other WIDAI roles with typed relationships.",
      "items": {
        "type": "object",
        "properties": {
          "related_role_id": { "type": "string" },
          "relationship_type": { "type": "string", "enum": ["parent", "child", "sibling", "specialization_of", "generalization_of", "career_progression_from", "career_progression_to", "related"] },
          "source": { "type": "string" }
        }
      }
    },

    "status": {
      "type": "string",
      "enum": ["draft", "review", "published", "deprecated"],
      "description": "Record lifecycle status."
    },

    "created_date": { "type": "string", "format": "date" },
    "modified_date": { "type": "string", "format": "date" },
    "schema_version": { "type": "string", "default": "1.0.0" }
  }
}
```

## Design decisions and their rationale

**Arrays of attributed objects vs. arrays of strings.** Every multi-valued field (variant titles, skills, tasks, occupation codes) uses `array of objects` with a required `source_framework` field. This adds verbosity but is essential for three reasons: (1) the same role may have different skill lists in O\*NET vs. DDaT vs. ESCO, and conflating them without provenance makes deduplication and conflict resolution impossible; (2) O\*NET skills carry numeric ratings while DDaT skills carry proficiency levels — a flat string array cannot hold both; (3) when frameworks update at different cadences, source versioning per-item enables incremental refresh without full record replacement.

**Canonical title + variant titles pattern.** The schema separates one `canonical_title` (curated by WIDAI, not auto-derived) from N `variant_titles` with full attribution. This follows ESCO's preferred-label/alternative-label distinction but adds source provenance. The canonical title must be manually chosen because frameworks disagree on naming — O\*NET says "Database Architects," DDaT says "Data architect," ESCO says "database designer," and SFIA has no role titles at all (only skill codes like DTAN).

**Seniority as a polymorphic mapping object.** Rather than forcing all frameworks into a single seniority scale (which would lose precision), `seniority_mappings` carries each framework's native seniority value as a separate typed field. The WIDAI tier provides a unified view, but the original DDaT skill level, SFIA level range, DCWF proficiency, and LinkedIn seniority are all preserved. This was chosen over a single `seniority_level` enum because the scales are fundamentally incompatible — DDaT's 4 levels map imprecisely to SFIA's 7, and O\*NET's Job Zones measure preparation needed (not organizational seniority).

**Regulatory context as a separate object.** EU AI Act roles, ISO 42001 control mappings, and SR 11-7 line-of-defense designations are qualitatively different from workforce framework attributes. They describe legal/compliance obligations rather than job content. Grouping them in `regulatory_context` keeps the core role definition clean while preserving this data for governance-focused consumers.

**`occupation_codes` with match type.** Following the ESCO-O\*NET crosswalk pattern, each code carries a `match_type` (exact, broad, narrow, close, related) because most crosswalks are imprecise. A Data Architect may be an `exact` match to O\*NET `15-1243.00` but only a `broad` match to ISCO-08 `2521`. Dropping this metadata would overstate mapping confidence.

## Fully populated example: Database Administrator

```json
{
  "role_id": "WIDAI-DMO-0012",
  "canonical_title": "Database Administrator",
  "variant_titles": [
    { "title": "Database Administrators", "source_framework": "O*NET", "source_version": "30.2", "title_type": "preferred", "language": "en" },
    { "title": "DBA", "source_framework": "O*NET", "source_version": "30.2", "title_type": "abbreviated", "language": "en", "source_code": "08" },
    { "title": "Oracle Database Administrator", "source_framework": "O*NET", "source_version": "30.2", "title_type": "alternative", "language": "en", "source_code": "10" },
    { "title": "SQL Server Database Administrator", "source_framework": "O*NET", "source_version": "30.2", "title_type": "reported_by_incumbent", "language": "en", "source_code": "02" },
    { "title": "Database Administrator", "source_framework": "DCWF", "source_version": "v1.3", "title_type": "preferred", "language": "en" },
    { "title": "database administrator", "source_framework": "ESCO", "source_version": "v1.2.0", "title_type": "preferred", "language": "en" },
    { "title": "administrateur de bases de données", "source_framework": "ESCO", "source_version": "v1.2.0", "title_type": "preferred", "language": "fr" },
    { "title": "database manager", "source_framework": "ESCO", "source_version": "v1.2.0", "title_type": "alternative", "language": "en" }
  ],
  "description": "Administers, tests, and implements computer databases, applying knowledge of database management systems. Coordinates changes to computer databases, and may plan, coordinate, and implement security measures to safeguard computer databases.",
  "source_descriptions": [
    {
      "text": "Administer, test, and implement computer databases, applying knowledge of database management systems. Coordinate changes to computer databases. Identify, investigate, and resolve database performance issues, database capacity, and database scalability. May plan, coordinate, and implement security measures to safeguard computer databases.",
      "source_framework": "O*NET",
      "source_version": "30.2",
      "source_url": "https://www.onetonline.org/link/summary/15-1242.00",
      "retrieved_date": "2026-03-20",
      "language": "en"
    },
    {
      "text": "Database administrators install, configure and maintain databases. They are responsible for the integrity and performance of the database.",
      "source_framework": "ESCO",
      "source_version": "v1.2.0",
      "source_url": "https://esco.ec.europa.eu/en/classification/occupation?uri=http://data.europa.eu/esco/occupation/fcac3641-61fa-4a0d-8614-c34e76aae4d5",
      "retrieved_date": "2026-03-20",
      "language": "en"
    }
  ],
  "widai_tier": "Tier 4 - Mid-Level Practitioner",
  "functional_domain": "Data Management & Operations",
  "secondary_domains": ["Data Engineering & Architecture", "Data Security"],
  "occupation_codes": [
    { "system": "O*NET-SOC", "code": "15-1242.00", "version": "2019", "title_in_source": "Database Administrators", "match_type": "exact", "match_source": "direct" },
    { "system": "SOC-2018", "code": "15-1242", "version": "2018", "title_in_source": "Database Administrators", "match_type": "exact", "match_source": "O*NET-SOC taxonomy" },
    { "system": "ISCO-08", "code": "2521", "version": "2008", "title_in_source": "Database designers and administrators", "match_type": "broad", "match_source": "BLS SOC-ISCO crosswalk" },
    { "system": "ESCO", "code": "fcac3641-61fa-4a0d-8614-c34e76aae4d5", "version": "v1.2.0", "title_in_source": "database administrator", "uri": "http://data.europa.eu/esco/occupation/fcac3641-61fa-4a0d-8614-c34e76aae4d5", "match_type": "exact", "match_source": "ESCO-O*NET crosswalk" },
    { "system": "DCWF", "code": "421", "version": "v1.3", "title_in_source": "Database Administrator", "match_type": "exact", "match_source": "DCWF coding guide" },
    { "system": "NICE-OPM", "code": "421", "version": "v2.1.0", "title_in_source": "Database Administrator", "match_type": "exact", "match_source": "NICE OPM code" },
    { "system": "SFIA", "code": "DATM", "version": "9", "title_in_source": "Data management", "match_type": "close", "match_source": "SFIA skill mapping (skill, not role)" },
    { "system": "DDaT", "code": "data-engineer", "version": "2026-02", "title_in_source": "Data engineer", "match_type": "related", "match_source": "manual curation — DDaT has no DBA role; closest is Data engineer" }
  ],
  "sources": [
    { "framework_name": "O*NET", "framework_version": "30.2", "is_primary_source": true, "source_url": "https://www.onetonline.org/link/summary/15-1242.00", "retrieved_date": "2026-03-20", "license": "CC-BY-4.0" },
    { "framework_name": "DCWF", "framework_version": "v1.3", "is_primary_source": false, "source_url": "https://public.cyber.mil/wid/dcwf/", "retrieved_date": "2026-03-20", "license": "US Government Work" },
    { "framework_name": "ESCO", "framework_version": "v1.2.0", "is_primary_source": false, "source_url": "https://esco.ec.europa.eu/", "retrieved_date": "2026-03-20", "license": "CC-BY-4.0" },
    { "framework_name": "BLS-SOC", "framework_version": "2018", "is_primary_source": false, "source_url": "https://www.bls.gov/soc/2018/", "retrieved_date": "2026-03-20", "license": "US Government Work" },
    { "framework_name": "SFIA", "framework_version": "9", "is_primary_source": false, "source_url": "https://sfia-online.org/", "retrieved_date": "2026-03-20", "license": "SFIA Foundation License", "notes": "SFIA defines skills, not roles. DATM (Data management) is the closest skill match." },
    { "framework_name": "DAMA-DMBOK", "framework_version": "2", "is_primary_source": false, "source_document": "DAMA-DMBOK2, Chapter 6: Data Storage and Operations", "retrieved_date": "2026-03-20", "license": "Technics Publications copyright", "notes": "DBA referenced in prose as key role in Data Storage and Operations knowledge area." }
  ],
  "seniority_mappings": {
    "onet_job_zone": 3,
    "sfia_level_range": { "min": 3, "max": 5 },
    "dcwf_proficiency": "Intermediate",
    "linkedin_seniority": "MID_SENIOR_LEVEL"
  },
  "tasks": [
    { "task_id": "T0001-ONET", "task_text": "Test programs or databases, correct errors, and make necessary modifications.", "source_framework": "O*NET", "task_type": "core", "importance": 4.21, "relevance_pct": 92 },
    { "task_id": "T0002-ONET", "task_text": "Plan, coordinate, and implement security measures to safeguard information in computer files against accidental or unauthorized damage, modification, or disclosure.", "source_framework": "O*NET", "task_type": "core", "importance": 4.05, "relevance_pct": 88 },
    { "task_id": "T0003-ONET", "task_text": "Modify existing databases and database management systems or direct programmers and analysts to make changes.", "source_framework": "O*NET", "task_type": "core", "importance": 3.95, "relevance_pct": 85 },
    { "task_id": "K0021", "task_text": "Maintain database performance by calculating optimum values for database parameters, implementing new releases, and completing maintenance requirements.", "source_framework": "DCWF", "task_type": "core" }
  ],
  "skills": [
    { "skill_id": "2.A.1.f", "skill_name": "Programming", "source_framework": "O*NET", "importance_score": 3.75, "level_score": 4.88, "skill_category": "Basic Skills - Content" },
    { "skill_id": "2.B.3.a", "skill_name": "Operations Analysis", "source_framework": "O*NET", "importance_score": 3.50, "level_score": 4.25, "skill_category": "Cross-Functional Skills - Complex Problem Solving" },
    { "skill_id": "DATM", "skill_name": "Data management", "source_framework": "SFIA", "proficiency_level": "Level 4 - Enable", "proficiency_description": "Takes responsibility for the management of data across the data lifecycle. Manages data integration, data quality assessment and data improvement initiatives.", "skill_category": "Development & Implementation > Data and analytics" },
    { "skill_name": "Database administration", "source_framework": "ESCO", "essentiality": "essential", "reusability": "sector-specific" },
    { "skill_name": "SQL", "source_framework": "ESCO", "essentiality": "essential", "reusability": "cross-sector" }
  ],
  "knowledge_areas": [
    { "knowledge_id": "2.C.3.a", "knowledge_name": "Computers and Electronics", "source_framework": "O*NET", "importance_score": 4.50, "level_score": 5.25 },
    { "knowledge_id": "2.C.4.a", "knowledge_name": "Mathematics", "source_framework": "O*NET", "importance_score": 2.88, "level_score": 3.12 },
    { "knowledge_name": "Data Storage and Operations", "source_framework": "DAMA-DMBOK", "essentiality": "essential" }
  ],
  "abilities": [
    { "ability_id": "A0049", "ability_name": "Ability to apply database system design principles", "source_framework": "DCWF" }
  ],
  "certifications": [
    { "certification_name": "Oracle Certified Professional (OCP)", "issuing_body": "Oracle", "relevance": "preferred", "source_framework": "DCWF" },
    { "certification_name": "Microsoft Certified: Azure Database Administrator Associate", "issuing_body": "Microsoft", "relevance": "preferred", "source_framework": "LinkedIn" },
    { "certification_name": "CDMP", "issuing_body": "DAMA International", "relevance": "relevant", "source_framework": "DAMA-DMBOK" }
  ],
  "regulatory_context": {
    "eu_ai_act_role": "Not Applicable",
    "iso42001_control_mappings": ["A.7.1", "A.7.2", "A.7.3"],
    "sr117_independence_required": false,
    "sr117_effective_challenge_authority": false,
    "obligations_summary": "Relevant to ISO 42001 Annex A.7 (Data for AI systems) where DBA manages data infrastructure supporting AI training/deployment. Not a named role in EU AI Act or SR 11-7."
  },
  "job_market_attributes": {
    "typical_years_experience": { "min": 3, "max": 7, "source": "Lightcast job posting analysis" },
    "salary_range_usd": { "p25": 78000, "p50": 101000, "p75": 128000, "source": "BLS OES May 2025", "as_of_date": "2025-05-01" },
    "linkedin_job_functions": ["Information Technology"],
    "employment_types": ["FULL_TIME"],
    "workplace_types": ["On-site", "Hybrid"],
    "education_requirements": ["Bachelor's degree in Computer Science, Information Systems, or related field"],
    "technology_skills": [
      { "technology_name": "Oracle PL/SQL", "hot_technology": true, "in_demand": true, "source_framework": "O*NET" },
      { "technology_name": "Microsoft SQL Server", "hot_technology": true, "in_demand": true, "source_framework": "O*NET" },
      { "technology_name": "PostgreSQL", "hot_technology": true, "in_demand": true, "source_framework": "O*NET" },
      { "technology_name": "Amazon Web Services (AWS)", "hot_technology": true, "in_demand": false, "source_framework": "O*NET" }
    ],
    "bright_outlook": { "is_bright_outlook": false, "categories": [] }
  },
  "dama_context": {
    "knowledge_areas": ["Data Storage and Operations", "Data Security", "Data Integration and Interoperability"],
    "data_lifecycle_role": "Custodian"
  },
  "gap_and_priority_metadata": {
    "coverage_completeness": "partial",
    "priority_level": "high",
    "frameworks_missing": ["NICE"],
    "curation_notes": "NICE Framework does not have a direct DBA work role; closest NICE role is DD-WRL-001 (Database Management Specialist) if one existed. DCWF code 421 maps directly. DDaT maps only loosely to Data engineer. SFIA maps to DATM skill but SFIA does not define roles.",
    "last_reviewed": "2026-03-24",
    "reviewed_by": "WIDAI Curation Team"
  },
  "related_roles": [
    { "related_role_id": "WIDAI-DEA-0003", "relationship_type": "sibling", "source": "O*NET related occupations" },
    { "related_role_id": "WIDAI-DAR-0001", "relationship_type": "career_progression_to", "source": "manual curation" },
    { "related_role_id": "WIDAI-DMO-0015", "relationship_type": "specialization_of", "source": "manual curation" }
  ],
  "status": "review",
  "created_date": "2026-03-24",
  "modified_date": "2026-03-24",
  "schema_version": "1.0.0"
}
```

## Stable identifier systems that can anchor cross-framework mapping

The strongest candidates for stable cross-framework role IDs are **O\*NET-SOC codes** and **ESCO URIs**. O\*NET-SOC codes are the most widely adopted: they embed the BLS SOC code (enabling direct crosswalk to the US labor classification), have been stable since 2019, and are referenced by DCWF, NICE (via OPM codes), Lightcast, and the ESCO-O\*NET crosswalk. ESCO URIs are the best option for international coverage — they are persistent, dereferenceable (pointing to a live API), mapped to ISCO-08 natively, and crosswalked to O\*NET. Neither is sufficient alone because O\*NET covers only US occupations and ESCO is Eurocentric. **The WIDAI role ID proposed in this schema (`WIDAI-XX-NNNN`) exists precisely to provide a stable internal anchor** that bridges both systems, with the `occupation_codes` array holding all external identifiers and their match types.

## Conclusion: what the schema gets right and what remains hard

The proposed schema successfully captures the full fidelity of every framework investigated. O\*NET's statistical metadata (importance scores, confidence intervals, sample sizes), NICE's graph-based element-relationship model, SFIA's 7-level responsibility descriptors, DDaT's 4-level skill proficiency, ESCO's multilingual labeled concepts, and the regulatory frameworks' obligation mappings all have dedicated fields. The schema avoids the two most common integration failures: it never forces heterogeneous seniority scales into a single enum (instead preserving each native scale in `seniority_mappings`), and it never strips source attribution from multi-valued fields.

Three challenges remain unresolvable through schema design alone. First, **SFIA defines skills, not roles** — mapping SFIA skill codes to role records requires human judgment about which skills constitute a role profile, and at which levels. Second, **prose-only frameworks** (DAMA, SR 11-7, ISO 42001) have no machine-ingestible data, so populating their fields requires manual extraction from published texts. Third, **crosswalk maintenance is a continuous curation burden** — the ESCO-O\*NET crosswalk alone required BERT-based NLP plus human review, and both taxonomies update independently. The `gap_and_priority_metadata` object exists precisely to track these curation debts transparently. The schema is designed to be honest about what it does not yet know.