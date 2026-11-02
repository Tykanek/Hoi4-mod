import glob

for f in glob.glob('localisation/english/*_l_english.yml'):
    with open(f, 'rb') as fp:
        raw = fp.read()
    if b'\xc2\xa7' in raw:
        print('Found \xc2\xa7 (section sign in UTF-8) in:', f)

