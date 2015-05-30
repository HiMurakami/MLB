# -*- coding: utf-8 -*-
#import urllib2
#if __name__ == "__main__":
#	url = "http://mlb.mlb.com/home" # GettingURL 

#	htmldata = urllib2.urlopen(url) # Open URL
#	print unicode(htmldata.read(),"utf-8")
#	htmldata.close()


#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import requests
import lxml.html
 
URL = "http://make.bcde.jp/category/1/"
 
#Webページ(HTML)の取得
req = requests.get(URL)
root = lxml.html.fromstring(req.text)
 
#<a href=""></a>によるリンクを抽出する
anchors = root.xpath('//a')
for anchor in anchors:
    print anchor.attrib['href']
 
#h1の中身を抽出する
h1s = root.xpath('//h1')
for h1 in h1s:
    print h1.text
 
#idを指定して、タグに直接囲われたテキストを抽出
content1 = root.get_element_by_id('content1').text
print content1
 
#idを指定して、タグの中のテキストをすべて抽出
content = root.get_element_by_id('content').text_content()
print content