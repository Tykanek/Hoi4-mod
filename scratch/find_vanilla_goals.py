import os

vanilla_goals = r'C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\gfx\interface\goals'
files = os.listdir(vanilla_goals)
keywords = ['intelligence', 'spy', 'conspiracy', 'sabotage', 'money', 'gold', 'trade', 'treaty', 'secret', 'propaganda', 'rifle', 'infiltrate', 'subversive']
matches = [f for f in files if any(k in f.lower() for k in keywords)]
print(f'Found {len(matches)} matches in vanilla goals:')
for m in matches[:30]:
    print(m)
