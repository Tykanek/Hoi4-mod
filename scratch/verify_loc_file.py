with open('localisation/english/ben_covert_l_english.yml', 'rb') as f:
    raw = f.read()

print(f'Total byte length: {len(raw)}')
print(f'First 25 bytes: {raw[:25]}')

assert raw.startswith(b'\xef\xbb\xbf'), "Missing BOM"
assert not raw[3:].startswith(b'\xef\xbb\xbf'), "Extra BOM found!"
assert raw[3:15] == b'l_english:\r\n', f"Unexpected header: {raw[3:15]}"

# Check decoding
text = raw.decode('utf-8')
print("Successfully decoded as UTF-8 without errors!")
assert '\ufffd' not in text, "Found replacement character \\ufffd!"

lines = text.splitlines()
print(f'Line count: {len(lines)}')
print(f'Line 1: {repr(lines[0])}')
print(f'Line 2: {repr(lines[1])}')
print(f'Line 5: {repr(lines[4])}')
print(f'Line 6: {repr(lines[5])}')
print(f'Line 7: {repr(lines[6])}')

# Check every non-comment non-empty line after line 1 starts with ' ' and has :0 "
entry_count = 0
for idx, l in enumerate(lines[1:], start=2):
    if not l.strip() or l.strip().startswith('#'):
        continue
    assert l.startswith(' '), f"Line {idx} does not start with space: {repr(l)}"
    assert ':0 "' in l, f"Line {idx} missing ':0 \"': {repr(l)}"
    assert l.endswith('"'), f"Line {idx} does not end with '\"': {repr(l)}"
    entry_count += 1

print(f'Total validated localization entries: {entry_count}')
