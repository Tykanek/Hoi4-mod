with open('interface/BEN_focus_icons.gfx', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.findall(r'(spriteType\s*=\s*\{\s*name\s*=\s*\"GFX_focus_BEN_[^\"]+_shine\".*?legacy_lazy_load\s*=\s*no\s*\})', text, re.DOTALL)
print(f'Matched working shine definitions: {len(matches)}')
if matches:
    print('Sample 1:')
    print(matches[0][:400])
    print('...\n' + matches[0][-100:])

