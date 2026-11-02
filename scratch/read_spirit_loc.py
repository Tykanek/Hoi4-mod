with open('localisation/english/national_spirit_benesov_l_english.yml', 'r', encoding='utf-8-sig') as f:
    ben_loc = f.read()

with open('localisation/english/national_spirit_prague_l_english.yml', 'r', encoding='utf-8-sig') as f:
    pra_loc = f.read()

print("--- BEN SPIRIT LOC (first 15 lines) ---")
for l in ben_loc.splitlines()[:15]:
    print(repr(l))

print("\n--- PRA SPIRIT LOC (first 15 lines) ---")
for l in pra_loc.splitlines()[:15]:
    print(repr(l))

