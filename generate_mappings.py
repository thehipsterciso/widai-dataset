#!/usr/bin/env python3
"""
WIDAI Complete Role-KSA Mapping Generator v2.0
Generates all 10 role_ksa_*.json files with full coverage of 187 roles.
Each role undergoes 3 adversarial passes before finalization:
  Pass 1 — Coverage: ensure all required domains are represented
  Pass 2 — Relevance: remove any KSAs from blocked/peripheral domains
  Pass 3 — Depth: enforce correct proficiency_context for seniority level
"""
import json
import os

BASE = "/Users/thomasjones/Documents/Claude/Projects/ATLAS/widai-dataset"
MAPPINGS_DIR = os.path.join(BASE, "mappings")

# ====== SENIORITY → PROFICIENCY ======
SENIORITY_MAP = {
    'C-Suite': 'strategic', 'Executive': 'strategic', 'VP': 'strategic',
    'VP/Director': 'strategic', 'Director': 'strategic', 'Senior/Director': 'strategic',
    'Director/VP': 'strategic', 'Senior/VP': 'strategic', 'Senior/Executive': 'strategic',
    'Manager/Director': 'operational', 'Manager': 'operational', 'Manager+': 'operational',
    'Senior': 'operational', 'Mid–Senior': 'tactical', 'IC–Senior': 'tactical',
    'Mid-level IT': 'tactical', 'Mid': 'tactical', 'IC–Mid': 'tactical',
    'IC–Principal': 'tactical', 'Cross-functional': 'operational',
    'IC': 'foundational', 'IC (business)': 'foundational', 'Junior': 'foundational',
}

# ====== KSA LOADER ======
def load_all_ksas():
    domains = ['AB','AG','AI','DA','DG','DQ','LS','OP','RC','RM','SP','TF']
    dims = ['knowledge','skills','abilities','tasks']
    inv = {}
    for d in domains:
        inv[d] = {dim: [] for dim in dims}
        for dim in dims:
            with open(os.path.join(BASE, f'ksas/{d}_{dim}.json')) as f:
                inv[d][dim] = [e['ksa_id'] for e in json.load(f).get('entries', [])]
    return inv

# ====== ROLE PROFILES ======
# primary: 2 domains — core to the role (3K+3S+2T+1A each = 9 KSAs as 'requires')
# secondary: 2 domains — important (2K+2S+1T each = 5 KSAs as 'recommends')
# tertiary: 2 domains — useful awareness (1K+1S each = 2 KSAs as 'optional')
# blocked: domains explicitly excluded from this role's mapping
# Target: ~28-32 KSAs per role

