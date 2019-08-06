<!-- Title: Collective communication: many to many -->

<!-- Short description:

In this article we discuss how to use collective communication to exchange
data between all the processes in a communicator.

-->


# Collective communication: many to many

Collective communication routines in MPI include also routines for global
communication between all the processes. Global collective communication is
extremely costly in terms of performance, so if possible one should avoid
using them. Nevertheless, in some situations they are exactly the correct
approach to implement an parallel algorithm.

Let us look next how to use collective communication to exchange data between
all the processes in a communicator, i.e. how to move data from
*many to many*.


## Allreduce
  : all processes receive the results of reduction

## Alltoall
  : each process sends and receives to/from each other

## Alltoallv
  : each process sends and receives different amount of data to/from
    each other


# Collective communication: common mistakes

Some common mistakes to avoid when using collectives include:

1. Using a collective operation within one branch of an if-else test based on
   the rank of the process

   ~~~python
   if rank == 0:
       comm.bcast(...)
   ~~~

   All processes in a communicator must call a collective routine!

2. Assuming that all processes making a collective call would complete at
   the same time.

   Even a collective operation such a barrier only ensures that a process
   holds until everyone reaches the call. With data movement call (scatter,
   bcast etc.) even this may not be true, since MPI only guarantees that the
   process will proceed only when it is *safe* to do so. MPI implementations
   can (and do!) use communication caches that may allow some of the processes
   to continue from a collective call *even before communication happens*.

3. Using the input buffer also as an output buffer.

   ~~~python
   comm.Scatter(a, a, MPI.SUM)
   ~~~

   Always use different memory locations (arrays) for input and output!
