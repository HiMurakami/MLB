import urllib2
import datetime

from xlwt import Workbook

team = ["Toronto","Boston","NY Yankees","Baltimore","Tampa Bay",			# 0, 1, 2, 3. 4
		"Detroit","Chi White Sox","Kansas City","Cleveland","Minnesota",	# 5, 6, 7, 8, 9
		"Seattle","Oakland","LA Angels","Texas","Houston",					#10,11,12,13,14
		"Washington","NY Mets","Atlanta","Miami","Philadelphia",			#15,16,17,18,19
		"St. Louis","Chi Cubs","Pittsburgh","Cincinnati","Milwaukee",		#20,21,22,23,24
		"LA Dodgers","San Francisco","San Diego","Arizona","Colorado"]		#25,26,27,28,29

TEAM = ["TOR","BOS","NYY","BAL","TBR",	# 0, 1, 2, 3. 4
		"DET","CHW","KCR","CLE","MIN",	# 5, 6, 7, 8, 9
		"SEA","OAK","LAA","TEX","HOU",	#10,11,12,13,14
		"WSN","NYM","ATL","MIA","PHI",	#15,16,17,18,19
		"STL","CHC","PIT","CIN","MIL",	#20,21,22,23,24
		"LAD","SFG","SDP","ARI","COL"]	#25,26,27,28,29


wb = Workbook()
ws = wb.add_sheet( "number of win" )
b=1
for i in range(30):
	ws.write( b, 0, team[i] )
	b = b + 2

c=1
for j in range(4,12):
	for i in range(1,32):
		ws.write( 0, c, 0000 + j*100 + i )
		c = c + 1



s =  datetime.datetime.now() 
yy = s.year
mm = s.month
dd = s.day
#for i in range(30):

for p in range(4,12):
	for q in range(1,32):
		mm = p
		dd = q
		winner=""
		loser =""
		url = 'http://www.baseball-reference.com/play-index/st.cgi?date='+ str(yy) +'-'+ str(mm) +'-'+ str(dd)
		#url = 'http://www.baseball-reference.com/play-index/st.cgi?date='+ str(s.year) +'-06-02'
		fp = urllib2.urlopen(url)
		html = fp.read()
		fp.close()
		
		a = html.splitlines()
		for i in range(4,34): #html l4 - l33
			if len(html) == 0:
				break
			if len(a[i]) == 0:
				i=i
			elif len(a[i]) == 6:
				break
			else:
				
				pwinner = winner
				ploser = loser
				winner = a[i][a[i].find("<strong>")+len("<strong>")] + a[i][ a[i].find("<strong>")+len("<strong>")+1] + a[i][ a[i].find("<strong>")+len("<strong>")+2]
				winner = winner.replace("<","")  
				if a[i].find("<strong>") == 0:
					loser = a[i][len(winner) + len("<strong></strong>")+4] + a[i][len(winner) + len("<strong></strong>")+5] + a[i][len(winner) + len("<strong></strong>") + 6]   
				else:
					loser = a[i][0] + a[i][1] + a[i][2]
					loser = loser.replace(" ","")
				tmp=0
				for j in range(30): #number of team
					if winner == pwinner or loser == ploser or winner == ploser :
						tmp = 1
					if winner ==  TEAM[j]:
						print winner+str(tmp)
						ws.write( j*2+1+tmp, (int(mm)-4)*31 + int(dd), "won" )
					elif loser ==  TEAM[j]:
						print "    " + loser+str(tmp)
						ws.write( j*2+1+tmp, (int(mm)-4)*31 + int(dd), "lost" )
					tmp=0

		wb.save( "mlb.xls" )