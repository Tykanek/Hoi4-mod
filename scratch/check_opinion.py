import os
import re

loc_dir = r'localisation\english'
defined_keys = {}
for fname in os.listdir(loc_dir):
    if fname.endswith('.yml'):
        p = os.path.join(loc_dir, fname)
        with open(p, 'r', encoding='utf-8', errors='ignore') as fp:
            for line in fp:
                m = re.match(r'^\s*([A-Za-z0-9_.\-]+):(?:\d+)?\s*\"(.*)\"\s*$', line)
                if m:
                    defined_keys[m.group(1)] = (fname, m.group(2))

op_mods = [
    'ben_reaffirmed_czech_ties',
    'ben_loyal_to_republic',
    'ben_declared_independence_opinion',
    'ben_denounced_old_republic',
    'ben_cut_ties',
    'ben_cze_conceded_moravia',
    'ben_cze_rejected_moravia',
    'ben_cze_conceded_silesia',
    'ben_cze_rejected_silesia'
]

for op in op_mods:
    if op in defined_keys:
        print(f"FOUND: {op} -> {defined_keys[op]}")
    else:
        print(f"MISSING: {op}")

