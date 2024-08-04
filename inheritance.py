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

drHla = Doctor("Hla Cho",40,"Surgical")
drHla.work() #Inheritance from Human class's method
drHla.eat() #Inheritance from Human class's method