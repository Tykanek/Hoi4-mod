import os

vanilla = r'C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV'
for root, dirs, files in os.walk(os.path.join(vanilla, 'common')):
    if 'modifier' in root.lower() or any('modifier' in f.lower() for f in files):
        print(root, files)

