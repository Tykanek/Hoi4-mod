with open('localisation/english/ben_covert_l_english.yml', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if '§' in l:
        print(f'Line {i+1}: {repr(l.strip())}')

