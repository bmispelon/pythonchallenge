# http://www.pythonchallenge.com/pc/def/map.html
# Translate a string using a simple letter-shifting cypher.

from string import ascii_lowercase, maketrans

def get_shifted_trans_table(n, alphabet):
    """Return a translation table (suitable for use in str.replace) where all
    the letters of the given alphabet have been shifted by n.
    
    """
    n = n % len(alphabet) # handles negative numbers
    
    shifted = alphabet[n:] + alphabet[:n]
    return maketrans(alphabet, shifted)


if __name__ == '__main__':
    import fileinput
    
    table = get_shifted_trans_table(+2, ascii_lowercase)
    
    for line in fileinput.input():
        print line.translate(table)
