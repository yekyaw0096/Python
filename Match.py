import re

m = re.search("([a-z]*)\.py", "hello.py")
print(m.groups())

m = re.match("(http|https)://(www\.\w+\.(com|org|gov))", "http://www.google.com something") #match is OK with part of m is matched
print("Match start ", m.start() , " Match end ",m.end())

m = re.fullmatch("(http|https)://(www\.\w+\.(com|org|gov))", "http://www.google.com") #fullmatch is matching precisely
print("Match ", m)

lst = m = re.findall("(http|https)://(www\.\w+\.(com|org|gov))", "http://www.google.com something http://www.yahoo.com") #findall the matching more
for item in lst:
    print("Match ",item)
#match list are returned
    
iter = re.finditer("(http|https)://(www\.\w+\.(com|org|gov))", "http://www.google.com something http://www.yahoo.com") #findall the matching more
for item in iter:
    print("Match ",item)    
#match objects are returned

replaced = re.sub("(http|https)://(www\.\w+\.(com|org|gov))", "domain", "http://www.google.com something http://www.yahoo.com") #Replaced with string
print("Replaced ",replaced)    

replaced = re.subn("(http|https)://(www\.\w+\.(com|org|gov))", "domain", "http://www.google.com something http://www.yahoo.com") #return replaced number of times
print("Replaced ",replaced)    

lst_str = re.split("\.", "www.google.com") #split the phrase with space
for s in lst_str:
    print("Lst str ",s)