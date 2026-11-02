import os, re

game_dir = r'C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV'

pictures_to_check = [
    'generic_intel_bonus',
    'generic_spy_political',
    'generic_exploit_mines',
    'generic_goods_red_bonus',
    'generic_research_bonus',
    'generic_disruption',
    'generic_infantry_bonus',
    'generic_spy_intel',
]

def check_sprite(pic_name):
    sprite_name = f'GFX_idea_{pic_name}'
    found_in = []

    # Check mod interface
    for root, dirs, files in os.walk('interface'):
        for f in files:
            if f.endswith('.gfx'):
                p = os.path.join(root, f)
                with open(p, 'r', encoding='utf-8', errors='ignore') as fp:
                    t = fp.read()
                if sprite_name in t:
                    found_in.append(('MOD', f))

    # Check vanilla interface
    for root, dirs, files in os.walk(os.path.join(game_dir, 'interface')):
        for f in files:
            if f.endswith('.gfx'):
                p = os.path.join(root, f)
                with open(p, 'r', encoding='utf-8', errors='ignore') as fp:
                    t = fp.read()
                if sprite_name in t:
                    found_in.append(('VANILLA', f))

    return found_in

print("=== CHECKING SPRITES ===")
for pic in pictures_to_check:
    res = check_sprite(pic)
    if res:
        print(f'[FOUND] picture = {pic} -> GFX_idea_{pic} in {res}')
    else:
        print(f'[MISSING!!!] picture = {pic} -> GFX_idea_{pic} NOT FOUND ANYWHERE!')

