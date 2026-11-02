import os, re

vanilla = r'C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV'

# Look for add_equipment_to_stockpile examples with negative amount
files = []
for root, dirs, fnames in os.walk(os.path.join(vanilla, 'events')):
    for f in fnames:
        if f.endswith('.txt'):
            p = os.path.join(root, f)
            with open(p, 'r', encoding='utf-8', errors='ignore') as fp:
                c = fp.read()
                if 'add_equipment_to_stockpile' in c and 'amount = -' in c:
                    for m in re.finditer(r'add_equipment_to_stockpile\s*=\s*\{([^}]+)\}', c):
                        if '-' in m.group(1):
                            print(f'{f}: {m.group(1).strip()}')
                            files.append(f)
                            if len(files) >= 10: break
    if len(files) >= 10: break

