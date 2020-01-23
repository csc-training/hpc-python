## Optimising heat equation with Cython

### Creating a Cython extension

Write a `setup.py` for creating a Cython version of [heat.py](heat.py)
module, and use it from the main program [heat_main.py](heat_main.py).
How much does simple Cythonization (i.e. diminishing the interpreting
overhead) improve the performance?

### Optimising

Based on the profile in the performance measurement
[exercise](../../performance/cprofile) optimise the most time
consuming part of the algorithm. If you did not finish the profiling
exercise, you can look at example profile [here](profile.md). 

Utilize all the tricks you have learned so far (type declarations,
fast array indexing, compiler directives, C functions, ...).

Investigate how the different optimizations affect the performance. You
can use applications own timers and/or **timeit**. Annotated HTML-report with
`cython -a …` can be useful when tuning performance.

When finished with the optimisation, compare performance to
Python/NumPy model solution (in
[numpy/heat-equation](../../numpy/heat-equation)), which uses array 
operations. You can play around also with larger input data as provided in
[bottle_medium.dat](bottle_medium.dat) and [bottle_large.dat](bottle_large.dat).

