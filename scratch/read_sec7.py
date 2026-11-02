with open('scratch/master_validation.py', 'r', encoding='utf-8') as f:
    text = f.read()

import re
m = re.search(r'# --- 7\. Check GFX / Icons ---.*?(?=# --- 8)', text, re.DOTALL)
if m:
    print(m.group(0))

