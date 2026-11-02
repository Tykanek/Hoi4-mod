with open('events/ben_covert_events.txt', 'r', encoding='utf-8') as f:
    text = f.read()

new_events = """

# ------------------------------------------------------------
# Fallback Narrative Events (When PRA Absent / Depleted)
# ------------------------------------------------------------

country_event = {
	id = ben_covert.25
	title = ben_covert.25.t
	desc = ben_covert.25.d
	picture = GFX_report_event_generic_conference
	is_triggered_only = yes

	option = {
		name = ben_covert.25.a
	}
}

country_event = {
	id = ben_covert.26
	title = ben_covert.26.t
	desc = ben_covert.26.d
	picture = GFX_report_event_generic_read_write
	is_triggered_only = yes

	option = {
		name = ben_covert.26.a
	}
}

country_event = {
	id = ben_covert.27
	title = ben_covert.27.t
	desc = ben_covert.27.d
	picture = GFX_report_event_generic_read_write
	is_triggered_only = yes

	option = {
		name = ben_covert.27.a
	}
}

# ------------------------------------------------------------
# Isolated Debug Event for Console Testing (event ben_covert.99)
# ------------------------------------------------------------

country_event = {
	id = ben_covert.99
	title = "Covert Operations Verification Console"
	desc = "Isolated testing harness for Beneshov-Prague resource transfers and countermeasure flags. Used to verify mathematical 1:1 conservation."
	picture = GFX_report_event_generic_conference
	is_triggered_only = yes

	# Test 1: Equipment transfer
	option = {
		name = "Test: Steal 200 Rifles from PRA"
		if = {
			limit = {
				country_exists = PRA
				PRA = { has_equipment = { infantry_equipment > 199 } }
			}
			PRA = {
				add_equipment_to_stockpile = {
					type = infantry_equipment
					amount = -200
				}
			}
			add_equipment_to_stockpile = {
				type = infantry_equipment
				amount = 200
				producer = PRA
			}
		}
	}

	# Test 2: Political Power transfer
	option = {
		name = "Test: Divert 50 PP from PRA"
		if = {
			limit = {
				country_exists = PRA
				PRA = { has_political_power > 49 }
			}
			PRA = { add_political_power = -50 }
			add_political_power = 50
		}
	}

	# Test 3: Manpower transfer
	option = {
		name = "Test: Relocate 800 Manpower from PRA"
		if = {
			limit = {
				country_exists = PRA
				PRA = { has_manpower > 799 }
			}
			PRA = { add_manpower = -800 }
			add_manpower = 800
		}
	}

	# Test 4: Toggle Arsenal Fortification on PRA
	option = {
		name = "Test: Toggle PRA Arsenals Fortified Flag"
		if = {
			limit = { country_exists = PRA }
			PRA = {
				if = {
					limit = { has_country_flag = pra_arsenals_fortified }
					clr_country_flag = pra_arsenals_fortified
				}
				else = {
					set_country_flag = pra_arsenals_fortified
				}
			}
		}
	}

	# Test 5: Toggle Infiltrators Purged Flag on PRA
	option = {
		name = "Test: Toggle PRA Infiltrators Purged Flag"
		if = {
			limit = { country_exists = PRA }
			PRA = {
				if = {
					limit = { has_country_flag = pra_infiltrators_purged }
					clr_country_flag = pra_infiltrators_purged
				}
				else = {
					set_country_flag = pra_infiltrators_purged
				}
			}
		}
	}
}
"""

with open('events/ben_covert_events.txt', 'w', encoding='utf-8') as f:
    f.write(text + new_events)

print('Updated events/ben_covert_events.txt with fallback events and debug event ben_covert.99!')

