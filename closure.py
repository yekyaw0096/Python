def counter():
    print("Counter function ")

    i = 1
    def next():
        nonlocal i # This var is from outer function
        i = i + 1
        print("Inner Function ", i)
        return i
    return next #reuse the inner function even though the outer function is called.

next_func = counter()
print("Next ",next_func())
print("Next ",next_func())
