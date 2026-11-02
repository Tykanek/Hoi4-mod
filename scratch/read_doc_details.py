import os

game_dir = r'C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV'
doc_dir = os.path.join(game_dir, 'documentation')

with open(os.path.join(doc_dir, 'modifiers_documentation.md'), 'r', encoding='utf-8', errors='ignore') as fp:
    mod_lines = fp.readlines()

print("--- MODIFIERS WITH send_volunteer ---")
for i, l in enumerate(mod_lines):
    if 'send_volunteer' in l.lower():
        for j in range(max(0, i-2), min(len(mod_lines), i+8)):
            print(mod_lines[j], end='')
        print("-" * 30)

with open(os.path.join(doc_dir, 'effects_documentation.md'), 'r', encoding='utf-8', errors='ignore') as fp:
    eff_lines = fp.readlines()

print("\n--- EFFECTS WITH rule OR can_not_declare_war ---")
for i, l in enumerate(eff_lines):
    if 'can_not_declare_war' in l or 'set_rule' in l or 'clear_rule' in l:
        for j in range(max(0, i-2), min(len(eff_lines), i+8)):
            print(eff_lines[j], end='')
        print("-" * 30)

