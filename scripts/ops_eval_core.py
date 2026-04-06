#!/usr/bin/env python3
"""
WIDAI OPS Category — Shared Evaluation Engine (Passes 2, 3, 4)
Covers all 15 OPS roles with role-specific calibration.
Calibration target: 80–160 included KSAs per role.
"""
import json, os, re, datetime

# ── Domain labels ─────────────────────────────────────────────────────────────
DOMAIN_LABELS = {
    'TF': 'Technology Fundamentals',
    'DA': 'Data Architecture',
    'DQ': 'Data Quality',
    'DG': 'Data Governance',
    'SP': 'Security & Privacy',
    'AI': 'AI & ML Infrastructure',
    'AG': 'AI Governance',
    'RC': 'Risk & Compliance',
    'RM': 'Risk Management',
    'LS': 'Leadership & Strategy',
    'OP': 'Operations & Program Management',
    'AB': 'Analytics & BI',
}

# ── Per-role configuration ─────────────────────────────────────────────────────
# tier: exec / director / manager / mid / ic
# affinity: 0.0–1.0 (how naturally does this domain map to this role)
ROLE_CONFIG = {
    'WIDAI-OPS-0125': {
        'name': 'Data and AI Program Manager',
        'tier': 'manager',
        'affinity': {
            'OP': 0.82, 'LS': 0.75, 'DG': 0.38, 'AG': 0.32, 'RM': 0.30,
            'RC': 0.27, 'AI': 0.28, 'SP': 0.22, 'TF': 0.18, 'DA': 0.15,
            'DQ': 0.12, 'AB': 0.13,
        },
        'scope_notes': (
            "Data and AI Program Manager — mid-to-senior manager. Core: program/project management "
            "of data/AI initiatives, stakeholder alignment, delivery governance, roadmap ownership, "
            "risk/issue management, budget oversight, cross-functional coordination, executive "
            "reporting, change management. Extends into LS (leadership) and DG (governance "
            "coordination). NOT enterprise strategy setter; NOT individual technical executor."
        ),
    },
    'WIDAI-OPS-0126': {
        'name': 'Data and AI Adoption Specialist',
        'tier': 'mid',
        'affinity': {
            'OP': 0.82, 'LS': 0.72, 'AI': 0.42, 'DG': 0.38, 'AB': 0.32,
            'TF': 0.25, 'DA': 0.18, 'DQ': 0.20, 'AG': 0.28, 'RM': 0.18,
            'RC': 0.15, 'SP': 0.12,
        },
        'scope_notes': (
            "Data and AI Adoption Specialist — IC to mid-level. Core: driving adoption of data/AI "
            "tools, measuring adoption, managing behavioral change, removing adoption barriers, "
            "developing communication plans, enablement programs, user engagement. Extends into LS "
            "for change management framing. NOT primary trainer; NOT program manager; NOT technical "
            "implementer."
        ),
    },
    'WIDAI-OPS-0127': {
        'name': 'Data and AI Literacy Trainer',
        'tier': 'mid',
        'affinity': {
            'OP': 0.80, 'LS': 0.65, 'AI': 0.48, 'DG': 0.38, 'AB': 0.35,
            'TF': 0.32, 'DA': 0.18, 'DQ': 0.20, 'AG': 0.32, 'RM': 0.15,
            'RC': 0.12, 'SP': 0.12,
        },
        'scope_notes': (
            "Data and AI Literacy Trainer — mid-level. Core: designing and delivering training on "
            "data literacy and AI concepts, curriculum development, facilitation, learning design, "
            "workshop delivery, competency assessment. Extends into LS for instructional strategy. "
            "NOT change manager; NOT AI engineer; NOT technical implementer."
        ),
    },
    'WIDAI-OPS-0128': {
        'name': 'Data Operations Specialist',
        'tier': 'mid',
        'affinity': {
            'OP': 0.82, 'TF': 0.72, 'DQ': 0.72, 'DA': 0.55, 'AI': 0.35,
            'DG': 0.42, 'LS': 0.18, 'AB': 0.28, 'AG': 0.18, 'RM': 0.22,
            'RC': 0.15, 'SP': 0.22,
        },
        'scope_notes': (
            "Data Operations Specialist — mid-level. Core: day-to-day data pipeline operations, "
            "ETL/ELT management, data quality monitoring and validation, pipeline maintenance, "
            "incident triage, SLA tracking, data workflow orchestration. Primary technical executor "
            "of data engineering operations. NOT data architect; NOT data scientist."
        ),
    },
    'WIDAI-OPS-0129': {
        'name': 'Analytics Translator',
        'tier': 'mid',
        'affinity': {
            'OP': 0.80, 'LS': 0.68, 'AB': 0.50, 'AI': 0.40, 'DG': 0.32,
            'TF': 0.30, 'DA': 0.35, 'DQ': 0.28, 'AG': 0.25, 'RM': 0.22,
            'RC': 0.15, 'SP': 0.12,
        },
        'scope_notes': (
            "Analytics Translator — mid-to-senior. Core: bridging technical analytics/data science "
            "teams and business stakeholders, translating data insights into business decisions, "
            "framing business problems as analytical questions, communicating data narratives, "
            "enabling self-service analytics. NOT primary analyst; NOT decision-maker."
        ),
    },
    'WIDAI-OPS-0130': {
        'name': 'Data Evangelist',
        'tier': 'mid',
        'affinity': {
            'OP': 0.80, 'LS': 0.70, 'AB': 0.50, 'AI': 0.42, 'DG': 0.38,
            'TF': 0.25, 'DA': 0.20, 'DQ': 0.22, 'AG': 0.30, 'RM': 0.15,
            'RC': 0.12, 'SP': 0.12,
        },
        'scope_notes': (
            "Data Evangelist — mid-level. Core: internal advocacy for data-driven culture, "
            "promoting data literacy and adoption, building data communities, championing data use "
            "across business units, creating awareness campaigns, storytelling with data. "
            "NOT governance role; NOT technical executor."
        ),
    },
    'WIDAI-OPS-0131': {
        'name': 'AI Adoption / Change Manager',
        'tier': 'manager',
        'affinity': {
            'OP': 0.82, 'LS': 0.78, 'AI': 0.45, 'DG': 0.38, 'AG': 0.35,
            'AB': 0.28, 'TF': 0.22, 'DA': 0.18, 'DQ': 0.15, 'RM': 0.28,
            'RC': 0.18, 'SP': 0.15,
        },
        'scope_notes': (
            "AI Adoption / Change Manager — manager-level. Core: managing organizational change "
            "programs for AI adoption, change readiness assessment, stakeholder engagement and "
            "communication planning, change champion networks, measuring adoption outcomes, "
            "removing organizational barriers to AI use. NOT enterprise strategy setter."
        ),
    },
    'WIDAI-OPS-0132': {
        'name': 'Citizen Data Steward',
        'tier': 'ic',
        'affinity': {
            'OP': 0.78, 'DG': 0.72, 'DQ': 0.65, 'AB': 0.38, 'TF': 0.30,
            'DA': 0.28, 'LS': 0.20, 'AI': 0.22, 'AG': 0.25, 'RM': 0.18,
            'RC': 0.20, 'SP': 0.18,
        },
        'scope_notes': (
            "Citizen Data Steward — IC (business). Core: decentralized data stewardship at business "
            "unit level, data quality monitoring for owned datasets, applying governance policies, "
            "maintaining data definitions and documentation, flagging data issues. "
            "NOT governance program manager; NOT data architect."
        ),
    },
    'WIDAI-OPS-0133': {
        'name': 'AI Trainer',
        'tier': 'ic',
        'affinity': {
            'OP': 0.72, 'AI': 0.78, 'TF': 0.48, 'DQ': 0.42, 'DA': 0.28,
            'DG': 0.30, 'LS': 0.15, 'AB': 0.25, 'AG': 0.35, 'RM': 0.18,
            'RC': 0.15, 'SP': 0.15,
        },
        'scope_notes': (
            "AI Trainer — IC to mid-level. Core: training and fine-tuning AI/ML models, data "
            "annotation and labeling, RLHF/human feedback collection, prompt engineering for model "
            "training, evaluation dataset curation, model calibration support. "
            "NOT ML engineer; NOT model architect."
        ),
    },
    'WIDAI-OPS-0134': {
        'name': 'Data Mesh Enabling Team Coach',
        'tier': 'mid',
        'affinity': {
            'OP': 0.80, 'DA': 0.55, 'DG': 0.55, 'TF': 0.52, 'DQ': 0.50,
            'LS': 0.55, 'AI': 0.32, 'AB': 0.35, 'AG': 0.25, 'RM': 0.20,
            'RC': 0.15, 'SP': 0.20,
        },
        'scope_notes': (
            "Data Mesh Enabling Team Coach — mid-to-senior. Core: enabling domain teams to own and "
            "produce data products, coaching teams on data-as-a-product principles, facilitating "
            "federated data governance, data mesh architecture enablement, self-serve data "
            "infrastructure guidance. NOT data architect (primary); NOT governance manager."
        ),
    },
    'WIDAI-OPS-0135': {
        'name': 'AI Solutions Engineer',
        'tier': 'mid',
        'affinity': {
            'TF': 0.82, 'AI': 0.82, 'OP': 0.50, 'DA': 0.52, 'DQ': 0.35,
            'DG': 0.30, 'LS': 0.22, 'AB': 0.35, 'AG': 0.30, 'RM': 0.25,
            'RC': 0.18, 'SP': 0.35,
        },
        'scope_notes': (
            "AI Solutions Engineer — mid-to-senior. Core: designing and building AI-powered "
            "solutions, integrating AI models into products/workflows, MLOps, LLM application "
            "development, prompt engineering, RAG pipelines, API development, customer-facing "
            "AI solution deployment. Primarily technical executor."
        ),
    },
    'WIDAI-OPS-0136': {
        'name': 'AI Supervisor / Agent Coordinator',
        'tier': 'manager',
        'affinity': {
            'AI': 0.82, 'OP': 0.55, 'LS': 0.55, 'TF': 0.25, 'AG': 0.25,
            'DG': 0.20, 'DQ': 0.28, 'DA': 0.20, 'AB': 0.30, 'RM': 0.35,
            'RC': 0.25, 'SP': 0.30,
        },
        'scope_notes': (
            "AI Supervisor / Agent Coordinator — manager-level. Core: supervising AI agent systems "
            "and multi-agent workflows, defining escalation protocols, human-in-the-loop oversight, "
            "coordinating agent task routing and handoffs, monitoring agentic system performance. "
            "NOT enterprise AI strategist; NOT model developer (primary)."
        ),
    },
    'WIDAI-OPS-0137': {
        'name': 'Forward-Deployed Engineer',
        'tier': 'mid',
        'affinity': {
            'TF': 0.82, 'OP': 0.50, 'AI': 0.62, 'DA': 0.48, 'DQ': 0.35,
            'DG': 0.22, 'LS': 0.28, 'AB': 0.32, 'AG': 0.22, 'RM': 0.25,
            'RC': 0.15, 'SP': 0.30,
        },
        'scope_notes': (
            "Forward-Deployed Engineer — mid-to-senior. Core: on-site customer implementation, "
            "integrating AI/data solutions into customer environments, customer-facing technical "
            "problem solving, deployment and integration support, rapid prototyping for customers, "
            "feedback loop from deployment to product. Primarily technical executor."
        ),
    },
    'WIDAI-OPS-0138': {
        'name': 'AI UX Designer',
        'tier': 'mid',
        'affinity': {
            'TF': 0.78, 'AI': 0.72, 'OP': 0.50, 'SP': 0.45, 'AB': 0.40,
            'DG': 0.28, 'DA': 0.28, 'LS': 0.25, 'DQ': 0.22, 'AG': 0.22,
            'RM': 0.20, 'RC': 0.15,
        },
        'scope_notes': (
            "AI UX Designer — mid-to-senior. Core: designing AI-native user experiences, "
            "human-AI interaction design, user research for AI products, prototyping and testing AI "
            "interfaces, designing for transparency and trust in AI, accessibility in AI UX. "
            "NOT AI engineer; NOT product manager (primary)."
        ),
    },
    'WIDAI-OPS-0139': {
        'name': 'Conversational AI Designer',
        'tier': 'mid',
        'affinity': {
            'AI': 0.80, 'TF': 0.75, 'OP': 0.55, 'SP': 0.38, 'AB': 0.35,
            'DG': 0.25, 'DA': 0.22, 'LS': 0.22, 'DQ': 0.20, 'AG': 0.28,
            'RM': 0.18, 'RC': 0.15,
        },
        'scope_notes': (
            "Conversational AI Designer — mid-level. Core: designing conversational interfaces "
            "(chatbots, voice assistants, virtual agents), dialogue flow design, NLU/NLP integration, "
            "intent and entity design, persona development, usability testing for conversational "
            "systems. NOT NLP engineer; NOT backend developer."
        ),
    },
}

