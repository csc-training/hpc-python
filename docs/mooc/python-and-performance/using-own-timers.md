<!-- Title: Using applications own timers -->

<!-- Short description:

We discuss in this article how you can insert timing routines for measuring
the time spent in a specific part of a program.

-->

# Using applications own timers

By inserting timing routines to a program, the time spent in specific parts
of the program can be measured.

In order to get a bigger picture of the performance of a program, it can be
useful to measure the time spent in a specific region of the program. The
region can be a function, or just a part of a function, and the region can
contain calls to other functions. In a typical usage pattern one obtains a
value from some "clock" (normally in units of seconds) at the beginning and
end of the region and by subtracting the two values one obtains the time spent
in the region.

Python standard library has a **time** module which provides various
time-related functions. In particular the `time.process_time` function can be
used for measuring a specific region:

~~~python
from math import exp, sin
import time

def calculate(a):
    result = 0
    for val in a:
        result += exp(val) * sin(val)
    return result

x = [0.1 * i for i in range(1000)]
t0 = time.process_time()
for r in range(1000):
    calculate(x)
t1 = time.process_time()
print("Time spent", t1 - t0)
~~~

~~~bash
$ python timing.py
Time spent 0.231697958
~~~

Many Python based simulation programs provide at the end of a run a timing
report, which is often generated with application's own timers. As an example
a snippet from the output of quantum mechanical simulation software GPAW:

~~~
...
 Hamiltonian:                         3.195     0.012   0.2% |
  Atomic:                             0.477     0.084   1.7% ||
   XC Correction:                     0.393     0.393   7.8% |--|
  Communicate energies:               0.001     0.001   0.0% |
  Hartree integrate/restrict:         0.064     0.064   1.3% ||
  Poisson:                            1.670     1.670  33.3% |------------|
  XC 3D grid:                         0.958     0.958  19.1% |-------|
...
~~~

## Bonus: timing with a context manager

Python context managers provide a nice feature for executing functions when
entering and exiting a region. The example below shows how one can utilize
a context manager and the `with` statement for timing a part of a code. If you
are not familiar with context managers you can find more information
[here](https://docs.python.org/3/reference/datamodel.html#context-managers).

~~~python
from math import exp, sin
import time

class Timer:
    def __enter__(self):
        self.start = time.process_time()
        return self

    def __exit__(self, *args):
        self.end = time.process_time()
        self.interval = self.end - self.start

def calculate(a):
    result = 0
    for val in a:
        result += exp(val) * sin(val)
    return result

x = [0.1 * i for i in range(1000)]
with Timer() as t:
    for r in range(1000):
        calculate(x)
print("Time spent", t.interval)
~~~
