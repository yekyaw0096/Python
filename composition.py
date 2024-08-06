class Engine:
    def __init__(self):
        print("Engine constructor")
    
    def start(self):
        print("Engine starts")

class Car:
    def __init__(self):
        self.engine = Engine() #composition
    
    def start(self):
        print("Car start")
        self.engine.start()
        
car = Car()
car.start()