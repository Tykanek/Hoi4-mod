from PIL import Image

im = Image.new('RGBA', (100, 88), (255, 0, 0, 255))
im.save('scratch/test_dds.dds', format='DDS')
im2 = Image.open('scratch/test_dds.dds')
print('Saved and opened test DDS successfully:', im2.size, im2.mode)
