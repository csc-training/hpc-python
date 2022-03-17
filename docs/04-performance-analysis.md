---
title:  Performance analysis
lang:   en
---

# Performance measurement {.section}

# Measuring application performance

- Correctness is the most import factor in any application
    - Premature optimization is the root of all evil\!
- Before starting to optimize application, one should measure where time is
  spent
    - Typically 90 % of time is spent in 10 % of application

<div class=column>
- Mind the algorithm!
    - Recursive calculation of Fibonacci numbers
</div>

<div class=column>

<small>

|                                |   Speedup |
|--------------------------------|-----------|
| Pure Python                    | 1         |
| Pure C                         | 126       |
| Pure Python (better algorithm) | 24e6      |

</small>

</div>



# Measuring application performance

- Applications own timers
- **timeit** module
- **cProfile** module
- Full fedged profiling tools: TAU, Intel Vtune, Python Tools for Visual
  Studio ...


# Measuring application performance

- Python **time** module can be used for measuring time spent in specific
  part of the program
    - `time.perf_counter()` : include time spent in other processes
	- `time.process_time()` : only time in current process

```python
import time

t0 = time.process_time()
for n in range(niter):
    heavy_calculation()
t1 = time.process_time()

print('Time spent in heavy calculation', t1-t0)
```


# timeit module

- Easy timing of small bits of Python code
- Tries to avoid common pitfalls in measuring execution times
- Command line interface and Python interface
- `%timeit` magic in IPython

```python
In [1]: from mymodule import func
In [2]: %timeit func()

10 loops, best of 3: 433 msec per loop
```
```bash
$ python -m timeit -s "from mymodule import func" "func()"

10 loops, best of 3: 433 msec per loop
```


# cProfile

- Execution profile of Python program
    - Time spent in different parts of the program
    - Call graphs
- Python API:
- Profiling whole program from command line

```python
import cProfile
...

# profile statement and save results to a file func.prof
cProfile.run('func()', 'func.prof')
```
```bash
$ python -m cProfile -o myprof.prof myprogram.py
```


# Investigating profile with pstats

- Printing execution time of selected functions
- Sorting by function name, time, cumulative time, ...
- Python module interface and interactive browser

<div class="column">

```
In [1]: from pstats import Stats
In [2]: p = Stats('myprof.prof')
In [3]: p.strip_dirs()
In [4]: p.sort_stats('time')
In [5]: p.print_stats(5)

Mon Oct 12 10:11:00 2016 my.prof
...
```

</div>
<div class="column">

```bash
$ python -m pstats myprof.prof

Welcome to the profile statistics
% strip
% sort time
% stats 5

Mon Oct 12 10:11:00 2016 my.prof
...
```

</div>


# Summary

- Python has various built-in tools for measuring application performance
- **time** module
- **timeit** module
- **cProfile** and **pstats** modules
