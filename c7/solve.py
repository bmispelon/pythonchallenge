# http://www.pythonchallenge.com/pc/def/oxygen.html
# The image found at oxygen.png contains a gray line.
# The levels of gray are actually ascii and decoding it produces the solution.
import Image

def decode(bytes):
    """Return the string corresponding the the given list of bytes"""
    return ''.join(chr(b) for b in bytes)

if __name__ == '__main__':
    im = Image.open('oxygen.png')
    
    # crop to the gray line to a 1px high image
    im = im.crop((0, 43, 607, 44))
    
    bytes = [t[0] for t in im.getdata()]
    
    message = decode(bytes[::7]) # each gray square is 7px wide (sort-of)
    # The message contains another list of bytes to decode
    
    bytes = [int(s) for s in message[43:-1].split(',')]
    print decode(bytes)
