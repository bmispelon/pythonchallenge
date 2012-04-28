# http://www.pythonchallenge.com/pc/return/bull.html
# Calculate the length of the 30th element of the following sequence:
# 1, 11, 21, 1211, 111221, ...
from itertools import groupby

def next_step(s):
    """Return the next element in the sequence."""
    return ''.join('%s%s' % (len(list(g)), k) for k, g in groupby(s))

def gen_sequence(start='1'):
    """Generate the sequence 1, 11, 21, 1211, ..."""
    s = start
    while True:
        yield s
        s = next_step(s)

if __name__ == '__main__':
    _, item = zip(range(31), gen_sequence())[-1]
    print len(item)
