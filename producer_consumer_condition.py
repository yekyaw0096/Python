from threading import *
import time
import random

items = []

condition = Condition()

class Producer(Thread):
    
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        for i in range(10):
            with condition:
                item = random.randint(0,256)
                #condition.acquire() #get the lock
                items.append(item)
                print("Produce ",item)
                time.sleep(1) # 1 second sleeping
                condition.notifyAll() #notify the wait() to ready to use
                time.sleep(1)
                #condition.release() #release the lock
            
#Consumer is trying to pop while Producer is not start working. Consumer gets nothing to pop.

class Consumer(Thread):
    
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        for i in range(10):
            time.sleep(1)
            with condition:
                print("Consumer is waiting")
                condition.wait()
                item = items.pop()
                print("Item Consume ",item)

producer = Producer()
consumer = Consumer()

producer.start()
consumer.start()