import os
import re
from collections import defaultdict

loc_dir = r'localisation\english'
defined_keys = defaultdict(list)
for fname in os.listdir(loc_dir):
    if fname.endswith('.yml'):
        p = os.path.join(loc_dir, fname)
        with open(p, 'r', encoding='utf-8', errors='ignore') as fp:
            for line in fp:
                m = re.match(r'^\s*([A-Za-z0-9_.\-]+):(?:\d+)?\s*\"(.*)\"\s*$', line)
                if m:
                    defined_keys[m.group(1)].append((fname, m.group(2)))

ideas = [
  'ben_great_beneshov_depression_1',
  'ben_great_beneshov_depression_2',
  'ben_great_beneshov_depression_3',
  'ben_great_beneshov_depression_4',
  'ben_great_beneshov_depression_5',
  'ben_matej_dvorak_getting_everyone_drunk',
  'ben_dependent_on_czech_deliveries',
  'ben_collapsed_local_economy',
  'ben_broken_production_system',
  'ben_army_without_supply_system',
  'ben_untrained_local_militia',
  'ben_no_officer_corps',
  'ben_air_force_in_name_only',
  'ben_no_trained_pilots',
  'ben_no_aviation_industry',
  'ben_improvised_airfields',
  'ben_struggling_local_economy',
  'ben_reduced_czech_dependency',
  'ben_disorganized_production',
  'ben_improvised_supply_system',
  'ben_partially_trained_garrison',
  'ben_inexperienced_officer_corps',
  'ben_embryonic_air_force',
  'ben_basic_pilot_training',
  'ben_small_aviation_workshops',
  'ben_repaired_airfields',
  'ben_recovered_local_economy',
  'ben_reorganized_benesov_army',
  'ben_reorganized_air_command',
  'ben_public_morale_program',
  'ben_pospisil_strategic_theory',
  'ben_state_strategic_education',
  'ben_stepans_distribution_network',
  'ben_pospisil_doctrine',
  'ben_claimant_to_czech_leadership',
  'ben_socialist_successor_federation'
]

missing_ideas = []
for i in ideas:
    if i not in defined_keys:
        missing_ideas.append((i, 'name'))
    if f'{i}_desc' not in defined_keys:
        missing_ideas.append((i, 'desc'))

print(f'Missing idea loc count: {len(missing_ideas)}')
for m in missing_ideas:
    print(' ', m)