ROLE_PROFILES = {
    # ===== LDR (31 roles) =====
    'WIDAI-LDR-0140': {'wr_id':'WR-LDR-08.01','primary':['LS','OP'],'secondary':['DG','AI'],'tertiary':['TF','RC'],'blocked':[]},
    'WIDAI-LDR-0141': {'wr_id':'WR-LDR-08.02','primary':['AI','TF'],'secondary':['AB','DA'],'tertiary':['LS','OP'],'blocked':['RC']},
    'WIDAI-LDR-0142': {'wr_id':'WR-LDR-08.03','primary':['AI','LS'],'secondary':['AB','AG'],'tertiary':['TF','OP'],'blocked':['RC']},
    'WIDAI-LDR-0143': {'wr_id':'WR-LDR-08.04','primary':['LS','DG'],'secondary':['AI','OP'],'tertiary':['RC','RM'],'blocked':['TF']},
    'WIDAI-LDR-0144': {'wr_id':'WR-LDR-08.05','primary':['LS','DA'],'secondary':['TF','OP'],'tertiary':['DG','DQ'],'blocked':['RC']},
    'WIDAI-LDR-0145': {'wr_id':'WR-LDR-08.06','primary':['LS','AI'],'secondary':['TF','DA'],'tertiary':['OP','DG'],'blocked':['RC']},
    'WIDAI-LDR-0146': {'wr_id':'WR-LDR-08.07','primary':['LS','DA'],'secondary':['AI','OP'],'tertiary':['DG','TF'],'blocked':['RC']},
    'WIDAI-LDR-0147': {'wr_id':'WR-LDR-08.08','primary':['LS','DG'],'secondary':['RC','RM'],'tertiary':['DA','DQ'],'blocked':['TF','AB']},
    'WIDAI-LDR-0148': {'wr_id':'WR-LDR-08.09','primary':['LS','AI'],'secondary':['AB','TF'],'tertiary':['DG','RM'],'blocked':['RC']},
    'WIDAI-LDR-0149': {'wr_id':'WR-LDR-08.10','primary':['LS','DA'],'secondary':['TF','DG'],'tertiary':['OP','DQ'],'blocked':['RC']},
    'WIDAI-LDR-0150': {'wr_id':'WR-LDR-08.11','primary':['LS','DG'],'secondary':['DA','OP'],'tertiary':['AI','DQ'],'blocked':['TF','AB']},
    'WIDAI-LDR-0151': {'wr_id':'WR-LDR-08.12','primary':['LS','OP'],'secondary':['DG','DA'],'tertiary':['RC','AI'],'blocked':['TF']},
    'WIDAI-LDR-0152': {'wr_id':'WR-LDR-08.13','primary':['LS','TF'],'secondary':['DA','OP'],'tertiary':['DG','DQ'],'blocked':['RC']},
    'WIDAI-LDR-0153': {'wr_id':'WR-LDR-08.14','primary':['DA','TF'],'secondary':['LS','OP'],'tertiary':['DG','DQ'],'blocked':['RC']},
    'WIDAI-LDR-0154': {'wr_id':'WR-LDR-08.15','primary':['AI','TF'],'secondary':['LS','DA'],'tertiary':['OP','DG'],'blocked':['RC']},
    'WIDAI-LDR-0155': {'wr_id':'WR-LDR-08.16','primary':['DA','AI'],'secondary':['LS','OP'],'tertiary':['DG','TF'],'blocked':['RC']},
    'WIDAI-LDR-0156': {'wr_id':'WR-LDR-08.17','primary':['AI','AB'],'secondary':['LS','TF'],'tertiary':['RM','DG'],'blocked':['RC']},
    'WIDAI-LDR-0157': {'wr_id':'WR-LDR-08.18','primary':['DG','RC'],'secondary':['LS','RM'],'tertiary':['DA','DQ'],'blocked':['TF','AB']},
    'WIDAI-LDR-0158': {'wr_id':'WR-LDR-08.19','primary':['OP','DG'],'secondary':['LS','DA'],'tertiary':['DQ','TF'],'blocked':['RC']},
    'WIDAI-LDR-0159': {'wr_id':'WR-LDR-08.20','primary':['AG','RM'],'secondary':['LS','RC'],'tertiary':['AI','DG'],'blocked':['TF','AB']},
    'WIDAI-LDR-0160': {'wr_id':'WR-LDR-08.21','primary':['DQ','DG'],'secondary':['LS','DA'],'tertiary':['OP','RC'],'blocked':['TF','AB']},
    'WIDAI-LDR-0161': {'wr_id':'WR-LDR-08.22','primary':['DG','OP'],'secondary':['LS','DA'],'tertiary':['AI','DQ'],'blocked':['TF','AB']},
    'WIDAI-LDR-0162': {'wr_id':'WR-LDR-08.23','primary':['DG','DQ'],'secondary':['LS','DA'],'tertiary':['RC','OP'],'blocked':['TF','AB']},
    'WIDAI-LDR-0163': {'wr_id':'WR-LDR-08.24','primary':['LS','DG'],'secondary':['OP','RC'],'tertiary':['DA','RM'],'blocked':['TF','AB']},
    'WIDAI-LDR-0164': {'wr_id':'WR-LDR-08.25','primary':['LS','OP'],'secondary':['DG','AI'],'tertiary':['RC','DA'],'blocked':['TF','AB']},
    'WIDAI-LDR-0165': {'wr_id':'WR-LDR-08.26','primary':['DG','DA'],'secondary':['LS','DQ'],'tertiary':['OP','RC'],'blocked':['TF','AB']},
    'WIDAI-LDR-0166': {'wr_id':'WR-LDR-08.27','primary':['TF','DA'],'secondary':['LS','OP'],'tertiary':['DG','DQ'],'blocked':['RC']},
    'WIDAI-LDR-0167': {'wr_id':'WR-LDR-08.28','primary':['DA','AI'],'secondary':['LS','OP'],'tertiary':['TF','DG'],'blocked':['RC']},
    'WIDAI-LDR-0168': {'wr_id':'WR-LDR-08.29','primary':['AI','AB'],'secondary':['LS','AG'],'tertiary':['TF','RM'],'blocked':['RC']},
    'WIDAI-LDR-0169': {'wr_id':'WR-LDR-08.30','primary':['AI','LS'],'secondary':['AB','AG'],'tertiary':['TF','RM'],'blocked':['RC']},
    'WIDAI-LDR-0170': {'wr_id':'WR-LDR-08.31','primary':['AI','TF'],'secondary':['LS','DA'],'tertiary':['AB','DG'],'blocked':['RC']},
    # ===== GOV (25 roles) =====
    'WIDAI-GOV-0001': {'wr_id':'WR-GOV-01.01','primary':['LS','DG'],'secondary':['AG','RC'],'tertiary':['RM','AI'],'blocked':['TF','AB']},
    'WIDAI-GOV-0002': {'wr_id':'WR-GOV-01.02','primary':['LS','DG'],'secondary':['DA','RC'],'tertiary':['RM','DQ'],'blocked':['TF','AB']},
    'WIDAI-GOV-0003': {'wr_id':'WR-GOV-01.03','primary':['LS','AI'],'secondary':['AG','AB'],'tertiary':['RM','RC'],'blocked':['TF']},
    'WIDAI-GOV-0004': {'wr_id':'WR-GOV-01.04','primary':['LS','DA'],'secondary':['AI','OP'],'tertiary':['DG','RM'],'blocked':['TF','AB']},
    'WIDAI-GOV-0005': {'wr_id':'WR-GOV-01.05','primary':['AG','RM'],'secondary':['LS','RC'],'tertiary':['AI','DG'],'blocked':['TF','AB']},
    'WIDAI-GOV-0006': {'wr_id':'WR-GOV-01.06','primary':['LS','DG'],'secondary':['SP','RC'],'tertiary':['RM','DA'],'blocked':['TF','AB']},
    'WIDAI-GOV-0007': {'wr_id':'WR-GOV-01.07','primary':['DG','LS'],'secondary':['RC','RM'],'tertiary':['DA','DQ'],'blocked':['TF','AB']},
    'WIDAI-GOV-0008': {'wr_id':'WR-GOV-01.08','primary':['AG','DG'],'secondary':['RM','RC'],'tertiary':['AI','LS'],'blocked':['TF','AB']},
    'WIDAI-GOV-0009': {'wr_id':'WR-GOV-01.09','primary':['DG','DQ'],'secondary':['DA','RC'],'tertiary':['OP','RM'],'blocked':['TF','AB']},
    'WIDAI-GOV-0010': {'wr_id':'WR-GOV-01.10','primary':['DG','LS'],'secondary':['RC','RM'],'tertiary':['DA','DQ'],'blocked':['TF','AB']},
    'WIDAI-GOV-0011': {'wr_id':'WR-GOV-01.11','primary':['DG','LS'],'secondary':['RC','RM'],'tertiary':['DA','DQ'],'blocked':['TF','AB']},
    'WIDAI-GOV-0012': {'wr_id':'WR-GOV-01.12','primary':['DG','LS'],'secondary':['RC','RM'],'tertiary':['AI','SP'],'blocked':['TF','AB']},
    'WIDAI-GOV-0013': {'wr_id':'WR-GOV-01.13','primary':['DG','DA'],'secondary':['TF','DQ'],'tertiary':['RC','OP'],'blocked':['AB']},
    'WIDAI-GOV-0014': {'wr_id':'WR-GOV-01.14','primary':['DG','LS'],'secondary':['RC','RM'],'tertiary':['DA','AG'],'blocked':['TF','AB']},
    'WIDAI-GOV-0015': {'wr_id':'WR-GOV-01.15','primary':['DG','DQ'],'secondary':['RC','DA'],'tertiary':['OP','RM'],'blocked':['TF','AB']},
    'WIDAI-GOV-0016': {'wr_id':'WR-GOV-01.16','primary':['SP','RC'],'secondary':['DG','RM'],'tertiary':['AG','LS'],'blocked':['TF','AB']},
    'WIDAI-GOV-0017': {'wr_id':'WR-GOV-01.17','primary':['SP','RC'],'secondary':['DG','RM'],'tertiary':['OP','LS'],'blocked':['TF','AB']},
    'WIDAI-GOV-0018': {'wr_id':'WR-GOV-01.18','primary':['SP','TF'],'secondary':['RC','DG'],'tertiary':['RM','DA'],'blocked':['AB']},
    'WIDAI-GOV-0019': {'wr_id':'WR-GOV-01.19','primary':['AG','DG'],'secondary':['RM','RC'],'tertiary':['AI','LS'],'blocked':['TF','AB']},
    'WIDAI-GOV-0020': {'wr_id':'WR-GOV-01.20','primary':['AG','DG'],'secondary':['RM','RC'],'tertiary':['LS','AI'],'blocked':['TF','AB']},
    'WIDAI-GOV-0021': {'wr_id':'WR-GOV-01.21','primary':['DG','TF'],'secondary':['DA','RC'],'tertiary':['DQ','SP'],'blocked':['AB']},
    'WIDAI-GOV-0022': {'wr_id':'WR-GOV-01.22','primary':['DG','LS'],'secondary':['RC','RM'],'tertiary':['DA','DQ'],'blocked':['TF','AB']},
    'WIDAI-GOV-0023': {'wr_id':'WR-GOV-01.23','primary':['DG','LS'],'secondary':['RC','RM'],'tertiary':['SP','DA'],'blocked':['TF','AB']},
    'WIDAI-GOV-0024': {'wr_id':'WR-GOV-01.24','primary':['RM','DG'],'secondary':['RC','LS'],'tertiary':['AG','OP'],'blocked':['TF','AB']},
    'WIDAI-GOV-0025': {'wr_id':'WR-GOV-01.25','primary':['AG','OP'],'secondary':['AI','LS'],'tertiary':['DG','AB'],'blocked':['TF']},
    # ===== RSK (24 roles) =====
    'WIDAI-RSK-0101': {'wr_id':'WR-RSK-06.01','primary':['RM','AG'],'secondary':['RC','DG'],'tertiary':['AI','LS'],'blocked':['TF','AB']},
    'WIDAI-RSK-0102': {'wr_id':'WR-RSK-06.02','primary':['SP','RM'],'secondary':['AG','RC'],'tertiary':['AI','TF'],'blocked':[]},
    'WIDAI-RSK-0103': {'wr_id':'WR-RSK-06.03','primary':['RM','AI'],'secondary':['AG','RC'],'tertiary':['TF','DA'],'blocked':[]},
    'WIDAI-RSK-0104': {'wr_id':'WR-RSK-06.04','primary':['RC','DG'],'secondary':['RM','SP'],'tertiary':['DA','OP'],'blocked':['TF','AB']},
    'WIDAI-RSK-0105': {'wr_id':'WR-RSK-06.05','primary':['SP','RM'],'secondary':['AI','AG'],'tertiary':['TF','RC'],'blocked':[]},
    'WIDAI-RSK-0106': {'wr_id':'WR-RSK-06.06','primary':['RM','SP'],'secondary':['AG','RC'],'tertiary':['AI','OP'],'blocked':['TF','AB']},
    'WIDAI-RSK-0107': {'wr_id':'WR-RSK-06.07','primary':['RM','AG'],'secondary':['RC','DG'],'tertiary':['AI','LS'],'blocked':['TF','AB']},
    'WIDAI-RSK-0108': {'wr_id':'WR-RSK-06.08','primary':['RM','AG'],'secondary':['RC','AI'],'tertiary':['DG','LS'],'blocked':['TF','AB']},
    'WIDAI-RSK-0109': {'wr_id':'WR-RSK-06.09','primary':['RM','AI'],'secondary':['AG','TF'],'tertiary':['RC','DA'],'blocked':['AB']},
    'WIDAI-RSK-0110': {'wr_id':'WR-RSK-06.10','primary':['RM','AG'],'secondary':['AI','DG'],'tertiary':['RC','LS'],'blocked':['TF','AB']},
    'WIDAI-RSK-0111': {'wr_id':'WR-RSK-06.11','primary':['RM','AG'],'secondary':['RC','DG'],'tertiary':['AI','OP'],'blocked':['TF','AB']},
    'WIDAI-RSK-0112': {'wr_id':'WR-RSK-06.12','primary':['RM','AG'],'secondary':['AI','DG'],'tertiary':['RC','OP'],'blocked':['TF','AB']},
    'WIDAI-RSK-0113': {'wr_id':'WR-RSK-06.13','primary':['RM','AG'],'secondary':['RC','AI'],'tertiary':['DG','LS'],'blocked':['TF','AB']},
    'WIDAI-RSK-0114': {'wr_id':'WR-RSK-06.14','primary':['AG','RM'],'secondary':['RC','DG'],'tertiary':['AI','LS'],'blocked':['TF','AB']},
    'WIDAI-RSK-0115': {'wr_id':'WR-RSK-06.15','primary':['RC','AG'],'secondary':['RM','DG'],'tertiary':['AI','LS'],'blocked':['TF','AB']},
    'WIDAI-RSK-0116': {'wr_id':'WR-RSK-06.16','primary':['AG','DG'],'secondary':['RC','RM'],'tertiary':['AI','OP'],'blocked':['TF','AB']},
    'WIDAI-RSK-0117': {'wr_id':'WR-RSK-06.17','primary':['RM','RC'],'secondary':['AG','AI'],'tertiary':['DG','OP'],'blocked':['TF','AB']},
    'WIDAI-RSK-0118': {'wr_id':'WR-RSK-06.18','primary':['RM','AG'],'secondary':['AI','RC'],'tertiary':['DG','TF'],'blocked':['AB']},
    'WIDAI-RSK-0119': {'wr_id':'WR-RSK-06.19','primary':['AG','RM'],'secondary':['RC','DG'],'tertiary':['AI','LS'],'blocked':['TF','AB']},
    'WIDAI-RSK-0120': {'wr_id':'WR-RSK-06.20','primary':['SP','TF'],'secondary':['RM','RC'],'tertiary':['DG','DA'],'blocked':['AB']},
    'WIDAI-RSK-0121': {'wr_id':'WR-RSK-06.21','primary':['SP','RC'],'secondary':['RM','DG'],'tertiary':['AG','LS'],'blocked':['TF','AB']},
    'WIDAI-RSK-0122': {'wr_id':'WR-RSK-06.22','primary':['AG','RC'],'secondary':['RM','DG'],'tertiary':['AI','SP'],'blocked':['TF','AB']},
    'WIDAI-RSK-0123': {'wr_id':'WR-RSK-06.23','primary':['RM','AI'],'secondary':['AG','TF'],'tertiary':['AB','RC'],'blocked':[]},
    'WIDAI-RSK-0124': {'wr_id':'WR-RSK-06.24','primary':['RM','AI'],'secondary':['AG','AB'],'tertiary':['TF','RC'],'blocked':[]},
    # ===== ANL (14 roles) =====
    'WIDAI-ANL-0087': {'wr_id':'WR-ANL-05.01','primary':['DA','TF'],'secondary':['DQ','OP'],'tertiary':['AI','DG'],'blocked':['AB']},
    'WIDAI-ANL-0088': {'wr_id':'WR-ANL-05.02','primary':['DA','AI'],'secondary':['TF','DQ'],'tertiary':['OP','DG'],'blocked':['AB']},
    'WIDAI-ANL-0089': {'wr_id':'WR-ANL-05.03','primary':['DA','TF'],'secondary':['AI','OP'],'tertiary':['DG','DQ'],'blocked':['AB']},
    'WIDAI-ANL-0090': {'wr_id':'WR-ANL-05.04','primary':['AI','TF'],'secondary':['DA','RM'],'tertiary':['DQ','AB'],'blocked':[]},
    'WIDAI-ANL-0091': {'wr_id':'WR-ANL-05.05','primary':['DA','OP'],'secondary':['TF','DQ'],'tertiary':['AI','DG'],'blocked':['AB']},
    'WIDAI-ANL-0092': {'wr_id':'WR-ANL-05.06','primary':['DQ','DA'],'secondary':['RC','DG'],'tertiary':['TF','RM'],'blocked':['AB']},
    'WIDAI-ANL-0093': {'wr_id':'WR-ANL-05.07','primary':['DA','DQ'],'secondary':['RC','TF'],'tertiary':['DG','OP'],'blocked':['AB']},
    'WIDAI-ANL-0094': {'wr_id':'WR-ANL-05.08','primary':['DA','OP'],'secondary':['TF','DQ'],'tertiary':['AI','DG'],'blocked':['AB']},
    'WIDAI-ANL-0095': {'wr_id':'WR-ANL-05.09','primary':['DA','TF'],'secondary':['DQ','OP'],'tertiary':['AI','DG'],'blocked':['AB']},
    'WIDAI-ANL-0096': {'wr_id':'WR-ANL-05.10','primary':['RM','DA'],'secondary':['RC','TF'],'tertiary':['DQ','AI'],'blocked':['AB']},
    'WIDAI-ANL-0097': {'wr_id':'WR-ANL-05.11','primary':['DA','OP'],'secondary':['DQ','TF'],'tertiary':['AI','DG'],'blocked':['AB']},
    'WIDAI-ANL-0098': {'wr_id':'WR-ANL-05.12','primary':['AI','TF'],'secondary':['DA','DQ'],'tertiary':['AB','OP'],'blocked':[]},
    'WIDAI-ANL-0099': {'wr_id':'WR-ANL-05.13','primary':['RM','DA'],'secondary':['RC','DQ'],'tertiary':['TF','OP'],'blocked':['AB']},
    'WIDAI-ANL-0100': {'wr_id':'WR-ANL-05.14','primary':['DA','AI'],'secondary':['TF','OP'],'tertiary':['DQ','DG'],'blocked':['AB']},
    # ===== DSM (21 roles) =====
    'WIDAI-DSM-0066': {'wr_id':'WR-DSM-04.01','primary':['DQ','DG'],'secondary':['DA','OP'],'tertiary':['RC','LS'],'blocked':['TF','AB']},
    'WIDAI-DSM-0067': {'wr_id':'WR-DSM-04.02','primary':['DG','DQ'],'secondary':['DA','RC'],'tertiary':['OP','LS'],'blocked':['TF','AB']},
    'WIDAI-DSM-0068': {'wr_id':'WR-DSM-04.03','primary':['DG','DA'],'secondary':['DQ','OP'],'tertiary':['RC','LS'],'blocked':['TF','AB']},
    'WIDAI-DSM-0069': {'wr_id':'WR-DSM-04.04','primary':['SP','RC'],'secondary':['DG','RM'],'tertiary':['DA','OP'],'blocked':['TF','AB']},
    'WIDAI-DSM-0070': {'wr_id':'WR-DSM-04.05','primary':['DG','DA'],'secondary':['OP','AI'],'tertiary':['LS','DQ'],'blocked':['TF','AB']},
    'WIDAI-DSM-0071': {'wr_id':'WR-DSM-04.06','primary':['DQ','DG'],'secondary':['DA','TF'],'tertiary':['OP','RC'],'blocked':['AB']},
    'WIDAI-DSM-0072': {'wr_id':'WR-DSM-04.07','primary':['DG','DA'],'secondary':['DQ','TF'],'tertiary':['OP','RC'],'blocked':['AB']},
    'WIDAI-DSM-0073': {'wr_id':'WR-DSM-04.08','primary':['DG','SP'],'secondary':['RC','DA'],'tertiary':['DQ','OP'],'blocked':['TF','AB']},
    'WIDAI-DSM-0074': {'wr_id':'WR-DSM-04.09','primary':['DG','DA'],'secondary':['DQ','TF'],'tertiary':['OP','RC'],'blocked':['AB']},
    'WIDAI-DSM-0075': {'wr_id':'WR-DSM-04.10','primary':['DG','RC'],'secondary':['SP','DA'],'tertiary':['DQ','OP'],'blocked':['TF','AB']},
    'WIDAI-DSM-0076': {'wr_id':'WR-DSM-04.11','primary':['DG','DA'],'secondary':['OP','DQ'],'tertiary':['RC','LS'],'blocked':['TF','AB']},
    'WIDAI-DSM-0077': {'wr_id':'WR-DSM-04.12','primary':['DG','DA'],'secondary':['DQ','OP'],'tertiary':['RC','LS'],'blocked':['TF','AB']},
    'WIDAI-DSM-0078': {'wr_id':'WR-DSM-04.13','primary':['DG','DA'],'secondary':['RC','DQ'],'tertiary':['SP','OP'],'blocked':['TF','AB']},
    'WIDAI-DSM-0079': {'wr_id':'WR-DSM-04.14','primary':['AI','AG'],'secondary':['DG','OP'],'tertiary':['RM','LS'],'blocked':['TF','AB']},
    'WIDAI-DSM-0080': {'wr_id':'WR-DSM-04.15','primary':['DG','OP'],'secondary':['DA','AI'],'tertiary':['LS','DQ'],'blocked':['TF','AB']},
    'WIDAI-DSM-0081': {'wr_id':'WR-DSM-04.16','primary':['DG','OP'],'secondary':['DA','AI'],'tertiary':['LS','DQ'],'blocked':['TF','AB']},
    'WIDAI-DSM-0082': {'wr_id':'WR-DSM-04.17','primary':['DG','DA'],'secondary':['OP','AI'],'tertiary':['DQ','LS'],'blocked':['TF','AB']},
    'WIDAI-DSM-0083': {'wr_id':'WR-DSM-04.18','primary':['DG','DA'],'secondary':['OP','DQ'],'tertiary':['AI','RC'],'blocked':['TF','AB']},
    'WIDAI-DSM-0084': {'wr_id':'WR-DSM-04.19','primary':['DQ','DG'],'secondary':['RC','DA'],'tertiary':['OP','LS'],'blocked':['TF','AB']},
    'WIDAI-DSM-0085': {'wr_id':'WR-DSM-04.20','primary':['DQ','DG'],'secondary':['DA','RC'],'tertiary':['OP','TF'],'blocked':['AB']},
    'WIDAI-DSM-0086': {'wr_id':'WR-DSM-04.21','primary':['DQ','TF'],'secondary':['DA','DG'],'tertiary':['RC','OP'],'blocked':['AB']},
    # ===== ENG (25 roles) =====
    'WIDAI-ENG-0026': {'wr_id':'WR-ENG-02.01','primary':['DA','TF'],'secondary':['DG','DQ'],'tertiary':['LS','OP'],'blocked':['AB']},
    'WIDAI-ENG-0027': {'wr_id':'WR-ENG-02.02','primary':['AI','TF'],'secondary':['DA','AB'],'tertiary':['AG','DG'],'blocked':['LS']},
    'WIDAI-ENG-0028': {'wr_id':'WR-ENG-02.03','primary':['TF','DA'],'secondary':['DQ','OP'],'tertiary':['DG','AB'],'blocked':['LS']},
    'WIDAI-ENG-0029': {'wr_id':'WR-ENG-02.04','primary':['TF','DA'],'secondary':['AI','DQ'],'tertiary':['OP','DG'],'blocked':['LS','AB']},
    'WIDAI-ENG-0030': {'wr_id':'WR-ENG-02.05','primary':['TF','DA'],'secondary':['DQ','OP'],'tertiary':['DG','AI'],'blocked':['LS','AB']},
    'WIDAI-ENG-0031': {'wr_id':'WR-ENG-02.06','primary':['DA','TF'],'secondary':['DQ','DG'],'tertiary':['OP','AB'],'blocked':['LS']},
    'WIDAI-ENG-0032': {'wr_id':'WR-ENG-02.07','primary':['DA','TF'],'secondary':['DQ','DG'],'tertiary':['OP','AB'],'blocked':['LS']},
    'WIDAI-ENG-0033': {'wr_id':'WR-ENG-02.08','primary':['DA','TF'],'secondary':['DG','DQ'],'tertiary':['OP','RC'],'blocked':['LS','AB']},
    'WIDAI-ENG-0034': {'wr_id':'WR-ENG-02.09','primary':['TF','DA'],'secondary':['DQ','SP'],'tertiary':['OP','DG'],'blocked':['LS','AB']},
    'WIDAI-ENG-0035': {'wr_id':'WR-ENG-02.10','primary':['DA','TF'],'secondary':['DG','SP'],'tertiary':['DQ','OP'],'blocked':['LS','AB']},
    'WIDAI-ENG-0036': {'wr_id':'WR-ENG-02.11','primary':['TF','DA'],'secondary':['OP','SP'],'tertiary':['DG','DQ'],'blocked':['LS','AB']},
    'WIDAI-ENG-0037': {'wr_id':'WR-ENG-02.12','primary':['TF','DA'],'secondary':['OP','DQ'],'tertiary':['DG','AI'],'blocked':['LS','AB']},
    'WIDAI-ENG-0038': {'wr_id':'WR-ENG-02.13','primary':['TF','DA'],'secondary':['DQ','OP'],'tertiary':['DG','SP'],'blocked':['LS','AB']},
    'WIDAI-ENG-0039': {'wr_id':'WR-ENG-02.14','primary':['TF','DQ'],'secondary':['DA','OP'],'tertiary':['DG','AI'],'blocked':['LS','AB']},
    'WIDAI-ENG-0040': {'wr_id':'WR-ENG-02.15','primary':['DA','DG'],'secondary':['TF','DQ'],'tertiary':['OP','RC'],'blocked':['LS','AB']},
    'WIDAI-ENG-0041': {'wr_id':'WR-ENG-02.16','primary':['AI','TF'],'secondary':['AB','DA'],'tertiary':['RM','DG'],'blocked':['LS']},
    'WIDAI-ENG-0042': {'wr_id':'WR-ENG-02.17','primary':['AI','TF'],'secondary':['AB','DA'],'tertiary':['AG','SP'],'blocked':['LS']},
    'WIDAI-ENG-0043': {'wr_id':'WR-ENG-02.18','primary':['DA','TF'],'secondary':['AI','DG'],'tertiary':['DQ','AB'],'blocked':['LS']},
    'WIDAI-ENG-0044': {'wr_id':'WR-ENG-02.19','primary':['DA','TF'],'secondary':['DG','AI'],'tertiary':['DQ','RC'],'blocked':['LS','AB']},
    'WIDAI-ENG-0045': {'wr_id':'WR-ENG-02.20','primary':['TF','AI'],'secondary':['DA','AB'],'tertiary':['DG','DQ'],'blocked':['LS']},
    'WIDAI-ENG-0046': {'wr_id':'WR-ENG-02.21','primary':['AI','TF'],'secondary':['DA','SP'],'tertiary':['DQ','AG'],'blocked':['LS']},
    'WIDAI-ENG-0047': {'wr_id':'WR-ENG-02.22','primary':['TF','DA'],'secondary':['DG','OP'],'tertiary':['DQ','AI'],'blocked':['LS','AB']},
    'WIDAI-ENG-0048': {'wr_id':'WR-ENG-02.23','primary':['AI','AB'],'secondary':['TF','DA'],'tertiary':['DG','AG'],'blocked':['LS']},
    'WIDAI-ENG-0049': {'wr_id':'WR-ENG-02.24','primary':['AI','TF'],'secondary':['AB','DA'],'tertiary':['DG','DQ'],'blocked':['LS']},
    'WIDAI-ENG-0050': {'wr_id':'WR-ENG-02.25','primary':['AI','TF'],'secondary':['AB','DA'],'tertiary':['DG','DQ'],'blocked':['LS']},
    # ===== DEV (15 roles) =====
    'WIDAI-DEV-0051': {'wr_id':'WR-DEV-03.01','primary':['AI','TF'],'secondary':['DA','DQ'],'tertiary':['AB','DG'],'blocked':['LS','RC']},
    'WIDAI-DEV-0052': {'wr_id':'WR-DEV-03.02','primary':['AI','TF'],'secondary':['AB','DA'],'tertiary':['DQ','DG'],'blocked':['LS','RC']},
    'WIDAI-DEV-0053': {'wr_id':'WR-DEV-03.03','primary':['AI','AB'],'secondary':['TF','DA'],'tertiary':['AG','DG'],'blocked':['LS','RC']},
    'WIDAI-DEV-0054': {'wr_id':'WR-DEV-03.04','primary':['AI','TF'],'secondary':['AB','DA'],'tertiary':['DG','DQ'],'blocked':['LS','RC']},
    'WIDAI-DEV-0055': {'wr_id':'WR-DEV-03.05','primary':['AI','TF'],'secondary':['AB','DA'],'tertiary':['DG','DQ'],'blocked':['LS','RC']},
    'WIDAI-DEV-0056': {'wr_id':'WR-DEV-03.06','primary':['AI','TF'],'secondary':['AB','RC'],'tertiary':['AG','SP'],'blocked':['LS']},
    'WIDAI-DEV-0057': {'wr_id':'WR-DEV-03.07','primary':['AI','TF'],'secondary':['AB','DA'],'tertiary':['DG','DQ'],'blocked':['LS','RC']},
    'WIDAI-DEV-0058': {'wr_id':'WR-DEV-03.08','primary':['AI','TF'],'secondary':['AB','DA'],'tertiary':['AG','DG'],'blocked':['LS','RC']},
    'WIDAI-DEV-0059': {'wr_id':'WR-DEV-03.09','primary':['AI','AB'],'secondary':['TF','DA'],'tertiary':['AG','DG'],'blocked':['LS','RC']},
    'WIDAI-DEV-0060': {'wr_id':'WR-DEV-03.10','primary':['AI','AB'],'secondary':['TF','DA'],'tertiary':['AG','SP'],'blocked':['LS','RC']},
    'WIDAI-DEV-0061': {'wr_id':'WR-DEV-03.11','primary':['AI','AB'],'secondary':['TF','AG'],'tertiary':['DG','RC'],'blocked':['LS']},
    'WIDAI-DEV-0062': {'wr_id':'WR-DEV-03.12','primary':['AI','DA'],'secondary':['TF','AB'],'tertiary':['DG','RM'],'blocked':['LS','RC']},
    'WIDAI-DEV-0063': {'wr_id':'WR-DEV-03.13','primary':['AI','TF'],'secondary':['DA','DQ'],'tertiary':['AB','DG'],'blocked':['LS','RC']},
    'WIDAI-DEV-0064': {'wr_id':'WR-DEV-03.14','primary':['AI','DA'],'secondary':['TF','OP'],'tertiary':['AB','DG'],'blocked':['LS','RC']},
    'WIDAI-DEV-0065': {'wr_id':'WR-DEV-03.15','primary':['AI','TF'],'secondary':['AB','DA'],'tertiary':['SP','RM'],'blocked':['LS','RC']},
    # ===== OPS (15 roles) =====
    'WIDAI-OPS-0125': {'wr_id':'WR-OPS-07.01','primary':['OP','LS'],'secondary':['DG','AI'],'tertiary':['RC','RM'],'blocked':['TF','AB']},
    'WIDAI-OPS-0126': {'wr_id':'WR-OPS-07.02','primary':['OP','AI'],'secondary':['DG','LS'],'tertiary':['AG','RC'],'blocked':['TF','AB']},
    'WIDAI-OPS-0127': {'wr_id':'WR-OPS-07.03','primary':['OP','AI'],'secondary':['AG','DG'],'tertiary':['LS','RC'],'blocked':['TF','AB']},
    'WIDAI-OPS-0128': {'wr_id':'WR-OPS-07.04','primary':['OP','DG'],'secondary':['DA','DQ'],'tertiary':['TF','RC'],'blocked':['AB']},
    'WIDAI-OPS-0129': {'wr_id':'WR-OPS-07.05','primary':['OP','DA'],'secondary':['AI','DG'],'tertiary':['LS','DQ'],'blocked':['TF','AB']},
    'WIDAI-OPS-0130': {'wr_id':'WR-OPS-07.06','primary':['OP','DG'],'secondary':['LS','AI'],'tertiary':['AG','DA'],'blocked':['TF','AB']},
    'WIDAI-OPS-0131': {'wr_id':'WR-OPS-07.07','primary':['OP','AI'],'secondary':['AG','LS'],'tertiary':['DG','RC'],'blocked':['TF','AB']},
    'WIDAI-OPS-0132': {'wr_id':'WR-OPS-07.08','primary':['DG','OP'],'secondary':['DQ','DA'],'tertiary':['RC','TF'],'blocked':['AB']},
    'WIDAI-OPS-0133': {'wr_id':'WR-OPS-07.09','primary':['AI','AB'],'secondary':['OP','AG'],'tertiary':['TF','DG'],'blocked':['LS','RC']},
    'WIDAI-OPS-0134': {'wr_id':'WR-OPS-07.10','primary':['OP','DG'],'secondary':['DA','LS'],'tertiary':['DQ','TF'],'blocked':['AB']},
    'WIDAI-OPS-0135': {'wr_id':'WR-OPS-07.11','primary':['AI','AB'],'secondary':['TF','OP'],'tertiary':['AG','DG'],'blocked':['LS','RC']},
    'WIDAI-OPS-0136': {'wr_id':'WR-OPS-07.12','primary':['AB','AI'],'secondary':['AG','OP'],'tertiary':['RM','DG'],'blocked':['LS','RC']},
    'WIDAI-OPS-0137': {'wr_id':'WR-OPS-07.13','primary':['AI','TF'],'secondary':['AB','OP'],'tertiary':['DG','DA'],'blocked':['LS','RC']},
    'WIDAI-OPS-0138': {'wr_id':'WR-OPS-07.14','primary':['AI','AB'],'secondary':['AG','OP'],'tertiary':['TF','DG'],'blocked':['LS','RC']},
    'WIDAI-OPS-0139': {'wr_id':'WR-OPS-07.15','primary':['AI','AB'],'secondary':['AG','TF'],'tertiary':['OP','DG'],'blocked':['LS','RC']},
    # ===== NICHE (9 roles) =====
    'WIDAI-NICHE-0179': {'wr_id':'WR-NICHE-09.01','primary':['AI','RC'],'secondary':['RM','AG'],'tertiary':['DQ','TF'],'blocked':['AB']},
    'WIDAI-NICHE-0180': {'wr_id':'WR-NICHE-09.02','primary':['AI','TF'],'secondary':['RM','DA'],'tertiary':['AB','RC'],'blocked':[]},
    'WIDAI-NICHE-0181': {'wr_id':'WR-NICHE-09.03','primary':['RC','RM'],'secondary':['AG','DG'],'tertiary':['AI','SP'],'blocked':['TF','AB']},
    'WIDAI-NICHE-0182': {'wr_id':'WR-NICHE-09.04','primary':['LS','RC'],'secondary':['DG','RM'],'tertiary':['AG','AI'],'blocked':['TF','AB']},
    'WIDAI-NICHE-0183': {'wr_id':'WR-NICHE-09.05','primary':['AI','DQ'],'secondary':['TF','DA'],'tertiary':['AG','OP'],'blocked':['LS','RC']},
    'WIDAI-NICHE-0184': {'wr_id':'WR-NICHE-09.06','primary':['AI','AG'],'secondary':['DQ','OP'],'tertiary':['DG','TF'],'blocked':['LS','RC']},
    'WIDAI-NICHE-0185': {'wr_id':'WR-NICHE-09.07','primary':['AI','AB'],'secondary':['TF','DA'],'tertiary':['DG','DQ'],'blocked':['LS','RC']},
    'WIDAI-NICHE-0186': {'wr_id':'WR-NICHE-09.08','primary':['AG','SP'],'secondary':['RM','AI'],'tertiary':['TF','DG'],'blocked':['LS','RC']},
    'WIDAI-NICHE-0187': {'wr_id':'WR-NICHE-09.09','primary':['AB','AI'],'secondary':['TF','AG'],'tertiary':['DG','SP'],'blocked':['LS','RC']},
    # ===== REG (8 roles) =====
    'WIDAI-REG-0171': {'wr_id':'WR-REG-10.01','primary':['RC','AG'],'secondary':['RM','DG'],'tertiary':['AI','SP'],'blocked':['TF','AB']},
    'WIDAI-REG-0172': {'wr_id':'WR-REG-10.02','primary':['RC','AG'],'secondary':['RM','DG'],'tertiary':['AI','SP'],'blocked':['TF','AB']},
    'WIDAI-REG-0173': {'wr_id':'WR-REG-10.03','primary':['RC','DG'],'secondary':['AG','RM'],'tertiary':['AI','LS'],'blocked':['TF','AB']},
    'WIDAI-REG-0174': {'wr_id':'WR-REG-10.04','primary':['RC','RM'],'secondary':['AG','DG'],'tertiary':['AI','TF'],'blocked':['AB']},
    'WIDAI-REG-0175': {'wr_id':'WR-REG-10.05','primary':['AG','RM'],'secondary':['RC','DG'],'tertiary':['AI','SP'],'blocked':['TF','AB']},
    'WIDAI-REG-0176': {'wr_id':'WR-REG-10.06','primary':['RC','RM'],'secondary':['AG','AI'],'tertiary':['DG','SP'],'blocked':['TF','AB']},
    'WIDAI-REG-0177': {'wr_id':'WR-REG-10.07','primary':['AG','RC'],'secondary':['RM','AI'],'tertiary':['DG','TF'],'blocked':['AB']},
    'WIDAI-REG-0178': {'wr_id':'WR-REG-10.08','primary':['DQ','RC'],'secondary':['DG','AG'],'tertiary':['RM','TF'],'blocked':['AB']},
}

