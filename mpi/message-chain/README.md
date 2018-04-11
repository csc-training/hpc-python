## Message chain

Write a simple program where every MPI task sends data to the next one. Let
**ntasks** be the number of the tasks, and **myid** the rank of the current
task. Your program should work as follows:

- Every task with a rank less than ntasks-1 sends a message to task myid+1.
  For example, task 0 sends a message to task 1.
- The message content is an integer array where each element is initialized to
  myid.
- The sender prints out the number of elements it sends.
- All tasks with rank ≥ 1 receive messages.
- Each receiver prints out their myid, and the first element in the received
  array.

1. Implement the program described above using `Send` and `Recv`.
2. Use `Sendrecv` instead of `Send` and `Recv` when sending and receiving.
3. Can the code be simplified using `MPI.PROC_NULL`?

