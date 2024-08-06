class Engine:
    def __init__(self):
        print("Engine constructor")
    
    def start(self):
        print("Engine starts")

class DieselEngine:
    def __init__(self):
        print("DieselEngine constructor")
    
    def start(self):
        print("DieselEngine starts")


class Car:
    def __init__(self, engine):
        self.engine = engine #composition
    
    def start(self):
        print("Car start")
        self.engine.start()
        
diesel_engine = DieselEngine() #inversion of control (Dependency inversion)
engine = Engine() #construct from outside and easy to call and use
car = Car(diesel_engine)
car.start()