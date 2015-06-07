import urllib2
import datetime
from xlwt import Workbook

###int###
today = datetime.datetime.now() - datetime.timedelta(hours=4)
yy = today.year
mm = str(today.month)
dd = str(today.day)
if today.day < 10:
	mm = '0'+str(today.month)
	dd = '0'+str(today.day)

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
b3 = {}
wb = Workbook()
ws = wb.add_sheet( "Detector"+str(yy)+str(mm)+str(dd) ) 

ws.write(0,1,'win')
ws.write(0,2,'pitcher')
ws.write(0,3,'win')
ws.write(0,4,'loss')
ws.write(0,5,'SP')
ws.write(0,6,'RP1')
ws.write(0,7,'RP2')
ws.write(0,8,'RP3')
ws.write(0,9,'CL')
ws.write(0,10,'R/G')
ws.write(0,11,'ERA*R/G')
ws.write(0,12,'differ')

url = 'http://gd2.mlb.com/components/game/mlb/year_2015/month_'+mm+'/day_'+dd+'/epg.xml'
fp = urllib2.urlopen(url)
html = fp.read()
fp.close()
a = html.split('venue=')
url = 'http://gd2.mlb.com/components/game/mlb/year_2015/month_'+mm+'/day_'+dd+'/scoreboard.xml'
fp = urllib2.urlopen(url)
html = fp.read()
fp.close()
a1= html.split('<sg_game>')

url = 'http://www.baseball-reference.com/leagues/MLB/2015-standard-batting.shtml'
fp = urllib2.urlopen(url)
html = fp.read()
fp.close()
a2 = html.split('<tr  class=\"\">')

url = 'http://www.baseball-reference.com/teams/NYY/2015.shtml'
fp = urllib2.urlopen(url)
html = fp.read()
fp.close()
a3 = html.split('<strong>RP</strong></td>')

for i in range(1,31): 
	b2 = a2[i].splitlines()
	b2 = b2[4][len('   <td align="right" >'):len('   <td align="right" >')+4]
	b3[i-1] = float(b2)

for i in range(1,len(a)):
	b  =  a[i].splitlines()
	b1 =  a1[i].splitlines()

	teamwin1 = b[59][17:25].replace(' ','').replace('=','').replace('\"','')
	teamwin2 = b[61][17:25].replace(' ','').replace('=','').replace('\"','')
	
	pname1   = b1[14][27:40].replace('\"','')
	pwin1    = b1[13][34:37].replace('\"','')
	t = 44+len(pwin1)
	ploss1   = b1[13][ t :t+3].replace('\"','').replace(' ','')
	t = 52 +len(ploss1)
	pera1    = b1[13][ t :t+6].replace('\"','').replace('-','0')
	
	
	pname2   = b1[11][27:40].replace('\"','')
	pwin2    = b1[10][34:37].replace('\"','')
	t = 44+len(pwin2)
	ploss2   = b1[10][ t :t+3].replace('\"','')
	t = 52 +len(ploss2)
	pera2    = b1[10][ t :t+5].replace('\"','').replace('-','0')
	
	tmp1 = b[34][24:len(b)].replace('\"','')+','+teamwin1+','+pname1+","+pwin1+','+ploss1+","+pera1
	tmp2 = b[42][24:len(b)].replace('\"','')+','+teamwin2+','+pname2+','+pwin2+','+ploss2+','+pera2
	tmp1 = tmp1.replace('<','').replace('>','').replace('/','')
	tmp2 = tmp2.replace('<','').replace('>','').replace('/','')
	print tmp1
	print tmp2
	ok1 = tmp1.split(',')
	ok2 = tmp2.split(',')
	
	ok1[1] = int(ok1[1])
	ok1[3] = int(ok1[3])
	ok1[4] = int(ok1[4])
	ok1[5] = float(ok1[5])
	ok2[1] = int(ok2[1])
	ok2[3] = int(ok2[3])
	ok2[4] = int(ok2[4])
	ok2[5] = float(ok2[5])

	
	for j in range(0,len(ok1)):
		ws.write((i-1)*3+1,j,ok1[j])
		ws.write((i-1)*3+2,j,ok2[j])
	for k in range(0,30):
		if ok1[0] == team[k]:
			ws.write((i-1)*3+1,10,b3[k]) #R/G
			ws.write((i-1)*3+1,11,ok2[5]*b3[k]) #ERA*R/G
			k1 = ok2[5]*b3[k]
			
			url = 'http://www.baseball-reference.com/teams/'+tm[k]+'/2015.shtml'
			fp = urllib2.urlopen(url)
			html = fp.read()
			fp.close()
			a3 = html.split('<strong>CL</strong></td>')
			cl = a3[1].splitlines()
			a4 = html.split('<strong>RP</strong></td>')
			rp1 = a4[1].splitlines()
			rp2 = a4[2].splitlines()
			rp3 = a4[3].splitlines()

			cl[0] = float(cl[6][cl[6].find('ERA')+7:cl[6].find('ERA')+11])
			rp1[0]= float(rp1[6][rp1[6].find('ERA')+7:rp1[6].find('ERA')+11])
			rp2[0]= float(rp2[6][rp2[6].find('ERA')+7:rp2[6].find('ERA')+11])
			rp3[0]= float(rp3[6][rp3[6].find('ERA')+7:rp3[6].find('ERA')+11])
			
			ws.write((i-1)*3+1,6,rp1[0])
			ws.write((i-1)*3+1,7,rp2[0])
			ws.write((i-1)*3+1,8,rp3[0])
			ws.write((i-1)*3+1,9,cl[0])
			
		if ok2[0] == team[k]:
			ws.write((i-1)*3+2,10,b3[k]) #R/G
			ws.write((i-1)*3+2,11,ok1[5]*b3[k])#ERA*R/G
			k2 = ok1[5]*b3[k]
			
			url = 'http://www.baseball-reference.com/teams/'+tm[k]+'/2015.shtml'
			fp = urllib2.urlopen(url)
			html = fp.read()
			fp.close()
			a3 = html.split('<strong>CL</strong></td>')
			cl = a3[1].splitlines()
			a4 = html.split('<strong>RP</strong></td>')
			rp1 = a4[1].splitlines()
			rp2 = a4[2].splitlines()
			rp3 = a4[3].splitlines()

			cl[1] = float(cl[6][cl[6].find('ERA')+7:cl[6].find('ERA')+11])
			rp1[1]= float(rp1[6][rp1[6].find('ERA')+7:rp1[6].find('ERA')+11])
			rp2[1]= float(rp2[6][rp2[6].find('ERA')+7:rp2[6].find('ERA')+11])
			rp3[1]= float(rp3[6][rp3[6].find('ERA')+7:rp3[6].find('ERA')+11])
			
			ws.write((i-1)*3+2,6,rp1[1])
			ws.write((i-1)*3+2,7,rp2[1])
			ws.write((i-1)*3+2,8,rp3[1])
			ws.write((i-1)*3+2,9,cl[1])
			

	if k1>k2 :
		ws.write((i-1)*3+1,12,k1-k2) #differ
		if k1-k2 >10 :
			if ok1[5]!=0 and ok2[5]!=0: 
				ws.write((i-1)*3+1,13,'!!!')
	else:
		ws.write((i-1)*3+2,12,k2-k1) #differ
		if k2-k1 >10 :
			if ok1[5]!=0 and ok2[5]!=0: 
				ws.write((i-1)*3+2,13,'!!!')
	
	print ''
wb.save( "test.xls" )