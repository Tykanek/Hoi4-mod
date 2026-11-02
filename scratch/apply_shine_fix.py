with open('interface/BEN_focus_icons.gfx', 'r', encoding='utf-8') as f:
    text = f.read()

target_sprites = [
    "GFX_focus_BEN_eyes_on_prague_shine",
    "GFX_focus_BEN_the_missing_rifles_shine",
    "GFX_focus_BEN_follow_the_money_shine",
    "GFX_focus_BEN_a_better_life_in_benesov_shine",
    "GFX_focus_BEN_the_irregular_migration_scandal_shine",
    "GFX_focus_BEN_the_invisible_hand_of_benesov_shine",
    "GFX_focus_BEN_a_city_that_bleeds_its_rival_shine",
    "GFX_focus_BEN_the_prague_files_shine",
]

for s in target_sprites:
    assert s in text, f"{s} not found in text"

# For each sprite, we want to ensure `\t\tlegacy_lazy_load = no` is inserted right before the closing `\t}` of the spriteType
# Let's inspect each sprite block
import re

modified_text = text
for s in target_sprites:
    pattern = r'(spriteType\s*=\s*\{\s*name\s*=\s*\"' + re.escape(s) + r'\".*?\t\t\}\n)(\t\})'
    m = re.search(pattern, modified_text, re.DOTALL)
    assert m, f"Pattern not matched for {s}"
    replacement = m.group(1) + "\t\tlegacy_lazy_load = no\n" + m.group(2)
    modified_text = re.sub(pattern, replacement, modified_text, count=1, flags=re.DOTALL)

with open('interface/BEN_focus_icons.gfx', 'w', encoding='utf-8') as f:
    f.write(modified_text)

print("Updated interface/BEN_focus_icons.gfx successfully!")

