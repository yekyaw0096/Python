file = open("write_file.py","r")

ten_char = file.read(10) #read only first 10 characters
print("Ten characters ",ten_char)

read_line = file.readline() # continue to read only one line after the end of first read
print("Read by line ",read_line)

read_all_lines = file.readlines() #read all lines stored in list
print("Read all lines ", read_all_lines)

file.close()