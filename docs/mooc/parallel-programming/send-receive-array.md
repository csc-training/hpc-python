<!-- Title: Fast communication of large arrays -->

<!-- Short description:

In this article we discuss how to send and receive NumPy arrays using MPI.

-->


# Fast communication of large arrays

MPI for Python offers very convenient and flexible routines for sending and
receiving general Python objects. Unfortunately, this flexibility comes with
a cost in performance. In practice, what happens under the hood is that Python
objects are converted to byte streams (pickled) when sending and back to
Python objects (unpickled) when receiving. These conversions may add a
serious overhead to communication.

Good news is that MPI for Python offers alternative routines for sending
and receiving contiguous memory buffers (such as NumPy arrays) with very
little overhead. To distinguish between the two types of routines, the names
of the flexible, all-purpose routines are all in lower case whereas the names
of the fast, contiguous memory specific routines always start with an upper
case letter.

When using one of the upper case methods, the underlying MPI implementation
can simply copy memory blocks without any conversions. If the amount of data
to be communicated is large, this will give an enormous performance
improvement. It is therefore always advisable to use only the upper case
methods (apart from maybe some simple initialisation).


## Send/receive NumPy arrays

Sending and receiving a NumPy array efficiently is very straightforward. Since
MPI for Python knows NumPy arrays, it can automatically take care of most of
the details.

To send, one basically just needs to use the upper case method `Send()`
giving the NumPy array and destination rank as arguments:

~~~python
Send(data, dest)
~~~

To receive, one needs to first prepare a NumPy array to receive the data to
and then use the upper case method `Recv()` giving the array and source rank
as arguments:

~~~python
data = numpy.empty(shape, dtype)
Recv(data, source)
~~~

Note the difference between the upper/lower case methods on the receive side!
Upper case `Recv()` *does not* return the data, but instead copies it to an
existing array.

Example:

~~~python
from mpi4py import MPI
import numpy

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

data = numpy.empty(100, dtype=float)
if rank == 0:
    data[:] = numpy.arange(100, dtype=float)
    comm.Send(data, dest=1)
elif rank == 1:
    comm.Recv(data, source=0)
~~~


## Combined send and receive

MPI supports also of sending one message and receiving another with a single
call. This reduces the risk of deadlocks in many common situations.

For example, when doing a simple message exchange (i.e. two processes send
and receive a message to/from each other) one needs to be careful to have one
process first receive and the other send and then vice versa to avoid a
deadlock. With a combined send and receive, both processes can simply call a
single MPI call and be done with it.

The combined routine `Sendrecv()` is similar to the separate `Send()` and
`Recv()` routines. It basically just combines the two and the arguments
reflect this:

~~~python
buffer = numpy.empty(data.shape, dtype=data.dtype)
Sendrecv(data, dest=tgt, recvbuf=buffer, source=src)
~~~

The destination (`tgt`) and source (`src`) ranks can be the same or they can
be different. If no destination or source is desired (e.g. on boundaries) one
can use `MPI.PROC_NULL` to indicate no communication. Just like with the upper
case receive, the receive buffer (`buffer`) needs to exist before the call and
be sufficiently large to hold all the data to be received.


~~~python
data = numpy.arange(10, dtype=float) * (rank + 1)
buffer = numpy.empty(10, float)

if rank == 0:
    tgt, src = 1, 1
elif rank == 1:
    tgt, src = 0, 0

comm.Sendrecv(data, dest=tgt, recvbuf=buffer, source=src)
~~~


## Communicate any contiguous array

### MPI datatypes

MPI has a number of predefined datatypes to represent data, e.g. `MPI.INT` for
an integer and `MPI.DOUBLE` for a floating point number (in Python float is
double precision). If needed, one can also define custom datatypes, which can
be handy e.g. to use non-contiguous data buffers.

MPI has e.g. the following pre-defined datatypes available:

  - MPI.INT for an integer (`int`)
  - MPI.DOUBLE for a floating point number (`float`)
  - MPI.CHAR for a single character (`str`)
  - MPI.COMPLEX for a complex number (`complex`)

### Manual definition of a memory buffer

When communicating a Python object (lower case methods) or a NumPy array
(upper case methods), the datatype does not need to be specified. Objects are
serialised into byte streams and the datatype of a NumPy array is
automatically detected. If you have another type of contiguous array (i.e. an
object referring to a contiguous memory space containing multiple elements of
a single datatype), you have to do it manually instead.

The data buffer argument for the upper case methods is actually expected to
yield three pieces of information:

  - location in memory
  - number of elements
  - datatype of the elements

These can be automatically obtained from a NumPy array, but now we need to
define them manually as a list of three items: `[buffer, count, datatype]`.

For example, assuming `data` contains an array of 100 integers, we could send
it like this:

~~~python
comm.Send([data, 100, MPI.INT], dest=tgt)
~~~

If one is working with simple contiguous arrays, the number of elements in an
array can also be inferred from the byte size of the buffer (`data`) and the
byte size of the datatype. Thus, for such cases one can optionally also use a
shorter syntax: `[buffer, datatype]`. Since the number of elements is usually
trivially known, it is a good idea to simply stick with the 3-element syntax.

An example of sending and receiving a manually defined memory buffer (using a
NumPy array for the buffer just for simplicity):

~~~python
from mpi4py import MPI
import numpy

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

data = numpy.empty(100, dtype=float)
if rank == 0:
    data[:] = numpy.arange(100, dtype=float)
    comm.Send([data, 100, MPI.DOUBLE], dest=1)
elif rank == 1:
    comm.Recv([data, 100, MPI.DOUBLE], source=0)
~~~
