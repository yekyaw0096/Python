def my_sum(*numbers): #variable length argument is *numbers
    print("Numbers ",numbers, "type ", type(numbers))
    return sum(numbers)

print("Sum ",my_sum(1,2))
print("Sum2 ", my_sum(1,2,3,4,5))

number_tuple = 1,2,3,4,5,6,7
print("Sum ", my_sum(*number_tuple)) #* for tuple unpacking