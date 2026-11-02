with open('common/national_focus/prague.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if 'id = pra_crush_benesov_threat' in l:
        for j in range(max(0, i-5), min(len(lines), i+35)):
            print(f'{j+1}: {lines[j]}', end='')
        break

