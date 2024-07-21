my_tuple = "Aung Aung", 23
name, age = my_tuple # name = my_tuple[0], age = my_tuple[1]
#tuple is like a parcel to unpack. destructuring*

print("Name ",name, " Age ", age)
name = name.upper()
print("My Tuple ", my_tuple)

my_lst = [1,2,3,4]
another_tuple = (my_lst,1)
another_lst,_ = another_tuple
#another_lst is my_lst

print("Another list ", another_lst)
print("Another list == my_lst", another_lst is my_lst)

def process(*argv): #tuple packing, become as tuple 
    print("Argv ", argv, type(argv))
process(1,2,"Hello")