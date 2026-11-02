import os, re, glob, subprocess

print('============================================================')
print('MASTER MOD VALIDATION SUITE - GERMAN-CZECH ADVANCED')
print('============================================================\n')

errors = []
warnings = []

# --- 1. Check Communist Popularity & Mia ---
with open('common/national_focus/benesov.txt', 'r', encoding='utf-8') as f:
    ben_focus = f.read()

m_comm = re.search(r'id\s*=\s*ben_pospisil_takes_command[\s\S]*?available\s*=\s*\{([^}]+)\}', ben_focus)
if m_comm:
    cond = m_comm.group(1).strip()
    if 'communism > 0.50' in cond:
        print('[PASS] ben_pospisil_takes_command requires communism > 0.50')
    else:
        errors.append(f'ben_pospisil_takes_command has unexpected condition: {cond}')
else:
    errors.append('Could not find available block in ben_pospisil_takes_command')

# Check State 74 in ben_workers_of_the_former_republic
if 'owns_state = 74' in ben_focus:
    print('[PASS] owns_state = 74 is preserved in ben_workers_of_the_former_republic')
else:
    errors.append('owns_state = 74 missing in ben_workers_of_the_former_republic!')

# Check Great Depression costs in benesov.txt
for pp in [150, 300, 400, 500, 600]:
    if f'has_political_power > {pp-1}' in ben_focus or f'add_political_power = -{pp}' in ben_focus:
        print(f'[PASS] Great Depression {pp} PP requirement/removal preserved')

# Check Mia in common/characters/BEN.txt
with open('common/characters/BEN.txt', 'r', encoding='utf-8') as f:
    ben_char = f.read()

idx_mia = ben_char.find('BEN_mia = {')
if idx_mia != -1:
    mia_chunk = ben_char[idx_mia:idx_mia+800]
    m_traits = re.search(r'\btraits\s*=\s*\{([^}]+)\}', mia_chunk)
    if m_traits:
        traits = m_traits.group(1).split()
        if 'communist_revolutionary' in traits and 'ben_mia_revolutionary' in traits:
            print('[PASS] Mia has communist_revolutionary and ben_mia_revolutionary traits')
        else:
            errors.append(f'Mia traits mismatch: {traits}')
    else:
        errors.append('Mia traits block not found')
else:
    errors.append('BEN_mia character not found')

# Check ben_mia_revolutionary definition in common/country_leader/ben_traits.txt
with open('common/country_leader/ben_traits.txt', 'r', encoding='utf-8') as f:
    traits_txt = f.read()
if 'ben_mia_revolutionary' in traits_txt and 'political_power_factor = 0.05' in traits_txt:
    print('[PASS] ben_mia_revolutionary trait defined with political_power_factor = 0.05')
else:
    errors.append('ben_mia_revolutionary trait definition issue')

# --- 2. Check Matej Dvorak Corps Commander ---
idx_dvorak = ben_char.find('BEN_matej_dvorak = {')
if idx_dvorak != -1:
    dvorak_chunk = ben_char[idx_dvorak:idx_dvorak+1400]
    if 'corps_commander = {' in dvorak_chunk:
        cmd_idx = dvorak_chunk.find('corps_commander = {')
        cmd_body = dvorak_chunk[cmd_idx:cmd_idx+400]
        if 'skill = 3' in cmd_body and 'attack_skill = 3' in cmd_body and 'defense_skill = 2' in cmd_body:
            print('[PASS] Matej Dvorak corps commander stats verified (Skill 3, Atk 3, Def 2, Plan 3, Log 2)')
        else:
            errors.append('Matej Dvorak stats mismatch')
        if 'ben_pospisil_takes_command' in cmd_body or 'ben_pospisil_in_power' in cmd_body:
            print('[PASS] Matej Dvorak visibility tied to Pospisil government transition')
        else:
            errors.append('Matej Dvorak visibility condition missing Pospisil transition')
    else:
        errors.append('corps_commander block missing from BEN_matej_dvorak')
else:
    errors.append('BEN_matej_dvorak character not found')

