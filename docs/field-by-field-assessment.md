# WIDAI schema field-by-field use case assessment for data and AI applications

**Every field in the WIDAI 187-role schema has defensible use cases in the data and AI space, but the fields vary dramatically in value density.** The identity, content, cross-framework mapping, and relationship fields form the schema's high-value core — they power knowledge graphs, ML training pipelines, semantic search, and RAG systems. The classification and regulatory context fields serve narrower but critical governance and compliance functions. A handful of fields, particularly in job market attributes and domain-specific context, carry weaker standalone justification and should be evaluated for consolidation. This assessment covers every field and nested object across all 12 field groups, scoped strictly to data and AI applications.

---

## Identity fields anchor the entire data product

These five fields form the irreducible core of the schema. Without them, no downstream AI or data application is possible.

### `role_id` (WIDAI-{DOMAIN}-{SEQUENCE})

**Primary use case.** Serves as the canonical foreign key for every downstream system that references WIDAI roles — knowledge graphs, vector databases, recommendation engines, and governance dashboards. The deterministic format (`WIDAI-{DOMAIN}-{SEQUENCE}`) enables both human readability and machine-parseable domain extraction, which is critical for partitioning in data mesh architectures.

**Secondary use cases.** Grounds LLM outputs in RAG systems by providing traceable citations back to authoritative records. Enables hybrid search (combining BM25 keyword retrieval on role_ids with dense vector similarity) — a pattern Neo4j's Advanced RAG guide identifies as essential because "semantic search excels at understanding meaning but can miss rare terms like IDs and codes." Also serves as the join key linking WIDAI to external model inventories, vendor capability matrices, and organizational charts.

**Inherent value.** A globally unique, stable identifier transforms 187 role definitions from a flat list into an addressable, referenceable data product. Per Zhamak Dehghani's data mesh principles, addressability through canonical identifiers is a prerequisite for data-as-a-product.

**Residual value.** Combined with `occupation_codes`, enables federated identity resolution across O\*NET, ESCO, SFIA, and DCWF. Combined with `related_roles`, forms the edge list for a complete role knowledge graph. Combined with `skills` and `tasks`, becomes the anchor node in a multi-relational skills ontology suitable for graph neural networks.

**Verdict: KEEP AS-IS.** The identifier format is well-designed — deterministic, human-readable, and namespace-scoped. No modification needed.

### `canonical_title`

**Primary use case.** Provides the single authoritative label for each role node in knowledge graphs, search indices, and UI surfaces. Essential for **job title normalization** — the core NLP task where free-text titles from job postings, resumes, and org charts are resolved to standardized entries. TechWolf's JobBERT model (trained on 10.5M job postings) and the ESCO-O\*NET crosswalk both depend on a single "preferred label" as the normalization target.

**Secondary use cases.** Seeds the `skos:prefLabel` property when the schema is serialized to RDF/linked data. Functions as the display name in career intelligence platforms (Eightfold, Gloat, Lightcast). Serves as the anchor text for embedding generation in vector databases — role descriptions chunked with canonical titles produce higher-quality embeddings than descriptions alone.

**Inherent value.** Resolves the fundamental ambiguity problem in workforce data. LinkedIn's Knowledge Graph team performs continuous entity resolution to standardize millions of diverse member-entered titles into canonical entities — a canonical_title field provides this ground truth for a domain-specific taxonomy.

**Residual value.** Combined with `variant_titles`, creates a complete synonym dictionary for entity resolution. Combined with `atlas_tier` and `functional_domain`, enables structured faceted search and filtering.

**Verdict: KEEP AS-IS.** Single authoritative title is the correct design pattern, mirroring SKOS `prefLabel` and ESCO's preferred label convention.

### `variant_titles` (array of objects)

**Primary use case.** Powers **entity resolution and deduplication** across heterogeneous data sources. The `title_type` enum (`preferred/alternative/hidden/historical/abbreviated/reported_by_incumbent/employer_posting`) maps almost perfectly to established patterns: `preferred/alternative/hidden` are direct SKOS equivalents (`skos:prefLabel`, `skos:altLabel`, `skos:hiddenLabel`). The `reported_by_incumbent` and `employer_posting` types capture real-world title variation that no other framework tracks — Indeed's deduplication pipeline identifies "similar job titles" as a core challenge, and this field provides the curated ground truth.

**Secondary use cases.** Expands the vocabulary surface for semantic search, improving recall when users search with non-standard titles. Serves as training data for job title normalization models — TechWolf's Synthetic-ESCO-skill-sentences dataset (138,260 pairs covering 99.5% of ESCO) demonstrates that synonym coverage directly improves ML model performance. The `source_framework` and `source_version` sub-fields enable framework-specific lookups (e.g., "What does SFIA call this role?" or "What does DDaT call this role?"). The `language` (BCP 47) sub-field enables multilingual entity resolution — critical for ESCO's 25-language coverage.

**Inherent value.** A curated synonym dictionary for 187 data/AI roles has immediate value for any NLP system processing workforce text. The title_type taxonomy is more comprehensive than most systems, which typically only track preferred + alternative.

**Residual value.** Combined with `occupation_codes`, creates a complete lookup table mapping any observed title variant → canonical role → framework-specific codes. This is the entity resolution pipeline in a single join. Combined with `skills` arrays, enables the distant supervision training approach used by JobBERT (roles with similar skills are likely the same entity).

**Verdict: KEEP AS-IS.** The title_type enum is exceptionally well-designed. The `reported_by_incumbent` and `employer_posting` types are genuinely novel additions to the SKOS pattern and capture variation that matters for real-world data ingestion.

### `description` (WIDAI-curated canonical description)

