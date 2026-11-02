from parse_actual_ideas import parse_ideas, all_sprites, game_dir
import os, re

pra_ideas = parse_ideas('common/ideas/prague.txt')
print(f'Checking all {len(pra_ideas)} ideas in prague.txt:')
for name, body in pra_ideas:
    pic_m = re.search(r'picture\s*=\s*([a-zA-Z0-9_]+)', body)
    pic = pic_m.group(1) if pic_m else name
    sprite = f'GFX_idea_{pic}'
    if sprite in all_sprites:
        tex, gfx_path, is_mod = all_sprites[sprite]
        full_tex = tex if os.path.isabs(tex) else (tex if is_mod and os.path.exists(tex) else os.path.join(game_dir, tex))
        exists = os.path.exists(full_tex)
        print(f'[OK] {name} -> {sprite} -> {tex} (exists: {exists})')
    else:
        print(f'[MISSING] {name} -> {sprite}')

