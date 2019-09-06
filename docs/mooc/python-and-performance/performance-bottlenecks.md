<!-- Title: Why are Python programs slow? -->

<!-- Short description:

Why are Python programs sometimes slower than programs written in another
language? In this article Dr. Jussi Enkovaara discusses the main causes.

-->

# Why are Python programs slow?

Python is very flexible and dynamic language, but the flexibility comes with
a price.

Computer programs are nowadays practically always written in a high-level
human readable programming language and then translated to the actual machine
instructions that a processor understands. There are two main approaches for
this translation:

 - For **compiled** programming languages, the translation is done by
   a compiler before the execution of the program
 - For **interpreted** languages, the translation is done by an interpreter
   during the execution of the program

Compiled languages are typically more efficient, but the behaviour of
the program during runtime is more static than with interpreted languages.
The compilation step can also be time consuming, so the software cannot
always be tested as rapidly during development as with interpreted
languages.

Python is an interpreted language, and many features that make development
rapid with Python are a result of that, with the price of reduced performance
in some cases.

## Dynamic typing

Python is a very dynamic language. As variables get type only during the
runtime as values (Python objects) are assigned to them, it is more difficult
for the interpreter to optimize the execution (in comparison, a compiler can
make extensive analysis and optimization before the execution). Even though,
in recent years, there has been a lot of progress in just-in-time (JIT)
compilation techniques that allow programs to be optimized at runtime, the
inherent, very dynamic nature of the Python programming language remains one
of its main performance bottlenecks.

## Flexible data structures

The built-in data structures of Python, such as lists and dictionaries,
are very flexible, but they are also very generic, which makes them not so
well suited for extensive numerical computations. Actually, the implementation
of the data structures (e.g. in the standard CPython interpreter) is often
quite efficient when one needs to process different types of data. However,
when one is processing only a single type of data, for example only
floating point numbers, there is a lot of unnecessary overhead due to the
generic nature of these data structures.

## Multithreading

The performance of a single CPU core has stagnated over the last ten years,
and as such most of the speed-up in modern CPUs is coming from using multiple
CPU cores, i.e. parallel processing. Parallel processing is normally based
either on multiple threads or multiple processes. Unfortunately, the memory
management of the standard CPython interpreter is not thread-safe, and it uses
something called Global Interpreter Lock (GIL) to safeguard memory integrity.
In practice, this limits the benefits of multiple threads only to some
special situations (e.g. I/O). Fortunately, parallel processing with multiple
processes is relatively straightforward also with Python.

In summary, the flexibility and dynamic nature of Python, that enhances
the programmer productivity greatly, is also the main cause for the
performance problems. Flexibility comes with a price! Fortunately, as we
discuss in the course, many of the bottlenecks can be circumvented.
