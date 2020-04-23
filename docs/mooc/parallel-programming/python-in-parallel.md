<!-- Title: Parallel programming with Python -->

<!-- Short description:

In this article we give an overview of parallel programming approaches in the
Python ecosystem.

-->

Python has a rich ecosystem also for parallel computing, both standard
library and third party packages provide tools for different parallel
programming approaches.

In this course we focus on the message passing approach (with the **mpi4py**
package), that is normally the most appropriate solution for tightly
coupled parallel problems. In this article we review briefly some
other parallel programming packages available for Python, which can be
useful if the parallel problem is not communication intensive.

Python [standard library](https://docs.python.org/3/library/concurrency.html)
contains some modules that can be used for parallel programming for a
single shared memory computer, *i.e.* they are not suitable for
distributed computing. They are also mainly meant for launching
concurrent tasks with no (or moderate) dependencies and communication
needs between the tasks. The
[threading](https://docs.python.org/3/library/threading.html) module
provides a thread based approach, whereas
[multiprocessing](https://docs.python.org/3/library/multiprocessing.html)
is based on child processes. There is also a higher level
[concurrent.futures](https://docs.python.org/3/library/concurrent.futures.html)
module which can utilize either threads or processes. Using multiple
processes has a higher memory overhead, however, in the standard
CPython interpreter there is something called the Global Interpreter
Lock, which allows only one thread to execute Python code at once
(even though certain performance-oriented libraries might overcome
this limitation). Even though CPU-intensive tasks cannot execute in
parallel with threading, it can still be an appropriate model if you
want to run multiple I/O-bound tasks simultaneously.

For parallel data analytics that needs to scale over multiple
computers, one can utilize [Dask](https://dask.org/) or
[PySpark](https://spark.apache.org/docs/latest/api/python/pyspark.html)
third party packages. **Dask** is a Python library providing
advanced parallelism with easy to use interfaces (e.g. NumPy-like parallel
Dask array). **PySpark** is a Python interface to Apache Spark, a
general distributed cluster-computing framework for big data processing.

We will now move on to learn message passing with Python in more
detail, but please comment if you have experiences about these other
approaches!
