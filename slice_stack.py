str = "Hello from python"
print("str[1:3] ", str[1:3])
print("str[1:] ", str[1:])
print("str[:5] ", str[:5])
print("str[0::2] ", str[0::2])
print("str[:]", str[:])
print("str[:] == str", str[:] is str)
print("str[::-1] ", str[::-1])

print("Length ", len(str))
print("'Hello' in ", 'Hello' in str)#return true/false
print("'Hello' in ", 'hello' in str)#case sensitive