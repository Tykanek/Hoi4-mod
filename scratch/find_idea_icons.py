import os, re

game_dir = r'C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV'

with open(os.path.join(game_dir, 'interface', 'ideas.gfx'), 'r', encoding='utf-8', errors='ignore') as fp:
    t = fp.read()

sprites = re.findall(r'name\s*=\s*\"(GFX_idea_[^\"]*volunteer[^\"]*)\"', t, re.IGNORECASE)
print('Volunteer idea sprites in vanilla:', sprites)

sprites_rest = re.findall(r'name\s*=\s*\"(GFX_idea_[^\"]*restrict[^\"]*)\"', t, re.IGNORECASE)
print('Restriction idea sprites in vanilla:', sprites_rest)

sprites_generic = re.findall(r'name\s*=\s*\"(GFX_idea_generic_[^\"]*)\"', t, re.IGNORECASE)
print('Some generic idea sprites:', [s for s in sprites_generic if any(w in s for w in ['volunteer', 'army', 'war', 'neutral', 'mil'])][:15])

