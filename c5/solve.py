# http://www.pythonchallenge.com/pc/def/peak.html
# Load the pickle file located at banner.p
# Inside the pickle is a list of lists.
# Each element of the outer list represent a line.
# Each element inside the sub-list is a tuple of (char, repeat)
# When printing each character (repeated as indicated in the tuple) for each line.
# One gets an ascii-art of the solution.
import pickle

if __name__ == '__main__':
    with open('banner.p') as f:
        o = pickle.load(f)
    
    print '\n'.join(''.join(n * char for char, n in line) for line in o)


