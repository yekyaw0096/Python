str = "Welcome from Python Programming and Welcome"
print("Count Weclome ", str.count("Welcome"))
print("Count Welcome from index one ", str.count("Welcome",1))
print("Count Welcome from index one ", str.find("Welcome",1))

sub_string = "Welcome"
start_index = 0
count = 0
while str.find(sub_string, start_index) != -1:
    start_index = str.find(sub_string,start_index)+1
    count += 1
    
print("Total count ", count)

sub_string = "Welcome"
print("Welcome in str ", sub_string in str)

count = 0
index = 0
while index < len(str):
    another_str = str[index:index+len(sub_string)]
    print("Another sub ",another_str)
    if( sub_string in another_str):
        count += 1
    index = index+1

print("Count ", count)
