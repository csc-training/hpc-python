from multiprocessing import Process, Lock

def hello(lock, id):
    lock.acquire()
    print 'Hello world! My ID is', id
    lock.release()

lock = Lock()
for i in range(10):
    Process(target=hello, args=(lock, i)).start()

