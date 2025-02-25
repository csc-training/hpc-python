# SPDX-FileCopyrightText: 2019 CSC - IT Center for Science Ltd. <www.csc.fi>
#
# SPDX-License-Identifier: MIT

import numpy as np

mat = np.eye(6, k=1) + np.eye(6, k=-1)
print(mat)
