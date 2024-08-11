print("Start")

try:
    
    a = int(input("Enter a "))
    b = int(input("Enter b "))
    
    print("a/b is",a/b)
    print("After exception line")

except (ZeroDivisionError,ValueError):
    print("Error when division by zero or input value error")

#except ValueError:
#    print("Please enter valid number value")

except: #general error
    print("Error occur but I have no idea what error is it!")

finally: #cleanup code
    print("finally is run whatever try or except")

print("End")