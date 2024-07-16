my_list = [10,20,30,40,50]

user_input = int(input("Enter a number to find in the list! "))
found = False
index = 0

while not found and index < len(my_list):
    if my_list[index] == user_input:
        print("Found at index ", index)
        found = True
    else:
        index += 1
            
print("End of while")