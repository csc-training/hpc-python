---
title:  Python and High-Performance Computing
lang:   en
---

# Efficiency

- Python is an interpreted language
    - no pre-compiled binaries, all code is translated on-the-fly to
      machine instructions
    - byte-code as a middle step which may be stored (.pyc)

- All objects are dynamic in Python
    - nothing is fixed == optimisation nightmare
    - lot of overhead from metadata

- Flexibility is good, but comes with a cost!


# Improving Python performance

- Array based computations with NumPy
- Using extended Cython programming language
- Embed compiled code in a Python program
    - C/C++, Fortran
- Utilize parallel processing


# Parallelisation strategies for Python

- Global Interpreter Lock (GIL)
    - CPython's memory management is not thread-safe
    - no threads possible, except for I/O etc.
    - affects overall performance of threading

- Process-based "threading" with multiprocessing
    - fork independent processes that have a limited way to communicate

- **Message-passing** is the Way to Go to achieve true parallelism in Python
