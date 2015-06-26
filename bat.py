
import urllib
import urllib2
import datetime
from xlwt import Workbook
from xlrd import open_workbook

###int###
today = datetime.datetime.now() - datetime.timedelta(hours=4)
yy = today.year
mm = str(today.month)
dd = str(today.day)

if today.month < 10:
	mm = '0'+str(today.month)
if today.day < 10:
	dd = '0'+str(today.day)
	
yesterday = datetime.datetime.now() - datetime.timedelta(hours=4) - datetime.timedelta(days=1)
yy1 = str(yesterday.year)
mm1 = str(yesterday.month)
dd1 = str(yesterday.day)
if yesterday.month < 10:
	mm1 = '0'+str(yesterday.month)
if yesterday.day < 10:
	dd1 = '0'+str(yesterday.day)


yesterday = datetime.datetime.now() - datetime.timedelta(hours=4) - datetime.timedelta(days=2)
yy2 = str(yesterday.year)
mm2 = str(yesterday.month)
dd2 = str(yesterday.day)
if yesterday.month < 10:
	mm2 = '0'+str(yesterday.month)
if yesterday.day < 10:
	dd2 = '0'+str(yesterday.day)


yesterday = datetime.datetime.now() - datetime.timedelta(hours=4) - datetime.timedelta(days=3)
yy3 = str(yesterday.year)
mm3 = str(yesterday.month)
dd3 = str(yesterday.day)
if yesterday.month < 10:
	mm3 = '0'+str(yesterday.month)
if yesterday.day < 10:
	dd3 = '0'+str(yesterday.day)



team = ["Arizona","Atlanta","Baltimore","Boston","Chi Cubs",
		"Chi White Sox","Cincinnati","Cleveland","Colorado","Detroit",
		"Houston","Kansas City","LA Angels","LA Dodgers","Miami",
		"Milwaukee","Minnesota","NY Mets","NY Yankees","Oakland",
		"Philadelphia","Pittsburgh","San Diego","Seattle","San Francisco",
		"St. Louis","Tampa Bay","Texas","Toronto","Washington"]	

tm = [  "ARI","ATL","BAL","BOS","CHC",
		"CHW","CIN","CLE","COL","DET",
		"HOU","KCR","LAA","LAD","MIA",
		"MIL","MIN","NYM","NYY","OAK",
		"PHI","PIT","SDP","SEA","SFG",
		"STL","TBR","TEX","TOR","WSN"]
		
tmf = [  "ARI","ATL","BAL","BOS","CHN",
		"CHA","CIN","CLE","COL","DET",
		"HOU","KCA","ANA","LAN","MIA",
		"MIL","MIN","NYN","NYA","OAK",
		"PHI","PIT","SDN","SEA","SFN",
		"SLN","TBA","TEX","TOR","WAS"]		

b3 = {}
TeamName={}
NAME={}



#################################################################################
#exel file initialized
#################################################################################
workbook = open_workbook('test.xls')
sheet = workbook.sheet_by_index(0)

new_workbook = Workbook()
new_sheet = new_workbook.add_sheet('test')

for i in range(sheet.nrows):
	data = [sheet.cell_value(i, col) for col in range(sheet.ncols)]
	print sheet.cell(i,0).value
	NAME[i] = sheet.cell(i,0).value
	for index, value in enumerate(data):
		new_sheet.write(i, index, value)
		
#book = xlrd.open_workbook('test_book.xls')
#sheet_1 = book.sheet_by_index(0)
#for row in range(sheet_1.nrows):
#	print sheet.cell(i,0).value
 
new_sheet.write(0,10,'R/G')
new_sheet.write(0,11,'AB1')
new_sheet.write(0,12,'H1')
new_sheet.write(0,13,'AB2')
new_sheet.write(0,14,'H2')
new_sheet.write(0,15,'AB3')
new_sheet.write(0,16,'H3')



#################################################################################

for row in range(sheet.nrows):
	TeamName[row] = sheet.cell(row,0).value
#print 'Loading',
	#print TeamName[row]

#################################################################################
url = 'http://www.baseball-reference.com/leagues/MLB/2015-standard-batting.shtml'
fp = urllib2.urlopen(url)
html = fp.read()
fp.close()
a2 = html.split('<tr  class=\"\">')

