import sys; sys.path.append('scratch')
from parse_actual_ideas import parse_ideas

ben_ideas = dict(parse_ideas('common/ideas/benesov.txt'))
pra_ideas = dict(parse_ideas('common/ideas/prague.txt'))

overlap = set(ben_ideas.keys()) & set(pra_ideas.keys())
print('Ideas in both benesov.txt and prague.txt:', overlap)

