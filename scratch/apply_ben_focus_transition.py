with open('common/national_focus/benesov.txt', 'r', encoding='utf-8') as f:
    text = f.read()

assert 'ben_unrestricted_volunteers' not in text, "ben_unrestricted_volunteers already in file"

target = '''\t\t\t\tcreate_wargoal = {
\t\t\t\t\ttype = take_core_state
\t\t\t\t\ttarget = HUN
\t\t\t\t\tgenerator = { 664 }
\t\t\t\t}
\t\t\t}
\t\t}
\t}'''

replacement = '''\t\t\t\tcreate_wargoal = {
\t\t\t\t\ttype = take_core_state
\t\t\t\t\ttarget = HUN
\t\t\t\t\tgenerator = { 664 }
\t\t\t\t}
\t\t\t}
\t\t\tif = {
\t\t\t\tlimit = { has_idea = ben_military_restraint }
\t\t\t\tswap_ideas = {
\t\t\t\t\tremove_idea = ben_military_restraint
\t\t\t\t\tadd_idea = ben_unrestricted_volunteers
\t\t\t\t}
\t\t\t}
\t\t\telse_if = {
\t\t\t\tlimit = { NOT = { has_idea = ben_unrestricted_volunteers } }
\t\t\t\tadd_ideas = ben_unrestricted_volunteers
\t\t\t}
\t\t\tclear_rule = {
\t\t\t\tcan_not_declare_war = yes
\t\t\t}
\t\t}
\t}'''

target_norm = target.replace('\r\n', '\n')
text_norm = text.replace('\r\n', '\n')
assert target_norm in text_norm, "Target not found in benesov.txt"

updated = text_norm.replace(target_norm, replacement)
with open('common/national_focus/benesov.txt', 'w', encoding='utf-8') as f:
    f.write(updated)

print("Updated common/national_focus/benesov.txt successfully!")

