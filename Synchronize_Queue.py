from threading import *
import queue
import random

#items = queue.Queue() #queue is used for first in first out (FIFO)
#items = queue.LifoQueue() #Queue is used as Stack which is Last in first out
items = queue.PriorityQueue() #Queue return the smallest number as priority

class Producer(Thread):
    
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        for i in range(10):
            item = random.randint(0,256)
            items.put(item)
            print("Item Produce ",item)
            
#Consumer is trying to pop while Producer is not start working. Consumer gets nothing to pop.

class Consumer(Thread):
    
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        for i in range(10):
            item = items.get()
            print("Item consume", item)

producer = Producer()
consumer = Consumer()

producer.start()
consumer.start()