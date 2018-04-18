from multiprocessing import Process, Array

def squared(a, i):
    a.acquire()
    a[i] = i * i
    a.release()

numbers = Array('i', range(10))
p = [Process(target=squared, args=[numbers, i]) for i in range(10)]

for i in range(10):
    p[i].start()
for i in range(10):
    p[i].join()

print(numbers[:])

