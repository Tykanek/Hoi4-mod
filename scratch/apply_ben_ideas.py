with open('common/ideas/benesov.txt', 'r', encoding='utf-8') as f:
    text = f.read()

assert 'ben_military_restraint' not in text, "ben_military_restraint already in file"

target = '''\t\tpra_infiltrators_purged = {
\t\t\tpicture = generic_spy_intel
\t\t\tallowed = { always = no }
\t\t\tremoval_cost = -1
\t\t\tmodifier = {
\t\t\t\tforeign_subversive_activites = -0.20
\t\t\t\tstability_factor = 0.05
\t\t\t}
\t\t}
}
}'''

replacement = '''\t\tpra_infiltrators_purged = {
\t\t\tpicture = generic_spy_intel
\t\t\tallowed = { always = no }
\t\t\tremoval_cost = -1
\t\t\tmodifier = {
\t\t\t\tforeign_subversive_activites = -0.20
\t\t\t\tstability_factor = 0.05
\t\t\t}
\t\t}

\t\t# ============================================================
\t\t# Starting Military Restraint & Volunteer Expeditions
\t\t# ============================================================

\t\tben_military_restraint = {
\t\t\tpicture = generic_neutrality_drift_bonus
\t\t\tallowed = { always = yes }
\t\t\tallowed_civil_war = { always = yes }
\t\t\tremoval_cost = -1

\t\t\trule = {
\t\t\t\tcan_not_declare_war = yes
\t\t\t\tcan_send_volunteers = yes
\t\t\t}

\t\t\tmodifier = {
\t\t\t\tsend_volunteer_divisions_required = -1.0
\t\t\t\tsend_volunteers_tension = -1.0
\t\t\t\tsend_volunteer_size = 100
\t\t\t\tsend_volunteer_factor = 5.0
\t\t\t}
\t\t}

\t\tben_unrestricted_volunteers = {
\t\t\tpicture = generic_volunteer_expedition_bonus
\t\t\tallowed = { always = yes }
\t\t\tallowed_civil_war = { always = yes }
\t\t\tremoval_cost = -1

\t\t\trule = {
\t\t\t\tcan_send_volunteers = yes
\t\t\t}

\t\t\tmodifier = {
\t\t\t\tsend_volunteer_divisions_required = -1.0
\t\t\t\tsend_volunteers_tension = -1.0
\t\t\t\tsend_volunteer_size = 100
\t\t\t\tsend_volunteer_factor = 5.0
\t\t\t}
\t\t}
\t}
}'''

# Normalize newlines
target_norm = target.replace('\r\n', '\n')
text_norm = text.replace('\r\n', '\n')
assert target_norm in text_norm, "Target pattern not found in benesov.txt"

updated = text_norm.replace(target_norm, replacement)
with open('common/ideas/benesov.txt', 'w', encoding='utf-8') as f:
    f.write(updated)

print("Updated common/ideas/benesov.txt successfully!")

