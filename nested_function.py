def outer_func():
    print("Outer Function")
    i = 1
    
    def inner():
        print("Inner Function", i) #inner function can access outer function var
    inner()

outer_func()