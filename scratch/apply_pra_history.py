with open('history/countries/PRA - Prague.txt', 'r', encoding='utf-8') as f:
    text = f.read()

target = '''recruit_character = PRA_BEN_shared_field_marshal

set_stability = 0.30'''

replacement = '''recruit_character = PRA_BEN_shared_field_marshal

# Starting National Spirits
add_ideas = {
\tpra_military_restraint
}

set_stability = 0.30'''

assert target in text, "Target not found in PRA history"
text = text.replace(target, replacement, 1)

with open('history/countries/PRA - Prague.txt', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated history/countries/PRA - Prague.txt successfully!")

