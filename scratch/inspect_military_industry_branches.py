with open(r'common\national_focus\benesov.txt', 'r', encoding='utf-8') as f:
    text = f.read()

import re

# Let's inspect focuses 1 to 41 (Army, Air, Industry)
focus_chunks = text.split('focus = {')[1:]

print("Auditing Army (1-11), Air (12-23), Physical Industry (29-41)...")
for i, chunk in enumerate(focus_chunks[:41], 1):
    m_id = re.search(r'id\s*=\s*([^\s\}]+)', chunk)
    fid = m_id.group(1) if m_id else f"Unknown_{i}"

    # get reward
    m_reward = re.search(r'completion_reward\s*=\s*\{([^{}]*(?:\{[^{}]*(?:\{[^{}]*\}[^{}]*)*\}[^{}]*)*)\}', chunk)
    reward_text = m_reward.group(1).strip() if m_reward else "None"

    # summarize reward
    ideas_add = re.findall(r'(?:add_ideas|add_idea)\s*=\s*([^\s\}]+)', reward_text)
    ideas_rem = re.findall(r'(?:remove_ideas|remove_idea)\s*=\s*([^\s\}]+)', reward_text)
    factories = re.findall(r'(?:add_extra_state_shared_building_slots|add_building_construction)\s*=\s*\{([^}]+)\}', reward_text)
    events = re.findall(r'(?:country_event|news_event)\s*=\s*\{\s*id\s*=\s*([^\s\}]+)', reward_text)

    print(f"[{i:02d}] {fid}:")
    if ideas_add: print(f"     +Idea: {ideas_add}")
    if ideas_rem: print(f"     -Idea: {ideas_rem}")
    if factories: print(f"     Factories/Slots: {factories}")
    if events: print(f"     Events: {events}")
    if not (ideas_add or ideas_rem or factories or events):
        # print first 2 lines of reward
        first_lines = [l.strip() for l in reward_text.splitlines()[:2]]
        print(f"     Reward: {first_lines}")

