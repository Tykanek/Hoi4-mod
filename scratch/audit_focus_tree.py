import re
from collections import defaultdict

with open(r'common\national_focus\benesov.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Parse focuses
# A clean parser splitting by 'focus = {'
focus_chunks = text.split('focus = {')[1:]

focuses = {}
for chunk in focus_chunks:
    # get id
    m_id = re.search(r'id\s*=\s*([^\s\}]+)', chunk)
    if not m_id:
        continue
    fid = m_id.group(1)

    # x, y, cost
    x = re.search(r'\bx\s*=\s*([^\s\}]+)', chunk)
    y = re.search(r'\by\s*=\s*([^\s\}]+)', chunk)
    cost = re.search(r'\bcost\s*=\s*([^\s\}]+)', chunk)
    icon = re.search(r'\bicon\s*=\s*([^\s\}]+)', chunk)

    # prerequisites
    # each prerequisite = { focus = X focus = Y }
    prereqs = []
    for pm in re.finditer(r'prerequisite\s*=\s*\{([^}]+)\}', chunk):
        p_foci = re.findall(r'focus\s*=\s*([^\s\}]+)', pm.group(1))
        if p_foci:
            prereqs.append(p_foci) # OR within one prerequisite block, AND across multiple blocks

    # mutually exclusive
    mut_ex = []
    for mm in re.finditer(r'mutually_exclusive\s*=\s*\{([^}]+)\}', chunk):
        m_foci = re.findall(r'focus\s*=\s*([^\s\}]+)', mm.group(1))
        mut_ex.extend(m_foci)

    # available
    # extract available block
    avail = None
    m_avail = re.search(r'available\s*=\s*\{', chunk)
    if m_avail:
        # find matching brace
        start = m_avail.end()
        brace_count = 1
        pos = start
        while pos < len(chunk) and brace_count > 0:
            if chunk[pos] == '{': brace_count += 1
            elif chunk[pos] == '}': brace_count -= 1
            pos += 1
        avail = chunk[start:pos-1].strip()

    # completion_reward
    reward = None
    m_reward = re.search(r'completion_reward\s*=\s*\{', chunk)
    if m_reward:
        start = m_reward.end()
        brace_count = 1
        pos = start
        while pos < len(chunk) and brace_count > 0:
            if chunk[pos] == '{': brace_count += 1
            elif chunk[pos] == '}': brace_count -= 1
            pos += 1
        reward = chunk[start:pos-1].strip()

    focuses[fid] = {
        'x': x.group(1) if x else None,
        'y': y.group(1) if y else None,
        'cost': cost.group(1) if cost else None,
        'icon': icon.group(1) if icon else None,
        'prereqs': prereqs,
        'mut_ex': mut_ex,
        'avail': avail,
        'reward': reward
    }

print(f"Parsed {len(focuses)} focuses.")

# 1. Check for broken prerequisite references
broken_prereqs = []
for fid, data in focuses.items():
    for p_group in data['prereqs']:
        for p in p_group:
            if p not in focuses:
                broken_prereqs.append((fid, p))

print("Broken prerequisites:", broken_prereqs)

# 2. Check for broken mutually exclusive references
broken_mutex = []
for fid, data in focuses.items():
    for m in data['mut_ex']:
        if m not in focuses:
            broken_mutex.append((fid, m))

print("Broken mutually exclusive:", broken_mutex)

# 3. Check for cycles or unreachability
# Starting focuses (no prerequisites)
roots = [fid for fid, data in focuses.items() if len(data['prereqs']) == 0]
print(f"Roots ({len(roots)}): {roots}")

# Build dependency graph
# A focus F can be reached if for EVERY prerequisite group G, at least one focus in G can be reached
reachable = set(roots)
changed = True
while changed:
    changed = False
    for fid, data in focuses.items():
        if fid in reachable:
            continue
        # check if all prereq groups satisfied
        can_reach = True
        for p_group in data['prereqs']:
            if not any(p in reachable for p in p_group):
                can_reach = False
                break
        if can_reach and data['prereqs']:
            reachable.add(fid)
            changed = True

unreachable = set(focuses.keys()) - reachable
print(f"Unreachable focuses ({len(unreachable)}): {unreachable}")

# 4. Check coordinate collisions
coords = defaultdict(list)
for fid, data in focuses.items():
    coords[(data['x'], data['y'])].append(fid)

collisions = {c: f for c, f in coords.items() if len(f) > 1}
print(f"Coordinate collisions ({len(collisions)}):")
for c, f in collisions.items():
    print(f"  Coord {c}: {f}")

