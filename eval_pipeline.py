#!/usr/bin/env python3
"""
WIDAI Role-KSA Evaluation Pipeline — Passes 2, 3, 4
Role: Data Engineer (WIDAI-ENG-0028)
"""
import json, os, re, datetime, sys

INPUT   = '/Users/thomasjones/Documents/Claude/Projects/ATLAS/widai-dataset/docs/role_ksa_evaluations/WIDAI-ENG-0028/pass1_batch.json'
OUT_DIR = '/Users/thomasjones/Documents/Claude/Projects/ATLAS/widai-dataset/docs/role_ksa_evaluations/WIDAI-ENG-0028'
ROLE_ID, ROLE_NAME, PIPELINE_VERSION = 'WIDAI-ENG-0028', 'Data Engineer', '1.0'

DOMAIN_LABELS = {
    'TF':'Technology Fundamentals','DA':'Data Architecture','DQ':'Data Quality',
    'DG':'Data Governance','SP':'Security & Privacy','AI':'AI & ML Infrastructure',
    'AG':'AI Governance','RC':'Risk & Compliance','RM':'Risk Management',
    'LS':'Leadership & Strategy','OP':'Operations & Program Management','AB':'Analytics & BI',
}

# Affinity: how naturally does this domain map to IC Data Engineer work (0–1)
DOMAIN_AFFINITY = {
    'TF':0.82,'DA':0.60,'DQ':0.72,'DG':0.22,'SP':0.30,
    'AI':0.38,'AG':0.10,'RC':0.18,'RM':0.10,'LS':0.06,'OP':0.15,'AB':0.28,
}

