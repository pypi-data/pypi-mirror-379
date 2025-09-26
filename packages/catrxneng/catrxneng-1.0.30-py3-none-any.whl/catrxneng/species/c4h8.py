from .species import Species
from ..quantities import *


class C4H8(Species):
    def __init__(self, T=None):
        self.mol_weight = 56.108
        self.c_atoms = 4
        self.h_atoms = 8
        super().__init__(T)
