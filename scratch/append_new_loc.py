with open('localisation/english/ben_covert_l_english.yml', 'r', encoding='utf-8') as f:
    text = f.read()

new_loc = """
 # --- New Custom Tooltips & Fallbacks ---
 ben_op_pra_arsenals_not_fortified_tt: "§RPrague's central armories are currently under fortified military guard.§!"
 pra_has_sufficient_pp_tt: "§RPrague treasury has at least 50 Political Power to divert.§!"
 pra_infiltrators_not_purged_tt: "§RPrague police are conducting an active anti-espionage crackdown.§!"
 pra_has_sufficient_manpower_tt: "§RPrague has at least 400 available manpower in reserve.§!"

 ben_archived_trade_ledgers: "Archived Commercial Ledgers"
 ben_archived_trade_ledgers_desc: "Salvaged municipal accounting ledgers provide valuable insights into regional supply networks and commercial arrangements."

 ben_covert.25.t: "Prague Depots Inactive"
 ben_covert.25.d: "Our reconnaissance squad found the storage depots in Prague empty and inactive. Without military equipment to divert, our scouts thoroughly mapped the district transport nodes, providing our staff with valuable operational experience."
 ben_covert.25.a: "Take note of the terrain."

 ben_covert.26.t: "Prague Treasury Depleted"
 ben_covert.26.d: "Our financial infiltrators report that Prague's municipal accounts are completely drained or inaccessible. Rather than returning empty-handed, our agents recovered historical trade contracts and merchant directories."
 ben_covert.26.a: "Knowledge is valuable in its own right."

 ben_covert.27.t: "Focusing on Our Own Workers"
 ben_covert.27.d: "With Prague unable or unwilling to spare working hands, Beneshov's municipal council redirected administrative focus toward local district welfare and community solidarity."
 ben_covert.27.a: "Beneshov relies on its own strength."
"""

with open('localisation/english/ben_covert_l_english.yml', 'w', encoding='utf-8-sig') as f:
    f.write(text.strip() + '\n' + new_loc)

print('Updated localisation/english/ben_covert_l_english.yml successfully!')

