import os, re
from collections import defaultdict

loc_dir = r'localisation\english'
defined_keys = set()
for fname in os.listdir(loc_dir):
    if fname.endswith('.yml'):
        with open(os.path.join(loc_dir, fname), 'r', encoding='utf-8', errors='ignore') as fp:
            for line in fp:
                m = re.match(r'^\s*([A-Za-z0-9_.\-]+):(?:\d+)?\s*\"(.*)\"\s*$', line)
                if m:
                    defined_keys.add(m.group(1))

# Check decisions
dec_files = [
    'common/decisions/ben_emergency_economy.txt',
    'common/decisions/ben_integration.txt',
    'common/decisions/ben_pra_bidding_war.txt',
    'common/decisions/ben_pra_rivalry.txt',
    'common/decisions/ben_propaganda.txt'
]

cat_files = [
    'common/decisions/categories/ben_decisions_categories.txt',
    'common/decisions/categories/ben_pra_bidding_war_categories.txt'
]

missing_loc = defaultdict(list)

for cf in cat_files:
    with open(cf, 'r', encoding='utf-8', errors='ignore') as fp:
        cats = re.findall(r'(\b[a-zA-Z0-9_]+)\s*=\s*\{', fp.read())
        for c in cats:
            if c not in ('priority', 'allowed', 'visible', 'custom_icon'):
                if c not in defined_keys:
                    missing_loc['decision_category'].append(c)
                if f"{c}_desc" not in defined_keys:
                    missing_loc['decision_category_desc'].append(f"{c}_desc")

for df in dec_files:
    with open(df, 'r', encoding='utf-8', errors='ignore') as fp:
        text = fp.read()
        decs = re.findall(r'(\b[a-zA-Z0-9_]+)\s*=\s*\{[^{}]*?(?:cost|days_remove|days_re_enable)', text)
        for d in decs:
            if d not in defined_keys:
                missing_loc['decision'].append(d)
            if f"{d}_desc" not in defined_keys:
                missing_loc['decision_desc'].append(f"{d}_desc")
        # tooltips
        tts = re.findall(r'tooltip\s*=\s*([a-zA-Z0-9_]+)', text)
        for tt in tts:
            if tt not in defined_keys:
                missing_loc['tooltip'].append(tt)

# Check events in ben_flavor_events.txt and beneshov_event.txt
for ef in ['events/ben_flavor_events.txt', 'events/beneshov_event.txt', 'events/ben_pra_bidding_war_events.txt', 'events/ben_pra_bidding_war_debug.txt']:
    with open(ef, 'r', encoding='utf-8', errors='ignore') as fp:
        text = fp.read()
        e_titles = re.findall(r'title\s*=\s*([a-zA-Z0-9_.]+)', text)
        e_descs = re.findall(r'desc\s*=\s*([a-zA-Z0-9_.]+)', text)
        e_opts = re.findall(r'name\s*=\s*([a-zA-Z0-9_.]+)', text)
        for t in e_titles:
            if t not in defined_keys: missing_loc['event_title'].append(t)
        for d in e_descs:
            if d not in defined_keys: missing_loc['event_desc'].append(d)
        for o in e_opts:
            if o not in defined_keys: missing_loc['event_option'].append(o)

# Check ideas
for inf in ['common/ideas/benesov.txt', 'common/ideas/ben_companies.txt']:
    with open(inf, 'r', encoding='utf-8', errors='ignore') as fp:
        text = fp.read()
        for line in text.splitlines():
            line_c = line.split('#')[0]
            m = re.match(r'^\s*([a-zA-Z0-9_]+)\s*=\s*\{', line_c)
            if m:
                tok = m.group(1)
                if tok not in ('ideas', 'country', 'hidden_ideas', 'allowed', 'modifier', 'targeted_modifier', 'ai_will_do', 'limit', 'if', 'equipment_bonus', 'research_bonus', 'traits'):
                    if tok not in defined_keys:
                        missing_loc['idea'].append(tok)
                    if f"{tok}_desc" not in defined_keys:
                        missing_loc['idea_desc'].append(f"{tok}_desc")

for cat, items in missing_loc.items():
    print(f"Missing {cat} ({len(items)}): {items}")

