import os
import re

loc_dir = r'localisation\english'
non_ascii_findings = []

for fname in os.listdir(loc_dir):
    if fname.endswith('.yml'):
        p = os.path.join(loc_dir, fname)
        with open(p, 'rb') as fp:
            raw = fp.read()

        # Strip UTF-8 BOM if present
        if raw.startswith(b'\xef\xbb\xbf'):
            content_bytes = raw[3:]
        else:
            content_bytes = raw

        try:
            text = content_bytes.decode('utf-8')
        except UnicodeDecodeError as e:
            print(f"ERROR: {fname} cannot decode as UTF-8: {e}")
            continue

        for lno, line in enumerate(text.splitlines(), 1):
            # Check if this line is in a BEN file or mentions BEN
            is_ben_context = ('benesov' in fname.lower() or
                              'mod_characters' in fname.lower() or
                              'countries' in fname.lower() or
                              'ben' in line.lower() or
                              'pospisil' in line.lower() or
                              'dvorak' in line.lower())

            # Find any non-ASCII characters
            non_ascii_chars = [c for c in line if ord(c) > 127]
            if non_ascii_chars and is_ben_context:
                non_ascii_findings.append((fname, lno, non_ascii_chars, line.strip()))

print(f"Total non-ASCII lines in BEN context: {len(non_ascii_findings)}")
for fname, lno, chars, line in non_ascii_findings:
    # Safely print without console charmap crash
    char_codes = [f"{c} (U+{ord(c):04X})" for c in chars]
    print(f"{fname}:{lno} -> Chars: {', '.join(char_codes)}")
    safe_line = line.encode('ascii', 'backslashreplace').decode('ascii')
    print(f"   {safe_line}")

