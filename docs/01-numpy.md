---
title:  Numpy basics
lang:   en
---

# Numpy – fast array interface

- Standard Python is not well suitable for numerical computations
    - lists are very flexible but also slow to process in numerical
      computations

- Numpy adds a new **array** data type
    - static, multidimensional
    - fast processing of arrays
    - some linear algebra, random numbers


# Numpy arrays

- All elements of an array have the same type
- Array can have multiple dimensions
- The number of elements in the array is fixed, shape can be changed


# Python list vs. NumPy array

TODO: insert pic


# Creating numpy arrays

From a list:
```python
>>> import numpy as np
>>> a = np.array((1, 2, 3, 4), float)
>>> a
array([ 1., 2., 3., 4.])

>>> list1 = [[1, 2, 3], [4,5,6]]
>>> mat = np.array(list1, complex)
>>> mat
array([[ 1.+0.j, 2.+0.j, 3.+0.j],
       [ 4.+0.j, 5.+0.j, 6.+0.j]])

>>> mat.shape
(2, 3)

>>> mat.size
6
```


# Creating numpy arrays

More ways for creating arrays:
```python
>>> import numpy as np
>>> a = np.arange(10)
>>> a
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

>>> b = np.linspace(-4.5, 4.5, 5)
>>> b
array([-4.5 , -2.25, 0. , 2.25, 4.5 ])

>>> c = np.zeros((4, 6), float)
>>> c.shape
(4, 6)

>>> d = np.ones((2, 4))
>>> d
array([[ 1., 1., 1., 1.],
       [ 1., 1., 1., 1.]])
```


# Non-numeric data

- NumPy supports also storing non-numerical data e.g. strings (largest
  element determines the item size)

```python
>>> a = np.array(['foo', 'foo-bar'])
>>> a
array(['foo', 'foo-bar'], dtype='|U7')
```

- Character arrays can, however, be sometimes useful

```python
>>> dna = 'AAAGTCTGAC'
>>> a = np.array(dna, dtype='c')
>>> a
array([b'A', b'A', b'A', b'G', b'T', b'C', b'T', b'G', b'A', b'C'],
      dtype='|S1')
```


# Indexing of arrays

```python
>>> mat = np.array([[1, 2, 3], [4, 5, 6]])
>>> mat[0,2]
3

>>> mat[1,-2]
5
```

# Slicing of arrays

```python
>>> a = np.arange(10)
>>> a[2:]
array([2, 3, 4, 5, 6, 7, 8, 9])

>>> a[:-1]
array([0, 1, 2, 3, 4, 5, 6, 7, 8])

>>> a[1:3] = -1
>>> a
array([0, -1, -1, 3, 4, 5, 6, 7, 8, 9])

>>> a[1:7:2]
array([1, 3, 5])
```


# Slicing of arrays in multiple dimensions

```python
>>> a = np.zeros((4, 4))
>>> a[1:3, 1:3] = 2.0
>>> a
array([[ 0., 0., 0., 0.],
       [ 0., 2., 2., 0.],
       [ 0., 2., 2., 0.],
       [ 0., 0., 0., 0.]])
```


# Views and copies of arrays

- Simple assignment creates references to arrays
- Slicing creates "views" to the arrays
- Use copy() for real copying of arrays

```python
a = np.arange(10)
b = a              # reference, changing values in b changes a
b = a.copy()       # true copy

c = a[1:4]         # view, changing c changes elements [1:4] of a
c = a[1:4].copy()  # true copy of subarray
```


# Array manipulation

- reshape : change the shape of array

```python
>>> mat = np.array([[1, 2, 3], [4, 5, 6]])
>>> mat
array([[1, 2, 3],
       [4, 5, 6]])

>>> mat.reshape(3,2)
array([[1, 2],
       [3, 4],
       [5, 6]])
```

- ravel : flatten array to 1-d

```python
>>> mat.ravel()
array([1, 2, 3, 4, 5, 6])
```


# Array manipulation

- concatenate : join arrays together

