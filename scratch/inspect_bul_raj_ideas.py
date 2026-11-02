import os

game_dir = r'C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV'

paths = [
    os.path.join(game_dir, 'common', 'ideas', 'bulgaria.txt'),
    os.path.join(game_dir, 'common', 'ideas', 'british_raj_goe.txt'),
]

for p in paths:
    if os.path.exists(p):
        print("=== Checking:", p)
        with open(p, 'r', encoding='utf-8', errors='ignore') as fp:
            lines = fp.readlines()
        for i, l in enumerate(lines):
            if 'can_not_declare_war' in l or 'can_send_volunteers' in l:
                start = max(0, i - 10)
                end = min(len(lines), i + 15)
                for j in range(start, end):
                    print(lines[j], end='')
                print("-" * 40)

