# Case study: parallel sum

How can a problem be split into smaller pieces that can be executed in
parallel? How to do it efficiently? These are the key questions when
designing a parallel algorithm.

Designing a good strategy for work distribution is usually the most essential
part of writing a parallel program. Common approaches utilise either data
parallelism or task parallelism. In *data parallelism* one distributes a
(large) dataset to multiple processors and then the processors operate on
separate pieces of the data in parallel. In *task parallelism* one breaks down
the algorithm into smaller tasks that are then distributed and executed in
parallel.

Let us now look into an example implementation of a parallel algorithm for
calculating the sum of all values in an array.

## Initial state

Assume we have an array A that contains a large number of floating point
numbers. The values have been read from a file by the first MPI task (rank 0).

## Goal

Calculate the total sum of all elements in array A in parallel.

## Parallel algorithm

Our parallel algorithm consist of three main steps: 1) distribute the data,
2) compute local sums, and 3) gather and combine the partial results. Steps 1
and 3 can be further broken down into sub-steps to better illustrate the MPI
communication needed.

1. Scatter the data
  1. receive operation in scatter
  2. send operation in scatter
2. Compute partial sums in parallel
3. Reduce partial sums
  1. Partial sum on P1 sent to P0
- Step 3.1: Receive operation in reduction
- Step 3.2: send operation in reduction
- Step 3.3: compute final answer
  2. P0 sums the partial sums

FIXME: missing figure


### Step 1.1: Receive operation for scatter

P1 posts a receive to receive half of the array from P0

FIXME: missing figure

### Step 1.2: Send operation for scatter

P0 posts a send to send the lower part of the array to P1

FIXME: missing figure

### Step 2: Compute the partial sums in parallel

P0 & P1 computes their parallel sums and store them locally

FIXME: missing figure

### Step 3.1: Receive operation for reduction

P0 posts a receive to receive partial sum

FIXME: missing figure

### Step 3.2: Send operation for reduction

P1 posts a send with partial sum

FIXME: missing figure

### Step 3.3: Combine the partial sums

P0 sums the partial sums

FIXME: missing figure
