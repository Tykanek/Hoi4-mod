for p in ['common/decisions/categories/ben_decisions_categories.txt', 'common/decisions/ben_covert_operations.txt']:
    with open(p, 'r', encoding='utf-8') as f:
        t = f.read()
    ob = t.count('{')
    cb = t.count('}')
    print(p, f'{ob} open, {cb} close. Balance: {ob - cb}')
