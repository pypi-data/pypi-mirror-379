from .species import Species
from ..quantities import *


class C3H6(Species):
    def __init__(self, T=None):
        self.mol_weight = 42.081
        self.c_atoms = 3
        self.h_atoms = 6
        super().__init__(T)
