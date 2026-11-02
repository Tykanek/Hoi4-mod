with open('common/ideas/benesov.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Fix double prefix on ben_socialist_successor_federation
target1 = '''\t\tben_socialist_successor_federation = {
\t\t\tpicture = GFX_idea_ben_pospisil_doctrine'''

repl1 = '''\t\tben_socialist_successor_federation = {
\t\t\tpicture = ben_pospisil_doctrine'''

assert target1.replace('\r\n', '\n') in text.replace('\r\n', '\n'), "target1 not found"
text_norm = text.replace('\r\n', '\n')
text_norm = text_norm.replace(target1.replace('\r\n', '\n'), repl1)

# 2. Fix pra_bureaucratic_migration_scandal and pra_disinformation_turmoil
target2 = '''\t\tpra_bureaucratic_migration_scandal = {
\t\t\tpicture = generic_disruption
\t\t\tallowed = { always = no }
\t\t\tremoval_cost = -1
\t\t\tmodifier = {
\t\t\t\tstability_factor = -0.10
\t\t\t\tpolitical_power_gain = -0.15
\t\t\t}
\t\t}

\t\tpra_disinformation_turmoil = {
\t\t\tpicture = generic_disruption
\t\t\tallowed = { always = no }
\t\t\tremoval_cost = -1
\t\t\tmodifier = {
\t\t\t\tstability_factor = -0.05
\t\t\t\tpolitical_power_gain = -0.10
\t\t\t}
\t\t}

\t\tpra_arsenal_fortified = {
\t\t\tpicture = generic_infantry_bonus
\t\t\tallowed = { always = no }
\t\t\tremoval_cost = -1
\t\t\tmodifier = {
\t\t\t\tforeign_subversive_activites = -0.20
\t\t\t\tstability_factor = 0.03
\t\t\t}
\t\t}

\t\tpra_infiltrators_purged = {
\t\t\tpicture = generic_spy_intel'''

repl2 = '''\t\tpra_bureaucratic_migration_scandal = {
\t\t\tpicture = generic_immigration
\t\t\tallowed = { always = no }
\t\t\tremoval_cost = -1
\t\t\tmodifier = {
\t\t\t\tstability_factor = -0.10
\t\t\t\tpolitical_power_gain = -0.15
\t\t\t}
\t\t}

\t\tpra_disinformation_turmoil = {
\t\t\tpicture = generic_spy_coup
\t\t\tallowed = { always = no }
\t\t\tremoval_cost = -1
\t\t\tmodifier = {
\t\t\t\tstability_factor = -0.05
\t\t\t\tpolitical_power_gain = -0.10
\t\t\t}
\t\t}

\t\tpra_arsenal_fortified = {
\t\t\tpicture = generic_supply_depot
\t\t\tallowed = { always = no }
\t\t\tremoval_cost = -1
\t\t\tmodifier = {
\t\t\t\tforeign_subversive_activites = -0.20
\t\t\t\tstability_factor = 0.03
\t\t\t}
\t\t}

\t\tpra_infiltrators_purged = {
\t\t\tpicture = generic_secret_police'''

assert target2.replace('\r\n', '\n') in text_norm, "target2 not found"
text_norm = text_norm.replace(target2.replace('\r\n', '\n'), repl2)

with open('common/ideas/benesov.txt', 'w', encoding='utf-8') as f:
    f.write(text_norm)

print("common/ideas/benesov.txt updated with valid spirit pictures!")

