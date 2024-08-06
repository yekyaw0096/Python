class Parent:
    var_one = "var one of Parent"
    
    def __init__(self):
        print("Parent constructor")
        self.var_two = "instance of Parent" #cannot access instance variable

    def instance_method(self):
        print("Parent instance method")

    @classmethod
    def class_method(cls):
        print("Parent class method ")
    
    @staticmethod
    def static_method():
        print("Parent Static method")

class Child(Parent):
    
    def __init__(self):
        super().__init__() #to call from super constructor
        print("Child constructor")

    def method(self):
        print("Super var_one ", super().var_one)
        #print("Super var two ", super().var_two) ****Only instance variable from parent is not accessible
        super().class_method()
        super().static_method()

    @classmethod
    def child_class_method(cls):
        #super().instance_method()
        pass
    
    @staticmethod
    def child_static_method():
        #super(Child,Child).instance_method()
        super(Child,Child).class_method()

c = Child()
c.method()
c.child_class_method()
c.child_static_method

#child class method cannot call super instance method
#static method cannot call instance method
#super(Child,Child).class_method() can be called