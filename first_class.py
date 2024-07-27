def get_another():
    return hello

def invoke(func):
    print("Invoke function is called ")
    func()

def hello():
    print ("Hello function is called ")

x = hello

x() #it becomes hello() function #Rule 1
invoke(hello) #Rule 2

print("Invoked get another function")
get_another()()

#to be first class variable
#Rule 1: can b stored in variable
#Rule 2: can be passed as parameter
#Rule 3: can be returned from function