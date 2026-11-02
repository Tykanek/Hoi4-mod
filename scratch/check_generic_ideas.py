import os

vanilla = r'C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV'
p = os.path.join(vanilla, 'common', 'ideas', '00_basic_ideas.txt')
if not os.path.exists(p):
    p = os.path.join(vanilla, 'common', 'ideas', 'generic.txt')

with open(p, 'r', encoding='utf-8', errors='ignore') as fp:
    text = fp.read()

import re
matches = re.findall(r'(\b[a-zA-Z0-9_]*subvers[a-zA-Z0-9_]*\s*=\s*[-0-9\.]+)', text)
for m in set(matches):
    print(m)