**Primary use case.** Serves as the primary text for **vector embedding generation** in RAG systems and semantic search. Production RAG pipelines use structured text templates like `"Role: {title}. Domain: {functional_domain}. Description: {description}. Key skills: {skills}."` to create embedding-ready chunks — the description field provides the richest semantic signal for similarity computation.

**Secondary use cases.** Functions as the reference text for zero-shot and few-shot classification of job postings into WIDAI roles. The OECD's semi-supervised approach used O\*NET skill definitions as "semantic anchors" for BERT-based classification — WIDAI descriptions would serve the same function. Also powers AI-generated job descriptions, competency frameworks, and training curricula when used as input context for generative models.

**Inherent value.** A curated, consistent description across all 187 roles — written in a single authorial voice rather than copied from disparate sources — produces cleaner embeddings and more reliable similarity scores than raw source text.

**Residual value.** Combined with `source_descriptions`, enables comparative analysis between the curated synthesis and original source texts — useful for detecting semantic drift or bias in curation. Combined with `skills` and `tasks`, creates multi-view representations of each role that improve retrieval quality through late fusion.

**Verdict: KEEP AS-IS.** Canonical descriptions are the single most important text field for embedding-based applications.

### `source_descriptions` (array of objects)

**Primary use case.** Provides **data provenance and auditability** for the canonical description. When an AI system makes decisions based on WIDAI role definitions (e.g., recommending candidates, flagging compliance gaps), auditors and regulators need to trace the definition back to its authoritative source. The `source_url`, `retrieved_date`, and `source_framework` sub-fields directly align with the Data & Trust Alliance's 22-metadata-field provenance standard.

**Secondary use cases.** Enables **multi-source training data generation** — each source description provides a different perspective on the same role, creating natural augmentation for NLP models. The ESCO-O\*NET crosswalk's success (85% top-1 accuracy) came from encoding multiple textual views of each occupation. Also supports temporal analysis: comparing descriptions across `source_version` values reveals how role definitions evolve. The `language` sub-field enables cross-lingual transfer learning.

**Inherent value.** Preserving verbatim source text (versus only the curated synthesis) is a data engineering best practice — it enables re-curation, error correction, and regression testing without re-fetching from external sources.

**Residual value.** Combined with `description`, enables fine-tuning contrastive learning models (source descriptions as positive pairs with the canonical description). Combined with `sources`, creates a complete citation graph from role definitions to framework documents.

**Verdict: KEEP AS-IS.** Provenance at the description level is essential for trustworthy AI applications. The sub-field structure is well-designed.

---

## Classification fields structure the taxonomy's information architecture

These fields define how roles are organized, filtered, and hierarchically arranged. Their primary value is in enabling structured queries, faceted search, and organizational modeling.

### `atlas_tier` (5-level enum)

**Primary use case.** Provides the **seniority axis for organizational design models**. Gartner's CDAO research identifies three archetypes (Expert D&A Leader, Connector CDAO, Pioneer CDAx) mapped to organizational tiers. A structured 5-tier hierarchy enables automated org chart generation, span-of-control analysis, and headcount planning for data/AI teams — problems that **70% of CDAOs** now own as primary responsibilities.

**Secondary use cases.** Functions as a **metadata filter in RAG systems** — when a user queries "What skills does a senior ML engineer need?", the system can filter to Tier 2-3 before running vector similarity, dramatically improving precision. Also enables seniority-appropriate career path recommendations (preventing systems from suggesting VP roles to associates) and compensation benchmarking within tiers.

**Inherent value.** A consistent 5-level hierarchy across 187 roles creates an immediately usable organizational skeleton. Without this field, any consuming system would need to infer seniority from titles — an error-prone NLP task.

**Residual value.** Combined with `seniority_mappings`, enables cross-framework seniority normalization (WIDAI Tier 3 ≈ SFIA Level 5 ≈ O\*NET Job Zone 4). Combined with `related_roles` (career_progression_from/to), creates a directed acyclic graph of career ladders within each tier.

**Verdict: KEEP AS-IS.** Five tiers is the right granularity — it matches O\*NET's 5 Job Zones and provides enough resolution for org design without over-fragmenting.

### `functional_domain` (11-domain enum)

**Primary use case.** Enables **domain-based partitioning** for organizational design and workforce planning. The 11 domains (Data Management & Operations through Data Leadership) map to the functional teams that CDAIOs actually build. Gartner finds that mature organizations create dedicated teams for data governance, ML/AI, analytics, and data engineering — these map cleanly to the enum values.

**Secondary use cases.** Powers faceted search and filtering in data catalogs and career platforms. Enables domain-specific skills gap analysis (e.g., "What's our coverage in AI Governance & Ethics?"). Functions as a graph partition key in knowledge graphs, enabling efficient community detection algorithms to identify related role clusters.

**Inherent value.** A controlled vocabulary of 11 domains provides the classification backbone for any analytics built on top of WIDAI — workforce dashboards, compliance coverage maps, and training needs assessments all depend on domain groupings.

**Residual value.** Combined with `atlas_tier`, creates a 5×11 matrix that maps the entire CDAIO organizational space. Combined with `skills`, enables domain-specific competency models. Combined with `regulatory_context`, identifies which domains carry regulatory obligations.

**Verdict: KEEP AS-IS.** Eleven domains is appropriate for the CDAIO scope. The enum values cover the major functional areas identified in Gartner, McKinsey, and industry research.

### `secondary_domains` (array of strings)

**Primary use case.** Captures **cross-functional role alignment**, reflecting the reality that most data/AI roles span multiple domains. A Data Ethics Officer might primarily sit in AI Governance & Ethics but also touch Privacy & Compliance and Data Leadership. This field enables multi-label classification of roles, which is more accurate than single-label for workforce planning.

