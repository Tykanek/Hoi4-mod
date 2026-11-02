import os

with open('interface/BEN_focus_icons.gfx', 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.splitlines()
names = [l.split('=')[1].strip().strip('"') for l in lines if 'name =' in l]
print(f'Total icons: {len(names)}')
for n in names[:20]:
    print(n)
