# Introduction and performance analysis

## Welcome to the course

1. Welcome to Python in High Performance Computing (video)
2. [Prerequisities and structure of the course](python-and-performance/prerequisities.md)
3. How well do you know Python? (quiz)
4. [Setting up the programming environment](python-and-performance/setting-environment.md)

## Performance challenges in Python

5. Outline of Python performance issues (video)
6. [Why are Python programs slow?](python-and-performance/performance-bottlenecks.md)
7. Experiences about performance of Python programs (discussion)

## Performance analysis

8. [Where program spends time?](python-and-performance/performance-analysis.md)
9. [Using applications own timers](python-and-performance/using-own-timers.md)
10. [Measuring small code snippets with timeit](python-and-performance/using-timeit.md)
11. Using cProfile (video)
12. [Introducing heat equation](python-and-performance/heat-equation.md)
13. [Hands-on: Performance analysis of heat equation solver](../../performance/cprofile/)
14. Pros and cons of various performance analysis approaches (discussion)

## Revision

15. [Week 1 summary](python-and-performance/summary.md)


# Numerical computing

## Using NumPy

1. Welcome to week 2 (video)
2. Differences between Python lists and NumPy arrays (video)
3. [Creating and accessing NumPy arrays](numerical-computing/creating-and-accessing.md)
4. [Hands-on: Array creation](../../numpy/array-creation/)
5. [Hands-on: Array slicing](../../numpy/array-slicing/)

## Operating with NumPy arrays

6. [Arithmetics and elementary functions](numerical-computing/simple-operations.md)
7. [Vectorised operations](numerical-computing/vectorised-operations.md)
8. [Hands-on: Finite difference](../../numpy/finite-difference/)
9. [Hands-on: Numerical integration](../../numpy/integration/)
10. [Broadcasting](numerical-computing/broadcasting.md)
11. [Hands-on: Split and combine arrays](../../numpy/split-combine/)
12. [Hands-on: Translation with broadcasting](../../numpy/broadcast-translation/)
13. Avoiding explicit loops with NumPy arrays (discussion)

## NumPy tools

14. [File I/O](numerical-computing/file-io.md)
15. [Hands-on: Input and output](../../numpy/input-output/)
16. [Random numbers](numerical-computing/random-numbers.md)
17. [Hands-on: Random numbers](../../numpy/random-numbers/)
18. [Linear algebra and polynomials](numerical-computing/linear-algebra.md)
19. [Hands-on: Linear algebra](../../numpy/linear-algebra/)

## Deeper view into NumPy

20. [Anatomy of NumPy arrays](numerical-computing/anatomy-of-ndarray.md)
21. [Temporary arrays](numerical-computing/temporary-arrays.md)
22. [Hands-on: Temporary arrays](../../numpy/temporary-arrays/)
23. [Speeding up complex expressions with Numexpr](numerical-computing/numexpr.md)
24. [Hands-on: Numexpr](../../numpy/numexpr/)

## Revision

25. [Week 2 summary](numerical-computing/summary.md)
26. Limitations of NumPy (discussion)


# Using compiled code and libraries

## Using Cython

## Interfacing with external libraries

## Revision


# Parallel programming

## Introduction to parallel programming

1. Welcome to week 4 (video)
2. [Parallel programming concepts](parallel-programming/concepts.md)
3. Processes and threads (video)

## Message passing with Python

4. [Introduction to MPI](parallel-programming/intro-to-mpi.md)
5. Execution and data model in MPI (video)
6. [Case study: Parallel sum](parallel-programming/parallel-sum.md)
7. [Hands-on: Hello world](../../mpi/hello-world/)

## Point-to-point communication

8. [MPI communication](parallel-programming/send-receive.md)
9. [Fast communication of large arrays](parallel-programming/send-receive-array.md)
10. [Hands-on: Message exchange](../../mpi/message-exchange/)
11. [Hands-on: Message chain](../../mpi/message-chain/)
12. [Non-blocking communication](parallel-programming/non-blocking.md)
13. [Hands-on: Non-blocking communication](../../mpi/non-blocking/)
14. [Communicators](parallel-programming/communicators.md)
15. Communication modes (discussion)

## Collective communication

16. [Collective communication: one to many](parallel-programming/collectives-1-to-n.md)
17. [Collective communication: many to one](parallel-programming/collectives-n-to-1.md)
18. [Collective communication: many to many](parallel-programming/collectives-n-to-n.md)
19. Do you understand collective communication? (quiz)
20. [Hands-on: Collective operations](../../mpi/collectives/)

## Revision

21. [Week 4 summary](parallel-programming/summary.md)
22. [Bonus hands-on: Parallel heat equation solver](../../mpi/heat-equation/)

