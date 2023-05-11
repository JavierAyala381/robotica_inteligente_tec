import threading
from threading import Thread, Lock
import time
import random
import multiprocessing

MAXVAL = 100

class Datathreads(Thread):
    counter = 0  # Class variable.
    counter_lock = Lock()  # Control concurrent access to shared class variable.

    def __init__(self, name):
        super().__init__()  # Initialize base class.
        self.name = name
        self.delay = random.randint(1, 2)

    def run(self):
        print('Starting Thread:', self.name)
        while True:
            with self.counter_lock:
                if self.counter >= MAXVAL:
                    break  # Exit while loop (also releases lock).
                Datathreads.counter +=1
                print(self.name, '-------->', self.counter)
            time.sleep(self.delay)
        print('Execution of Thread:', self.name, 'is complete!')

n_threads = multiprocessing.cpu_count()

''' Create and start worker threads, then wait for them all to finish. '''
workers = [Datathreads(name=f'Thread #{i}')  for i in range(n_threads)]
for worker in workers:
    worker.start()
# Wait for all threads to finish.
for worker in workers:
    worker.join()
print()
print('Thread execution is complete!')
print('final counter value:', Datathreads.counter)