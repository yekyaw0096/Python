import os
from datetime import *

stats = os.stat("./walk.py") #stat is for accessing the status of the file
print("File size in bytes ",stats.st_size) #st_size is for file size
print("Last Modified ",datetime.fromtimestamp(stats.st_mtime)) #st_mtime is for file modified time
print("Last Access ",datetime.fromtimestamp(stats.st_atime)) #st_atime is for file access time