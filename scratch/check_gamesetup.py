import os, re

game_dir = r'C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV'
p = os.path.join(game_dir, 'interface', 'frontendgamesetupview.gui')
with open(p, 'r', encoding='utf-8', errors='ignore') as f:
    c = f.read()

for m in re.finditer(r'containerWindowType\s*=\s*\{[^{}]*name\s*=\s*"([^"]+)"', c):
    print('Window:', m.group(1))

# Check backgrounds in this file
for m in re.finditer(r'quadTextureSprite\s*=\s*"([^"]+)"', c):
    print('Sprite:', m.group(1))

