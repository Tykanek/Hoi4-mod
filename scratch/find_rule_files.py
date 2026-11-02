import os

game_dir = r'C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV'

for root, dirs, files in os.walk(os.path.join(game_dir, 'common')):
    for f in files:
        if f.endswith('.txt'):
            p = os.path.join(root, f)
            with open(p, 'r', encoding='utf-8', errors='ignore') as fp:
                t = fp.read()
            if 'can_not_declare_war' in t and ('rule =' in t or 'rule=' in t):
                print(f'Rule with can_not_declare_war in: {p}')
            if 'can_send_volunteers' in t and ('rule =' in t or 'rule=' in t):
                print(f'Rule with can_send_volunteers in: {p}')

