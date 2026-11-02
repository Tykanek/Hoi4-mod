import os, re

game_dir = r'C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV'

# Check all ideas in common/ideas
for root, dirs, files in os.walk(os.path.join(game_dir, 'common', 'ideas')):
    for f in files:
        if f.endswith('.txt'):
            p = os.path.join(root, f)
            with open(p, 'r', encoding='utf-8', errors='ignore') as fp:
                t = fp.read()
            if 'rule = {' in t or 'rule={' in t:
                # print matching idea names and the rule
                matches = re.finditer(r'([a-zA-Z0-9_]+)\s*=\s*\{[^{}]*(?:modifier\s*=\s*\{[^{}]*\}[^{}]*)*rule\s*=\s*\{([^{}]+)\}', t)
                for m in matches:
                    print(f'{f}: {m.group(1)} has rule = {{ {m.group(2).strip()} }}')

