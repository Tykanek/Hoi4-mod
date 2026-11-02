import os

vanilla_goals = r'C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\gfx\interface\goals'
for f in os.listdir(vanilla_goals):
    if 'propaganda' in f.lower() or 'people' in f.lower() or 'worker' in f.lower() or 'population' in f.lower():
        print(f)
