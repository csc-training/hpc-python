from multiprocessing import Process, Array

def squared(a):
    """
    Squared sum of a list.

    Args:
        a: (float): write your description
    """
    for i in range(len(a)):
        a[i] = a[i] * a[i]

numbers = Array('i', range(10))
p = Process(target=squared, args=[numbers])
p.start()
p.join()

print(numbers[:])

