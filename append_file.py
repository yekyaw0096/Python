file = open("notes.txt", "a") #append mode is a

messages = ["Apple ","Orange "]
file.writelines(messages)
file.write(" Append From Python")

file.close()