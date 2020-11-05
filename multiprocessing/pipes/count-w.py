from multiprocessing import Process, Pipe
from fasta import Fasta

def count(pipe, letter):
    """
    Count the number of letter

    Args:
        pipe: (todo): write your description
        letter: (todo): write your description
    """
    txt = pipe.recv()
    n = txt.count(letter)
    pipe.send(n)
    pipe.close()

left, right = Pipe()

p = Process(target=count, args=[right, 'W'])
p.start()

fasta = Fasta('5ire.fasta.txt')
chain = fasta['C']
left.send(chain)
n = left.recv()

print 'Chain C contains %d trypthophans' % n

