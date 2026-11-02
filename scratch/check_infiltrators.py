with open('common/ideas/benesov.txt', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('ben_master_infiltrators')
print(repr(text[idx-20:idx+250]))

