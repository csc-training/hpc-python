from multiprocessing import Process, Array

def squared(a, i):
    """
    Squared version of get_squared.

    Args:
        a: (todo): write your description
        i: (float): write your description
    """
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

