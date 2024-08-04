class Parent:
    def __init__(self):
        print("This is Parent Constructor")
        
    def external_method(self):
        print("External method")
        
    class Inner:
        def __init__(self):
            print("Inner Class Constructor")
            
        def internal_method(self):
            print("This is internal method")
    
external = Parent() #construct object
external.external_method()
internal = external.Inner()
internal.internal_method() #internal method can only construct via external object