**Secondary use cases.** Enables graph edge construction between domains (roles that bridge domains create implicit domain-to-domain relationships). Powers recommendation engines that suggest roles from adjacent domains for internal mobility. Supports skills gap analysis that accounts for shared competencies across domains.

**Inherent value.** Prevents the forced single-classification problem that plagues rigid taxonomies. Real workforce data is inherently multi-label.

**Residual value.** Combined with `functional_domain`, creates a bipartite graph of primary and secondary domain affiliations that reveals organizational interdependencies. Combined with `skills`, identifies the specific competencies that create cross-domain bridges.

**Verdict: KEEP WITH MODIFICATIONS.** The field should use the same controlled enum as `functional_domain` rather than free-text strings, to ensure consistency and enable reliable joins. Currently specified as "array of strings" — should be "array of functional_domain enum values."

### `category_code` and `category_title`

**Primary use case.** Provides a **coarser grouping** (10 categories: GOV/ENG/DEV/DSM/ANL/RSK/OPS/LDR/REG/NICHE) than the 11 functional domains, useful for executive-level dashboards and high-level portfolio views where domain-level granularity is excessive.

**Secondary use cases.** The short codes (GOV, ENG, etc.) are machine-friendly for use in compound identifiers, URL slugs, and API query parameters. Enables quick visual scanning in tabular reports and spreadsheet exports.

**Inherent value.** A two-level classification (category → domain) creates a useful drill-down hierarchy for analytics. The 10-category system provides executive-consumable groupings.

**Residual value.** Limited beyond what `functional_domain` already provides. The mapping between category_code and functional_domain should be deterministic — if it isn't, the two fields create ambiguity.

**Verdict: KEEP WITH MODIFICATIONS.** Formalize the mapping between `category_code` and `functional_domain` as a deterministic hierarchy. If the mapping is already one-to-one or many-to-one, document it explicitly in the schema. If the two dimensions are independent, rename `category_code` to clarify its orthogonal purpose (e.g., `work_type_code`). As currently described, the relationship between these 10 codes and the 11 domains is unclear, creating potential confusion for consumers.

### `inventory_sequence` (integer 1-187)

**Primary use case.** Provides a **stable sort order** for deterministic rendering in reports, exports, and UI listings. Without an explicit sequence field, consumers would need to sort by title (alphabetical, language-dependent) or role_id (which embeds domain but not meaningful order within domains).

**Secondary use cases.** Enables pagination in APIs. Functions as a human-friendly reference number for verbal communication ("role number 42"). Supports batch processing where deterministic ordering matters for reproducibility.

**Inherent value.** Minimal standalone value — it is an administrative convenience rather than a semantic property.

**Residual value.** Combined with `functional_domain`, could encode within-domain ordering (e.g., seniority-ranked within each domain). But this relationship is not currently specified.

**Verdict: KEEP AS-IS.** Low-cost field with genuine utility for deterministic ordering. Not worth removing, but not worth over-investing in either.

### `in_atlas_v030` (boolean)

**Primary use case.** Tracks **schema lineage** — which roles existed in the prior version of WIDAI. This is essential for change management when consumers depend on the dataset: they need to distinguish new additions from existing roles to manage migration.

**Secondary use cases.** Enables temporal analysis of how the data/AI role landscape is expanding. Supports rollback scenarios and version comparison dashboards.

**Inherent value.** Low standalone value — it is metadata about a specific schema transition event.

**Residual value.** Combined with lifecycle fields (`created_date`, `status`), creates a complete version history. But a single boolean tracking one specific prior version is brittle — it won't scale as WIDAI releases v0.4.0, v0.5.0, etc.

**Verdict: KEEP WITH MODIFICATIONS.** Replace with a more general `introduced_in_version` field (string, e.g., "v0.3.0" or "v0.4.0") that scales across schema versions. The current boolean only answers one question and will become increasingly irrelevant as the schema evolves.

### `atlas_work_role_id` (pointer to work role definition)

**Primary use case.** Creates a **foreign key relationship** to the WIDAI base structure's work role definitions, enabling normalization. Multiple WIDAI role records may map to the same underlying work role (e.g., a "Senior ML Engineer" and "Staff ML Engineer" might share a common work role definition but differ in tier).

**Secondary use cases.** Enables aggregation across seniority levels for workforce planning (counting all people in a work role family regardless of tier). Supports data normalization by separating role-level attributes from work-role-level attributes.

**Inherent value.** Standard relational design pattern that reduces redundancy and improves maintainability. Critical for any consuming system that needs to reason about work roles abstractly.

**Residual value.** Combined with `atlas_tier`, creates the work-role × seniority matrix. Combined with external WIDAI tables, enables join-based enrichment without denormalizing everything into the role record.

**Verdict: KEEP AS-IS.** Standard foreign key pattern. Well-designed.

---

## Provenance fields establish trust for downstream AI systems

### `sources` (array of objects)

**Primary use case.** Provides **data lineage and trust scoring** for every role definition. The `url_status` enum (`resolvable/paywalled/framework_level/placeholder`) is particularly valuable — it explicitly communicates whether the source can be independently verified, which is essential for AI audit trails. IBM tested the Data & Trust Alliance's provenance standards in their AI model clearance process and reported measurable increases in efficiency and data quality.

**Secondary use cases.** Enables **automated source freshness monitoring** — a pipeline can periodically check `resolvable` URLs and flag broken links. Supports regulatory compliance: the EU AI Act (Article 10) requires providers of high-risk AI systems to implement data governance covering training data provenance. The `source_framework` and `reference` sub-fields enable citation generation for reports and documentation.

**Inherent value.** Source provenance transforms WIDAI from an opinionated taxonomy into an evidence-based, auditable reference dataset. This distinction matters for adoption in regulated industries (financial services, healthcare, government).

