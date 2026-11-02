with open('common/national_focus/benesov.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Inspect current blocks
idx1 = text.find('id = ben_the_missing_rifles')
idx2 = text.find('id = ben_follow_the_money')
idx3 = text.find('id = ben_a_better_life_in_benesov')

print('--- ben_the_missing_rifles ---')
print(text[idx1:idx1+1100])

