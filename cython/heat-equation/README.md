## Optimising with Cython

### Type declarations
Create a `setup.py` file in order to speed up the heat equation solver with
Cython. Based on the profile in the previous exercise, insert static type
declarations to proper locations. Investigate the effect on performance. You
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

