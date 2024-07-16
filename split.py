str = "Apple Orange Banana"
str_list = str.split()
print("str_list ",str_list)
print("str ",str)

date_str = "03-08-2024"
date_str_list = date_str.split("-")
print("date list ",date_str_list)

date_str_new = "/".join(date_str_list)#list or set can be joined with "/"
print("date str new ",date_str_new)
