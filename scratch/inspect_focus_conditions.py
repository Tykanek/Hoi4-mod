import re

with open(r'common\national_focus\benesov.txt', 'r', encoding='utf-8') as f:
    text = f.read()

focus_chunks = text.split('focus = {')[1:]

print("=== FOCUS COST / DURATION CHECK ===")
non_standard_costs = []
for chunk in focus_chunks:
    m_id = re.search(r'id\s*=\s*([^\s\}]+)', chunk)
    m_cost = re.search(r'\bcost\s*=\s*([^\s\}]+)', chunk)
    if m_id and m_cost:
        fid = m_id.group(1)
        cost_val = float(m_cost.group(1))
        # 30 days is ~4.286
        if abs(cost_val - 4.286) > 0.01:
            non_standard_costs.append((fid, cost_val, round(cost_val * 7)))

print(f"Focuses with non-30-day duration ({len(non_standard_costs)}): {non_standard_costs}")

print("\n=== MUTUALLY EXCLUSIVE PAIRS ===")
mutex_pairs = []
for chunk in focus_chunks:
    m_id = re.search(r'id\s*=\s*([^\s\}]+)', chunk)
    m_mutex = re.findall(r'mutually_exclusive\s*=\s*\{([^}]+)\}', chunk)
    if m_id and m_mutex:
        fid = m_id.group(1)
        for mm in m_mutex:
            foci = re.findall(r'focus\s*=\s*([^\s\}]+)', mm)
            for other in foci:
                pair = tuple(sorted([fid, other]))
                if pair not in mutex_pairs:
                    mutex_pairs.append(pair)

for p in mutex_pairs:
    print(" ", p)

print("\n=== AVAILABLE CONDITIONS ===")
for chunk in focus_chunks:
    m_id = re.search(r'id\s*=\s*([^\s\}]+)', chunk)
    m_avail = re.search(r'available\s*=\s*\{', chunk)
    if m_id and m_avail:
        start = m_avail.end()
        brace_count = 1
        pos = start
        while pos < len(chunk) and brace_count > 0:
            if chunk[pos] == '{': brace_count += 1
            elif chunk[pos] == '}': brace_count -= 1
            pos += 1
        avail = chunk[start:pos-1].strip()
        print(f"Focus {m_id.group(1)} available:")
        for line in avail.splitlines():
            print(f"    {line}")

