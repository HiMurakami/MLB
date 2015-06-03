import urllib2
import datetime

s =  datetime.datetime.now() 
#url = 'http://www.baseball-reference.com/play-index/st.cgi?date='+ str(s.year) +'-'+ str(s.month) +'-'+ str(s.day-1)
url = 'http://www.baseball-reference.com/play-index/st.cgi?date='+ str(s.year) +'-06-01'
fp = urllib2.urlopen(url)
html = fp.read()
fp.close()

a = html.splitlines()
for i in range(4,30):
	if len(a[i]) == 0:
		i=i
	elif len(a[i]) == 6:
		break
	else:
		winner = a[i][ a[i].find("<strong>") + len("<strong>") ] + a[i][ a[i].find("<strong>") + len("<strong>") + 1] + a[i][ a[i].find("<strong>") + len("<strong>") + 2 ]
		winner = winner.replace("<","")  
		if a[i].find("<strong>") == 0:
			loser = a[i][len(winner) + len("<strong></strong>")+4] + a[i][len(winner) + len("<strong></strong>")+5] + a[i][len(winner) + len("<strong></strong>")+6]   
		else:
			loser = a[i][0] + a[i][1] + a[i][2]
			loser = loser.replace(" ","")
		print winner + "  win"
		print loser  + "  lose"