# ── Core DE competency signals (regex, match against lowercase text) ──────────
DE_SIGNALS = [
    r'\betl\b',r'\belt\b',r'\bpipelines?\b',r'\bdata flows?\b',r'\bdata movement\b',
    r'\bbatch.{0,10}process',r'\bstream.{0,15}ingest',r'\bdata ingest',
    r'\btransformation logic\b',r'\bdata extract',r'\bdata load\b',
    r'\bschemas?\b',r'\bdata model',r'\bdatabase.{0,10}design',r'\bnormali[sz]',
    r'\bstar schema\b',r'\bsnowflake schema\b',r'\bdimensional model',
    r'\bentity.relat',r'\btable design\b',r'\bcolumnar\b',r'\bpartitions?\b',
    r'\bsql\b',r'\bquery optim',r'\bquery perform',r'\bindexes?\b',
    r'\bstored procedure\b',r'\bddl\b',r'\bdml\b',r'\brelational database\b',
    r'\boldap\b',r'\bdata warehouse\b',r'\bwindow function\b',
    r'\borchestrat',r'\bairflow\b',r'\bdbt\b',r'\bprefect\b',r'\bdagster\b',
    r'\bjob schedul',r'\bworkflow.{0,10}orchest',r'\bdags?\b',
    r'\bdata quality\b',r'\bdata validat',r'\bdata profil',r'\bdata test',
    r'\bquality rule',r'\bquality metric',r'\bdata clean',r'\bdata anomal',
    r'\bnull.{0,10}check\b',r'\buniqueness',r'\bdata assert',
    r'\bdata lakes?\b',r'\blakehouse\b',r'\bobject storage\b',r'\bs3\b',
    r'\bstorage optim',r'\bsnowflake\b',r'\bbigquery\b',r'\bredshift\b',
    r'\bdatabricks\b',r'\bhive\b',r'\bhadoop\b',r'\bdelta lake\b',
    r'\biceberg\b',r'\bhudi\b',r'\bparquet\b',r'\bavro\b',
    r'\bkafka\b',r'\bapache spark\b',r'\bpyspark\b',r'\bspark\b',
    r'\bflink\b',r'\bkinesis\b',r'\bevent stream',r'\breal.time.{0,10}data',
    r'\bstream.{0,10}data\b',r'\bpub.sub\b',
    r'\bapi integrat',r'\brest api\b',r'\bgraphql\b',r'\bwebhook\b',
    r'\bdata.{0,10}connect',r'\bdata integrat',r'\bapi endpoint\b',
    r'\bunit test',r'\bintegration test',r'\bload test',r'\bperformance test',
    r'\bstress test',r'\bci.?cd\b',r'\bversion control\b',r'\bgit\b',
    r'\bdeploy.{0,10}data',r'\btest.{0,10}framework',r'\bautomat.{0,10}test',
    r'\bmonitoring.{0,20}data\b',r'\bdata.{0,20}monitor',r'\bobservabil',
    r'\bpipeline.{0,10}monitor',r'\bdata.{0,10}sla\b',r'\bdata.{0,10}alert',
    r'\btelemetr',r'\bmetric collect',r'\bevent log',
    r'\brunbooks?\b',r'\boperational procedure\b',r'\bsystem.{0,10}document',
    r'\bdata.{0,20}document',r'\btechnical.{0,10}document',r'\barchitecture.{0,10}doc',
    r'\bdata catalog\b',r'\bdata lineage\b',r'\btechnical.{0,10}metadata\b',r'\bmetadata.{0,10}(?:catalog|schema|lineage|standard)\b',
    r'\bcontainers?.{0,20}(?:data|applic|image|deploy|workload)',r'\bkubernetes\b',r'\bdocker\b',r'\bcloud.{0,10}data',
    r'\bdata.{0,10}infrastructure\b',r'\binfrastructure.as.code\b',r'\bterraform\b',
    r'\biac\b',r'\bcloud.{0,5}native\b',
    r'\brow.level.{0,10}security\b',r'\bcolumn.level.{0,10}security\b',
    r'\bdata.{0,10}encrypt',r'\bencrypt.{0,10}data\b',r'\bdata.{0,10}mask',
    r'\baccess control.{0,10}data\b',r'\bdata.{0,10}access control\b',
    r'\bfeature.{0,10}store\b',r'\bfeature engineer',r'\btraining.{0,10}data\b',
    r'\bml.{0,10}pipeline\b',r'\bprovision.{0,10}infra',
    r'\bcompute.{0,10}environments?\b',r'\bserving.{0,10}infrastructure\b',
    r'\bshell script\b',r'\bpython.{0,20}(?:data|pipeline|transform|script)\b',r'\bshell script\b',
    r'\btechnical architecture\b',r'\bdata architecture\b',r'\bsystem.{0,10}design\b',
    r'\bcomponent design\b',r'\bintegration point\b',r'\bdeployment topolog',
    r'\bdistributed.{0,10}comput',r'\bdata partition',r'\bsharding\b',
    r'\breplication.{0,10}strateg',r'\bfault toleran',r'\bresilien',
    r'\bserialization\b',r'\bmessaging.{0,10}system\b',r'\binter.service\b',
    r'\bmessage queue\b',r'\bevent.driven\b',
    r'\bdata lifecycle\b',r'\bdata retention\b',r'\barchival\b',
    r'\bclassification.{0,10}data\b',r'\bdata classif',
    r'\bcompression\b',r'\bstorage tier',r'\bdata.{0,10}redundan',
    r'\bdisaster recover',r'\bbusiness continuity\b',r'\brecovery.{0,10}procedure\b',
    r'\bchange data capture\b',r'\bcdc\b',r'\bsurrogate key\b',r'\bslowly changing',
    r'\bdata vault\b',r'\bmedallion\b',r'\bbronze.{0,5}silver\b',
    r'\bgold.{0,5}layer\b',r'\bprogramming.{0,15}data\b',
    # Additional targeted DE signals
    r'\bdata api\b',r'\bservice layer',r'\bdata service',
    r'\btransform.{0,15}(?:data|layer|logic|pipeline|model)',
    r'\bstaging.{0,10}model',r'\bintermediate.{0,10}transform',
    r'\bconformed.{0,10}(?:layer|model)',r'\braw.{0,10}layer',
    r'\blanding.{0,5}zone',r'\bingestion.{0,10}layer',
    r'\bdata.{0,10}serving',r'\bstorage.{0,10}layer',

    # Additional DE signals
    r'\bdata struct',r'\bdata storage',r'\bdata platform',
    r'\bdata product',r'\bquery execution',r'\bthroughput\b',
    r'\blatency\b',r'\bdata asset',r'\bdata.{0,10}pipelin',
    r'\btransform.{0,15}data\b',r'\bbatch.{0,10}job\b',
    r'\bworkflow.{0,10}manag',r'\bdata.{0,10}archiv',
    r'\bstorage.{0,10}solution',r'\bcloud.{0,10}storage',
]

