with open('localisation/english/ben_covert_l_english.yml', 'r', encoding='utf-8', errors='replace') as f:
    text = f.read()

for i, l in enumerate(text.splitlines()):
    if '' in l:
        print(f'Line {i+1}: {repr(l)}')

