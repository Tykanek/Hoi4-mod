with open('interface/BEN_focus_icons.gfx', 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.splitlines()
for l in lines[:25]:
    print(l)
