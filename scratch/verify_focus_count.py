with open('common/national_focus/benesov.txt', 'r', encoding='utf-8') as f:
    text = f.read()

import re
focuses = re.findall(r'^\s*id\s*=\s*([a-zA-Z0-9_]+)', text, flags=re.MULTILINE)
print(f'Total focuses now: {len(focuses)}')
print(f'Unique focuses: {len(set(focuses))}')

ob = text.count('{')
cb = text.count('}')
print(f'Brackets: {ob} open, {cb} close. Balance: {ob - cb}')
