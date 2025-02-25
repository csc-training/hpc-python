# SPDX-FileCopyrightText: 2019 CSC - IT Center for Science Ltd. <www.csc.fi>
#
# SPDX-License-Identifier: MIT

from distutils.core import setup, Extension
from Cython.Build import cythonize

ext = Extension("fib",
                sources=["fib.pyx"],
               )

setup(
     ext_modules=cythonize(ext)
)

