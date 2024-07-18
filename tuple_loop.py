lst = ["apple","orange","grape","pineapple"]
#[("APPPLE",5),...]

lst_two = [(x.upper(),len(x))for x in lst if len(x)>5] 
#list_functions + for loop + if coniditon / List Comprehension
print("List two ",lst_two)

marks = [
    ("Myanmar", 30),
    ("English", 50),
    ("Maths", 40),     
         ]

pass_subject = [sub for sub in marks if sub[1]>39]
print("Pass subjects ", pass_subject)

pass_exam = len(marks) == len(pass_subject)
print("Pass exam ",pass_exam)