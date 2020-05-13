<!-- Title: Interfacing C code with CFFI -->

<!-- Short description:

In this article we discuss how external code written in C can be utilized
from Python code with the help of the CFFI package.

-->

# Interfacing C code with CFFI

Many high-performance libraries have nowadays also Python interfaces, and
can thus be used directly from Python code. However, sometimes one might want
to utilize a library that does not have a Python interface, or use own code
written in C or Fortran.

Python standard defines a
[C Application Programmer Interface (API)](https://docs.python.org/3/c-api/)
which is the most comprehensive way to interact with external code written in
C or C++. However, in many cases one can interact with C/C++ more easily by
using [CFFI](https://cffi.readthedocs.io) package or Cython. We start by
looking at how to use CFFI.

CFFI is an external package providing a C Foreign Function Interface for
Python. CFFI allows one to interact with almost any C code from Python.
However, C++ is not currently supported. User needs to add C-like declarations
to Python code and, even though the declarations can often be directly
copy-pasted from C headers or documentation, some understanding of C is
normally required.

CFFI has two different main modes, "ABI" and "API". In ABI mode one accesses
the library at binary level, while in API mode a separate compilation step
with a C compiler is used. ABI mode can be easier to start with, but API mode
is faster and more robust and is thus normally the recommended mode.


## Calling a C library function

For illustrating how to use CFFI in the API mode, let's see how one can call
functions from C math library within Python code. The approach works for any
shared object, i.e. .dll (Windows) or .so (Linux and others) or .dylib
(OS X). To start with, we create a Python file which we will call
**build_mymath.py**:

~~~python
from cffi import FFI
ffibuilder = FFI()

ffibuilder.cdef("""
    double sqrt(double x);  // list all the function prototypes from the
    double sin(double x);   // library that we want to use
                """)

# set_source() gives the name of the python extension module to
# produce, and some C source code as a string.  This C code needs
# to make the declarated functions, types and globals available,
# so it is often just the "#include".
ffibuilder.set_source("_my_math",
"""
     #include <math.h>   // the C header of the library
""",
   library_dirs = [],  # here we can provide where the library is located,
                       # as we are using C standard library empty list is enough
   libraries = ['m']   # name of the library we want to interface
)

ffibuilder.compile(verbose=True)
~~~

When we execute the script, CFFI creates a Python extension module, called
`_my_math` in this case, that exposes the selected functions:

~~~bash
$ python3 build_mymath.py
generating ./_mymath.c
running build_ext
building '_mymath' extension
gcc -pthread -Wno-unused-result -Wsign-compare -DDYNAMIC_ANNOTATIONS_ENABLED=1
-DNDEBUG -O2 -g -pipe -Wall -Wp,-D_FORTIFY_SOURCE=2 -fexceptions
-fstack-protector-strong --param=ssp-buffer-size=4 -grecord-gcc-switches -m64
-mtune=generic -D_GNU_SOURCE -fPIC -fwrapv -fPIC -I/usr/include/python3.6m -c
_mymath.c -o ./_mymath.o
gcc -pthread -shared -Wl,-z,relro -g ./_mymath.o -L/usr/lib64 -lm -lpython3.6m
-o ./_mymath.cpython-36m-x86_64-linux-gnu.so
~~~

We can now `import` the module, and use the functions we selected via the
`lib` handle:

~~~python
from _mymath import lib

a = lib.sqrt(4.5)
b = lib.sin(1.2)
~~~

The library functions assume C double precision numbers as input arguments,
but CFFI takes care of converting Python float objects into C numbers, as well
as converting the returned C doubles into Python floats.

## Creating Python extension from C source

Sometimes one might want to utilize direct C source code instead of an
existing library. Assume the above `sqrt` and `sin` functions would be
implemented in a file `mymath.c` instead of the C math library. Procedure for
generating the Python extension module is almost the same as before, the only
difference is that we provide the `sources` argument to the `set_source`
function. If the C code uses some libraries, these are still provided in the
`libraries` argument, and **build_mymath.py** could look like:

~~~python
from cffi import FFI
ffibuilder = FFI()

ffibuilder.cdef("""
    double sqrt(double x);   // list all the function prototypes from the
    double sin(double x);    // library that we want to use
                """)

# set_source() gives the name of the python extension module to
# produce, and some C source code as a string.  This C code needs
# to make the declarated functions, types and globals available,
# so it is often just the "#include".
ffibuilder.set_source("_my_math",
"""
    double sqrt(double x);   // we don't have a header, so function prototypes
    double sin(double x);    // are provided directly
""",
   sources = ['mymath.c'],
   library_dirs = [],
   libraries = ['m']   # if mymath utilizes math library we need to include it
                       # here
)

ffibuilder.compile(verbose=True)
~~~

## Passing NumPy arrays to external C code

Only simple scalar numbers can be automatically converted between Python
objects and C types. For more complex data structures such as NumPy arrays
some additional steps might be needed. In C, arrays are passed to functions
as pointers, and as the pointer does not have any information about the size
of the array, the size has to be normally passed as a separate argument.

Let us assume we have a C-function `add` which sums up two arrays and returns
the result in the third:

~~~c
// c = a + b
void add(double *a, double *b, double *c, int n)
{
  for (int i=0; i<n; i++)
     c[i] = a[i] + b[i];
}
~~~

If we want to use this function from Python, we can use CFFI for creating
an extension module just as previously. When we use the module and the
function, `cast` and `from_buffer` functions can be used for obtaining
pointers to the "data areas" of NumPy arrays:

~~~python
from add_module import ffi, lib

a = np.random.random((1000000,1))
b = np.random.random((1000000,1))
c = np.zeros_like(a)

# Pointer objects need to be passed to library
aptr = ffi.cast("double *", ffi.from_buffer(a))
bptr = ffi.cast("double *", ffi.from_buffer(b))
cptr = ffi.cast("double *", ffi.from_buffer(c))

lib.add(aptr, bptr, cptr, len(a))
~~~

Beware that `aptr`, `bptr` and `cptr` resemble now in many ways C pointers,
and if you deal carelessly with them you can get Segmentation faults!
