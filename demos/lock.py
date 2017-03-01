from multiprocessing import Process, Lock
import random
import time

def hello(lock, id):
    lock.acquire()
    time.sleep(random.uniform(1, id % 4))
    print 'Hello world! My ID is', id
    lock.release()

lock = Lock()
for i in range(10):
    Process(target=hello, args=(lock, i)).start()

