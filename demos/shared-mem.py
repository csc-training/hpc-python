from multiprocessing import Process, Array

def squared(a):
    for i in range(len(a)):
        a[i] = a[i] * a[i]

numbers = Array('i', range(10))
p = Process(target=squared, args=[numbers])
p.start()
p.join()

print(numbers[:])

