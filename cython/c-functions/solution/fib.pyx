# SPDX-FileCopyrightText: 2019 CSC - IT Center for Science Ltd. <www.csc.fi>
#
# SPDX-License-Identifier: MIT

cpdef int fibonacci(int n):
    if n < 2:
        return n
    return fibonacci(n-2) + fibonacci(n-1)

def fibonacci_py(n):
    if n < 2:
        return n
    return fibonacci_py(n-2) + fibonacci_py(n-1)
