import os

for root, dirs, files in os.walk('.'):
    if '.git' in root:
        continue
    for f in files:
        if f.endswith('.txt'):
            p = os.path.join(root, f)
            with open(p, 'r', encoding='utf-8', errors='ignore') as fp:
                t = fp.read()
            if 'set_autonomy' in t and ('BEN' in t or 'PRA' in t):
                print(f'{p} has set_autonomy with BEN/PRA')
            if 'puppet = BEN' in t or 'puppet = PRA' in t:
                print(f'{p} has puppet = BEN/PRA')

