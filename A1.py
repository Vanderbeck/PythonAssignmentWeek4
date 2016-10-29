#Import Libraries
import urllib
from BeautifulSoup import *
#Set regular expressions
import re
R = re.compile('[0-9]+')

#Open and interpret a URL
# url_input = raw_input('Enter URL')
url_input = 'http://python-data.dr-chuck.net/comments_42.html'
html = urllib.urlopen(url_input).read()
soup = BeautifulSoup(html)

#Querry BeautifulSoup. return 'span' variables. Sum the numbers.
## FIANL SUBMISSION ###
tags = soup('span')
total = int(0)

for tag in tags:
    num = int(tag.contents[0])
    total = total + num

print total


### THE EXAMPLE ###
# tags = soup('span')
# count = 0
# for tag in tags:
#     # Look at the parts of a tag
#     count = count+1
#     print count
#     print 'TAG:',tag
#     print 'URL:',tag.get('href', None)
#     print 'Contents:',tag.contents[0]
#     print 'Attrs:',tag.attrs

### HOW I DID IT ###
# ClassComments =soup('span')
#
# #Initialize loop variables
# total = int(0)
# CC_str = str(ClassComments)
#
# #Seperate numbers from the lines and add them
# nums_list = R.findall(CC_str)
#
# for nums in nums_list:
#     nums = int(nums)
#     total = total + nums
#
# #Print Result
# print total
