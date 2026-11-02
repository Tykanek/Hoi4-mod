import os

game_dir = r'C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV'
loc_dir = os.path.join(game_dir, 'localisation')

for root, dirs, files in os.walk(loc_dir):
    for f in files:
        if 'english' in f:
            p = os.path.join(root, f)
            with open(p, 'r', encoding='utf-8', errors='ignore') as fp:
                t = fp.read()
            if 'can_not_declare_war' in t:
                for line in t.splitlines():
                    if 'can_not_declare_war' in line:
                        print(f'{f}: {line.strip()}')

