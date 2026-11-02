import os

game_dir = r'C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV'

files_to_check = ['BUL.txt', 'SWE.txt', 'vichy_france.txt', '00_ideologies.txt']

for root, dirs, files in os.walk(os.path.join(game_dir, 'common', 'ideas')):
    for f in files:
        if f in files_to_check or any(k in f for k in ['BUL', 'SWE', 'vichy']):
            p = os.path.join(root, f)
            with open(p, 'r', encoding='utf-8', errors='ignore') as fp:
                t = fp.read()
            for line in t.splitlines():
                if 'can_not_declare_war' in line or 'can_send_volunteers' in line:
                    print(f'{f}: {line}')

# Also check how rule = { ... } is structured inside an idea in BUL.txt or SWE.txt
with open(os.path.join(game_dir, 'common', 'ideas', 'BUL.txt'), 'r', encoding='utf-8', errors='ignore') as fp:
    t = fp.read()

import re
matches = re.findall(r'(\w+\s*=\s*\{[^{}]*rule\s*=\s*\{[^{}]*\}[^{}]*\})', t)
for m in matches[:5]:
    print("--- BUL idea with rule ---")
    print(m)