```python
>>> mat1 = np.array([[1, 2, 3], [4, 5, 6]])
>>> mat2 = np.array([[7, 8, 9], [10, 11, 12]])
>>> np.concatenate((mat1, mat2))
array([[ 1, 2, 3],
       [ 4, 5, 6],
       [ 7, 8, 9],
       [10, 11, 12]])

>>> np.concatenate((mat1, mat2), axis=1)
array([[ 1, 2, 3,  7,  8,  9],
       [ 4, 5, 6, 10, 11, 12]])
```

- split : split array to N pieces

```python
>>> np.split(mat1, 3, axis=1)
[array([[1], [4]]), array([[2], [5]]), array([[3], [6]])]
```


# Array operations

- Most operations for numpy arrays are done element-wise
  (+  -  \*  /  \*\*)

```python
>>> a = np.array([1.0, 2.0, 3.0])
>>> b = 2.0
>>> a * b
array([ 2., 4., 6.])

>>> a + b
array([ 3., 4., 5.])

>>> a * a
array([ 1., 4., 9.])
```

# Array operations

- Numpy has special functions which can work with array arguments
  (sin, cos, exp, sqrt, log, ...)

```python
>>> import numpy, math
>>> a = numpy.linspace(-math.pi, math.pi, 8)
>>> a
array([-3.14159265, -2.24399475, -1.34639685, -0.44879895,
        0.44879895,  1.34639685,  2.24399475,  3.14159265])

>>> numpy.sin(a)
array([ -1.22464680e-16, -7.81831482e-01, -9.74927912e-01,
        -4.33883739e-01,  4.33883739e-01,  9.74927912e-01,
         7.81831482e-01,  1.22464680e-16])

>>> math.sin(a)
Traceback (most recent call last):
  File "<stdin>", line 1, in ?
TypeError: only length-1 arrays can be converted to Python scalars
```


# Numpy tools { .section }


# I/O with Numpy

- Numpy provides functions for reading data from file and for writing data
  into the files
- Simple text files
    - numpy.loadtxt
    - numpy.savetxt
    - Data in regular column layout
    - Can deal with comments and different column delimiters


# Random numbers

- The module numpy.random provides several functions for constructing
  random arrays
    - random: uniform random numbers
    - normal: normal distribution
    - choice: random sample from given array
    - ...

```python
>>> import numpy.random as rnd
>>> rnd.random((2,2))
array([[ 0.02909142, 0.90848 ],
       [ 0.9471314 , 0.31424393]])

>>> rnd.choice(np.arange(4), 10)
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
>>> x = np.linspace(-4, 4, 7)
>>> y = x**2 + rnd.random(x.shape)
>>>
>>> p = np.polyfit(x, y, 2)
>>> p
array([ 0.96869003, -0.01157275, 0.69352514])
```


# Linear algebra

- Numpy can calculate matrix and vector products efficiently: `dot`,
  `vdot`, ...
- Eigenproblems: `linalg.eig`, `linalg.eigvals`, ...
- Linear systems and matrix inversion: `linalg.solve`, `linalg.inv`

```python
>>> A = np.array(((2, 1), (1, 3)))
>>> B = np.array(((-2, 4.2), (4.2, 6)))
>>> C = np.dot(A, B)
>>>
>>> b = np.array((1, 2))
>>> np.linalg.solve(C, b) # solve C x = b
array([ 0.04453441, 0.06882591])
```


# Linear algebra

- Normally, NumPy utilises high performance libraries in linear algebra
  operations
- Example: matrix multiplication C = A * B matrix dimension 200
    - pure python: 5.30 s
    - naive C:     0.09 s
    - numpy.dot:   0.01 s


# Numpy advanced topics { .section }


# Anatomy of NumPy array

- **ndarray** type is made of
    - one dimensional contiguous block of memory (raw data)
    - indexing scheme: how to locate an element
    - data type descriptor: how to interpret an element

TODO: add pic


# NumPy indexing

- There are many possible ways of arranging items of N-dimensional
  array in a 1-dimensional block
- NumPy uses **striding** where N-dimensional index ($n_0, n_1, ..., n_{N-1}$)
  corresponds to offset from the beginning of 1-dimensional block

TODO: add pic 


# ndarray attributes

