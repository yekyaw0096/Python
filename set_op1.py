marks = {
    "Myanmar":40,
    "English":50,
    "Math":60,
    12:3000
}
print("Marks ", marks) #Key,value pair is dictionary or associated array

for ele in marks: #dictionary can get key only
    print("Elements : ", ele, "marks ", marks[ele]) #for value need to be marks[ele]

for key,value in marks.items():
    print("Key ",key, " => ", value)

print("Items ", marks.items()) #return tuple-list
print("List ", list(marks)) #return only keys