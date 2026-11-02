with open('common/ideas/prague.txt', 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.splitlines()
print(f'Total lines in common/ideas/prague.txt: {len(lines)}')
print("First 30 lines:")
for l in lines[:30]:
    print(l)
print("Last 30 lines:")
for l in lines[-30:]:
    print(l)