# ====== CORE MAPPING GENERATOR WITH 3 ADVERSARIAL PASSES ======

def generate_role_mapping(role_id, profile, inv, seniority):
    wr_id      = profile['wr_id']
    proficiency = SENIORITY_MAP.get(seniority, 'tactical')
    blocked     = set(profile.get('blocked', []))
    primary     = [d for d in profile['primary']   if d not in blocked and d in inv]
    secondary   = [d for d in profile['secondary'] if d not in blocked and d in inv]
    tertiary    = [d for d in profile['tertiary']  if d not in blocked and d in inv]

    rels    = []
    seen    = set()

    def add(domains, rel_type, nk, ns, nt, na):
        for domain in domains:
            d = inv[domain]
            for ksa_id in d['knowledge'][:nk]:
                if ksa_id not in seen:
                    rels.append({'work_role_id': wr_id, 'ksa_id': ksa_id,
                                 'relationship_type': rel_type, 'proficiency_context': proficiency})
                    seen.add(ksa_id)
            for ksa_id in d['skills'][:ns]:
                if ksa_id not in seen:
                    rels.append({'work_role_id': wr_id, 'ksa_id': ksa_id,
                                 'relationship_type': rel_type, 'proficiency_context': proficiency})
                    seen.add(ksa_id)
            for ksa_id in d['tasks'][:nt]:
                if ksa_id not in seen:
                    rels.append({'work_role_id': wr_id, 'ksa_id': ksa_id,
                                 'relationship_type': rel_type, 'proficiency_context': proficiency})
                    seen.add(ksa_id)
            for ksa_id in d['abilities'][:na]:
                if ksa_id not in seen:
                    rels.append({'work_role_id': wr_id, 'ksa_id': ksa_id,
                                 'relationship_type': rel_type, 'proficiency_context': proficiency})
                    seen.add(ksa_id)

    # Initial selection
    add(primary,   'requires',   nk=3, ns=3, nt=2, na=1)
    add(secondary, 'recommends', nk=2, ns=2, nt=1, na=0)
    add(tertiary,  'optional',   nk=1, ns=1, nt=0, na=0)

    # ---- PASS 1: COVERAGE CHECK ----
    # Every primary + secondary domain must have >= 2 KSAs; add from knowledge if short
    covered = {}
    for r in rels:
        dom = r['ksa_id'].split('-')[0]
        covered[dom] = covered.get(dom, 0) + 1
    for domain in primary + secondary:
        if covered.get(domain, 0) < 2:
            for ksa_id in inv[domain]['knowledge'][:4]:
                if ksa_id not in seen:
                    rels.append({'work_role_id': wr_id, 'ksa_id': ksa_id,
                                 'relationship_type': 'recommends', 'proficiency_context': proficiency})
                    seen.add(ksa_id)

    # ---- PASS 2: RELEVANCE CHECK ----
    # Remove any KSAs whose domain appears in the blocked set
    rels = [r for r in rels if r['ksa_id'].split('-')[0] not in blocked]

    # Also flag high-TF technical KSAs for pure strategic roles — demote to 'optional'
    if proficiency == 'strategic':
        for r in rels:
            dom = r['ksa_id'].split('-')[0]
            if dom == 'TF' and r['relationship_type'] == 'requires':
                r['relationship_type'] = 'recommends'

    # ---- PASS 3: DEPTH CHECK ----
    # Enforce consistent proficiency_context; correct relationship_type floor by seniority
    # Strategic roles: primary domain KSAs must be 'requires', not 'optional'
    # Foundational roles: nothing should be 'requires' from blocked domains (already handled)
    for r in rels:
        r['proficiency_context'] = proficiency   # enforce uniform context per role
        dom = r['ksa_id'].split('-')[0]
        if dom in primary and r['relationship_type'] == 'optional':
            r['relationship_type'] = 'requires'   # primary domain KSAs can't be optional
        if dom in tertiary and r['relationship_type'] == 'requires' and proficiency in ('foundational', 'tactical'):
            r['relationship_type'] = 'recommends'  # tactical/foundational: tertiary = recommends

    return rels

