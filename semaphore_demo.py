from threading import *
import time

sem = Semaphore(2) #create two thread limit and automatically reduce per thread use until 0

def one(thread_name):
    
    sem.acquire() #Become semaphore(1)
    print("Get lock ",thread_name)
    
    for i in range(1,20):
        print("Process ",thread_name, " => ",i)
    
    print("Release Lock ", thread_name, " sem ", sem)
    sem.release()

t1 = Thread(target=one, args=("one ", ))
t2 = Thread(target=one, args=("two ", ))
t3 = Thread(target=one, args=("three ", ))

t1.start()
t2.start()
t3.start()
    