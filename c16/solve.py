# http://www.pythonchallenge.com/pc/return/mozart.html
# The image given in this problem contains pink markers (one on each line).
# Shifting each line so that the markers align yields a new image containing
# the solution.
import Image
import itertools

MARKER_PINK = (255, 0, 255)

def splitlines(image):
    """Generate lines of pixels from the given image."""
    width, height = image.size
    pixels = iter(image.getdata())
    for y in range(height):
        line = []
        for _ in range(width):
            line.append(next(pixels))
        yield line

def find_marker(pixels, color=MARKER_PINK, default=None):
    """Locate the marker on a given line of pixels.
    The marker is composed of five contiguous pixels of the same color.
    
    """
    try:
        index = pixels.index(color)
    except ValueError:
        # Marker not found
        return default
        
    if set(pixels[index: index+5]) == {color}:
        return index
    else:
        # Marker found but not contiguously
        return default

def shift_image(im):
    """Generate the shifted lines of the given image
    where each line is shifted so that the markers are all aligned on th left.
    
    """
    for line in splitlines(im):
        marker = find_marker(line) - 1
        yield line[marker:] + line[:marker]

if __name__ == '__main__':
    im = Image.open('mozart.gif').convert('RGB')
    out = Image.new(im.mode, im.size)
    
    adjusted = adjust_image(im)
    
    pixels = itertools.chain.from_iterable(adjusted)
    out.putdata(list(pixels))
    out.show()
