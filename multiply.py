my_list = [10,20,30,40]

for i in my_list:
    print ("I is ", i)
    i *= 2
    
for i in range(len(my_list)):
    print("i is ", i)
    print("Item ", my_list[i])
    my_list[i] *= 2

print("My List ", my_list)