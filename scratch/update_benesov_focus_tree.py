with open('common/national_focus/benesov.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update ben_pospisil_takes_command requirement to > 0.50 and add flag
old_target = """\tfocus = {
\t\tid = ben_pospisil_takes_command
\t\ticon = GFX_focus_BEN_pospisil_takes_command
\t\tprerequisite = { focus = ben_dvorak_has_lost_the_streets }
\t\tavailable = {
\t\t\tcommunism > 0.40
\t\t}
\t\tx = 22
\t\ty = 14
\t\tcost = 4.286
\t\tsearch_filters = { FOCUS_FILTER_POLITICAL }
\t\tai_will_do = { factor = 10 }

\t\tcompletion_reward = {
\t\t\tset_politics = {
\t\t\t\truling_party = communism
\t\t\t\telections_allowed = no
\t\t\t}
\t\t\tcountry_event = { id = benesov.6 hours = 6 }
\t\t}
\t}"""

new_target = """\tfocus = {
\t\tid = ben_pospisil_takes_command
\t\ticon = GFX_focus_BEN_pospisil_takes_command
\t\tprerequisite = { focus = ben_dvorak_has_lost_the_streets }
\t\tavailable = {
\t\t\tcommunism > 0.50
\t\t}
\t\tx = 22
\t\ty = 14
\t\tcost = 4.286
\t\tsearch_filters = { FOCUS_FILTER_POLITICAL }
\t\tai_will_do = { factor = 10 }

\t\tcompletion_reward = {
\t\t\tset_politics = {
\t\t\t\truling_party = communism
\t\t\t\telections_allowed = no
\t\t\t}
\t\t\tset_country_flag = ben_pospisil_in_power
\t\t\tcountry_event = { id = benesov.6 hours = 6 }
\t\t}
\t}"""

if old_target in text:
    text = text.replace(old_target, new_target)
    print('Updated ben_pospisil_takes_command successfully!')
else:
    print('ERROR: old_target not matched exactly, checking substring...')
    idx = text.find('id = ben_pospisil_takes_command')
    print(text[idx-20:idx+450])
    raise SystemExit('Mismatch in ben_pospisil_takes_command')

new_covert_focuses = """

\t# ============================================================
\t# COVERT RIVALRY AGAINST PRAGUE (8 FOCUSES)
\t# ============================================================

\tfocus = {
\t\tid = ben_eyes_on_prague
\t\ticon = GFX_focus_BEN_eyes_on_prague
\t\tprerequisite = { focus = ben_the_deliveries_have_stopped }
\t\tx = 30
\t\ty = 7
\t\tcost = 4.286
\t\tsearch_filters = { FOCUS_FILTER_POLITICAL }
\t\tai_will_do = { factor = 10 }

\t\tcompletion_reward = {
\t\t\tadd_political_power = 25
\t\t\tadd_ideas = ben_eyes_on_prague_spirit
\t\t\tcustom_effect_tooltip = ben_eyes_on_prague_tt
\t\t}
\t}

\tfocus = {
\t\tid = ben_the_missing_rifles
\t\ticon = GFX_focus_BEN_the_missing_rifles
\t\tprerequisite = { focus = ben_eyes_on_prague }
\t\tx = 29
\t\ty = 8
\t\tcost = 4.286
\t\tsearch_filters = { FOCUS_FILTER_INDUSTRY }
\t\tai_will_do = { factor = 10 }

\t\tcompletion_reward = {
\t\t\tif = {
\t\t\t\tlimit = {
\t\t\t\t\tcountry_exists = PRA
\t\t\t\t\tPRA = {
\t\t\t\t\t\thas_equipment = {
\t\t\t\t\t\t\tinfantry_equipment > 250
\t\t\t\t\t\t}
\t\t\t\t\t}
\t\t\t\t}
\t\t\t\tPRA = {
\t\t\t\t\tadd_equipment_to_stockpile = {
\t\t\t\t\t\ttype = infantry_equipment
\t\t\t\t\t\tamount = -250
\t\t\t\t\t}
\t\t\t\t\tcountry_event = { id = ben_covert.2 hours = 6 }
\t\t\t\t}
\t\t\t\tadd_equipment_to_stockpile = {
\t\t\t\t\ttype = infantry_equipment
\t\t\t\t\tamount = 250
\t\t\t\t\tproducer = PRA
\t\t\t\t}
\t\t\t\tcountry_event = { id = ben_covert.1 hours = 6 }
\t\t\t}
\t\t\telse_if = {
\t\t\t\tlimit = {
\t\t\t\t\tcountry_exists = PRA
\t\t\t\t\tPRA = {
\t\t\t\t\t\thas_equipment = {
\t\t\t\t\t\t\tinfantry_equipment > 50
\t\t\t\t\t\t}
\t\t\t\t\t}
\t\t\t\t}
\t\t\t\tPRA = {
\t\t\t\t\tadd_equipment_to_stockpile = {
\t\t\t\t\t\ttype = infantry_equipment
\t\t\t\t\t\tamount = -100
\t\t\t\t\t}
\t\t\t\t\tcountry_event = { id = ben_covert.2 hours = 6 }
\t\t\t\t}
\t\t\t\tadd_equipment_to_stockpile = {
\t\t\t\t\ttype = infantry_equipment
\t\t\t\t\tamount = 100
\t\t\t\t\tproducer = PRA
\t\t\t\t}
\t\t\t\tcountry_event = { id = ben_covert.1 hours = 6 }
\t\t\t}
\t\t\telse = {
\t\t\t\tadd_equipment_to_stockpile = {
\t\t\t\t\ttype = infantry_equipment
\t\t\t\t\tamount = 100
\t\t\t\t}
\t\t\t\tcountry_event = { id = ben_covert.1 hours = 6 }
\t\t\t}
\t\t}
\t}

\tfocus = {
\t\tid = ben_follow_the_money
\t\ticon = GFX_focus_BEN_follow_the_money
\t\tprerequisite = { focus = ben_the_missing_rifles }
\t\tx = 29
\t\ty = 9
\t\tcost = 4.286
\t\tsearch_filters = { FOCUS_FILTER_POLITICAL }
\t\tai_will_do = { factor = 10 }

\t\tcompletion_reward = {
\t\t\tif = {
\t\t\t\tlimit = { country_exists = PRA }
\t\t\t\tPRA = {
\t\t\t\t\tadd_political_power = -50
\t\t\t\t\tcountry_event = { id = ben_covert.4 hours = 6 }
\t\t\t\t}
\t\t\t\tadd_political_power = 50
\t\t\t\tcountry_event = { id = ben_covert.3 hours = 6 }
\t\t\t}
\t\t\telse = {
\t\t\t\tadd_political_power = 30
\t\t\t\tcountry_event = { id = ben_covert.3 hours = 6 }
\t\t\t}
\t\t}
\t}

\tfocus = {
\t\tid = ben_a_better_life_in_benesov
\t\ticon = GFX_focus_BEN_a_better_life_in_benesov
\t\tprerequisite = { focus = ben_eyes_on_prague }
\t\tx = 31
\t\ty = 8
\t\tcost = 4.286
\t\tsearch_filters = { FOCUS_FILTER_MANPOWER }
\t\tai_will_do = { factor = 10 }

\t\tcompletion_reward = {
\t\t\tif = {
\t\t\t\tlimit = { country_exists = PRA }
\t\t\t\tPRA = {
\t\t\t\t\tadd_manpower = -800
\t\t\t\t}
\t\t\t\tadd_manpower = 800
\t\t\t\tcountry_event = { id = ben_covert.5 hours = 6 }
\t\t\t}
\t\t\telse = {
\t\t\t\tadd_manpower = 500
\t\t\t\tcountry_event = { id = ben_covert.5 hours = 6 }
\t\t\t}
\t\t}
\t}

\tfocus = {
\t\tid = ben_the_irregular_migration_scandal
\t\ticon = GFX_focus_BEN_the_irregular_migration_scandal
\t\tprerequisite = { focus = ben_a_better_life_in_benesov }
\t\tx = 31
\t\ty = 9
\t\tcost = 4.286
\t\tsearch_filters = { FOCUS_FILTER_POLITICAL }
\t\tai_will_do = { factor = 10 }

\t\tcompletion_reward = {
\t\t\tif = {
\t\t\t\tlimit = { country_exists = PRA }
\t\t\t\tPRA = {
\t\t\t\t\tadd_timed_idea = {
\t\t\t\t\t\tidea = pra_bureaucratic_migration_scandal
\t\t\t\t\t\tdays = 180
\t\t\t\t\t}
\t\t\t\t\tcountry_event = { id = ben_covert.6 hours = 6 }
\t\t\t\t}
\t\t\t\tcountry_event = { id = ben_covert.7 hours = 6 }
\t\t\t}
\t\t\telse = {
\t\t\t\tadd_stability = 0.05
\t\t\t}
\t\t}
\t}

\tfocus = {
\t\tid = ben_the_invisible_hand_of_benesov
\t\ticon = GFX_focus_BEN_the_invisible_hand_of_benesov
\t\tprerequisite = { focus = ben_follow_the_money }
\t\tprerequisite = { focus = ben_the_irregular_migration_scandal }
\t\tx = 30
\t\ty = 10
\t\tcost = 4.286
\t\tsearch_filters = { FOCUS_FILTER_POLITICAL }
\t\tai_will_do = { factor = 10 }

\t\tcompletion_reward = {
\t\t\tadd_ideas = ben_master_infiltrators
\t\t\tcountry_event = { id = ben_covert.8 hours = 6 }
\t\t}
\t}

\tfocus = {
\t\tid = ben_a_city_that_bleeds_its_rival
\t\ticon = GFX_focus_BEN_a_city_that_bleeds_its_rival
\t\tprerequisite = { focus = ben_the_invisible_hand_of_benesov }
\t\tx = 30
\t\ty = 11
\t\tcost = 4.286
\t\tsearch_filters = { FOCUS_FILTER_POLITICAL }
\t\tai_will_do = { factor = 10 }

\t\tcompletion_reward = {
\t\t\tadd_ideas = ben_bleeding_prague
\t\t\tadd_political_power = 50
\t\t}
\t}

\tfocus = {
\t\tid = ben_the_prague_files
\t\ticon = GFX_focus_BEN_the_prague_files
\t\tprerequisite = { focus = ben_a_city_that_bleeds_its_rival }
\t\tx = 30
\t\ty = 12
\t\tcost = 4.286
\t\tsearch_filters = { FOCUS_FILTER_POLITICAL }
\t\tai_will_do = { factor = 10 }

\t\tcompletion_reward = {
\t\t\tcountry_event = { id = ben_covert.10 hours = 6 }
\t\t}
\t}
"""

last_brace = text.rfind('}')
if last_brace != -1:
    updated = text[:last_brace] + new_covert_focuses + text[last_brace:]
    with open('common/national_focus/benesov.txt', 'w', encoding='utf-8') as f:
        f.write(updated)
    print('Updated common/national_focus/benesov.txt with 8 new covert focuses!')
else:
    raise SystemExit('Closing brace not found!')
