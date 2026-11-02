import os, shutil

vanilla_goals = r'C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\gfx\interface\goals'
shutil.copyfile(
    os.path.join(vanilla_goals, 'focus_generic_population_growth.dds'),
    'gfx/interface/goals/focus_BEN_a_better_life_in_benesov.dds'
)
print('Copied focus_generic_population_growth.dds -> focus_BEN_a_better_life_in_benesov.dds')
