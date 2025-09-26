from .species import Species
from ..quantities import *


class C4H10(Species):
    def __init__(self, T=None):
        self.mol_weight = 58.124
        self.c_atoms = 4
        self.h_atoms = 10
        super().__init__(T)
