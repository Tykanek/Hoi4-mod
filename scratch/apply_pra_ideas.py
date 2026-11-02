with open('common/ideas/prague.txt', 'r', encoding='utf-8') as f:
    text = f.read()

assert 'pra_military_restraint' not in text, "pra_military_restraint already in file"

target = '''        pra_colonel_state = {
            picture = pra_colonel_state
            modifier = {
                political_power_factor = 0.10
                mobilization_speed = 0.20
                justify_war_goal_time = -0.15
                war_support_factor = 0.15
                stability_factor = 0.12
            }
        }


    }
}'''

replacement = '''        pra_colonel_state = {
            picture = pra_colonel_state
            modifier = {
                political_power_factor = 0.10
                mobilization_speed = 0.20
                justify_war_goal_time = -0.15
                war_support_factor = 0.15
                stability_factor = 0.12
            }
        }

        # ========================================================
        # Starting Military Restraint & Volunteer Expeditions
        # ========================================================

        pra_military_restraint = {
            picture = generic_neutrality_drift_bonus
            allowed = { always = yes }
            allowed_civil_war = { always = yes }
            removal_cost = -1

            rule = {
                can_not_declare_war = yes
                can_send_volunteers = yes
            }

            modifier = {
                send_volunteer_divisions_required = -1.0
                send_volunteers_tension = -1.0
                send_volunteer_size = 100
                send_volunteer_factor = 5.0
            }
        }

        pra_unrestricted_volunteers = {
            picture = generic_volunteer_expedition_bonus
            allowed = { always = yes }
            allowed_civil_war = { always = yes }
            removal_cost = -1

            rule = {
                can_send_volunteers = yes
            }

            modifier = {
                send_volunteer_divisions_required = -1.0
                send_volunteers_tension = -1.0
                send_volunteer_size = 100
                send_volunteer_factor = 5.0
            }
        }

    }
}'''

target_norm = target.replace('\r\n', '\n')
text_norm = text.replace('\r\n', '\n')
assert target_norm in text_norm, "Target pattern not found in prague.txt"

updated = text_norm.replace(target_norm, replacement)
with open('common/ideas/prague.txt', 'w', encoding='utf-8') as f:
    f.write(updated)

print("Updated common/ideas/prague.txt successfully!")

