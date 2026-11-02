with open('common/ideas/benesov.txt', 'r', encoding='utf-8') as f:
    text = f.read()

open_b = text.count('{')
close_b = text.count('}')
print(f'Bracket count: {open_b} open, {close_b} close. Balance: {open_b - close_b}')
