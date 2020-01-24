from fib import fibonacci
from fib_py import fibonacci as fibonacci_py, fibonacci_cached
from timeit import repeat

ncython = 100
npython = 10
ncached = 10000000

# Pure Python
time_python = repeat("fibonacci_py(30)", number=npython, globals=locals())
time_python = min(time_python) / npython

# Cython
time_cython = repeat("fibonacci(30)", number=ncython, globals=locals())
time_cython = min(time_cython) / ncython

# Python, cached
time_cached = repeat("fibonacci_cached(30)", number=ncached, globals=locals())
time_cached = min(time_cached) / ncached

print("Pure Python:          {:5.4f} s".format(time_python))
print("Cython:               {:5.4f} ms".format(time_cython*1.e3))
print("Speedup:              {:5.1f}".format(time_python / time_cython))
print("Pure Python cached:   {:5.4f} us".format(time_cached*1.e6))
print("Speedup over Cython:  {:5.1e}".format(time_cython / time_cached))

