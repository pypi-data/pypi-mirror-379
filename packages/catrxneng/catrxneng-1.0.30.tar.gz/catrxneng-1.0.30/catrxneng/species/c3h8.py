from .species import Species
from ..quantities import *


class C3H8(Species):
    def __init__(self, T=None):
        self.mol_weight = 44.097
        self.c_atoms = 3
        self.h_atoms = 8
        super().__init__(T)
