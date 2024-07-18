lst = list(range(1,11))
print("list ",lst)

for item in lst: #item is read-only
    item *= 2
print("List ",lst)

lst_two = []
for item in lst:
    lst_two.append(item*2)
print("List two ", lst_two)

lst_three = [x*2 for x in lst_two] #like looping
print("lst three ",lst_three)