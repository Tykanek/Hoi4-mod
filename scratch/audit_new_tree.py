with open('common/national_focus/benesov.txt', 'r', encoding='utf-8') as f:
    text = f.read()

import re

# Parse every focus
blocks = text.split('focus = {')[1:]
focus_map = {}
coords = {}

for b in blocks:
    m_id = re.search(r'id\s*=\s*([a-zA-Z0-9_]+)', b)
    m_x = re.search(r'\bx\s*=\s*(\d+)', b)
    m_y = re.search(r'\by\s*=\s*(\d+)', b)
    m_cost = re.search(r'cost\s*=\s*([\d\.]+)', b)
    m_pre = re.findall(r'prerequisite\s*=\s*\{\s*focus\s*=\s*([a-zA-Z0-9_]+)\s*\}', b)
    
    if m_id and m_x and m_y:
        fid = m_id.group(1)
        x = int(m_x.group(1))
        y = int(m_y.group(1))
        cost = m_cost.group(1) if m_cost else None
        focus_map[fid] = {'x': x, 'y': y, 'cost': cost, 'pre': m_pre}
        if (x, y) in coords:
            print(f'COLLISION at ({x}, {y}): {fid} and {coords[(x, y)]}')
        coords[(x, y)] = fid

print(f'Total parsed: {len(focus_map)}')
print(f'Unique coordinates: {len(coords)}')

# Check prerequisites
broken_pre = 0
for fid, data in focus_map.items():
    for p in data['pre']:
        if p not in focus_map:
            print(f'BROKEN PREREQUISITE: {fid} -> {p}')
            broken_pre += 1

if broken_pre == 0:
    print('All prerequisites are 100% valid!')

# Check cost
non_30_days = 0
for fid, data in focus_map.items():
    if data['cost'] != '4.286':
        print(f'Non-standard cost: {fid} has cost={data["cost"]}')
        non_30_days += 1

if non_30_days == 0:
    print('All 84 focuses have cost = 4.286 (30 days)!')
