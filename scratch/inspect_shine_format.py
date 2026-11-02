with open('interface/BEN_focus_icons.gfx', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's find one existing shine sprite (e.g. earlier in the file)
lines = text.splitlines()

# Print lines 20-50
print("--- EXISTING WORKING SHINE EXAMPLE ---")
for i in range(min(len(lines), 60)):
    if 'shine' in lines[i].lower():
        start = max(0, i - 1)
        end = min(len(lines), i + 35)
        for j in range(start, end):
            print(lines[j])
        break

print("\n--- NEW SHINE SPRITES AT END OF FILE ---")
for i in range(len(lines) - 1, -1, -1):
    if 'eyes_on_prague_shine' in lines[i]:
        start = max(0, i - 1)
        end = len(lines)
        for j in range(start, min(end, start + 50)):
            print(lines[j])
        break

