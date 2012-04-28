# http://www.pythonchallenge.com/pc/def/integrity.html
# The source of the page contains a username and a password encoded with gzip2.
import bz2

username = 'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
password = 'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'

if __name__ == '__main__':
    print 'username : %s' % bz2.decompress(username)
    print 'password : %s' % bz2.decompress(password)


