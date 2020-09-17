<!-- Title: Broadcasting -->

<!-- Short description:

In this article we show how to work with arrays that have different, but
compatible, shapes.

-->


# Array manipulation

When working with NumPy arrays it is sometimes necessary to manipulate the
shape and/or size of them. One can for example modify the shape of an array as
well as split or join arrays into new arrays. Let us look into three array
manipulations:

  - reshape an array
  - join two or more arrays
  - split an array

## Reshape

Even though the number of elements in a NumPy array is fixed, the shape of the
array is not. One is free to change the shape as long as the number of
elements stays the same. For example, one can reshape a 2x3 array into a 3x2
array:

~~~python
a = numpy.array([[1, 2, 3], [4, 5, 6]])

print(a.shape)
# output: (2,3)

a.shape = (3,2)

print(a)
# output: [[1 2],
#          [3 4],
#          [5 6]]
~~~

Similar result can also be achieved by using the **reshape()** method of an
array, which will return a *new array* in the desired shape:

~~~python
a = numpy.array([[1, 2, 3], [4, 5, 6]])
b = a.reshape(3,2)

print(a)
# output: [[1 2 3],
#          [4 5 6]]

print(b)
# output: [[1 2],
#          [3 4],
#          [5 6]]
~~~

There is also a special, short-hand method called **ravel()** to flatten an
array into 1D:

~~~python
c = a.ravel()

print(c)
# output: [1 2 3 4 5 6]
~~~

The same effect could of course be achieved by using `a.reshape(a.size)`.


## Concatenate

If one has multiple NumPy arrays, one can join them together using the
**concatenate()** function as long as they have the same shape expect in the
dimension along which they will be joined.

For example, two 2x3 arrays can be combined into a new 4x3 array:

~~~python
a = numpy.array([[1, 2, 3], [4, 5, 6]])
b = numpy.array([[7, 8, 9], [10, 11, 12]])
c = numpy.concatenate((a, b))

print(c)
# output: [[ 1  2  3],
           [ 4  5  6],
           [ 7  8  9],
           [10 11 12]]
~~~

One can also specify the axis (dimension) along which the arrays will be
joined:

~~~python
d = numpy.concatenate((a, b), axis=1)

print(d)
# output: [[ 1  2  3  7  8  9],
           [ 4  5  6 10 11 12]]
~~~

## Split

A NumPy array can also be split into multiple, equally-sized smaller arrays by
using the **split()** function. The only requirement is that the split needs
to be an equal division, i.e. the resulting arrays need to have the same
shape.

For example, a 2x3 can be split either into two 1x3 arrays or three 2x1
arrays:

~~~python
a = numpy.array([[1, 2, 3], [4, 5, 6]])
x = numpy.split(a, 2)
y = numpy.split(a, 3, axis=1)

print(x)
# output: [array([[1, 2, 3]]), array([[4, 5, 6]])]

print(y)
# output: [array([[1], [4]]), array([[2], [5]]), array([[3], [6]])]
~~~

If one tries to do an unequal split (e.g. `numpy.split(a, 2, axis=1)` in the
example above) an error will be raised.


# Broadcasting

As was discussed earlier, mathematical (and logical) operations are applied
element-wise with NumPy arrays. For this to work, when applying an operation
involving two arrays, requires that the two arrays have the same shape. For
example `a + b` would do an addition of each element in `a` with the
corresponding element in `b` and would result in a new array that has the same
shape as `a` and `b`.

Now, let us consider what happens if the two arrays *do not have the same
shape*. If the shapes of the arrays are completely different in all
dimensions, there is nothing to be done and the operation will fail. But, if
the shapes are the same in one (or more) dimensions it is possible that NumPy
is able to do what is called *broadcasting*.

Simplest example of broadcasting is when one e.g. multiplies an array with a
scalar value:

~~~python
a = numpy.arange(4)
print(a * 2)
# output: [0 2 4 6]
~~~

The scalar value is broadcasted to the array, i.e. it is used in the operation
for all the elements. Conceptually, one can think of there being another array
filled with the scalar value, even though NumPy is smart enough not to make
an actual array or even to do any extra memory copies.

### Compatibility rules

The exact rules for when two arrays are compatible enough to broadcast are
quite simple, but in practice quite hard to follow. Dimensions of the two
arrays are compared (starting from the trailing dimensions) and are deemed
compatible if either one of them is 1 or if they are equal.

The complexity starts to creep in with the fact that two arrays can also have
different number of dimensions. Also, if one of the dimensions is 1, the array
is "copied" in that dimension to match the other array.

Examples of how the dimensions of arrays are matched when broadcasting
**successfully**:

~~~
    a: 8 x 3
    b:     3
a * b: 8 x 3

    a: 3 x 2
    b: 1 x 2
a * b: 3 x 2

    a: 4 x 1 x 6 x 1
    b:     5 x 1 x 3
a * b: 4 x 5 x 6 x 3
~~~

Examples of **failed** broadcasting due to mismatch(es) in the dimensions:

~~~
    a: 8 x 3
    b:     2  # mismatch in the last dimension

    a: 3 x 2
    b: 2 x 2  # mismatch in the first dimension

    a: 4 x 2 x 6 x 1
    b:     5 x 1 x 3  # mismatch in the third from last dimension
~~~

It is very easy to make wrong assumptions intuitively, so careful
consideration is always needed when broadcasting.


### Examples

Operations are applied element-wise following the above rules with
broadcasting happening in each dimension that is either 1 or non-existing.

Example: A 3x2 array multiplied by a 1x2 array:

~~~python
a = numpy.arange(6).reshape(3,2)
b = numpy.array([7,11], float).reshape(1,2)

print(a)
# output: [[0 1],
#          [2 3],
#          [4 5]]

print(b)
# output: [[ 7.  11.]]

c = a * b

print(c)
# output: [[  0.  11.],
#          [ 14.  33.],
#          [ 28.  55.]]
~~~

Example: A 4x1x6 array multiplied by a 2x6 array:

~~~python
a = numpy.arange(4*6).reshape(4,1,6)
b = numpy.arange(2*6).reshape(2,6)

print(a)
# output: [[[ 0  1  2  3  4  5]]
#
#          [[ 6  7  8  9 10 11]]
#
#          [[12 13 14 15 16 17]]
#
#          [[18 19 20 21 22 23]]]

print(b)
# output: [[ 0  1  2  3  4  5]
#          [ 6  7  8  9 10 11]]

c = a * b

print(c)
# output: [[[  0   1   4   9  16  25],
#           [  0   7  16  27  40  55]],
#
#          [[  0   7  16  27  40  55],
#           [ 36  49  64  81 100 121]],
#
#          [[  0  13  28  45  64  85],
#           [ 72  91 112 135 160 187]],
#
#          [[  0  19  40  63  88 115],
#           [108 133 160 189 220 253]]]
~~~

Example: calculate distances to a fixed point (`origin`) from a list of
coordinates (`points`):

~~~python
points = numpy.random.random((100, 3))  # 100 coordinates in 3D
origin = numpy.array((1.0, 2.2, -2.2))  # fixed point

# calculate distances
distances = (points - origin)**2
distances = numpy.sqrt(numpy.sum(distances, axis=1))

# find the most distant point
i = numpy.argmax(distances)
print(points[i])
~~~
