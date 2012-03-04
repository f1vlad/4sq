#!/usr/local/bin/python

import urllib
user = "f1vlad" # specify your foursquare username
output_path = "/var/www/fs.f1vlad.com/etc/%s.4sq.rss" % user # specify output file where location would be written
url = "http://foursquare.com/search?q=%s&x=0&y=0" % user # nothing to touch here



#print 'test'
#page = urllib.urlopen('http://foursquare.com/search?q=f1vlad&x=0&y=0')
#loc = page.read()
#print loc



try:
    page = urllib.urlopen(url)
    loc = page.read()
    start = loc.index("div class=\"address\"")+20
    offset = loc[start:start+400].index("</div>")
    loc=loc[start:start+offset]
except:
    loc = 'Off the grid'

rss_file = '<rss version="2.0"><channel><title>%s last spotted location</title><link>http://f1vlad.com</link><description></description><language>en-us</language><lastBuildDate></lastBuildDate><item><title>%s</title><link>http://</link><description></description><pp
ubDate></pubDate></item></channel></rss>' % (user,loc)


f = open(output_path,'w')
f.write(rss_file)
# print loc[start:start+offset]