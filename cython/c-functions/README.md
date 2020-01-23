## Using C-functions

Fibonacci numbers are a sequence of integers defined by the recurrence 
relation 
   
   F<sub>n</sub> = F<sub>n-1</sub> + F<sub>n-2</sub>
 
with the initial values F<sub>0</sub>=0, F<sub>1</sub>=1.

The module [fib.py](fib.py) contains a function `fibonacci(n)` that
calculates recursively F<sub>n</sub>. The function can be used e.g. as

```python
from fib import fibonacci

fibonacci(30)
```

Make a Cython version of the module, and investigate how adding type
information and making `fibonacci` a C-function affects performance
(hint: function needs to be called both from Python and C). Use
`timeit` for performance measurements, either from command line

```bash
$ python3 -m timeit -s "from fib import fibonacci" "fibonacci(30)"
```

or within IPython

```python
In []: %timeit fibonacci(30)
```

**Note:** this recursive algorithm is very inefficient way of calculating
Fibonacci numbers and pure Python implemention of better algorithm
outperforms Cython implementation drastically.
