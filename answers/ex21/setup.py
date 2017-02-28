from distutils.core import setup, Extension
from Cython.Build import cythonize

ext = Extension("evolve_cyt",
                sources=["evolve_cyt.pyx", "evolve.c"])
setup(
     ext_modules=cythonize(ext)
)
