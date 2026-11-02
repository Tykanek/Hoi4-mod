with open('common/decisions/ben_covert_operations.txt', 'r', encoding='utf-8') as f:
    text = f.read()

import re
m1 = re.search(r'pra_audit_central_arsenal\s*=\s*\{.*?\n\t\}', text, re.DOTALL)
if m1:
    print('--- pra_audit_central_arsenal ---')
    print(m1.group(0))

m2 = re.search(r'pra_purge_infiltrators\s*=\s*\{.*?\n\t\}', text, re.DOTALL)
if m2:
    print('--- pra_purge_infiltrators ---')
    print(m2.group(0))

