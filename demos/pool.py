from multiprocessing import Pool
import time

def f(x):
    """
    Return a function f ( x ).

    Args:
        x: (int): write your description
    """
    return x**2

pool = Pool(8)

# Blocking execution (with a single process)
result = pool.apply(f, [4])
print(result)

# Non-blocking execution "in the background"
result = pool.apply_async(f, [12])
while not result.ready():
    print("waiting...")
    time.sleep(1)
print(result.get())

