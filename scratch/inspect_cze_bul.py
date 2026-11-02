import os

game_dir = r'C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV'

with open(os.path.join(game_dir, 'common', 'ideas', 'czechoslovakia.txt'), 'r', encoding='utf-8', errors='ignore') as fp:
    t = fp.read()

import re
m = re.search(r'CZE_aggressive_foreign_policy_idea\s*=\s*\{.*?\n\t\}', t, re.DOTALL)
if m:
    print("--- CZE_aggressive_foreign_policy_idea ---")
    print(m.group(0))

with open(os.path.join(game_dir, 'common', 'ideas', 'bulgaria.txt'), 'r', encoding='utf-8', errors='ignore') as fp:
    t = fp.read()

m2 = re.search(r'BUL_army_restrictions\s*=\s*\{.*?\n\t\}', t, re.DOTALL)
if m2:
    print("--- BUL_army_restrictions ---")
    print(m2.group(0))

