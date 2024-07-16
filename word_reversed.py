str = input("Enter String ")
words = str.split()
result = ""
print("Words ",words)

for word in words:
    print((word[::-1]))
    result = word[::-1] + " " + result
print("Result ",result)