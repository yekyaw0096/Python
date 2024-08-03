class Human:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def display(self):
        print("Name ", self.name)
        print("Age ", self.age)

h1 = Human("CC", 27)
h1.school = "UCSY" #dynamically add new instance variable
# *** bad practice for encapsulation principle ***
print("h1 ", h1.__dict__)