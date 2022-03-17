---
title:  Numpy tools
lang:   en
---


# Numpy tools

- NumPy contains ready to use tools for many common tasks
- I/O
- Random numbers
- Polynomials
- Linear algebra


# I/O with Numpy

- Numpy provides functions for reading data from file and for writing data
  into the files
- Simple text files
    - `numpy.loadtxt`
    - `numpy.savetxt`
    - Data in regular column layout
    - Can deal with comments and different column delimiters


# Random numbers

- The module `numpy.random` provides several functions for constructing
  random arrays
    - `random`: uniform random numbers
    - `normal`: normal distribution
    - `choice`: random sample from given array
    - ...

```python
>>> import numpy.random as rnd
>>> rnd.random((2,2))
array([[ 0.02909142, 0.90848 ],
       [ 0.9471314 , 0.31424393]])

>>> rnd.choice(numpy.arange(4), 10)
array([0, 1, 1, 2, 1, 1, 2, 0, 2, 3])
```


# Polynomials

- Polynomial is defined by an array of coefficients p
  $p(x, N) = p[0] x^{N-1} + p[1] x^{N-2} + ... + p[N-1]$
- For example:
    - Least square fitting: `numpy.polyfit`
    - Evaluating polynomials: `numpy.polyval`
    - Roots of polynomial: `numpy.roots`

```python
>>> x = numpy.linspace(-4, 4, 7)
>>> y = x**2 + rnd.random(x.shape)
>>>
>>> p = numpy.polyfit(x, y, 2)
>>> p
array([ 0.96869003, -0.01157275, 0.69352514])
```


# Linear algebra

- Numpy can calculate matrix and vector products efficiently: `dot`,
  `vdot`, ...
- Eigenproblems: `linalg.eig`, `linalg.eigvals`, ...
- Linear systems and matrix inversion: `linalg.solve`, `linalg.inv`

```python
>>> A = numpy.array(((2, 1), (1, 3)))
>>> B = numpy.array(((-2, 4.2), (4.2, 6)))
>>> C = numpy.dot(A, B)
>>>
>>> b = numpy.array((1, 2))
>>> numpy.linalg.solve(C, b) # solve C x = b
array([ 0.04453441, 0.06882591])
```


# Linear algebra

- Normally, NumPy utilises high performance libraries in linear algebra
  operations
- Example: matrix multiplication C = A * B matrix dimension 1000
    - pure python:           522.30 s
    - naive C:                 1.50 s
    - numpy.dot:               0.04 s
    - library call from C:     0.04 s



# Summary

- NumPy contains many useful tools for numerical computing
- [Scipy](https://scipy.org/) includes even wider set of utilities for
  scientific computing
- Further useful packages
    - Visualization: [matplotlib](https://matplotlib.org/),
      [Mayavi](https://docs.enthought.com/mayavi/mayavi/)
    - Data analysis: [pandas](https://pandas.pydata.org/)
