
import urllib2, cookielib

cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
opener.addheaders=[('User-Agent', "Mozilla/5. (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11"),('Accept-Language','ja,en-us;q=0.7,en;q=0.3')]
urllib2.install_opener(opener)
