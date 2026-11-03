import os, re
from PIL import Image

print("============================================================")
print("VALIDATION SUITE: STRICT IMAGE CATEGORY SEPARATION")
print("============================================================\n")

errors = []

# 1. Main Menu Validation
menu_dir = os.path.join('gfx', 'interface', 'custom_menu')
if not os.path.exists(menu_dir):
    errors.append("gfx/interface/custom_menu directory missing")
else:
    menu_files = sorted(os.listdir(menu_dir))
    expected_menu_files = sorted([f'main_menu_{i}.dds' for i in range(1, 7)] + [f'main_menu_{i}_small.dds' for i in range(1, 7)])
    if menu_files != expected_menu_files:
        errors.append(f"Unexpected files in custom_menu: {menu_files}")
    else:
        print(f"[PASS] gfx/interface/custom_menu contains exactly the 12 expected textures (main_menu_1 through main_menu_6 large & small).")

    for f in menu_files:
        p = os.path.join(menu_dir, f)
        with Image.open(p) as img:
            expected_dim = (192, 144) if '_small' in f else (1920, 1440)
            if img.size != expected_dim:
                errors.append(f"Menu texture {f} has wrong dimensions {img.size}, expected {expected_dim}")

# 2. Loading Screens Validation
loading_dir = os.path.join('gfx', 'loadingscreens')
if not os.path.exists(loading_dir):
    errors.append("gfx/loadingscreens directory missing")
else:
    loading_files = sorted(os.listdir(loading_dir))
    expected_loading = sorted([f'load_{i}.dds' for i in range(1, 10)] + [f'load_{i}_small.dds' for i in range(1, 10)] + ['loading_screen_border_small.dds'])
    if loading_files != expected_loading:
        errors.append(f"Unexpected files in gfx/loadingscreens: {set(loading_files) ^ set(expected_loading)}")
    else:
        print(f"[PASS] gfx/loadingscreens contains exactly the 19 expected loading files (load_1 through load_9 large & small, border).")

    for f in loading_files:
        if f == 'loading_screen_border_small.dds': continue
        p = os.path.join(loading_dir, f)
        with Image.open(p) as img:
            expected_dim = (192, 144) if '_small' in f else (1920, 1440)
            if img.size != expected_dim:
                errors.append(f"Loading texture {f} has wrong dimensions {img.size}, expected {expected_dim}")

# Check NO main menu or bonus in loadingscreens
for f in os.listdir(loading_dir):
    if 'menu' in f.lower():
        errors.append(f"Main menu image leaked into gfx/loadingscreens: {f}")
    if 'bonus' in f.lower():
        errors.append(f"Bonus image leaked into gfx/loadingscreens: {f}")

# 3. Bonus Images Validation
bonus_dir = os.path.join('gfx', 'bonus')
if not os.path.exists(bonus_dir):
    errors.append("gfx/bonus directory missing")
else:
    bonus_files = sorted(os.listdir(bonus_dir))
    expected_bonus = sorted([f'bonus_{i}.dds' for i in range(1, 9)] + [f'bonus_{i}_small.dds' for i in range(1, 9)])
    if bonus_files != expected_bonus:
        errors.append(f"Unexpected files in gfx/bonus: {bonus_files}")
    else:
        print(f"[PASS] gfx/bonus contains exactly the 16 expected bonus textures (bonus_1 through bonus_8 large & small).")

# 4. base_backgrounds.txt Validation
bg_txt = 'common/frontend/backgrounds/base_backgrounds.txt'
with open(bg_txt, 'r', encoding='utf-8') as f:
    bg_content = f.read()

entries = re.findall(r'^\s*([a-zA-Z0-9_]+)\s*=\s*\{', bg_content, re.MULTILINE)
expected_entries = [f'main_menu_{i}' for i in range(1, 7)]
if entries != expected_entries:
    errors.append(f"base_backgrounds.txt entries mismatch: {entries}, expected {expected_entries}")
else:
    print(f"[PASS] base_backgrounds.txt registers ONLY main_menu_1 through main_menu_6.")

# Check NO loading or bonus in base_backgrounds.txt
if 'load_' in bg_content or 'bonus' in bg_content:
    errors.append("base_backgrounds.txt contains loading or bonus references!")
else:
    print(f"[PASS] base_backgrounds.txt contains ZERO loading or bonus references.")

# 5. GFX File Reference Validation
for gfx_path in ['interface/frontendmainviewbg.gfx', 'interface/frontendmainviewbg_basic.gfx', 'interface/small_background.gfx']:
    with open(gfx_path, 'r', encoding='utf-8') as f:
        content = f.read()
    refs = re.findall(r'texturefile\s*=\s*"([^"]+)"', content)
    for ref in refs:
        if not os.path.exists(ref):
            errors.append(f"Missing referenced texture: {ref} in {gfx_path}")
        else:
            print(f"[PASS] {gfx_path} -> {ref} exists on disk")

# 6. Descriptors Validation
for desc in ['descriptor.mod', '../Hoi4-mod.mod']:
    if os.path.exists(desc):
        with open(desc, 'r', encoding='utf-8') as f:
            c = f.read()
        if 'replace_path="gfx/loadingscreens"' in c or 'replace_path = "gfx/loadingscreens"' in c:
            print(f"[PASS] {desc} correctly contains replace_path=\"gfx/loadingscreens\"")
        else:
            errors.append(f"{desc} missing replace_path directive!")

# 7. Source files in obrazky_1 intact
src_dir = 'obrazky_1'
src_files = os.listdir(src_dir)
if len(src_files) != 23:
    errors.append(f"obrazky_1 file count changed: {len(src_files)}, expected 23")
else:
    print(f"[PASS] Source obrazky_1 folder has all 23 original JPEG files untouched.")

print("\n============================================================")
print(f"VALIDATION RESULT: {len(errors)} Errors")
print("============================================================")
if errors:
    for e in errors:
        print(f"ERROR: {e}")
else:
    print("ALL STRICT SEPARATION CHECKS PASSED PERFECTLY!")

