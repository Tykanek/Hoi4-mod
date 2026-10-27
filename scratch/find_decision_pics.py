import os, re

hoi4_dir = r'C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV'
with open(os.path.join(hoi4_dir, 'interface', 'decisions.gfx'), 'r', encoding='utf-8') as f:
    text = f.read()

pictures = []
for m in re.finditer(r'name\s*=\s*"([^"]*decision_cat_picture[^"]*)"', text):
    pictures.append(m.group(1))

print(pictures[:10])

