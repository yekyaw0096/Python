file = open("write_file.py","r")

lines = file.readlines()
for line in lines:
    print(line, end="") #end='' is remove spaces between lines (use empty string)

file.close()