with open("write_file.py","r") as file:

    ten_char = file.read(10) #read only first 10 characters
    print("Ten characters ",ten_char)
    print("tell ", file.tell()) #use tell() to locate the cursor position

    read_line = file.readline()
    print("Read by line ",read_line)

    read_all_lines = file.readlines()
    print("Read all lines ", read_all_lines)
