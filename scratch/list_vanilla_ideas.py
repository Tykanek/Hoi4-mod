import os
vanilla = r'C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV'
print(os.listdir(os.path.join(vanilla, 'common', 'ideas'))[:10])

