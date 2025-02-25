# SPDX-FileCopyrightText: 2019 CSC - IT Center for Science Ltd. <www.csc.fi>
#
# SPDX-License-Identifier: MIT

import add
import numpy as np

a = np.random.random(10)
b = np.ones_like(a)
print(a)
add.add(a, b)
print(a)
