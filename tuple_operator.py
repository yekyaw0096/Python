my_tuple = range(20,25)
tuple_a = tuple(my_tuple)
print("Tuple constructor from range ", tuple_a)

tuple_b = tuple(range(29,34))
print("B tuple ", tuple_b)

tuple_c = tuple_a + tuple_b #two tuples are concatenated
print("Tuple C ", tuple_c)

students = ("Maung Aung","Tin Hla","Yee Soe")
students_repeated = students*2
print("Students_repated ",students_repeated)
print("Students_repeated length ", len(students_repeated))
print("Students_repeated count(Maung Aung) ",students_repeated.count("Maung Aung"))
print("Students_repeated index(Maung Aung) ",students_repeated.index("Maung Aung"))

#print("Students_repeated index(Maung Maung) ",students_repeated.index("Maung Maung"))
print("String index ","Hello".find("Hllo"))
#Collection.index() not found -> return exception, String.find() not found -> return -1

another_tuple = (2,1,4,5,3)
sorted_tuple = sorted(another_tuple)
print("Sorted tuple ",sorted_tuple)
print("Min ",min(another_tuple))
print("Max ",max(another_tuple))

string_tuple = "Two","Three","One"
print("Sorted String ", sorted(string_tuple))