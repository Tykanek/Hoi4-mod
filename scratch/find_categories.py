import os
for root, dirs, files in os.walk('common'):
    if 'categor' in root.lower() or any('categor' in f.lower() for f in files):
        print(root, files)
