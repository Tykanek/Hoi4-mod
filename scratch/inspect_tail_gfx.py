with open('interface/BEN_focus_icons.gfx', 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.splitlines()
start_idx = 0
for i, l in enumerate(lines):
    if 'Covert Operations' in l or 'eyes_on_prague' in l:
        start_idx = max(0, i - 2)
        break

for idx in range(start_idx, len(lines)):
    print(f'{idx+1}: {lines[idx]}')

