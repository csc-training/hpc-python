import numpy as np
from time import perf_counter

def calculate(a):
    result = np.exp(a) * np.sin(a)
    return result

x = np.random.random((100, 100))
t0 = perf_counter()
for r in range(1000):
    calculate(x)
t1 = perf_counter()
print("Time spent", t1 - t0)
