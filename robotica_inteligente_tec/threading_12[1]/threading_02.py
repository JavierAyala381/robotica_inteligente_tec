import threading
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
t1 = threading.Thread(target=thread_delay, args=('t1', 1))
t2 = threading.Thread(target=thread_delay, args=('t2', 3))

t1.start()
t2.start()

t1.join()
t2.join()

print("Thread execution is complete!")