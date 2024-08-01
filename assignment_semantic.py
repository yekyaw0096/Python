a = 10
b = a # for immutable type, b copy from a *separated entities

a += 1

print("B is ",b)
print("a is ",a)

lst = [100,200]
lst_two = lst #mutable object

lst.append(300)
lst_two.append(400)

print("lst ",lst," id ",id(lst))
print("lst_two ", lst_two," id ",id(lst_two))

lst_two = [400,500] #lst_two become separated object
lst_two.append(100)

print("lst ",lst," id ",id(lst))
print("lst_two ", lst_two," id ",id(lst_two))