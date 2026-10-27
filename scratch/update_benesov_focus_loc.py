import os

path = r'localisation\english\benesov_focus_l_english.yml'

with open(path, 'rb') as f:
    raw = f.read()

# Verify initial BOM
assert raw.startswith(b'\xef\xbb\xbf'), "File must start with UTF-8 BOM"

# Split into lines
lines = raw[3:].split(b'\r\n')

# Check first line is l_english:
assert lines[0] == b'l_english:', f"First line must be l_english: but was {lines[0]}"

new_lines = []
for line in lines:
    new_lines.append(line)
    if line.strip() == b'ben_denounced_old_republic:0 "Denounced the Old Republic"':
        new_lines.append(b' ben_cut_ties:0 "Severed Czechoslovak Ties"')
        new_lines.append(b' ben_cze_conceded_moravia:0 "Conceded Moravia"')
        new_lines.append(b' ben_cze_rejected_moravia:0 "Refused to Cede Moravia"')
        new_lines.append(b' ben_cze_conceded_silesia:0 "Conceded Sudeten Silesia"')
        new_lines.append(b' ben_cze_rejected_silesia:0 "Refused to Cede Sudeten Silesia"')
    elif b'ben_demand_moravia_tt:0' in line:
        new_lines[-1] = b' ben_demand_moravia_tt:0 "Sends a formal demand to Czechoslovakia to cede Moravia to Beneshov."'
    elif b'ben_demand_silesia_tt:0' in line:
        new_lines[-1] = b' ben_demand_silesia_tt:0 "Sends a formal demand to Czechoslovakia to cede Sudeten Silesia and Zaolzie to Beneshov."'

# Ensure trailing empty line so it ends with \r\n
if new_lines[-1] != b'':
    new_lines.append(b'')

new_content = b'\xef\xbb\xbf' + b'\r\n'.join(new_lines)

with open(path, 'wb') as f:
    f.write(new_content)

print("Updated benesov_focus_l_english.yml successfully.")
print(f"File size: {len(new_content)} bytes")
print("BOM check:", new_content.startswith(b'\xef\xbb\xbf'))
print("Ends with CRLF:", new_content.endswith(b'\r\n'))

