from ase.build import molecule
from gpaw import GPAW
import cProfile

atoms = molecule('C6H6')
atoms.center(3.5)

calc = GPAW(h=0.2, xc='PBE', txt='benzene.txt')

atoms.set_calculator(calc)
cProfile.run("atoms.get_potential_energy()", "gpaw.prof")

