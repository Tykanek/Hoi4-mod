import os

game_dir = r'C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV'

for root, dirs, files in os.walk(game_dir):
    for f in files:
        if f.endswith('.txt'):
            p = os.path.join(root, f)
            with open(p, 'r', encoding='utf-8', errors='ignore') as fp:
                t = fp.read()
            if 'can_not_declare_war' in t and 'history' in p:
                print('History with can_not_declare_war:', p)
            if 'set_rule' in t and 'can_not_declare_war' in t:
                print('File with set_rule can_not_declare_war:', p)

