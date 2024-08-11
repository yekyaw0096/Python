import csv

with open("data.csv","r") as file_csv:
    
    reader = csv.reader(file_csv) #reader object need to call first in csv

    data = list(reader)
    for item in data:
        print("Item ",item)
    
print("Read csv file done")
    
    
    