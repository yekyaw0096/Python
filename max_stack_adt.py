#st(lst,max_length)
def push(st, ele):
    if(len(st[0])<st[1]):
        st[0].append(ele)
    else:
        print("Error!")

def pop(st):
    if len(st[0]) > 0:
        return st[0].pop()
    else:
        return None #improve pop and return no error

def is_empty(st):
    return len(st[0]) == 0

max_length = 5
my_stack = []
st = (my_stack,max_length)

push(st,100)
push(st,200)
push(st,300)
push(st,400)
push(st,500)
push(st,600)

while not is_empty(st):
    print("not is_empty Pop ", pop(st))

print("stack ",st)


