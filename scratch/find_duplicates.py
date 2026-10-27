import os
import re
from collections import defaultdict

loc_dir = r'localisation\english'
defined_keys = defaultdict(list)

for fname in os.listdir(loc_dir):
    if fname.endswith('.yml'):
        p = os.path.join(loc_dir, fname)
        with open(p, 'r', encoding='utf-8', errors='ignore') as fp:
            for lno, line in enumerate(fp, 1):
                m = re.match(r'^\s*([A-Za-z0-9_.\-]+):(?:\d+)?\s*\"(.*)\"\s*$', line)
                if m:
                    defined_keys[m.group(1)].append((fname, lno, m.group(2)))

ben_related_duplicates = {}
all_duplicates = {}

for k, v in defined_keys.items():
    if len(v) > 1:
        all_duplicates[k] = v
        # Check if related to BEN
        is_ben = any(
            'ben' in f.lower() or 
            'ben' in k.lower() or 
            'pospisil' in k.lower() or 
            'dvorak' in k.lower() or 
            k.startswith('BEN')
            for f, _, _ in v
        )
        if is_ben:
            ben_related_duplicates[k] = v

print(f"Total duplicate keys across all English files: {len(all_duplicates)}")
print(f"BEN-related duplicate keys: {len(ben_related_duplicates)}")

for k, v in ben_related_duplicates.items():
    print(f"\nKey: {k}")
    for fname, lno, val in v:
        print(f"  {fname}:{lno} -> \"{val}\"")

