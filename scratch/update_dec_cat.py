with open('common/decisions/categories/ben_decisions_categories.txt', 'r', encoding='utf-8') as f:
    text = f.read()

if 'ben_covert_operations_against_prague' in text:
    print('Already added!')
else:
    new_cats = """
ben_covert_operations_against_prague = {
	icon = generic_intelligence

	allowed = {
		original_tag = BEN
	}

	visible_when_empty = no

	visible = {
		original_tag = BEN
		has_completed_focus = ben_eyes_on_prague
		country_exists = PRA
	}

	priority = {
		base = 165
	}
}

pra_counter_espionage_measures = {
	icon = generic_intelligence

	allowed = {
		original_tag = PRA
	}

	visible_when_empty = no

	visible = {
		original_tag = PRA
		country_exists = BEN
		BEN = { has_completed_focus = ben_eyes_on_prague }
	}

	priority = {
		base = 150
	}
}
"""
    with open('common/decisions/categories/ben_decisions_categories.txt', 'w', encoding='utf-8') as f:
        f.write(text + new_cats)
    print('Updated categories successfully!')
