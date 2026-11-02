import glob, re

loc_keys = set()
for f in glob.glob('localisation/english/*_l_english.yml'):
    with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
        for line in fp:
            line = line.strip()
            if line.startswith('#') or not line or line.startswith('l_english:'):
                continue
            m = re.match(r'^\s*([a-zA-Z0-9_\.]+)\s*:', line)
            if m:
                loc_keys.add(m.group(1))

print(f'Total English loc keys: {len(loc_keys)}')

check_keys = [
    'ben_op_pra_arsenals_not_fortified_tt',
    'pra_has_sufficient_pp_tt',
    'pra_infiltrators_not_purged_tt',
    'pra_has_sufficient_manpower_tt',
    'ben_archived_trade_ledgers',
    'ben_archived_trade_ledgers_desc',
    'ben_covert.25.t', 'ben_covert.25.d', 'ben_covert.25.a',
    'ben_covert.26.t', 'ben_covert.26.d', 'ben_covert.26.a',
    'ben_covert.27.t', 'ben_covert.27.d', 'ben_covert.27.a',
]

missing = [k for k in check_keys if k not in loc_keys]
if missing:
    print('MISSING KEYS:', missing)
else:
    print('ALL NEW TOOLTIPS, IDEAS, AND FALLBACK EVENTS LOCALIZED!')

