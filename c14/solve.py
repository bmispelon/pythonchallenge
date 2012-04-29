# http://www.pythonchallenge.com/pc/return/italy.html
# The input is a 1px high, 10 000px wide image (wire.png).
# As the main image and the title of the page suggest, we need to "wrap" these pixels
# around a 100x100 image. This yields an image of the solution.
import Image
from itertools import chain

def wrap_around(seq, width, height):
    """Wrap the sequence around a matrix of width x height,
    starting in the top left corner, going right and turning right when we
    encounter either the edge of the matrix or a cell that already has a value."""
    x_inc, y_inc = (1, 0)
    x, y = (0, 0)
    matrix = [[None] * width for _ in range(height)]
    
    for item in seq:
        matrix[x][y] = item
        (x, y) = (x + x_inc, y + y_inc)
        
        if not 0 <= x < width or not 0 <= y < height or matrix[x][y] is not None:
            (x, y) = (x - x_inc, y - y_inc)
            x_inc, y_inc = turn_right(x_inc, y_inc)
            (x, y) = (x + x_inc, y + y_inc)
    
    return chain(*matrix)

def turn_right(x_inc, y_inc):
    """
    (1, 0) -> (0, 1)
    (0, 1) -> (-1, 0)
    (-1, 0) -> (0, -1)
    (0, -1) -> (1, 0)
    """
    return -y_inc, x_inc

if __name__ == '__main__':
    im = Image.open('wire.png')
    out = Image.new(im.mode, (100, 100))
    pixels = list(wrap_around(im.getdata(), *out.size))
    out.putdata(pixels)
    out.show()


