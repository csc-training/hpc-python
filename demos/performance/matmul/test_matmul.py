import os
from timeit import repeat
import numpy as np
from matmul import multiply

os.system('./mm 1000')

a = np.random.random((1000, 1000))
b = np.random.random((1000, 1000))

nnumpy = 100

time_numpy = repeat("c = np.dot(a, b)", number=nnumpy, globals=locals())
time_numpy = min(time_numpy) / nnumpy
print("Time with numpy.dot:  {:5.3f} s".format(time_numpy))

npython = 1
time_python = repeat("c = multiply(a, b)", number=npython, 
                     repeat=1, globals=locals())

print("Time with Python:   {:5.3f} s".format(time_python[0]))
