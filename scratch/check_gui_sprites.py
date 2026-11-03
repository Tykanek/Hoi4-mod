import os, re
game_dir = r'C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV'
gui_path = os.path.join(game_dir, 'interface', 'frontendmainview.gui')
with open(gui_path, 'r', encoding='utf-8', errors='ignore') as f:
    c = f.read()

sprites = set(re.findall(r'(?:quadTextureSprite|spriteType)\s*=\s*"([^"]+)"', c))
for s in sorted(sprites):
    print(s)

