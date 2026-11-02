with open('common/ideas/benesov.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(max(0, 725), min(len(lines), 770)):
    print(f'{i+1}: {lines[i]}', end='')

