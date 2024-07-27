def first():
    print("First is called")
    return second() + 30 #60

def second():
    print("Second is called")
    return third() + 20 #30

def third():
    print("Third is called")
    return 10
    
x = first() #60

print("x is ", x)