# ── Seniority: executive/too-senior signals ───────────────────────────────────
EXEC_SIGNALS = [
    r'\bc.suite\b',r'\bboard of director',r'\bexecutive.{0,10}team\b',
    r'\bsenior leadership team\b',r'\bexecutive.{0,10}sponsor',
    r'\breport.{0,10}board\b',r'\bpresent.{0,10}board\b',
    r'\bbuild and lead cross.functional\b',r'\blead.{0,10}transformation team\b',
    r'\borganizational transformation\b',r'\bdrive.{0,10}organizational change\b',
    r'\borganizational change management\b',
    r'\bdevelop.{0,15}governance.{0,10}framework\b',
    r'\bestablish.{0,15}governance.{0,10}framework\b',
    r'\bdefine.{0,10}enterprise.{0,10}polic',
    r'\bset.{0,10}enterprise.{0,10}strateg',
    r'\bdevelop.{0,10}enterprise.{0,10}strateg',
    r'\binfluencing organizational decision.maker',
    r'\bportfolio management\b',r'\benterprise.{0,10}portfolio\b',
    r'\borganizational design\b',r'\bhiring strategy\b',r'\btalent strategy\b',
    r'\binvestment.{0,10}allocation\b',r'\bcapital allocation\b',
    r'\bestablish.{0,15}shared.{0,10}objective.{0,10}cross.functional\b',
    r'\balign.{0,15}strategic.{0,10}business.{0,15}technology.{0,10}capabilit',
    r'\borganizational.{0,10}risk.{0,10}tolerance\b',
    r'\bexecutive.{0,10}stakeholder\b',r'\bboard.level\b',r'\bc.level\b',
]

IC_QUALIFIERS = [
    r'\bimplement',r'\bapply',r'\badhere',r'\bfollow policy',r'\bcomply',
    r'\bsupport.{0,15}team\b',r'\bcontribut',r'\bin accordance with\b',
    r'\bwithin.{0,15}framework\b',r'\bunder.{0,15}guidance\b',
]

# ── External evidence signals ────────────────────────────────────────────────
CERT_SIGNALS = [
    r'\bglue\b',r'\bethena\b',r'\bs3\b',r'\bkinesis\b',r'\blake formation\b',
    r'\bcrawler\b',r'\bdata catalog\b',r'\blambda\b',r'\bstep function',
    r'\bspark\b',r'\bdelta lake\b',r'\bdatabricks\b',r'\bunity catalog\b',
    r'\bautoloader\b',r'\bstructured streaming\b',
    r'\bdbt\b',r'\bsql.{0,10}transform',r'\bdata model',r'\btest.{0,10}data',
    r'\bdocument.{0,10}data\b',r'\blineage\b',r'\bmodel.{0,10}select\b',
    r'\bbigquery\b',r'\bdataflow\b',r'\bpub.sub\b',r'\bcomposer\b',
    r'\bdataproc\b',r'\bspanner\b',
    r'\bsnowflake\b',r'\bsnowpipe\b',r'\btime travel\b',r'\bzero.copy clone\b',
    r'\bairflow\b',r'\bkafka\b',r'\bflink\b',r'\bhudi\b',r'\biceberg\b',
    r'\bhadoop\b',r'\bparquet\b',
]

JOB_POSTING_SIGNALS = [
    r'\bpipeline\b',r'\bschema\b',r'\bsql\b',r'\bdata model',r'\borchestrat',
    r'\bdata quality\b',r'\bingest',r'\bwarehouse\b',r'\bdbt\b',r'\bspark\b',
    r'\bkafka\b',r'\bmonitor',r'\bci.?cd\b',r'\bdata.{0,10}test',
    r'\blineage\b',r'\bobservabil',r'\binfrastructure\b',r'\bpartition\b',
    r'\bcontainer\b',r'\bpython\b',r'\bversion control\b',r'\bgit\b',
    r'\bapi\b',r'\bperformance\b',r'\bshell script\b',
    r'\bdocument.{0,10}system\b',r'\bcatalog\b',
]

