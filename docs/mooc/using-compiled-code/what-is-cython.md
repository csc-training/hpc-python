<!-- Title: What is Cython? -->

!-- Short description:

What is Cython? In this article we give overview of Cython, the optimising
static compiler and extension language.

-->

Cython is optisiming static compiler for Python, and it provides also its own programming language which is a superset of standard Python. 

[Cython](https://cython.org/) is designed to provide C-like performance for a code that is mostly written in Python, by adding only a few C-like declarations to an existing Python code. As such, Cython provides the best of the both Python and C worlds: good programmer productivity of Python together with high performance of C. Especially for scientific programs performing lot of numerical computations, Cython can speed up the execution times more than an order of magnitude. Cython makes it also easy to interact with external C/C++ code.

Cython works by transferring existing Python/Cython code into C, which generally is not easily readable by humans. The resulting C-code calls functions from Python C application programming interface (API), and requires thus existing Python compiler and runtime system. The Cython generated code is compiled into a Python module. Normally, this module cannot be used as such, but it needs to be imported from Python program which utilizes the functionality implemented in Cython.

The main mechanism on how Cython speeds up Python programs is by adding static declarations for variables. Thus, programmer loses some of the dynamic nature of Python when working with Cython. This works best for fundamental data types (integers, floats, strings) and contiguous arrays (such as NumPy arrays), operations on lists and dictionaries do not normally benefit much from Cython.

In summary, Cython can alleviate the following Python performance bottlenecks discussed in Week 1:

 - Interpretation overhead
 - Unboxing / boxing Python objects
 - Overheads of Python control structures
 - Function call overheads
