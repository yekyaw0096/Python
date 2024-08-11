note_file = open("notes.txt", "w")

print("name ", note_file.name)
print("mode ", note_file.mode)
print("readable ", note_file.readable())
print("writeable ", note_file.writable())
print("is closed ",note_file.closed) #file is open

note_file.close()
print("is closed ", note_file.closed) #file is closed now