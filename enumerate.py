my_list = [10,20,30,40]

for i in my_list:
    print("I is ", i)
    i *= 2

#enumerate loop for both index and value
for index, value in enumerate(my_list):
    print("Index ", index, " value ", value)
    my_list[index] *= 2

print("My list ", my_list)