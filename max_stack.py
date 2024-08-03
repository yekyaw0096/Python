def push(lst, max, ele):
    if(len(lst)<max):
        lst.append(ele)
    else:
        print("greater than max!")

def pop(lst):
    if len(lst) > 0:
        return lst.pop()
    else:
        return None #improve pop and return no error

def is_empty(lst):
    return len(lst) == 0

max_length = 5
my_stack = []
push(my_stack,max_length,100)
push(my_stack,max_length,200)
push(my_stack,max_length,300)
push(my_stack,max_length,400)
push(my_stack,max_length,500)
push(my_stack,max_length,600)

while not is_empty(my_stack):
    print("not is_empty Pop ", pop(my_stack))

print("stack ",my_stack)


