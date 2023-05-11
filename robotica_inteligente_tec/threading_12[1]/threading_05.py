import threading
import time

def thread_delay(thread_name, delay):
    count = 0
    while count < 3:
        time.sleep(delay)
        count += 1
        print(thread_name, '-------->', time.time())

class DataCampThread(threading.Thread):
    def __init__(self, name, delay):
        threading.Thread.__init__(self)
        self.name = name
        self.delay = delay


    def run(self):
        print('Starting Thread:', self.name)
        thread_delay(self.name,self.delay)
        print('Execution of Thread:', self.name, 'is complete!')


t1 = DataCampThread('t1', 1)
t2 = DataCampThread('t2', 3)    

t1.start()
t2.start()

t1.join()
t2.join()

print("Thread execution is complete!")