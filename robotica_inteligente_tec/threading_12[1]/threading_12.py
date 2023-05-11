import threading
from threading import Thread, Lock
import time
import multiprocessing
import random

def create_workers(n_threads, counter, maxval):
    workers = []
    for n in range(n_threads):
        worker = DataThreads('Thread - ' + str(n), counter, maxval)
        workers.append(worker)
    for worker in workers:
        worker.start()
    for worker in workers:
        worker.join()

    return DataThreads.counter

def sum_delay(thread_name, num, delay):
    num += delay
    print(thread_name, 'delay(', delay ,')','---->', num)
    return num

class DataThreads(Thread):
    counter = 0
    counter_lock = Lock()
    
    def __init__(self, name, cou, mv):
        super().__init__()
        self.name = name
        DataThreads.counter = cou
        DataThreads.max_val = mv
        self.delay = random.randint(1, 2)

    def run(self):
        print('Starting Thread:', self.name)
        while True:
            with self.counter_lock:
                if self.counter >= DataThreads.max_val:
                    break  # Exit while loop (also releases lock).
                DataThreads.counter = sum_delay(self.name, DataThreads.counter, self.delay)
            time.sleep(self.delay) # otherwise one thread can keep the thread all to itself
            # Normally other operations would be done after the thread
        print('Execution of Thread:', self.name, 'is complete!')

if __name__ == '__main__':
    n_threads = 5#multiprocessing.cpu_count() # create the agent
    counter = 7
    maxval = 20
    counter = create_workers(n_threads, counter, maxval)
    print(counter)
    print("Thread execution is complete!")