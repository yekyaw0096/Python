import re

my_str = "foo123bar"

print("Search by regex ", re.search('[0-9][0-9][0-9]',my_str)) # 0-9 = 0 to 9
print("Search by regex ", re.search('[0-9][0-9][0-9]',"hello434"))
print("Search by regex ", re.search('[0-9][0-9][0-9]',"234"))

print("Search by regex ", re.search('[abc]',"Helloa")) #[] mean or

#335 113 157
print("Search by regex ", re.search('[1357][1357][1357]',"Hello9525"))
print("Search by regex ", re.search('[a-z][1357][1357]',"Hello50157"))
print("Search by regex ", re.search('1...3',"1abc3")) # . means any character is OK

print("Search by regex ", re.search('^Java',"JavaScript")) # ^ start with 
print("Search by regex ", re.search('^Java'," JavaScript")) #Space is not count

print("Search by regex ", re.search('Java$',"Programming in Java")) # $ is end with 
print("Search by regex ", re.search('Java$',"Programming in JavaScript"))

print("Search by regex ", re.search('[a-z]*[1-5]*',"program123")) # * = comes with unlimited amount
print("Search by regex ", re.search('[a-z]*[1-5]*',"123wex")) # assume can be start with 0
print("Search by regex ", re.search('[a-z]*[1-5]*',""))

print("Search by regex ", re.search('[a-z]+[1-5]+',"abc123wex"))
print("Search by regex ", re.search('[a-z]+[1-5]+',"123wex")) #Not match, cannot assume 0
print("Search by regex ", re.search('[a-z]+[1-5]+',"program"))

print("Search by regex ", re.search('[a-z]+[1-5]?',"abc123wex")) #? = optional to be able to include one time

print("Search by regex ", re.search('[0-9]{5}',"12365")) #{} = define included amount
print("Search by regex ", re.search('[0-9]{2,5}',"125")) #{2,5} = minimum 2 and maximum 5
print("Search by regex ", re.search('[0-9]{2,5}',"58oil"))

