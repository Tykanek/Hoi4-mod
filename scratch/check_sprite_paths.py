import os, re

game_dir = r'C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV'
with open(os.path.join(game_dir, 'interface', 'ideas.gfx'), 'r', encoding='utf-8', errors='ignore') as fp:
    t = fp.read()

for name in ['GFX_idea_generic_volunteer_expedition_bonus', 'GFX_idea_generic_neutrality_drift_bonus', 'GFX_idea_tfv_can_conscription_crisis']:
    m = re.search(r'name\s*=\s*\"' + name + r'\"[^\}]*texturefile\s*=\s*\"([^\"]+)\"', t)
    if m:
        print(name, '->', m.group(1))
    else:
        print(name, 'not found in ideas.gfx')

