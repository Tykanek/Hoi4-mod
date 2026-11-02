import os, re

vanilla = r'C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV'

subvers_mods = set()
for root, dirs, files in os.walk(os.path.join(vanilla, 'common')):
    for f in files:
        if f.endswith('.txt'):
            p = os.path.join(root, f)
            with open(p, 'r', encoding='utf-8', errors='ignore') as fp:
                for line in fp:
                    if 'subversive' in line:
                        m = re.findall(r'([a-zA-Z0-9_]*subversive[a-zA-Z0-9_]*)', line)
                        for x in m:
                            subvers_mods.add(x)

print('All vanilla modifiers with "subversive":')
for m in sorted(subvers_mods):
    print(' ', m)

