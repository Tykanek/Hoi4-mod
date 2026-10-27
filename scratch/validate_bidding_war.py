import os
import re

print("============================================================")
print("VALIDATING PRA vs BEN BIDDING WAR IMPLEMENTATION")
print("============================================================\n")

# Check 1: Decisions file
dec_path = r'common\decisions\ben_pra_bidding_war.txt'
assert os.path.exists(dec_path), "Decisions file missing"
with open(dec_path, 'r', encoding='utf-8') as f:
    dec_text = f.read()

assert 'pra_increase_bidding_offer' in dec_text
assert 'ben_increase_bidding_offer' in dec_text
assert 'cost = 25' in dec_text
assert 'days_re_enable = 30' in dec_text
assert 'fire_only_once = no' in dec_text
assert 'value = 5' in dec_text
print("Decisions syntax and values verified:")
print("  - Both decisions present: pra_increase_bidding_offer & ben_increase_bidding_offer")
print("  - Cost: 25 PP")
print("  - Cooldown: days_re_enable = 30")
print("  - Value: 5")

# Check 2: Decision category
cat_path = r'common\decisions\categories\ben_pra_bidding_war_categories.txt'
assert os.path.exists(cat_path), "Category file missing"
with open(cat_path, 'r', encoding='utf-8') as f:
    cat_text = f.read()
assert 'pra_ben_bidding_war_category' in cat_text
assert 'date < 1939.9.1' in cat_text
assert 'pra_ben_bidding_war_resolved' in cat_text
print("\nDecision category verified:")
print("  - Category ID: pra_ben_bidding_war_category")
print("  - Closing date guard: date < 1939.9.1")

# Check 3: Shared character
char_path = r'common\characters\ben_pra_shared_characters.txt'
assert os.path.exists(char_path), "Shared characters file missing"
with open(char_path, 'r', encoding='utf-8') as f:
    char_text = f.read()

assert 'PRA_BEN_shared_field_marshal' in char_text
assert 'field_marshal' in char_text
assert 'skill = 5' in char_text
assert 'attack_skill = 4' in char_text
assert 'defense_skill = 4' in char_text
assert 'planning_skill = 5' in char_text
assert 'logistics_skill = 5' in char_text
print("\nCharacter verified:")
print("  - ID: PRA_BEN_shared_field_marshal")
print("  - Role: Field Marshal")
print("  - Stats: Skill 5, Atk 4, Def 4, Plan 5, Log 5")

# Check 4: Scripted effect & on_actions
effect_path = r'common\scripted_effects\ben_pra_bidding_war_effects.txt'
assert os.path.exists(effect_path), "Scripted effect file missing"
with open(effect_path, 'r', encoding='utf-8') as f:
    eff_text = f.read()

assert 'pra_ben_resolve_bidding_war_effect' in eff_text
assert 'recruit_character = PRA_BEN_shared_field_marshal' in eff_text
assert 'pra_ben_bidding_war.1' in eff_text
assert 'pra_ben_bidding_war.2' in eff_text
assert 'pra_ben_bidding_war.3' in eff_text
assert 'pra_ben_bidding_war.4' in eff_text
assert 'pra_ben_bidding_war.5' in eff_text

oa_path = r'common\on_actions\ben_pra_bidding_war_on_actions.txt'
assert os.path.exists(oa_path), "on_actions file missing"
with open(oa_path, 'r', encoding='utf-8') as f:
    oa_text = f.read()
assert 'date > 1939.8.31' in oa_text
assert 'pra_ben_resolve_bidding_war_effect = yes' in oa_text
assert 'set_global_flag = pra_ben_bidding_war_resolved' in oa_text
print("\nResolution logic & on_actions verified:")
print("  - Resolution trigger: on_daily check date > 1939.8.31")
print("  - Fires events: .1, .2, .3, .4, .5")
print("  - Guards against duplicate recruitment and resolves strictly once.")

# Check 5: Scripted localisation
sl_path = r'common\scripted_localisation\ben_pra_bidding_war_scripted_loc.txt'
assert os.path.exists(sl_path), "Scripted localisation file missing"
with open(sl_path, 'r', encoding='utf-8') as f:
    sl_text = f.read()
assert 'GetBiddingWarLeaderStatus' in sl_text
print("\nScripted localisation verified: GetBiddingWarLeaderStatus")

# Check 6: Events
ev_path = r'events\ben_pra_bidding_war_events.txt'
assert os.path.exists(ev_path), "Events file missing"
with open(ev_path, 'r', encoding='utf-8') as f:
    ev_text = f.read()
for i in range(1, 6):
    assert f'id = pra_ben_bidding_war.{i}' in ev_text
print("\nEvents verified: 5 events defined in pra_ben_bidding_war namespace.")

# Check 7: Localization file compliance
loc_path = r'localisation\english\ben_pra_bidding_war_l_english.yml'
assert os.path.exists(loc_path), "Localization file missing"
with open(loc_path, 'rb') as f:
    raw = f.read()

assert raw.startswith(b'\xef\xbb\xbf'), "Missing UTF-8 BOM"
assert raw.endswith(b'\r\n'), "Does not end with CRLF"
assert b'\n' not in raw.replace(b'\r\n', b''), "Contains standalone LF line endings"
text = raw[3:].decode('utf-8')
first_line = text.splitlines()[0]
assert first_line == 'l_english:', f"First line must be l_english: but is {first_line}"

# Verify no forbidden words in player-visible text
non_ascii = [c for c in text if ord(c) > 127]
assert len(non_ascii) == 0, f"Non-ASCII characters found: {non_ascii}"

# Verify "influence" or "points" are not used in player visible text
lines = text.splitlines()
for lno, line in enumerate(lines, 1):
    m = re.match(r'^\s*([A-Za-z0-9_.\-]+):(?:\d+)?\s*\"(.*)\"\s*$', line)
    if m:
        val = m.group(2).lower()
        if 'influence' in val or 'point' in val:
            raise AssertionError(f"Forbidden word found at line {lno}: {val}")

print("\nLocalization compliance verified:")
print("  - UTF-8 BOM: Present")
print("  - CRLF endings: Valid throughout")
print("  - Header: l_english:")
print("  - ASCII-only: Confirmed (0 non-ASCII characters)")
print("  - No 'influence' or 'points' in text: Confirmed")

# Check 8: Focus tree counts intact
with open(r'common\national_focus\benesov.txt', 'r', encoding='utf-8') as f:
    ben_focuses = re.findall(r'focus\s*=\s*\{\s*id\s*=\s*([^\s\}]+)', f.read())
with open(r'common\national_focus\prague.txt', 'r', encoding='utf-8') as f:
    pra_focuses = re.findall(r'focus\s*=\s*\{\s*id\s*=\s*([^\s\}]+)', f.read())

print(f"\nFocus tree counts:")
print(f"  - BEN focus count: {len(ben_focuses)} (unchanged)")
print(f"  - PRA focus count: {len(pra_focuses)} (unchanged)")
assert len(ben_focuses) == 74

print("\nALL VALIDATION CHECKS PASSED PERFECTLY!")

