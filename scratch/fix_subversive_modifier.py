with open('common/ideas/benesov.txt', 'r', encoding='utf-8') as f:
    text = f.read()

target = 'subversive_activites_up = 0.20'
replacement = 'subversive_activites_upkeep = -0.20'

assert target in text, f"{target} not found"
updated = text.replace(target, replacement)

with open('common/ideas/benesov.txt', 'w', encoding='utf-8') as f:
    f.write(updated)

print('Updated subversive_activites_upkeep in common/ideas/benesov.txt successfully!')