**Residual value.** Combined with `source_descriptions`, creates a complete audit chain from curated role definition → source framework text → source URL. Combined with `gap_and_priority_metadata.frameworks_missing`, identifies where provenance is incomplete.

**Verdict: KEEP AS-IS.** The `url_status` enum is a thoughtful design choice that most schemas omit. It honestly communicates source accessibility, which is critical for trust.

### `seniority_level` (free text from source reports)

**Primary use case.** Preserves the **original seniority language** used by source frameworks, which may not map cleanly to the WIDAI 5-tier system. This is useful for entity resolution when matching WIDAI roles against external data that uses source-specific seniority language.

**Secondary use cases.** Provides NLP training data for seniority extraction models. Supports audit trails where regulators need to see the original source language.

**Inherent value.** Low — the free-text format limits machine-readability. The value is primarily archival.

**Residual value.** Combined with `atlas_tier` and `seniority_mappings`, provides a three-way cross-reference (WIDAI tier, source language, framework-specific levels) that resolves seniority ambiguities.

**Verdict: KEEP WITH MODIFICATIONS.** Consider restructuring as an array of objects (like `source_descriptions`) with `seniority_text`, `source_framework`, and `source_version` sub-fields to track which source provided which seniority language. Free text from a single unnamed source is less useful than attributed free text from multiple sources.

---

## Content fields are the schema's highest-potential assets

These four field groups (tasks, skills, knowledge_areas, abilities) are marked as deferred but represent **the most valuable fields in the entire schema** for AI/ML applications. Their population should be the highest priority.

### `tasks` (array of objects)

**Primary use case.** Enables **AI automation exposure analysis** — the dominant application of task-level occupational data in current research. The Upjohn Institute's AI Exposure Score, Pew Research Center's classification of 41 O\*NET work activities for AI susceptibility, and McKinsey's Skill Change Index all operate at the task level. Without populated task data, WIDAI cannot support the most policy-relevant analysis in the data/AI space: which role functions are automatable, augmentable, or resistant to AI.

**Secondary use cases.** Powers **task-based job matching** — TechWolf's foundational approach starts with "understanding actual work performed, then derives skills implications." Tasks serve as training labels for extreme multi-label classification models (TechWolf's ConTeXT-match achieves state-of-the-art using task/skill ESCO data). The `importance` score and `relevance_pct` sub-fields enable weighted analysis: a role where 80% of tasks are AI-automatable has a different strategic profile than one where only 20% are. The `task_type` sub-field enables filtering by task category.

**Inherent value.** O\*NET's content model demonstrates that tasks are the atomic unit of work — more granular than skills and more actionable than descriptions. Populating tasks for 187 data/AI roles would create the first domain-specific task inventory for the CDAIO space.

**Residual value.** Combined with `skills`, enables task-to-skill mapping that powers learning recommendation engines (identifying which skills enable which tasks). Combined with `atlas_tier`, reveals how task composition changes across seniority levels. Combined with `regulatory_context`, identifies which tasks carry compliance obligations.

**Verdict: KEEP AS-IS — PRIORITIZE POPULATION.** The sub-field structure (`task_id`, `task_text`, `source_framework`, `task_type`, `importance`, `relevance_pct`) is well-designed and mirrors O\*NET's proven content model. This field should be the top population priority.

### `skills` (array of objects)

**Primary use case.** Powers **skills gap analysis** — the most commercially valuable application of workforce taxonomy data. McKinsey recommends a 3-step process: build skills taxonomy, assess current state with targets per skill, then make structural adjustments. The `importance_score`, `proficiency_level`, and `essentiality` sub-fields directly enable this quantitative comparison. The World Economic Forum reports that **39% of workers' core skills** will change by 2030, and structured skills data is the foundation for measuring this shift.

**Secondary use cases.** Serves as training labels for **skill extraction models** — TechWolf's datasets on Hugging Face (138,260 sentence-skill pairs covering 99.5% of ESCO) demonstrate that curated skill arrays are essential ML training data. The `skill_category` sub-field enables grouped analysis. The `reusability` sub-field identifies transferable versus role-specific skills, powering internal mobility recommendations. Lightcast's open skills taxonomy (32,000+ skills) feeds 6,000 organizations and 250 HR tech partners — a 187-role domain-specific skill inventory would serve the same function for the CDAIO space.

**Inherent value.** **Skills are the lingua franca of the modern talent marketplace.** LinkedIn tracks 41,000+ skills; Lightcast maintains 34,000 validated skills; Cornerstone's Skills Graph covers 50,000+ unique skills. A curated, domain-specific skill inventory with importance and proficiency scoring has immediate commercial value.

**Residual value.** Combined with `tasks`, creates the task-skill mapping graph that drives learning recommendations. Combined with `occupation_codes`, enables cross-framework skill benchmarking (comparing WIDAI skill requirements against O\*NET importance scores). Combined with `certifications`, identifies the credential pathways that validate specific skills. Combined with `job_market_attributes.technology_skills`, bridges conceptual skills (e.g., "machine learning") to specific tools (e.g., "TensorFlow 2.x").

**Verdict: KEEP AS-IS — PRIORITIZE POPULATION.** The sub-field structure is comprehensive and well-aligned with O\*NET's content model and ESCO's skill property model. Second-highest population priority after tasks.

### `knowledge_areas` (array of objects)

**Primary use case.** Distinguishes **what practitioners need to know** from what they need to be able to do (skills) or what they actually do (tasks). This three-way distinction (knowledge/skills/tasks) follows O\*NET's proven content model and is essential for **curriculum design and training program development**. Knowledge areas map to educational content, while skills map to practical competency.

