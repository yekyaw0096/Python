class Stack:
    def __init__(self, max_length): #self = this
        self.lst = []
        self.max_length = max_length
        print("Constructor run ",max_length)
    
    def push(self, ele):
        if( len(self.lst) < self.max_length):
            self.lst.append(ele)
        else:
            print("Error")
    
    def is_empty(self):
        return len(self.lst) == 0
    
    def pop(self):
        if not self.is_empty:
            return self.lst.pop()
        else:
            return None
    
s1 = Stack(5) #call class will make self constructor method run
s1.push(100)
s1.push(200)
s1.push(300)
s1.push(400)
s1.push(500)
s1.push(600)

while not s1.is_empty:
    print("Pop until s1 is empty ", s1.pop())
    
s2 = stack(4)
s2.push(1000)