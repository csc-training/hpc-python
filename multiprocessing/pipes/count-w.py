# SPDX-FileCopyrightText: 2019 CSC - IT Center for Science Ltd. <www.csc.fi>
#
# SPDX-License-Identifier: MIT

from multiprocessing import Process, Pipe
from fasta import Fasta

def count(pipe, letter):
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