**Secondary use cases.** Enables knowledge graph construction where knowledge areas serve as nodes linked to roles, skills, and educational resources. The `essentiality` sub-field distinguishes foundational knowledge (must-have) from enriching knowledge (nice-to-have), enabling prioritized training paths. Supports AI literacy compliance under EU AI Act Article 4, which requires "sufficient level of AI literacy" — knowledge_areas defines what that means for each role.

**Inherent value.** The knowledge/skill/task triad is a well-established occupational analysis pattern. Omitting knowledge_areas would collapse two distinct dimensions (knowing vs. doing) into one, reducing the schema's analytical power.

**Residual value.** Combined with `skills`, enables gap analysis that distinguishes "doesn't know" from "can't do." Combined with `dama_context.knowledge_areas`, creates a domain-specific knowledge map for data management roles. Combined with `certifications`, identifies which credentials validate which knowledge areas.

**Verdict: KEEP AS-IS.** Follows the established KSA (Knowledge, Skills, Abilities) framework used by O\*NET, NICE/DCWF, and government HR systems worldwide.

### `abilities` (array of objects)

**Primary use case.** Captures **innate or developed cognitive and physical capabilities** that distinguish performance levels. O\*NET defines 52 distinct abilities (e.g., deductive reasoning, oral comprehension, information ordering). In the data/AI context, abilities like "mathematical reasoning" and "pattern recognition" differentiate AI researchers from AI project managers even when their skills lists overlap.

**Secondary use cases.** Feeds into assessment design — ability taxonomies define what pre-employment or development assessments should measure. Supports career path prediction by identifying abilities that transfer across role families.

**Inherent value.** Moderate standalone value. Abilities are the weakest of the KSA(T) quartet for practical applications in the data/AI space. Most consuming systems (skills gap tools, career platforms, ML training pipelines) operate primarily on skills and tasks.

**Residual value.** Combined with `skills` and `tasks`, completes the full KSA(T) content model. Combined with `atlas_tier`, could reveal how ability requirements shift with seniority. But the thin sub-field structure (`ability_id`, `ability_name`, `source_framework`) limits the analytical depth compared to the richer skills and tasks structures.

**Verdict: KEEP WITH MODIFICATIONS.** Add `importance_score` and `level_score` sub-fields to match the skills structure, enabling quantitative analysis. The current structure is too sparse for meaningful analytical use. If population resources are scarce, this field should be lowest priority among the content fields.

---

## Cross-framework mappings enable the interoperability backbone

### `occupation_codes` (array of objects)

**Primary use case.** Creates **cross-framework interoperability** — the single most technically challenging and commercially valuable capability a role taxonomy can offer. The ESCO-O\*NET crosswalk (built using BERT transformer models, achieving 85% top-1 accuracy) demonstrates that structured cross-framework mappings with typed match relations are the de facto standard for occupational data interoperability. The `match_type` enum (`exact/broad/narrow/close/related`) directly mirrors the official ESCO-O\*NET crosswalk relation types.

**Secondary use cases.** Enables **cross-national workforce planning** — a multinational organization can map WIDAI roles to O\*NET (US), ESCO (EU), DDaT (UK), SFIA (global IT), and ANZSCO (Australia/NZ) simultaneously, enabling consistent global role definitions. The `system` enum covering 12 frameworks (O\*NET-SOC, SOC-2018, ISCO-08, ESCO, NICE, NICE-OPM, DCWF, SFIA, DDaT, Census, NOC, ANZSCO) makes WIDAI a Rosetta Stone for occupational classification. Also powers entity resolution at scale: when an ATS ingests a job posting tagged with SOC code 15-2051, the system can resolve it to the correct WIDAI role via the occupation_codes mapping. The `uri` sub-field enables linked data integration.

**Inherent value.** The Occupation Ontology (OccO) project specifically addresses the "n-squared problem" of needing crosswalks between every pair of standards. WIDAI's occupation_codes field solves this by serving as a hub — mapping each role to all relevant frameworks simultaneously rather than requiring pairwise mappings between frameworks.

**Residual value.** Combined with `variant_titles`, creates a complete lookup table: any observed title variant → canonical role → any framework-specific code. Combined with `seniority_mappings`, adds level normalization to the cross-framework mapping. Combined with `skills`, enables cross-framework skill benchmarking (comparing WIDAI skill requirements against O\*NET importance scores or ESCO essential/optional designations).

**Verdict: KEEP AS-IS.** This is arguably the schema's most distinctive and defensible field. The `match_type` enum and `match_source` sub-field are well-designed and follow established crosswalk standards.

### `seniority_mappings` (object)

**Primary use case.** Normalizes **seniority across four independent leveling systems** — O\*NET Job Zones (1-5), SFIA levels (1-7), DCWF proficiency (Basic/Intermediate/Advanced), and DDaT skill levels. This is essential for cross-framework workforce planning: when a UK government department using DDaT needs to compare its staffing against a US federal agency using DCWF, seniority_mappings provides the translation layer. The `linkedin_seniority` enum adds the most commercially prevalent leveling system.

**Secondary use cases.** Enables **compensation benchmarking** across frameworks and geographies. BLS salary data is organized by O\*NET Job Zone; SFIA-based organizations benchmark by SFIA level; adding LinkedIn seniority enables market rate comparison. Also supports career path recommendations that cross framework boundaries.

**Inherent value.** NIST has published a formal report ("Defining a Proficiency Scale for the NICE Framework") exploring alignment between SFIA levels and NICE work roles, demonstrating that seniority normalization is an active area of standards development. Having this pre-computed in the schema saves consuming systems from solving a hard mapping problem.

**Residual value.** Combined with `atlas_tier`, creates a five-way seniority cross-reference. Combined with `job_market_attributes.salary_range_usd`, enables seniority-adjusted compensation analysis. Combined with `occupation_codes`, creates the most complete role-level interoperability package available.