# ── OPS competency signals ─────────────────────────────────────────────────────
OPS_SIGNALS = [
    # Program / Project Management
    r'\bprogram.{0,15}(?:manage|plan|govern|roadmap|charter|deliverable|budget|oversight|office|lifecycle|kpi|metric|report)',
    r'\bproject.{0,15}(?:manage|plan|govern|charter|deliverable|budget|lifecycle|milestone|scope)',
    r'\bportfolio.{0,15}(?:manage|overview|dashboard|tracker|review|budget|govern|monitor)',
    r'\bstakeholder.{0,20}(?:manage|align|communicat|engag|report|present)',
    r'\bstakeholder',
    r'\bworkstream',
    r'\bmilestone',
    r'\bdeliverable',
    r'\bgovernance.{0,15}(?:model|structure|framework|process|review|checkpoint)',
    r'\brisk.{0,15}(?:log|register|manage|track|mitigation)',
    r'\bbudget.{0,20}(?:manage|oversee|track|forecast|request)',
    r'\bexecutive.{0,15}(?:report|present|brief|dashboard|communic)',
    r'\bchange.{0,10}manage',
    r'\borganizational.{0,20}(?:readiness|capabilit|culture|matur)',
    r'\bknowledge management',
    r'\bdata storytelling',
    r'\broadmap.{0,20}(?:develop|own|maintain|communicat)',
    r'\bprogram.{0,10}(?:status|health|oversight|report)',
    r'\bcross.functional\b',
    r'\binterdisciplinar',
    r'\bescalation.{0,15}(?:path|process|protocol)',
    r'\bdependenc',

    # Adoption / Enablement / Change Management
    r'\badopt',
    r'\benablement',
    r'\buser.{0,20}(?:engagement|experience|satisfaction|acceptance)',
    r'\bcommunication.{0,15}plan',
    r'\bbarrier.{0,15}(?:adopt|change|use)',
    r'\bchange.{0,10}(?:readiness|champion|network|agent)',
    r'\bchange.{0,10}(?:program|strateg)',
    r'\borganizational change\b',
    r'\bcultural change\b',
    r'\buser acceptance\b',
    r'\bbehavioral change\b',
    r'\badoption.{0,15}(?:metric|rate|barrier|driver|strategy|plan|roadmap)',
    r'\benablement.{0,15}(?:program|strategy|content|material)',
    r'\bdriving.{0,15}(?:adoption|change)',
    r'\bimpact.{0,15}assessment',

    # Training / Literacy / Facilitation
    r'\btraining.{0,20}(?:program|material|session|workshop|course|module|facilitat|design)',
    r'\bcurricul',
    r'\bliterac',
    r'\bworkshop',
    r'\blearning.{0,15}(?:objective|outcome|path|program|journey|design)',
    r'\bdata.{0,15}(?:literacy|skills|competency|training)',
    r'\bai.{0,15}(?:literacy|training|education|awareness)',
    r'\bcapacity.{0,15}(?:build|develop)',
    r'\bskills?.{0,10}development\b',
    r'\bfacilitat.{0,20}(?:session|workshop|training)',
    r'\binstruction.{0,10}design',
    r'\bonboarding.{0,15}(?:program|material|process|training)',
    r'\bknowledge transfer\b',
    r'\btraining.{0,15}(?:need|assessment|gap)',

    # Data Operations / Pipelines
    r'\bdata.{0,20}(?:pipeline|ingestion|flow|movement|transport)',
    r'\betl\b|extract.{0,10}transform.{0,10}load',
    r'\bdata.{0,15}(?:operation|ops|workflow|process)',
    r'\borchestrat',
    r'\bpipeline.{0,15}(?:monitor|maintain|design|build|develop|manage)',
    r'\bdata.{0,15}(?:schedule|batch|job|load|extract)',
    r'\bsla.{0,15}(?:monitor|manage|track)',
    r'\boperational.{0,15}(?:monitor|metric|kpi|dashboard)',
    r'\bdata.{0,15}integration\b',
    r'\bdata.{0,10}(?:warehouse|lake|lakehouse).{0,15}(?:operation|manage|maintain)',
    r'\bdata.{0,15}(?:freshness|latency|availability)',
    r'\bincident.{0,20}(?:response|manag|escalat|triage)',

    # Analytics Communication / Translation
    r'\banalytics.{0,20}(?:translat|communicat|present|insight|story)',
    r'\bdata.{0,20}translat',
    r'\binsight.{0,20}(?:communicat|deliver|present|translat)',
    r'\bdata.{0,20}(?:driven|inform).{0,20}(?:decision|recommend)',
    r'\bself.serv.{0,15}(?:analytics|BI|reporting)',
    r'\bbusiness.{0,15}(?:requirement|need|problem|objective).{0,20}(?:translat|understand|elicit)',
    r'\bvisualiz',

    # Data Evangelism / Culture
    r'\bdata.{0,15}(?:culture|mindset|champion|advocacy|evangel)',
    r'\bevangel',
    r'\badvoca',
    r'\bdata.driven.{0,15}(?:culture|decision|approach|mindset)',
    r'\bdata.{0,15}(?:awareness|promot)',
    r'\bcommunity.{0,15}(?:build|manage|develop|foster)',
    r'\bchampion',

    # Data Mesh / Data Products
    r'\bdata mesh\b',
    r'\bdata.{0,15}product.{0,20}(?:owner|manage|develop|design|build|think)',
    r'\bdomain.{0,15}(?:team|owner|data|product)',
    r'\bfederat.{0,20}(?:governance|data|model)',
    r'\bdata.{0,15}as.{0,15}a.{0,15}product\b',
    r'\bself.serv.{0,15}(?:data|infrastructure)',
    r'\bdata.{0,15}contract',
    r'\bdata.{0,15}(?:discoverability|discoverab)',
    r'\bcoach.{0,20}(?:team|domain|data)',
    r'\bcenter.{0,10}(?:of excellence|of expertise)',
    r'\bcoe\b',

    # AI Solutions Engineering
    r'\bai.{0,15}(?:solution|application|system|deployment|implementation)',
    r'\bml.{0,15}(?:model|pipeline|deployment|solution)',
    r'\bmodel.{0,15}(?:deploy|serve|inference|productioniz)',
    r'\bmlops\b',
    r'\bllm.{0,15}(?:application|deployment|solution|fine.tun)',
    r'\bfine.tun',
    r'\bprompt.{0,10}engineer',
    r'\brag\b|retrieval.{0,10}augmented',
    r'\btechnical.{0,15}(?:solutio|implement|design)',
    r'\bprototype.{0,20}(?:develop|build|design)',
    r'\bintegrat.{0,20}(?:solution|system|api|data)',
    r'\bapi.{0,20}(?:design|develop|integrat|build)',

    # AI Agent Coordination
    r'\bagent.{0,20}(?:coordinat|orchestrat|supervise|manage)',
    r'\bmulti.agent',
    r'\bagentic',
    r'\bai.{0,15}(?:agent|assistant|bot).{0,20}(?:manage|deploy|coordinat|supervise)',
    r'\bhuman.{0,15}(?:oversight|in.the.loop|review)',
    r'\bworkflow.{0,20}(?:automat|orchestrat|design)',
    r'\bprocess.{0,20}automat',

    # AI Training / Annotation
    r'\bannotat',
    r'\bdata.{0,15}label',
    r'\brlhf\b',
    r'\breinforcement.{0,15}(?:learn|feedback)',
    r'\bhuman.{0,15}feedback',
    r'\bmodel.{0,15}(?:train|fine.tun|calibrat)',
    r'\btraining.{0,15}(?:data|dataset|sample)',
    r'\bground.{0,10}truth',
    r'\bdata.{0,15}(?:collection|curati|sampling)',

    # UX / Conversational Design
    r'\bux.{0,15}(?:design|research|testing)',
    r'\buser.{0,15}(?:research|testing|interview|persona|journey)',
    r'\bconversational.{0,15}(?:design|ai|interface|flow)',
    r'\bdialogue.{0,15}(?:design|flow|management)',
    r'\bchatbot\b',
    r'\bvirtual.{0,10}(?:agent|assistant)',
    r'\bvoice.{0,15}(?:design|interface|ux)',
    r'\bnlu\b|natural.{0,10}language.{0,10}understanding',
    r'\bnlp\b|natural.{0,10}language.{0,10}processing',
    r'\bintent.{0,15}(?:design|classification|recognit)',
    r'\bentity.{0,15}(?:design|extract|recognit)',
    r'\bhuman.centered.{0,10}design\b',
    r'\bdesign.{0,15}(?:thinking|sprint|prototype)',
    r'\bwireframe\b',
    r'\busability.{0,15}(?:test|study)',

    # Common cross-role signals
    r'\bdata.{0,20}(?:and|&).{0,20}ai.{0,20}(?:adopt|initiat|program|tool)',
    r'\bai.{0,20}(?:adopt|initiat|program|transformation)',
    r'\bscaling.{0,20}(?:data|ai|adoption)',
    r'\baccelerator',
]

