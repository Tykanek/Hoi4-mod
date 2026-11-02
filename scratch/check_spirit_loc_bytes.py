with open('localisation/english/national_spirit_benesov_l_english.yml', 'rb') as f:
    raw_ben = f.read()
print('BEN spirit loc length:', len(raw_ben), 'starts with BOM:', raw_ben.startswith(b'\xef\xbb\xbf'))
print('Number of BOMs:', len(raw_ben) - len(raw_ben.lstrip(b'\xef\xbb\xbf')))

with open('localisation/english/national_spirit_prague_l_english.yml', 'rb') as f:
    raw_pra = f.read()
print('PRA spirit loc length:', len(raw_pra), 'starts with BOM:', raw_pra.startswith(b'\xef\xbb\xbf'))
print('Number of BOMs:', len(raw_pra) - len(raw_pra.lstrip(b'\xef\xbb\xbf')))

