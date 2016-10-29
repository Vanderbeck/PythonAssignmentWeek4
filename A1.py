#Import Libraries
import urllib
from BeautifulSoup import *
#Set regular expressions
import re
R = re.compile('[0-9]+')

#Open and interpret a URL
html = urllib.urlopen('http://python-data.dr-chuck.net/comments_42.html').read()
soup = BeautifulSoup(html)

#Querry BeautifulSoup. return 'span' variables
ClassComments =soup('span')

#Initialize loop variables
total = int(0)
CC_str = str(ClassComments)

#Seperate numbers from the lines and add them
nums_list = R.findall(CC_str)

for nums in nums_list:
    nums = int(nums)
    total = total + nums

#Print Result
print total
