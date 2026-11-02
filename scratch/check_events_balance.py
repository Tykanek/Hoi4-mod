with open('events/ben_covert_events.txt', 'r', encoding='utf-8') as f:
    t = f.read()
ob = t.count('{')
cb = t.count('}')
print(f'Events balance: {ob} open, {cb} close. Balance: {ob - cb}')
