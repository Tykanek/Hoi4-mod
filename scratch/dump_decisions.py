for path in [
    'common/decisions/ben_emergency_economy.txt',
    'common/decisions/ben_integration.txt',
    'common/decisions/ben_pra_rivalry.txt',
    'common/decisions/categories/ben_decisions_categories.txt'
]:
    print('========================================================')
    print('FILE:', path)
    print('========================================================')
    with open(path, 'r', encoding='utf-8') as f:
        print(f.read())

