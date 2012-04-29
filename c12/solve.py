# http://www.pythonchallenge.com/pc/return/evil.html
# The page contains an image: evil1.jpg
# It turns out that 3 other images exist: evil2, evil3, and evil4.
# The second one leads us to a new file: evil2.gfx
# That file seems to be random binary data at first glance,
# but it's actually five different images merged together.
# By taking every fifth byte from offsets 0 to 4, you can extract them.
# Note: the original evil1.jpg image seem to have data encoded in it, but I was unable to decode it.
# It probably contains hints on how to reach and/or decode the evil2.gfx file.

if __name__ == '__main__':
    with open('evil2.gfx', 'rb') as f:
        raw = f.read()
    
    file_extensions = ['jpg', 'png', 'gif', 'png', 'jpg'] # found using the unix `file` command
    for offset, ext in enumerate(file_extensions):
        filename = 'solution_%s.%s' % (offset, ext)
        with open(filename, 'wb') as f:
            f.write(raw[offset::5])
