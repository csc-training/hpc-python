<!-- Title: Arithmetics and elementary functions -->

<!-- Short description:

In this article we show how to do simple numerical operations with arrays.

-->

# Element-wise operations

Simple calculations are very straightforward with NumPy arrays. Basic
arithmetic operations (`+ - * / **`) can all be used with arrays. The main
thing to keep in mind is that most operations are done **element-wise**.

~~~python
a = numpy.array([1.0, 2.0, 3.0])
b = 2.0

print(a * b)
# output: [ 2.  4.  6.]

print(a + b)
# output: [ 3.  4.  5.]

print(a * a)
# output: [ 1.  4.  9.]
~~~

# Elementary functions

NumPy provides also a wide range of elementary mathematical functions (sin,
cos, exp, sqrt, log, ...) that work with arrays (as well as single values). In
many ways NumPy can be used as a drop-in replacement for the `math` module.

~~~python
import numpy, math
a = numpy.linspace(-math.pi, math.pi, 8)

print(a)
# output:
#   [-3.14159265 -2.24399475 -1.34639685 -0.44879895  0.44879895 1.34639685
#     2.24399475  3.14159265]

print(numpy.sin(a))
# output:
#   [ -1.22464680e-16  -7.81831482e-01  -9.74927912e-01  -4.33883739e-01
#      4.33883739e-01   9.74927912e-01   7.81831482e-01   1.22464680e-16]

print(math.sin(a))
Traceback (most recent call last):
  File "<stdin>", line 1, in ?
TypeError: only length-1 arrays can be converted to Python scalars
~~~
