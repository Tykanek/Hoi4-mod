with open('common/ideas/benesov.txt', 'r', encoding='utf-8') as f:
    text = f.read()

if 'ben_archived_trade_ledgers' in text:
    print('Already present!')
else:
    target = 'ben_prague_defector_engineers = {'
    idx = text.find(target)
    new_idea = """ben_archived_trade_ledgers = {
			picture = generic_goods_red_bonus
			allowed = { always = no }
			removal_cost = -1
			modifier = {
				consumer_goods_factor = -0.03
				trade_opinion_factor = 0.10
			}
		}

		"""
    updated = text[:idx] + new_idea + text[idx:]
    with open('common/ideas/benesov.txt', 'w', encoding='utf-8') as f:
        f.write(updated)
    print('Added ben_archived_trade_ledgers successfully!')