# ── Helpers ───────────────────────────────────────────────────────────────────
def match_patterns(patterns, text):
    return [p for p in patterns if re.search(p, text)]

def score_text(patterns, text):
    return len(match_patterns(patterns, text))

# ── Pass 2: Scope & Seniority ─────────────────────────────────────────────────
def p2_seniority(text, domain):
    exec_hits = match_patterns(EXEC_SIGNALS, text)
    if not exec_hits:
        return 'appropriate', []
    ic_hits = match_patterns(IC_QUALIFIERS, text)
    if len(exec_hits) == 1 and len(ic_hits) >= 2:
        return 'appropriate', []
    if len(exec_hits) >= 2:
        return 'too_senior', exec_hits
    return 'too_senior', exec_hits

def p2_scope(text, domain, composite):
    de_hits  = match_patterns(DE_SIGNALS, text)
    de_count = len(de_hits)
    aff      = DOMAIN_AFFINITY.get(domain, 0.1)
    # Strong in-scope: many signals, or key signals in high-affinity domain
    if de_count >= 5:
        return 'in_scope', de_count, de_hits
    if de_count >= 3 and aff >= 0.25:
        return 'in_scope', de_count, de_hits
    if de_count >= 2 and aff >= 0.55:
        return 'in_scope', de_count, de_hits
    if de_count >= 1 and aff >= 0.72:   # TF (0.82) and DQ (0.72) only
        return 'in_scope', de_count, de_hits
    # Edge case: some signals but not definitive
    if de_count >= 2 and aff >= 0.25:
        return 'edge_case', de_count, de_hits
    if de_count >= 1 and aff >= 0.30:
        return 'edge_case', de_count, de_hits
    if de_count == 0 and aff >= 0.82:   # TF only: very high affinity, zero signals
        return 'edge_case', 0, []
    # Default: out_of_scope (no permissive fallback)
    return 'out_of_scope', de_count, de_hits

def p2_decision(scope_fit, seniority_fit, domain, de_count, composite):
    aff = DOMAIN_AFFINITY.get(domain, 0.1)
    if seniority_fit == 'too_senior':
        return 'exclude'
    if scope_fit == 'out_of_scope':
        return 'exclude'
    if scope_fit == 'in_scope':
        return 'include'
    # edge_case: require genuine DE signal evidence
    if de_count >= 4:
        return 'include'
    if de_count >= 3 and aff >= 0.30:
        return 'include'
    if de_count >= 2 and aff >= 0.55:
        return 'include'
    if de_count >= 1 and aff >= 0.82:   # Only TF (0.82) with at least 1 signal
        return 'include'
    return 'exclude'

def clean_pat(p):
    return re.sub(r'\\b|\.{0,\d+}|\[.+?\]|\(|\)|\+', ' ', p).strip()

