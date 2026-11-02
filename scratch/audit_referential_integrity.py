import os
import re
from collections import defaultdict

print("========================================================")
print("COMPREHENSIVE BEN SANITY & REFERENTIAL INTEGRITY AUDIT")
print("========================================================")

# 1. Load all ideas
all_ideas = set()
for f in os.listdir('common/ideas'):
    if f.endswith('.txt'):
        with open(os.path.join('common/ideas', f), 'r', encoding='utf-8', errors='ignore') as fp:
            text = fp.read()
            # extract ideas inside ideas = { ... }
            lines = text.splitlines()
            for line in lines:
                line_c = line.split('#')[0]
                m = re.match(r'^\s*([a-zA-Z0-9_]+)\s*=\s*\{', line_c)
                if m:
                    tok = m.group(1)
                    if tok not in ('ideas', 'country', 'hidden_ideas'):
                        all_ideas.add(tok)

print(f"Total ideas loaded from common/ideas/: {len(all_ideas)}")

# 2. Load all events
all_events = set()
for f in os.listdir('events'):
    if f.endswith('.txt'):
        with open(os.path.join('events', f), 'r', encoding='utf-8', errors='ignore') as fp:
            text = fp.read()
            ev_ids = re.findall(r'id\s*=\s*([a-zA-Z0-9_.]+)', text)
            all_events.update(ev_ids)

print(f"Total events loaded from events/: {len(all_events)}")

# 3. Load all characters
all_characters = set()
for f in os.listdir('common/characters'):
    if f.endswith('.txt'):
        with open(os.path.join('common/characters', f), 'r', encoding='utf-8', errors='ignore') as fp:
            text = fp.read()
            chars = re.findall(r'(\b[A-Za-z0-9_]+)\s*=\s*\{', text)
            for c in chars:
                if c not in ('characters', 'portraits', 'civilian', 'army', 'navy', 'country_leader', 'corps_commander', 'field_marshal', 'navy_leader', 'advisor', 'traits', 'allowed', 'available', 'visible', 'modifier', 'ai_will_do', 'IF', 'limit', 'NOT', 'OR', 'AND'):
                    all_characters.add(c)

print(f"Total characters loaded: {len(all_characters)}")

# 4. Load all opinion modifiers
all_opinions = set()
for root, dirs, files in os.walk('common/opinion_modifiers'):
    for f in files:
        if f.endswith('.txt'):
            with open(os.path.join(root, f), 'r', encoding='utf-8', errors='ignore') as fp:
                text = fp.read()
                ops = re.findall(r'(\b[a-zA-Z0-9_]+)\s*=\s*\{[^{}]*value\s*=', text)
                all_opinions.update(ops)

print(f"Total opinion modifiers loaded: {len(all_opinions)}")

# 5. Load all GFX entries
all_gfx = set()
for root, dirs, files in os.walk('interface'):
    for f in files:
        if f.endswith('.gfx'):
            with open(os.path.join(root, f), 'r', encoding='utf-8', errors='ignore') as fp:
                text = fp.read()
                gfxs = re.findall(r'name\s*=\s*\"([^\"]+)\"', text)
                all_gfx.update(gfxs)

print(f"Total GFX names loaded: {len(all_gfx)}")

# 6. Check BEN Focus Tree references
with open('common/national_focus/benesov.txt', 'r', encoding='utf-8') as fp:
    focus_text = fp.read()

# Check add_ideas, remove_ideas, swap_ideas
ideas_referenced = re.findall(r'(?:add_ideas|remove_ideas|has_idea|add_idea|remove_idea)\s*=\s*([a-zA-Z0-9_]+)', focus_text)
missing_ideas = [i for i in set(ideas_referenced) if i not in all_ideas]
print(f"\nMissing ideas referenced in benesov.txt ({len(missing_ideas)}): {missing_ideas}")

# Check country_event, news_event
events_referenced = re.findall(r'(?:country_event|news_event)\s*=\s*\{\s*id\s*=\s*([a-zA-Z0-9_.]+)', focus_text)
missing_events = [e for e in set(events_referenced) if e not in all_events]
print(f"Missing events referenced in benesov.txt ({len(missing_events)}): {missing_events}")

# Check opinion modifiers
opinions_referenced = re.findall(r'modifier\s*=\s*([a-zA-Z0-9_]+)', focus_text)
# filter for opinion modifier context
missing_opinions = []
for op in set(opinions_referenced):
    if op.startswith('ben_') and op not in all_opinions:
        missing_opinions.append(op)
print(f"Missing opinion modifiers referenced in benesov.txt ({len(missing_opinions)}): {missing_opinions}")

# Check focus icons
focus_icons = re.findall(r'icon\s*=\s*([a-zA-Z0-9_]+)', focus_text)
missing_icons = [icon for icon in set(focus_icons) if icon not in all_gfx]
print(f"Missing focus icons ({len(missing_icons)}): {missing_icons}")


