## Simple message exchange

### Communicating general Python objects

Write a simple program where two processes send and receive a message to/from
each other using `send` and `recv`. The message content is a dictionary 
`{‘rank’ : myrank}`  where `myrank` is the rank of the sending process.
After receiving a message, each process should print out the rank of the
process and the value in the received dictionary.

### Communicating NumPy arrays

In each process, construct a 100 000 element NumPy array which is initialized
to the rank of process. Send and receive the array using `Send` and `Recv` and
after receiving print out the rank of process together with the first element
of the received array. Investigate what happens when reordering the send and
receive calls in one of the processes.

