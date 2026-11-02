with open('common/national_focus/benesov.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if 'id = ben_enforce_the_workers_mandate' in l:
        for j in range(max(0, i-2), min(len(lines), i+65)):
            print(f'{j+1}: {lines[j]}', end='')
        break

