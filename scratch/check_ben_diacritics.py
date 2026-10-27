import os
import re

loc_dir = r'localisation\english'

ben_files = [
    'benesov_focus_l_english.yml',
    'events_benesov_l_english.yml',
    'national_spirit_benesov_l_english.yml',
    'mod_characters_l_english.yml'
]

diacritics_pattern = re.compile(r'[^\x00-\x7F]')

for fname in os.listdir(loc_dir):
    if not fname.endswith('.yml'):
        continue
    p = os.path.join(loc_dir, fname)
    with open(p, 'r', encoding='utf-8', errors='ignore') as fp:
        for lno, line in enumerate(fp, 1):
            # If line defines a BEN key or is in a BEN file
            is_ben_key = False
            m = re.match(r'^\s*([A-Za-z0-9_.\-]+):(?:\d+)?\s*\"(.*)\"\s*$', line)
            if m:
                k = m.group(1)
                val = m.group(2)
                if fname in ben_files or 'ben' in k.lower() or 'pospisil' in k.lower() or 'dvorak' in k.lower() or k.startswith('BEN'):
                    is_ben_key = True
            elif fname in ben_files:
                is_ben_key = True
                val = line

            if is_ben_key:
                # check for non-ascii
                matches = diacritics_pattern.findall(line)
                if matches:
                    print(f"File {fname}:{lno} has non-ASCII characters {matches}:")
                    print(f"  Line: {line.strip().encode('ascii', 'backslashreplace').decode('ascii')}")

