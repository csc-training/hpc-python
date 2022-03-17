---
title:  Advanced concepts in NumPy
lang:   en
---


# Anatomy of NumPy array

- **ndarray** type is made of
    - one dimensional contiguous block of memory (raw data)
    - indexing scheme: how to locate an element
    - data type descriptor: how to interpret an element

![](img/ndarray-in-memory.svg){.center width=50%}


# NumPy indexing

- There are many possible ways of arranging items of N-dimensional
  array in a 1-dimensional block
- NumPy uses **striding** where N-dimensional index ($n_0, n_1, ..., n_{N-1}$)
  corresponds to offset from the beginning of 1-dimensional block
  
$$
offset = \sum_{k=0}^{N-1} s_k n_k, s_k \text{ is stride in dimension k}
$$


![](img/ndarray-in-memory-offset.svg){.center width=50%}

# ndarray attributes

`a = numpy.array(...)`
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
>>> x = numpy.arange(10,1,-1)
>>> x
array([10, 9, 8, 7, 6, 5, 4, 3, 2])

>>> x[numpy.array([3, 3, 1, 8])]
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
- Example: difference
    - for loop is ~80 times slower!

<div class="column">
```python
# brute force using a for loop
arr = numpy.arange(1000)
dif = numpy.zeros(999, int)
for i in range(1, len(arr)):
    dif[i-1] = arr[i] - arr[i-1]

# vectorized operation
arr = numpy.arange(1000)
dif = arr[1:] - arr[:-1]
```
</div>

<div class="column">
![](img/vectorised-difference.svg){.center width=90%}
</div>

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
points = numpy.random.random((100, 3))
origin = numpy.array((1.0, 2.2, -2.2))
dists = (points - origin)**2
dists = numpy.sqrt(numpy.sum(dists, axis=1))

# find the most distant point
i = numpy.argmax(dists)
print(points[i])
```


# Temporary arrays

- In complex expressions, NumPy stores intermediate values in
  temporary arrays
- Memory consumption can be higher than expected

```{.python emphasize=5:5-5:11,5:15-5:21}
a = numpy.random.random((1024, 1024, 50))
b = numpy.random.random((1024, 1024, 50))

# two temporary arrays will be created
c = 2.0 * a - 4.5 * b

# three temporary arrays will be created due to unnecessary parenthesis
c = (2.0 * a - 4.5 * b) + 1.1 * (numpy.sin(a) + numpy.cos(b))
```


# Temporary arrays

- Broadcasting approaches can lead also to hidden temporary arrays
- Example: pairwise distance of **M** points in 3 dimensions
    - Input data is M x 3 array
    - Output is M x M array containing the distance between points i
      and j
	- There is a temporary 1000 x 1000 x 3 array

```{.python emphasize=2:17-2:44}
X = numpy.random.random((1000, 3))
D = numpy.sqrt(((X[:, numpy.newaxis, :] - X) ** 2).sum(axis=-1))
```



# Summary

- NumPy arrays consist internally of contiguous data block and strides
  to describe dimensions and shape
- Vectorization improves performance
- Arrays can be broadcasted into same shapes
- Expression evaluation can lead into temporary arrays
