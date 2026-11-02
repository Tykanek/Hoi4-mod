import os

vanilla = r'C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV'
with open(os.path.join(vanilla, 'common', 'country_leader', '00_traits.txt'), 'r', encoding='utf-8', errors='ignore') as fp:
    text = fp.read()

idx = text.find('head_of_intelligence = {')
print(text[idx:idx+300])

