def fibonacci(n):
    """
    Fibonacci n.

    Args:
        n: (int): write your description
    """
    if n < 2:
        return n
    return fibonacci(n-2) + fibonacci(n-1)
