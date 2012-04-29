# http://www.pythonchallenge.com/pc/return/disproportional.html
# The page at ../phonebook.php exposes a XML RPC endpoint.
# Calling listMethods() on it yields only one interesting method: phone()
# The solution to this problem in given when calling 'Bert' (case sensitive)
# The fact that Bert is evil is told in the previous problem (evil4.jpg).
import xmlrpclib

PROXY_URL = 'http://www.pythonchallenge.com/pc/phonebook.php'

if __name__ == '__main__':
    proxy = xmlrpclib.ServerProxy(PROXY_URL)
    number = raw_input('Who to call?: ')
    while number:
        print 'Calling "%s" ...' % number
        print proxy.phone(number)
        number = raw_input('Who to call?: ')
