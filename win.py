import urllib2
fp = urllib2.urlopen('http://mlb.mlb.com/home')
html = fp.read()
fp.close()
 
#TEAM[k][j][i][h]

Aeast = ["Toronto","Boston","NY Yankees","Baltimore","Tampa Bay"]
Acent = ["Detroit","Chi White Sox","Kansas City","Cleveland","Minnesota"]
Awest = ["Seattle","Oakland","LA Angels","Texas","Houston"]
Neast = ["Washington","NY Mets","Atlanta","Miami","Philadelphia"]
Ncent = ["St. Louis","Chi Cubs","Pittsburgh","Cincinnati","Milwaukee"]
Nwest = ["LA Dodgers","San Francisco","San Diego","Arizona","Colorado"]

AL = [Aeast, Acent, Awest]
NL = [Neast, Ncent, Nwest]

TEAM = [AL, NL]

for k in range(2):
 for j in range(3):
  for i in range(5):
   a = TEAM[k][j][i]+"</td>\n<td class=\"td-w\">"
   tmp1 = html[html.find(a) + len(a)]     + html[html.find(a) + len(a) + 1] + html[html.find(a) + len(a) + 2] 
   tmp2 = html[html.find(a) + len(a) +25] + html[html.find(a) + len(a) +26] + html[html.find(a) + len(a) +27]
   print TEAM[k][j][i] + ": ",
   print int(tmp1.replace("<","").replace("t","")),
   print int(tmp2.replace("<","").replace("t",""))

#  TEAM[k][j][i][0] = int(tmp1.replace("<","").replace("t",""))
#  TEAM[k][j][i][1] = int(tmp2.replace("<","").replace("t",""))