for i in range(1,31): 
	b2 = a2[i].splitlines()
	b2 = b2[4][len('   <td align="right" >'):len('   <td align="right" >')+4]
	b3[i-1] = float(b2) ###R/G
	
for i in range(1,sheet.nrows+1):
	for j in range(30):
		if TeamName[i-1] == team[j]:
			new_sheet.write(i-1, index+1, b3[j]) ###input R/G

#################################################################################
print yy1+mm1+dd1
url = 'http://gd2.mlb.com/components/game/mlb/year_2015/month_'+mm1+'/day_'+dd1+'/epg.xml'
#url = 'http://gd2.mlb.com/components/game/mlb/year_2015/month_06/day_14/epg.xml'

fp = urllib2.urlopen(url)
html = fp.read()
fp.close()
a = html.split('venue=')

for i in range(1,len(a)):
	b  =  a[i].splitlines()
	tmp1 = b[34][24:len(b)].replace('\"','')
	tmp2 = b[42][24:len(b)].replace('\"','')
	tmp1 = tmp1.replace('<','').replace('>','').replace('/','')
	tmp2 = tmp2.replace('<','').replace('>','').replace('/','')
	ok1 = tmp1.split(',')
	name1 = ok1
	ok2 = tmp2.split(',')
	name2 = ok2
	for j in range(30):
		if ok1[0] == team[j]:
			ok1[0] =tmf[j]
		if ok2[0] == team[j]:
			ok2[0] =tmf[j]
		
	url = 'http://www.baseball-reference.com/boxes/'+ok2[0]+'/'+ ok2[0] +'2015'+ mm1 + dd1 +'0.shtml'
	#url = 'http://www.baseball-reference.com/boxes/'+ok2[0]+'/'+ ok2[0] +'201506140.shtml'


	fp = urllib2.urlopen(url)
	html = fp.read()
	fp.close()
	
	html_split = html.split('<td align=\"left\" >Team Totals</td>')
	#print len(html_split)
	if len(html_split) < 3:
		continue
	bat1 = html_split[1].split('\n')
	bat2 = html_split[2].split('\n')
	ab1 = int(bat1[1][54:56].rstrip('<').rstrip('/'))
	ab2 = int(bat2[1][54:56].rstrip('<').rstrip('/'))
	h1 =  int(bat1[3][22:24].rstrip('<').rstrip('/'))
	h2 =  int(bat2[3][22:24].rstrip('<').rstrip('/'))
	#print ok1[0] +' '+ ab1 +' '+ h1
	#print ok2[0] +' '+ ab2 +' '+ h2
	print name1[0]
	print name2[0]
	
	for j in range(30):
		if name1[0] == tmf[j]:
			name1[0] = team[j]
		if name2[0] == tmf[j]:
			name2[0] = team[j]
	
	for j in range(sheet.nrows):
		if name1[0]==NAME[j]:
			new_sheet.write(j, index+2, ab1)
			new_sheet.write(j, index+3, h1)
		if name2[0]==NAME[j]:
			new_sheet.write(j, index+2, ab2)
			new_sheet.write(j, index+3, h2)
"""	
	for j in range(sheet.nrows/3):
		for k in range(30):
			if name1[0]==tmf[k] or name2[0]==tmf[k] :
				new_workbook.save('output.xls')
				if(TeamName[j*3+1]==team[k] or TeamName[j*3+1]==team[k]):
					new_sheet.write(j*3+1, index+2, ab1)
					new_sheet.write(j*3+1, index+3, h1)
						
				if(TeamName[j*3+2]==team[k] or TeamName[j*3+2]==team[k]):
					new_sheet.write(j*3+2, index+2, ab2)
					new_sheet.write(j*3+2, index+3, h2)
"""
#################################################################################
print '!!!!!!!!!!!!!!!!'
print yy2+mm2+dd2

url = 'http://gd2.mlb.com/components/game/mlb/year_2015/month_'+mm2+'/day_'+dd2+'/epg.xml'
#url = 'http://gd2.mlb.com/components/game/mlb/year_2015/month_06/day_13/epg.xml'

fp = urllib2.urlopen(url)
html = fp.read()
fp.close()
a = html.split('venue=')

