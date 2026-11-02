import os, re

loc_dir = r'localisation\english'
defined_keys = set()
for fname in os.listdir(loc_dir):
    if fname.endswith('.yml'):
        with open(os.path.join(loc_dir, fname), 'r', encoding='utf-8', errors='ignore') as fp:
            for line in fp:
                m = re.match(r'^\s*([A-Za-z0-9_.\-]+):(?:\d+)?\s*\"(.*)\"\s*$', line)
                if m:
                    defined_keys.add(m.group(1))

companies = [
    'BEN_beneshov_construction_directorate',
    'BEN_district_railway_authority',
    'BEN_beneshov_electrical_works',
    'BEN_national_workshop_cooperative',
    'BEN_beneshov_arms_works',
    'BEN_pospisil_engineering_cooperative',
    'BEN_pecka_industrial_combine',
    'BEN_beneshov_aviation_workshops',
    'BEN_workers_strategic_institute',
    'BEN_beneshov_logistics_school',
    'BEN_district_aviation_committee',
    'BEN_department_of_improvised_warfare'
]

missing_comp = []
for c in companies:
    if c not in defined_keys:
        missing_comp.append(c)

print(f"Missing company localization ({len(missing_comp)}): {missing_comp}")

