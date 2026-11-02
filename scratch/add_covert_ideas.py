with open('common/ideas/benesov.txt', 'r', encoding='utf-8') as f:
    text = f.read()

if 'ben_eyes_on_prague_spirit' in text:
    print('Already added!')
else:
    new_ideas = """
		# ============================================================
		# Anti-Prague Covert Rivalry Spirits
		# ============================================================

		ben_eyes_on_prague_spirit = {
			picture = generic_intel_bonus
			allowed = { always = no }
			removal_cost = -1
			modifier = {
				decryption_factor = 0.10
				foreign_subversive_activites = -0.10
				intel_network_gain_factor = 0.15
			}
		}

		ben_master_infiltrators = {
			picture = generic_spy_political
			allowed = { always = no }
			removal_cost = -1
			modifier = {
				decryption_factor = 0.15
				subversive_activites_up = 0.20
				political_power_gain = 0.05
			}
		}

		ben_bleeding_prague = {
			picture = generic_exploit_mines
			allowed = { always = no }
			removal_cost = -1
			modifier = {
				political_power_gain = 0.10
				consumer_goods_factor = -0.03
			}
		}

		ben_prague_defector_engineers = {
			picture = generic_research_bonus
			allowed = { always = no }
			removal_cost = -1
			modifier = {
				research_speed_factor = 0.03
			}
		}

		pra_bureaucratic_migration_scandal = {
			picture = generic_disruption
			allowed = { always = no }
			removal_cost = -1
			modifier = {
				stability_factor = -0.10
				political_power_gain = -0.15
			}
		}

		pra_disinformation_turmoil = {
			picture = generic_disruption
			allowed = { always = no }
			removal_cost = -1
			modifier = {
				stability_factor = -0.05
				political_power_gain = -0.10
			}
		}

		pra_arsenal_fortified = {
			picture = generic_infantry_bonus
			allowed = { always = no }
			removal_cost = -1
			modifier = {
				foreign_subversive_activites = -0.20
				stability_factor = 0.03
			}
		}

		pra_infiltrators_purged = {
			picture = generic_spy_intel
			allowed = { always = no }
			removal_cost = -1
			modifier = {
				foreign_subversive_activites = -0.20
				stability_factor = 0.05
			}
		}
"""
    # Insert right before the last two closing braces
    last_two_braces = text.rfind('}')
    second_last = text.rfind('}', 0, last_two_braces)
    updated = text[:second_last] + new_ideas + text[second_last:]
    with open('common/ideas/benesov.txt', 'w', encoding='utf-8') as f:
        f.write(updated)
    print('Added new covert ideas to common/ideas/benesov.txt successfully!')
