import re

m = re.search("([a-z]*)\.py", "hello.py")
print(m.groups())

m = re.search("(http|https)://(www\.\w+\.(com|org|gov))", "http://www.google.com")
print("m ",m)
print("m groups ", m.groups()[1])