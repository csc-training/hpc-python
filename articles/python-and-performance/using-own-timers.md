# Using applications own timers

We discuss in this article how programmer can insert timing routines for
measuring time spent in spesific parts of a program.

By inserting spesific timing routines time spent in spesific parts of a
program can be measured.

In order to get a bigger picture about performance of a program it can be
useful to measure time spent in spesific region of the program. The region
can be whole function, or just a part of a function, and the region can
contain calls to other functions. In a typical usage pattern one obtains a
value from some "clock" (normally in units of seconds) in the beginning of the
region, and by reading from "clock" again in the end of region and subtracting
the two values one obtains the time spent in the region.

Python standard library has **time** module which provides various 
time-related function. In particular the `time.process_time` function can be
used for measuring spesific region:

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

~~~
$ python timing.py
Time spent 0.231697958
~~~

Many Python based simulation programs provide in the end of a run timing report
which is often generated with application's own timers, as an example a snippet 
from the output of quantum mechanical simulation software GPAW:

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

## Bonus: timing with context manager

Python context managers provide a nice feature for executing functions when
entering and exiting a region, the example below shows how one can utilize
context manager and `with` statement for timing part of a code. If you are
not familiar with context managers you can find more information [here](https://docs.python.org/3/reference/datamodel.html#context-managers).

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
