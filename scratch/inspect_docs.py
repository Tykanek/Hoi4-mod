import os

game_dir = r'C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV'
doc_dir = os.path.join(game_dir, 'documentation')

for f in os.listdir(doc_dir):
    if f.endswith('.md'):
        with open(os.path.join(doc_dir, f), 'r', encoding='utf-8', errors='ignore') as fp:
            t = fp.read()
        if 'can_not_declare_war' in t or 'can_send_volunteers' in t:
            print(f'{f} mentions the rules!')
        if 'send_volunteer' in t:
            print(f'{f} mentions send_volunteer!')

