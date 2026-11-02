import os, re, glob

# 1. Load all loc keys
loc_keys = set()
for f in glob.glob('localisation/english/*_l_english.yml'):
    with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
        for line in fp:
            line = line.strip()
            if line.startswith('#') or not line or line.startswith('l_english:'):
                continue
            m = re.match(r'^\s*([a-zA-Z0-9_\.]+)\s*:', line)
            if m:
                loc_keys.add(m.group(1))

print(f'Total English loc keys loaded: {len(loc_keys)}')

# 2. Check the 8 new focuses
focus_keys = [
    'ben_eyes_on_prague', 'ben_eyes_on_prague_desc', 'ben_eyes_on_prague_tt',
    'ben_the_missing_rifles', 'ben_the_missing_rifles_desc',
    'ben_follow_the_money', 'ben_follow_the_money_desc',
    'ben_a_better_life_in_benesov', 'ben_a_better_life_in_benesov_desc',
    'ben_the_irregular_migration_scandal', 'ben_the_irregular_migration_scandal_desc',
    'ben_the_invisible_hand_of_benesov', 'ben_the_invisible_hand_of_benesov_desc',
    'ben_a_city_that_bleeds_its_rival', 'ben_a_city_that_bleeds_its_rival_desc',
    'ben_the_prague_files', 'ben_the_prague_files_desc'
]

# 3. Check decisions & categories
dec_keys = [
    'ben_covert_operations_against_prague', 'ben_covert_operations_against_prague_desc',
    'ben_op_steal_infantry_equipment', 'ben_op_steal_infantry_equipment_desc',
    'ben_op_divert_funds', 'ben_op_divert_funds_desc',
    'ben_op_recruit_defectors', 'ben_op_recruit_defectors_desc',
    'ben_op_disinformation_campaign', 'ben_op_disinformation_campaign_desc',
    'ben_op_political_scandal', 'ben_op_political_scandal_desc',
    'pra_counter_espionage_measures', 'pra_counter_espionage_measures_desc',
    'pra_audit_central_arsenal', 'pra_audit_central_arsenal_desc',
    'pra_purge_infiltrators', 'pra_purge_infiltrators_desc'
]

# 4. Check ideas
idea_keys = [
    'ben_eyes_on_prague_spirit', 'ben_eyes_on_prague_spirit_desc',
    'ben_master_infiltrators', 'ben_master_infiltrators_desc',
    'ben_bleeding_prague', 'ben_bleeding_prague_desc',
    'ben_prague_defector_engineers', 'ben_prague_defector_engineers_desc',
    'pra_bureaucratic_migration_scandal', 'pra_bureaucratic_migration_scandal_desc',
    'pra_disinformation_turmoil', 'pra_disinformation_turmoil_desc',
    'pra_arsenal_fortified', 'pra_arsenal_fortified_desc',
    'pra_infiltrators_purged', 'pra_infiltrators_purged_desc'
]

# 5. Check traits
trait_keys = [
    'ben_mia_revolutionary', 'ben_mia_revolutionary_desc'
]

# 6. Check events
event_keys = [
    'ben_covert.1.t', 'ben_covert.1.d', 'ben_covert.1.a',
    'ben_covert.2.t', 'ben_covert.2.d', 'ben_covert.2.a',
    'ben_covert.3.t', 'ben_covert.3.d', 'ben_covert.3.a',
    'ben_covert.4.t', 'ben_covert.4.d', 'ben_covert.4.a',
    'ben_covert.5.t', 'ben_covert.5.d', 'ben_covert.5.a',
    'ben_covert.6.t', 'ben_covert.6.d', 'ben_covert.6.a', 'ben_covert.6.b',
    'ben_covert.7.t', 'ben_covert.7.d', 'ben_covert.7.a',
    'ben_covert.8.t', 'ben_covert.8.d', 'ben_covert.8.a',
    'ben_covert.10.t', 'ben_covert.10.d', 'ben_covert.10.a', 'ben_covert.10.b',
    'ben_covert.11.t', 'ben_covert.11.d', 'ben_covert.11.a',
    'ben_covert.12.t', 'ben_covert.12.d', 'ben_covert.12.a',
    'ben_covert.20.t', 'ben_covert.20.d', 'ben_covert.20.a',
    'ben_covert.21.t', 'ben_covert.21.d', 'ben_covert.21.a',
    'ben_covert.22.t', 'ben_covert.22.d', 'ben_covert.22.a',
    'ben_covert.23.t', 'ben_covert.23.d', 'ben_covert.23.a',
    'ben_covert.24.t', 'ben_covert.24.d', 'ben_covert.24.a',
    'pra_covert_counter.1.t', 'pra_covert_counter.1.d', 'pra_covert_counter.1.a',
    'pra_covert_counter.2.t', 'pra_covert_counter.2.d', 'pra_covert_counter.2.a', 'pra_covert_counter.2.b',
    'pra_covert_counter.3.t', 'pra_covert_counter.3.d', 'pra_covert_counter.3.a'
]

all_expected = focus_keys + dec_keys + idea_keys + trait_keys + event_keys
missing = [k for k in all_expected if k not in loc_keys]

print(f'Total checked: {len(all_expected)}')
print(f'Missing keys: {len(missing)}')
if missing:
    for m in missing:
        print(f'  MISSING: {m}')
else:
    print('ALL NEW CONTENT LOCALIZATION KEYS PRESENT!')
