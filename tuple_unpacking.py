def division(num,divisor):
    if divisor == 0:
        return "Division by zero error", 0
    else:
        return None,num/divisor #able to return 2 values in tuple
print("Division ", division(3,2))

err, result = division(3,0) #return first one in err and second one in result
if (not err):
    print("Result is ", result)
else:
    print("Error ", err)