for i in range(1,len(a)):
	b  =  a[i].splitlines()
	tmp1 = b[34][24:len(b)].replace('\"','')
	tmp2 = b[42][24:len(b)].replace('\"','')
	tmp1 = tmp1.replace('<','').replace('>','').replace('/','')
	tmp2 = tmp2.replace('<','').replace('>','').replace('/','')
	ok1 = tmp1.split(',')
	name1 = ok1
	ok2 = tmp2.split(',')
	name2 = ok2
	for j in range(30):
		if ok1[0] == team[j]:
			ok1[0] =tmf[j]
		if ok2[0] == team[j]:
			ok2[0] =tmf[j]
	#print ok1[0]
	#print ok2[0]
		
	url = 'http://www.baseball-reference.com/boxes/'+ok2[0]+'/'+ ok2[0] +'2015'+ mm2 + dd2 +'0.shtml'
	#url = 'http://www.baseball-reference.com/boxes/'+ok2[0]+'/'+ ok2[0] +'201506130.shtml'


	fp = urllib2.urlopen(url)
	html = fp.read()
	fp.close()
	
	html_split = html.split('<td align=\"left\" >Team Totals</td>')
	#print len(html_split)
	if len(html_split) < 3:
		continue
	bat1 = html_split[1].split('\n')
	bat2 = html_split[2].split('\n')
	ab1 = int(bat1[1][54:56].rstrip('<').rstrip('/'))
	ab2 = int(bat2[1][54:56].rstrip('<').rstrip('/'))
	h1 =  int(bat1[3][22:24].rstrip('<').rstrip('/'))
	h2 =  int(bat2[3][22:24].rstrip('<').rstrip('/'))
	#print ok1[0] +' '+ ab1 +' '+ h1
	#print ok2[0] +' '+ ab2 +' '+ h2
	print name1[0]
	print name2[0]

	for j in range(30):
		if name1[0] == tmf[j]:
			name1[0] = team[j]
		if name2[0] == tmf[j]:
			name2[0] = team[j]
	
	for j in range(sheet.nrows):
		if name1[0]==NAME[j]:
			new_sheet.write(j, index+4, ab1)
			new_sheet.write(j, index+5, h1)
		if name2[0]==NAME[j]:
			new_sheet.write(j, index+4, ab2)
			new_sheet.write(j, index+5, h2)
"""
	for j in range(sheet.nrows/3):
		for k in range(30):
			if name1[0]==tmf[k] or name2[0]==tmf[k] :
				new_workbook.save('output.xls')
				if(TeamName[j*3+1]==team[k] or TeamName[j*3+1]==team[k]):
					new_sheet.write(j*3+1, index+4, ab1)
					new_sheet.write(j*3+1, index+5, h1)
					#print '!!!!!!!!!!!!!!!!'
						
				if(TeamName[j*3+2]==team[k] or TeamName[j*3+2]==team[k]):
					new_sheet.write(j*3+2, index+4, ab2)
					new_sheet.write(j*3+2, index+5, h2)
					#print '????????????????'
"""
#################################################################################
print '!!!!!!!!!!!!!!!!'
print yy3+mm3+dd3
url = 'http://gd2.mlb.com/components/game/mlb/year_2015/month_'+mm3+'/day_'+dd3+'/epg.xml'
#url = 'http://gd2.mlb.com/components/game/mlb/year_2015/month_06/day_12/epg.xml'

fp = urllib2.urlopen(url)
html = fp.read()
fp.close()
a = html.split('venue=')

