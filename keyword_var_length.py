def sum_marks(**marks): #** for multiple keyword parameters
    total = 0
    print("Numbers ",marks, 'type ',type(marks))

    for k,v in marks.items():
        total += v
        return total

print("Sum ",sum_marks(myanmar=50,english=60,math=80))

our_marks = {
    "eng":100,
    "math":50,
    "myanmar":60,
}

print("Sum ",sum_marks(**our_marks)) #** for unpacking