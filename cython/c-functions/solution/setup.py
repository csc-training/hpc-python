from distutils.core import setup, Extension
from Cython.Build import cythonize

ext = Extension("fib",
                sources=["fib.pyx"],
               )

setup(
     ext_modules=cythonize(ext)
)

