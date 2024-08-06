class Human():
    
    def __init__(self):
        print("Human constructor")
    
    def work(self):
        print("Human work")

    def breath(self):
        print("Human breath")

class Doctor(Human):
    
    def __init__(self):
        print("Doctor constructor")
    
    def work(self): #override as child have different specific function than parent
        super().work() # if additional parent function is needed 
        print("Doctor work")
        
    #Override only happen in inheritance

d = Doctor()
d.work()
d.breath()