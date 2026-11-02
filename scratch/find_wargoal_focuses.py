import re

def search_wargoals(path, country):
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()

    # find all focus blocks
    focuses = re.findall(r'focus\s*=\s*\{([^{}]*(?:\{[^{}]*(?:\{[^{}]*\}[^{}]*)*\}[^{}]*)*)\}', text)
    print(f'=== {country}: Total focuses {len(focuses)} ===')
    for b in focuses:
        id_m = re.search(r'id\s*=\s*([a-zA-Z0-9_]+)', b)
        fid = id_m.group(1) if id_m else 'unknown'
        if 'create_wargoal' in b or 'declare_war' in b or 'war_goal' in b or 'wargoal' in b:
            print(f'Focus: {fid}')
            # print completion_reward
            m_comp = re.search(r'completion_reward\s*=\s*\{([^{}]*(?:\{[^{}]*(?:\{[^{}]*\}[^{}]*)*\}[^{}]*)*)\}', b)
            if m_comp:
                print('Completion reward:')
                for l in m_comp.group(1).strip().splitlines()[:15]:
                    print('  ', l.strip())
            print('-'*40)

search_wargoals('common/national_focus/prague.txt', 'PRA')
search_wargoals('common/national_focus/benesov.txt', 'BEN')

