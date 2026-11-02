with open('localisation/english/mod_characters_l_english.yml', 'r', encoding='utf-8') as f:
    text = f.read()

if 'ben_mia_revolutionary:' in text:
    print('Already present!')
else:
    new_loc = """ ben_mia_revolutionary: "Proletarian Mascot"
 ben_mia_revolutionary_desc: "Mia's unwavering loyalty and quiet dignity rally party comrades, improving district coordination and boosting administrative political power."
"""
    with open('localisation/english/mod_characters_l_english.yml', 'w', encoding='utf-8') as f:
        f.write(text + new_loc)
    print('Added Mia revolutionary trait loc!')
