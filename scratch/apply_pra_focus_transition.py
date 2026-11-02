with open('common/national_focus/prague.txt', 'r', encoding='utf-8') as f:
    text = f.read()

assert 'pra_unrestricted_volunteers' not in text, "pra_unrestricted_volunteers already in file"

target = '''        completion_reward = {
            create_wargoal = {
                type = annex_everything
                target = BEN
            }
            country_event = { id = pra_mohammedis.4 }
        }'''

replacement = '''        completion_reward = {
            create_wargoal = {
                type = annex_everything
                target = BEN
            }
            country_event = { id = pra_mohammedis.4 }
            if = {
                limit = { has_idea = pra_military_restraint }
                swap_ideas = {
                    remove_idea = pra_military_restraint
                    add_idea = pra_unrestricted_volunteers
                }
            }
            else_if = {
                limit = { NOT = { has_idea = pra_unrestricted_volunteers } }
                add_ideas = pra_unrestricted_volunteers
            }
            clear_rule = {
                can_not_declare_war = yes
            }
        }'''

target_norm = target.replace('\r\n', '\n')
text_norm = text.replace('\r\n', '\n')
assert target_norm in text_norm, "Target not found in prague.txt"

updated = text_norm.replace(target_norm, replacement)
with open('common/national_focus/prague.txt', 'w', encoding='utf-8') as f:
    f.write(updated)

print("Updated common/national_focus/prague.txt successfully!")

