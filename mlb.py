import urllib2
fp = urllib2.urlopen('http://mlb.mlb.com/home')
html = fp.read()
fp.close()
print html
