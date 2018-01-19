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
    print("waiting...")
    time.sleep(1)
print(result.get())

