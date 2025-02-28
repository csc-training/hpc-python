# SPDX-FileCopyrightText: 2019 CSC - IT Center for Science Ltd. <www.csc.fi>
#
# SPDX-License-Identifier: MIT

from multiprocessing import Process, Manager

def f(x):
    x['Apple'] = 0.70
    x['Orange'] = 1.20

manager = Manager()
fruits = manager.dict()

p = Process(target=f, args=[fruits])
p.start()
p.join()

print(fruits)

