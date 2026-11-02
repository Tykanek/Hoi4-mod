import sys, os
sys.path.append(os.path.dirname(__file__))
from parse_all_focuses import parse_focus_file
import re

focs = parse_focus_file('common/national_focus/benesov.txt')
for b in focs:
    id_m = re.search(r'id\s*=\s*([a-zA-Z0-9_]+)', b)
    fid = id_m.group(1) if id_m else 'unknown'
    if 'CZE' in b or 'czech' in b.lower():
        # check if it gives wargoal or targets CZE
        if any(w in b for w in ['wargoal', 'war', 'annex', 'puppet', 'conquer', 'claim']):
            print(f'BEN Focus: {fid}')
            m_comp = re.search(r'completion_reward\s*=\s*\{(.*)\}', b, re.DOTALL)
            if m_comp:
                for l in m_comp.group(1).strip().splitlines()[:20]:
                    print('  ', l.strip())
            print('='*40)
