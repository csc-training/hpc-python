<!-- Title: Interfacing Fortran code -->

<!-- Short description:

In this article we discuss how external code written in Fortran can be
utilized with the f2py tool.

-->

# Interfacing Fortran code

Fortran is still a widely used programming language in scientific computing
and it is actually well suited for numerically intensive applications.
Utilising Fortran code from Python is one plausible way of speeding up Python
applications.

Modern Fortran (since Fortran 2003) supports interoperability with C in a
standard way, and one possible way to use Fortran code from Python is to
provide a C interface in Fortran and then use CFFI or Cython. If one does not
want to work on the Fortran code, it is possible to create a Python
interface to Fortran also with the **f2py** tool.

The **f2py** is part of NumPy, and it is normally provided both as a command
line tool as well as a Python module. We discuss here the command line tool.

Assume we have the following Fortran code that adds together two arrays
(`c = a + b`):

~~~fortran
subroutine add(a, b, c, n)

  implicit none

  ! f2py understands only limited number of kind parameters
  real(kind=8), intent(in) :: a(n)
  real(kind=8), intent(in) :: b(n)
  real(kind=8), intent(out) :: c(n)
  integer :: n

  c = a + b

end subroutine
~~~

We can create a Python interface to this subroutine as follows:

~~~bash
$ f2py3 -c add.f90 -m fortran_module
~~~

The **-c** flag instructs f2py to compile and build a Python extension module
from file `add.f90`, and the name of the this module is designated with the
**-m** flag. We can now import the module, and use the functions from Python:

~~~python
import numpy as np
from fortran module import add

x = np.arange(10.)
y = np.arange(0.1, 10.1)
z = add(x, y)
~~~

As the arguments to the Fortran function were arrays, *f2py* generated
an interface that automatically does the conversion between a NumPy array and
a Fortran array. Also, the size argument `n` is automatically constructed from
the size of the arrays. As the argument `c` in the Fortran code had the
`intent(out)` attribute (meaning it is used only for output), the Python
interface treats it as a return value.

More complex examples on how to use f2py can be found in the
[f2py user guide](https://docs.scipy.org/doc/numpy/f2py/).
