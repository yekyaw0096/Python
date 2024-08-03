def push(lst, ele):
    print("ele ", ele)
    lst.append(ele)

def pop(lst):
    if len(lst) > 0:
        return lst.pop()
    else:
        return None #improve pop and return no error

def is_empty(lst):
    return len(lst) == 0

my_stack = []
push(my_stack,100)
push(my_stack,200)
push(my_stack,300)

while not is_empty(my_stack):
    print("not is_empty Pop ", pop(my_stack))

print("stack ",my_stack)

print("pop ",pop(my_stack))
print("pop ",pop(my_stack))
print("pop ",pop(my_stack))
print("pop ",pop(my_stack))
print("Is empty ", is_empty(my_stack))