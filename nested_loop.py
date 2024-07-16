digit = "012"
char_string = "ABC"
special_char = "#@$"

for d in digit:
    for c in char_string:
        for s in special_char:
            print("Nested Loop Password Generated ", d+c+s)
print("End of the nested loop")