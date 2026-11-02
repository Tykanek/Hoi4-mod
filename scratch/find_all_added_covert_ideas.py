import re

for path in ['events/ben_covert_events.txt', 'common/decisions/ben_covert_operations.txt', 'common/national_focus/benesov.txt']:
    with open(path, 'r', encoding='utf-8') as f:
        t = f.read()
    ideas = re.findall(r'(?:add_ideas|add_timed_idea)\s*=\s*(?:\{\s*idea\s*=\s*([a-zA-Z0-9_]+)|([a-zA-Z0-9_]+))', t)
    print(f'=== Ideas in {path} ===')
    for a, b in ideas:
        idea_name = a or b
        print(' ', idea_name)

