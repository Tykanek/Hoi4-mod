with open(r'common\national_focus\benesov.txt', 'r', encoding='utf-8') as f:
    text = f.read()

import re

focus_chunks = text.split('focus = {')[1:]

empty_rewards = []
for i, chunk in enumerate(focus_chunks, 1):
    m_id = re.search(r'id\s*=\s*([^\s\}]+)', chunk)
    fid = m_id.group(1) if m_id else f"Unknown_{i}"

    m_reward = re.search(r'completion_reward\s*=\s*\{', chunk)
    if not m_reward:
        empty_rewards.append((fid, "NO completion_reward block"))
    else:
        # extract body
        start = m_reward.end()
        brace = 1
        pos = start
        while pos < len(chunk) and brace > 0:
            if chunk[pos] == '{': brace += 1
            elif chunk[pos] == '}': brace -= 1
            pos += 1
        body = chunk[start:pos-1].strip()
        if not body:
            empty_rewards.append((fid, "EMPTY completion_reward block"))

print(f"Focuses with empty/missing completion_reward ({len(empty_rewards)}): {empty_rewards}")

