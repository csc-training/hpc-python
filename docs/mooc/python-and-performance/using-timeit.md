# Measuring small code snippets with timeit

In this article we discuss how the Python timeit module can help in
very short execution times

Measuring very small durations of program contains some pitfalls, which can be
avoided with the help of Python timeit module.

Sometimes one might be interested in measuring  the performance of very small
bits of Python code, such as single statements or function calls. Measuring
reliable very short durations can be challenging, and one needs typically at
minimum at least some statistics and error estimates.

In order to avoid common traps in such a measurements, Python standard library
contains the `timeit` module. The module can be used from the command line, 
within a program, or within a interactive interpreter (especially convenient 
with IPython) or in Jupyter notebooks. When code snippet is measured with 
`timeit`, the module takes care of running the snippet several times and 
calculating also statistics. 

The example below utilizes the IPython interpreter, more information about the
`timeit` module can be found from [Python documentation](https://docs.python.org/3/library/timeit.html).

IPython interpreter provides a special magic command `%timeit` which will 
measure the statement following it using the `timeit` module. In the following
we compate the execution time of `sin` and `cos` functions with the same input:

~~~
IPython 6.1.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: from math import sin, cos

In [2]: %timeit sin(0.2)
68.8 ns ± 0.181 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)

In [3]: %timeit cos(0.2)
71.1 ns ± 1.57 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)
~~~

As seen, `timeit` each measurement consist of huge number of evaluations, and
the measurent is repeated for statistics.

