from multiprocessing import Pool, Queue, Process
from pdb import PDB
from numpy import array

def average(chunk):
    '''Calculate the average of multiple coordinates. Returns a tuple of
       (average, weight) where
           average -- average coordinate
           weight  -- no. of coordinates averaged over'''
    return (sum(chunk) / len(chunk), len(chunk))

size = 10
pool = Pool(size)
pdb = PDB('5ire.pdb')
n = 100

# split into tasks
tasks = []
for i in range(0, len(pdb), n):
    chunk = pdb.coordinates[i:i+n]
    tasks.append(chunk)

# submit tasks to the pool
result = pool.map(average, tasks)

# wait for all tasks to finish
pool.close()
pool.join()

# collect results
averages = []
weights = []
for avg, w in result:
    averages.append(avg)
    weights.append(w)
averages = array(averages)
weights = array(weights, ndmin=2)

# calculate the center of coordinates
origo = sum(averages * weights.T) / len(pdb)
print(origo)

