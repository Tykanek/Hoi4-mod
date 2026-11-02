import os, re
from verify_covert_idea_textures import all_sprites, game_dir

def parse_ideas(path):
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()

    # Find ideas = { country = { ... } }
    # Let's find country = {
    c_idx = text.find('country = {')
    if c_idx == -1:
        c_idx = text.find('country={')
    assert c_idx != -1, f"country = {{ not found in {path}"

    start_idx = text.find('{', c_idx) + 1
    # Count braces to find end of country block
    b = 1
    i = start_idx
    n = len(text)
    while i < n and b > 0:
        if text[i] == '{':
            b += 1
        elif text[i] == '}':
            b -= 1
        i += 1
    country_body = text[start_idx:i-1]

    # Now parse ideas inside country_body
    # Each idea is name = { ... }
    ideas = []
    i = 0
    m = len(country_body)
    while i < m:
        # Match identifier = {
        match = re.match(r'\s*([a-zA-Z0-9_]+)\s*=\s*\{', country_body[i:])
        if match:
            idea_name = match.group(1)
            # Find matching closing brace
            brace_start = i + match.end() - 1
            b = 1
            j = brace_start + 1
            while j < m and b > 0:
                if country_body[j] == '{':
                    b += 1
                elif country_body[j] == '}':
                    b -= 1
                j += 1
            idea_body = country_body[brace_start+1:j-1]
            ideas.append((idea_name, idea_body))
            i = j
        else:
            i += 1
    return ideas

print("=== PARSING IDEAS IN BENESOV.TXT ===")
ben_ideas = parse_ideas('common/ideas/benesov.txt')
print(f'Total country ideas parsed in benesov.txt: {len(ben_ideas)}')

for name, body in ben_ideas:
    pic_m = re.search(r'picture\s*=\s*([a-zA-Z0-9_]+)', body)
    pic = pic_m.group(1) if pic_m else name
    sprite = f'GFX_idea_{pic}'
    exists = sprite in all_sprites
    if not exists:
        print(f'[MISSING SPRITE] {name}: picture={pic} -> {sprite} (NOT DEFINED)')
    else:
        tex, gfx_path, is_mod = all_sprites[sprite]
        full_tex = tex if os.path.isabs(tex) else (tex if is_mod and os.path.exists(tex) else os.path.join(game_dir, tex))
        if not os.path.exists(full_tex):
            print(f'[MISSING TEXTURE] {name}: picture={pic} -> {sprite} -> {full_tex} NOT ON DISK!')

print("\n=== PARSING IDEAS IN PRAGUE.TXT ===")
pra_ideas = parse_ideas('common/ideas/prague.txt')
print(f'Total country ideas parsed in prague.txt: {len(pra_ideas)}')

for name, body in pra_ideas:
    pic_m = re.search(r'picture\s*=\s*([a-zA-Z0-9_]+)', body)
    pic = pic_m.group(1) if pic_m else name
    sprite = f'GFX_idea_{pic}'
    exists = sprite in all_sprites
    if not exists:
        print(f'[MISSING SPRITE] {name}: picture={pic} -> {sprite} (NOT DEFINED)')
    else:
        tex, gfx_path, is_mod = all_sprites[sprite]
        full_tex = tex if os.path.isabs(tex) else (tex if is_mod and os.path.exists(tex) else os.path.join(game_dir, tex))
        if not os.path.exists(full_tex):
            print(f'[MISSING TEXTURE] {name}: picture={pic} -> {sprite} -> {full_tex} NOT ON DISK!')

