#!/usr/local/bin/python

import urllib
user = "f1vlad" # specify your foursquare username
output_path = "/var/www/fs.f1vlad.com/etc/%s.4sq.rss" % user # specify output file where location would be written
url = "http://foursquare.com/search?q=%s&x=0&y=0" % user # nothing to touch here

try:
    page = urllib.urlopen(url)
    loc = page.read()
    start=loc.index("div class=\"address\"")+20
    offset = loc[start+20:start+400].index("</div>")+1
    loc=loc[start:start+offset]
except IOerror:
    loc = 'Unknown'


rss_file = '<rss version="2.0"><channel><title>f1vlad last spotted location</title><link>http://f1vlad.com</link><description></description><language>en-us</language><lastBuildDate>Tue, 12 Apr 2005 14:21:32 EST</lastBuildDate><item><title>%s</title><link>http://</link><description></description><pubDate></pubDate></item></channel></rss>' % loc


f = open(output_path,'w')
f.write(rss_file)
# print loc[start:start+offset]

