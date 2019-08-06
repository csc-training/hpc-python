<!-- Title: Random numbers -->

<!-- Short description:

In this article we show how to generate NumPy arrays with random numbers.

-->

# Random numbers

NumPy provides a wide range of functions to generate random numbers in arrays.
These functions are available in the **numpy.random** module.

The random numbers are generated using the same, excellent pseudo-random
number generator called Mersenne Twister that is also used in the normal
**random** module. Mersenne Twister has a period of 2^19937-1 and is generally
regarded as a very good pseudo-random number generator (for non-cryptographic
purposes).

Several functions for constructing random arrays are provided, including:

  - random: uniform random numbers
  - normal: normal distribution
  - choice: random sample from given array

~~~python
a = numpy.random.random((2,2))

print(a)
# output:
#   [[ 0.02909142  0.90848 ]
#    [ 0.9471314   0.31424393]]

b = numpy.random.choice(numpy.arange(4), 10)

print(b)
# output: [0 1 1 2 1 1 2 0 2 3]
~~~
