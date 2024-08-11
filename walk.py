import os 

for dir_path, dir_names, filee_names in os.walk('../'): #transverse all the files within directory
    
    print("Dir path ", dir_path)
    print("Dir name ", dir_names)
    print("File path ", dir_path)

