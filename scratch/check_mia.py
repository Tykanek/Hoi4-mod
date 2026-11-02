with open('common/characters/BEN.txt', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('BEN_mia = {')
print(text[idx:idx+600])

