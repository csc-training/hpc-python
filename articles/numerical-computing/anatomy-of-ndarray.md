<!-- Title: Anatomy of NumPy arrays -->

<!-- Short description:

In this article we look more deeply into the internals of NumPy arrays.

-->


# Anatomy of NumPy arrays

The datatype of a NumPy array is called **ndarray**. If one looks into what an
**ndarray** is actually made of, one can see that it consists of the following:
  - one dimensional contiguous block of memory: raw data
  - indexing scheme: how to locate an element
  - data type descriptor: how to interpret an element

FIXME: missing figure

## NumPy indexing

There are many possible ways of arranging the elements of a N-dimensional
array in a 1-dimensional block (i.e. memory). NumPy uses **striding** where a
N-dimensional index (n[0], n[1], ..., n[-1]) corresponds to the offset from
the beginning of a 1-dimensional block.

FIXME: missing figure


## Attributes of an ndarray

`a = np.array(...)`
  : `a.flags`
    : various information about memory layout

    `a.strides`
    : bytes to step in each dimension when traversing

    `a.itemsize`
    : size of one array element in bytes

    `a.data`
    : Python buffer object pointing to start of arrays data

    `a.__array_interface__`
    : Python internal interface
