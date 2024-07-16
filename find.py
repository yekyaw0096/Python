str = "Welcome from Python Programming"
print("find on ",str.find("Python"))#return -1 if not found(Preferred to use)
print("index on ",str.index("Python"))#value errorized

application_type = "application/x-www-form-urlendcoded"
type = application_type[application_type.find("/")+1:]
print("Type ", type)