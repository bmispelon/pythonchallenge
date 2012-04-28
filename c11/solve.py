# http://www.pythonchallenge.com/pc/return/5808.html
# The trick for this one is to extract every other pixel on the cave.jpg image.
# When zoomed in, the image looks like that:
# 0_0_0...
# _0_0_...
# 0_0_0...
# ........
# Extracting only the "0" pixels yields an image containing the solution.
import Image

def range2d(x, y):
    """Generate 2D coordinate tuples."""
    for i in range(x):
        for j in range(y):
            yield i, j

def skip_pixels(im):
    """Skip every other pixel in the given image."""
    coords = range2d(*reversed(im.size))
    pixels = im.getdata()
    for (y, x), pixel in zip(coords, pixels):
        if x % 2 == y % 2:
            yield pixel

if __name__ == '__main__':
    im = Image.open('cave.jpg')
    halfwidth = (im.size[0] / 2, im.size[1])
    out = Image.new(im.mode, halfwidth)
    
    pixels = skip_pixels(im)
    out.putdata(list(pixels))
    out.show()
