import os

game_dir = r'C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV'
with open(os.path.join(game_dir, 'common', 'ideas', 'canada.txt'), 'r', encoding='utf-8', errors='ignore') as fp:
    lines = fp.readlines()

for i, l in enumerate(lines):
    if 'can_send_volunteers' in l:
        for j in range(max(0, i-5), min(len(lines), i+15)):
            print(lines[j], end='')
        print('-'*30)

