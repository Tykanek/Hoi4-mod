import os, re

game_dir = r'C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV'

print("Searching for rule definitions and occurrences...")
# Let's search common/game_rules, common/ideas, common/country_leader etc.
for root, dirs, files in os.walk(os.path.join(game_dir, 'common')):
    for f in files:
        if f.endswith('.txt'):
            p = os.path.join(root, f)
            with open(p, 'r', encoding='utf-8', errors='ignore') as fp:
                t = fp.read()
            if 'can_not_declare_war' in t:
                print(f'Found can_not_declare_war in {f}')
            if 'can_send_volunteers' in t:
                print(f'Found can_send_volunteers in {f}')

# Let's search modifiers list or documentation if available
doc_path = os.path.join(game_dir, 'documentation')
if os.path.exists(doc_path):
    print('Documentation dir exists:', os.listdir(doc_path))

