<!-- Title: Interfacing C code with Cython -->

<!-- Short description:

In this article we discuss how external code written in C can be utilized
from Python code with the help of Cython.

-->

# Interfacing C code with Cython

As Cython code compiles down to C code, it is relatively straightforward to
utilize also Cython for interfacing with C.

In order to use C functions and variables from the library, one must provide
external declarations for them in the Cython .pyx file. While normal `cdef`
declarations refer to functions and variables that are defined in the same
file, by adding `extern` keyword one can specify that they are defined
elsewhere. As an example, by having in a .pyx file the statement

~~~python
cdef extern void add(double *a, double *b, double *c, int n)
~~~

one could call `add` function within that file. In addition, the actual
library or source implementing the function needs to be included in 
**setup.py** when building the extension module with Cython.

With the above construct, Cython will add the declaration to the generated
.c file. However, when using libraries it is preferable to have the actual
library header included in the generated file. This can be achieved with the
following construct:

~~~python
cdef extern from "mylib.h"
    void add(double *a, double *b, double *c, int n)
    void subtract(double *a, double *b, double *c, int n)
~~~

Now, **mylib.h** header is included in the generated .c file, while the
statements in the following block specify that functions `add` and `subtract`
can be used within the .pyx file. It is important to understand that Cython
does not itself read the C header file, so you still need to provide
declarations from it that you use.


## Including the library in setup.py

Compared to building simple pure Cython modules, one has to provide some
extra information in the **setup.py**. If the code to be interfaced is in a
library (i.e. .so) one can use the following type of **setup.py**:

~~~python
from distutils.core import setup, Extension
from Cython.Build import cythonize

ext = Extension("module_name",
                sources=["cython_source.pyx",],
                libraries=["name",], # Cython module is linked against
                library_dirs=[".",]) # libname.so, looked in "."

setup(ext_modules=cythonize(ext))
~~~

One can also use direct C source files if more appropriate:

~~~python
from distutils.core import setup, Extension
from Cython.Build import cythonize

# Specify all sources in Extension object
ext = Extension("module_name",
                sources=["cython_source.pyx", "c_source.c"])

setup(ext_modules=cythonize(ext))
~~~


## Passing NumPy arrays from Cython to C

Similarly as when using CFFI to pass NumPy arrays into C, also in the case of
Cython one needs to be able to pass a pointer to the "data area" of an array.
For arrays that are declared as type of `ndarray`, Cython supports similar
`&` syntax as in C:

~~~
import numpy as np
cimport numpy as np

cdef extern from "myclib.h":

    void add(double *a, double *b, double *c, int n)

    void subtract(double *a, double *b, double *c, int n)

def add_py(np.ndarray[cnp.double_t,ndim=1] a,
           np.ndarray[cnp.double_t,ndim=1] b):

    add(&a[0], &b[0], &c[0], len(a))
~~~
