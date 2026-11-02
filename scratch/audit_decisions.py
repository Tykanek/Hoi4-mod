import os
import re

print("========================================================")
print("AUDITING BEN DECISIONS & CATEGORIES")
print("========================================================")

dec_files = [
    'common/decisions/ben_emergency_economy.txt',
    'common/decisions/ben_integration.txt',
    'common/decisions/ben_pra_bidding_war.txt',
    'common/decisions/ben_pra_rivalry.txt',
    'common/decisions/ben_propaganda.txt'
]

cat_files = [
    'common/decisions/categories/ben_decisions_categories.txt',
    'common/decisions/categories/ben_pra_bidding_war_categories.txt'
]

# 1. Load categories
categories = {}
for cf in cat_files:
    with open(cf, 'r', encoding='utf-8', errors='ignore') as fp:
        text = fp.read()
        # Find category blocks: <cat_id> = { ... }
        chunks = re.findall(r'(\b[a-zA-Z0-9_]+)\s*=\s*\{([^{}]*(?:\{[^{}]*(?:\{[^{}]*\}[^{}]*)*\}[^{}]*)*)\}', text)
        for cat_id, body in chunks:
            if cat_id not in ('priority', 'allowed', 'visible', 'custom_icon'):
                categories[cat_id] = body

print(f"Loaded {len(categories)} decision categories: {list(categories.keys())}")

# 2. Load decisions
decisions = {}
for df in dec_files:
    with open(df, 'r', encoding='utf-8', errors='ignore') as fp:
        text = fp.read()
        # Find category wraps or decision blocks
        # Usually file has: <category_id> = { <decision_1> = { ... } <decision_2> = { ... } }
        lines = text.splitlines()
        current_cat = None
        for chunk in text.split('\n\t}'):
            pass

print("\nScanning decisions line by line...")
for df in dec_files:
    print(f"\n--- {df} ---")
    with open(df, 'r', encoding='utf-8', errors='ignore') as fp:
        text = fp.read()
        # find all decision names
        # A decision has: cost =, complete_effect =, etc.
        d_matches = re.findall(r'(\b[a-zA-Z0-9_]+)\s*=\s*\{[^{}]*?(?:cost|available|complete_effect|days_remove|days_re_enable)', text)
        print(f"Decisions found ({len(d_matches)}): {d_matches}")
        for dm in d_matches:
            # find block
            idx = text.find(dm)
            end_idx = text.find('\n\t}', idx)
            snippet = text[idx:end_idx+3] if end_idx != -1 else text[idx:idx+400]
            # check if referenced category is valid
            # check available, cost, etc.

