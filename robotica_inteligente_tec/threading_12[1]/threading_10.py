import threading
from threading import Thread, Lock
import time
import random

MAXVAL = 10
counter = 0  # Global variable.
counter_lock = Lock()  # To coordinate concurrent access to global variable.
n_threads = 3

class DataThreads(Thread):
    def __init__(self, name):
        super().__init__()  # Initialize base class.
        self.name = name
        self.delay = random.randint(1, 2)

    def run(self):
        global counter
        print('Starting Thread:', self.name)
        while True:
            with counter_lock:
                if counter >= MAXVAL:
                    break  # Exit while loop (also releases lock).
                counter += 1
                print(self.name, '-------->', counter)
            time.sleep(self.delay)
        print('Execution of Thread:', self.name, 'is complete!')

''' Create and start worker threads, then wait for them all to finish. '''
workers = [DataThreads(name=f'Thread #{i}')  for i in range(n_threads)]
for worker in workers:
    worker.start()
for worker in workers: # Wait for all treads to finish.
    worker.join()

print()
print('Thread execution is complete!')
print('final counter value:', counter)