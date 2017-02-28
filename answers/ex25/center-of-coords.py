from multiprocessing import Process, Queue
from Queue import Empty
from pdb import PDB
from numpy import array, zeros

def average(q, r, size):
    while True:
        try:
            chunk = q.get(timeout=1)
        except Empty:
            break
        avg = sum(chunk) / size
        r.put(avg)

q = Queue()
r = Queue()

pdb = PDB('5ire.pdb')
n = 100

i = n
while i < len(pdb):
    q.put(pdb.coordinates[i-n:i].copy())
    i += n

p = [Process(target=average, args=(q, r, n)) for x in range(10)]
for i in range(10):
    p[i].start()
for i in range(10):
    p[i].join()

todo = len(pdb) % n
extra = pdb.coordinates[-1*todo:].copy()
extra = sum(extra)

results = []
while not r.empty():
    avg = r.get()
    results.append(avg)
results = array(results) * n

origo = ( sum(results) + extra ) / len(pdb)

print origo