# ── Seniority exclusion signals ────────────────────────────────────────────────
EXEC_SIGNALS = [
    r'\bboard of director',
    r'\breport.{0,10}board\b',
    r'\bpresent.{0,15}(?:to\s+)?(?:the\s+)?board\b',
    r'\bm\s*&\s*a\b|merger.{0,15}acquisition',
    r'\bset.{0,10}enterprise.{0,10}strateg',
    r'\boperating model.{0,15}(?:redesign|transform)',
    r'\borganizational design\b',
    r'\bhiring authority\b',
    r'\bheadcount.{0,15}(?:decision|approv)',
    r'\bcapital.{0,15}alloc.{0,20}(?:strateg|decision)',
    r'\bappoint.{0,10}(?:cdo|caio|ciso|cto|cfo)',
]

IC_QUALIFIERS = [
    r'\bimplement',
    r'\bapply\b',
    r'\bexecut',
    r'\bsupport\b',
    r'\bcontribut',
    r'\bparticipat',
    r'\bfollow\b',
    r'\badhere',
    r'\bcomply',
    r'\bunder.{0,15}guidance',
    r'\bin accordance with',
]

# ── External evidence signals ──────────────────────────────────────────────────
CERT_SIGNALS = [
    # General data/AI certs
    r'\bcdmp\b', r'\bdama\b', r'\bdata management\b',
    r'\bprosci\b', r'\bchange management.{0,15}(?:certif|professional)',
    r'\bpmp\b', r'\bpmi\b', r'\bscrum master\b', r'\bsafe\b', r'\bagile',
    r'\baws.{0,10}(?:certif|solution)', r'\bazure.{0,10}certif', r'\bgcp.{0,10}certif',
    r'\bpython\b', r'\bsql\b', r'\bspark\b', r'\bkafka\b',
    r'\bai literacy\b', r'\bresponsible ai\b',
    r'\bnist.{0,5}ai\b', r'\biso.{0,5}42001\b',
    r'\bux.{0,10}(?:certif|professional)',
    r'\bhci\b',
]

