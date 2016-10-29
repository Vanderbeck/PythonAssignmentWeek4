#Import Libraries
import urllib
from BeautifulSoup import *

#Set execution parameters
new_url = 'http://python-data.dr-chuck.net/known_by_Fikret.html' #Starting URL
target_count = 4
target_pos = 3

#setup Loop vars
iters = 0
while(iters<target_count):
    html = urllib.urlopen(new_url).read()
    soup = BeautifulSoup(html)

    print 'Retrieving:', new_url

    tags = soup('a')
    position = int(1)

    for tag in tags:
        new_url = tag.get('href', None)
        if new_url == None:
            continue
        else:
            position = position +1

        if position == target_pos:
            name = tag.contents[0]
            iters = iters+1
            break


    print 'Name No.', target_pos, ': ', name, '\n'
