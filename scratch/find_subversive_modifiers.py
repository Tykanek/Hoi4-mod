import os, re

vanilla = r'C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV'

# Search in common/ideas, common/country_leader, etc.
found = {}
for root, dirs, files in os.walk(os.path.join(vanilla, 'common')):
    for f in files:
        if f.endswith('.txt'):
            p = os.path.join(root, f)
            with open(p, 'r', encoding='utf-8', errors='ignore') as fp:
                for line in fp:
                    if 'foreign_subversive_activites' in line or 'subversive_activites' in line:
                        found[line.strip()] = found.get(line.strip(), 0) + 1

for k, v in sorted(found.items(), key=lambda x: -x[1])[:20]:
    print(f'{v}x: {k}')

