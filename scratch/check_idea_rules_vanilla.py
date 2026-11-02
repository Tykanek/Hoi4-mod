import os

game_dir = r'C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV'

# Check all ideas with rule = {
for root, dirs, files in os.walk(os.path.join(game_dir, 'common', 'ideas')):
    for f in files:
        if f.endswith('.txt'):
            p = os.path.join(root, f)
            with open(p, 'r', encoding='utf-8', errors='ignore') as fp:
                t = fp.read()
            if 'rule =' in t or 'rule=' in t:
                for line in t.splitlines():
                    if any(k in line for k in ['can_not_declare_war', 'can_send_volunteers', 'can_boost_other_ideologies', 'can_access_market']):
                        print(f'{f}: {line.strip()}')