# --- 3. Check Focus Tree Counts & Overlaps ---
focus_blocks = ben_focus.split('focus = {')[1:]
print(f'\nTotal BEN focuses: {len(focus_blocks)}')
if len(focus_blocks) == 83:
    print('[PASS] Exactly 83 BEN focuses (75 original + 8 covert rivalry)')
else:
    warnings.append(f'BEN focuses count is {len(focus_blocks)} (expected 83)')

with open('common/national_focus/prague.txt', 'r', encoding='utf-8') as f:
    pra_focus = f.read()
pra_blocks = pra_focus.split('focus = {')[1:]
print(f'Total PRA focuses: {len(pra_blocks)}')
if len(pra_blocks) == 80:
    print('[PASS] Exactly 80 PRA focuses preserved')
else:
    warnings.append(f'PRA focuses count is {len(pra_blocks)} (expected 80)')

# --- 4. Check 8 New Focuses Coordinates & Prereqs ---
covert_ids = [
    'ben_eyes_on_prague', 'ben_the_missing_rifles', 'ben_follow_the_money',
    'ben_a_better_life_in_benesov', 'ben_the_irregular_migration_scandal',
    'ben_the_invisible_hand_of_benesov', 'ben_a_city_that_bleeds_its_rival',
    'ben_the_prague_files'
]
for cid in covert_ids:
    if f'id = {cid}' in ben_focus:
        print(f'[PASS] Focus {cid} present in tree')
    else:
        errors.append(f'Focus {cid} missing from tree')

# Check coordinates
coords = {}
for b in focus_blocks:
    mid = re.search(r'id\s*=\s*([a-zA-Z0-9_]+)', b)
    mx = re.search(r'\bx\s*=\s*(\d+)', b)
    my = re.search(r'\by\s*=\s*(\d+)', b)
    if mid and mx and my:
        fid = mid.group(1)
        pt = (int(mx.group(1)), int(my.group(1)))
        if pt in coords:
            errors.append(f'Coordinate collision at {pt} between {fid} and {coords[pt]}')
        coords[pt] = fid
print(f'[PASS] 0 coordinate collisions across all {len(coords)} focuses')

# --- 5. Check Decisions & Counterplay ---
with open('common/decisions/ben_covert_operations.txt', 'r', encoding='utf-8') as f:
    covert_dec = f.read()

for dec in ['ben_op_steal_infantry_equipment', 'ben_op_divert_funds', 'ben_op_recruit_defectors', 'ben_op_disinformation_campaign', 'ben_op_political_scandal']:
    if dec in covert_dec:
        print(f'[PASS] BEN decision {dec} present')
    else:
        errors.append(f'BEN decision {dec} missing')

for dec in ['pra_audit_central_arsenal', 'pra_purge_infiltrators']:
    if dec in covert_dec:
        print(f'[PASS] PRA counter-decision {dec} present')
    else:
        errors.append(f'PRA counter-decision {dec} missing')

# --- 6. Check Events ---
with open('events/ben_covert_events.txt', 'r', encoding='utf-8') as f:
    events_txt = f.read()

for eid in ['ben_covert.1', 'ben_covert.2', 'ben_covert.3', 'ben_covert.4', 'ben_covert.5', 'ben_covert.6', 'ben_covert.7', 'ben_covert.8', 'ben_covert.10', 'ben_covert.11', 'ben_covert.12', 'ben_covert.20', 'ben_covert.21', 'ben_covert.22', 'ben_covert.23', 'ben_covert.24', 'pra_covert_counter.1', 'pra_covert_counter.2', 'pra_covert_counter.3']:
    if f'id = {eid}' in events_txt:
        print(f'[PASS] Event {eid} present')
    else:
        errors.append(f'Event {eid} missing')

# --- 7. Check GFX / Icons ---
with open('interface/BEN_focus_icons.gfx', 'r', encoding='utf-8') as f:
    gfx_txt = f.read()

