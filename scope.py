x = "Hello"

def hello():
    
    y = "Inner y"
    #x = "inner x"
     
    global x #var become to use the global
    x = "Update global var"
    
    print("X inside hello function is ", x)
    print("Y inside hello is ",y)

hello()
print("X outside is ", x)