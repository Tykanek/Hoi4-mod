with open('history/countries/BEN - Benesov.txt', 'r', encoding='utf-8') as f:
    ben_hist = f.read()

with open('history/countries/PRA - Prague.txt', 'r', encoding='utf-8') as f:
    pra_hist = f.read()

print("--- BEN HISTORY START ---")
print(ben_hist[:600])

print("\n--- PRA HISTORY START ---")
print(pra_hist[:600])