**Verdict: KEEP AS-IS.** The field structure is well-designed. The `sfia_level_range` object with min/max is particularly good — it acknowledges that WIDAI roles may span SFIA levels rather than mapping 1:1.

---

## Certification field maps credentials to roles

### `certifications` (array of objects)

**Primary use case.** Enables **certification gap analysis** and credential-based workforce planning. As AI governance matures, specific certifications are becoming required or preferred for specific roles: PECB ISO 42001 Lead Implementer for AI governance roles, CIPP/E for privacy roles, HackTheBox AI Red Teamer for security roles, and emerging IEEE CertifAIEd credentials. The `relevance` enum (`required/preferred/recommended/relevant`) provides critical nuance — a required certification is a hard gate, while a relevant one is an enrichment signal.

**Secondary use cases.** Powers **procurement evaluation** — organizations can specify minimum certifications for vendor-proposed team members in RFPs. Supports regulatory compliance: GDPR Article 37 requires DPOs to have "expert knowledge of data protection law and practices," which is demonstrated through certifications like CIPP/E or CDPSE. Feeds recommendation engines that suggest certifications based on career path targets.

**Inherent value.** A curated mapping from 187 data/AI roles to relevant certifications creates an immediately usable credential planning tool. The `issuing_body` sub-field enables filtering by certifier (e.g., only ISACA certifications, only cloud vendor certifications).

**Residual value.** Combined with `skills`, identifies which skills are validated by which credentials. Combined with `job_market_attributes`, enables analysis of certification impact on compensation. Combined with `regulatory_context`, identifies which certifications satisfy regulatory competency requirements.

**Verdict: KEEP AS-IS.** Well-structured. The `relevance` enum with four levels is the right granularity for practical use.

---

## Regulatory context is a high-value differentiator

### `regulatory_context` (object)

**Primary use case.** Maps roles to **specific regulatory obligations** across three major regulatory frameworks: EU AI Act, ISO 42001, and SR 11-7. This is the schema's most forward-looking and differentiating field. The EU AI Act (effective August 2026) defines five operator roles (provider, deployer, importer, distributor, authorized representative) with distinct obligations — the `eu_ai_act_role` enum enables immediate role-to-obligation mapping. The `sr117_independence_required` boolean directly addresses the Federal Reserve's mandate that model validation "should be done by people who are not responsible for development or use."

**Secondary use cases.** The `eu_ai_act_risk_tiers` array enables risk-tier-based workforce planning — organizations can identify which roles are involved with high-risk AI systems and apply appropriate competency requirements. The `iso42001_control_mappings` array maps each role to specific ISO 42001 controls (e.g., Clause 5.3 for roles/responsibilities, Clause 7.2 for competence, Annex A.3 for roles), supporting certification audit preparation. The `obligations_summary` string provides human-readable regulatory context for non-specialist consumers. The `sr117_effective_challenge_authority` boolean identifies roles authorized to perform effective challenge — critical for bank regulatory examinations.

**Inherent value.** **No other workforce taxonomy includes structured regulatory obligation mappings.** This field single-handedly differentiates WIDAI from O\*NET, ESCO, SFIA, and every other occupational framework in the market. As regulatory pressure on AI intensifies globally, this field's value will compound.

**Residual value.** Combined with `certifications`, identifies which credentials satisfy regulatory competency requirements. Combined with `skills`, defines the competency profile for each regulatory obligation. Combined with `atlas_tier`, enables analysis of regulatory authority distribution across seniority levels. Combined with `related_roles`, maps the complete regulatory accountability chain from board level (Tier 1) to practitioners (Tier 5).

**Verdict: KEEP WITH MODIFICATIONS.** Add NIST AI RMF function mappings (GOVERN/MAP/MEASURE/MANAGE) as a sub-field — NIST AI RMF is the most widely adopted US AI governance framework and its GOVERN 1.5 subcategory specifically addresses organizational roles. Also consider adding a `jurisdictions` array to indicate which regulatory frameworks apply to each role based on geography, supporting multinational compliance mapping.

---

## Domain-specific context needs scope expansion or deprecation

### `dama_context` (object)

**Primary use case.** Maps roles to **DAMA-DMBOK knowledge areas** (14 knowledge areas including Data Governance, Data Architecture, Data Quality, etc.), steward types, and data lifecycle roles. This is relevant for organizations using DAMA's framework to structure their data management practices — a common pattern, given that DAMA-DMBOK is the most widely referenced data management body of knowledge.

**Secondary use cases.** The `steward_type` enum enables classification of data stewardship models (business steward, technical steward, operational steward). The `data_lifecycle_role` enum maps roles to lifecycle stages (creation, storage, use, archival, deletion), supporting GDPR data lifecycle compliance.

**Inherent value.** Moderate. DAMA is relevant but represents only one of several data management frameworks. The field is narrowly scoped to data management roles and has limited applicability to ML engineering, AI governance, or AI safety roles.

**Residual value.** Combined with `functional_domain`, enriches the data management subset of roles. Combined with `knowledge_areas`, creates a DAMA-specific competency model. But for roles outside the data management domain (roughly 7-8 of the 11 functional domains), this field adds no value.

**Verdict: KEEP WITH MODIFICATIONS.** Either expand this pattern to include equivalent context objects for other major frameworks (e.g., `nist_context`, `togaf_context`, `mlops_context`) or rename to `framework_specific_context` as a generic extensible pattern. A single domain-specific context field for DAMA creates an asymmetry that signals DAMA's primacy over other equally relevant frameworks.

---

## Job market attributes serve economic intelligence applications

### `job_market_attributes` (object)

This is a complex nested object with multiple sub-fields that serve different purposes. Assessment is provided per sub-field group.

### `typical_years_experience` (min/max), `salary_range_usd` (p25/p50/p75/source/as_of_date)

