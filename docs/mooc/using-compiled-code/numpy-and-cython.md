<!-- Title: Using NumPy with Cython -->

<!-- Short description:

In this article we present how to efficiently utilize NumPy arrays with
Cython.

-->

# Using NumPy with Cython

NumPy arrays are the work horses of numerical computing with Python, and
Cython allows one to work more efficiently with them.

As discussed in week 2, when working with NumPy arrays in Python one should
avoid `for`-loops and indexing individual elements and instead try to write
operations with NumPy arrays in a vectorized form. The reason is two-fold:
overhead inherent to Python `for`-loops and overhead from indexing a NumPy
array.

When taking Cython into the game that is no longer true. When the Python
`for` structure only loops over integer values (e.g. `for in range(N)`),
Cython can convert that into a pure C `for` loop. Also, when additional Cython
declarations are made for NumPy arrays, indexing can be as fast as indexing
C arrays.


## Compile time definitions for NumPy

In order to create more efficient C-code for NumPy arrays, additional
declarations are needed. To start with, one uses the Cython `cimport`
statement for getting access to NumPy types:

~~~python
cimport numpy as cnp
~~~

The `cimport` statement imports C data types, C functions and variables, and
extension types. It cannot be used to import any Python objects, and it
doesn’t imply any Python import at run time.

By declaring the type and dimensions of an array before actually creating it,
Cython can access the NumPy array more efficiently:

~~~python
import numpy as np   # Normal NumPy import
cimport numpy as cnp # Import for NumPY C-API

def func():  # declarations can be made only in function scope
    cdef cnp.ndarray[cnp.int_t, ndim=2] data
    data = np.empty((N, N), dtype=int)

    …
    for i in range(N):
        for j in range(N):
            data[i,j] = …       # double loop is done in nearly C speed
~~~


## More indexing enhancements

Python is still performing bounds checking for arrays (i.e. trying to access
outside the allocated memory gives an error), and allowing negative indexing.
If negative indexing is not needed, and one is certain that there are no
out of bounds errors in indexing, performance can be enhanced even more by
disabling negative indexing and bounds checking for all indexing operations
within the function. This is done by using cython decorators before the
function as follows:

~~~python
import numpy as np   # Normal NumPy import
cimport numpy as cnp # Import for NumPY C-API
cimport cython

@cython.boundscheck(False)
@cython.wraparound(False)
def func():  # declarations can be made only in function scope
    cdef cnp.ndarray[cnp.int_t, ndim=2] data
    data = np.empty((N, N), dtype=int)

    …
    for i in range(N):
        for j in range(N):
            data[i,j] = …       # double loop is done in nearly C speed
~~~


## Efficient NumPy array indexing in Mandelbrot calculation

Our **kernel** function does not offer further easy optimization, but we can
make the indexing and loops more efficient in the higher level
**compute_mandel** function. To do this, we provide declarations for the
NumPy arrays, transform the `for` -loops to be simple integers, and disable
also the bounds checking and negative indexing:

~~~python
cimport numpy as cnp
import cython
...
@cython.boundscheck(False)
@cython.wraparound(False)
def compute_mandel(double cr, double ci, int N, double bound=1.5,
                   double lim=1000.,  int cutoff=1000000):
    cdef cnp.ndarray[cnp.int_t, ndim=2] mandel
    mandel = np.empty((N, N), dtype=int)

    cdef cnp.ndarray[cnp.double_t, ndim=1] grid_x
    grid_x = np.linspace(-bound, bound, N)

    cdef int i,j
    cdef double x, y

    t0 = time()
    for i in range(N):
        for j in range(N):
            x = grid_x[i]
            y = grid_x[j]
            mandel[i,j] = kernel(x, y, cr, ci, lim, cutoff)
    return mandel, time() - t0
~~~

After these additions the final timing results are:

  - Pure Python: 0.57 s
  - Static type declarations in the kernel: 14 ms
  - Kernel as C-function: 9.6 ms
  - Fast indexing: 2.5 ms

Thus, at the end we were able to increase the speed of the application by a
factor of 230! Naturaly, not all application benefit from Cythonization by
that much, but at least an order of magnitude improvement in performance is
very typical.
