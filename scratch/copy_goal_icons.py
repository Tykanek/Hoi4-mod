import os, shutil

vanilla_goals = r'C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV\gfx\interface\goals'
target_dir = 'gfx/interface/goals'

mappings = {
    'focus_BEN_eyes_on_prague.dds': 'focus_generic_secret_service_agency.dds',
    'focus_BEN_the_missing_rifles.dds': 'focus_generic_arms_trade.dds',
    'focus_BEN_follow_the_money.dds': 'focus_GER_the_swiss_gold.dds',
    'focus_BEN_a_better_life_in_benesov.dds': 'focus_generic_propaganda.dds',
    'focus_BEN_the_irregular_migration_scandal.dds': 'focus_generic_conspiracy.dds',
    'focus_BEN_the_invisible_hand_of_benesov.dds': 'focus_generic_secret_agent_operative.dds',
    'focus_BEN_a_city_that_bleeds_its_rival.dds': 'focus_generic_sabotage.dds',
    'focus_BEN_the_prague_files.dds': 'focus_generic_diplomatic_treaty.dds'
}

for dest, src in mappings.items():
    src_path = os.path.join(vanilla_goals, src)
    dest_path = os.path.join(target_dir, dest)
    if os.path.exists(src_path):
        shutil.copyfile(src_path, dest_path)
        print(f'Copied {src} -> {dest}')
    else:
        print(f'WARNING: {src_path} not found!')
