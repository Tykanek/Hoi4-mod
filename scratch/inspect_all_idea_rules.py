import os, re

game_dir = r'C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV'

ideas_dir = os.path.join(game_dir, 'common', 'ideas')

found_ideas = []
for f in os.listdir(ideas_dir):
    if f.endswith('.txt'):
        p = os.path.join(ideas_dir, f)
        with open(p, 'r', encoding='utf-8', errors='ignore') as fp:
            t = fp.read()
        # Find idea blocks containing rule = {
        for m in re.finditer(r'([a-zA-Z0-9_]+)\s*=\s*\{[^{}]*(?:modifier\s*=\s*\{[^{}]*\}[^{}]*)*rule\s*=\s*\{([^{}]*)\}', t):
            found_ideas.append((f, m.group(1), m.group(2).strip()))

print(f'Total ideas found with rule = {{}}: {len(found_ideas)}')
for f, name, r in found_ideas[:20]:
    print(f'{f}: {name} -> rule = {{ {r} }}')

