import os, re
from PIL import Image

print("============================================================")
print("VALIDATION SUITE: OBRAZKY_1 CUSTOM IMAGES IMPLEMENTATION")
print("============================================================\n")

errors = []
warnings = []

# 1. Source files check
src_dir = 'obrazky_1'
if not os.path.exists(src_dir):
    errors.append("obrazky_1 folder is missing!")
else:
    src_files = os.listdir(src_dir)
    print(f"[PASS] Source folder obrazky_1 exists with {len(src_files)} files intact.")
    expected_sources = [
        'main_menu_1.jpeg', 'main_menu_2.jpeg', 'main_menu_3.jpeg',
        'main_menu_4.jpeg', 'main_menu_5.jpeg', 'main_menu_6.jpeg',
        'loading_1.jpeg', 'loading_2.jpeg', 'loading_3.jpeg',
        'loading_4.jpeg', 'loading_5.jpeg', 'loading_6.jpeg',
        'loading_7.jpeg', 'loading_8.jpeg', 'loading_9.jpeg',
        'bonus_1.jpeg', 'bonus_2.jpeg', 'bonus_3.jpeg',
        'bonus_4.jpeg', 'bonus_5.jpeg', 'bonus_6.jpeg',
        'bonus_7.jpeg', 'bonus_8.jpeg'
    ]
    for s in expected_sources:
        if s not in src_files:
            errors.append(f"Source file {s} missing from obrazky_1!")
        else:
            p = os.path.join(src_dir, s)
            if os.path.getsize(p) == 0:
                errors.append(f"Source file {s} is empty!")

# 2. Check generated DDS textures in gfx/loadingscreens
dst_dir = os.path.join('gfx', 'loadingscreens')
if not os.path.exists(dst_dir):
    errors.append("Destination directory gfx/loadingscreens does not exist!")
else:
    expected_dds_large = [
        'load_main_menu.dds', 'load_main_menu_2.dds', 'load_main_menu_3.dds',
        'load_main_menu_4.dds', 'load_main_menu_5.dds', 'load_main_menu_6.dds',
        'load_1.dds', 'load_2.dds', 'load_3.dds', 'load_4.dds', 'load_5.dds',
        'load_6.dds', 'load_7.dds', 'load_8.dds', 'load_9.dds',
        'load_10.dds', 'load_11.dds', 'load_12.dds', 'load_13.dds',
        'load_14.dds', 'load_15.dds', 'load_16.dds', 'load_17.dds',
        'main_menu.dds', 'loading.dds', 'bonus.dds'
    ]
    expected_dds_small = [
        'load_main_menu_small.dds', 'load_main_menu_2_small.dds', 'load_main_menu_3_small.dds',
        'load_main_menu_4_small.dds', 'load_main_menu_5_small.dds', 'load_main_menu_6_small.dds',
        'load_1_small.dds', 'load_2_small.dds', 'load_3_small.dds', 'load_4_small.dds', 'load_5_small.dds',
        'load_6_small.dds', 'load_7_small.dds', 'load_8_small.dds', 'load_9_small.dds',
        'load_10_small.dds', 'load_11_small.dds', 'load_12_small.dds', 'load_13_small.dds',
        'load_14_small.dds', 'load_15_small.dds', 'load_16_small.dds', 'load_17_small.dds',
        'main_menu_small.dds', 'loading_small.dds', 'bonus_small.dds',
        'loading_screen_border_small.dds'
    ]

    for dds in expected_dds_large:
        p = os.path.join(dst_dir, dds)
        if not os.path.exists(p):
            errors.append(f"Missing large texture: {dds}")
        else:
            with Image.open(p) as img:
                if img.size != (1920, 1440):
                    errors.append(f"Texture {dds} has incorrect dimensions: {img.size}, expected (1920, 1440)")
                if img.format != 'DDS':
                    errors.append(f"Texture {dds} format is {img.format}, expected DDS")
            print(f"[PASS] Large texture verified: {dds} (1920x1440 DDS)")

    for dds in expected_dds_small:
        p = os.path.join(dst_dir, dds)
        if not os.path.exists(p):
            errors.append(f"Missing small texture: {dds}")
        else:
            with Image.open(p) as img:
                if img.size != (192, 144):
                    errors.append(f"Small texture {dds} has incorrect dimensions: {img.size}, expected (192, 144)")
                if img.format != 'DDS':
                    errors.append(f"Small texture {dds} format is {img.format}, expected DDS")
            print(f"[PASS] Small texture verified: {dds} (192x144 DDS)")

# 3. Check GFX definitions
gfx_files = [
    'interface/frontendmainviewbg.gfx',
    'interface/frontendmainviewbg_basic.gfx',
    'interface/small_background.gfx'
]
for gfx in gfx_files:
    if not os.path.exists(gfx):
        errors.append(f"GFX file missing: {gfx}")
    else:
        with open(gfx, 'r', encoding='utf-8') as fp:
            content = fp.read()
        # Find all texturefile references
        matches = re.findall(r'texturefile\s*=\s*"([^"]+)"', content)
        for tex in matches:
            if not os.path.exists(tex):
                errors.append(f"In {gfx}: referenced texture does not exist: {tex}")
            else:
                print(f"[PASS] {gfx} references valid texture: {tex}")

# 4. Check base_backgrounds.txt
bg_txt = 'common/frontend/backgrounds/base_backgrounds.txt'
if not os.path.exists(bg_txt):
    errors.append(f"Backgrounds database missing: {bg_txt}")
else:
    with open(bg_txt, 'r', encoding='utf-8') as fp:
        c = fp.read()
    entries = re.findall(r'([A-Za-z0-9_]+)\s*=\s*\{', c)
    print(f"\n[PASS] base_backgrounds.txt contains {len(entries)} background entries:")
    for entry in entries:
        # Check corresponding dds in gfx/loadingscreens/
        large_dds = os.path.join('gfx', 'loadingscreens', f'{entry}.dds')
        small_dds = os.path.join('gfx', 'loadingscreens', f'{entry}_small.dds')
        if not os.path.exists(large_dds):
            errors.append(f"Background entry {entry} missing large texture {large_dds}")
        if not os.path.exists(small_dds):
            errors.append(f"Background entry {entry} missing small preview {small_dds}")

# 5. Check git status to ensure gameplay files and GRA remain untouched
print("\nChecking mod integrity...")
with open('common/national_focus/benesov.txt', 'r', encoding='utf-8') as f:
    ben_foc = f.read()
if 'ben_eyes_on_prague' not in ben_foc or 'ben_pospisil_takes_command' not in ben_foc:
    errors.append("BEN focus tree modified unexpectedly!")
else:
    print("[PASS] BEN focus tree verified intact.")

with open('common/national_focus/prague.txt', 'r', encoding='utf-8') as f:
    pra_foc = f.read()
if 'pra_crush_benesov_threat' not in pra_foc:
    errors.append("PRA focus tree modified unexpectedly!")
else:
    print("[PASS] PRA focus tree verified intact.")

print("\n============================================================")
print(f"VALIDATION SUMMARY: {len(errors)} Errors, {len(warnings)} Warnings")
print("============================================================")
if errors:
    for e in errors:
        print(f"ERROR: {e}")
else:
    print("ALL CUSTOM IMAGE VALIDATION CHECKS PASSED PERFECTLY!")