JOB_POSTING_SIGNALS = [
    r'\bstakeholder\b', r'\bprogram\b', r'\bproject\b', r'\badoption\b',
    r'\benablement\b', r'\bchange management\b', r'\btraining\b', r'\bliteracy\b',
    r'\bworkshop\b', r'\bfacilitat', r'\banalytics\b', r'\bdata pipeline\b',
    r'\betl\b', r'\borchestrat', r'\bannotat', r'\brlhf\b', r'\bfine.tun',
    r'\bprompt', r'\bllm\b', r'\brag\b', r'\bmlops\b',
    r'\bagent\b', r'\bchatbot\b', r'\bconversational\b', r'\bdialogue\b',
    r'\bnlp\b', r'\bnlu\b', r'\bux\b', r'\buser research\b',
    r'\bdata mesh\b', r'\bdata product\b', r'\bcoach\b',
    r'\badvocacy\b', r'\bevangel', r'\bchampion\b', r'\bculture\b',
    r'\bincident\b', r'\bmonitoring\b', r'\bpipeline\b', r'\bsla\b',
    r'\bintegrat', r'\bdeploy', r'\bprototype\b', r'\bapi\b',
]

# ── Helpers ────────────────────────────────────────────────────────────────────
def match_patterns(patterns, text):
    return [p for p in patterns if re.search(p, text)]

