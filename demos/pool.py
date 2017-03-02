from multiprocessing import Pool

def f(x):
    return x**2

pool = Pool(8)

# Blocking execution (with a single process)
result = pool.apply(f, (4,))
print(result)

# Non-blocking execution "in the background"
result = pool.apply_async(f, (12,))
print(result.get(timeout=1))

