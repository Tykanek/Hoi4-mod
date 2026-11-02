with open('localisation/english/ben_covert_l_english.yml', 'rb') as f:
    raw = f.read(100)
print('First 100 bytes of ben_covert_l_english.yml:')
print(raw)

with open('localisation/english/benesov_focus_l_english.yml', 'rb') as f:
    raw_ref = f.read(100)
print('\nFirst 100 bytes of working benesov_focus_l_english.yml:')
print(raw_ref)

with open('localisation/english/mod_characters_l_english.yml', 'rb') as f:
    raw_ref2 = f.read(100)
print('\nFirst 100 bytes of working mod_characters_l_english.yml:')
print(raw_ref2)

