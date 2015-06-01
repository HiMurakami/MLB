import urllib2
import re
fp = urllib2.urlopen('http://mlb.mlb.com/home')
#fp = urllib2.urlopen('http://google.com')
html = fp.read()
fp.close()

colw = "Colorado</td>\n<td class=\"td-w\">"
print "COL:",
#for i in range(30):
print html[html.find(colw) + len(colw)], 
print html[html.find(colw) + len(colw) + 1], 
print ", ", 
print html[html.find(colw) + len(colw) +25], 
print html[html.find(colw) + len(colw) +26] 
