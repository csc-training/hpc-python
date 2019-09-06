<!-- Title: Speeding up complex expressions with Numexpr -->

<!-- Short description:

In this article we show how to speed up complex expressions with Numexpr.

-->

# Numexpr

Complex expressions with large NumPy arrays present a bit of a catch-22
situation performance-wise.

On the one hand, using a one-liner for the expression is not a good idea due
to high memory usage (unnecessary temporary arrays that are need for the
evaluation).

On the other hand, evaluation of the expression with one operation at a time
can lead into suboptimal performance. Effectively, one carries out multiple
*for* loops in the NumPy C-code.

Numexpr package provides tools for fast evaluation of array expressions.

~~~python
x = numpy.random.random((1000000, 1))
y = numpy.random.random((1000000, 1))

import numexpr
poly = numexpr.evaluate("((.25*x + .75)*x - 1.5)*x - 2")
~~~

The expression is enclosed in quotes and will be evaluated using a single
C-loop. Speed-ups in comparison to NumPy are typically between 0.95 and 4.
Performance improves normaly most with arrays that do not fit in CPU cache.

Supported operators and functions include e.g.:

  - +, -, \*, /, \*\*
  - sin, cos, tan
  - exp, log, sqrt

## Thread support

By default, *numexpr* tries to use multiple threads, which can also speed up
the execution. The number of threads can be queried and set with:

~~~python
numexpr.set_num_threads(n)
~~~

The number of threads can also be controlled by the environment variables
`OMP_NUM_THREADS` or `NUMEXPR_NUM_THREADS`.
