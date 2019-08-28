## Numerical integration

A simple method for evaluating integrals numerically is by the middle Riemann
sum

<!--- Equation
S = \sum_{i=1}^n f(x'_i) \Delta x
--->

![img](https://quicklatex.com/cache3/e2/ql_30419670e67bc2b3d039e8a9d8653de2_l3.png)

with

<!--- Equation
x'_i = (x_i + x_{i-1}) / 2
--->

![img](https://quicklatex.com/cache3/09/ql_f124fd5c831e873c6abd41160fae2d09_l3.png)

Calculate the integral in the interval [0,π/2] and investigate how much the
Riemann sum of **sin** differs from 1.0. Avoid `for` loops. Investigate also
how the results changes with the choice of Δx.
