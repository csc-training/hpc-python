## Optimising with Cython

### Creating a Cython extension
Based on the profile in the performance measurement [exercise](../../performance/cprofile) 
write a `setup.py` for creating a Cython module for the most time consuming part of the heat equation solver. 
If you did not finish the profiling exercise, you can look at example profile [here](profile.md).

### Type declarations
Insert static type declarations to proper locations. Investigate the effect on performance. You
can use applications own timers and/or **timeit**. Annotated HTML-report with
`cython –a …` can be useful when tuning performance

### C-functions, fast indexing and directives

Continue optimising the code by reducing function call overhead, utilizing
fast array indexing and including compiler directives. When finished with the
optimisation, compare performance to Python/NumPy model solution (in
[numpy/heat-equation](../../numpy/heat-equation)), which uses array
operations. You can play around also with larger input data as provided in
[bottle_medium.dat](bottle_medium.dat) and
[bottle_large.dat](bottle_large.dat).

