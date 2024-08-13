from threading import *
import time
import random

items = []

class Producer(Thread):
    
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        for i in range(10):
            item = random.randint(0,256)
            items.append(item)
            print("Produce ",item)
            time.sleep(1) # 1 second sleeping
            
#Consumer is trying to pop while Producer is not start working. Consumer gets nothing to pop.

class Consumer(Thread):
    
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        for i in range(10):
            item = items.pop()
            print("Item Consume ",item)
            #time.sleep(1) # 1 second sleeping

producer = Producer()
consumer = Consumer()

producer.start()
consumer.start()