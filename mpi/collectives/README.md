## Collective operations

In this exercise we test different routines for collective communication. 

First, write a program where rank 0 sends an array containing numbers from 0
to 7 to all the other ranks using collective communication.

Next, we continue with four MPI tasks with following initial data vectors:

|        |    |    |    |    |    |    |    |    |
|--------|----|----|----|----|----|----|----|----|
|Task 0: |  0 |  1 |  2 |  3 |  4 |  5 |  6 |  7 |
|Task 1: |  8 |  9 | 10 | 11 | 12 | 13 | 14 | 15 |
|Task 2: | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
|Task 3: | 24 | 25 | 26 | 27 | 28 | 29 | 30 | 31 |

In addition, each task has a receive buffer for eight elements and the values
in the buffer are initialized to -1. Implement a program that sends and
receives values from the data vectors to receive buffers using a single
collective communication routine for each case, so that the receive buffers
will have the following values. You can start from the skeleton file
[skeleton.py](skeleton.py).

### Case 1

|        |    |    |    |    |    |    |    |    |
|--------|----|----|----|----|----|----|----|----|
|Task 0: |  0 |  1 | -1 | -1 | -1 | -1 | -1 | -1 |
|Task 1: |  2 |  3 | -1 | -1 | -1 | -1 | -1 | -1 |
|Task 2: |  4 |  5 | -1 | -1 | -1 | -1 | -1 | -1 |
|Task 3: |  6 |  7 | -1 | -1 | -1 | -1 | -1 | -1 |

### Case 2

|        |    |    |    |    |    |    |    |    |
|--------|----|----|----|----|----|----|----|----|
|Task 0: | -1 | -1 | -1 | -1 | -1 | -1 | -1 | -1 |
|Task 1: |  0 |  1 |  8 |  9 | 16 | 17 | 24 | 25 |
|Task 2: | -1 | -1 | -1 | -1 | -1 | -1 | -1 | -1 |
|Task 3: | -1 | -1 | -1 | -1 | -1 | -1 | -1 | -1 |

### Case 3

|        |    |    |    |    |    |    |    |    |
|--------|----|----|----|----|----|----|----|----|
|Task 0: |  8 | 10 | 12 | 14 | 16 | 18 | 20 | 22 |
|Task 1: | -1 | -1 | -1 | -1 | -1 | -1 | -1 | -1 |
|Task 2: | 40 | 42 | 44 | 46 | 48 | 50 | 52 | 54 |
|Task 3: | -1 | -1 | -1 | -1 | -1 | -1 | -1 | -1 |

Tip: create two communicators
