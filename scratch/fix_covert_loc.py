import re

input_path = 'localisation/english/ben_covert_l_english.yml'
with open(input_path, 'rb') as f:
    raw = f.read()

# Strip all leading BOMs
while raw.startswith(b'\xef\xbb\xbf'):
    raw = raw[3:]

text = raw.decode('utf-8')
lines = text.splitlines()

output_lines = []
output_lines.append('l_english:')

for line in lines:
    s = line.strip()
    if not s:
        output_lines.append('')
        continue
    if s == 'l_english:':
        continue
    if s.startswith('#'):
        # Keep comment formatted with single leading space
        output_lines.append(f' {s}')
        continue

    # key entry: match key and value
    m = re.match(r'^\s*([a-zA-Z0-9_\.]+):(?:\d*)\s*\"(.*)\"\s*$', line)
    if m:
        key = m.group(1)
        val = m.group(2)
        output_lines.append(f' {key}:0 "{val}"')
    else:
        print(f'Warning: unhandled line: {line}')
        output_lines.append(line)

content_str = '\r\n'.join(output_lines) + '\r\n'
encoded_bytes = content_str.encode('utf-8')

with open(input_path, 'wb') as f:
    f.write(b'\xef\xbb\xbf' + encoded_bytes)

print('ben_covert_l_english.yml rewritten cleanly!')