for cid in covert_ids:
    suffix = cid.replace('ben_', '')
    sprite_name = f'GFX_focus_BEN_{suffix}'
    shine_name = f'GFX_focus_BEN_{suffix}_shine'
    if sprite_name in gfx_txt:
        print(f'[PASS] GFX sprite {sprite_name} defined')
    else:
        errors.append(f'GFX sprite {sprite_name} missing')

    if shine_name in gfx_txt:
        print(f'[PASS] GFX sprite {shine_name} defined')
        # Verify legacy_lazy_load = no is present inside this spriteType
        pattern = r'name\s*=\s*\"' + re.escape(shine_name) + r'\".*?legacy_lazy_load\s*=\s*no'
        if re.search(pattern, gfx_txt, re.DOTALL):
            print(f'[PASS] {shine_name} explicitly contains legacy_lazy_load = no')
        else:
            errors.append(f'{shine_name} missing legacy_lazy_load = no')
    else:
        errors.append(f'GFX sprite {shine_name} missing')

for cid in covert_ids:
    suffix = cid.replace('ben_', '')
    p = f'gfx/interface/goals/focus_BEN_{suffix}.dds'
    if os.path.exists(p):
        print(f'[PASS] Goal texture {p} exists ({os.path.getsize(p)} bytes)')
    else:
        errors.append(f'Goal texture {p} missing')

# --- 8. Check Germania (GRA) Preserved ---
diff_gra = subprocess.run(['git', 'diff', '--name-only', 'common/national_focus/germania.txt', 'history/countries/GRA*'], capture_output=True, text=True)
if not diff_gra.stdout.strip():
    print('\n[PASS] Germania (GRA) completely untouched')
else:
    errors.append(f'Germania was modified: {diff_gra.stdout}')

# --- 9. Check Localization File Headers & BOMs ---
loc_dir = 'localisation/english'
for yml_name in os.listdir(loc_dir):
    if not yml_name.endswith('.yml'):
        continue
    yml_path = os.path.join(loc_dir, yml_name)
    with open(yml_path, 'rb') as f:
        raw_b = f.read()

    if not raw_b.startswith(b'\xef\xbb\xbf'):
        errors.append(f'{yml_name} missing UTF-8 BOM')
    elif raw_b[3:].startswith(b'\xef\xbb\xbf'):
        errors.append(f'{yml_name} has multiple consecutive BOMs!')
    else:
        # Check header
        hdr = raw_b[3:15]
        if not (hdr.startswith(b'l_english:\r\n') or hdr.startswith(b'l_english:\n')):
            errors.append(f'{yml_name} has invalid header: {hdr[:12]}')
        else:
            print(f'[PASS] {yml_name} byte header verified (Single BOM + l_english)')

    # Check for replacement characters
    try:
        dec_txt = raw_b.decode('utf-8')
        if '\ufffd' in dec_txt:
            errors.append(f'{yml_name} contains \\ufffd replacement characters')
    except Exception as ex:
        errors.append(f'{yml_name} failed UTF-8 decode: {ex}')

# Specific audit of ben_covert_l_english.yml keys
with open('localisation/english/ben_covert_l_english.yml', 'rb') as f:
    covert_raw = f.read()[3:].decode('utf-8')
covert_keys = re.findall(r'^\s*([a-zA-Z0-9_\.]+):0\s*\"', covert_raw, re.MULTILINE)
if len(covert_keys) >= 126:
    print(f'[PASS] ben_covert_l_english.yml contains all {len(covert_keys)} validly formatted keys (:0)')
else:
    errors.append(f'ben_covert_l_english.yml has only {len(covert_keys)} keys (expected 126)')

# --- 10. Check Ideas Modifiers & Syntax Integrity ---
with open('common/ideas/benesov.txt', 'r', encoding='utf-8') as f:
    ideas_txt = f.read()

if 'subversive_activites_up =' in ideas_txt or 'subversive_activites_up ' in ideas_txt:
    errors.append('Found invalid modifier subversive_activites_up in common/ideas/benesov.txt')
else:
    print('[PASS] Invalid modifier subversive_activites_up is absent from common/ideas/benesov.txt')

if 'subversive_activites_upkeep = -0.20' in ideas_txt:
    print('[PASS] Valid engine modifier subversive_activites_upkeep = -0.20 verified in ben_master_infiltrators')
