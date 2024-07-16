my_list = [1,2,3,4]

for i in my_list:
    print("Item ", i)
    if i==3:
        break #if no break, else is also invoked
else:
    print("for complete normally")
print("end of loop")