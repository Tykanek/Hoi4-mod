import os
import re

for p in ['common/ideas/benesov.txt', 'common/ideas/ben_companies.txt']:
    print('========================================================')
    print('FILE:', p)
    print('========================================================')
    with open(p, 'r', encoding='utf-8') as f:
        text = f.read()

    # parse ideas
    lines = text.splitlines()
    for l in lines:
        if '= {' in l and not any(k in l for k in ['ideas', 'country', 'hidden_ideas', 'allowed', 'modifier', 'targeted_modifier', 'ai_will_do', 'limit', 'if', 'equipment_bonus']):
            print(' ', l.strip())

