import os

game_dir = r'C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV'

with open(os.path.join(game_dir, 'common', 'ideas', 'bulgaria.txt'), 'r', encoding='utf-8', errors='ignore') as fp:
    lines = fp.readlines()

for i, l in enumerate(lines):
    if 'BUL_army_restrictions =' in l:
        for j in range(i, min(len(lines), i + 45)):
            print(lines[j], end='')
        break

