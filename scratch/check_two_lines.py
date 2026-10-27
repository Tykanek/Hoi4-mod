import os

loc_dir = r'localisation\english'
ben_files = ['benesov_focus_l_english.yml', 'events_benesov_l_english.yml', 'national_spirit_benesov_l_english.yml', 'mod_characters_l_english.yml']
for fname in os.listdir(loc_dir):
    if not fname.endswith('.yml'):
        continue
    p = os.path.join(loc_dir, fname)
    with open(p, 'rb') as fp:
        raw = fp.read()
    if raw.startswith(b'\xef\xbb\xbf'):
        text = raw[3:].decode('utf-8', errors='replace')
    else:
        text = raw.decode('utf-8', errors='replace')
    for lno, line in enumerate(text.splitlines(), 1):
        is_ben = fname in ben_files or 'ben' in line.lower() or 'pospisil' in line.lower() or 'dvorak' in line.lower()
        if is_ben:
            non_ascii = [c for c in line if ord(c) > 127]
            if non_ascii:
                print(f"{fname}:{lno} -> {non_ascii} -> {line.strip().encode('ascii', 'backslashreplace').decode('ascii')}")

