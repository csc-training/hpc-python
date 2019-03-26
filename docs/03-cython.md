---
title:  Cython and interfacing external libraries
lang:   en
---

# Cython {.section}

# Cython

- Optimising static compiler for Python
- Extended Cython programming language
- Tune readable Python code into plain C performance by adding static
  type declarations
- Easy interfacing to external C libraries


# Python overheads

- Interpreting
- "Boxing" - everything is an object
- Function call overhead
- Global interpreter lock - no threading benefits (CPython)


# Interpreting

- Cython command generates a C/C++ source file from a Cython source file
- C/C++ source is then compiled into an extension module
- Interpreting overhead is normally not drastic

```python
from distutils.core import setup
from Cython.Build import cythonize

# Normally, one compiles cython extended code with .pyx ending
setup(ext_modules=cythonize("mandel_cyt.py"), )
```

```bash
$ python setup.py build_ext --inplace

In [1]: import mandel_cyt
```


# Case study: Mandelbrot fractal

- Pure Python: 2.71 s
- Compiled with Cython: 2.61 s

```python
def kernel(zr, zi, cr, ci, lim, cutoff):
    count = 0

    while ((zr*zr + zi*zi) < (lim*lim)) and count < cutoff:
        zr = zr * zr - zi * zi + cr
        zi = zr * zr - zi * zi + cr
        count += 1

    return count
```


# "Boxing"

- In Python, everything is an object

FIXME: missing figure


# Static type declarations

- Cython extended code should have .pyx ending
    - Cannot be run with normal Python
- Types are declared with `cdef` keyword
    - In function signatures only type is given

<div class="column">

```python
def integrate(f, a, b, N):
    s = 0
    dx = (b - a) / N
    for i in range(N):
        s += f(a + i * dx)
    return s * dx
```

</div>
<div class="column">

```python
def integrate(f, double a, double b, int N):
    cdef double s = 0
    cdef int i
    cdef double dx = (b - a) / N
    for i in range(N):
        s += f(a + i * dx)
    return s * dx
```
</div>


# Static type declarations

- Pure Python: 2.71 s
- Type declarations in kernel: 20.2 ms


# Function call overhead

- Function calls in Python can involve lots of checking and "boxing"
- Overhead can be reduced by declaring functions to be C-functions
    - **cdef** keyword: functions can be called only from Cython
    - **cpdef** keyword: generate also Python wrapper (can have additional
    overhead in some cases)


# Using C functions

- Static type declarations: 20.2 ms
- Kernel as C function: 12.5 ms

```python
cdef int kernel(double zr, double zi, ...):
    cdef int count = 0
    while ((zr*zr + zi*zi) < (lim*lim)) and count < cutoff:
        zr = zr * zr - zi * zi + cr
        zi = zr * zr - zi * zi + cr
        count += 1
    return count
```


# NumPy arrays with Cython

- Cython supports fast indexing for NumPy arrays
- Type and dimensions of array have to be declared

```python
import numpy as np    # normal NumPy import
cimport numpy as cnp  # import for NumPY C-API

def func(): # declarations can be made only in function scope
    cdef cnp.ndarray[cnp.int_t, ndim=2] data
    data = np.empty((N, N), dtype=int)

    ...

    for i in range(N):
        for j in range(N):
            data[i,j] = ... # double loop is done in nearly C speed
```


# Compiler directives

- Compiler directives can be used for turning of certain Python features
  for additional performance
    - boundscheck (False) : assume no IndexErrors
    - wraparound (False): no negative indexing
    - ...

```python
import numpy as np    # normal NumPy import
cimport numpy as cnp  # import for NumPY C-API

import cython

@cython.boundscheck(False)

def func(): # declarations can be made only in function scope
    cdef cnp.ndarray[cnp.int_t, ndim=2] data
    data = np.empty((N, N), dtype=int)
```


# Final performance

- Pure Python: 2.7 s
- Static type declarations: 20.2 ms
- Kernel as C function: 12.5 ms
- Fast indexing and directives: 2.4 ms


# Where to add types?

- Typing everything reduces readibility and can even slow down the
  performance
- Profiling should be first step when optimising
- Cython is able to provide annotated HTML-report
- Lines are colored according to the level of "typedness"
    - white lines translate to pure C
    - lines that require the Python C-API are yellow (darker as they
    translate to more C-API interaction)

```bash
$ cython -a cython_module.pyx
$ firefox cython_module.html
```


# HTML-report {.section}

# Profiling Cython code

- By default, Cython code does not show up in profile produced by
  cProfile
- Profiling can be enabled for entire source file or on per function
  basis

```python
# cython: profile=True
import cython

@cython.profile(False)
cdef func():
    ...
```

```python
# cython: profile=False
import cython

@cython.profile(True)
cdef func():
    ...
```


# Summary

- Cython is optimising static compiler for Python
- Possible to add type declarations with Cython language
- Fast indexing for NumPy arrays
- At best cases, huge speed ups can be obtained
    - Some compromise for Python flexibility


# Further functionality in Cython

- Using C structs and C++ classes in Cython
- Exceptions handling
- Parallelisation (threading) with Cython
- ...


# Interfacing external libraries {.section}

# Increasing performance with compiled code

- There are Python interfaces for many high performance libraries
- However, sometimes one might want to utilize a library without Python
  interface
    - Existing libraries
    - Own code written in C or Fortran
- Python C-API provides the most comprehensive way to extend Python
- Cffi, cython, and f2py can provide easier approaches


# cffi

- C Foreign Function Interface for Python
- Interact with almost any C code
- C-like declarations within Python
    - Can often be copy-pasted from headers / documentation
- ABI and API modes
    - ABI does not require compilation
    - API can be more robust
    - Only ABI discussed here
- Some understanding of C required


# cffi example 1

```python
from cffi import FFI

ffi = FFI()

# Use sqrt from C standard math library
lib = ffi.dlopen("libm.so")
ffi.cdef("""float sqrtf(float x);""")

# Python takes care of proper datatype conversion
a = lib.sqrtf(4)
print(a)
```


# cffi example 2

```python
from cffi import FFI
import numpy as np

ffi = FFI()

lib = ffi.dlopen("./myclib.so") # Use functions from users own library

ffi.cdef("""void add(double *x, double *y, int n);""")
ffi.cdef("""void subtract(double *x, double *y, int n);""")

a = np.random.random((1000000,1))
b = np.zeros_like(a)

# "Pointer" objects need to be passed to library
aptr = ffi.cast("double *", ffi.from_buffer(a))
bptr = ffi.cast("double *", ffi.from_buffer(b))

lib.add(bptr, aptr, len(a))
lib.subtract(bptr, aptr, len(a))
```


# Summary

- External libraries can be interfaced in various ways
- cffi provides easy interfacing to C libraries
    - System libraries and user libraries
    - Python can take care of some datatype conversions
