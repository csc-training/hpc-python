from multiprocessing import Process, Manager

def squared(a, i):
    a[i] = a[i] * a[i]

manager = Manager()
numbers = manager.list()
numbers.extend(range(10))

p = [Process(target=squared, args=[numbers, i]) for i in range(10)]

for i in range(10):
    p[i].start()
for i in range(10):
    p[i].join()

print numbers[:]

