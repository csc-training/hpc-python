from distutils.core import setup, Extension
import numpy as np

setup(
     ext_modules=[Extension('example',
                            sources=['example.c'],
                            include_dirs=[np.get_include()]
                           ),
                 ]
)

