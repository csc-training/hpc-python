from cffi import FFI
import numpy as np

ffi = FFI()
lib = ffi.dlopen('./libmyclib.so')
ffi.cdef("""
            void add(double *, double *, int);
            void subtract(double *, double *, int);
         """)

a = np.random.random(10)
b = np.ones_like(a)

# "pointer" objects
aptr = ffi.cast("double *", ffi.from_buffer(a))
bptr = ffi.cast("double *", ffi.from_buffer(b))

print("a:", a)
print("b:", b)
lib.add(aptr, bptr, len(a))
print("a + b", a)
