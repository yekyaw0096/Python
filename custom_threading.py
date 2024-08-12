from threading import *

class MyThread(Thread):
    
    def __init__(self,name):
        super().__init__()
        self.name = name
    
    def run(self): #write code in run() which will run in thread 
        for i in range(1,20):
            print("Thread ",self.name, " i ", i)

print("Active Thread Counts ",active_count())

threadA = MyThread("ThreadA")
threadB = MyThread("ThreadB")

threadA.start()
threadB.start()
print("Active Thread Counts ",active_count())
#main thread, threadA, threadB