#scenario - 1_____________________
def inc(num):
    print("Inc ",num)
    num += 1

i = 100
inc(i)
inc(i)

print("I is ", i)

#scenario - 2_____________________Only Change

def append(lst):
    lst.append(100)

my_list = []
append(my_list)
append(my_list)

print("My List ",my_list)

#scenario - 3_____________________

def update(lst):
    lst = [200,200]

update(my_list)
print("My List After",my_list)