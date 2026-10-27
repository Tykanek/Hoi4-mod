import os
import re

loc_dir = r'localisation\english'
defined_keys = set()
for fname in os.listdir(loc_dir):
    if fname.endswith('.yml'):
        p = os.path.join(loc_dir, fname)
        with open(p, 'r', encoding='utf-8', errors='ignore') as fp:
            for line in fp:
                m = re.match(r'^\s*([A-Za-z0-9_.\-]+):(?:\d+)?\s*\"(.*)\"\s*$', line)
                if m:
                    defined_keys.add(m.group(1))

# Search all script files for ben_ tokens
script_dirs = [r'common', r'events', r'history']
ben_tokens = set()

for sdir in script_dirs:
    for root, dirs, files in os.walk(sdir):
        for f in files:
            if f.endswith('.txt'):
                with open(os.path.join(root, f), 'r', encoding='utf-8', errors='ignore') as fp:
                    for line in fp:
                        # strip comments
                        line_clean = line.split('#')[0]
                        # find tokens matching ben_\w+ or BEN_\w+
                        matches = re.findall(r'\b(ben_[a-z0-9_]+|BEN_[a-z0-9_]+)\b', line_clean)
                        for tok in matches:
                            # check the context of tok in the line
                            ben_tokens.add((tok, os.path.join(root, f), line_clean.strip()))

# Distinguish between internal script IDs (flags, variables, event IDs) vs player-visible keys
# Internal flags: set_country_flag, has_country_flag, clr_country_flag, has_global_flag, etc.
# Player visible: add_ideas, add_opinion_modifier, custom_effect_tooltip, custom_trigger_tooltip, focus id, event title/desc/option, etc.

flag_contexts = ['country_flag', 'global_flag', 'unit_leader_flag', 'state_flag']
visible_contexts = ['add_ideas', 'remove_ideas', 'has_idea', 'swap_ideas', 'custom_effect_tooltip', 'custom_trigger_tooltip', 'modifier =', 'opinion_modifier =', 'idea_token =', 'slot =', 'traits =']

categorized = {}
for tok, fpath, line in ben_tokens:
    # Check if it's purely a flag
    is_flag = any(fc in line for fc in flag_contexts)
    # Check if visible
    is_visible = any(vc in line for vc in visible_contexts) or 'focus = {' in line or 'id = ' in line
    if tok not in categorized:
        categorized[tok] = {'files': set(), 'is_flag': False, 'is_visible': False, 'samples': []}
    categorized[tok]['files'].add(os.path.basename(fpath))
    if is_flag:
        categorized[tok]['is_flag'] = True
    if is_visible:
        categorized[tok]['is_visible'] = True
    if len(categorized[tok]['samples']) < 3:
        categorized[tok]['samples'].append(line)

print(f"Total unique ben_/BEN_ tokens: {len(categorized)}")

missing_visible = []
for tok, data in sorted(categorized.items()):
    in_loc = tok in defined_keys
    # if it's visible and not in loc
    if not in_loc:
        # Check if it's only a flag or internal id
        if not data['is_flag'] or data['is_visible']:
            missing_visible.append((tok, data))

print(f"\nTokens not in loc that might be visible: {len(missing_visible)}")
for tok, data in missing_visible:
    print(f"\nToken: {tok}")
    print(f"  Files: {data['files']}")
    print(f"  IsFlag: {data['is_flag']}, IsVisible: {data['is_visible']}")
    for s in data['samples']:
        print(f"    sample: {s}")