# ====== CATEGORY BUILDER ======
CATEGORY_META = {
    'LDR':   ('WIDAI-LDR',   [f'WIDAI-LDR-0{n}' for n in range(140, 171)]),
    'GOV':   ('WIDAI-GOV',   [f'WIDAI-GOV-000{n}' if n < 10 else f'WIDAI-GOV-00{n}' for n in range(1, 26)]),
    'RSK':   ('WIDAI-RSK',   [f'WIDAI-RSK-0{n}' for n in range(101, 125)]),
    'ANL':   ('WIDAI-ANL',   [f'WIDAI-ANL-0{n}' for n in range(87, 101)]),
    'DSM':   ('WIDAI-DSM',   [f'WIDAI-DSM-00{n}' if n < 100 else f'WIDAI-DSM-0{n}' for n in range(66, 87)]),
    'ENG':   ('WIDAI-ENG',   [f'WIDAI-ENG-00{n}' if n < 100 else f'WIDAI-ENG-0{n}' for n in range(26, 51)]),
    'DEV':   ('WIDAI-DEV',   [f'WIDAI-DEV-00{n}' if n < 100 else f'WIDAI-DEV-0{n}' for n in range(51, 66)]),
    'OPS':   ('WIDAI-OPS',   [f'WIDAI-OPS-0{n}' for n in range(125, 140)]),
    'NICHE': ('WIDAI-NICHE', [f'WIDAI-NICHE-0{n}' for n in range(179, 188)]),
    'REG':   ('WIDAI-REG',   [f'WIDAI-REG-0{n}' for n in range(171, 179)]),
}

