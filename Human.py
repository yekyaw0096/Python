class Human:
    planet = "Earth" #static variable
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def display(self):
        print("Name ", self.name, " Age ", self.age, " Planet ", self.planet) #planet can also use with self but better use with class name.

    @classmethod
    def class_method(cls):
        print("This is class method ",cls.planet)

    @staticmethod
    def static_method():
        print("Normal method ", Human.planet)
    
h1 = Human("CC", 27)
h1.school = "UCSY" #dynamically add new instance variable
# *** bad practice for encapsulation principle ***
del h1.school
print("h1 ", h1.__dict__) #bad practice in production code
Human.planet = "Mars"
h1.display()

h2 = Human("Mg Mg ", 18)
h2.display() #separated copy from h1

h1.class_method()
Human.static_method() #good practice
h1.static_method() #bad practice