import operator

my_string = """
Programming with Java
Programming with Javascript with node
Programming with Python with Django
"""

words = my_string.split()
print("Words ", words)

unique_words = set(words)
print("Unique word ", unique_words)

results = [(w,my_string.count(w)) for w in unique_words]
results.sort(key=operator.itemgetter(1),reverse=True) #reverse = True -> Descending
#sort with second keys
print("Result ",results)