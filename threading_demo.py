from threading import *

def method1():
    for i in range(1,15):
        print("Child Thread ", i)

thread = Thread(target = method1) #create thread with target to run the method1, divide the thread
thread.start() #without start(), the thread will not start

for i in range(1, 16):
    print("Main Thread ", i)
    
#Main and Child thread will run concurrently
