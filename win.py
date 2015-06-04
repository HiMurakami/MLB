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

for p in range(4,12):
	for q in range(1,32):
		mm = p
		dd = q
		url = 'http://www.baseball-reference.com/play-index/st.cgi?date='+ str(yy) +'-'+ str(mm) +'-'+ str(dd)
		#url = 'http://www.baseball-reference.com/play-index/st.cgi?date='+ str(s.year) +'-06-02'
		fp = urllib2.urlopen(url)
		html = fp.read()
		fp.close()
		
		a = html.splitlines()
		for i in range(4,34):
			if len(html) == 0:
				break
			if len(a[i]) == 0:
				i=i
			elif len(a[i]) == 6:
				break
			else:
				winner = a[i][a[i].find("<strong>")+len("<strong>")] + a[i][ a[i].find("<strong>")+len("<strong>")+1] + a[i][ a[i].find("<strong>")+len("<strong>")+2]
				winner = winner.replace("<","")  
				if a[i].find("<strong>") == 0:
					loser = a[i][len(winner) + len("<strong></strong>")+4] + a[i][len(winner) + len("<strong></strong>")+5] + a[i][len(winner) + len("<strong></strong>") + 6]   
				else:
					loser = a[i][0] + a[i][1] + a[i][2]
					loser = loser.replace(" ","")
							
				for i in range(30):
					#team[i] = team[i].replace(" ","")
					#team[i] = team[i].replace(".","")
					if winner ==  TEAM[i]:
						print winner
						ws.write( i*2+1, (int(mm)-4)*31 + int(dd), "won" )
					if loser ==  TEAM[i]:
						print "    " + loser
						ws.write( i*2+1, (int(mm)-4)*31 + int(dd), "lost" )

		wb.save( "mlb.xls" )