**Primary use case.** Enables **labor market intelligence and compensation benchmarking** for data/AI roles. BLS provides exactly this structure (10th-90th percentile wages via OEWS), and LinkedIn Salary adds Bayesian-smoothed percentile distributions. McKinsey's 2025 research found that **jobs requiring AI skills command a 56% wage premium** — structured salary data quantifies this premium at the role level. The `as_of_date` sub-field is critical: salary data depreciates rapidly, and consumers need to know whether the data reflects 2024 or 2026 market conditions.

**Secondary use cases.** Powers compensation design for CDAIO organizations. Enables ROI analysis for upskilling investments (comparing salary uplift from career_progression transitions against training costs). Supports vendor procurement by establishing market rates for specific role types.

**Inherent value.** High for the salary data; moderate for years_experience. BLS and LinkedIn already publish this data publicly — WIDAI's value-add is curating it for 187 specific data/AI roles and maintaining it over time.

**Residual value.** Combined with `skills`, enables skill premium analysis (which skills correlate with higher percentile salaries). Combined with `atlas_tier`, creates seniority-adjusted compensation bands. Combined with `certifications`, quantifies the certification premium.

**Verdict: KEEP AS-IS.** The p25/p50/p75 structure with source attribution and as_of_date is well-designed and mirrors BLS/industry standards. Consider adding a `currency` field to support non-USD markets as the schema scales internationally.

### `linkedin_job_functions`, `employment_types`, `workplace_types`, `education_requirements`

**Primary use case.** These sub-fields capture **market context** — how roles appear in the wild on job platforms. `linkedin_job_functions` enables mapping WIDAI roles to LinkedIn's internal taxonomy, supporting API integration. `employment_types` (full-time, contract, etc.) and `workplace_types` (remote, hybrid, on-site) capture the structural attributes of roles that affect talent availability.

**Secondary use cases.** Power job posting generation and matching. Support workforce planning by identifying which roles can be filled remotely (expanding talent pools) versus those requiring on-site presence.

**Inherent value.** Moderate. These are convenience fields that reduce the integration burden for consuming systems but could also be derived from job posting data at query time.

**Residual value.** Combined with `salary_range_usd`, enables analysis of the remote work premium/discount for specific roles. Combined with `occupation_codes`, enables cross-platform job market analysis.

**Verdict: KEEP AS-IS.** Low maintenance cost, genuine convenience value for career platforms and job matching applications.

### `technology_skills` (array of objects)

**Primary use case.** Bridges the gap between **conceptual skills** (captured in the `skills` field) and **specific tools and technologies**. A role might require the skill "machine learning" (conceptual) and the technology skills "TensorFlow," "PyTorch," and "scikit-learn" (concrete). Lightcast's data shows AI fluency demand grew **7x in two years** — technology_skills captures this demand at the tool level. Specific technologies carry measurable salary premiums (ML +25%, Deep Learning +30%, Cloud/Big Data +20%).

**Secondary use cases.** Powers **technical assessment** in hiring and vendor evaluation. Enables technology adoption analysis across the CDAIO organization. Feeds procurement decisions (which cloud platforms, ML frameworks, or data tools does each role need?).

**Inherent value.** High. Technology skills change faster than conceptual skills — having a separate, rapidly-updateable field for tools avoids polluting the more stable `skills` taxonomy with volatile technology names.

**Residual value.** Combined with `skills`, creates a conceptual-to-concrete skill mapping. Combined with `salary_range_usd`, quantifies technology-specific salary premiums.

**Verdict: KEEP AS-IS.** Well-designed separation of concerns between `skills` (stable, conceptual) and `technology_skills` (volatile, tool-specific).

### `bright_outlook` (object)

**Primary use case.** Mirrors BLS's Bright Outlook designation, flagging roles with projected rapid growth. BLS projects Data Scientists at **34% growth** (2024-2034). This field enables quick filtering for high-growth roles in workforce planning dashboards.

**Secondary use cases.** Supports career counseling and internal mobility recommendations by highlighting roles with strong market demand.

**Inherent value.** Low-to-moderate. BLS already publishes this data publicly, and the binary nature of "bright outlook" oversimplifies complex demand dynamics.

**Residual value.** Combined with `skills`, identifies which skills are associated with high-growth roles. Combined with `salary_range_usd`, enables growth-adjusted compensation analysis.

**Verdict: KEEP AS-IS.** Minimal maintenance cost, useful convenience field. Consider enriching with projected growth rate percentages rather than just a binary/object flag.

---

## Curation metadata enables governance at scale

### `gap_and_priority_metadata` (object)

**Primary use case.** Enables **data stewardship workflow management** for the WIDAI dataset itself. The `coverage_completeness` enum (`complete/partial/stub`) functions as a data quality metric — aligned with MDM best practices where "volume and quality of golden records" is a key KPI. The `priority_level` enum enables triage by data stewards. The `frameworks_missing` array identifies specific enrichment targets.

**Secondary use cases.** Powers **trust scoring for downstream consumers** — a consuming AI system can weight role records by completeness, giving higher confidence to `complete` records and lower confidence to `stub` records. The `last_reviewed` date supports the periodic review requirement in NIST AI RMF GOVERN 1.5. The `curation_notes` string enables human-readable context for editorial decisions. The `reviewed_by` string creates an accountability trail.

**Inherent value.** This field makes WIDAI a self-aware data product — it knows its own quality and communicates it to consumers. This is a rare and valuable design pattern that most taxonomies lack.

**Residual value.** Combined with `sources`, creates a complete quality assessment: which sources are available, which are missing, and how complete the record is. Combined with lifecycle fields, enables quality trend analysis over time.

