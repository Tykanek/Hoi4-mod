with open('localisation/english/ben_covert_l_english.yml', 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.splitlines()
print(f'Total lines: {len(lines)}')
print('First 10 lines:')
for i, l in enumerate(lines[:10]):
    print(f'{i+1}: {repr(l)}')

print('\nCheck every non-empty line:')
key_errors = []
for i, l in enumerate(lines):
    stripped = l.strip()
    if not stripped or stripped.startswith('#') or stripped == 'l_english:':
        continue
    # HOI4 expects " key:0 \"...\"" or " key: \"...\""
    if not (l.startswith(' ') or l.startswith('\t')):
        key_errors.append((i+1, 'No leading space', l))
    if ':' not in l:
        key_errors.append((i+1, 'No colon', l))
    else:
        # check quotes
        after_colon = l.split(':', 1)[1].strip()
        if not (after_colon.startswith('"') or (len(after_colon) > 1 and after_colon[0].isdigit() and after_colon[1:].strip().startswith('"'))):
            key_errors.append((i+1, 'Malformed value quotes', l))

print(f'Syntax errors found: {len(key_errors)}')
for e in key_errors:
    print(e)

