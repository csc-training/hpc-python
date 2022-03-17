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
    - tools for linear algebra, random numbers, *etc.*


# Numpy arrays

- All elements of an array have the same type
- Array can have multiple dimensions
- The number of elements in the array is fixed, shape can be changed


# Python list vs. NumPy array

![](img/list-vs-array.svg)


# Creating numpy arrays

From a list:
```python
>>> import numpy
>>> a = numpy.array((1, 2, 3, 4), float)
>>> a
array([ 1., 2., 3., 4.])

>>> list1 = [[1, 2, 3], [4,5,6]]
>>> mat = numpy.array(list1, complex)
>>> mat
array([[ 1.+0.j, 2.+0.j, 3.+0.j],
       [ 4.+0.j, 5.+0.j, 6.+0.j]])

>>> mat.shape
(2, 3)

>>> mat.size
6
```


# Helper functions for creating arrays: 1

- `arange` and `linspace` can generate ranges of numbers:

```python
>>> a = numpy.arange(10)
>>> a
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

>>> b = numpy.arange(0.1, 0.2, 0.02)
>>> b
array([0.1 , 0.12, 0.14, 0.16, 0.18])

>>> c = numpy.linspace(-4.5, 4.5, 5)
>>> c
array([-4.5 , -2.25, 0. , 2.25, 4.5 ])
```

# Helper functions for creating arrays: 2

- array with given shape initialized to `zeros`, `ones` or arbitrary
  value (`full`):

```python
>>> a = numpy.zeros((4, 6), float)
>>> a.shape
(4, 6)

>>> b = numpy.ones((2, 4))
>>> b
array([[ 1., 1., 1., 1.],
       [ 1., 1., 1., 1.]])
	   
>>> c = numpy.full((2, 3), 4.2)
>>> c
array([[4.2, 4.2, 4.2],
       [4.2, 4.2, 4.2]])
```

- Empty array (no values assigned) with `empty`

# Helper functions for creating arrays: 3

- Similar arrays as an existing one with `zeros_like`, `ones_like`, 
  `full_like` and `empty_like`:

```python
>>> a = numpy.zeros((4, 6), float)
>>> b = numpy.empty_like(a)
>>> c = numpy.ones_like(a)
>>> d = numpy.full_like(a, 9.1)
```

# Non-numeric data

- NumPy supports also storing non-numerical data e.g. strings (largest
  element determines the item size)

```python
>>> a = numpy.array(['foo', 'foo-bar'])
>>> a
array(['foo', 'foo-bar'], dtype='|U7')
```

- Character arrays can, however, be sometimes useful

```python
>>> dna = 'AAAGTCTGAC'
>>> a = numpy.array(dna, dtype='c')
>>> a
array([b'A', b'A', b'A', b'G', b'T', b'C', b'T', b'G', b'A', b'C'],
      dtype='|S1')
```


# Accessing arrays

<div class="column">
- Simple indexing:

```python
>>> mat = numpy.array([[1, 2, 3], [4, 5, 6]])
>>> mat[0,2]
3

>>> mat[1,-2]
5
```
</div>

<div class="column">
- Slicing:

```python
>>> a = numpy.arange(10)
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
</div>

# Slicing of arrays in multiple dimensions

- Multidimensional arrays can be sliced along multiple dimensions
- Values can be assigned to only part of the array
```python
>>> a = numpy.zeros((4, 4))
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
- Use `copy()` for real copying of arrays

```python
a = numpy.arange(10)
b = a              # reference, changing values in b changes a
b = a.copy()       # true copy

c = a[1:4]         # view, changing c changes elements [1:4] of a
c = a[1:4].copy()  # true copy of subarray
```


# Array manipulation

- `reshape` : change the shape of array

```python
>>> mat = numpy.array([[1, 2, 3], [4, 5, 6]])
>>> mat
array([[1, 2, 3],
       [4, 5, 6]])

>>> mat.reshape(3,2)
array([[1, 2],
       [3, 4],
       [5, 6]])
```

- `ravel` : flatten array to 1-d

```python
>>> mat.ravel()
array([1, 2, 3, 4, 5, 6])
```


# Array manipulation

- `concatenate` : join arrays together

```python
>>> mat1 = numpy.array([[1, 2, 3], [4, 5, 6]])
>>> mat2 = numpy.array([[7, 8, 9], [10, 11, 12]])
>>> numpy.concatenate((mat1, mat2))
array([[ 1, 2, 3],
       [ 4, 5, 6],
       [ 7, 8, 9],
       [10, 11, 12]])

>>> numpy.concatenate((mat1, mat2), axis=1)
array([[ 1, 2, 3,  7,  8,  9],
       [ 4, 5, 6, 10, 11, 12]])
```

- `split` : split array to N pieces

```python
>>> numpy.split(mat1, 3, axis=1)
[array([[1], [4]]), array([[2], [5]]), array([[3], [6]])]
```


# Array operations

- Most operations for numpy arrays are done element-wise
  (`+`, `-`,  `*`,  `/`,  `**`)

```python
>>> a = numpy.array([1.0, 2.0, 3.0])
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


# Summary

- Numpy provides a static array data structure
- Multidimensional arrays
- Fast mathematical operations for arrays