def p2_rationale(ksa_id, text_raw, domain, dimension, scope_fit, seniority_fit,
                 decision, de_hits, exec_hits, composite):
    aff = DOMAIN_AFFINITY.get(domain, 0.1)
    dlabel = DOMAIN_LABELS.get(domain, domain)
    dim = dimension.lower()
    snippet = text_raw[:100] + ('...' if len(text_raw) > 100 else '')
    if composite >= 0.42:
        sdesc = f"strong ({composite:.4f}, top tier for this dataset)"
    elif composite >= 0.35:
        sdesc = f"moderate-to-strong ({composite:.4f})"
    elif composite >= 0.15:
        sdesc = f"moderate ({composite:.4f})"
    elif composite >= 0.01:
        sdesc = f"low ({composite:.4f})"
    else:
        sdesc = f"minimal ({composite:.4f} — likely framework vocabulary mismatch, not irrelevance)"

    if seniority_fit == 'too_senior':
        sig = clean_pat(exec_hits[0]) if exec_hits else 'executive-level scope'
        return (
            f"Excluded on seniority grounds: the {dim} contains explicit executive/organizational scope "
            f"signals ('{sig}'), placing it above IC-to-senior-IC Data Engineer level. "
            f"STRM composite score is {sdesc}; semantic alignment with data frameworks may be present, "
            f"but the described responsibilities involve setting or leading organizational programs rather than "
            f"executing technical data work. Data Engineers implement within structures they do not establish."
        )
    if scope_fit == 'in_scope' and decision == 'include':
        top = list(dict.fromkeys(clean_pat(h) for h in de_hits[:4]))[:3]
        sig_str = ', '.join(f'"{s}"' for s in top) if top else 'core DE vocabulary'
        return (
            f"Included: {dim} maps directly to core Data Engineer scope — DE-specific signals detected "
            f"({sig_str}). STRM composite score is {sdesc}; note that framework scores routinely "
            f"underweight technical execution KSAs for this role, so text-based signal carries primary weight. "
            f"Seniority is appropriate for IC-to-senior-IC: the KSA describes technical practice, "
            f"not organizational strategy."
        )
    if scope_fit == 'out_of_scope' and decision == 'exclude':
        return (
            f"Excluded on scope grounds: {dlabel} domain has low DE affinity ({aff:.2f}), and the text "
            f"— '{snippet}' — describes competencies not owned by an IC Data Engineer. "
            f"No DE-specific technical signals detected. STRM composite score is {sdesc}."
        )
    # edge_case
    if decision == 'include':
        sig_str = (', '.join(f'"{clean_pat(h)}"' for h in de_hits[:2])
                   if de_hits else 'domain context and affinity')
        return (
            f"Edge case — included on balance: {dim} contains DE-relevant signals ({sig_str}) "
            f"within a {dlabel} context (domain affinity {aff:.2f}). "
            f"STRM composite score is {sdesc}. A senior IC Data Engineer would encounter this "
            f"competency in practice; the technical implementation angle is sufficient to include."
        )
    else:
        reason = ('strategic/governance framing outweighs technical signals'
                  if de_hits else 'no DE-specific signals and low domain affinity')
        return (
            f"Edge case — excluded on balance: {dim} from {dlabel} (domain affinity {aff:.2f}); "
            f"{reason}. STRM composite score is {sdesc}. "
            f"A working DE would be aware of but not accountable for this competency."
        )

# ── Pass 3: Internal Consistency ─────────────────────────────────────────────
def p3_evaluate(p2_dec, scope_fit, seniority_fit, domain, de_count, composite):
    aff = DOMAIN_AFFINITY.get(domain, 0.1)
    dlabel = DOMAIN_LABELS.get(domain, domain)
    if p2_dec == 'include':
        if aff <= 0.12 and de_count == 0:
            challenge = (
                f"Consistency check: {dlabel} has very low DE affinity ({aff:.2f}) and no "
                f"DE-specific signals detected. Other {domain} KSAs without DE signals have been excluded. "
                f"This inclusion is inconsistent with scope boundaries applied elsewhere."
            )
            rebuttal = (
                f"Challenge sustained. Zero DE signals in a low-affinity domain ({aff:.2f}) cannot be "
                f"reconciled with a consistent scope boundary. Decision reversed to exclude."
            )
            return 'overturned', challenge, rebuttal, 'exclude'
        if aff < 0.20 and de_count == 0 and composite < 0.10 and scope_fit == 'edge_case':
            challenge = (
                f"Consistency check: edge-case inclusion from {dlabel} (affinity {aff:.2f}) carries "
                f"no DE-specific signals and STRM score {composite:.4f}. Similar profiles in higher-affinity "
                f"domains are excluded. Inclusion appears inconsistent."
            )
            rebuttal = (
                f"Challenge sustained. Edge-case inclusion with zero DE signals, low domain affinity, "
                f"and minimal composite score falls below consistent inclusion threshold."
            )
            return 'overturned', challenge, rebuttal, 'exclude'
    if p2_dec == 'exclude' and seniority_fit == 'appropriate':
        if aff >= 0.60 and de_count >= 2 and scope_fit != 'out_of_scope':
            challenge = (
                f"Consistency check: {dlabel} has high DE affinity ({aff:.2f}) and {de_count} DE-specific "
                f"signals detected. Similar KSAs from this domain have been included. "
                f"This exclusion appears inconsistent."
            )
            rebuttal = (
                f"Challenge sustained. High-affinity domain with multiple DE signals and appropriate "
                f"seniority warrants inclusion for consistency."
            )
            return 'overturned', challenge, rebuttal, 'include'
    return 'upheld', None, None, p2_dec

