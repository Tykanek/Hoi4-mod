import os, re

game_dir = r'C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV'
loc_dir = os.path.join(game_dir, 'localisation')

for root, dirs, files in os.walk(loc_dir):
    for f in files:
        if 'english' in f:
            p = os.path.join(root, f)
            with open(p, 'r', encoding='utf-8', errors='ignore') as fp:
                t = fp.read()
            matches = re.findall(r'(RULE_[A-Z0-9_]*WAR[A-Z0-9_]*:\s*\".*\")', t)
            if matches:
                print(f, matches)

