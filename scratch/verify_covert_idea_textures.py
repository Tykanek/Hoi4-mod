import os, re

game_dir = r'C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV'

ideas_to_check = {
    'ben_eyes_on_prague_spirit': 'generic_intel_bonus',
    'ben_master_infiltrators': 'generic_spy_political',
    'ben_bleeding_prague': 'generic_exploit_mines',
    'ben_archived_trade_ledgers': 'generic_goods_red_bonus',
    'ben_prague_defector_engineers': 'generic_research_bonus',
    'pra_bureaucratic_migration_scandal': 'generic_immigration',
    'pra_disinformation_turmoil': 'generic_spy_coup',
    'pra_arsenal_fortified': 'generic_supply_depot',
    'pra_infiltrators_purged': 'generic_secret_police',
    'ben_socialist_successor_federation': 'ben_pospisil_doctrine',
}

all_sprites = {}

def scan_gfx(dir_path, is_mod=False):
    for root, dirs, files in os.walk(dir_path):
        for f in files:
            if f.endswith('.gfx'):
                p = os.path.join(root, f)
                with open(p, 'r', encoding='utf-8', errors='ignore') as fp:
                    content = fp.read()
                matches = re.finditer(r'spriteType\s*=\s*\{[^{}]*name\s*=\s*\"([^\"]+)\"[^{}]*texturefile\s*=\s*\"([^\"]+)\"[^{}]*\}', content, re.DOTALL)
                for m in matches:
                    name = m.group(1)
                    tex = m.group(2)
                    all_sprites[name] = (tex, p, is_mod)

scan_gfx('interface', is_mod=True)
scan_gfx(os.path.join(game_dir, 'interface'), is_mod=False)

all_ok = True
for idea_id, pic in ideas_to_check.items():
    expected_sprite = f'GFX_idea_{pic}'
    if expected_sprite in all_sprites:
        tex, gfx_path, is_mod = all_sprites[expected_sprite]
        full_tex_path = tex if os.path.isabs(tex) else (tex if is_mod and os.path.exists(tex) else os.path.join(game_dir, tex))
        exists = os.path.exists(full_tex_path)
        if exists:
            print(f'[PASS] {idea_id}: picture={pic} -> {expected_sprite} -> {tex} (exists on disk)')
        else:
            print(f'[FAIL] {idea_id}: texture not on disk: {full_tex_path}')
            all_ok = False
    else:
        print(f'[FAIL] {idea_id}: sprite {expected_sprite} not defined')
        all_ok = False

if all_ok:
    print("\nALL COVERT NATIONAL SPIRIT ICONS SUCCESSFULLY VERIFIED!")
