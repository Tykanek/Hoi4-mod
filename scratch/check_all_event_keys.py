import re
import os

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

with open(r'events\beneshov_event.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Match each event id
event_ids = re.findall(r'id\s*=\s*(benesov[^\s\}]+)', text)
print("Event IDs:", event_ids)

# Find all title, desc, and option name references
titles = re.findall(r'title\s*=\s*([^\s\}]+)', text)
descs = re.findall(r'desc\s*=\s*([^\s\}]+)', text)
option_names = re.findall(r'name\s*=\s*(benesov[^\s\}]+)', text)

missing = []
for k in titles + descs + option_names:
    if k not in defined_keys:
        missing.append(k)

print("Total event keys checked:", len(titles + descs + option_names))
print("Missing event keys:", missing)

