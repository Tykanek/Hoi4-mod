with open('common/national_focus/benesov.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace ben_the_missing_rifles completion_reward
old_rifles = """\tfocus = {
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
\t}"""

new_rifles = """\tfocus = {
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
\t\t\t\t\t\t\tinfantry_equipment > 249
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
\t\t\t\t\t\t\tinfantry_equipment > 99
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
\t\t\telse_if = {
\t\t\t\tlimit = {
\t\t\t\t\tcountry_exists = PRA
\t\t\t\t\tPRA = {
\t\t\t\t\t\thas_equipment = {
\t\t\t\t\t\t\tinfantry_equipment > 49
\t\t\t\t\t\t}
\t\t\t\t\t}
\t\t\t\t}
\t\t\t\tPRA = {
\t\t\t\t\tadd_equipment_to_stockpile = {
\t\t\t\t\t\ttype = infantry_equipment
\t\t\t\t\t\tamount = -50
\t\t\t\t\t}
\t\t\t\t\tcountry_event = { id = ben_covert.2 hours = 6 }
\t\t\t\t}
\t\t\t\tadd_equipment_to_stockpile = {
\t\t\t\t\ttype = infantry_equipment
\t\t\t\t\tamount = 50
\t\t\t\t\tproducer = PRA
\t\t\t\t}
\t\t\t\tcountry_event = { id = ben_covert.1 hours = 6 }
\t\t\t}
\t\t\telse = {
\t\t\t\t# PRA has < 50 rifles or PRA does not exist: Zero rifles fabricated!
\t\t\t\tarmy_experience = 10
\t\t\t\tadd_command_power = 15
\t\t\t\tcountry_event = { id = ben_covert.25 hours = 6 }
\t\t\t}
\t\t}
\t}"""

# Replace ben_follow_the_money
old_money = """\tfocus = {
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
\t}"""

new_money = """\tfocus = {
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
\t\t\t\tlimit = {
\t\t\t\t\tcountry_exists = PRA
\t\t\t\t\tPRA = {
\t\t\t\t\t\thas_political_power > 49
\t\t\t\t\t}
\t\t\t\t}
\t\t\t\tPRA = {
\t\t\t\t\tadd_political_power = -50
\t\t\t\t\tcountry_event = { id = ben_covert.4 hours = 6 }
\t\t\t\t}
\t\t\t\tadd_political_power = 50
\t\t\t\tcountry_event = { id = ben_covert.3 hours = 6 }
\t\t\t}
\t\t\telse_if = {
\t\t\t\tlimit = {
\t\t\t\t\tcountry_exists = PRA
\t\t\t\t\tPRA = {
\t\t\t\t\t\thas_political_power > 19
\t\t\t\t\t}
\t\t\t\t}
\t\t\t\tPRA = {
\t\t\t\t\tadd_political_power = -20
\t\t\t\t\tcountry_event = { id = ben_covert.4 hours = 6 }
\t\t\t\t}
\t\t\t\tadd_political_power = 20
\t\t\t\tcountry_event = { id = ben_covert.3 hours = 6 }
\t\t\t}
\t\t\telse = {
\t\t\t\t# PRA has < 20 PP or PRA does not exist: Zero PP fabricated!
\t\t\t\tadd_timed_idea = {
\t\t\t\t\tidea = ben_archived_trade_ledgers
\t\t\t\t\tdays = 180
\t\t\t\t}
\t\t\t\tcountry_event = { id = ben_covert.26 hours = 6 }
\t\t\t}
\t\t}
\t}"""

# Replace ben_a_better_life_in_benesov
old_life = """\tfocus = {
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
\t}"""

new_life = """\tfocus = {
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
\t\t\t\tlimit = {
\t\t\t\t\tcountry_exists = PRA
\t\t\t\t\tPRA = {
\t\t\t\t\t\thas_manpower > 799
\t\t\t\t\t}
\t\t\t\t}
\t\t\t\tPRA = {
\t\t\t\t\tadd_manpower = -800
\t\t\t\t}
\t\t\t\tadd_manpower = 800
\t\t\t\tcountry_event = { id = ben_covert.5 hours = 6 }
\t\t\t}
\t\t\telse_if = {
\t\t\t\tlimit = {
\t\t\t\t\tcountry_exists = PRA
\t\t\t\t\tPRA = {
\t\t\t\t\t\thas_manpower > 299
\t\t\t\t\t}
\t\t\t\t}
\t\t\t\tPRA = {
\t\t\t\t\tadd_manpower = -300
\t\t\t\t}
\t\t\t\tadd_manpower = 300
\t\t\t\tcountry_event = { id = ben_covert.5 hours = 6 }
\t\t\t}
\t\t\telse = {
\t\t\t\t# PRA has < 300 manpower or PRA does not exist: Zero manpower fabricated!
\t\t\t\tadd_stability = 0.10
\t\t\t\tcountry_event = { id = ben_covert.27 hours = 6 }
\t\t\t}
\t\t}
\t}"""

assert old_rifles in text, "old_rifles not found"
text = text.replace(old_rifles, new_rifles)

assert old_money in text, "old_money not found"
text = text.replace(old_money, new_money)

assert old_life in text, "old_life not found"
text = text.replace(old_life, new_life)

with open('common/national_focus/benesov.txt', 'w', encoding='utf-8') as f:
    f.write(text)

print('Updated focuses in common/national_focus/benesov.txt successfully!')

