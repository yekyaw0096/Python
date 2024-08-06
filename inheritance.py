class Human:

    def __init__(self, name, age):
        print("Human constructor name ", name," Age ", age)
        self.name = name
        self.age = age
    
    def work(self):
        print("Human work", self.name, "work!")
        
    def eat(self):
        print("Human work", self.name, "eat!")    
        
class Doctor(Human): #Inheritance from Human class
    def __init__(self, name, age, medical_field):
        super().__init__(name, age) #Parent constructor
        self.medical_field = medical_field #Self constructor
        print("Doctor constructor")

    def work(self):
        super().work()
        print("Doctor treat patient") # add new functionalities
        
class Robot:
    def __init__(self):
        pass
    
    def work(self):
        print("Robot works")
    
d = Doctor("Hla Cho",40,"Surgical")
d.work() #Inheritance from Human class's method
d.eat() #Inheritance from Human class's method

d = Robot()
d.work()