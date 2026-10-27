import os
import re

files = [
    r'common\national_focus\benesov.txt',
    r'events\beneshov_event.txt',
    r'common\ideas\benesov.txt',
    r'common\characters\BEN.txt',
    r'common\country_leader\ben_traits.txt'
]

tooltips = set()
for path in files:
    with open(path, 'r', encoding='utf-8') as f:
        t = f.read()
    for m in re.finditer(r'custom_(?:effect|trigger)_tooltip\s*=\s*([A-Za-z0-9_]+)', t):
        tooltips.add(m.group(1))

print('Tooltips found:', tooltips)

# check against defined keys
loc_dir = r'localisation\english'
defined_keys = set()
for fname in os.listdir(loc_dir):
    if fname.endswith('.yml'):
        p = os.path.join(loc_dir, fname)
        with open(p, 'r', encoding='utf-8', errors='ignore') as fp:
            for line in fp:
                m = re.match(r'^\s*([A-Za-z0-9_.\-]+):(?:\d+)?\s*\"(.*)\"\s*$', line)
                if m:
                    defined_keys.add(m.group(1))

for tt in tooltips:
    if tt in defined_keys:
        print(f'FOUND tooltip: {tt}')
    else:
        print(f'MISSING tooltip: {tt}')

