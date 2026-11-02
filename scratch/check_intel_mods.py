import os, re

vanilla = r'C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV'

intel_mods = set()
for root, dirs, files in os.walk(os.path.join(vanilla, 'common')):
    for f in files:
        if f.endswith('.txt'):
            p = os.path.join(root, f)
            with open(p, 'r', encoding='utf-8', errors='ignore') as fp:
                for line in fp:
                    if 'intel_' in line or 'operative_' in line:
                        m = re.findall(r'(\b[a-zA-Z0-9_]*(?:intel_|operative_)[a-zA-Z0-9_]*)\s*=', line)
                        for x in m:
                            intel_mods.add(x)

print('Vanilla intel and operative modifiers:')
for m in sorted(intel_mods):
    print(' ', m)

