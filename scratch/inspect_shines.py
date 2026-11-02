import re

with open('interface/BEN_focus_icons.gfx', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's inspect other working shine sprites in this file or other gfx files to see how legacy_lazy_load is placed
sprite_blocks = re.findall(r'SpriteType\s*=\s*\{([^}]+(?:animation\s*=\s*\{[^}]+\}[^}]*)*)\}', text, re.IGNORECASE)
print(f'Total SpriteType blocks: {len(sprite_blocks)}')

# Let's search for existing occurrences of legacy_lazy_load in interface/
for l in text.splitlines():
    if 'legacy_lazy_load' in l:
        print('Found legacy_lazy_load:', l)

