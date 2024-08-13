from threading import *
import time

sem = BoundedSemaphore(2) #semaphore's release is limited as acquire number

print("Acquire 1")
sem.acquire()

print("Acquire 2")
sem.acquire()

print("Release 1")
sem.release()

print("Release 2")
sem.release()

print("Release 3")
sem.release()

print("Release 4")
sem.release()

print("Done ")

#Release can be much more than Acquire in normal semaphore.