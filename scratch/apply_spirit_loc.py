import os

def update_loc_file(path, new_entries):
    with open(path, 'rb') as f:
        raw = f.read()

    # Strip BOM
    has_bom = raw.startswith(b'\xef\xbb\xbf')
    clean_bytes = raw
    while clean_bytes.startswith(b'\xef\xbb\xbf'):
        clean_bytes = clean_bytes[3:]

    text = clean_bytes.decode('utf-8')
    # Ensure ends with newline
    if not text.endswith('\n'):
        text += '\r\n'

    addition = '\r\n'.join(new_entries) + '\r\n'
    full_text = text + addition

    # Write back with single BOM
    with open(path, 'wb') as f:
        f.write(b'\xef\xbb\xbf' + full_text.encode('utf-8'))

    print(f"Updated {path} successfully!")

ben_entries = [
    ' # ========================================================',
    ' # Starting Military Restraint & Volunteer Expeditions',
    ' # ========================================================',
    ' ben_military_restraint:0 "Beneshov\'s Military Restraint"',
    ' ben_military_restraint_desc:0 "Bound by the fragile political order of the former republic, Beneshov cannot independently pursue offensive wars until it formally challenges Czechoslovakia. In the meantime, the city\'s soldiers are free to gain experience abroad through unrestricted volunteer expeditions."',
    ' ben_unrestricted_volunteers:0 "Beneshov Volunteer Expeditions"',
    ' ben_unrestricted_volunteers_desc:0 "Having formally asserted its sovereign authority against Czechoslovakia, Beneshov is no longer bound by military restraint. Its expeditionary forces remain free to participate in foreign wars through unrestricted volunteer expeditions."'
]

pra_entries = [
    ' # ========================================================',
    ' # Starting Military Restraint & Volunteer Expeditions',
    ' # ========================================================',
    ' pra_military_restraint:0 "Prague\'s Military Restraint"',
    ' pra_military_restraint_desc:0 "Prague\'s leadership is not yet prepared to launch an independent war against its rival. Until the confrontation with Beneshov is formally authorized, Prague must exert its military influence through unrestricted volunteer expeditions."',
    ' pra_unrestricted_volunteers:0 "Prague Volunteer Expeditions"',
    ' pra_unrestricted_volunteers_desc:0 "With the confrontation against Beneshov formally authorized, Prague\'s former military restraint has been cast aside. The capital\'s armed divisions remain free to deploy abroad on unrestricted volunteer expeditions."'
]

update_loc_file('localisation/english/national_spirit_benesov_l_english.yml', ben_entries)
update_loc_file('localisation/english/national_spirit_prague_l_english.yml', pra_entries)

