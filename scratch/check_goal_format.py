from PIL import Image

for name in ['focus_BEN_count_what_remains', 'focus_BEN_stepans_distribution_network', 'focus_BEN_inventory_the_armories']:
    im = Image.open(f'gfx/interface/goals/{name}.dds')
    print(name, im.size, im.format, im.mode)
