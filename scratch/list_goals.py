import os

files = os.listdir('gfx/interface/goals')
print(f'Total goals DDS: {len(files)}')
ben_goals = [f for f in files if 'ben' in f.lower() or 'pra' in f.lower() or 'intelligence' in f.lower() or 'spy' in f.lower() or 'rifle' in f.lower()]
print('Relevant files:')
for f in ben_goals:
    print(f)
