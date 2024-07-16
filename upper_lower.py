str = "Apple Orange Banana "

new_str = str.upper()
print("Upper ",new_str)

print("Lower ",new_str.lower())

print("Swap str ", str.swapcase())

print("Title ", new_str.title())

print("Capitalized str ", str.capitalize())

print("str.startwith ", str.startswith("Apple"))

print("str.endwith ", str.strip().endswith("Banana")) #space remove to strip 

num_str = input("Enter num ")
while not num_str.isdigit():
    num_str = input("Please enter correct number ")
num = int(num_str)
print(num, " is number")
