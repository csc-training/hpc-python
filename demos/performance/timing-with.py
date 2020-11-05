import numpy as np
import time

class Timer:
    def __enter__(self):
        """
        Enter the process.

        Args:
            self: (todo): write your description
        """
        self.start = time.process_time()
        return self

    def __exit__(self, *args):
        """
        Intervaluates the exit.

        Args:
            self: (todo): write your description
        """
        self.end = time.process_time()
        self.interval = self.end - self.start


def calculate(a):
    """
    Calculate the sum of a vector

    Args:
        a: (float): write your description
    """
    result = np.exp(a) * np.sin(a)
    return result

x = np.random.random((100, 100))

with Timer() as t:
    for r in range(1000):
        calculate(x)

print("Time spent", t.interval)