`a = np.array(...)`
  : `a.flags`
    : various information about memory layout

    `a.strides`
    : bytes to step in each dimension when traversing

    `a.itemsize`
    : size of one array element in bytes

    `a.data`
    : Python buffer object pointing to start of arrays data

    `a.__array_interface__`
    : Python internal interface


# Advanced indexing

- Numpy arrays can be indexed also with other arrays (integer or
  boolean)

```python
>>> x = np.arange(10,1,-1)
>>> x
array([10, 9, 8, 7, 6, 5, 4, 3, 2])

>>> x[np.array([3, 3, 1, 8])]
array([7, 7, 9, 2])
```

- Boolean "mask" arrays

```python
>>> m = x > 7
>>> m
array([ True, True, True, False, False, ...

>>> x[m]
array([10, 9, 8])
```

- Advanced indexing creates copies of arrays


# Vectorized operations

- `for` loops in Python are slow
- Use "vectorized" operations when possible
- Example: difference  (TODO: add pic)
    - for loop is ~80 times slower!

```python
# brute force using a for loop
arr = np.arange(1000)
dif = np.zeros(999, int)
for i in range(1, len(arr)):
    dif[i-1] = arr[i] - arr[i-1]

# vectorized operation
arr = np.arange(1000)
dif = arr[1:] - arr[:-1]
```


# Broadcasting

- If array shapes are different, the smaller array may be broadcasted
  into a larger shape

```python
>>> from numpy import array
>>> a = array([[1,2],[3,4],[5,6]], float)
>>> a
array([[ 1., 2.],
       [ 3., 4.],
       [ 5., 6.]])

>>> b = array([[7,11]], float)
>>> b
array([[ 7., 11.]])

>>> a * b
array([[ 7., 22.],
       [ 21., 44.],
       [ 35., 66.]])
```


# Broadcasting

- Example: calculate distances from a given point

```python
# array containing 3d coordinates for 100 points
points = np.random.random((100, 3))
origin = np.array((1.0, 2.2, -2.2))
dists = (points - origin)**2
dists = np.sqrt(np.sum(dists, axis=1))

# find the most distant point
i = np.argmax(dists)
print(points[i])
```


# Temporary arrays

- In complex expressions, NumPy stores intermediate values in
  temporary arrays
- Memory consumption can be higher than expected

```python
a = np.random.random((1024, 1024, 50))
b = np.random.random((1024, 1024, 50))

# two temporary arrays will be created
c = 2.0 * a - 4.5 * b

# three temporary arrays will be created due to unnecessary parenthesis
c = (2.0 * a - 4.5 * b) + 1.1 * (np.sin(a) + np.cos(b))
```

TODO: fix missing brackets (temp1, temp2)


# Temporary arrays

- Broadcasting approaches can lead also to hidden temporary arrays
- Example: pairwise distance of **M** points in 3 dimensions
    - Input data is M x 3 array
    - Output is M x M array containing the distance between points i and j

```python
X = np.random.random((1000, 3))
D = np.sqrt(((X[:, np.newaxis, :] - X) ** 2).sum(axis=-1))
```

TODO: fix missing bracket (Temporary 1000 x 1000 x 3 array)


# Numexpr

- Evaluation of complex expressions with one operation at a time can lead
  also into suboptimal performance
    - Effectively, one carries out multiple *for* loops in the NumPy
      C-code

- Numexpr package provides fast evaluation of array expressions

```python
import numexpr as ne
x = np.random.random((1000000, 1))
y = np.random.random((1000000, 1))
poly = ne.evaluate("((.25*x + .75)*x - 1.5)*x - 2")
```


# Numexpr

- By default, numexpr tries to use multiple threads
- Number of threads can be queried and set with
  `ne.set_num_threads(nthreads)`
- Supported operators and functions:
  +,-,\*,/,\*\*, sin, cos, tan, exp, log, sqrt
- Speedups in comparison to NumPy are typically between 0.95 and 4
- Works best on arrays that do not fit in CPU cache


# Summary

- Numpy provides a static array data structure
- Multidimensional arrays
- Fast mathematical operations for arrays
- Tools for linear algebra and random numbers
- Arrays can be broadcasted into same shapes
- Expression evaluation can lead into temporary arrays
