import time
from threading import *

def double(n):
    
    for i in range(0, n):
        print("I am double => ", i*2)
        time.sleep(1) #time.sleep() is used to stop using the cpu for a while

def square(n):
    
    for i in range(0, n):
        print("I am square => ", i*i)
        time.sleep(1)

start_time = time.time() #start the thread time

threadA = Thread(target = double, args = (5,))
threadB = Thread(target = square, args = (5,))

threadA.start()
threadB.start()

print("Active Thread Counts ",active_count())
print("Thread A is alive ",threadA.is_alive()) #is_alive => using the thread
print("Thread B is alive ",threadB.is_alive())

thread_list = enumerate()
for thread in thread_list:
    print("Thread ", thread.name, " is daemon ", thread.isDaemon()) #Daemon thread is thread running in background
    print("Threading ",thread.name)

threadA.join() #wait for threadA finish
threadB.join() #wait for threadB finish

print("Active Thread Counts ",active_count())
for thread in thread_list:
    print("After Threading ",thread.name)
    
#and follow by end_time process after finishing the A and B join()

end_time = time.time()
print("Time ", end_time - start_time)
