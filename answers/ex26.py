from multiprocessing import Process, Pool
from Queue import Empty
from pdb import PDB
from numpy import array, zeros

def average(chunk):
    return sum(chunk) / len(chunk)

pool = Pool(10)

pdb = PDB('5ire.pdb')
n = 100

i = n
results = []
while i < len(pdb):
    chunk = pdb.coordinates[i-n:i].copy()
    i += n
    res = pool.apply_async(average, (chunk,))
    results.append(res)

todo = len(pdb) % n
extra = pdb.coordinates[-1*todo:].copy()
extra = sum(extra)

pool.close()
pool.join()

averages = []
for res in results:
    avg = res.get()
    averages.append(avg)
averages = array(averages) * n

origo = ( sum(averages) + extra ) / len(pdb)

print origo

