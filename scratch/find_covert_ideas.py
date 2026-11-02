import re

files = [
    'common/ideas/benesov.txt',
    'common/ideas/prague.txt',
    'common/national_focus/benesov.txt',
    'common/decisions/ben_covert_operations.txt',
    'events/ben_covert_events.txt',
]

ideas_referenced = set()
for path in files:
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()

    # find add_ideas = X, add_timed_idea = { idea = X }, swap_ideas = { ... }
    m1 = re.findall(r'add_ideas\s*=\s*([a-zA-Z0-9_]+)', text)
    ideas_referenced.update(m1)

    m2 = re.findall(r'idea\s*=\s*([a-zA-Z0-9_]+)', text)
    ideas_referenced.update(m2)

    m3 = re.findall(r'add_idea\s*=\s*([a-zA-Z0-9_]+)', text)
    ideas_referenced.update(m3)

covert_ideas = [i for i in ideas_referenced if 'covert' in i or 'pra_' in i or 'ben_' in i]
print('Covert / relevant ideas found:')
for i in sorted(covert_ideas):
    print(' ', i)

