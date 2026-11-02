import os, re

game_dir = r'C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV'

with open(os.path.join(game_dir, 'interface', 'ideas.gfx'), 'r', encoding='utf-8', errors='ignore') as fp:
    t = fp.read()

# find all GFX_idea_generic_
matches = re.findall(r'name\s*=\s*\"GFX_idea_(generic_[^\"]+)\"', t)
print(f'Total generic idea sprites: {len(matches)}')
for m in sorted(set(matches)):
    print(m)

