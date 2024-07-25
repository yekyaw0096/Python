def list_total(lst=[]): #default return  is []
    print("Lst ", lst)
    return sum(lst)

print("Total ", list_total([1,2,3,4]))
print("Total ", list_total())

def append(lst=[]):
    lst.append(100)
    return lst

my_lst = [1,3,4]
print("List append ", append(my_lst))

print("List Append ", append())
print("List Append ", append()) #default value works only one time, if call multiple times, default values are added more.