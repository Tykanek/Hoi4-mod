with open('common/national_focus/benesov.txt', 'r', encoding='utf-8') as f:
    text = f.read()

import re
all_ids = re.findall(r'^\s*id\s*=\s*([a-zA-Z0-9_]+)', text, flags=re.MULTILINE)
blocks = text.split('focus = {')[1:]
parsed_ids = []
for b in blocks:
    m_id = re.search(r'id\s*=\s*([a-zA-Z0-9_]+)', b)
    if m_id:
        parsed_ids.append(m_id.group(1))

missing = set(all_ids) - set(parsed_ids)
print('Difference between all_ids and split blocks:', missing)
