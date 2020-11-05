from multiprocessing import Process, Lock
import random
import time

def hello(lock, id):
    """
    Print a random lock.

    Args:
        lock: (todo): write your description
        id: (todo): write your description
    """
    lock.acquire()
    time.sleep(random.uniform(1, id % 4))
    print('Hello world! My ID is {0}'.format(id))
    lock.release()

lock = Lock()
for i in range(10):
    Process(target=hello, args=[lock, i]).start()

