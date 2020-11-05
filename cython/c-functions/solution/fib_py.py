from functools import lru_cache

def fibonacci(n):
    """
    Fibonacci n.

    Args:
        n: (int): write your description
    """
    if n < 2:
        return n
    return fibonacci(n-2) + fibonacci(n-1)

@lru_cache(maxsize=None)
def fibonacci_cached(n):
    """
    Return the number nibonacci number.

    Args:
        n: (int): write your description
    """
    if n < 2:
        return n
    return fibonacci_cached(n-2) + fibonacci_cached(n-1)