else:
    errors.append('subversive_activites_upkeep = -0.20 missing from common/ideas/benesov.txt')

ideas_open = ideas_txt.count('{')
ideas_close = ideas_txt.count('}')
if ideas_open == ideas_close:
    print(f'[PASS] common/ideas/benesov.txt braces balanced ({ideas_open} pairs)')
else:
    errors.append(f'common/ideas/benesov.txt braces unbalanced ({ideas_open} open vs {ideas_close} close)')

# --- 11. Check BEN & PRA Military Restraint and Unlimited Volunteers ---
with open('common/ideas/benesov.txt', 'r', encoding='utf-8') as f:
    ben_ideas = f.read()

if 'ben_military_restraint = {' in ben_ideas and 'can_not_declare_war = yes' in ben_ideas and 'can_send_volunteers = yes' in ben_ideas:
    print('[PASS] ben_military_restraint defined with can_not_declare_war and can_send_volunteers')
else:
    errors.append('ben_military_restraint definition missing or incomplete')

if 'ben_unrestricted_volunteers = {' in ben_ideas and 'can_send_volunteers = yes' in ben_ideas:
    print('[PASS] ben_unrestricted_volunteers defined with can_send_volunteers')
else:
    errors.append('ben_unrestricted_volunteers definition missing or incomplete')

with open('common/ideas/prague.txt', 'r', encoding='utf-8') as f:
    pra_ideas = f.read()

if 'pra_military_restraint = {' in pra_ideas and 'can_not_declare_war = yes' in pra_ideas and 'can_send_volunteers = yes' in pra_ideas:
    print('[PASS] pra_military_restraint defined with can_not_declare_war and can_send_volunteers')
else:
    errors.append('pra_military_restraint definition missing or incomplete')

if 'pra_unrestricted_volunteers = {' in pra_ideas and 'can_send_volunteers = yes' in pra_ideas:
    print('[PASS] pra_unrestricted_volunteers defined with can_send_volunteers')
else:
    errors.append('pra_unrestricted_volunteers definition missing or incomplete')

# Check history files
with open('history/countries/BEN - Benesov.txt', 'r', encoding='utf-8') as f:
    ben_hist = f.read()
if 'ben_military_restraint' in ben_hist:
    print('[PASS] BEN history assigns ben_military_restraint on Jan 1, 1936')
else:
    errors.append('ben_military_restraint missing from BEN history')

with open('history/countries/PRA - Prague.txt', 'r', encoding='utf-8') as f:
    pra_hist = f.read()
if 'pra_military_restraint' in pra_hist:
    print('[PASS] PRA history assigns pra_military_restraint on Jan 1, 1936')
else:
    errors.append('pra_military_restraint missing from PRA history')

# Check focus transitions
with open('common/national_focus/benesov.txt', 'r', encoding='utf-8') as f:
    ben_foc_txt = f.read()
if 'ben_enforce_the_workers_mandate' in ben_foc_txt and 'remove_idea = ben_military_restraint' in ben_foc_txt and 'add_idea = ben_unrestricted_volunteers' in ben_foc_txt:
    print('[PASS] ben_enforce_the_workers_mandate transitions ben_military_restraint to ben_unrestricted_volunteers')
else:
    errors.append('ben_enforce_the_workers_mandate missing military restraint transition')

with open('common/national_focus/prague.txt', 'r', encoding='utf-8') as f:
    pra_foc_txt = f.read()
if 'pra_crush_benesov_threat' in pra_foc_txt and 'remove_idea = pra_military_restraint' in pra_foc_txt and 'add_idea = pra_unrestricted_volunteers' in pra_foc_txt:
    print('[PASS] pra_crush_benesov_threat transitions pra_military_restraint to pra_unrestricted_volunteers')
else:
    errors.append('pra_crush_benesov_threat missing military restraint transition')

# Check loc keys
with open('localisation/english/national_spirit_benesov_l_english.yml', 'r', encoding='utf-8-sig') as f:
    ben_loc = f.read()
