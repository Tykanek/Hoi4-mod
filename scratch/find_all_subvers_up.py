import os

for root, dirs, files in os.walk('.'):
    if '.git' in root or 'scratch' in root: continue
    for f in files:
        if f.endswith(('.txt', '.yml', '.gui', '.gfx')):
            p = os.path.join(root, f)
            with open(p, 'r', encoding='utf-8', errors='ignore') as fp:
                c = fp.read()
                if 'subversive_activites_up' in c:
                    print(f'Match in {p}:')
                    for line in c.splitlines():
                        if 'subversive_activites_up' in line:
                            print(' ', line)

