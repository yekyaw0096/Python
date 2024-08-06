class Money:
    def __init__(self,value):
        self.value = value
    
    def __radd__(self,other): #reverse adding
        print("rAdd method called")
        return Money(self.value + other)
        
    def __add__(self,other):
        print("Add method called")
        return Money(self.value + other.value)
    
    def __iadd__(self,other): #iadd is compound assignment/ add value to self value
        print("iAdd method called")
        return Money(self.value + other.value)
    
    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self, other):
        return self.value < other.value
    
    def __repr__(self):
        return "(Money {})".format(self.value)

    def __str__(self):
        print("Called str ")
        return"(Money {})".format(self.value)

m1 = Money(10)
m2 = Money(20)
m3 = m1 + m2 + Money(50)
#m1 is self and m2 is other/ m3 is operator overloading of +
print("M3 is ", m3.value)
print("M3 ",m3 == Money(80))
print("M3 < 100 ", m3 < Money(100))

m3 += Money(10)
print("M3 of iadd is ", m3.value)

print("M3 Object is ", m3)

print("M3 ", str(m3) + " is ")

print("M4 ", 20 + Money(20))