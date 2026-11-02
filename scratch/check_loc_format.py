import re

with open('localisation/english/ben_covert_l_english.yml', 'rb') as f:
    raw = f.read()

while raw.startswith(b'\xef\xbb\xbf'):
    raw = raw[3:]

lines = raw.decode('utf-8').splitlines()

non_colon_0 = []
for i, line in enumerate(lines):
    s = line.strip()
    if not s or s.startswith('#') or s == 'l_english:':
        continue
    if not re.match(r'^\s[a-zA-Z0-9_\.]+:0\s*\".*\"$', line):
        non_colon_0.append((i+1, line))

print(f'Total lines not using standard single-space + :0 format: {len(non_colon_0)}')
for num, l in non_colon_0[:15]:
    print(f'{num}: {l}')

