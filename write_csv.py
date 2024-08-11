import csv

with open("data.csv","a",newline="") as file_csv:
    
    writer = csv.writer(file_csv) #writer object need to call first in csv
    
    id = int(input("Enter id "))
    name = input("Enter name ")
    occupation = input("Enter occupation ")
    writer.writerow([id,name,occupation])