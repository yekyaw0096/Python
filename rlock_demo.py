from threading import *
import time

lock = RLock() #Re-entrance lock/ entering into same thread/ not work for different thread

def factorial(n):
    print("Try to get lock from n ",n)
    lock.acquire()
    print("Get lock for n ",n)
    if n == 0:
        return 1
    else:
        result = n * factorial(n-1) #same factorial from def factorial(n) method
        lock.release()
        return result
    
print("Factorial ", factorial(3))