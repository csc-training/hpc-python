from multiprocessing import Pool, Queue, Process
from pdb import PDB
from numpy import array

def average(chunk):
    '''Calculate the average of multiple coordinates. Returns a tuple of
       (average, weight) where
           average -- average coordinate
           weight  -- no. of coordinates averaged over'''
    return (sum(chunk) / len(chunk), len(chunk))

# TODO: if using Queue, write a new worker() function that processes tasks
#       from one queue and puts results in another

# TODO: setup a Pool of Workers or Queue(s)
pdb = PDB('5ire.pdb')
n = 100

# split into tasks
tasks = []
for i in range(0, len(pdb), n):
    chunk = pdb.coordinates[i:i+n].copy()
    tasks.append(chunk)

# TODO: process all tasks in parallel
for chunk in tasks:
    ...

# TODO: collect results from each task
averages = []
weights = [] # no. of coordinates in each chunk
...
averages = array(averages)
weights = array(weights, ndmin=2)

# calculate the center of coordinates
origo = sum(averages * weights.T) / len(pdb)
print origo

