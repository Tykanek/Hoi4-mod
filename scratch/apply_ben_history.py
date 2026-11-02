with open('history/countries/BEN - Benesov.txt', 'r', encoding='utf-8') as f:
    text = f.read()

target = '''# Starting national debuffs and laws
add_ideas = {
\t# Laws
\tvolunteer_only'''

replacement = '''# Starting national debuffs and laws
add_ideas = {
\t# Starting Military Restraint & Volunteers
\tben_military_restraint

\t# Laws
\tvolunteer_only'''

assert target in text, "Target not found in BEN history"
text = text.replace(target, replacement, 1)

with open('history/countries/BEN - Benesov.txt', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated history/countries/BEN - Benesov.txt successfully!")

