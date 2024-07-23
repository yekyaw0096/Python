marks = {
    "Myanmar":40,
    "English":50,
    "Math":60,
}

key = "Myanmar1"
value = marks.pop(key,0) #return key or if not found return 0
print("Key -> ",value) #get method is better and safe

print("Marks popitem ",marks.popitem()) #Last in first out
print("Marks ", marks)

for item in  reversed(marks):
    print("Item ",item)
    
print("Key ", marks.setdefault(key, "Ma shi")) #if there is no key, return default value

marks.update(Bio=50, Chem=60)
print("After update ", marks)