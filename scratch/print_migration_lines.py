with open('common/ideas/benesov.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if 'pra_bureaucratic_migration_scandal' in l:
        for j in range(max(0, i-2), min(len(lines), i+45)):
            print(f'{j+1}: {lines[j]}', end='')
        break

