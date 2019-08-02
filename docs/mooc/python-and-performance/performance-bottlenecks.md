# Why are Python programs slow?

Why are Python programs sometimes slower than programs written in another languages? In this article Dr. Jussi Enkovaara discusses the main causes.

## Performance bottlenecks

Computer programs are nowadays practically always written in high-level
human readable programming languages, and then translated to the machine
instructions that processor understands. There are two main approaches on how
this translation is done:

 - For **compiled** programming languages, the translation is done by
   the compiler before the execution of the program
 - For **interpreted** languages, the translation is done during the
   execution of the program

Compiled languages are typically more efficient, but the behaviour of
the program during the runtime is more static than with interpred languages.
The compilation step can also be time consuming, so the software cannot 
always be tested as rapidly during the development as with interpreted 
languages.

Python is interpreted language, and many features that make development
rapid with Python are result of that, with the price of reduced performance in
some cases.

Python is also very dynamic language. As variables get type only during the
runtime as values (Python objects) are assigned to them, it is more difficult
for the interpreter the optimize the execution (Compiler can make extensive
analysis and optimization before the execution). Even though there has been
in recent years much progress in Just-in-time (JIT) compilation technology
where programs can be optimized at runtime, the very dynamic inherent nature 
of the Python programming language is one of the main performance bottlenecks.

The built-in data structures of Python, such as lists and dictionaries
are very flexible, but they are also very generic which makes them not so
well suited for extensive numerical computations. The implementation of the
data structures is actually often quite efficient (e.g. in the standard
CPython interpreter) for the cases where one needs to process different
types of data, however, when one is processing only e.g. floating numbers,
there is lots overhead due to generic nature of these data structures.

The speed of single CPU cores has stagnated for last ten years, and much of
the speedup in modern CPUs is coming from using multiple CPU cores, i.e. 
parallel processing. Parallel processing is normally based either on multiple
threads or multiple processes. The memory management of standard CPython 
interpreter is not thread-safe, and there is a so called global interpreter
lock (GIL) which limits speedup from multithreading only to special cases 
(i.e. I/O). Fortunately, parallel processing with multiple process is 
relatively straightforward also with Python.

In summary, the flexibility and dynamic nature of Python, which enhance
the programmer productivity greatly, are also the main causes for the 
performance problems. Flexibility comes with a price! Fortunately, as we
discuss in the course, many of the bottlenecks can be circumveted.


