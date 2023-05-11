from time import sleep
from threading import Thread
 
class CustomThread(Thread):
    def run(self): # override the run function
        sleep(1) # block for a moment
        # display a message
        print('This is coming from another thread')
        self.value = 99 # store return value
 
# create the thread
thread = CustomThread()
thread.start() # start the thread
# wait for the thread to finish
print('Waiting for the thread to finish')
thread.join()
# get the value returned from run
value = thread.value
print(f'The value is: {value} ')
