with open('scratch/master_validation.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print('Total lines in master_validation.py:', len(lines))
for l in lines[-40:]:
    print(l, end='')

