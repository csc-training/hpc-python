import numpy as np
import time

class Timer:
    def __enter__(self):
        self.start = time.process_time()
        return self

    def __exit__(self, *args):
        self.end = time.process_time()
        self.interval = self.end - self.start


def calculate(a):
    result = np.exp(a) * np.sin(a)
    return result

x = np.random.random((100, 100))

with Timer() as t:
    for r in range(1000):
        calculate(x)

print("Time spent", t.interval)
