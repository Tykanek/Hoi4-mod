with open('history/countries/BEN - Benesov.txt', 'r', encoding='utf-8') as f:
    ben_lines = f.readlines()

print("--- BEN HISTORY IDEAS ---")
for i, l in enumerate(ben_lines):
    if 'add_ideas' in l:
        for j in range(i, min(len(ben_lines), i+30)):
            print(ben_lines[j], end='')
        break

with open('history/countries/PRA - Prague.txt', 'r', encoding='utf-8') as f:
    pra_lines = f.readlines()

print("\n--- PRA HISTORY IDEAS ---")
for i, l in enumerate(pra_lines):
    if 'add_ideas' in l:
        for j in range(i, min(len(pra_lines), i+30)):
            print(pra_lines[j], end='')
        break

