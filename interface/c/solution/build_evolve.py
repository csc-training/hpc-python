from cffi import FFI
ffibuilder = FFI()

ffibuilder.cdef("""
         void evolve(double *u, double *u_previous, int nx, int ny,
                     double a, double dt, double dx2, double dy2);
         """)


ffibuilder.set_source("_evolve",  # name of the output C extension
"""
         void evolve(double *u, double *u_previous, int nx, int ny,
                     double a, double dt, double dx2, double dy2);
""",
    sources=['evolve.c'],   
    extra_compile_args=['-O3'],
    library_dirs=['.'],
    # libraries=['evolve'],
)

if __name__ == "__main__":
    ffibuilder.compile(verbose=True)
