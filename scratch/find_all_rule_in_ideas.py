import os, re

game_dir = r'C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV'

for root, dirs, files in os.walk(os.path.join(game_dir, 'common', 'ideas')):
    for f in files:
        if f.endswith('.txt'):
            p = os.path.join(root, f)
            with open(p, 'r', encoding='utf-8', errors='ignore') as fp:
                t = fp.read()
            # find all occurrences of rule = {
            matches = re.finditer(r'([a-zA-Z0-9_]+)\s*=\s*\{[^{}]*rule\s*=\s*\{([^}]+)\}', t)
            for m in matches:
                parent = m.group(1)
                content = m.group(2).strip().replace('\n', ' ')
                print(f'{f}: {parent} -> rule = {{ {content} }}')