def score_text(patterns, text):
    return len(match_patterns(patterns, text))

def clean_pat(p):
    return re.sub(r'\\b|\.{0,\d+}|\[.+?\]|\(|\)|\+|\?|\\', ' ', p).strip()[:60]

# ── Pass 2: Scope check ────────────────────────────────────────────────────────
def p2_scope(text, domain, composite, affinity):
    ops_hits  = match_patterns(OPS_SIGNALS, text)
    count     = len(ops_hits)
    aff       = affinity.get(domain, 0.10)

    if count >= 5:
        return 'in_scope', count, ops_hits
    if count >= 3 and aff >= 0.25:
        return 'in_scope', count, ops_hits
    if count >= 2 and aff >= 0.55:
        return 'in_scope', count, ops_hits
    if count >= 1 and aff >= 0.60:          # threshold fixed from 0.72 → 0.60
        return 'in_scope', count, ops_hits
    # edge case
    if count >= 2 and aff >= 0.25:
        return 'edge_case', count, ops_hits
    if count >= 1 and aff >= 0.28:
        return 'edge_case', count, ops_hits
    if count == 0 and aff >= 0.82:
        return 'edge_case', 0, []
    return 'out_of_scope', count, ops_hits

# ── Pass 2: Seniority check ────────────────────────────────────────────────────
def p2_seniority(text, domain, tier):
    exec_hits = match_patterns(EXEC_SIGNALS, text)
    ic_hits   = match_patterns(IC_QUALIFIERS, text)

    if tier == 'ic':
        if exec_hits and len(ic_hits) < 2:
            return 'too_senior', exec_hits[:2]
        if len(exec_hits) >= 2:
            return 'too_senior', exec_hits[:2]
    elif tier == 'mid':
        if len(exec_hits) >= 2 and len(ic_hits) < 2:
            return 'too_senior', exec_hits[:2]
        board_ma = [h for h in exec_hits
                    if re.search(r'board|m\s*&\s*a|merger', h)]
        if board_ma and not ic_hits:
            return 'too_senior', board_ma[:2]
    elif tier == 'manager':
        board_ma = [h for h in exec_hits
                    if re.search(r'board of director|m\s*&\s*a|merger', h)]
        if board_ma and not ic_hits:
            return 'too_senior', board_ma[:1]
    # director and exec tiers: no exclusions in OPS

    return 'appropriate', []

# ── Pass 2: Decision ───────────────────────────────────────────────────────────
def p2_decision(scope_fit, seniority_fit, domain, count, composite, affinity):
    aff = affinity.get(domain, 0.10)
    if seniority_fit == 'too_senior':
        return 'exclude'
    if scope_fit == 'out_of_scope':
        return 'exclude'
    if scope_fit == 'in_scope':
        return 'include'
    # edge_case
    if count >= 4:
        return 'include'
    if count >= 3 and aff >= 0.28:
        return 'include'
    if count >= 2 and aff >= 0.55:
        return 'include'
    if count >= 1 and aff >= 0.60:          # threshold fixed from 0.72 → 0.60
        return 'include'
    return 'exclude'

