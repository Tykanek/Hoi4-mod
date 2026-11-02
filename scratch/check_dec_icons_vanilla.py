import os, re

game_dir = r'C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV'

with open(os.path.join(game_dir, 'common', 'decisions', 'generic.txt'), 'r', encoding='utf-8', errors='ignore') as fp:
    t = fp.read()

icons = re.findall(r'icon\s*=\s*([a-zA-Z0-9_]+)', t)
print('Some vanilla decision icons:', set(icons[:15]))