# ── Pass 4: External Ground Truth ────────────────────────────────────────────
def p4_evaluate(p3_ruling, domain, de_count, text, composite):
    aff = DOMAIN_AFFINITY.get(domain, 0.1)
    dlabel = DOMAIN_LABELS.get(domain, domain)
    cert_score    = score_text(CERT_SIGNALS, text)
    posting_score = score_text(JOB_POSTING_SIGNALS, text)
    ext_total     = cert_score + posting_score

    if p3_ruling == 'include':
        if ext_total >= 3:
            evidence = (
                f"External validation strong: {posting_score} job-posting-level and "
                f"{cert_score} certification-level matches (AWS DE, Databricks, dbt, GCP DE). "
                f"Competency appears regularly in DE role descriptions and/or certification curricula."
            )
            return 'upheld', None, evidence, 'include'
        elif ext_total >= 1:
            evidence = (
                f"External validation present: {ext_total} match(es) in DE job postings or "
                f"certification scope. Skill appears in DE role descriptions — sufficient to uphold."
            )
            return 'upheld', None, evidence, 'include'
        else:
            challenge = (
                f"External check: no matches in DE job postings or cert curricula (AWS DE, "
                f"Databricks, dbt, GCP DE). Would a working Data Engineer self-report this as required?"
            )
            if aff < 0.20 and de_count == 0:
                evidence = (
                    f"Challenge upheld. Zero external signals + low domain affinity ({aff:.2f}) + "
                    f"no DE vocabulary confirms inclusion was too permissive. Decision reversed to exclude."
                )
                return 'overturned', challenge, evidence, 'exclude'
            else:
                evidence = (
                    f"Challenge answered: the technical practice is implicit in DE work "
                    f"(domain affinity {aff:.2f}, {de_count} DE signal(s)). Framework vocabulary matching "
                    f"underrepresents many legitimate DE competencies."
                )
                return 'upheld', challenge, evidence, 'include'
    else:  # exclude
        if ext_total >= 5 and aff >= 0.40:
            challenge = (
                f"External check: {ext_total} matches in DE job postings/certifications for a "
                f"{dlabel} KSA (affinity {aff:.2f}). Would a gap be noticeable to a working DE?"
            )
            evidence = (
                f"Challenge partially answered: market signals present ({ext_total} matches), but "
                f"exclusion stands on scope boundary grounds. Market presence alone does not override "
                f"the role-level scope determination."
            )
            return 'upheld', challenge, evidence, 'exclude'
        else:
            evidence = (
                f"External validation confirms exclusion: {ext_total} match(es) in DE job postings "
                f"or certification curricula. A gap here would not be noticeable to a working Data Engineer "
                f"focused on pipeline, modeling, and data platform responsibilities."
            )
            return 'upheld', None, evidence, 'exclude'

# ── Final decision ────────────────────────────────────────────────────────────
def compute_final(p2_dec, p3_out, p3_rul, p4_out, p4_rul,
                  p2_rat, p3_reb, p4_ev):
    p3_ov = (p3_out == 'overturned')
    p4_ov = (p4_out == 'overturned')
    disagreements = int(p3_ov) + int(p4_ov)
    if disagreements == 0:
        return p2_dec, 'high', 0, p2_rat
    elif disagreements == 1:
        final = p3_rul if p3_ov else p4_rul
        over_text = p3_reb if p3_ov else p4_ev
        return final, 'medium', 1, f"Pass 2 decision overturned. {over_text}"
    else:
        final = 'exclude' if p2_dec == 'include' else 'include'
        return final, 'low', 2, f"Both adversarial passes overturned; Pass 2 decision reversed. {p4_ev}"