# ── Pass 2: Rationale ─────────────────────────────────────────────────────────
def p2_rationale(ksa_id, text_raw, domain, dimension, scope_fit, seniority_fit,
                 decision, ops_hits, exec_hits, composite, affinity, tier, role_name):
    aff    = affinity.get(domain, 0.10)
    dlabel = DOMAIN_LABELS.get(domain, domain)
    dim    = dimension.lower()

    if composite >= 0.42:
        sdesc = f"strong ({composite:.4f})"
    elif composite >= 0.35:
        sdesc = f"moderate ({composite:.4f})"
    elif composite >= 0.15:
        sdesc = f"low ({composite:.4f})"
    else:
        sdesc = f"minimal ({composite:.4f})"

    tier_label = {
        'exec': 'executive', 'director': 'director', 'manager': 'manager',
        'mid': 'mid-level professional', 'ic': 'IC practitioner'
    }.get(tier, tier)

    if seniority_fit == 'too_senior':
        sig = clean_pat(exec_hits[0]) if exec_hits else 'above-role-tier scope'
        return (
            f"Excluded on seniority: the {dim} contains scope signals (\"{sig}\") that exceed "
            f"the {tier_label} {role_name} tier. STRM: {sdesc}."
        )
    if scope_fit == 'in_scope' and decision == 'include':
        top = list(dict.fromkeys(clean_pat(h) for h in ops_hits[:4]))[:3]
        sig_str = ', '.join(f'"{s}"' for s in top) if top else 'OPS-domain vocabulary'
        return (
            f"Included: {dim} maps to {role_name} scope — role signals ({sig_str}). "
            f"STRM: {sdesc}. Domain {dlabel} (affinity {aff:.2f}), seniority appropriate."
        )
    if scope_fit == 'out_of_scope' and decision == 'exclude':
        snippet = text_raw[:80] + '...' if len(text_raw) > 80 else text_raw
        return (
            f"Excluded on scope: {dlabel} (affinity {aff:.2f}) — "
            f"\"{snippet}\" — no role signals. STRM: {sdesc}."
        )
    # edge_case
    if decision == 'include':
        sig_str = (', '.join(f'"{clean_pat(h)}"' for h in ops_hits[:2])
                   if ops_hits else 'domain context and affinity')
        return (
            f"Edge case — included: {dim} in {dlabel} (affinity {aff:.2f}); "
            f"role signals ({sig_str}). STRM: {sdesc}."
        )
    else:
        reason = 'insufficient signal match for domain affinity' if ops_hits else 'no role signals and low domain affinity'
        return (
            f"Edge case — excluded: {dim} in {dlabel} (affinity {aff:.2f}); "
            f"{reason}. STRM: {sdesc}."
        )

# ── Pass 3: Internal Consistency ──────────────────────────────────────────────
def p3_evaluate(p2_dec, scope_fit, seniority_fit, domain, count, composite, affinity):
    aff    = affinity.get(domain, 0.10)
    dlabel = DOMAIN_LABELS.get(domain, domain)

    if p2_dec == 'include':
        # Challenge: very low affinity + zero role signals
        if aff <= 0.15 and count == 0:
            challenge = (
                f"Consistency check: {dlabel} has very low OPS affinity ({aff:.2f}) and zero "
                f"role-specific signals. Other {domain} KSAs without OPS signals have been excluded."
            )
            rebuttal = (
                f"Challenge sustained. Zero OPS signals in a very low-affinity domain ({aff:.2f}) "
                f"is inconsistent with the applied scope boundary. Reversed to exclude."
            )
            return 'overturned', challenge, rebuttal, 'exclude'

        if aff < 0.22 and count == 0 and composite < 0.12 and scope_fit == 'edge_case':
            challenge = (
                f"Consistency check: edge-case inclusion from {dlabel} (affinity {aff:.2f}) "
                f"with no OPS signals and minimal composite ({composite:.4f})."
            )
            rebuttal = "Challenge sustained. Edge case with zero signals and low affinity reversed."
            return 'overturned', challenge, rebuttal, 'exclude'

    if p2_dec == 'exclude' and seniority_fit == 'appropriate':
        if aff >= 0.65 and count >= 3 and scope_fit != 'out_of_scope':
            challenge = (
                f"Consistency check: {dlabel} has high OPS affinity ({aff:.2f}) and {count} "
                f"role signals. Similar KSAs from this domain were included."
            )
            rebuttal = "Challenge sustained. High affinity + multiple signals warrants inclusion."
            return 'overturned', challenge, rebuttal, 'include'

    return 'upheld', None, None, p2_dec

# ── Pass 4: External Ground Truth ─────────────────────────────────────────────
def p4_evaluate(p3_ruling, domain, count, text, composite, affinity, role_name):
    aff          = affinity.get(domain, 0.10)
    dlabel       = DOMAIN_LABELS.get(domain, domain)
    cert_score   = score_text(CERT_SIGNALS, text)
    post_score   = score_text(JOB_POSTING_SIGNALS, text)
    ext_total    = cert_score + post_score

    if p3_ruling == 'include':
        if ext_total >= 3:
            evidence = (
                f"External strong: {post_score} job-posting + {cert_score} cert matches for "
                f"{role_name} role."
            )
            return 'upheld', None, evidence, 'include'
        elif ext_total >= 1:
            evidence = (
                f"External present: {ext_total} match(es) — sufficient to uphold for {role_name}."
            )
            return 'upheld', None, evidence, 'include'
        else:
            challenge = (
                f"External check: 0 job-posting or cert matches. Required for {role_name}?"
            )
            if aff < 0.22 and count == 0:
                evidence = (
                    f"Challenge upheld: zero external signals + low affinity ({aff:.2f}) + "
                    f"no OPS vocabulary. Reversed to exclude."
                )
                return 'overturned', challenge, evidence, 'exclude'
            else:
                evidence = (
                    f"Challenge answered: OPS competency implicit in {role_name} practice "
                    f"(domain affinity {aff:.2f}, {count} signal(s)). Framework vocabulary "
                    f"underrepresents many operational competencies."
                )
                return 'upheld', challenge, evidence, 'include'
    else:  # exclude
        if ext_total >= 5 and aff >= 0.45:
            challenge = (
                f"External check: {ext_total} matches in job postings/certs for "
                f"{dlabel} KSA (affinity {aff:.2f}). Gap noticeable for {role_name}?"
            )
            evidence = (
                f"Market signals present ({ext_total} matches) but exclusion stands on scope "
                f"boundary. Market presence alone does not override role-level scope for {role_name}."
            )
            return 'upheld', challenge, evidence, 'exclude'
        else:
            evidence = (
                f"External confirms exclusion: {ext_total} match(es). Gap not material to "
                f"{role_name}."
            )
            return 'upheld', None, evidence, 'exclude'

