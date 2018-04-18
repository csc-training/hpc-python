from multiprocessing import Process
import os

def hello(name):
    print('Hello ' + name)
    print('My PID is {0}'.format(os.getpid()))
    print("My parent's PID is {0}".format(os.getppid()))

# Create a new process
p = Process(target=hello, args=['Alice'])

# Start the process
p.start()
print('Spawned a new process from PID {0}'.format(os.getpid()))

# End the process
p.join()

