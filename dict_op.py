marks = {
    "Myanmar":40,
    "English":50,
    "Math":60,
    12:3000
}

key = "Bio"
value = marks.get(key,0) #return key or if not found return 0
print("Key -> ",value) #get method is better and safe

marks["Myanmar"] = 77
print("Marks ", marks)

del marks["Myanmar"]
print("Marks ",marks)

print("Keys ",marks.keys())
print("Values ",marks.values())

iterator = iter(marks) #return key, value
for k in iterator:
    print("Key ", k)
    
new_dict = dict.fromkeys(iter(marks),[10,20]) #return copy of dict
print("New Dict ", new_dict)
