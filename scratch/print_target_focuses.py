import sys, os
sys.path.append(os.path.dirname(__file__))
from parse_all_focuses import parse_focus_file
import re

for tag, path, target_id in [('PRA', 'common/national_focus/prague.txt', 'pra_crush_benesov_threat'), ('BEN', 'common/national_focus/benesov.txt', 'ben_enforce_the_workers_mandate')]:
    focs = parse_focus_file(path)
    for b in focs:
        id_m = re.search(r'id\s*=\s*([a-zA-Z0-9_]+)', b)
        fid = id_m.group(1) if id_m else 'unknown'
        if fid == target_id:
            print(f'=== {tag}: {fid} ===')
            print(b)
