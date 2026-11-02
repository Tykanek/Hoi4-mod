with open('common/characters/BEN.txt', 'r', encoding='utf-8') as f:
    text = f.read()

idx_mia = text.find('BEN_mia = {')
chunk = text[idx_mia:idx_mia+800]
print(chunk)

