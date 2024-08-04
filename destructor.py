class MyClass:
    def __init__(self):
        self.list = [x for x in range(1000)]
    
    def __del__(self):
        print("Destructor called ")
        self.list = None #memory is reclaimed from list memory usage
        
a = MyClass()
del a