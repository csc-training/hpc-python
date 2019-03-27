<!-- Title: Using static typing -->

!-- Short description:

In this article we describe how giving away dynamic typing of variables
can increase the performance of the program.

-->

Python is both strongly typed and dynamically typed language. Strong typing
means that the variables do have a type, and the type matters when performing 
operations on a variable. Dynamic typic means that the type of the variable is 
determined only during the runtime.

Due to strong typing, types need to be compatible with respect to operand when 
performing operations. For example Python allows one to add an integer and a 
float, but adding an integer to a string produces error. Due to dynamic typing, 
in Python the same variable can have different type in different parts of the
execution. Dynamic typing can make the programming more flexible, but with a
price for the performance.

## Everything is an object

One of the key features of Python is that everything is an object, and the type
is just one attribute of the object. As an illustration, we can assign a single
integer to a variable, and use the Python built-in function `dir` for finding 
out the attributes of the object. If you execute the following two lines in the
interactive interpreter, it should becoma clear that Python integer is much more
complex than just a number. Please feel free to experiment also with other 
types!

~~~python
n = 5
dir(n)
~~~

The fact that everything is an object means that there is a lot of "unboxing" 
and "boxing" involved when Python performs operations with variables. For 
example, when just adding two integers

~~~python
a = 7
b = 6
c = a + b
~~~

there are several steps Python needs to make:

  1. Check the types of the both operands
  2. Check whether they both support **+** operation
  3. Extract the function that performs **+** operation (due to operator 
     overloading objects can have a custom definition for addition
  4. Extract the actual values of the objects
  5. Perform the **+** operation
  6. Construct a new integer object for the result

TODO: add figure about boxing/unboxing

Due to fact that Python is dynamically typed, the interpreter cannot know 
beforehand what type of objects one is dealing with, and everytime two variables
are added one needs to perform all the above steps.

## Adding static type information

What if one knows that e.g. in certain function the variables have always the
same type? That's where Cython steps in: Cython allows one to add static typing
information so that boxing and unboxing is not needed, and one can operate 
directly with the actual values.

When Cythonizing a Python code, static type information can be added either:

  - In function signatures by prefixing the formal arguments by their type
  - By declaring variables with the **cdef** Cython keyword, followed by the 
    the type

A simple Python function adding two objects could be Cythonized for example as
follows:

~~~python
def add (int x, int y):
    cdef int result
    result = x + y
    return result
~~~
The function works now only with integers but with less boxing/unboxing 
overheads.

The types provided in Cython code are C types, and the variables with type
information are pure C variables and not Python objects. When calling a 
Cythonized function from Python, there is an automatic conversion from the
Python object of actual arguments to the C value of formal argument, and when
returning a C variable it is converted to corresponding Python object. Automatic
conversions are carried out also in most cases within the Cython code where 
there both Python objects and C variables are involved. 

The table below lists the most common C types and their corresponding Python 
types. More information can be found in [Cython documentation](https://cython.readthedocs.io/en/latest/src/userguide/language_basics.html).

|  From Python types | To C types    |
| -------------------| --------------|
| int                | int, long     |
| int, float         | float, double |
| str/bytes          | char *        |


| From C types    |  To Python types |
| ----------------| -----------------|
| int, long       | int              |
| float, double   | float            |
| char *          | str/bytes        |


## Static typing in Mandelbrot kernel

Let's investigate possible speed up by introducing static typing to the 
**kernel** function in the **mandelbrot.pyx** module. Pure Python version was:

~~~python
def kernel(zr, zi, cr, ci, lim, cutoff):
    ''' Computes the number of iterations `n` such that 
        |z_n| > `lim`, where `z_n = z_{n-1}**2 + c`.
    '''
    count = 0
    while ((zr*zr + zi*zi) < (lim*lim)) and count < cutoff:
        zr, zi = zr * zr - zi * zi + cr, 2 * zr * zi + ci
        count += 1
    return count
~~~

and we can add type information both to the function signature and to the 
function body:

~~~python
def kernel(double zr, double zi, double cr, double ci, double lim, int cutoff):
    ''' Computes the number of iterations `n` such that 
        |z_n| > `lim`, where `z_n = z_{n-1}**2 + c`.
    '''
    cdef int count = 0
    while ((zr*zr + zi*zi) < (lim*lim)) and count < cutoff:
        zr, zi = zr * zr - zi * zi + cr, 2 * zr * zi + ci
        count += 1
    return count
~~~

When measuring now the performance, we obtain the following results:

  - Pure Python:  0.6 s
  - Static type declarations in the kernel: 20.2 ms

Thus, we obtained a speed up of ~30 !


