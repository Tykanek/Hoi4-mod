import sys, os
sys.path.append(os.path.dirname(__file__))
from parse_all_focuses import parse_focus_file
import re

focs = parse_focus_file('common/national_focus/prague.txt')
for b in focs:
    id_m = re.search(r'id\s*=\s*([a-zA-Z0-9_]+)', b)
    fid = id_m.group(1) if id_m else 'unknown'
    if 'BEN' in b or 'benesov' in b.lower():
        print(f'PRA Focus: {fid}')
        for line in b.strip().splitlines()[:10]:
            print('  ', line.strip())
        print('-'*30)