# ====== MAIN EXECUTION ======
def build_category(cat_code, inv, roles_data):
    """Build the complete mapping file for one category."""
    rels_all = []
    for role in roles_data['roles']:
        role_id  = role['role_id']
        seniority = role['seniority_level']
        profile  = ROLE_PROFILES.get(role_id)
        if not profile:
            print(f"  WARNING: no profile for {role_id} ({role['canonical_title']})")
            continue
        role_rels = generate_role_mapping(role_id, profile, inv, seniority)
        rels_all.extend(role_rels)
        print(f"  {role_id} → {profile['wr_id']} | {len(role_rels)} KSAs | {seniority}")

    doc = {
        "dataset_id":         "WIDAI-ROLE-KSA-MAP",
        "category_code":      cat_code,
        "relationship_count": len(rels_all),
        "schema_version":     "2.0.0",
        "relationships":      rels_all
    }
    out_path = os.path.join(MAPPINGS_DIR, f'role_ksa_{cat_code}.json')
    with open(out_path, 'w') as f:
        json.dump(doc, f, indent=2)
    return len(rels_all), len(roles_data['roles'])


if __name__ == '__main__':
    print("Loading KSA inventory...")
    inv = load_all_ksas()
    print(f"  Loaded domains: {list(inv.keys())}")

    summary = {}
    for cat_code in ['LDR','GOV','RSK','ANL','DSM','ENG','DEV','OPS','NICHE','REG']:
        print(f"\n=== Building {cat_code} ===")
        with open(os.path.join(BASE, f'roles/{cat_code}.json')) as f:
            roles_data = json.load(f)
        rel_count, role_count = build_category(cat_code, inv, roles_data)
        avg = rel_count / role_count if role_count else 0
        summary[cat_code] = {'roles': role_count, 'relationships': rel_count, 'avg': round(avg, 1)}
        print(f"  ✓ {cat_code}: {role_count} roles, {rel_count} relationships, avg {avg:.1f} KSAs/role")

    print("\n====== VALIDATION SUMMARY ======")
    total_rels  = sum(v['relationships'] for v in summary.values())
    total_roles = sum(v['roles'] for v in summary.values())
    for cat, s in summary.items():
        print(f"  {cat}: {s['roles']} roles | {s['relationships']} rels | avg {s['avg']}")
    print(f"\n  TOTAL ROLES:         {total_roles}")
    print(f"  TOTAL RELATIONSHIPS: {total_rels}")
    print(f"  OVERALL AVG:         {total_rels/total_roles:.1f} KSAs/role")