**Verdict: KEEP AS-IS.** Excellent schema design. The combination of quality metrics, prioritization, gap identification, and audit trail in a single metadata object is well-structured and follows MDM best practices. Keep nesting shallow (2-3 levels) per JSON schema design experts' recommendations — this object stays within that range.

---

## Relationship fields power the knowledge graph

### `related_roles` (array of objects)

**Primary use case.** Creates the **edge list for the WIDAI role knowledge graph**. The `relationship_type` enum (`parent/child/sibling/specialization_of/generalization_of/career_progression_from/career_progression_to/related`) provides the typed edges needed for graph-based reasoning. ESCO's Neo4j implementation uses `skos:broader` and `skos:narrower` for hierarchy; WIDAI's richer relationship vocabulary enables more sophisticated graph queries.

**Secondary use cases.** Powers **career path recommendation engines** — the `career_progression_from/to` edges create directed paths that platforms like Eightfold, Gloat, and TalentGuard use for internal mobility recommendations. The `specialization_of/generalization_of` edges enable drill-down/roll-up navigation in career explorers. The `parent/child` edges define the organizational hierarchy. KDD 2025's CAPER paper demonstrates that temporal knowledge graphs with role/skill relationships achieve state-of-the-art career trajectory prediction.

**Inherent value.** **Relationships are the highest-leverage field in the schema.** A flat list of 187 roles is a reference table; a connected graph of 187 roles with typed relationships is a knowledge graph. The difference in analytical power is orders of magnitude — graph algorithms (community detection, shortest path, centrality) become available only when relationships are populated.

**Residual value.** Combined with `skills`, enables skill gap computation between current and target roles (the core operation powering career path recommendations). Combined with `atlas_tier`, creates the complete career ladder visualization. Combined with `functional_domain`, reveals cross-domain career transitions. Combined with `regulatory_context`, maps the regulatory accountability chain.

**Verdict: KEEP AS-IS.** The relationship_type enum is comprehensive and well-designed. The `source` sub-field (tracking where each relationship was derived) is a valuable provenance feature.

---

## Lifecycle fields close the data governance loop

### `status` (enum: draft/review/published/deprecated)

**Primary use case.** Implements **content lifecycle management** for the WIDAI dataset. MDM platforms universally implement workflow-based governance with configurable approval processes — this 4-state lifecycle mirrors the pattern used by Semarchy, Ataccama, and other MDM vendors. Consuming systems can filter to `published` records for production use while data stewards work on `draft` and `review` records.

**Secondary use cases.** The `deprecated` status enables soft deletion — roles that become obsolete are marked rather than removed, preserving referential integrity for historical analysis and audit trails. Supports the EU AI Act's documentation requirements by tracking when roles were established and retired.

**Inherent value.** Essential for any dataset that serves as a data product. Without lifecycle states, consumers cannot distinguish authoritative records from work-in-progress.

**Residual value.** Combined with `created_date` and `modified_date`, creates a complete temporal audit trail. Combined with `gap_and_priority_metadata`, enables quality-aware lifecycle management (e.g., `stub` records should remain in `draft` until completeness improves).

**Verdict: KEEP AS-IS.** Standard and essential.

### `created_date`, `modified_date`, `schema_version`

**Primary use case.** Implements **temporal governance and version control**. The `schema_version` field is particularly important — it enables consuming systems to detect breaking changes and adapt their parsing logic accordingly. Saxo Bank's data mesh implementation uses "GitOps for domain management" with schema versioning as a core requirement.

**Secondary use cases.** Supports the EU AI Act's requirement that providers keep technical documentation for 10 years and deployers retain logs for at least 6 months. Enables "time-travel queries" — reconstructing what the WIDAI dataset looked like at any point in time. Powers change detection pipelines that notify consumers when records they depend on are modified.

**Inherent value.** Table stakes for any data product. Without timestamps and version tracking, the dataset cannot be managed, audited, or integrated reliably.

**Residual value.** Combined with `status`, creates a complete state machine history. Combined with `sources.retrieved_date`, enables freshness comparison between the WIDAI record and its underlying sources.

**Verdict: KEEP AS-IS.** Standard and essential. Consider adding a `version` field at the record level (distinct from `schema_version`) to track individual record revisions if the schema evolves to support record-level versioning.

---

## Twelve fields warrant modification, none warrant deprecation

Across the entire schema, the assessment identifies **zero fields that should be deprecated**. Every field has at least one defensible use case in the data and AI space. However, the fields vary dramatically in value density, and twelve modifications would strengthen the schema:

| Field | Verdict | Rationale |
|-------|---------|-----------|
| `secondary_domains` | Modify | Use `functional_domain` enum values instead of free-text strings |
| `category_code` / `category_title` | Modify | Formalize the deterministic mapping to `functional_domain` |
| `in_atlas_v030` | Modify | Replace with `introduced_in_version` (string) for scalability |
| `seniority_level` | Modify | Restructure as array of attributed objects with source_framework |
| `abilities` | Modify | Add `importance_score` and `level_score` sub-fields |
| `regulatory_context` | Modify | Add NIST AI RMF function mappings and `jurisdictions` array |
| `dama_context` | Modify | Generalize to extensible `framework_specific_context` pattern |

The schema's highest-value fields are `occupation_codes`, `related_roles`, `skills`, `tasks`, `regulatory_context`, and `variant_titles` — these six fields power the applications that most differentiate WIDAI from existing taxonomies. The content fields (tasks, skills, knowledge_areas, abilities) represent the schema's largest unrealized value and should be the top population priority. The regulatory context field is WIDAI's most unique competitive advantage — no other occupational framework offers structured regulatory obligation mappings, and as AI regulation intensifies globally, this field's value will compound rapidly. The schema is mature, well-designed, and ready to serve as the canonical reference data product for the CDAIO organizational domain.