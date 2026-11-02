import os, re

vanilla = r'C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV'
with open(os.path.join(vanilla, 'common', 'country_leader', '00_traits.txt'), 'r', encoding='utf-8', errors='ignore') as fp:
    text = fp.read()

for m in re.finditer(r'([a-zA-Z0-9_]+)\s*=\s*\{[^}]*subvers[^}]*\}', text):
    print(m.group(0))

