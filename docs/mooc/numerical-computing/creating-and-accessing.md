<!-- Title: Creating and accessing NumPy arrays -->

<!-- Short description:

In this article we show how to create and access NumPy arrays.

-->

# Creating and accessing NumPy arrays

NumPy arrays have a fixed number of elements and all the elements have the
same datatype, both specified when creating the array. Even though the number
of elements is fixed, the shape of the array can be changed as long as the
number of elements remains the same.

## Creating arrays

### From existing data

NumPy arrays can be created in several different ways. The simplest way is
to use the **array** constructor and provide the data directly as an
argument. For example, in order to generate a one-dimensional array containing
the numbers 1,2,3,4 one can use:

~~~python
import numpy
x = numpy.array((1, 2, 3, 4))
~~~

This will generate a NumPy array containing four elements of integer type.

Unless explicitly specified, the datatype is automatically set based on the
values used to create the array. In this case they were all integers and thus
integer type was used. If the list would have contained one floating point
number (e.g. [1, 2, 3.1, 4]) then the array created would have used floating
point type for all elements.

The first argument of `array()` is the data for the array. It can be a single
list (or tuple), or a nested list of uniformly sized lists that mimics a
multi-dimensional array.

The second argument of `array()` is the datatype to be used for the array. It
can be one of the basic datatypes in Python (`int`, `float` etc.) or it can be
one of the more precise datatypes used internally by NumPy (`numpy.int8`,
`numpy.float128` etc.). If the second argument is not given, a datatype that
can represent all the input data is selected automatically.

~~~python
x = numpy.array((1, 2, 3, 4), float)

print(x)
# output: [ 1.  2.  3.  4.]


data = [[1, 2, 3], [4, 5, 6]]
y = numpy.array(data, complex)

print(y)
# output: [[ 1.+0.j  2.+0.j  3.+0.j]
#          [ 4.+0.j  5.+0.j  6.+0.j]]

print(y.shape)
# output: (2, 3)

print(y.size)
# output: 6
~~~

### Using helper functions

NumPy also provides quite a few handy helper functions that can be used to
generate the kinds of number sequences often used or to initialise the array
with in a given way.

Two extremely helpful functions for generating ranges of numbers are called
**arange** and **linspace**.

Similar to the regular `range()` function, `numpy.arange()` creates an array
containing evenly spaces values within a given interval.

~~~python
a = numpy.arange(10)

print(a)
# output: [0 1 2 3 4 5 6 7 8 9]
~~~

Optionally, one can also specify start and stop values (instead of just stop)
as well as a step between the values. It is also not limited to integers, but
can handle floating point numbers just as well.

Another common need is to generate a fixed number of evenly spaced values
within an interval, which is exactly what `numpy.linspace()` does.

~~~python
b = numpy.linspace(-4.5, 4.5, 5)

print(b)
# output: [-4.5  -2.25  0.    2.25  4.5]
~~~

One can also create an array of a given shape and initialise it to zeros, 
ones , or arbitrary value using the handy functions **zeros**,  **ones**, or 
**full**.

~~~python
c = numpy.zeros((4, 6), float)
d = numpy.ones((2, 4))
e = numpy.full((3, 2), 4.2)

print(c.shape)
print(d)
print(e)
# output:
#   (4, 6)
#   [[ 1.  1.  1.  1.]
#    [ 1.  1.  1.  1.]]
#   [[4.2 4.2]
#    [4.2 4.2]
#    [4.2 4.2]]
~~~

One can also create a truly empty array by using the function **empty**. This
will create an array and allocate memory for it, but not assign any values to
it. In practice, this means that the values of an empty array are unspecified
(whatever happened to be in the computer memory allocated to the array). Thus,
if one uses `empty`, it is crucial to always assign values to all the
elements before trying to use them.

Sometimes one would like to create an array with the same shape as an existing
array. In this case one can utilize the functions **zeros_like**, 
**ones_like**, **full_like** and **empty_like**:

~~~python
a = numpy.zeros((4, 6), float)
b = numpy.empty_like(a)
c = numpy.ones_like(a)
d = numpy.full_like(a, 9.1)
~~~

In addition to numbers, NumPy supports also storing non-numerical data, e.g.
strings. For strings, the largest element determines the item size, so in
practice arbitrary strings are not that suitable, but character arrays can be
sometimes useful.

~~~python
s = numpy.array(['foo', 'foo-bar'])

print(repr(s))
# output: array(['foo', 'foo-bar'],
#               dtype='|U7')

dna = 'AAAGTCTGAC'
c = numpy.array(dna, dtype='c')

print(repr(c))
# output:
#   array([b'A', b'A', b'A', b'G', b'T', b'C', b'T', b'G', b'A', b'C'],
#         dtype='|S1')
~~~


## Accessing arrays

NumPy arrays can be accessed in a similar way to normal Python lists. Only
key difference stems from the fact that NumPy arrays can be truly
multi-dimensional. This means that instead of a single index value, elements
in a NumPy array can have multiple index values (one for each dimension).

To access a single element in a 2D array, one should use the index value in
each dimension separated by a comma:

~~~python
data = numpy.array([[1, 2, 3], [4, 5, 6]])
x = data[0,2]
y = data[1,-2]

print(x, y)
# output: 3 5
~~~

Slicing syntax can also be used with NumPy arrays to select only some part of
the array.

~~~python
a = numpy.arange(10)

print(a[2:])
# output: [2 3 4 5 6 7 8 9]

print(a[:-1])
# output: [0 1 2 3 4 5 6 7 8]

print(a[1:7:2])
# output: [1 3 5]
~~~

Multi-dimensional arrays can be sliced, too, and in multiple dimensions as
well. One can also assign values to only some part of an array using the
slicing syntax.

~~~python
a = numpy.arange(10)
a[1:3] = -1

b = numpy.zeros((4, 4))
b[1:3, 1:3] = 2.0

print(a)
print(b)
# output:
#   [ 0 -1 -1  3  4  5  6  7  8  9]
#   [[ 0.  0.  0.  0.]
#    [ 0.  2.  2.  0.]
#    [ 0.  2.  2.  0.]
#    [ 0.  0.  0.  0.]]
~~~

### Views and copies of arrays

Simple assignment creates a new reference to an array, just like for any other
Python object. Thus, if you modify the array using the new reference, the
changes are visible also via any old reference to the same array.

To make a true copy of an array, one should use the `copy()` method:

~~~python
a = np.arange(10)
b = a              # reference, changing values in b changes a
b = a.copy()       # true copy
~~~

In contrast, slicing an array will create something called a *view* to the
array. It is like a window showing only a some part of the full array. Any
modifications to the elements in the view are directly reflected in the
original array. In fact, no real copy is made and as such any manipulation
will just change the original array.

Once again, to make a true copy, one should use the `copy()` method:

~~~python
a = np.arange(10)
c = a[1:4]         # view, changing c changes elements [1:4] of a
c = a[1:4].copy()  # true copy of subarray
~~~
