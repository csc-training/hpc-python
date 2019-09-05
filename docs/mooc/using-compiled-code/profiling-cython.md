<!-- Title: Profiling Cython -->

<!-- Short description:

By default, Cython code does not show up when using cProfile. In this article
we discuss how to enable profiling for Cython code.

-->

# Profiling Cython

As the first rule of optimization is to measure performance before starting
any optimization work, one should have made profile of the pure Python code
before starting any Cythonization. However, in the next optimization cycle
one should profile also the Cython code.

By default, Cython code does not show up in the measurements of cProfile. One
can, however, enable profiling either for the whole module or for individual
functions. In order to enable profiling for the whole function, simply
include a global directive at the top of a file:

~~~ python
# cython: profile=True

import numpy as np

def myfunc():
...
~~~

In order to enable profiling for a single function, one can include the
cython decorator before a function definition:

~~~ python
cimport cython

@cython.profile(True)
def my_func():
    ...
~~~

As profiling adds always some overhead, small functions that are called very
frequently can mess up the profile. In these cases one can use the decorator
for disabling profiling for some functions (if profiling is enabled for the
whole module).

~~~ python
# cython: profile=True
cimport cython

@cython.profile(False)
def my_func_not_to_profile():
    ...
~~~
