with open("write_file.py","w") as file:

    file.seek(10,0)
    file.write("hello")