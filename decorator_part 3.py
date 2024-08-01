def counter():
    yield 1
    yield 2
    yield 3
    yield 4

count = counter()
print("count ",type(count))
print(next(count))    #Each return give the yield number+1
print(next(count))    # yield is used by next()
print(next(count)) 
print(next(count)) 

print("Count ",count)

for i in counter():
    print ("I is ", i)