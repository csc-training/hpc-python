from multiprocessing import Pool, Queue, Process
from pdb import PDB
from numpy import array

def average(chunk):
    '''Calculate the average of multiple coordinates. Returns a tuple of
       (average, weight) where
           average -- average coordinate
           weight  -- no. of coordinates averaged over'''
    return (sum(chunk) / len(chunk), len(chunk))

def worker(q, r):
    '''Work through tasks in the queue, calculating the average coordinate
       and relative weight for each chunk of coordinates.
         q -- input queue containing arrays of coordinates
         r -- output queue for partial results'''
    while True:
        chunk = q.get()
        if chunk is None:
            break
        r.put(average(chunk))

size = 10
q = Queue()
r = Queue()
pdb = PDB('5ire.pdb')
n = 100

# split into tasks
tasks = []
for i in range(0, len(pdb), n):
    chunk = pdb.coordinates[i:i+n].copy()
    tasks.append(chunk)

# add tasks into the queue
for chunk in tasks:
    q.put(chunk)

# create parallel processes
p = []
for i in range(size):
    p.append(Process(target=worker, args=[q, r]))
    q.put(None)  # add sentinels to signal STOP
    p[i].start()

# wait for all tasks to finish
for i in range(size):
    p[i].join()

# collect results
averages = []
weights = []
while not r.empty():
    avg, w = r.get()
    averages.append(avg)
    weights.append(w)
averages = array(averages)
weights = array(weights, ndmin=2)

# calculate the center of coordinates
origo = sum(averages * weights.T) / len(pdb)
print(origo)

