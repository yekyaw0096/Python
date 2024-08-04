import sys
import gc
lst = [100,200,300] #lst is count
lst_2 = lst #lst is count

print("Reference count in stack ", sys.getrefcount(lst)) #lst is count
lst_2 = None
print("Reference count in stack ", sys.getrefcount(lst))

#print("GC ",gc.get_objects())
#print("GC ",gc.garbage)
print("GC ",gc.collect())
