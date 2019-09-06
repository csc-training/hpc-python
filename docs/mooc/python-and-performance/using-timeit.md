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


## Using timeit with IPython

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

## Using timeit from command line

The `timeit` module can be used also from command line. The expression to be
measured is given as string, and possible setup (e.g. module import) is
provided with **-s** argument:

~~~bash
python3 -m timeit -s "from math import sin" "sin(0.2)"
10000000 loops, best of 3: 0.052 usec per loop
~~~

The setup statement (`from math import sin`) above is executed once initially,
and the actual statement then multiple times.

Whole Python scripts cannot be directly measured, but if the script provides
e.g. a `main` function it can be measured. For larger entities one might want
to specify also how many times the statement is executed with **-n** argument:

~~~bash
python3 -m timeit -n 3 -s "from mandel_main import main" "main()"
3 loops, best of 3: 569 msec per loop
~~~

In above, a single measurement consists of three evaluations of `main` and the 
measurement is then repeated three times.

The `timeit` module can be used also directly inside scripts, more information
can be found in the [Documentation of timeit](https://docs.python.org/3/library/timeit.html).
