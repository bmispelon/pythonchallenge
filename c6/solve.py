# http://www.pythonchallenge.com/pc/def/channel.html
# There is a zip file located at channel.zip
# The zip archive contains a bunch of text files, linked like in problem 4, 
# along with a readme file.
# When you unroll the list, you get to a file that tells you to "join the comments".
# Each file in the archive has a comment. Joining the comments in the order in
# which the list unrolls produces an ascii-art of the solution (sort-of)
from __future__ import print_function
import re
import zipfile

if __name__ == '__main__':
    
    with zipfile.ZipFile('channel.zip') as z:
        nothing = 90052 # given in readme
        rxp = re.compile('\d+')
        
        while True:
            name = '%s.txt' % nothing
            
            text = z.open(name).read()
            info = z.getinfo(name)
            
            match = rxp.search(text)
            if match is None: # We reached the end of the "linked list"
                break 
            else:
                nothing = match.group(0)
                print(info.comment, end='')
        
        print()

