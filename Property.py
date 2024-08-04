class Student:
    def __init__(self,name,age):
        self._name = name #_var is used as a flag for private to others developers
        self._age = age
    
    @property
    def age(self):
        print("getter is run")
        return self._age
    
    @age.setter
    def age(self, age):
        print("setter is run")
        if 0 > age > 100:
            self._age = age
    
    @age.deleter
    def age(self):
        print("Deleter is run")
        del self._age
    
    def display(self):
        print("Name ", self._name, " Age ", self._age)
        

class School:
    def __init__(self):
        self._student_list = []
    
    def enroll(self, student):
        print("Student ",student._name," have been enrolled")
        self._student_list.append(student)

mgMg = Student("Mg Mg ", 18)
#mgMg.name = "Name change from outside"
mgMg.age = 20 #setter is run
mgMg.display()
print("Read MgMg Age ", mgMg.age)
del mgMg.age

school = School()
school.enroll(mgMg)