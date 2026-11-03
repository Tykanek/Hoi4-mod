import os, shutil
from PIL import Image

def detect_format(raw):
    if raw.startswith(b'\xff\xd8\xff'): return 'JPEG'
    if raw.startswith(b'\x89PNG\r\n\x1a\n'): return 'PNG'
    if raw.startswith(b'RIFF') and raw[8:12] == b'WEBP': return 'WEBP'
    if raw.startswith(b'DDS '): return 'DDS'
    if raw.startswith(b'BM'): return 'BMP'
    if raw.startswith(b'GIF87a') or raw.startswith(b'GIF89a'): return 'GIF'
    return 'UNKNOWN'

src_dir = 'obrazky_1'
dst_dir = os.path.join('gfx', 'loadingscreens')
os.makedirs(dst_dir, exist_ok=True)

# File mappings: (source_filename, base_output_name)
mapping = [
    # Main menu backgrounds
    ('main_menu_1.jpeg', 'load_main_menu'),
    ('main_menu_2.jpeg', 'load_main_menu_2'),
    ('main_menu_3.jpeg', 'load_main_menu_3'),
    ('main_menu_4.jpeg', 'load_main_menu_4'),
    ('main_menu_5.jpeg', 'load_main_menu_5'),
    ('main_menu_6.jpeg', 'load_main_menu_6'),

    # Loading screens (load_1 is startup loading screen)
    ('loading_1.jpeg', 'load_1'),
    ('loading_2.jpeg', 'load_2'),
    ('loading_3.jpeg', 'load_3'),
    ('loading_4.jpeg', 'load_4'),
    ('loading_5.jpeg', 'load_5'),
    ('loading_6.jpeg', 'load_6'),
    ('loading_7.jpeg', 'load_7'),
    ('loading_8.jpeg', 'load_8'),
    ('loading_9.jpeg', 'load_9'),

    # Bonus illustrations as additional loading screens (load_10 to load_17)
    ('bonus_1.jpeg', 'load_10'),
    ('bonus_2.jpeg', 'load_11'),
    ('bonus_3.jpeg', 'load_12'),
    ('bonus_4.jpeg', 'load_13'),
    ('bonus_5.jpeg', 'load_14'),
    ('bonus_6.jpeg', 'load_15'),
    ('bonus_7.jpeg', 'load_16'),
    ('bonus_8.jpeg', 'load_17'),
]

game_dir = r'C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV'

# Copy vanilla loading_screen_border_small.dds
border_src = os.path.join(game_dir, 'gfx', 'loadingscreens', 'loading_screen_border_small.dds')
if os.path.exists(border_src):
    shutil.copy2(border_src, os.path.join(dst_dir, 'loading_screen_border_small.dds'))
    print('Copied loading_screen_border_small.dds to mod')

records = []

for src_name, out_base in mapping:
    src_path = os.path.join(src_dir, src_name)
    with open(src_path, 'rb') as fp:
        raw_head = fp.read(32)
    fmt = detect_format(raw_head)

    with Image.open(src_path) as img:
        orig_w, orig_h = img.size
        # Stretch / resize to 1920x1440
        large_img = img.resize((1920, 1440), Image.Resampling.LANCZOS)
        large_path = os.path.join(dst_dir, f'{out_base}.dds')
        large_img.convert('RGBA').save(large_path)

        # Create small thumbnail 192x144
        small_img = img.resize((192, 144), Image.Resampling.LANCZOS)
        small_path = os.path.join(dst_dir, f'{out_base}_small.dds')
        small_img.convert('RGBA').save(small_path)

        records.append({
            'source': src_name,
            'detected_format': fmt,
            'orig_size': f'{orig_w}x{orig_h}',
            'dest_large': f'{out_base}.dds',
            'large_size': os.path.getsize(large_path),
            'dest_small': f'{out_base}_small.dds',
            'small_size': os.path.getsize(small_path)
        })
        print(f'Converted {src_name} ({fmt}, {orig_w}x{orig_h}) -> {out_base}.dds (1920x1440) & {out_base}_small.dds (192x144)')

# Create aliases for direct name matching
shutil.copy2(os.path.join(dst_dir, 'load_main_menu.dds'), os.path.join(dst_dir, 'main_menu.dds'))
shutil.copy2(os.path.join(dst_dir, 'load_main_menu_small.dds'), os.path.join(dst_dir, 'main_menu_small.dds'))

shutil.copy2(os.path.join(dst_dir, 'load_1.dds'), os.path.join(dst_dir, 'loading.dds'))
shutil.copy2(os.path.join(dst_dir, 'load_1_small.dds'), os.path.join(dst_dir, 'loading_small.dds'))

shutil.copy2(os.path.join(dst_dir, 'load_10.dds'), os.path.join(dst_dir, 'bonus.dds'))
shutil.copy2(os.path.join(dst_dir, 'load_10_small.dds'), os.path.join(dst_dir, 'bonus_small.dds'))

print(f'\nTotal converted images: {len(records)}')

