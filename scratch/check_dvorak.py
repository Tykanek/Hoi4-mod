with open('common/characters/BEN.txt', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('BEN_matej_dvorak = {')
print(text[idx:idx+1200])

