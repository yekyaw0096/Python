my_set = {1,2,3,4}
my_set.add(110) #unorder
my_set.update([10,20,40,50], range(7))
print("My set ",my_set)

set_clone = my_set.copy()
print("MySet is set_clone ",my_set is set_clone)
print("set_clone ", set_clone) #not same object

element = -10
#if element in set_clone: 
# #if condition to silent ignore the unable to remove
    #set_clone.remove(element)
#element in set_clone and set_clone.remove(element)
set_clone.discard(60)

set_clone.clear()

#after clear, following loop will not work
while len(set_clone)>0:
    print("Pop ", set_clone.pop())
    
print("Union ",{1,2} | {3,4,1}, " ",{10,20}.union({30,40,1})) #union = |
print("Intersect ", {1,2} & {1,3,5}," ",{10,20}.intersection({30,40,20})) #& = intersection
print("Intersect ", {1,2} - {1,3,5}," ",{10,20}.difference({30,40,20})) # - = difference
print("Symmetric Diff ",{1,2} ^ {1,3,5}," ",{10,20}.symmetric_difference({30,40,20}))