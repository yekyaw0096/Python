class A:
    def __init__(self):
        print("Constructor ")
    
    def methodA(self):
        print("Method A in class A")

class B:
    def __init__(self):
        print("Constructor ")
    
    def methodB(self):
        print("Method B")
        
    def methodA(self):
        print("Method A in Class B")    

class C(A,B):
    def __init__(self):
        super().__init__()
        B.__init__(self)
        print("Constructor C")
    
    def methodC(self):
        B.methodA(self)
        super().methodB()
        
    def methodA(self):
        print(" C's method A ")

c = C()
c.methodC()
c.methodA()
print("C MRO - method resolution order ", C.mro())
    