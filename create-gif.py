import glob
from PIL import Image

maxW = 0
maxH = 0

DIRECTORY = 'wave-input'

numFiles = len(glob.glob(DIRECTORY + '/*.png'))

for num in range(numFiles - 1):
    im = Image.open(DIRECTORY + '/%05d.png' % (num + 1))
    if im.width > maxW:
        maxW = im.width
    if im.height > maxH:
        maxH = im.height

for num in range(numFiles - 1):
    each_image = Image.new("RGBA", (maxW, maxH))
    im = Image.open(DIRECTORY + '/%05d.png' % (num + 1))
    each_image.paste(im, (0,0))
    each_image.save('gifready/%05d.png' % num)
