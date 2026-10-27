import os, re

hoi4_dir = r'C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV'
with open(os.path.join(hoi4_dir, 'interface', '_leader_portraits.gfx'), 'r', encoding='utf-8') as f:
    text = f.read()

for m in re.finditer(r'name\s*=\s*"([^"]*generic_land[^"]*)"', text):
    print(m.group(1))