for i in range(1,len(a)):
	b  =  a[i].splitlines()
	tmp1 = b[34][24:len(b)].replace('\"','')
	tmp2 = b[42][24:len(b)].replace('\"','')
	tmp1 = tmp1.replace('<','').replace('>','').replace('/','')
	tmp2 = tmp2.replace('<','').replace('>','').replace('/','')
	ok1 = tmp1.split(',')
	name1 = ok1
	ok2 = tmp2.split(',')
	name2 = ok2
	for j in range(30):
		if ok1[0] == team[j]:
			ok1[0] =tmf[j]
		if ok2[0] == team[j]:
			ok2[0] =tmf[j]
	#print ok1[0]
	#print ok2[0]
		
	url = 'http://www.baseball-reference.com/boxes/'+ok2[0]+'/'+ ok2[0] +'2015'+ mm3 + dd3 +'0.shtml'
	#url = 'http://www.baseball-reference.com/boxes/'+ok2[0]+'/'+ ok2[0] +'201506120.shtml'

	fp = urllib2.urlopen(url)
	html = fp.read()
	fp.close()
	
	html_split = html.split('<td align=\"left\" >Team Totals</td>')
	#print len(html_split)
	if len(html_split) < 3:
		continue
	bat1 = html_split[1].split('\n')
	bat2 = html_split[2].split('\n')
	ab1 = int(bat1[1][54:56].rstrip('<').rstrip('/'))
	ab2 = int(bat2[1][54:56].rstrip('<').rstrip('/'))
	h1 =  int(bat1[3][22:24].rstrip('<').rstrip('/'))
	h2 =  int(bat2[3][22:24].rstrip('<').rstrip('/'))
	#print ok1[0] +' '+ ab1 +' '+ h1
	#print ok2[0] +' '+ ab2 +' '+ h2
	print name1[0]
	print name2[0]

	for j in range(30):
		if name1[0] == tmf[j]:
			name1[0] = team[j]
		if name2[0] == tmf[j]:
			name2[0] = team[j]
	
	for j in range(sheet.nrows):
		if name1[0]==NAME[j]:
			new_sheet.write(j, index+6, ab1)
			new_sheet.write(j, index+7, h1)
		if name2[0]==NAME[j]:
			new_sheet.write(j, index+6, ab2)
			new_sheet.write(j, index+7, h2)

"""
	for j in range(sheet.nrows/3):
		for k in range(30):
			if name1[0]==tmf[k] or name2[0]==tmf[k] :
				new_workbook.save('output.xls')
				if(TeamName[j*3+1]==team[k] or TeamName[j*3+1]==team[k]):
					new_sheet.write(j*3+1, index+6, ab1)
					new_sheet.write(j*3+1, index+7, h1)
					#print '!!!!!!!!!!!!!!!!'

				if(TeamName[j*3+2]==team[k] or TeamName[j*3+2]==team[k]):
					new_sheet.write(j*3+2, index+6, ab2)
					new_sheet.write(j*3+2, index+7, h2)
					#print '????????????????'
"""
#################################################################################
new_workbook.save('output.xls')


#################################################################################
#AVG Calculater
workbook = open_workbook('output.xls')
sheet = workbook.sheet_by_index(0)

new_workbook = Workbook()
new_sheet = new_workbook.add_sheet('test')
for i in range(sheet.nrows):
	data = [sheet.cell_value(i, col) for col in range(sheet.ncols)]
	for index, value in enumerate(data):
		new_sheet.write(i, index, value)
new_sheet.write(0,17,'H/AB of 3G')
for row in range(1,sheet.nrows):
	ab1 = sheet.cell(row,index+2).value
	ab2 = sheet.cell(row,index+4).value
	ab3 = sheet.cell(row,index+6).value
	h1 = sheet.cell(row,index+3).value
	h2 = sheet.cell(row,index+5).value
	h3 = sheet.cell(row,index+7).value
	print ab1
	print ab2
	print ab3
	print h1
	print h2
	print h3
	
	if str(sheet.cell(row,index+3).value).replace(".","").isdigit() != True:
		h1 = 0;
		#print '1'
	if str(sheet.cell(row,index+5).value).replace(".","").isdigit() != True:
		h2 = 0;
	if str(sheet.cell(row,index+7).value).replace(".","").isdigit() != True:
		h3 = 0;
	if str(sheet.cell(row,index+2).value).replace(".","").isdigit() != True:
		ab1 = 0;
	if str(sheet.cell(row,index+4).value).replace(".","").isdigit() != True:
		ab2 = 0;
	if str(sheet.cell(row,index+6).value).replace(".","").isdigit() != True:
		ab3 = 0;


	if ab1+ab2+ab3 == 0:
		continue
	avg = float(h1+h2+h3) / float(ab1+ab2+ab3)
	new_sheet.write(row, index+8, avg)

#################################################################################
new_workbook.save('output.xls')



"""

"""

#wb.save( "test.xls" )