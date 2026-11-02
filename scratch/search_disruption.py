import os, re

game_dir = r'C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV'

for root, dirs, files in os.walk(game_dir):
    for f in files:
        if f.endswith('.gfx'):
            p = os.path.join(root, f)
            with open(p, 'r', encoding='utf-8', errors='ignore') as fp:
                t = fp.read()
            if 'disruption' in t.lower():
                matches = re.findall(r'name\s*=\s*\"([^\"]*disruption[^\"]*)\"', t, re.IGNORECASE)
                if matches:
                    print(f'{f}: {matches}')

