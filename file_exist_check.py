import os

file_name = "notes.txt"

if os.path.isfile(file_name): #file check
    print("File exists")

else:
    print("File does not exist")