<!-- Title: Linear algebra and polynomials -->

<!-- Short description:

In this article we briefly introduce some of NumPy's linear algebra and
polynomial functionality.

-->

# Linear algebra

NumPy includes linear algebra routines that can be quite handy. For
example, NumPy can calculate matrix and vector products efficiently (`dot`,
`vdot`), solve eigenproblems (`linalg.eig`, `linalg.eigvals`), solve linear
systems (`linalg.solve`), and do matrix inversion (`linalg.inv`).

~~~python
A = numpy.array(((2, 1), (1, 3)))
B = numpy.array(((-2, 4.2), (4.2, 6)))

C = numpy.dot(A, B)
b = numpy.array((1, 2))

print(C)
# output:
#   [[  0.2  14.4]
#    [ 10.6  22.2]]

print(b)
# output: [1 2]

# solve C x = b
x = numpy.linalg.solve(C, b)

print(x)
# output: [ 0.04453441  0.06882591]
~~~

Normally, NumPy utilises high performance numerical libraries in linear
algebra operations. This means that the performance of NumPy is actually quite
good and not far e.g. from the performance of a pure-C implementations using
the same libraries.


# Polynomials

NumPy has also support for polynomials. One can for example do least square
fitting, find the roots of a polynomial, and evaluate a polynomial.

A polynomial *f(x)* is defined by an 1D array of coefficients (*p*) with
length *N*, such that $f(x) = p[0] x^{N-1} + p[1] x^{N-2} + ... + p[N-1]$.

~~~python
# f(x) = x^2 + random noise (between 0,1)
x = numpy.linspace(-4, 4, 7)
f = x**2 + numpy.random.random(x.shape)

p = numpy.polyfit(x, f, 2)

print(p)
# output: [ 0.96869003  -0.01157275  0.69352514]
#   f(x) =  p[0] * x^2 + p[1] * x  + p[2]
~~~
