import re

with open('common/national_focus/benesov.txt', 'r', encoding='utf-8') as f:
    text = f.read()

icons = re.findall(r'icon\s*=\s*([a-zA-Z0-9_]+)', text)
print(f'Total icon references: {len(icons)}')
custom = [i for i in icons if i.startswith('GFX_focus_BEN_')]
generic = [i for i in icons if not i.startswith('GFX_focus_BEN_')]
print(f'Custom GFX_focus_BEN_: {len(custom)}')
print(f'Generic/Vanilla: {len(generic)}')
for g in generic:
    print(' ', g)
