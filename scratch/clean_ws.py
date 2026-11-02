with open('common/ideas/benesov.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

clean_lines = [l.rstrip() + '\n' for l in lines]
with open('common/ideas/benesov.txt', 'w', encoding='utf-8') as f:
    f.writelines(clean_lines)

print('Cleaned trailing whitespace in common/ideas/benesov.txt')

