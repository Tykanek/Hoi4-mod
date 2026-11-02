import os, re
from verify_covert_idea_textures import all_sprites, game_dir

mod_ideas_files = [
    'common/ideas/benesov.txt',
    'common/ideas/prague.txt',
    'common/ideas/ben_companies.txt',
]

def check_all_mod_ideas():
    missing = []
    found = []

    for path in mod_ideas_files:
        with open(path, 'r', encoding='utf-8') as f:
            text = f.read()

        # Parse idea definitions
        # Find lines like idea_name = { ... picture = X ... }
        idea_blocks = re.findall(r'([a-zA-Z0-9_]+)\s*=\s*\{([^{}]*(?:modifier\s*=\s*\{[^{}]*\}[^{}]*)*)\}', text)
        print(f'=== Checking {path}: {len(idea_blocks)} ideas found ===')
        for idea_name, body in idea_blocks:
            pic_m = re.search(r'picture\s*=\s*([a-zA-Z0-9_]+)', body)
            if pic_m:
                pic = pic_m.group(1)
            else:
                pic = idea_name # HOI4 defaults picture to idea_name if omitted!

            expected_sprite = f'GFX_idea_{pic}'
            if expected_sprite in all_sprites:
                tex, gfx_path, is_mod = all_sprites[expected_sprite]
                full_tex_path = tex if os.path.isabs(tex) else (tex if is_mod and os.path.exists(tex) else os.path.join(game_dir, tex))
                if os.path.exists(full_tex_path):
                    found.append((path, idea_name, pic, expected_sprite, full_tex_path))
                else:
                    missing.append((path, idea_name, pic, expected_sprite, f'Texture file missing: {full_tex_path}'))
            else:
                missing.append((path, idea_name, pic, expected_sprite, 'Sprite not defined'))

    print(f'\nTotal found valid ideas: {len(found)}')
    print(f'Total missing/broken ideas: {len(missing)}')
    for path, idea_name, pic, sprite, reason in missing:
        print(f'BROKEN: in {path} -> idea {idea_name} (pic={pic}): {reason}')

check_all_mod_ideas()

