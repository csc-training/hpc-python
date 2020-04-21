<!-- Title: Communicators -->

<!-- Short description:

In this article we discuss MPI communicators in more detail and show how to
create user-defined communicators.

-->


# Communicators

In MPI context, a *communicator* is a special object representing a group of
processes that participate in communication. When a MPI routine is called, the
communication will involve some or all of the processes in a communicator.

In C and Fortran, all MPI routines expect a communicator as one of the
arguments. In Python, most MPI routines are implemented as methods of a
communicator object.

A single process can belong to multiple communicators and will have an
*unique* ID (rank) in each of the communicators.

![](../../img/communicator.svg)


## User-defined communicators

All processes start in a global communicator called `MPI_COMM_WORLD` (or
`MPI.COMM_WORLD` in mpi4py), but the user can also define their own custom
communicators as needed.

- By default a single, universal communicator exists to which all
  processes belong (`MPI.COMM_WORLD`)

A new communicator is created as a collective operation of an existing
communicator. For example, to split the processes in a communicator into
smaller sub-groups, one could do the following:

~~~python
comm = MPI.COMM_WORLD
rank = comm.Get_rank()

color = rank % 4

local_comm = comm.Split(color)
local_rank = local_comm.Get_rank()

print("Global rank: %d Local rank: %d" % (rank, local_rank))
~~~

A distinct label (called `color`, which is actually just an integer number
between 0-3) is assigned to each process based on its rank in the original
communicator. New communicators are then created based on this value, so that
all processes with the same "color" end up in the same communicator.

If effect, this splits the processes in the original communicator into 4
sub-groups that each share a new communicator within the sub-group.
