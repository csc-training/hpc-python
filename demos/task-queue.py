from multiprocessing import Process, Queue

def f(q):
    while True:
        x = q.get()
        if x is None:
            break
        print(x**2)

q = Queue()
for i in range(10):
    q.put(i)

# task queue: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(3):
    q.put(None)
    p = Process(target=f, args=(q, ))
    p.start()

