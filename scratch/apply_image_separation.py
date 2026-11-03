import os, shutil

# 1. Directories
menu_dir = os.path.join('gfx', 'interface', 'custom_menu')
bonus_dir = os.path.join('gfx', 'bonus')
loading_dir = os.path.join('gfx', 'loadingscreens')

os.makedirs(menu_dir, exist_ok=True)
os.makedirs(bonus_dir, exist_ok=True)
os.makedirs(loading_dir, exist_ok=True)

# 2. Move/copy Main Menu textures to gfx/interface/custom_menu/
for i in range(1, 7):
    # Source might be load_main_menu.dds or load_main_menu_X.dds in gfx/loadingscreens
    src_large_name = 'load_main_menu.dds' if i == 1 else f'load_main_menu_{i}.dds'
    src_small_name = 'load_main_menu_small.dds' if i == 1 else f'load_main_menu_{i}_small.dds'

    src_large = os.path.join(loading_dir, src_large_name)
    src_small = os.path.join(loading_dir, src_small_name)

    dst_large = os.path.join(menu_dir, f'main_menu_{i}.dds')
    dst_small = os.path.join(menu_dir, f'main_menu_{i}_small.dds')

    if os.path.exists(src_large):
        shutil.copy2(src_large, dst_large)
        print(f'Copied {src_large} -> {dst_large}')
    if os.path.exists(src_small):
        shutil.copy2(src_small, dst_small)
        print(f'Copied {src_small} -> {dst_small}')

# 3. Move/copy Bonus textures to gfx/bonus/
for i in range(1, 9):
    # Bonus was previously load_10 through load_17
    load_num = 9 + i
    src_large = os.path.join(loading_dir, f'load_{load_num}.dds')
    src_small = os.path.join(loading_dir, f'load_{load_num}_small.dds')

    dst_large = os.path.join(bonus_dir, f'bonus_{i}.dds')
    dst_small = os.path.join(bonus_dir, f'bonus_{i}_small.dds')

    if os.path.exists(src_large):
        shutil.copy2(src_large, dst_large)
        print(f'Copied {src_large} -> {dst_large}')
    if os.path.exists(src_small):
        shutil.copy2(src_small, dst_small)
        print(f'Copied {src_small} -> {dst_small}')

# 4. Clean up gfx/loadingscreens:
# Keep ONLY load_1.dds to load_9.dds, load_1_small.dds to load_9_small.dds, and loading_screen_border_small.dds
keep_loading_files = {'loading_screen_border_small.dds'}
for i in range(1, 10):
    keep_loading_files.add(f'load_{i}.dds')
    keep_loading_files.add(f'load_{i}_small.dds')

for f in os.listdir(loading_dir):
    if f not in keep_loading_files:
        p = os.path.join(loading_dir, f)
        os.remove(p)
        print(f'Removed non-loading screen file: {f}')

print(f'\ngfx/loadingscreens now contains {len(os.listdir(loading_dir))} files:')
print(sorted(os.listdir(loading_dir)))

print(f'\ngfx/interface/custom_menu now contains {len(os.listdir(menu_dir))} files:')
print(sorted(os.listdir(menu_dir)))

print(f'\ngfx/bonus now contains {len(os.listdir(bonus_dir))} files:')
print(sorted(os.listdir(bonus_dir)))

