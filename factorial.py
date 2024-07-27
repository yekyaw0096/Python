def fact(n):
    if n == 1: # 1 - base case and 2 - parameter must included
        return 1
    else:
        return n * fact(n-1)
    #recursive call ( 3 - call it's own function but need to modify)
    #recursive need stack call and only can handle to 1000
print("3 ! => ", fact(3))

def imp_fact(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    return fact

print("Fact 998 ", imp_fact(998))