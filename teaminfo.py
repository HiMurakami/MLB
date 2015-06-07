import urllib2
import datetime

from xlwt import Workbook

team = ["Arizona","Atlanta","Baltimore","Boston","Chi Cubs",
		"Chi White Sox","Cincinnati","Cleveland","Colorado","Detroit",
		"Houston","Kansas City","LA Angels","LA Dodgers","Miami",
		"Milwaukee","Minnesota","NY Mets","NY Yankees","Oakland",
		"Philadelphia","Pittsburgh","San Diego","Seattle","San Francisco",
		"St. Louis","Tampa Bay","Texas","Toronto","Washington",]		

TEAM = ["TOR","BOS","NYY","BAL","TBR",	# 0, 1, 2, 3. 4
		"DET","CHW","KCR","CLE","MIN",	# 5, 6, 7, 8, 9
		"SEA","OAK","LAA","TEX","HOU",	#10,11,12,13,14
		"WSN","NYM","ATL","MIA","PHI",	#15,16,17,18,19
		"STL","CHC","PIT","CIN","MIL",	#20,21,22,23,24
		"LAD","SFG","SDP","ARI","COL"]	#25,26,27,28,29

url = 'http://www.baseball-reference.com/leagues/MLB/2015-standard-batting.shtml'
fp = urllib2.urlopen(url)
html = fp.read()
fp.close()
a = html.split('<tr  class=\"\">')
for i in range(1,31): 
	b = a[i].splitlines()
	print b[4][len('   <td align="right" >'):len('   <td align="right" >')+4]	