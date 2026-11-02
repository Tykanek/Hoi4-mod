with open('localisation/english/national_spirit_benesov_l_english.yml', 'r', encoding='utf-8-sig') as f:
    lines = f.readlines()
print("BEN loc last 10 lines:")
for l in lines[-10:]:
    print(repr(l))

with open('localisation/english/national_spirit_prague_l_english.yml', 'r', encoding='utf-8-sig') as f:
    lines = f.readlines()
print("PRA loc last 10 lines:")
for l in lines[-10:]:
    print(repr(l))

