def min_max(a,b):
    if a < b:
        return a,b
    else:
        return b,a

min, max = min_max(10,20)
print("Min ", min, "Max ", max )
#return tuple