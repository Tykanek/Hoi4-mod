import re
import os

with open(r'events\beneshov_event.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# load loc keys
loc_dir = r'localisation\english'
defined_keys = {}
for fname in os.listdir(loc_dir):
    if fname.endswith('.yml'):
        p = os.path.join(loc_dir, fname)
        with open(p, 'r', encoding='utf-8', errors='ignore') as fp:
            for line in fp:
                m = re.match(r'^\s*([A-Za-z0-9_.\-]+):(?:\d+)?\s*\"(.*)\"\s*$', line)
                if m:
                    defined_keys[m.group(1)] = (fname, m.group(2))

# parse event blocks
pattern = re.compile(r'country_event\s*=\s*\{([^{}]*(?:\{[^{}]*(?:\{[^{}]*\}[^{}]*)*\}[^{}]*)*)\}')
events = pattern.findall(text)

print(f"Total events: {len(events)}")
for ev in events:
    m_id = re.search(r'id\s*=\s*([^\s\}]+)', ev)
    m_title = re.search(r'title\s*=\s*([^\s\}]+)', ev)
    m_desc = re.search(r'desc\s*=\s*([^\s\}]+)', ev)
    options = re.findall(r'option\s*=\s*\{[^{}]*?name\s*=\s*([^\s\}]+)', ev)

    eid = m_id.group(1) if m_id else 'unknown'
    title = m_title.group(1) if m_title else None
    desc = m_desc.group(1) if m_desc else None

    print(f"\nEvent: {eid}")
    if title:
        status = 'OK' if title in defined_keys else 'MISSING'
        print(f"  Title [{title}]: {status}")
    if desc:
        status = 'OK' if desc in defined_keys else 'MISSING'
        print(f"  Desc  [{desc}]: {status}")
    for opt in options:
        status = 'OK' if opt in defined_keys else 'MISSING'
        print(f"  Option [{opt}]: {status}")

