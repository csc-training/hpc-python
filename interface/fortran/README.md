## Interfacing with Fortran

The file [evolve.f90](evolve.f90) contain a pure Fortran implementation of the
single time step in heat equation. Use **f2py** for creating Python interface,
and utilize the Fortran implementation in (heat_simple.py)[heat_simple.py] .
You may need to insert `f2py` attributes into the Fortran file.

