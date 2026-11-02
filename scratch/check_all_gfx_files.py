import os, re

for root, dirs, files in os.walk('interface'):
    for f in files:
        if f.endswith('.gfx'):
            p = os.path.join(root, f)
            with open(p, 'r', encoding='utf-8', errors='ignore') as fp:
                t = fp.read()
            # check for animation without legacy_lazy_load = no
            # split by spriteType
            parts = t.split('spriteType = {')
            for part in parts[1:]:
                # up to first closing brace at top level
                if 'animation =' in part or 'animation=' in part:
                    # check if legacy_lazy_load is in this sprite block
                    # find where this sprite block ends
                    b_count = 1
                    end_idx = 0
                    for ci, c in enumerate(part):
                        if c == '{':
                            b_count += 1
                        elif c == '}':
                            b_count -= 1
                            if b_count == 0:
                                end_idx = ci
                                break
                    block = part[:end_idx]
                    name_m = re.search(r'name\s*=\s*\"([^\"]+)\"', block)
                    name = name_m.group(1) if name_m else 'unknown'
                    if 'legacy_lazy_load' not in block:
                        print(f'{f}: {name} has animation but NO legacy_lazy_load')

