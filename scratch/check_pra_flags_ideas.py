import os

for root, dirs, files in os.walk('.'):
    if '.git' in root:
        continue
    for f in files:
        if f.endswith('.txt') or f.endswith('.yml'):
            p = os.path.join(root, f)
            with open(p, 'r', encoding='utf-8', errors='ignore') as fp:
                t = fp.read()
            if 'pra_arsenal_fortified' in t:
                print(f'{p} has pra_arsenal_fortified')
            if 'pra_infiltrators_purged' in t:
                print(f'{p} has pra_infiltrators_purged')

