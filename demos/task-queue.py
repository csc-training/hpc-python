from multiprocessing import Process, Queue

def f(q, i):
    while True:
        x = q.get()
        if x is None:
            break
        print('[{0}] {1}'.format(i, x**2))

q = Queue()
for i in range(100):
    q.put(i)

# task queue: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, ..., 99]

n = 3   # no. of processes
p = []  # list of processes
for i in range(n):
    p.append(Process(target=f, args=[q, i]))
    q.put(None)  # add sentinels to signal STOP

# start work on all processes
for i in range(n):
    p[i].start()

