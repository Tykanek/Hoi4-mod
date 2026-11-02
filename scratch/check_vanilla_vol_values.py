import os, re

game_dir = r'C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV'

ideas_dir = os.path.join(game_dir, 'common', 'ideas')

for root, dirs, files in os.walk(ideas_dir):
    for f in files:
        if f.endswith('.txt'):
            p = os.path.join(root, f)
            with open(p, 'r', encoding='utf-8', errors='ignore') as fp:
                t = fp.read()
            if 'send_volunteer_size' in t:
                # print snippet
                for line in t.splitlines():
                    if any(k in line for k in ['send_volunteer', 'send_volunteers']):
                        print(f'{f}: {line.strip()}')

