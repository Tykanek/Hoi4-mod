with open('common/ideas/benesov.txt', 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.splitlines()
print(f'Total lines in benesov.txt ideas: {len(lines)}')
print('\nLast 25 lines:')
for l in lines[-25:]:
    print(l)
