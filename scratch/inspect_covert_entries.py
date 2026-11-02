import re

with open('localisation/english/ben_covert_l_english.yml', 'rb') as f:
    raw = f.read()

while raw.startswith(b'\xef\xbb\xbf'):
    raw = raw[3:]

lines = raw.decode('utf-8').splitlines()

parsed_entries = []
for i, line in enumerate(lines):
    s = line.strip()
    if not s:
        parsed_entries.append(('blank', ''))
        continue
    if s.startswith('#'):
        parsed_entries.append(('comment', s))
        continue
    if s == 'l_english:':
        parsed_entries.append(('header', s))
        continue

    # key pattern
    m = re.match(r'^\s*([a-zA-Z0-9_\.]+):\s*\"(.*)\"\s*$', line)
    if not m:
        print(f'Failed to parse line {i+1}: {line}')
    else:
        k = m.group(1)
        val = m.group(2)
        parsed_entries.append(('entry', (k, val)))

print(f'Total parsed items: {len(parsed_entries)}')
entries_only = [item for t, item in parsed_entries if t == 'entry']
print(f'Total key-value entries: {len(entries_only)}')

