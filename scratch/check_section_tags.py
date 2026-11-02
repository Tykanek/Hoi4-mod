with open('localisation/english/ben_covert_l_english.yml', 'r', encoding='utf-8') as f:
    text = f.read()

import re
tags = re.findall(r'§.', text)
print(f'Total section tags found: {len(tags)}')
print('Tag counts:')
from collections import Counter
print(Counter(tags))

