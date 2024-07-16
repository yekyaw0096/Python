lst = [10,203,403]

for i in lst:
    print("Item : ", i)
    
for index,value in enumerate(lst):
    lst[index] *= 2
print("Double list ", lst)

new_list = []
int_list = list(range(0,30))
for i in int_list:
    if i%5==0:
        new_list.append(i)
print("list divided by 5 ", new_list)

list2 = list(range(0,5))
print("Sum ",sum(list2))

list2.insert(1,300)#1 is index
print("list 2 ",list2)

list2.insert(-1,367)#1 is index
print("list 2 ",list2)