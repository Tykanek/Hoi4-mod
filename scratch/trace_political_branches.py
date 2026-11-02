import re

with open(r'common\national_focus\benesov.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's see all focuses following ben_the_benesov_question
focus_chunks = text.split('focus = {')[1:]

tree = {}
for chunk in focus_chunks:
    m_id = re.search(r'id\s*=\s*([^\s\}]+)', chunk)
    if not m_id: continue
    fid = m_id.group(1)

    prereqs = []
    for pm in re.finditer(r'prerequisite\s*=\s*\{([^}]+)\}', chunk):
        p_foci = re.findall(r'focus\s*=\s*([^\s\}]+)', pm.group(1))
        if p_foci:
            prereqs.append(p_foci)
    tree[fid] = prereqs

def get_descendants(start):
    desc = set()
    frontier = [start]
    while frontier:
        curr = frontier.pop(0)
        for fid, prereqs in tree.items():
            for pgroup in prereqs:
                if curr in pgroup and fid not in desc:
                    desc.add(fid)
                    frontier.append(fid)
    return desc

republic_branch = get_descendants('ben_we_still_need_the_republic')
stand_alone_branch = get_descendants('ben_benesov_can_stand_alone')

print(f"Descendants of ben_we_still_need_the_republic ({len(republic_branch)}):")
for f in sorted(republic_branch):
    print(" ", f)

print(f"\nDescendants of ben_benesov_can_stand_alone ({len(stand_alone_branch)}):")
for f in sorted(stand_alone_branch):
    print(" ", f)

common = republic_branch & stand_alone_branch
print(f"\nCommon descendants between the two ({len(common)}): {common}")

