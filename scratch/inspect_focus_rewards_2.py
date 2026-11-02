with open('common/national_focus/benesov.txt', 'r', encoding='utf-8') as f:
    text = f.read()

idx2 = text.find('id = ben_follow_the_money')
idx3 = text.find('id = ben_a_better_life_in_benesov')

print('--- ben_follow_the_money ---')
print(text[idx2:idx2+600])

print('--- ben_a_better_life_in_benesov ---')
print(text[idx3:idx3+600])

