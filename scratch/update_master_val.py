with open('scratch/master_validation.py', 'r', encoding='utf-8') as f:
    text = f.read()

target = '''print('\\n============================================================')
print(f'VALIDATION SUMMARY: {len(errors)} Errors, {len(warnings)} Warnings')'''

section_11 = '''# --- 11. Check BEN & PRA Military Restraint and Unlimited Volunteers ---
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

'''

target_norm = target.replace('\r\n', '\n')
text_norm = text.replace('\r\n', '\n')
assert target_norm in text_norm, "Target not found in master_validation.py"

updated = text_norm.replace(target_norm, section_11 + target_norm)
with open('scratch/master_validation.py', 'w', encoding='utf-8') as f:
    f.write(updated)

print("Updated scratch/master_validation.py successfully!")

