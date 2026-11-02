import re

for path, expected_keys in [
    ('localisation/english/national_spirit_benesov_l_english.yml', ['ben_military_restraint', 'ben_military_restraint_desc', 'ben_unrestricted_volunteers', 'ben_unrestricted_volunteers_desc']),
    ('localisation/english/national_spirit_prague_l_english.yml', ['pra_military_restraint', 'pra_military_restraint_desc', 'pra_unrestricted_volunteers', 'pra_unrestricted_volunteers_desc'])
]:
    with open(path, 'r', encoding='utf-8-sig') as f:
        t = f.read()
    for k in expected_keys:
        m = re.search(r'^\s*' + k + r':0\s*\"(.*)\"$', t, re.MULTILINE)
        if m:
            print(f'[PASS] {k} -> {m.group(1)[:50]}...')
        else:
            print(f'[FAIL] {k} not found or formatted incorrectly')

