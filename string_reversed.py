str = input("Enter string ")
print("Reverse ", str[::-1])

words = str.split()
reversed_words = " ".join(words[::-1])#" ".join() to become a word list
print("Become words ", reversed_words)