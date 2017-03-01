from multiprocessing import Process
import os

def hello(name):
    print('Hello ' + name)
    print('My PID is {0}'.format(os.getpid()))
    print("My parent's PID is {0}".format(os.getppid()))

# Create a new process
p = Process(target=hello, args=('Alice', ))
p.start()  # start the process
p.join()   # end the process

print('Spawned a new process from PID {0}'.format(os.getpid()))

