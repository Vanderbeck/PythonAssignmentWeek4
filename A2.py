#Import Libraries
import urllib
from BeautifulSoup import *

#Set execution parameters
new_url = raw_input('Enter URL: ') #'http://python-data.dr-chuck.net/known_by_Fikret.html' #Starting URL
target_count = int(raw_input('Enter Target Count: '))
target_pos = int(raw_input('Enter Target Position: '))

#setup Loop vars
iters = 0
#Loop through web pages.
while(iters<target_count):
    html = urllib.urlopen(new_url).read()
    soup = BeautifulSoup(html)

    print 'Retrieving:', new_url

    tags = soup('a')
    position = int(0)

    #Loop through links in web page
    for tag in tags:
        new_url = tag.get('href', None)
        if new_url == None: #Make use the link goes somewhere
            continue
        else:
            position = position +1 #Keep track of the link position

        #If its the target link position, take the name and return to while loop
        if position == target_pos:
            name = tag.contents[0]
            iters = iters+1
            break


    print 'Name No.', target_pos, ': ', name, '\n'


# html = urllib.urlopen(new_url).read()
# soup = BeautifulSoup(html)
# tags = soup('a')
# count = int(0)
#
# for tag in tags:
#     count = count+1
#     print count
#     print 'TAG:',tag
#     print 'URL:',tag.get('href', None)
#     print 'Contents:',tag.contents[0]
#     print 'Attrs:',tag.attrs