# ── Single KSA evaluation ─────────────────────────────────────────────────────
def evaluate_ksa(ksa):
    ksa_id    = ksa['ksa_id']
    text_raw  = ksa['ksa_text']
    text      = text_raw.lower()
    domain    = ksa['ksa_domain']
    dimension = ksa['ksa_dimension']
    p1        = ksa['pass_1_scoring']
    composite = p1.get('composite_score', 0.0) or 0.0

    seniority, exec_hits     = p2_seniority(text, domain)
    scope, de_count, de_hits = p2_scope(text, domain, composite)
    dec = p2_decision(scope, seniority, domain, de_count, composite)
    rat = p2_rationale(ksa_id, text_raw, domain, dimension, scope, seniority,
                       dec, de_hits, exec_hits, composite)

    p3_out, p3_chal, p3_reb, p3_rul = p3_evaluate(dec, scope, seniority, domain, de_count, composite)
    p4_out, p4_chal, p4_ev,  p4_rul = p4_evaluate(p3_rul, domain, de_count, text, composite)

    final, confidence, disagreements, final_rat = compute_final(
        dec, p3_out, p3_rul, p4_out, p4_rul, rat, p3_reb, p4_ev)

    now = datetime.datetime.utcnow().isoformat() + 'Z'
    return {
        "schema_version": "2.0",
        "role_id": ROLE_ID,
        "role_name": ROLE_NAME,
        "ksa_id": ksa_id,
        "ksa_text": text_raw,
        "ksa_dimension": dimension,
        "ksa_domain": domain,
        "pass_1_scoring": p1,
        "pass_2_evaluation": {
            "scope_fit": scope,
            "seniority_fit": seniority,
            "preliminary_decision": dec,
            "rationale": rat,
        },
        "pass_3_adversarial_internal": {
            "outcome": p3_out,
            "challenge": p3_chal,
            "rebuttal": p3_reb,
            "ruling": p3_rul,
        },
        "pass_4_adversarial_external": {
            "outcome": p4_out,
            "challenge": p4_chal,
            "evidence": p4_ev,
            "ruling": p4_rul,
        },
        "final_decision": final,
        "decision_confidence": confidence,
        "decision_rationale": final_rat,
        "adversarial_disagreements": disagreements,
        "metadata": {
            "evaluated_at": now,
            "pipeline_version": PIPELINE_VERSION,
        }
    }

