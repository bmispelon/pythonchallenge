# http://www.pythonchallenge.com/pc/def/equality.html
# Find all lowercase letters that are surrounded by exactly three upper-cased ones.
# We assume that there is only one such letter per line.

from __future__ import print_function
import re

criteria = re.compile('[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]')

if __name__ == '__main__':
    import fileinput
    
    for line in fileinput.input():
        match = criteria.search(line)
        
        if match:
            print(match.group(1), end='')
    print()
