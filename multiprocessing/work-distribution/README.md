## Work distribution

Read the atom coordinates of the Zika virus [5ire.pdb](5ire.pdb) using the
simple parser provided in [pdb.py](pdb.py) (see comments in the file for
examples on how to use it). In [center-of-coords.py](center-of-coords.py) is a
skeleton code you may also use as a starting point.

Calculate the center of coordinates in parallel by dividing the coordinates
in smaller chunks (e.g. 100 coordinates) to separate tasks. After completing
the tasks in worker processes, combine the results in the master process.

If needed, figure out also how to deal with any coordinates left out of the
neat uniform-sized chunks.

a) Use a **Pool of Workers** to distribute the tasks to worker processes.
   *Hint: if you return also the weight of each chunk, you can process also
   non-uniform sized chunks.*

OR

b) Use a **Queue** to distribute the tasks to worker processes. Store the
   results for each chunk in a separate queue.
