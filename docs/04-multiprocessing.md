---
title:  Multiprocessing
lang:   en
---

# Processes and threads

![](img/processes-threads.png)

<div class="column">

## Process

- Independent execution units
- Have their own state information and *own memory* address space

</div>
<div class="column">

## Thread

- A single process may contain multiple threads
- Have their own state information, but *share* the *same memory*
  address space

</div>


# Processes and threads

![](img/processes-threads.png)

<div class="column">

## Process

- Long-lived: created when parallel program started, killed when
  program is finished
- Explicit communication between processes

</div>
<div class="column">

## Thread

- Short-lived: created when entering a parallel region, destroyed
  (joined) when region ends
- Communication through shared memory

</div>

# Processes and threads

![](img/processes-threads.png)

<div class="column">

## Process

- MPI
    - good performance
    - scales from a laptop to a supercomputer

</div>
<div class="column">

## Thread

- OpenMP
    - C / Fortran, not Python
- threading module
    - only for I/O bound tasks (maybe)
    - Global Interpreter Lock (GIL) limits usability

</div>


# Processes and threads

![](img/processes-threads.png)

<div class="column">

## Process

- MPI
    - good performance
    - scales from a laptop to a supercomputer

</div>
<div class="column">

## ~~Thread~~ Process

- multiprocessing module
    - relies on OS for forking worker processes that mimic threads
    - limited communication between the parallel processes

</div>


# Multiprocessing

- Underlying OS used to spawn new independent subprocesses
- processes are independent and execute code in an asynchronous manner
    - no guarantee on the order of execution
- Communication possible only through dedicated, shared communication
  channels
    - Queues, Pipes
    - must be created before a new process is forked


# Spawn a process

```python
from multiprocessing import Process
import os

def hello(name):
    print 'Hello', name
    print 'My PID is', os.getpid()
    print "My parent's PID is", os.getppid()

# Create a new process
p = Process(target=hello, args=('Alice', ))

# Start the process
p.start()
print 'Spawned a new process from PID', os.getpid()

# End the process
p.join()
```


# Communication

- Sharing data
    - shared memory, data manager
- Pipes
    - direct communication between two processes
- Queues
    - work sharing among a group of processes
- Pool of workers
    - offloading tasks to a group of worker processes


# Queues

- FIFO (*first-in-first-out*) task queues that can be used to distribute
  work among processes
- Shared among all processes
    - all processes can add and retrieve data from the queue
- Automatically takes care of locking, so can be used safely with minimal
  hassle


# Queues

```python
from multiprocessing import Process, Queue

def f(q):
    while True:
        x = q.get()
        if x is None:
            break
        print(x**2)

q = Queue()
for i in range(100):
    q.put(i)
# task queue: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, ..., 99]

for i in range(3):
    q.put(None)
    p = Process(target=f, args=(q, ))
    p.start()
```


# Queues

```python
from multiprocessing import Process, Queue

def f(q):
    while True:
        x = q.get()
        if x is None: # if sentinel, stop execution
            break
        print(x**2)

q = Queue()
for i in range(100):
    q.put(i)
# task queue: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, ..., 99]

for i in range(3):
    q.put(None) # add sentinels to the queue to signal STOP
    p = Process(target=f, args=(q, ))
    p.start()
```


# Pool of workers

- Group of processes that carry out tasks assigned to them
    1. Master process submits tasks to the pool
    2. Pool of worker processes perform the tasks
    3. Master process retrieves the results from the pool
- Blocking and non-blocking (= asynchronous) calls available


# Pool of workers

```python
from multiprocessing import Pool
import time

def f(x):
    return x**2

pool = Pool(8)

# Blocking execution (with a single process)
result = pool.apply(f, (4,))
print(result)

# Non-blocking execution "in the background"
result = pool.apply_async(f, (12,))
while not result.ready():
    time.sleep(1)
print(result.get())
# an alternative to "sleeping" is to use e.g. result.get(timeout=1)
```


# Pool of workers

```python
from multiprocessing import Pool
import time

def f(x):
    return x**2

pool = Pool(8)

# calculate x**2 in parallel for x in 0..9
result = pool.map(f, range(10))
print(result)

# non-blocking alternative
result = pool.map_async(f, range(10))
while not result.ready():
    time.sleep(1)
print(result.get())
```


# Summary

- Parallelism achieved by launching new OS processes
- Only limited communication possible
    - work sharing: queues / pool of workers
- Non-blocking execution available
    - do something else while waiting for results
- Further information:
  https://docs.python.org/2/library/multiprocessing.html
