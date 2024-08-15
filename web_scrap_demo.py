import re, urllib

import urllib.request

web_url = "http://www.google.com"

u = urllib.request.urlopen(web_url) #open url and scrap the element, source code

text = str(u.read()) # byte to string convert

print("Text ", text)

title = re.findall("<title>\.*</title>", text) #\. = ကြိုက်တာလာ
print("Title ", title)