# ── Final decision ─────────────────────────────────────────────────────────────
def compute_final(p2_dec, p3_out, p3_rul, p4_out, p4_rul, p2_rat, p3_reb, p4_ev):
    p3_ov = (p3_out == 'overturned')
    p4_ov = (p4_out == 'overturned')
    disagreements = int(p3_ov) + int(p4_ov)
    if disagreements == 0:
        return p2_dec, 'high', 0, p2_rat
    elif disagreements == 1:
        final     = p3_rul if p3_ov else p4_rul
        over_text = p3_reb if p3_ov else p4_ev
        return final, 'medium', 1, f"Pass 2 overturned. {over_text}"
    else:
        final = 'exclude' if p2_dec == 'include' else 'include'
        return final, 'low', 2, f"Both adversarial passes overturned; decision reversed. {p4_ev}"

# ── Single KSA evaluation ──────────────────────────────────────────────────────
def evaluate_ksa(ksa, role_id, role_name, tier, affinity, pipeline_version='1.0'):
    ksa_id    = ksa['ksa_id']
    text_raw  = ksa['ksa_text']
    text      = text_raw.lower()
    domain    = ksa['ksa_domain']
    dimension = ksa['ksa_dimension']
    p1        = ksa['pass_1_scoring']
    composite = p1.get('composite_score', 0.0) or 0.0

    seniority, exec_hits           = p2_seniority(text, domain, tier)
    scope, count, ops_hits         = p2_scope(text, domain, composite, affinity)
    dec                            = p2_decision(scope, seniority, domain, count, composite, affinity)
    rat                            = p2_rationale(ksa_id, text_raw, domain, dimension, scope,
                                                   seniority, dec, ops_hits, exec_hits,
                                                   composite, affinity, tier, role_name)

    p3_out, p3_chal, p3_reb, p3_rul = p3_evaluate(
        dec, scope, seniority, domain, count, composite, affinity)
    p4_out, p4_chal, p4_ev, p4_rul  = p4_evaluate(
        p3_rul, domain, count, text, composite, affinity, role_name)

    final, confidence, disagreements, final_rat = compute_final(
        dec, p3_out, p3_rul, p4_out, p4_rul, rat, p3_reb, p4_ev)

    now = datetime.datetime.now(datetime.timezone.utc).isoformat()
    return {
        "schema_version":  "2.0",
        "role_id":         role_id,
        "role_name":       role_name,
        "ksa_id":          ksa_id,
        "ksa_text":        text_raw,
        "ksa_dimension":   dimension,
        "ksa_domain":      domain,
        "pass_1_scoring":  p1,
        "pass_2_evaluation": {
            "scope_fit":            scope,
            "seniority_fit":        seniority,
            "preliminary_decision": dec,
            "rationale":            rat,
        },
        "pass_3_adversarial_internal": {
            "outcome":  p3_out,
            "challenge": p3_chal,
            "rebuttal":  p3_reb,
            "ruling":    p3_rul,
        },
        "pass_4_adversarial_external": {
            "outcome":   p4_out,
            "challenge": p4_chal,
            "evidence":  p4_ev,
            "ruling":    p4_rul,
        },
        "final_decision":         final,
        "decision_confidence":    confidence,
        "decision_rationale":     final_rat,
        "adversarial_disagreements": disagreements,
        "metadata": {
            "evaluated_at":   now,
            "pipeline_version": pipeline_version,
        },
    }

# ── Stats accumulation ─────────────────────────────────────────────────────────
def _accum_stats(stats, art):
    fd   = art['final_decision']
    dom  = art['ksa_domain']
    dim  = art['ksa_dimension']
    comp = art['pass_1_scoring'].get('composite_score', 0.0) or 0.0
    conf = art.get('decision_confidence', 'high')
    dis  = art.get('adversarial_disagreements', 0)

    stats['included' if fd == 'include' else 'excluded'] += 1
    (stats['composite_included'] if fd == 'include' else stats['composite_excluded']).append(comp)
    domk = stats['domain'].setdefault(dom, {'include': 0, 'exclude': 0})
    domk[fd] = domk.get(fd, 0) + 1
    dimk = stats['dimension'].setdefault(dim, {'include': 0, 'exclude': 0})
    dimk[fd] = dimk.get(fd, 0) + 1
    stats['confidence'][conf] = stats['confidence'].get(conf, 0) + 1
    stats['disagreements'][dis] = stats['disagreements'].get(dis, 0) + 1

    p3 = art.get('pass_3_adversarial_internal', {})
    p4 = art.get('pass_4_adversarial_external', {})
    if p3.get('challenge'):      stats['p3_challenges'] += 1
    if p3.get('outcome') == 'overturned': stats['p3_overturns'] += 1
    if p4.get('challenge'):      stats['p4_challenges'] += 1
    if p4.get('outcome') == 'overturned': stats['p4_overturns'] += 1

