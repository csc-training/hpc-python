<!-- Title: Avoiding function call overheads -->

<!-- Short description:

Function calls in Python are relatively expensive compared to some other
languages. In this article we show how Cython can reduce these overheads.

-->

# Avoiding function call overheads

Function calls in Python are relatively expensive in comparison to for
example C. Cython allows one to reduce this overhead significantly.

Main reason for the large function call overhead in Python is the "boxing"
and "unboxing" of function call arguments and return values. Once again,
dynamic typing makes programming more flexible but with a cost in
performance.

One can investigate the function call overhead in Python with the following
example. Let's make a simple code that does not perform much else than calls
a function in a loop:

~~~python
def inner(i):
    return i+1

def outer_1(n):
    x = 0
    for i in range(n):
        x = inner(x)
~~~

We can create also a version which does not have the function call:

~~~python
def outer_2(n):
    x = 0
    for i in range(n):
        x = x + 1
~~~

If one measures the performance of the two **outer** functions, one observes
that the one with the function call in the loop is typically 3-4 times slower.


## Using pure C functions

If a function is used only within a Cython module, one can get rid of a large
part of Python's function call overhead by declaring the function as a pure C
function, once again using the **cdef** keyword:

~~~python
cdef int add (int x, int y):
    cdef int result
    result = x + y
    return result
~~~

When a function is defined as a pure C function, it can be called only from
the corresponding Cython module, but not from a Python code. If a function is
called both from Cython and Python, Cython can generate an additional Python
wrapper by declaring the function with **cpdef** instead of *cdef*:

~~~python
cpdef int add (int x, int y):
    cdef int result
    result = x + y
    return result
~~~

This adds some overhead, so if the function is not called from Python it is
better to use just **cdef**.


## Mandelbrot kernel as pure C function

The **kernel** function is called only within the **mandelbrot.pyx** module,
so we can make it a pure C function:

~~~python
cdef int kernel(zr, zi, cr, ci, lim, cutoff):
    ''' Computes the number of iterations `n` such that
        |z_n| > `lim`, where `z_n = z_{n-1}**2 + c`.
    '''
    count = 0
    while ((zr*zr + zi*zi) < (lim*lim)) and count < cutoff:
        zr, zi = zr * zr - zi * zi + cr, 2 * zr * zi + ci
        count += 1
    return count
~~~

When continuing with the performance investigation, we obtain the following
results:

  - Pure Python:  0.57 s
  - Static type declarations in the kernel: 14 ms
  - Kernel as C-function: 9.6 ms

In this case the speed-up is not so drastic, but still a respectable 1.5.
