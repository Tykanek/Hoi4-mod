import os, struct, re

mod_root = r"C:\Users\lukas\Documents\Paradox Interactive\Hearts of Iron IV\mod\Hoi4-mod"
settings_path = r"C:\Users\lukas\Documents\Paradox Interactive\Hearts of Iron IV\settings.txt"

print("=" * 60)
print("AUDIT & VALIDATION: BACKGROUNDS, LOADING SCREENS & CUSTOM IMAGES")
print("=" * 60)

passed = 0
failed = 0

def check(condition, desc):
    global passed, failed
    if condition:
        print(f"[PASS] {desc}")
        passed += 1
    else:
        print(f"[FAIL] {desc}")
        failed += 1

# Check 1: base_backgrounds.txt registration
base_bg_path = os.path.join(mod_root, "common", "frontend", "backgrounds", "base_backgrounds.txt")
check(os.path.exists(base_bg_path), "common/frontend/backgrounds/base_backgrounds.txt exists")

with open(base_bg_path, "r", encoding="utf-8") as f:
    base_bg_content = f.read()

expected_menu_keys = [f"main_menu_{i}" for i in range(1, 7)]
for key in expected_menu_keys:
    check(f"{key} =" in base_bg_content, f"Entry {key} is registered in base_backgrounds.txt")

# Check 2 & 8: No loading screens in base_backgrounds.txt
for i in range(1, 10):
    check(f"load_{i} =" not in base_bg_content, f"Loading screen load_{i} is NOT in base_backgrounds.txt")

# Check 3: Check texture resolution, DDS magic, and size for main menu images in gfx/loadingscreens
loading_dir = os.path.join(mod_root, "gfx", "loadingscreens")
for i in range(1, 7):
    large_file = os.path.join(loading_dir, f"main_menu_{i}.dds")
    small_file = os.path.join(loading_dir, f"main_menu_{i}_small.dds")

    check(os.path.exists(large_file), f"main_menu_{i}.dds exists in gfx/loadingscreens")
    check(os.path.exists(small_file), f"main_menu_{i}_small.dds exists in gfx/loadingscreens")

    # Read headers
    with open(large_file, "rb") as f:
        magic = f.read(4)
        hdr = f.read(124)
        h, w = struct.unpack('<II', hdr[8:16])
        check(magic == b"DDS " and w == 1920 and h == 1440, f"main_menu_{i}.dds is valid DDS 1920x1440")

    with open(small_file, "rb") as f:
        magic = f.read(4)
        hdr = f.read(124)
        h, w = struct.unpack('<II', hdr[8:16])
        check(magic == b"DDS " and w == 192 and h == 144, f"main_menu_{i}_small.dds is valid DDS 192x144")

# Check 4: Check GFX sprites in interface/small_background.gfx and frontendmainviewbg.gfx
small_bg_gfx = os.path.join(mod_root, "interface", "small_background.gfx")
with open(small_bg_gfx, "r", encoding="utf-8") as f:
    small_gfx_content = f.read()

for i in range(1, 7):
    check(f"GFX_main_menu_{i}_small" in small_gfx_content, f"Sprite GFX_main_menu_{i}_small defined in small_background.gfx")

frontend_gfx = os.path.join(mod_root, "interface", "frontendmainviewbg.gfx")
with open(frontend_gfx, "r", encoding="utf-8") as f:
    fe_gfx_content = f.read()

check("GFX_frontend_bg" in fe_gfx_content, "Sprite GFX_frontend_bg defined in frontendmainviewbg.gfx")
for i in range(1, 7):
    check(f"GFX_main_menu_{i}" in fe_gfx_content, f"Sprite GFX_main_menu_{i} defined in frontendmainviewbg.gfx")

# Check 5: Rotation timer define exists
defines_file = os.path.join(mod_root, "common", "defines", "menu_rotation_defines.lua")
check(os.path.exists(defines_file), "common/defines/menu_rotation_defines.lua exists")
with open(defines_file, "r", encoding="utf-8") as f:
    check("TIME_TO_SWAP_BACKGROUNDS = 20" in f.read(), "TIME_TO_SWAP_BACKGROUNDS = 20 explicitly set")

# Check 6: Check user's settings.txt
if os.path.exists(settings_path):
    with open(settings_path, "r", encoding="utf-8", errors="ignore") as f:
        st = f.read()
    check("gfx/loadingscreens/main_menu_1.dds" in st, "settings.txt contains main_menu_1.dds")
    check("gfx/loadingscreens/main_menu_6.dds" in st, "settings.txt contains main_menu_6.dds")
    # check weights
    m_weight = re.search(r"weight=\{([^}]*)\}", st)
    if m_weight:
        weights = m_weight.group(1).split()
        check(len(weights) == 6 and all(w == "1" for w in weights), f"settings.txt has all 6 weights enabled (=1): {weights}")
    else:
        check(False, "settings.txt weight block found")

# Check 7: 9 Loading images present and valid
for i in range(1, 10):
    lf = os.path.join(loading_dir, f"load_{i}.dds")
    lfs = os.path.join(loading_dir, f"load_{i}_small.dds")
    check(os.path.exists(lf), f"Loading screen load_{i}.dds exists")
    check(os.path.exists(lfs), f"Loading screen thumbnail load_{i}_small.dds exists")
    with open(lf, "rb") as f:
        magic = f.read(4)
        hdr = f.read(124)
        h, w = struct.unpack('<II', hdr[8:16])
        check(magic == b"DDS " and w == 1920 and h == 1440, f"load_{i}.dds is valid DDS 1920x1440")

# Check 8: 8 Bonus images preserved in gfx/bonus
bonus_dir = os.path.join(mod_root, "gfx", "bonus")
check(os.path.exists(bonus_dir), "gfx/bonus/ exists")
for i in range(1, 9):
    bf = os.path.join(bonus_dir, f"bonus_{i}.dds")
    bfs = os.path.join(bonus_dir, f"bonus_{i}_small.dds")
    check(os.path.exists(bf), f"Bonus image bonus_{i}.dds preserved")
    check(os.path.exists(bfs), f"Bonus thumbnail bonus_{i}_small.dds preserved")

print("=" * 60)
print(f"RESULTS: {passed} PASSED, {failed} FAILED")
print("=" * 60)