# ── Write summary ──────────────────────────────────────────────────────────────
def _write_summary(stats, role_id, role_name, scope_notes, pipeline_version, summary_path):
    inc_s    = stats['composite_included']
    exc_s    = stats['composite_excluded']
    total    = stats['total']
    included = stats['included']
    cal_ok   = 80 <= included <= 160

    domain_summary = {}
    for dom, v in stats['domain'].items():
        domain_summary[dom] = {
            "include": v.get('include', 0),
            "exclude": v.get('exclude', 0),
            "total":   v.get('include', 0) + v.get('exclude', 0),
            "label":   DOMAIN_LABELS.get(dom, dom),
        }

    summary = {
        "schema_version":   "2.0",
        "role_id":          role_id,
        "role_name":        role_name,
        "pipeline_version": pipeline_version,
        "evaluated_at":     datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "total_ksas":       total,
        "included":         included,
        "excluded":         stats['excluded'],
        "inclusion_rate":   round(included / total, 4) if total else 0,
        "calibration": {
            "min":    80,
            "max":    160,
            "status": "ok" if cal_ok else "out_of_range",
        },
        "pass_1_notes":    "6 frameworks: dcwf, ddat, eu_ai_act, nice, nist_ai_rmf, onet.",
        "role_scope_notes": scope_notes,
        "domain_summary":   domain_summary,
    }

    tmp = summary_path + '.tmp'
    with open(tmp, 'w') as f:
        json.dump(summary, f, indent=2)
    os.rename(tmp, summary_path)

# ── Main evaluation entry point ────────────────────────────────────────────────
def run_evaluation(role_id, base_dir, pipeline_version='1.0'):
    cfg       = ROLE_CONFIG[role_id]
    role_name = cfg['name']
    tier      = cfg['tier']
    affinity  = cfg['affinity']
    scope_notes = cfg.get('scope_notes', '')

    input_path   = os.path.join(base_dir, role_id, 'pass1_batch.json')
    out_dir      = os.path.join(base_dir, role_id)
    summary_path = os.path.join(out_dir, 'summary.json')

    # Skip if valid summary exists
    if os.path.exists(summary_path):
        try:
            with open(summary_path) as f:
                s = json.load(f)
            cal = s.get('calibration', {})
            if cal.get('status') == 'ok':
                print(f"SKIP {role_id}: summary.json already valid "
                      f"({s.get('included', '?')} included, calibration ok).", flush=True)
                return
        except Exception:
            pass
        print(f"INFO {role_id}: existing summary invalid or out_of_range — rerunning.", flush=True)

    print(f"Loading {input_path} ...", flush=True)
    with open(input_path) as f:
        data = json.load(f)
    ksas  = data['scored_ksas']
    total = len(ksas)
    print(f"Loaded {total} KSAs for {role_name} (tier={tier}). Evaluating...", flush=True)

    stats = {
        'total': total, 'included': 0, 'excluded': 0,
        'domain': {d: {'include': 0, 'exclude': 0} for d in DOMAIN_LABELS},
        'dimension': {},
        'composite_included': [], 'composite_excluded': [],
        'p3_challenges': 0, 'p3_overturns': 0,
        'p4_challenges': 0, 'p4_overturns': 0,
        'confidence': {'high': 0, 'medium': 0, 'low': 0},
        'disagreements': {0: 0, 1: 0, 2: 0},
    }

    for i, ksa in enumerate(ksas):
        ksa_id   = ksa['ksa_id']
        out_path = os.path.join(out_dir, f'{ksa_id}.json')

        # Resumability — re-read and accumulate existing valid artifacts
        if os.path.exists(out_path):
            try:
                with open(out_path) as f:
                    art = json.load(f)
                # Accept artifact only if it was produced by this role
                if art.get('role_id') == role_id:
                    _accum_stats(stats, art)
                    if (i + 1) % 200 == 0:
                        print(f"  {i+1}/{total} (resuming)", flush=True)
                    continue
            except Exception:
                pass

        artifact = evaluate_ksa(ksa, role_id, role_name, tier, affinity, pipeline_version)
        _accum_stats(stats, artifact)

        tmp_path = out_path + '.tmp'
        with open(tmp_path, 'w') as f:
            json.dump(artifact, f, indent=2)
        os.rename(tmp_path, out_path)

        if (i + 1) % 100 == 0:
            pct = round(100 * (i + 1) / total, 1)
            print(
                f"  {i+1}/{total} ({pct}%) — "
                f"included:{stats['included']} excluded:{stats['excluded']}",
                flush=True
            )

    inc = stats['included']
    print(f"\nDone. Included: {inc}, Excluded: {stats['excluded']}", flush=True)
    cal_ok = 80 <= inc <= 160
    if not cal_ok:
        print(f"WARNING: {inc} included KSAs is outside 80–160 calibration range.", flush=True)
    else:
        print(f"Calibration OK: {inc} included (80–160 target).", flush=True)

    _write_summary(stats, role_id, role_name, scope_notes, pipeline_version, summary_path)
    print(f"Summary written to {summary_path}", flush=True)

    result = {
        'role_id':       role_id,
        'included':      inc,
        'excluded':      stats['excluded'],
        'rate':          round(inc / stats['total'], 3) if stats['total'] else 0,
        'calibration':   'ok' if cal_ok else 'out_of_range',
        'p3_overturns':  stats['p3_overturns'],
        'p4_overturns':  stats['p4_overturns'],
    }
    print(json.dumps(result))
    return result
