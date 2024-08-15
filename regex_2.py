import re

print("Search ", re.search("[a-z].py", "Hello.py"))
print("Search ", re.search("[a-z]*\.py", "hello.py")) #\ escape a grouping characters

print("Search ", re.search("[a-z]{3,}\.(com|org|gov)", "Hello.gov"))
# | means or 
# {3,} at least 3 to infinity
# # () = grouping

print("Search ", re.search("\w+", "word_character_123")) #Word character
print("Search ", re.search("\W+", "#$%&*!")) #non-word character / Special Characters

print("Search ", re.search("\d{9,11}", "0634132339")) #\d = digit
print("Search ", re.search("\D+", "hello.dd123")) #\D = non-digit

print("Search ", re.search("\s*hello", "how   hello")) #\s = white space, \r \n included
print("Search ", re.search("\S+", "1232432dsfasdf_")) #\S = non white space 

print("Search ", re.search(r"\bworld", "hello world")) #r\b = word boundary

