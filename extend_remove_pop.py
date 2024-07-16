lst_one = [10,20,30]
lst_two = ["Hello", "World"]

lst_one.extend(lst_two)
print("List One ",lst_one)

lst_one.remove("Hello")
print("Remove ",lst_one)

lst_one.pop()
print("Pop ",lst_one)

lst_one.pop(1)
print("Pop with parameter ", lst_one)