import re

with open('localisation/english/ben_covert_l_english.yml', 'rb') as f:
    raw = f.read()
while raw.startswith(b'\xef\xbb\xbf'):
    raw = raw[3:]
text = raw.decode('utf-8')

present_keys = {}
for line in text.splitlines():
    stripped = line.strip()
    if stripped.startswith('#') or not stripped or stripped.startswith('l_english:'):
        continue
    m = re.match(r'^([a-zA-Z0-9_\.]+):(?:\d*)\s*\"(.*)\"$', stripped)
    if m:
        present_keys[m.group(1)] = m.group(2)
    else:
        print('Unmatched line:', repr(line))

print(f'Total parsed keys in file: {len(present_keys)}')

# Check required focuses:
focuses = [
    'ben_eyes_on_prague',
    'ben_the_missing_rifles',
    'ben_follow_the_money',
    'ben_a_better_life_in_benesov',
    'ben_the_irregular_migration_scandal',
    'ben_the_invisible_hand_of_benesov',
    'ben_a_city_that_bleeds_its_rival',
    'ben_the_prague_files',
]
for f in focuses:
    for suffix in ['', '_desc']:
        k = f + suffix
        if k not in present_keys:
            print(f'MISSING focus key: {k}')

if 'ben_eyes_on_prague_tt' not in present_keys:
    print('MISSING ben_eyes_on_prague_tt')

# Check decisions
decisions = [
    'ben_covert_operations_category',
    'ben_covert_operations_category_desc',
    'ben_steal_military_intel',
    'ben_steal_military_intel_desc',
    'ben_steal_military_intel_tt',
    'ben_siphon_prague_equipment',
    'ben_siphon_prague_equipment_desc',
    'ben_siphon_prague_equipment_tt',
    'ben_smuggle_dissident_labor',
    'ben_smuggle_dissident_labor_desc',
    'ben_smuggle_dissident_labor_tt',
    'ben_infiltrate_prague_bureaucracy',
    'ben_infiltrate_prague_bureaucracy_desc',
    'ben_infiltrate_prague_bureaucracy_tt',
    'ben_sabotage_prague_factories',
    'ben_sabotage_prague_factories_desc',
    'ben_sabotage_prague_factories_tt',
    'pra_crack_down_on_ben_infiltrators',
    'pra_crack_down_on_ben_infiltrators_desc',
    'pra_crack_down_on_ben_infiltrators_tt',
    'pra_audit_municipal_security',
    'pra_audit_municipal_security_desc',
    'pra_audit_municipal_security_tt',
]
for d in decisions:
    if d not in present_keys:
        print(f'MISSING decision key: {d}')

# Check ideas
ideas = [
    'ben_eyes_on_prague_spirit',
    'ben_eyes_on_prague_spirit_desc',
    'ben_master_infiltrators',
    'ben_master_infiltrators_desc',
    'ben_bleeding_prague',
    'ben_bleeding_prague_desc',
    'ben_archived_trade_ledgers',
    'ben_archived_trade_ledgers_desc',
    'ben_prague_defector_engineers',
    'ben_prague_defector_engineers_desc',
    'pra_bureaucratic_migration_scandal',
    'pra_bureaucratic_migration_scandal_desc',
    'pra_disinformation_turmoil',
    'pra_disinformation_turmoil_desc',
    'pra_arsenal_fortified',
    'pra_arsenal_fortified_desc',
    'pra_infiltrators_purged',
    'pra_infiltrators_purged_desc',
]
for i in ideas:
    if i not in present_keys:
        print(f'MISSING idea key: {i}')

# Check events in events/ben_covert_events.txt
with open('events/ben_covert_events.txt', 'r', encoding='utf-8') as f:
    ev_text = f.read()

ev_titles = re.findall(r'title\s*=\s*([a-zA-Z0-9_\.]+)', ev_text)
ev_descs = re.findall(r'desc\s*=\s*([a-zA-Z0-9_\.]+)', ev_text)
ev_opts = re.findall(r'name\s*=\s*([a-zA-Z0-9_\.]+)', ev_text)

print(f'Event titles found in script: {len(ev_titles)}')
for t in ev_titles:
    if t not in present_keys:
        print(f'MISSING event title: {t}')

for d in ev_descs:
    if d not in present_keys:
        print(f'MISSING event desc: {d}')

for o in ev_opts:
    if o not in present_keys:
        print(f'MISSING event opt: {o}')

print('Audit script completed successfully!')