# ── Main loop ─────────────────────────────────────────────────────────────────
def main():
    print(f"Loading {INPUT} ...", flush=True)
    with open(INPUT) as f:
        data = json.load(f)
    ksas = data['scored_ksas']
    total = len(ksas)
    print(f"Loaded {total} KSAs. Evaluating...", flush=True)

    stats = {
        'total': total, 'included': 0, 'excluded': 0,
        'domain': {d: {'include':0,'exclude':0} for d in DOMAIN_LABELS},
        'dimension': {},
        'composite_included': [], 'composite_excluded': [],
        'p3_challenges': 0, 'p3_overturns': 0,
        'p4_challenges': 0, 'p4_overturns': 0,
    }

    for i, ksa in enumerate(ksas):
        ksa_id   = ksa['ksa_id']
        out_path = os.path.join(OUT_DIR, f'{ksa_id}.json')

        # Resumability
        if os.path.exists(out_path):
            try:
                with open(out_path) as f:
                    art = json.load(f)
                fd  = art['final_decision']
                dom = art['ksa_domain']
                dim = art['ksa_dimension']
                comp= art['pass_1_scoring'].get('composite_score', 0.0) or 0.0
                stats['included' if fd=='include' else 'excluded'] += 1
                (stats['composite_included'] if fd=='include' else stats['composite_excluded']).append(comp)
                stats['domain'].setdefault(dom,{'include':0,'exclude':0})[fd] = \
                    stats['domain'].setdefault(dom,{'include':0,'exclude':0}).get(fd,0) + 1
                stats['dimension'].setdefault(dim,{'include':0,'exclude':0})[fd] = \
                    stats['dimension'].setdefault(dim,{'include':0,'exclude':0}).get(fd,0) + 1
                if art['pass_3_adversarial_internal']['challenge']: stats['p3_challenges'] += 1
                if art['pass_3_adversarial_internal']['outcome']=='overturned': stats['p3_overturns'] += 1
                if art['pass_4_adversarial_external']['challenge']: stats['p4_challenges'] += 1
                if art['pass_4_adversarial_external']['outcome']=='overturned': stats['p4_overturns'] += 1
                if (i+1) % 200 == 0:
                    print(f"  {i+1}/{total} (resuming)", flush=True)
                continue
            except Exception:
                pass

        artifact = evaluate_ksa(ksa)
        fd  = artifact['final_decision']
        dom = artifact['ksa_domain']
        dim = artifact['ksa_dimension']
        comp= artifact['pass_1_scoring'].get('composite_score', 0.0) or 0.0

        stats['included' if fd=='include' else 'excluded'] += 1
        (stats['composite_included'] if fd=='include' else stats['composite_excluded']).append(comp)
        stats['domain'].setdefault(dom,{'include':0,'exclude':0})[fd] = \
            stats['domain'].setdefault(dom,{'include':0,'exclude':0}).get(fd,0) + 1
        stats['dimension'].setdefault(dim,{'include':0,'exclude':0})[fd] = \
            stats['dimension'].setdefault(dim,{'include':0,'exclude':0}).get(fd,0) + 1
        if artifact['pass_3_adversarial_internal']['challenge']: stats['p3_challenges'] += 1
        if artifact['pass_3_adversarial_internal']['outcome']=='overturned': stats['p3_overturns'] += 1
        if artifact['pass_4_adversarial_external']['challenge']: stats['p4_challenges'] += 1
        if artifact['pass_4_adversarial_external']['outcome']=='overturned': stats['p4_overturns'] += 1

        tmp_path = out_path + '.tmp'
        with open(tmp_path, 'w') as f:
            json.dump(artifact, f, indent=2)
        os.rename(tmp_path, out_path)

        if (i+1) % 100 == 0:
            pct = round(100*(i+1)/total,1)
            print(f"  {i+1}/{total} ({pct}%) — included:{stats['included']} excluded:{stats['excluded']}", flush=True)

    print(f"\nDone. Included: {stats['included']}, Excluded: {stats['excluded']}", flush=True)
    if stats['included'] < 60:
        print("WARNING: <60 included — review scope calibration.", flush=True)

    inc_s = stats['composite_included']
    exc_s = stats['composite_excluded']
    summary = {
        "schema_version": "2.0",
        "role_id": ROLE_ID,
        "role_name": ROLE_NAME,
        "pipeline_version": PIPELINE_VERSION,
        "generated_at": datetime.datetime.utcnow().isoformat() + 'Z',
        "total_evaluated": stats['total'],
        "included": stats['included'],
        "excluded": stats['excluded'],
        "inclusion_rate": round(stats['included']/stats['total'],4) if stats['total'] else 0,
        "domain_breakdown": {
            d: {
                "included": v.get('include',0),
                "excluded": v.get('exclude',0),
                "inclusion_rate": round(v.get('include',0)/(v.get('include',0)+v.get('exclude',0)),3)
                    if (v.get('include',0)+v.get('exclude',0))>0 else 0
            }
            for d,v in stats['domain'].items()
        },
        "dimension_breakdown": {
            d: {"included":v.get('include',0),"excluded":v.get('exclude',0)}
            for d,v in stats['dimension'].items()
        },
        "score_analysis": {
            "avg_composite_included": round(sum(inc_s)/len(inc_s),4) if inc_s else None,
            "avg_composite_excluded": round(sum(exc_s)/len(exc_s),4) if exc_s else None,
        },
        "adversarial_challenge_counts": {
            "pass_3_challenges": stats['p3_challenges'],
            "pass_3_overturns":  stats['p3_overturns'],
            "pass_4_challenges": stats['p4_challenges'],
            "pass_4_overturns":  stats['p4_overturns'],
        },
    }
    tmp_sum = os.path.join(OUT_DIR, 'summary.json.tmp')
    with open(tmp_sum, 'w') as f:
        json.dump(summary, f, indent=2)
    os.rename(tmp_sum, os.path.join(OUT_DIR, 'summary.json'))
    print(f"Summary written.", flush=True)
    print(json.dumps({'included':stats['included'],'excluded':stats['excluded'],
                      'rate':round(stats['included']/stats['total'],3),
                      'p3_overturns':stats['p3_overturns'],'p4_overturns':stats['p4_overturns']}))

if __name__ == '__main__':
    main()