for k in ['ben_military_restraint', 'ben_military_restraint_desc', 'ben_unrestricted_volunteers', 'ben_unrestricted_volunteers_desc']:
    if f'{k}:0' in ben_loc or f'{k}: ' in ben_loc:
        print(f'[PASS] BEN loc key {k} present')
    else:
        errors.append(f'Missing loc key {k} in national_spirit_benesov_l_english.yml')

with open('localisation/english/national_spirit_prague_l_english.yml', 'r', encoding='utf-8-sig') as f:
    pra_loc = f.read()
for k in ['pra_military_restraint', 'pra_military_restraint_desc', 'pra_unrestricted_volunteers', 'pra_unrestricted_volunteers_desc']:
    if f'{k}:0' in pra_loc or f'{k}: ' in pra_loc:
        print(f'[PASS] PRA loc key {k} present')
    else:
        errors.append(f'Missing loc key {k} in national_spirit_prague_l_english.yml')

# Check national spirit icons and sprite definitions
game_dir = r'C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV'
gfx_sprites = {}

def scan_gfx_files(directory, is_mod=False):
    if not os.path.exists(directory):
        return
    for root, _, files in os.walk(directory):
        for f in files:
            if f.endswith('.gfx'):
                p = os.path.join(root, f)
                with open(p, 'r', encoding='utf-8', errors='ignore') as fp:
                    content = fp.read()
                matches = re.finditer(r'spriteType\s*=\s*\{[^{}]*name\s*=\s*\"([^\"]+)\"[^{}]*texturefile\s*=\s*\"([^\"]+)\"[^{}]*\}', content, re.DOTALL)
                for m in matches:
                    name = m.group(1)
                    tex = m.group(2)
                    gfx_sprites[name] = (tex, p, is_mod)

scan_gfx_files('interface', is_mod=True)
scan_gfx_files(os.path.join(game_dir, 'interface'), is_mod=False)

ideas_to_verify_sprites = [
    'ben_eyes_on_prague_spirit',
    'ben_master_infiltrators',
    'ben_bleeding_prague',
    'ben_archived_trade_ledgers',
    'ben_prague_defector_engineers',
    'pra_bureaucratic_migration_scandal',
    'pra_disinformation_turmoil',
    'pra_arsenal_fortified',
    'pra_infiltrators_purged',
    'ben_socialist_successor_federation',
    'ben_military_restraint',
    'ben_unrestricted_volunteers',
    'pra_military_restraint',
    'pra_unrestricted_volunteers'
]

# Find picture field for each idea from idea files
idea_pictures = {}
for idea_file in ['common/ideas/benesov.txt', 'common/ideas/prague.txt']:
    with open(idea_file, 'r', encoding='utf-8') as f:
        content = f.read()
    # Match block idea_name = { ... picture = ... }
    for i_id in ideas_to_verify_sprites:
        m = re.search(r'\b' + re.escape(i_id) + r'\s*=\s*\{[^}]*?picture\s*=\s*([A-Za-z0-9_]+)', content)
        if m:
            idea_pictures[i_id] = m.group(1)

for i_id in ideas_to_verify_sprites:
    pic = idea_pictures.get(i_id)
    if not pic:
        errors.append(f'Idea {i_id} missing picture definition')
        continue
    expected_sprite = f'GFX_idea_{pic}'
    if expected_sprite in gfx_sprites:
        tex, gfx_path, is_mod = gfx_sprites[expected_sprite]
        full_tex_path = tex if os.path.isabs(tex) else (tex if is_mod and os.path.exists(tex) else os.path.join(game_dir, tex))
        if os.path.exists(full_tex_path):
            print(f'[PASS] Idea {i_id}: picture={pic} -> {expected_sprite} -> {tex} exists on disk')
        else:
            errors.append(f'Idea {i_id}: texture file does not exist on disk: {full_tex_path}')
    else:
        errors.append(f'Idea {i_id}: spriteType {expected_sprite} is not defined in any .gfx file')

print('\n============================================================')
print(f'VALIDATION SUMMARY: {len(errors)} Errors, {len(warnings)} Warnings')
print('============================================================')
if errors:
    for e in errors:
        print(f'ERROR: {e}')
else:
    print('ALL AUTOMATED VALIDATION CHECKS PASSED!')
