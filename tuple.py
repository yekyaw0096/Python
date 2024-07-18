my_tuple = "Mg Mg", 23 
#tuple can be used as object literal/ read-only = immutable

print("My Tuple", my_tuple)
print("Name ",my_tuple[0], "age ", my_tuple[1])

m_tuple = "Aung Aung", 
#need (,) to count as one element, if no (,) -> might be mistaken with string
print ("Type ", type(m_tuple))

student_tuple = (
                ("Aung Aung", 25),
                ("Hla Hla", 22)    
)

print("students ",student_tuple)
print("students[0] ",student_tuple[0])
#tuple is immutable and cannot change values


