import os
import re

loc_dir = r'localisation\english'
ben_files = [
    'benesov_focus_l_english.yml',
    'events_benesov_l_english.yml',
    'national_spirit_benesov_l_english.yml',
    'mod_characters_l_english.yml'
]

suspicious = []

for fname in os.listdir(loc_dir):
    if fname.endswith('.yml'):
        p = os.path.join(loc_dir, fname)
        with open(p, 'r', encoding='utf-8', errors='ignore') as fp:
            for lno, line in enumerate(fp, 1):
                m = re.match(r'^\s*([A-Za-z0-9_.\-]+):(?:\d+)?\s*\"(.*)\"\s*$', line)
                if m:
                    k = m.group(1)
                    val = m.group(2)
                    is_ben = (fname in ben_files or 'ben' in k.lower() or 'pospisil' in k.lower() or 'dvorak' in k.lower() or k.startswith('BEN'))
                    if is_ben:
                        v_strip = val.strip()
                        v_lower = v_strip.lower()
                        # check placeholders
                        if v_strip == "" or v_strip == "..." or "todo" in v_lower or "placeholder" in v_lower or "tbd" in v_lower:
                            suspicious.append((fname, lno, k, val, "Placeholder/empty"))
                        # check if raw ID is value
                        elif v_strip == k and not k.startswith("BEN_"): # BEN_mia: "Mia" etc
                            suspicious.append((fname, lno, k, val, "Raw key as value"))

print(f"Suspicious / placeholder BEN entries: {len(suspicious)}")
for s in suspicious:
    print(s)

