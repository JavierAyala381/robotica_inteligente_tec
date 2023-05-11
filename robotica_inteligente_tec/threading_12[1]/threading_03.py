import threading
import time

def volume_cube(a):
    print ("Volume of Cube:", a*a*a)

def volume_square(a):
    print ("Volume of Square:", a*a)

t1 = threading.Thread(target=volume_cube, args=(2,))
t2 = threading.Thread(target=volume_square, args=(3,))

t1.start()
t2.start()

t1.join()
t2.join()

print("Thread execution is complete!")