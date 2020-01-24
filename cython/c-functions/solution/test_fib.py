from fib import fibonacci
from fib_py import fibonacci as fibonacci_py
from timeit import repeat

ncython = 100
npython = 10

# Pure Python
time_python = repeat("fibonacci_py(30)", number=npython, globals=locals())
time_python = min(time_python) / npython

# Cython
time_cython = repeat("fibonacci(30)", number=ncython, globals=locals())
time_cython = min(time_cython) / ncython

print("Pure Python: {:5.4f} s".format(time_python))
print("Cython:      {:5.4f} s".format(time_cython))
print("Speedup:    {:5.1f}".format(time_python / time_cython))

