<!-- Title: Vectorised operations -->

<!-- Short description:

In this article we show how to perform complex numerical operations without
loops.

-->

# Vectorised operations

For loops in Python are slow. If one needs to apply a mathematical operation
on multiple (consecutive) elements of an array, it is always better to use a
vectorised operation if possible.

In practice, a vectorised operation means reframing the code in a manner that
completely avoids a loop and instead uses e.g. slicing to apply the operation
on the whole array (slice) at one go.

For example, the following code for calculating the difference of neighbouring
elements in an array:

~~~python
# brute force using a for loop
arr = numpy.arange(1000)
dif = numpy.zeros(999, int)
for i in range(1, len(arr)):
    dif[i-1] = arr[i] - arr[i-1]
~~~

can be re-written as a vectorised operation:

~~~python
# vectorised operation
arr = numpy.arange(1000)
dif = arr[1:] - arr[:-1]
~~~

![](../../img/vectorised-difference.png)

The first brute force approach using a for loop is approx. 80 times slower
than the second vectorised form!
