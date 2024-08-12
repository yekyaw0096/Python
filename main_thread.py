import threading

threading.currentThread().setDaemon(True) #Enabling the thread to run in background

threading.currentThread().setName("My Main Thread")
print("Current Thread running is ",threading.current_thread().getName())
print("Thread ID ",threading.currentThread().ident)

print("Is daemon ",threading.currentThread().isDaemon()) #cannot make background running if the thread is alive
