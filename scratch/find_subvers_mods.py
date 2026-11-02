import os

vanilla = r'C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV'
p = os.path.join(vanilla, 'common', 'modifier_definitions', 'modifier_definitions.txt')

with open(p, 'r', encoding='utf-8', errors='ignore') as fp:
    text = fp.read()

import re
matches = re.findall(r'([a-zA-Z0-9_]*subvers[a-zA-Z0-9_]*)', text)
print('Unique modifier names containing subvers in modifier_definitions.txt:')
for m in sorted(set(matches)):
    print(' ', m)
