from parse_actual_ideas import parse_ideas, all_sprites, game_dir
import os, re

ben_ideas = parse_ideas('common/ideas/benesov.txt')
print(f'Checking all {len(ben_ideas)} ideas in benesov.txt:')
for name, body in ben_ideas:
    pic_m = re.search(r'picture\s*=\s*([a-zA-Z0-9_]+)', body)
    pic = pic_m.group(1) if pic_m else name
    sprite = f'GFX_idea_{pic}'
    if sprite in all_sprites:
        tex, gfx_path, is_mod = all_sprites[sprite]
        full_tex = tex if os.path.isabs(tex) else (tex if is_mod and os.path.exists(tex) else os.path.join(game_dir, tex))
        exists = os.path.exists(full_tex)
        if not exists:
            print(f'[MISSING TEXTURE] {name} -> {sprite} -> {full_tex}')
    else:
        print(f'[MISSING SPRITE] {name} (pic={pic}) -> {sprite}')

