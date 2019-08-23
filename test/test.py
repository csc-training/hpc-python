from importlib import import_module

fail = False
required_modules = ['numpy', 'mpi4py', 'matplotlib', 'cython', 'cffi']
for mod in required_modules:
    try:
        import_module(mod)
        print("{} available".format(mod))
    except ImportError:
        print("{} is not available".format(mod))
        fail = True

print()

if fail:
    print("Test set failed")
else:
    print('Test set passed')
