my_tuple = ()
print("Empty tuple ",my_tuple)

my_tuple = 2, # , at the end to determine as tuple or it will be integer
print("Single tuple ",my_tuple)

two_tuple = 2,"Hello" #no need , if there is two elements for tuple
print("Two tuple ",two_tuple)

lst = [1,"Two",3]
three_tuple = tuple(lst)
print("Tuple constructor ",three_tuple) 

one_to_ten = range(1,21,2)
four_tuple = tuple(one_to_ten)
print("Tuple constructor from range ",four_tuple)

print("Tuple [1] ", four_tuple[1])
print("Tuple [1:5] ", four_tuple[1:5]) #index 1 to 5
print("Reversed Tuple [:-1] ", four_tuple[:-1])
print("Last Tuple [-1] ", four_tuple[-1])