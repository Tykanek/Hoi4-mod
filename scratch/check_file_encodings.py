import os

loc_dir = r'localisation\english'
for fname in sorted(os.listdir(loc_dir)):
    if fname.endswith('.yml'):
        p = os.path.join(loc_dir, fname)
        with open(p, 'rb') as fp:
            data = fp.read()
        has_bom = data.startswith(b'\xef\xbb\xbf')
        has_crlf = b'\r\n' in data
        ends_with_crlf = data.endswith(b'\r\n')
        # strip BOM
        text = data[3:].decode('utf-8', errors='replace') if has_bom else data.decode('utf-8', errors='replace')
        lines = text.splitlines()
        first_line = lines[0].strip() if lines else ""
        if not has_bom or not has_crlf or not ends_with_crlf or not first_line.startswith('l_english:'):
            print(f"File {fname}: BOM={has_bom}, CRLF={has_crlf}, EndsCRLF={ends_with_crlf}, Header='{repr(first_line)}'")

