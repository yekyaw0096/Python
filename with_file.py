with open("write_file.py","r") as file:

    lines = file.readlines()
    for line in lines:
        print(line, end="") #end='' is remove spaces between lines (use empty string)

#with ... as file and automatically closed the file at the end