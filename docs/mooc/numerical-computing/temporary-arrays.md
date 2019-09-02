<!-- Title: Temporary arrays -->

<!-- Short description:

In this article we show how NumPy uses temporary arrays to evaluate
expressions.

-->


# Temporary arrays

In complex expressions, NumPy stores intermediate values in temporary arrays.
This means that the memory consumption can be higher than expected. Consider
e.g. the following example:

~~~python
import numpy
a = numpy.random.random((1024, 1024, 50))
b = numpy.random.random((1024, 1024, 50))

c = 2.0 * a - 4.5 * b
~~~

In order to calculate the last line, two temporary arrays will be created to
store the intermediate results (`2.0 * a` and `4.5 * b`). If the arrays are
very large, it is easy to see this leading to unexpected out-of-memory errors
for the unwary.

Luckily, NumPy is smart enough to reuse temporary arrays when possible. Thus,
even if we have additional terms in the addition, only two temporary arrays
are needed:

~~~python
c = 2.0 * a - 4.5 * b + numpy.sin(a) + numpy.cos(b)
~~~

Now, if one adds some (unnecessary) parenthesis, the situation changes and
*three* temporary arrays are needed:

~~~python
c = 2.0 * a - 4.5 * b + (numpy.sin(a) + numpy.cos(b))
~~~

To alleviate for this, we could either remove the unnecessary parenthesis or
we could move the parenthesis to be first term in the addition, which would
allow for better reuse of the temporary arrays:

~~~python
c = (numpy.sin(a) + numpy.cos(b)) + 2.0 * a - 4.5 * b
~~~

Sometimes it is hard to see how many temporary arrays are needed, but if one
wants to conserve memory (when working with very, very large arrays), it is
usually a good idea to apply operations on an existing array one by one:

~~~python
c = 2.0 * a
c -= 4.5 * b
c += np.sin(a)
c += np.cos(b)
~~~

### Broadcasting and temporary arrays

Broadcasting approaches can also lead to unexpected temporary arrays. For
example, let us consider the calculation of the pairwise distance of **M**
points in three dimensions.

Input data is a M x 3 array and output is a M x M array containing the
distances between points i and j.

~~~python
X = np.random.random((1000, 3))
D = np.sqrt(((X[:, np.newaxis, :] - X) ** 2).sum(axis=-1))
#            ^^^^^^^^^^^^^^^^^^^^^^^^^
#           temporary 1000x1000x3 array
~~~
