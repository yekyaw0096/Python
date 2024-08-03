def stack(max_length):
    lst = []
    
    def push(ele):
        #print("push ")
        if(len(lst) < max_length):
            lst.append(ele)
    
    def pop():
        #print("Pop ")
        if not is_empty():
            return lst.pop()
        else:
            return None
        
    def is_empty():
        #print("is empty ")
        return len(lst) == 0
        
    return (push,pop,is_empty)

push,pop,is_empty = stack(5)
push(10)
push(20)
push(30)
push(40)
push(50)
push(60)

print("Pop ",pop())
print("Pop ",pop())
print("Pop ",pop())
print("Pop ",pop())
print("Pop ",pop())
print("Pop ",pop())
