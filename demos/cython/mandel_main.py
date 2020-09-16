import numpy as np
import matplotlib.pyplot as plt
import sys
from mandel import compute_mandel as compute_mandel_py
try:
    from mandel_cyt import compute_mandel as compute_mandel_cyt
except ImportError:
    pass

def plot_mandel(mandel):
    plt.imshow(mandel)
    plt.axis('off')
    plt.show()

def main(version='py'):
    kwargs = dict(cr=0.285, ci=0.01,
                  N=200,
                  bound=1.5)

    # choose pure Python or Cython version
    if version == 'py':
        print("Using pure Python")
        mandel_func = compute_mandel_py
    elif version == 'cyt': 
        print("Using Cython")
        try:
            mandel_func = compute_mandel_cyt
        except NameError as ex:
            raise RuntimeError("Cython extension missing") from ex
    else:
        raise RuntimeError("Unknown version")

    mandel_set, runtime = mandel_func(**kwargs)
    return mandel_set, runtime
    
if __name__ == '__main__':
    if len(sys.argv) == 2:
        mandel_set, runtime = main('cyt')
    else:
        mandel_set, runtime = main()
    print('Mandelbrot set generated in {0:5.2f} seconds'.format(runtime))
    plot_mandel(mandel_set)
    

