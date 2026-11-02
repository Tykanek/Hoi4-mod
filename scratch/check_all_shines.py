with open('interface/BEN_focus_icons.gfx', 'r', encoding='utf-8') as f:
    text = f.read()

import re
shines = re.findall(r'spriteType\s*=\s*\{[^}]*name\s*=\s*\"([^\"]+shine)\"[^}]*\}', text, re.DOTALL | re.IGNORECASE)
print(f'Total shine sprites: {len(shines)}')

# Let's count how many have legacy_lazy_load = no
with_lll = []
without_lll = []
for s in shines:
    # find block for s
    pattern = r'spriteType\s*=\s*\{[^}]*name\s*=\s*\"' + re.escape(s) + r'\"(.*?)\n\t\}'
    m = re.search(pattern, text, re.DOTALL | re.IGNORECASE)
    if m:
        block = m.group(1)
        if 'legacy_lazy_load' in block:
            with_lll.append(s)
        else:
            without_lll.append(s)
    else:
        print(f'Could not match block for {s}')

print(f'Shine sprites with legacy_lazy_load: {len(with_lll)}')
print(f'Shine sprites without legacy_lazy_load: {len(without_lll)}')
print('Without legacy_lazy_load:', without_lll)

