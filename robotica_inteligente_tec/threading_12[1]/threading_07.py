from threading import Thread
import time

def thread_delay(thread_name, delay):
    count = 0
    while count < 3:
        last_time = time.time()
        time.sleep(delay)
        count += 1
        now = time.time() - last_time
        #minute = int(now / 60)
        seconds = int(now % 60)
        print(thread_name, '-------->', seconds)#time.time())

class DataThread(Thread):
    def __init__(self, name, delay):
        Thread.__init__(self)
        self.name = name
        self.delay = delay
    def run(self):
        print('Starting Thread:', self.name)
        thread_delay(self.name, self.delay)
        print('Execution of Thread:', self.name, 'is complete!')

t1 = DataThread('t1', 1)
print(t1.name)
print(t1.daemon)
print(t1.native_id)
print(t1.is_alive())

t1.name = 'terminator1'
t1.daemon=True

t1.start()
print(t1.name)
print(t1.daemon)
print(t1.native_id)
print(t1.is_alive())
print('Waiting for the thread to finish')
t1.join()
print("Thread execution is complete!")

