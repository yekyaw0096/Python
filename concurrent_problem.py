from threading import *
import time

counter = 0
lock = Lock() #to lock the thread

def increment():
    global counter
    for i in range(0, 100):
        lock.acquire()
        counter += 1 #commonly used code for both threads = critical section / sometimes it is code block
        lock.release()
        #time.sleep(0.1)

def decrement():
    global counter
    for i in range(0, 100):
        lock.acquire()
        counter -= 1 #critical section
        lock.release() #lock.aquire() without lock.release() become dead lock.
        #time.sleep(0.1)

thread_1 = Thread(target=increment)
thread_2 = Thread(target=decrement)

thread_1.start()
thread_2.start()

thread_1.join()
thread_2.join()

print("Counter is ",counter) #thread_1 is increse and thread_2 is decrease, counter will be 0

#mutual exclusion = lock one thread to be able use while the other thread is using