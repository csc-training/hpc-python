from distutils.core import setup, Extension
from Cython.Build import cythonize

ext = Extension("evolve_cyt",
                sources=["evolve_cyt.pyx",],
                libraries=['evolve',],
                library_dirs=['.',])
setup(
     ext_modules=cythonize(ext)
)
