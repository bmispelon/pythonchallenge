# http://www.pythonchallenge.com/pc/def/ocr.html
# Find letters in a message.
from __future__ import print_function

if __name__ == '__main__':
    import fileinput
    
    for line in fileinput.input():
        letters = [c for c in line if c.isalpha()]
        if letters:
            print(''.join(letters), end='')
    print()
