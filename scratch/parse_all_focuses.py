def parse_focus_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()

    focuses = []
    i = 0
    n = len(text)
    while i < n:
        if text[i:i+5] == 'focus' and (i == 0 or text[i-1] in ' \t\n\r'):
            # check for = {
            eq_idx = text.find('=', i+5)
            brace_idx = text.find('{', eq_idx+1)
            if eq_idx != -1 and brace_idx != -1 and not text[i+5:eq_idx].strip():
                # count braces
                b = 1
                j = brace_idx + 1
                while j < n and b > 0:
                    if text[j] == '{':
                        b += 1
                    elif text[j] == '}':
                        b -= 1
                    j += 1
                focus_body = text[brace_idx+1:j-1]
                focuses.append(focus_body)
                i = j
                continue
        i += 1
    return focuses

import re

for tag, path in [('PRA', 'common/national_focus/prague.txt'), ('BEN', 'common/national_focus/benesov.txt')]:
    focs = parse_focus_file(path)
    print(f'=== {tag}: Total focuses parsed = {len(focs)} ===')
    for b in focs:
        id_m = re.search(r'id\s*=\s*([a-zA-Z0-9_]+)', b)
        fid = id_m.group(1) if id_m else 'unknown'
        if any(k in b for k in ['create_wargoal', 'declare_war', 'war_goal', 'wargoal']):
            print(f'Focus ID: {fid}')
            # print rewards
            m_comp = re.search(r'completion_reward\s*=\s*\{([^{}]*(?:\{[^{}]*(?:\{[^{}]*\}[^{}]*)*\}[^{}]*)*)\}', b)
            if m_comp:
                print('Completion reward snippet:')
                for l in m_comp.group(1).strip().splitlines()[:20]:
                    print('  ', l.strip())
            print('-'*40)

