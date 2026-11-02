import os, re

vanilla = r'C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV'

# Extract all modifier keys from vanilla common/
vanilla_modifiers = set()
for root, dirs, files in os.walk(os.path.join(vanilla, 'common')):
    for f in files:
        if f.endswith('.txt'):
            p = os.path.join(root, f)
            with open(p, 'r', encoding='utf-8', errors='ignore') as fp:
                for line in fp:
                    line = line.strip()
                    if line.startswith('#'): continue
                    m = re.match(r'^\s*([a-zA-Z0-9_]+)\s*=\s*[-0-9\.]+', line)
                    if m:
                        vanilla_modifiers.add(m.group(1))

print(f'Total vanilla modifier keys found: {len(vanilla_modifiers)}')

# Check our added ideas in common/ideas/benesov.txt
with open('common/ideas/benesov.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Grab all modifiers in the covert section
idx = text.find('# Anti-Prague Covert Rivalry Spirits')
covert_section = text[idx:]
lines = covert_section.splitlines()

checked = []
for l in lines:
    l = l.strip()
    if l.startswith('#'): continue
    m = re.match(r'^\s*([a-zA-Z0-9_]+)\s*=\s*[-0-9\.]+', l)
    if m:
        key = m.group(1)
        checked.append(key)
        if key in vanilla_modifiers:
            print(f'[VALID] {key}')
        else:
            print(f'[INVALID] {key} NOT found in vanilla common/!')

print(f'\nTotal modifiers checked: {len(checked)}')

