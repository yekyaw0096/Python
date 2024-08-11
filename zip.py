from zipfile import *

file = ZipFile("file_notes.zip","w",ZIP_DEFLATED) #Zip deflated = file compress to zip

file.write("notes.txt") # file name to zip
file.write("data.csv") # file name to zip

file.close()