from .species import Species
from ..quantities import *


class C2H6(Species):
    def __init__(self, T=None):
        self.mol_weight = 30.07
        self.c_atoms = 2
        self.h_atoms = 6
        super().__init__(T)
