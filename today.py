import urllib2
import datetime
from xlwt import Workbook

wb = Workbook()
ws = wb.add_sheet( "Today" )

ws.write(0,1,'win')
ws.write(0,2,'pitcher')
ws.write(0,3,'win')
ws.write(0,4,'loss')
ws.write(0,5,'ERA')

###int###
today = datetime.datetime.now() - datetime.timedelta(hours=4)
yy = today.year
mm = str(today.month)
dd = str(today.day)
if today.day < 10:
	mm = '0'+str(today.month)
	dd = '0'+str(today.day)

url = 'http://gd2.mlb.com/components/game/mlb/year_2015/month_'+mm+'/day_'+dd+'/epg.xml'
fp = urllib2.urlopen(url)
html = fp.read()
fp.close()
url1 = 'http://gd2.mlb.com/components/game/mlb/year_2015/month_'+mm+'/day_'+dd+'/scoreboard.xml'
fp1 = urllib2.urlopen(url1)
html1 = fp1.read()
fp1.close()

a = html.split('venue=')
a1= html1.split('<sg_game>')

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
	pera1    = b1[13][ t :t+6].replace('\"','').replace(' ','')
	
	pname2   = b1[11][27:40].replace('\"','')
	pwin2    = b1[10][34:37].replace('\"','')
	t = 44+len(pwin2)
	ploss2   = b1[10][ t :t+3].replace('\"','')
	t = 52 +len(ploss2)
	pera2    = b1[10][ t :t+5].replace('\"','')
	
	tmp1 = b[34][24:len(b)].replace('\"','')+','+teamwin1+','+pname1+","+pwin1+','+ploss1+","+pera1
	tmp2 = b[42][24:len(b)].replace('\"','')+','+teamwin2+','+pname2+','+pwin2+','+ploss2+','+pera2
	tmp1 = tmp1.replace('<','').replace('>','').replace('/','')
	tmp2 = tmp2.replace('<','').replace('>','').replace('/','')
	print tmp1
	print tmp2
	ok1 = tmp1.split(',')
	ok2 = tmp2.split(',')
	for j in range(0,len(ok1)):
		ws.write((i-1)*3+1,j,ok1[j])
		ws.write((i-1)*3+2,j,ok2[j])
	#print b[59]
	#print len(pwin1)
	print ''
	
p ='123ae'
print p.digits()
wb.save( "test.xls" )