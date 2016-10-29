import urllib
from BeautifulSoup import *

html = urllib.urlopen('http://python-data.dr-chuck.net/comments_42.html').read()


print html
