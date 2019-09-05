<!-- Title: Measuring small code snippets with timeit -->

<!-- Short description:

In this article we discuss how the Python timeit module can help in
measuring very short execution times

-->

# Measuring small code snippets with timeit

Measuring very short execution times has some pitfalls that can be avoided
with the help of the `timeit` Python module.

Sometimes one might be interested in measuring the performance of a very
small bit of Python code, such as a single statement or a function call.
Measuring reliably very short execution times can be challenging, and one
needs typically to gather some statistics for error estimates.

In order to avoid common traps in such a measurement, Python standard library
contains the `timeit` module. The module can be used from the command line,
within a program, or within an interactive interpreter (especially convenient
with IPython) or in Jupyter notebooks. When a code snippet is measured with
`timeit`, the module takes care of running the snippet several times and
calculating statistics.

The example below utilizes the IPython interpreter; more information about
the `timeit` module can be found in the
[Python documentation](https://docs.python.org/3/library/timeit.html).

IPython interpreter provides a special magic command `%timeit`, which will
measure the statement following it using the `timeit` module. In the
following example, we compare the execution time of `sin` and `cos` functions
with the same input:

~~~
IPython 6.1.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: from math import sin, cos

In [2]: %timeit sin(0.2)
68.8 ns ± 0.181 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)

In [3]: %timeit cos(0.2)
71.1 ns ± 1.57 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)
~~~

As can be seen, with `timeit` each measurement consist of a huge number of
evaluations (10000000 loops), and the measurent is even repeated multiple
times (7 runs) for better statistics.
