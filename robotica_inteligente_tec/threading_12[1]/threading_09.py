from time import sleep
from random import random
from threading import Thread
from threading import Lock

def task(lock, identifier, value):
    with lock: # acquire the lock
        print(f'thread: {identifier} got the lock, sleeping: {value}s')
        sleep(value)
 
lock = Lock() # create a shared lock
# start a few threads that attempt 
# to execute the same critical section
for i in range(10):
    # start a thread
    th = Thread(target=task, args=(lock, i, random()))
    th.start()

print('Finish all the threads...')