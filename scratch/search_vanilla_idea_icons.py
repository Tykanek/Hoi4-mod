import os, re

game_dir = r'C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV'

with open(os.path.join(game_dir, 'interface', 'ideas.gfx'), 'r', encoding='utf-8', errors='ignore') as fp:
    t = fp.read()

# Let's search for keywords in sprite names or texture files:
keywords = [
    'scandal', 'refugee', 'migration', 'immigrant', 'border', 'police',
    'propaganda', 'disinformation', 'press', 'media', 'radio', 'censorship',
    'strike', 'unrest', 'crisis', 'riot', 'instability', 'turmoil', 'subversive',
    'sabotage', 'infiltrat', 'purge', 'spy', 'intel', 'secret',
    'arsenal', 'fort', 'defense', 'bunker', 'security', 'guard', 'arms'
]

results = {k: [] for k in keywords}

# Match spriteType definitions
matches = re.finditer(r'spriteType\s*=\s*\{[^{}]*name\s*=\s*\"(GFX_idea_([^\"]+))\"[^{}]*texturefile\s*=\s*\"([^\"]+)\"[^{}]*\}', t)

for m in matches:
    full_name = m.group(1)
    short_name = m.group(2)
    tex = m.group(3)
    # check if tex exists on disk
    full_tex = os.path.join(game_dir, tex) if not os.path.isabs(tex) else tex
    exists = os.path.exists(full_tex)
    if not exists:
        continue

    for k in keywords:
        if k in short_name.lower() or k in tex.lower():
            results[k].append((short_name, tex))

for k, list_found in results.items():
    if list_found:
        print(f'=== KEYWORD: {k} ({len(list_found)} found) ===')
        for sn, tx in list_found[:10]:
            print(f'  {sn} -> {tx}')

