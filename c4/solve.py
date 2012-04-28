# http://www.pythonchallenge.com/pc/def/linkedlist.php
# Follow a chain of URLs of the form linkedlist.php?nothing=foo, where each URL gives the value of the next `foo`
import re
import urllib

def fetch_url(url):
    """Return the content located at the given URL."""
    handle = urllib.urlopen(url)
    content = handle.read()
    handle.close()
    return content

def get_content(nothing):
    """Retrieve the content for the page corresponding to the given `nothing` parameter."""
    url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s' % nothing
    
    return fetch_url(url)

def find_nothing(text):
    """Try to find a `nothing` parameter in the given text.
    Return None if not found."""
    match = re.search('nothing\D+(\d+)', text)
    if match is None:
        return None
    return match.group(1)


if __name__ == '__main__':
    # nothing = 12345 # the original starting parameter
    
    # when you reach 16044, you get a message telling you to divide by 2
    nothing = 16044 / 2
    MAX_ATTEMPTS = 400
    
    for _ in range(MAX_ATTEMPTS):
        print nothing
        text = get_content(nothing)
        nothing = find_nothing(text)
        
        if nothing is None:
            print text
            break
