import re
import os

with open(r'common\national_focus\benesov.txt', 'r', encoding='utf-8') as f:
    text = f.read()

focus_ids = re.findall(r'focus\s*=\s*\{\s*id\s*=\s*([^\s\}]+)', text)
print(f"Total focuses count: {len(focus_ids)}")

# load all defined keys
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

missing_names = []
missing_descs = []
for fid in focus_ids:
    if fid not in defined_keys:
        missing_names.append(fid)
    if f"{fid}_desc" not in defined_keys:
        missing_descs.append(f"{fid}_desc")

print(f"Missing focus names ({len(missing_names)}): {missing_names}")
print(f"Missing focus descs ({len(missing_descs)}): {missing_descs}")

