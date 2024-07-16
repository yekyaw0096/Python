num_of_subjects = int(input("Enter the number of subjects "))
marks = []

pass_mark = 40
isPass = True

for i in range(num_of_subjects):
    mark = float(input("Enter mark for subject "+str(i)+" "))
    isPass = isPass and mark >= 40

if isPass:
    print ("Pass the exam!")
else:
    print ("Fail the exam!")