import urllib
import re
from BeautifulSoup import *

html = urllib.urlopen('http://python-data.dr-chuck.net/comments_42.html').read()
soup = BeautifulSoup(html)

ClassComments = soup('span')
R = re.compile('comments.+')

for line in ClassComments:
    line = str(line)
    nums = R.findall(line)

print nums
