#!/usr/local/bin/python

import urllib
user = "f1vlad" # specify your foursquare username
output_path = "/var/www/fs.f1vlad.com/etc/%s.4sq.xml" % user # specify output file where location would be written
url = "http://foursquare.com/search?q=%s&x=0&y=0" % user # nothing to touch here

try:
    page = urllib.urlopen(url)
    loc = page.read()
    start=loc.index("div class=\"address\"")+20
    offset = loc[start+20:start+400].index("</div>")+1
    loc=loc[start:start+offset]
except IOerror:
    loc = 'Unknown'

f = open(output_path,'w')
f.write(loc)
# print loc[start:start+offset]

