import os
import re

loc_dir = r'localisation\english'
defined_keys = set()
for fname in os.listdir(loc_dir):
    if fname.endswith('.yml'):
        with open(os.path.join(loc_dir, fname), 'r', encoding='utf-8', errors='ignore') as fp:
            for line in fp:
                m = re.match(r'^\s*([A-Za-z0-9_.\-]+):(?:\d+)?\s*\"(.*)\"\s*$', line)
                if m:
                    defined_keys.add(m.group(1))

keys_to_test = [
    'ben_operation_broken_lion',
    'ben_operation_broken_lion_desc',
    'ben_czechoslovak_command_paralysis',
    'ben_czechoslovak_command_paralysis_desc',
    'benesov.26.t',
    'benesov.26.d',
    'benesov.26.a',
    'BEN_andrej_babis',
    'BEN_andrej_babis_desc',
    'BEN_Joe_Biden',
    'BEN_Joe_Biden_desc'
]

for k in keys_to_test:
    if k in defined_keys:
        print(f"FOUND: {k}")
    else:
        print(f"MISSING: {k}")

