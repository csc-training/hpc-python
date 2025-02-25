# SPDX-FileCopyrightText: 2019 CSC - IT Center for Science Ltd. <www.csc.fi>
#
# SPDX-License-Identifier: MIT

from distutils.core import setup, Extension
import numpy as np

setup(
     ext_modules=[Extension('example',
                            sources=['example.c'],
                            include_dirs=[np.get_include()]
                           ),
                 ]
)

